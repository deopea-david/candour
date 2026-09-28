/*
 * twocopies.c — load two SQLite libraries into ONE process and open the same
 * database file through both. Candour / Haunts investigation, 2026-09-28.
 *
 * Usage: twocopies <libA.dylib> <libB.dylib> <workdir>
 *   Pass the same path twice for the CONTROL run (dlopen returns the same
 *   image, so both "copies" are one library).
 *
 * Tests (all single-threaded and deterministic unless stated):
 *   T1  rollback-journal mode: A holds RESERVED (BEGIN IMMEDIATE); can B also?
 *   T2  WAL mode: A holds the write lock; can B also?  If yes, both commit;
 *       then count rows and run PRAGMA integrity_check.
 *   T3  WAL mode: B stays open; A opens, writes, closes.  Is the -wal file
 *       deleted under B?  Then B writes; A writes; everything closes; a fresh
 *       process-independent check counts rows and runs integrity_check.
 *   T4  rollback mode, the documented close() case: B holds RESERVED; A opens,
 *       reads, closes.  Does a SEPARATE process (/usr/bin/sqlite3) now get
 *       a write lock it should not be able to get?
 *   T5  stress: two threads, one per copy, WAL, busy_timeout, N inserts each.
 *       Count rows and integrity_check afterwards.
 */
#include <dlfcn.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>
#include <TargetConditionals.h>
#include <signal.h>

typedef struct sqlite3 sqlite3;
typedef struct sqlite3_stmt sqlite3_stmt;

typedef struct {
  const char *name;
  void *h;
  int (*open_v2)(const char *, sqlite3 **, int, const char *);
  int (*close_v2)(sqlite3 *);
  int (*exec)(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
  int (*busy_timeout)(sqlite3 *, int);
  const char *(*errmsg)(sqlite3 *);
  const char *(*libversion)(void);
  const char *(*sourceid)(void);
  int (*prepare_v2)(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
  int (*step)(sqlite3_stmt *);
  const unsigned char *(*column_text)(sqlite3_stmt *, int);
  int (*finalize)(sqlite3_stmt *);
  int (*threadsafe)(void);
} Lib;

#define SQLITE_OK 0
#define SQLITE_ROW 100
#define OPEN_FLAGS (0x00000002 | 0x00000004 | 0x00010000) /* READWRITE|CREATE|FULLMUTEX */

static void *sym(void *h, const char *n) {
  void *p = dlsym(h, n);
  if (!p) { fprintf(stderr, "missing symbol %s: %s\n", n, dlerror()); exit(2); }
  return p;
}

static void load(Lib *L, const char *path, const char *name) {
  L->name = name;
  L->h = dlopen(path, RTLD_NOW | RTLD_LOCAL);
  if (!L->h) { fprintf(stderr, "dlopen %s: %s\n", path, dlerror()); exit(2); }
  L->open_v2 = sym(L->h, "sqlite3_open_v2");
  L->close_v2 = sym(L->h, "sqlite3_close_v2");
  L->exec = sym(L->h, "sqlite3_exec");
  L->busy_timeout = sym(L->h, "sqlite3_busy_timeout");
  L->errmsg = sym(L->h, "sqlite3_errmsg");
  L->libversion = sym(L->h, "sqlite3_libversion");
  L->sourceid = sym(L->h, "sqlite3_sourceid");
  L->prepare_v2 = sym(L->h, "sqlite3_prepare_v2");
  L->step = sym(L->h, "sqlite3_step");
  L->column_text = sym(L->h, "sqlite3_column_text");
  L->finalize = sym(L->h, "sqlite3_finalize");
  L->threadsafe = sym(L->h, "sqlite3_threadsafe");
}

static sqlite3 *xopen(Lib *L, const char *path) {
  sqlite3 *db = NULL;
  int rc = L->open_v2(path, &db, OPEN_FLAGS, NULL);
  if (rc != SQLITE_OK) { fprintf(stderr, "[%s] open rc=%d\n", L->name, rc); exit(3); }
  L->busy_timeout(db, 0);
  return db;
}

/* Run SQL, print rc and message, return rc. */
static int run(Lib *L, sqlite3 *db, const char *sql) {
  char *err = NULL;
  int rc = L->exec(db, sql, NULL, NULL, &err);
  printf("    [%s] %-58s -> rc=%d%s%s\n", L->name, sql, rc, err ? " " : "", err ? err : "");
  return rc;
}

/* Return first column of first row as a malloc'd string. */
static char *scalar(Lib *L, sqlite3 *db, const char *sql) {
  sqlite3_stmt *st = NULL;
  char *out = NULL;
  int rc = L->prepare_v2(db, sql, -1, &st, NULL);
  if (rc != SQLITE_OK) {
    size_t n = strlen(L->errmsg(db)) + 32;
    out = malloc(n); snprintf(out, n, "ERROR(prepare rc=%d: %s)", rc, L->errmsg(db));
    return out;
  }
  rc = L->step(st);
  if (rc == SQLITE_ROW) {
    const unsigned char *t = L->column_text(st, 0);
    out = strdup(t ? (const char *)t : "NULL");
  } else {
    size_t n = strlen(L->errmsg(db)) + 32;
    out = malloc(n); snprintf(out, n, "ERROR(step rc=%d: %s)", rc, L->errmsg(db));
  }
  L->finalize(st);
  return out;
}

static int exists(const char *p) { struct stat s; return stat(p, &s) == 0; }
static long long ino(const char *p) { struct stat s; return stat(p, &s) == 0 ? (long long)s.st_ino : -1; }

static void fresh(const char *db) {
  char b[1024];
  unlink(db);
  snprintf(b, sizeof b, "%s-wal", db); unlink(b);
  snprintf(b, sizeof b, "%s-shm", db); unlink(b);
  snprintf(b, sizeof b, "%s-journal", db); unlink(b);
}

static void wal_state(const char *db, const char *label) {
  char w[1024], s[1024];
  snprintf(w, sizeof w, "%s-wal", db);
  snprintf(s, sizeof s, "%s-shm", db);
  printf("    files %-40s: -wal %s (inode %lld), -shm %s (inode %lld)\n", label,
         exists(w) ? "present" : "ABSENT ", ino(w), exists(s) ? "present" : "ABSENT ", ino(s));
}

/* Independent check in a separate process with the system sqlite3 CLI. */
static void cli_check(const char *db, const char *label) {
  char cmd[2048];
  printf("    independent check (%s) via /usr/bin/sqlite3 in a separate process:\n", label);
  snprintf(cmd, sizeof cmd,
           "/usr/bin/sqlite3 '%s' 'SELECT \"      rows: \" || count(*) || \"  distinct: \" || count(DISTINCT v) FROM t;' "
           "'SELECT \"      integrity_check: \" || group_concat(integrity_check, \" | \") FROM pragma_integrity_check;' 2>&1 | sed 's/^/      /'",
           db);
  fflush(stdout);
#if TARGET_OS_SIMULATOR
  (void)cmd; printf("      (simulator build: run this check from the host afterwards)\n");
#else
  system(cmd);
#endif
}

/* ---------------- T1 ---------------- */
static void t1(Lib *A, Lib *B, const char *dir) {
  char db[1024]; snprintf(db, sizeof db, "%s/t1.db", dir); fresh(db);
  printf("\nT1  rollback-journal mode: can two write locks be held at once?\n");
  sqlite3 *a = xopen(A, db);
  run(A, a, "PRAGMA journal_mode=DELETE; CREATE TABLE t(v INTEGER);");
  sqlite3 *b = xopen(B, db);
  run(A, a, "BEGIN IMMEDIATE; INSERT INTO t VALUES(1);");
  int rc = run(B, b, "BEGIN IMMEDIATE;");
  printf("    => B's write lock while A holds RESERVED: %s\n",
         rc == 5 ? "refused (SQLITE_BUSY) — locking works" : rc == 0 ? "GRANTED — no mutual exclusion" : "other");
  if (rc == 0) run(B, b, "ROLLBACK;");
  run(A, a, "COMMIT;");
  /* A holds a SHARED lock via an open read statement; can B commit a write (needs EXCLUSIVE)? */
  sqlite3_stmt *st = NULL;
  A->prepare_v2(a, "SELECT v FROM t", -1, &st, NULL);
  A->step(st); /* A now holds SHARED */
  rc = run(B, b, "INSERT INTO t VALUES(2);");
  printf("    => B's commit (needs EXCLUSIVE) while A is mid-read holding SHARED: %s\n",
         rc == 5 ? "refused (SQLITE_BUSY) — locking works" : rc == 0 ? "SUCCEEDED — wrote under an active reader" : "other");
  A->finalize(st);
  B->close_v2(b); A->close_v2(a);
}

/* ---------------- T2 ---------------- */
static void t2(Lib *A, Lib *B, const char *dir) {
  char db[1024]; snprintf(db, sizeof db, "%s/t2.db", dir); fresh(db);
  printf("\nT2  WAL mode: can two writers hold the WAL write lock at once, and what happens if they both commit?\n");
  sqlite3 *a = xopen(A, db);
  run(A, a, "PRAGMA journal_mode=WAL; CREATE TABLE t(v INTEGER); INSERT INTO t VALUES(0);");
  sqlite3 *b = xopen(B, db);
  run(B, b, "SELECT count(*) FROM t;");
  run(A, a, "BEGIN IMMEDIATE; INSERT INTO t VALUES(1);");
  int rc = run(B, b, "BEGIN IMMEDIATE;");
  printf("    => B's WAL write lock while A holds it: %s\n",
         rc == 5 ? "refused (SQLITE_BUSY) — locking works" : rc == 0 ? "GRANTED — two writers at once" : "other");
  if (rc == 0) {
    run(B, b, "INSERT INTO t VALUES(2);");
    run(A, a, "COMMIT;");
    run(B, b, "COMMIT;");
    char *ca = scalar(A, a, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
    char *cb = scalar(B, b, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
    printf("    A sees: %s\n    B sees: %s   (both commits succeeded; correct answer is 3 rows: 0,1,2)\n", ca, cb);
    free(ca); free(cb);
    char *ic = scalar(A, a, "PRAGMA integrity_check");
    printf("    integrity_check via A: %s\n", ic); free(ic);
  } else {
    run(A, a, "COMMIT;");
  }
  B->close_v2(b); A->close_v2(a);
  cli_check(db, "after both closed");
}

/* ---------------- T3 ---------------- */
static void t3(Lib *A, Lib *B, const char *dir) {
  char db[1024]; snprintf(db, sizeof db, "%s/t3.db", dir); fresh(db);
  printf("\nT3  WAL mode: B stays open (idle); A opens, writes and closes. No two writes overlap.\n");
  sqlite3 *b = xopen(B, db);
  run(B, b, "PRAGMA journal_mode=WAL; CREATE TABLE t(v INTEGER); INSERT INTO t VALUES(1);");
  wal_state(db, "after B's first write");
  sqlite3 *a = xopen(A, db);
  run(A, a, "INSERT INTO t VALUES(2);");
  A->close_v2(a);
  wal_state(db, "after A closes (B still open)");
  run(B, b, "INSERT INTO t VALUES(3);");
  wal_state(db, "after B writes again");
  a = xopen(A, db);
  run(A, a, "INSERT INTO t VALUES(4);");
  char *ca = scalar(A, a, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
  char *cb = scalar(B, b, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
  printf("    A sees: %s\n    B sees: %s   (every INSERT returned rc=0; correct answer is 4 rows: 1,2,3,4)\n", ca, cb);
  free(ca); free(cb);
  A->close_v2(a);
  wal_state(db, "after A closes again");
  B->close_v2(b);
  wal_state(db, "after B closes");
  cli_check(db, "after both closed");
}


/* ---------------- T3b ---------------- */
static void t3b(Lib *A, Lib *B, const char *dir) {
  char db[1024]; snprintf(db, sizeof db, "%s/t3b.db", dir); fresh(db);
  printf("\nT3b WAL mode: B (the long-lived app connection) stays open; A (capture) does open-write-close for three visits, B writes between them.\n");
  sqlite3 *b = xopen(B, db);
  run(B, b, "PRAGMA journal_mode=WAL; CREATE TABLE t(v INTEGER); INSERT INTO t VALUES(1);");
  wal_state(db, "start");
  int v = 2;
  for (int visit = 1; visit <= 3; visit++) {
    char sql[128];
    sqlite3 *a = xopen(A, db);
    snprintf(sql, sizeof sql, "INSERT INTO t VALUES(%d);", v++); run(A, a, sql);
    A->close_v2(a);
    char label[64]; snprintf(label, sizeof label, "after capture visit %d closes", visit);
    wal_state(db, label);
    snprintf(sql, sizeof sql, "INSERT INTO t VALUES(%d);", v++); run(B, b, sql);
    char *cb = scalar(B, b, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
    printf("    B sees: %s (expected %d rows)\n", cb, v - 1); free(cb);
  }
  sqlite3 *a = xopen(A, db);
  char *ca = scalar(A, a, "SELECT count(*)||' rows: '||group_concat(v) FROM t");
  printf("    fresh A connection sees: %s (expected %d rows)\n", ca, v - 1); free(ca);
  char *ic = scalar(A, a, "PRAGMA integrity_check"); printf("    integrity_check via A: %s\n", ic); free(ic);
  A->close_v2(a);
  B->close_v2(b);
  wal_state(db, "after all close");
  cli_check(db, "after all closed");
}

/* ---------------- T4 ---------------- */
static void t4(Lib *A, Lib *B, const char *dir) {
#if TARGET_OS_SIMULATOR
  (void)A; (void)B; (void)dir; printf("\nT4  skipped on the simulator (needs a second process)\n"); return;
#endif
  char db[1024]; snprintf(db, sizeof db, "%s/t4.db", dir); fresh(db);
  char cmd[2048];
  printf("\nT4  rollback mode, the documented close() case, observed from a separate process\n");
  sqlite3 *b = xopen(B, db);
  run(B, b, "PRAGMA journal_mode=DELETE; CREATE TABLE t(v INTEGER);");
  run(B, b, "BEGIN IMMEDIATE; INSERT INTO t VALUES(1);");
  snprintf(cmd, sizeof cmd,
           "/usr/bin/sqlite3 -cmd '.timeout 0' '%s' 'BEGIN IMMEDIATE; INSERT INTO t VALUES(99); COMMIT;' >/dev/null 2>&1 "
           "&& echo '      other process: write lock GRANTED' || echo '      other process: write lock refused (busy)'", db);
  printf("    B holds RESERVED. Another process tries to write:\n"); fflush(stdout);
#if !TARGET_OS_SIMULATOR
  system(cmd);
#endif
  sqlite3 *a = xopen(A, db);
  char *c = scalar(A, a, "SELECT count(*) FROM t");
  printf("    [%s] opened the same file, read count=%s, now closes\n", A->name, c); free(c);
  A->close_v2(a);
  printf("    A has closed. Another process tries to write again:\n"); fflush(stdout);
#if !TARGET_OS_SIMULATOR
  system(cmd);
#endif
  run(B, b, "COMMIT;");
  B->close_v2(b);
  cli_check(db, "after all closed (correct: B's row 1 present; 99 only if a lock was lost)");
}

/* ---------------- T5 ---------------- */
typedef struct { Lib *L; const char *db; int n; int id; int ok; int busy; int other; } Job;

static void *worker(void *p) {
  Job *j = p;
  sqlite3 *db = NULL;
  j->L->open_v2(j->db, &db, OPEN_FLAGS, NULL);
  j->L->busy_timeout(db, 5000);
  char sql[256];
  for (int i = 0; i < j->n; i++) {
    snprintf(sql, sizeof sql, "BEGIN IMMEDIATE; INSERT INTO t VALUES(%d); COMMIT;", j->id * 1000000 + i);
    int rc = j->L->exec(db, sql, NULL, NULL, NULL);
    if (rc == 0) j->ok++;
    else { if ((rc & 0xff) == 5) j->busy++; else j->other++; j->L->exec(db, "ROLLBACK", NULL, NULL, NULL); }
    /* Close and reopen every 50 inserts: models capture code that opens per event. */
    if (i % 50 == 49) { j->L->close_v2(db); j->L->open_v2(j->db, &db, OPEN_FLAGS, NULL); j->L->busy_timeout(db, 5000); }
  }
  j->L->close_v2(db);
  return NULL;
}

static void t5(Lib *A, Lib *B, const char *dir, int n) {
  char db[1024]; snprintf(db, sizeof db, "%s/t5.db", dir); fresh(db);
  printf("\nT5  stress: two threads, one per library, WAL, busy_timeout 5s, %d committed inserts each\n", n);
  sqlite3 *s = xopen(A, db);
  run(A, s, "PRAGMA journal_mode=WAL; CREATE TABLE t(v INTEGER);");
  A->close_v2(s);
  pthread_t ta, tb;
  Job ja = {A, db, n, 1, 0, 0, 0}, jb = {B, db, n, 2, 0, 0, 0};
  pthread_create(&ta, NULL, worker, &ja);
  pthread_create(&tb, NULL, worker, &jb);
  pthread_join(ta, NULL); pthread_join(tb, NULL);
  printf("    thread A: %d commits reported OK, %d busy, %d other errors\n", ja.ok, ja.busy, ja.other);
  printf("    thread B: %d commits reported OK, %d busy, %d other errors\n", jb.ok, jb.busy, jb.other);
  printf("    rows that should exist: %d\n", ja.ok + jb.ok);
  cli_check(db, "after both threads finished");
}

int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage: %s libA libB workdir [stressN]\n", argv[0]); return 1; }
  Lib A, B;
  load(&A, argv[1], "A");
  load(&B, argv[2], "B");
  printf("A = %s\n    version %s, threadsafe=%d, source %s\n", argv[1], A.libversion(), A.threadsafe(), A.sourceid());
  printf("B = %s\n    version %s, threadsafe=%d, source %s\n", argv[2], B.libversion(), B.threadsafe(), B.sourceid());
  printf("same loaded image (one copy)? %s\n", A.h == B.h ? "YES — control run" : "NO — two copies in one process");
  int n = argc > 4 ? atoi(argv[4]) : 2000;
  const char *sel = argc > 5 ? argv[5] : "1,2,3,3b,4,5";
  char buf[64]; snprintf(buf, sizeof buf, ",%s,", sel);
  if (strstr(buf, ",1,")) t1(&A, &B, argv[3]);
  if (strstr(buf, ",2,")) t2(&A, &B, argv[3]);
  if (strstr(buf, ",3,")) t3(&A, &B, argv[3]);
  if (strstr(buf, ",3b,")) t3b(&A, &B, argv[3]);
  if (strstr(buf, ",4,")) t4(&A, &B, argv[3]);
  if (strstr(buf, ",5,")) t5(&A, &B, argv[3], n);
  fflush(stdout);
  return 0;
}

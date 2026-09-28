/* lockprobe.c — which kind of lock does a given SQLite library take?
 * Opens a db through <lib>, takes a write lock (BEGIN IMMEDIATE -> RESERVED byte
 * 0x40000001), then a forked child asks the kernel with fcntl(F_GETLK) who holds it.
 * Classic POSIX record locks report the owner's pid; open-file-description (OFD)
 * locks report l_pid = -1. */
#include <dlfcn.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
typedef struct sqlite3 sqlite3;
int main(int c, char **v) {
  void *h = dlopen(v[1], RTLD_NOW | RTLD_LOCAL);
  int (*open_v2)(const char *, sqlite3 **, int, const char *) = dlsym(h, "sqlite3_open_v2");
  int (*exec)(sqlite3 *, const char *, void *, void *, char **) = dlsym(h, "sqlite3_exec");
  const char *(*ver)(void) = dlsym(h, "sqlite3_libversion");
  sqlite3 *db; unlink(v[2]);
  open_v2(v[2], &db, 6, NULL);
  exec(db, "PRAGMA journal_mode=DELETE; CREATE TABLE t(x); BEGIN IMMEDIATE; INSERT INTO t VALUES(1);", 0, 0, 0);
  printf("%s (SQLite %s), parent pid %d holds RESERVED\n", v[1], ver(), getpid());
  fflush(stdout);
  pid_t p = fork();
  if (p == 0) {
    int fd = open(v[2], O_RDWR);
    struct flock f; memset(&f, 0, sizeof f);
    f.l_type = F_WRLCK; f.l_whence = SEEK_SET; f.l_start = 0x40000001; f.l_len = 1;
    fcntl(fd, F_GETLK, &f);
    printf("  child F_GETLK on RESERVED byte: l_type=%s l_pid=%d  => %s\n",
           f.l_type == F_UNLCK ? "UNLCK" : f.l_type == F_WRLCK ? "WRLCK" : "RDLCK", (int)f.l_pid,
           f.l_type == F_UNLCK ? "no lock visible" : f.l_pid == -1 ? "OFD (open-file-description) lock" : "classic per-process POSIX lock");
    fflush(stdout); _exit(0);
  }
  waitpid(p, 0, 0);
  return 0;
}

/* After library L takes a write lock (RESERVED), can the SAME process take a classic
 * fcntl(F_SETLK) write lock on that byte through a fresh fd? Classic-vs-classic in one
 * process: always granted. If refused, L's lock is not a classic per-process lock. */
#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
typedef struct sqlite3 sqlite3;
int main(int c, char **v) {
  void *h = dlopen(v[1], RTLD_NOW | RTLD_LOCAL);
  int (*open_v2)(const char *, sqlite3 **, int, const char *) = dlsym(h, "sqlite3_open_v2");
  int (*exec)(sqlite3 *, const char *, void *, void *, char **) = dlsym(h, "sqlite3_exec");
  sqlite3 *db; unlink(v[2]); open_v2(v[2], &db, 6, NULL);
  exec(db, "PRAGMA journal_mode=DELETE; CREATE TABLE t(x); BEGIN IMMEDIATE; INSERT INTO t VALUES(1);", 0, 0, 0);
  int fd = open(v[2], O_RDWR);
  struct flock f; memset(&f, 0, sizeof f);
  f.l_type = F_WRLCK; f.l_whence = SEEK_SET; f.l_start = 0x40000001; f.l_len = 1;
  int r = fcntl(fd, F_SETLK, &f);
  printf("%-50s same-process classic F_SETLK on RESERVED byte: %s\n", v[1], r == 0 ? "GRANTED (library uses classic POSIX locks)" : strerror(errno));
  return 0;
}

/* Does the macOS kernel let one process take the same write lock twice through two fds? */
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
int lk(int fd, short t, off_t s){ struct flock f; memset(&f,0,sizeof f); f.l_type=t; f.l_whence=SEEK_SET; f.l_start=s; f.l_len=1; int r=fcntl(fd,F_SETLK,&f); return r==0?0:errno; }
int main(int c,char**v){
  int a=open(v[1],O_RDWR|O_CREAT,0644), b=open(v[1],O_RDWR);
  printf("fd a WRLCK: %s\n", lk(a,F_WRLCK,0x40000001)?"refused":"granted");
  printf("fd b WRLCK same byte, same process: %s\n", lk(b,F_WRLCK,0x40000001)?"refused":"granted");
  return 0; }

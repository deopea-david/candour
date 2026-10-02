#include <dlfcn.h>
#include <stdio.h>
#include <unistd.h>
typedef struct sqlite3 sqlite3;
typedef struct { int (*open_v2)(const char*,sqlite3**,int,const char*); int (*exec)(sqlite3*,const char*,void*,void*,char**); int (*ext)(sqlite3*); void (*cfg)(int,...); } L;
static void logcb(void*p,int e,const char*m){ printf("      sqlite log [%s] (%d) %s\n",(char*)p,e,m); }
static L load(const char*p){ void*h=dlopen(p,RTLD_NOW|RTLD_LOCAL); L l={dlsym(h,"sqlite3_open_v2"),dlsym(h,"sqlite3_exec"),dlsym(h,"sqlite3_extended_errcode"),dlsym(h,"sqlite3_config")}; return l; }
static void run(L*l,sqlite3*d,const char*n,const char*s){ char*e=0; int rc=l->exec(d,s,0,0,&e); printf("  [%s] %-40s rc=%d ext=%d %s\n",n,s,rc,l->ext(d),e?e:""); }
int main(int c,char**v){
  L A=load(v[1]), B=load(v[2]);
  A.cfg(16 /*SQLITE_CONFIG_LOG*/, logcb, "A"); B.cfg(16, logcb, "B");
  unlink(v[3]); sqlite3*a,*b; A.open_v2(v[3],&a,6,0); B.open_v2(v[3],&b,6,0);
  run(&A,a,"A","PRAGMA journal_mode=DELETE; CREATE TABLE t(x)");
  run(&A,a,"A","BEGIN IMMEDIATE");
  run(&B,b,"B","BEGIN");
  run(&B,b,"B","SELECT count(*) FROM t");
  run(&B,b,"B","INSERT INTO t VALUES(2)");
  return 0; }

#include <dlfcn.h>
#include <stdio.h>
int main(int c,char**v){ void*h=dlopen(v[1],RTLD_NOW|RTLD_LOCAL); if(!h){printf("dlopen: %s\n",dlerror());return 1;}
 const char*(*get)(int)=dlsym(h,"sqlite3_compileoption_get"); const char*(*ver)(void)=dlsym(h,"sqlite3_libversion"); const char*(*src)(void)=dlsym(h,"sqlite3_sourceid");
 printf("%s: SQLite %s  %s\n  ",v[1],ver(),src()); for(int i=0;get(i);i++) printf("%s ",get(i)); printf("\n"); return 0; }

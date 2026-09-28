import ctypes,sys
for p in sys.argv[1:]:
    L=ctypes.CDLL(p); L.sqlite3_compileoption_get.restype=ctypes.c_char_p
    i=0; out=[]
    while True:
        s=L.sqlite3_compileoption_get(i)
        if not s: break
        out.append(s.decode()); i+=1
    print(p, len(out)); print('  '+' '.join(out))

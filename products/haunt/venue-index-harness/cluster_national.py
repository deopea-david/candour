"""cluster_national.py - run the offline near-duplicate clustering over the WHOLE
scope-B index, to size the merge problem nationally and the cluster_id column."""
import duckdb, os, sys, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from harness import hav, name_sim, SP
from scopes import SCOPE
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"),read_only=True)
rows=con.execute("SELECT id,name,lat,lon FROM uk WHERE "+SCOPE['B']).fetchall()
print("rows",len(rows)); t=time.time()
MAXM,MINS=60.0,0.70
parent=list(range(len(rows)))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
g=MAXM/111320.0
cell={}
for i,(_,_,la,lo) in enumerate(rows): cell.setdefault((int(la/g),int(lo/(g*1.6))),[]).append(i)
pairs=0
for key,here in cell.items():
    cy,cx=key; bucket=[]
    for dy in(-1,0,1):
        for dx in(-1,0,1): bucket+=cell.get((cy+dy,cx+dx),[])
    for a in here:
        for b in bucket:
            if a>=b: continue
            if hav(rows[a][2],rows[a][3],rows[b][2],rows[b][3])>MAXM: continue
            pairs+=1
            if name_sim(rows[a][1],rows[b][1])>=MINS:
                ra,rb=find(a),find(b)
                if ra!=rb: parent[max(ra,rb)]=min(ra,rb)
cl=len({find(i) for i in range(len(rows))})
print(f"clusters {cl}  absorbed {len(rows)-cl} ({100*(len(rows)-cl)/len(rows):.2f}% of rows)  "
      f"pairs tested {pairs}  in {time.time()-t:.0f}s")

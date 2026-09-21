"""size_shipped.py - bundle impact of the REMEDIATED index: the CTO's minimal
schema plus the GERS attribute, the cluster_id attribute, and the FTS5 name
index that the name-search path (the spike's largest single lever) requires."""
import duckdb, gzip, os, sqlite3, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scopes import SCOPE
SP=os.path.dirname(os.path.abspath(__file__))
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"),read_only=True)
def build(rows, gers, fts):
    p=os.path.join(SP,"s.sqlite")
    if os.path.exists(p): os.remove(p)
    db=sqlite3.connect(p)
    cols="gers TEXT, name TEXT, cat TEXT, lat REAL, lon REAL, cluster_id INTEGER" if gers \
         else "name TEXT, cat TEXT, lat REAL, lon REAL"
    db.execute(f"CREATE TABLE venue({cols})")
    if gers: db.executemany("INSERT INTO venue VALUES (?,?,?,?,?,?)",[(r[0],r[1],r[2],r[3],r[4],i) for i,r in enumerate(rows)])
    else:    db.executemany("INSERT INTO venue VALUES (?,?,?,?)",[r[1:5] for r in rows])
    db.execute("CREATE INDEX ix ON venue(lat,lon)")
    if fts:
        db.execute("CREATE VIRTUAL TABLE venue_fts USING fts5(name, content='venue', content_rowid='rowid')")
        db.execute("INSERT INTO venue_fts(rowid,name) SELECT rowid,name FROM venue")
    db.commit(); db.execute("VACUUM"); db.close()
    return os.path.getsize(p)/1e6, len(gzip.compress(open(p,'rb').read(),6))/1e6
print(f"{'scope':<6}{'rows':>9}   {'minimal':>16}{'+GERS+cluster':>18}{'+FTS5 name idx':>20}")
for s,w in SCOPE.items():
    rows=con.execute("SELECT id,name,coalesce(basic_category,cat_primary),round(lat,5),round(lon,5) FROM uk WHERE "+w).fetchall()
    a=build(rows,False,False); b=build(rows,True,False); c=build(rows,True,True)
    print(f"{s:<6}{len(rows):>9}   {a[0]:>7.1f}/{a[1]:<7.1f}{b[0]:>9.1f}/{b[1]:<8.1f}{c[0]:>11.1f}/{c[1]:<8.1f}  (MB disk/gz)")
os.remove(os.path.join(SP,"s.sqlite"))

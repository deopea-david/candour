"""size_minimal.py - shipped size on the CTO's stated minimal schema
(name, category, lat/lon at 1e-5, indexed on (lat,lon)) -- i.e. WITHOUT the GERS id --
so the figure is comparable with venue-index-spike.md §2 (23.3 MB / 11.3 MB gz)."""
import duckdb, gzip, os, sqlite3, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scopes import SCOPE
SP=os.path.dirname(os.path.abspath(__file__))
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"),read_only=True)
print(f"{'scope':<6}{'rows':>9}{'no-GERS MB':>12}{'gz MB':>8}{'+GERS MB':>10}{'gz MB':>8}")
for s,w in SCOPE.items():
    rows=con.execute("SELECT id,name,coalesce(basic_category,cat_primary),round(lat,5),round(lon,5) FROM uk WHERE "+w).fetchall()
    out=[]
    for gers in (False,True):
        p=os.path.join(SP,"t.sqlite")
        if os.path.exists(p): os.remove(p)
        db=sqlite3.connect(p)
        if gers:
            db.execute("CREATE TABLE venue(gers TEXT,name TEXT,cat TEXT,lat REAL,lon REAL)")
            db.executemany("INSERT INTO venue VALUES (?,?,?,?,?)",rows)
        else:
            db.execute("CREATE TABLE venue(name TEXT,cat TEXT,lat REAL,lon REAL)")
            db.executemany("INSERT INTO venue VALUES (?,?,?,?)",[r[1:] for r in rows])
        db.execute("CREATE INDEX ix ON venue(lat,lon)"); db.commit(); db.execute("VACUUM"); db.close()
        out += [os.path.getsize(p)/1e6, len(gzip.compress(open(p,'rb').read(),6))/1e6]
    print(f"{s:<6}{len(rows):>9}{out[0]:>12.1f}{out[1]:>8.1f}{out[2]:>10.1f}{out[3]:>8.1f}")
os.remove(os.path.join(SP,"t.sqlite"))

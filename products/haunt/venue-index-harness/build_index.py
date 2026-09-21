"""build_index.py - scope row counts, shipped SQLite size and gzipped size
for each scope, plus a local working table of rows near the three sample areas."""
import duckdb, gzip, os, sqlite3, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scopes import SCOPE
SP=os.path.dirname(os.path.abspath(__file__))
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"))
AREAS={"manchester":(53.4808,-2.2426),"chorlton":(53.4425,-2.2790),"ludlow":(52.3681,-2.7185)}
print(f"{'scope':<6}{'rows':>10}{'sqlite MB':>12}{'gzip MB':>10}")
for s,w in SCOPE.items():
    n=con.execute(f"SELECT count(*) FROM uk WHERE {w}").fetchone()[0]
    p=os.path.join(SP,f"idx_{s}.sqlite")
    if os.path.exists(p): os.remove(p)
    # the CTO's stated minimal shipped schema: name, category, lat/lon at 1e-5, indexed on (lat,lon)
    rows=con.execute(f"""SELECT id, name, coalesce(basic_category,cat_primary),
                          round(lat,5), round(lon,5) FROM uk WHERE {w}""").fetchall()
    db=sqlite3.connect(p)
    db.execute("CREATE TABLE venue(gers TEXT, name TEXT, cat TEXT, lat REAL, lon REAL)")
    db.executemany("INSERT INTO venue VALUES (?,?,?,?,?)", rows)
    db.execute("CREATE INDEX ix ON venue(lat,lon)"); db.commit(); db.execute("VACUUM"); db.close()
    raw=os.path.getsize(p)
    gz=len(gzip.compress(open(p,'rb').read(),6))
    print(f"{s:<6}{n:>10}{raw/1e6:>12.1f}{gz/1e6:>10.1f}")
# working table: everything within 2 km of a sample-area centre, all scopes flagged
cl=" OR ".join(f"(abs(lat-{a})<0.02 AND abs(lon-{o})<0.032)" for a,o in AREAS.values())
con.execute(f"""CREATE OR REPLACE TABLE work AS SELECT id,name,confidence,cat_primary,basic_category,
   tax_hier, lat, lon, src,
   ({SCOPE['A']}) AS in_a, ({SCOPE['B']}) AS in_b, ({SCOPE['C']}) AS in_c
   FROM uk WHERE ({cl}) AND name IS NOT NULL""")
print("\nworking rows near the three areas:",
      con.execute("SELECT count(*) FROM work").fetchone()[0],
      "| in A", con.execute("SELECT count(*) FROM work WHERE in_a").fetchone()[0],
      "| in B", con.execute("SELECT count(*) FROM work WHERE in_b").fetchone()[0],
      "| in C", con.execute("SELECT count(*) FROM work WHERE in_c").fetchone()[0])
con.execute("COPY (SELECT * FROM work) TO '%s' (FORMAT PARQUET)"%os.path.join(SP,"work.parquet"))

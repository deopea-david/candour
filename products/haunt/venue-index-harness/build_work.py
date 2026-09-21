import duckdb, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scopes import SCOPE
SP=os.path.dirname(os.path.abspath(__file__))
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"))
AREAS={"manchester":(53.4808,-2.2426),"chorlton":(53.4425,-2.2790),"ludlow":(52.3681,-2.7185)}
cl=" OR ".join("(abs(lat-(%f))<0.02 AND abs(lon-(%f))<0.032)"%(a,o) for a,o in AREAS.values())
sql=("CREATE OR REPLACE TABLE work AS SELECT id,name,confidence,cat_primary,basic_category,"
     "tax_hier, lat, lon, src, (%s) AS in_a, (%s) AS in_b, (%s) AS in_c "
     "FROM uk WHERE (%s) AND name IS NOT NULL")%(SCOPE['A'],SCOPE['B'],SCOPE['C'],cl)
con.execute(sql)
q=lambda s: con.execute(s).fetchone()[0]
print("working rows:",q("SELECT count(*) FROM work"),"| A",q("SELECT count(*) FROM work WHERE in_a"),
      "| B",q("SELECT count(*) FROM work WHERE in_b"),"| C",q("SELECT count(*) FROM work WHERE in_c"))
con.execute("COPY (SELECT * FROM work) TO '%s' (FORMAT PARQUET)"%os.path.join(SP,"work.parquet"))
print("wrote work.parquet")

"""extract.py - rebuild the UK bbox extract of Overture Places 2026-08-19.0.
Same release, bbox and tooling as venue-index-spike.md §2."""
import duckdb, time, os
SP=os.path.dirname(os.path.abspath(__file__))
con = duckdb.connect(os.path.join(SP,"ovt.duckdb"))
con.execute("INSTALL httpfs; LOAD httpfs; INSTALL spatial; LOAD spatial; SET s3_region='us-west-2';")
P="s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/*.parquet"
t=time.time()
con.execute(f"""
CREATE OR REPLACE TABLE uk AS
SELECT id,
       names.primary            AS name,
       confidence,
       categories.primary       AS cat_primary,
       categories.alternate     AS cat_alt,
       basic_category,
       taxonomy.primary         AS tax_primary,
       taxonomy.hierarchy       AS tax_hier,
       operating_status,
       (bbox.xmin+bbox.xmax)/2  AS lon,
       (bbox.ymin+bbox.ymax)/2  AS lat,
       list_distinct(list_transform(sources, s -> s.dataset)) AS src
FROM read_parquet('{P}', hive_partitioning=1)
WHERE bbox.xmin BETWEEN -8.65 AND 1.77
  AND bbox.ymin BETWEEN 49.86 AND 60.86
""")
n=con.execute("SELECT count(*) FROM uk").fetchone()[0]
print("rows", n, "in %.1fs"%(time.time()-t))
con.execute("CREATE INDEX IF NOT EXISTS ix_uk_ll ON uk(lat,lon)")
con.close()

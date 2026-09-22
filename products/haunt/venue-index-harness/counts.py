import duckdb, os
SP=os.path.dirname(os.path.abspath(__file__))
con=duckdb.connect(os.path.join(SP,"ovt.duckdb"), read_only=True)
q=lambda s: con.execute(s).fetchone()[0]
print("all rows                      ", q("SELECT count(*) FROM uk"))
print("named, conf>=0.5              ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5"))
for c in ("pub","cafe","restaurant","coffee_shop"):
    print(f"  cat_primary={c:<12}        ", q(f"SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5 AND cat_primary='{c}'"))
print("food_and_drink named          ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND tax_hier[1]='food_and_drink'"))
print("food_and_drink named conf>=.5 ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5 AND tax_hier[1]='food_and_drink'"))
print("null taxonomy named conf>=.5  ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5 AND (tax_hier IS NULL OR len(tax_hier)=0)"))
print("cat_primary='inn'             ", q("SELECT count(*) FROM uk WHERE cat_primary='inn'"))
print("  ...of which hier[1]=lodging ", q("SELECT count(*) FROM uk WHERE cat_primary='inn' AND tax_hier[1]='lodging'"))
print("basic_category='bar'          ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5 AND basic_category='bar'"))
print("basic_category in (bar,rest)  ", q("SELECT count(*) FROM uk WHERE name IS NOT NULL AND confidence>=0.5 AND basic_category IN ('bar','restaurant')"))
print("operating_status non-null(f&d)", q("SELECT count(*) FROM uk WHERE tax_hier[1]='food_and_drink' AND name IS NOT NULL AND operating_status IS NOT NULL"))

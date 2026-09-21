"""match.py - resolve every sampled FSA venue to the set of Overture rows that ARE it.

Searches the full named extract within 500 m (not just a scope), so a venue can be
classified ABSENT / CAT / CONF exactly as venue-index-spike.md §4.3 does.
Writes truth.json: per venue, the matching row ids with distance and scope membership.
"""
import json, os, sys
import duckdb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import hav, name_sim, SP

MATCH_SIM = 0.72        # plus the distance-graded rule in accept()
con = duckdb.connect(os.path.join(SP, "ovt.duckdb"), read_only=True)
allrows = [dict(id=r[0], name=r[1], conf=r[2], cat=r[3] or r[4], lat=r[5], lon=r[6],
                in_a=r[7], in_b=r[8], in_c=r[9])
           for r in con.execute("SELECT id,name,confidence,basic_category,cat_primary,lat,lon,"
                                "in_a,in_b,in_c FROM work").fetchall()]
sample = json.load(open(os.path.join(SP, "sample.json")))
truth = {}
for area, vs in sample.items():
    for v in vs:
        key = f"{area}:{v['fhrsid']}"
        ms = []
        for r in allrows:
            d = hav(v["lat"], v["lon"], r["lat"], r["lon"])
            if d > 500: continue
            s = name_sim(v["name"], r["name"])
            # a weaker name match is only credible when the row is also close by
            if s >= MATCH_SIM and (d <= 150 or s >= 0.88):
                ms.append(dict(id=r["id"], name=r["name"], d=round(d, 1), sim=round(s, 3),
                               cat=r["cat"], conf=r["conf"],
                               in_a=bool(r["in_a"]), in_b=bool(r["in_b"]), in_c=bool(r["in_c"])))
        ms.sort(key=lambda m: m["d"])
        truth[key] = dict(area=area, name=v["name"], btype=v["btype"],
                          lat=v["lat"], lon=v["lon"], matches=ms)
json.dump(truth, open(os.path.join(SP, "truth.json"), "w"), indent=1)

# ---- classification of venues with no match inside the shipped scope, per §4.3
from collections import Counter
for scope, key in (("A", "in_a"), ("B", "in_b"), ("C", "in_c")):
    c = Counter()
    for k, t in truth.items():
        ins = [m for m in t["matches"] if m[key]]
        if ins: c["FOUND"] += 1
        elif not t["matches"]: c["ABSENT"] += 1
        elif any(m["conf"] < 0.5 for m in t["matches"]): c["CONF"] += 1
        else: c["CAT"] += 1
    print(scope, dict(c), "of", len(truth))

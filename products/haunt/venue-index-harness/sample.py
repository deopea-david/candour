"""sample.py - seeded stratified sample, same method and seed as
venue-index-spike.md §3: up to 25 Pub/bar/nightclub + up to 25
Restaurant/Cafe/Canteen per area, random.seed(20260918)."""
import json, os, random
SP=os.path.dirname(os.path.abspath(__file__))
fsa=json.load(open(os.path.join(SP,"fsa.json")))
random.seed(20260918)
out={}
for area in ("manchester","chorlton","ludlow"):
    rows=sorted(fsa[area], key=lambda r: r["fhrsid"])     # deterministic order before the draw
    picked=[]
    for bt in ("Pub/bar/nightclub","Restaurant/Cafe/Canteen"):
        pool=[r for r in rows if r["btype"]==bt]
        picked += random.sample(pool, min(25,len(pool)))
    out[area]=picked
    print(area, "drawn", len(picked),
          "pubs", sum(1 for r in picked if r["btype"]=="Pub/bar/nightclub"),
          "rest", sum(1 for r in picked if r["btype"]!="Pub/bar/nightclub"))
json.dump(out, open(os.path.join(SP,"sample.json"),"w"))
print("total drawn", sum(len(v) for v in out.values()))

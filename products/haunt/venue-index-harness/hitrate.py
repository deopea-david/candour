"""hitrate.py - Metric: top-N hit rate by scope, at a perfect location fix.
Comparable with venue-index-spike.md §4.2 (which measured scope A)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, SP
from handscores import NOT_A_VENUE, AMBIGUOUS, FALSE_MATCH, CLUBS

truth = json.load(open(os.path.join(SP, "truth.json")))
RADIUS, AREAS = 250.0, ("manchester", "chorlton", "ludlow")

def scored(t):
    k = f"{t['area']}:{t['name']}"
    return k not in NOT_A_VENUE and k not in AMBIGUOUS

def truth_ids(t, scope):
    key = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    if f"{t['area']}:{t['name']}" in FALSE_MATCH: return set()
    return {m["id"] for m in t["matches"] if m[key]}

for scope in ("A", "B", "C"):
    idx = Index(scope)
    print(f"\n=== scope {scope} — top-N hit rate, perfect fix, radius {RADIUS:.0f} m ===")
    print(f"{'area':<14}{'n':>4}{'rank1':>14}{'top3':>14}{'top5':>14}{'miss':>10}{'med cands':>11}")
    tot = [0, 0, 0, 0]; cand_all = []
    for area in AREAS:
        rows = [t for t in truth.values() if t["area"] == area and scored(t)]
        c = [0, 0, 0]; cands = []
        for t in rows:
            tid = truth_ids(t, scope)
            near = idx.near(t["lat"], t["lon"], RADIUS)
            cands.append(len(near))
            ranks = [i for i, (d, r) in enumerate(near) if r["id"] in tid]
            best = min(ranks) if ranks else 99
            if best == 0: c[0] += 1
            if best < 3: c[1] += 1
            if best < 5: c[2] += 1
        n = len(rows); cand_all += cands
        cands.sort(); med = cands[len(cands)//2] if cands else 0
        print(f"{area:<14}{n:>4}{c[0]:>6} ({100*c[0]/n:4.1f}%){c[1]:>6} ({100*c[1]/n:4.1f}%)"
              f"{c[2]:>6} ({100*c[2]/n:4.1f}%){n-c[2]:>5} ({100*(n-c[2])/n:4.1f}%){med:>11}")
        for i in range(3): tot[i] += c[i]
        tot[3] += n
    n = tot[3]
    print(f"{'ALL':<14}{n:>4}{tot[0]:>6} ({100*tot[0]/n:4.1f}%){tot[1]:>6} ({100*tot[1]/n:4.1f}%)"
          f"{tot[2]:>6} ({100*tot[2]/n:4.1f}%){n-tot[2]:>5} ({100*(n-tot[2])/n:4.1f}%)")

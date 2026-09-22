"""identity.py - the number that decides the venue page.

Across 20 simulated visits to ONE real pub, how many distinct Candour venue
identities does the user's journal accumulate? One = the venue page is correct.
More than one = the history is split, silently, permanently, with no backfill.

Models the design as specified: NEVER auto-select (ux-note.md §2.2); the user
picks their own pub out of the offered list; if it is not offered they take the
"this venue isn't listed" path and create a local venue.

Variants
  offline clustering of near-duplicate rows        on/off
  confirmation-history prior (sticky choice)       beta
  name-dedupe on the "not listed" path             on/off
  candidate list length L                          5 / 10 / 20
"""
import json, math, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, jitter, stable_seed, SP
from handscores import NOT_A_VENUE, AMBIGUOUS
from stability import SIGMA_A, GATE, VISITS, RADIUS

def simulate(scope, sigma, use_clusters, beta, dedupe, L, namesearch=False,
             visits=VISITS, seed=20260920):
    idx = Index(scope)
    if use_clusters: idx.build_clusters()
    truth = json.load(open(os.path.join(SP, "truth.json")))
    key = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    out = {}
    for area in ("manchester", "chorlton", "ludlow"):
        per = []
        for t in truth.values():
            if t["area"] != area: continue
            if f"{t['area']}:{t['name']}" in NOT_A_VENUE | AMBIGUOUS: continue
            tid = {idx.cluster.get(m["id"], m["id"]) if use_clusters else m["id"]
                   for m in t["matches"] if m[key]}
            rng = random.Random(stable_seed(seed, t["name"], area))
            hist = {}            # identity -> [confirmation query points]
            user = {}            # user-created identity -> [points]   (from "not listed")
            used = []
            for _ in range(visits):
                q = jitter(t["lat"], t["lon"], sigma, rng)
                near = idx.near(q[0], q[1], RADIUS)
                best = {}
                for d, r in near:
                    k = idx.cluster[r["id"]] if use_clusters else r["id"]
                    if k not in best or d < best[k][0]: best[k] = (d, r)
                cand = [(k, d) for k, (d, r) in best.items()]
                # the user's own previously-created venues are offered too
                for uk, pts in user.items():
                    mlat = sum(p[0] for p in pts) / len(pts); mlon = sum(p[1] for p in pts) / len(pts)
                    cand.append((uk, hav(q[0], q[1], mlat, mlon)))
                scored = []
                for k, d in cand:
                    s = -(d * d) / (2 * SIGMA_A * SIGMA_A)
                    if beta:
                        n = sum(1 for p in hist.get(k, []) if hav(q[0], q[1], p[0], p[1]) <= GATE)
                        if n: s += math.log(1.0 + beta * n)
                    scored.append((s, k, d))
                scored.sort(key=lambda z: (-z[0], z[2]))
                shown = [k for _, k, _ in scored[:L]]
                pick = next((k for k in shown if k in tid), None)          # their pub, from the index
                if pick is None:
                    pick = next((k for k in shown if k in user), None)     # their own earlier entry
                if pick is None and namesearch:
                    # the user types the name; the index is searched BY NAME within
                    # the query radius rather than only by distance (FTS5 is already
                    # in the CTO's row 5). Any index row that IS this venue qualifies.
                    pick = next((k for k, _ in cand if k in tid), None)
                if pick is None:                                           # "isn't listed"
                    if dedupe and user:            # typed name matches a venue they already made
                        pick = sorted(user, key=lambda uk: min(hav(q[0], q[1], *p) for p in user[uk]))[0]
                    else:
                        pick = f"user:{t['name']}:{len(user)}"
                    user.setdefault(pick, []).append(q)
                hist.setdefault(pick, []).append(q)
                used.append(pick)
            per.append(dict(name=t["name"], identities=len(set(used)), single=len(set(used)) == 1))
        out[area] = per
    return out

if __name__ == "__main__":
    cfgs = [
      ("as specified (rows, distance, L=5)",        "A", False, 0.0,  False, 5),
      ("+ widened scope B",                          "B", False, 0.0,  False, 5),
      ("+ clustering",                               "B", True,  0.0,  False, 5),
      ("+ sticky prior beta=4",                      "B", True,  4.0,  False, 5),
      ("+ name-dedupe on 'not listed'",              "B", True,  4.0,  True,  5),
      ("+ list length 10",                           "B", True,  4.0,  True, 10),
      ("+ list length 20",                           "B", True,  4.0,  True, 20),
      ("+ name search on 'not listed'",               "B", True,  4.0,  True, 20, True),
    ]
    for sigma in (10.0, 25.0, 50.0):
        print(f"\n=== sigma = {sigma:.0f} m — distinct Candour identities per real pub, 20 visits ===")
        print(f"{'design':<38}{'Manchester':>22}{'Chorlton':>22}{'Ludlow':>22}")
        print(f"{'':<38}" + "".join(f"{'median   %single':>22}" for _ in range(3)))
        for cfg in cfgs:
            label, scope, cl, beta, dd, L = cfg[:6]
            r = simulate(scope, sigma, cl, beta, dd, L, namesearch=(len(cfg) > 6))
            line = f"{label:<38}"
            for a in ("manchester", "chorlton", "ludlow"):
                p = r[a]
                line += f"{statistics.median(x['identities'] for x in p):>12.0f}{100*sum(x['single'] for x in p)/len(p):>9.1f}%"
            print(line)

"""stability.py - THE metric. Rank-1 identity stability across 20 simulated visits.

Comparable with venue-index-spike.md §5.2, which measured ranker R0 on scope A:
Manchester at sigma=25 m gave median 10 distinct rank-1 venues, modal share 0.27,
and 100% of venues whose rank-1 changed at least once.

Rankers
  R0  raw distance over index ROWS                      (the baseline / shipped design)
  R1  raw distance over CLUSTERS (near-duplicates merged offline)
  R2  R1 + the user's own confirmation history as a prior (sticky, bounded)

R2 score for candidate cluster c at query point q:
    -d(c,q)^2 / (2*SIGMA_A^2)  +  log(1 + BETA * n_c(q))
where n_c(q) counts previous confirmations of c made within GATE metres of q.
BETA is the prior strength; BETA=0 reduces R2 to R1.
"""
import json, math, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, jitter, stable_seed, SP
from handscores import NOT_A_VENUE, AMBIGUOUS

SIGMA_A, GATE, VISITS, RADIUS = 25.0, 150.0, 20, 250.0

def rank(idx, q, use_clusters, hist=None, beta=0.0, radius=RADIUS):
    """Return ranked list of identities (cluster ids or row ids), best first."""
    near = idx.near(q[0], q[1], radius)
    best = {}
    for d, r in near:
        k = idx.cluster[r["id"]] if use_clusters else r["id"]
        if k not in best or d < best[k][0]: best[k] = (d, r)
    scored = []
    for k, (d, r) in best.items():
        s = -(d * d) / (2 * SIGMA_A * SIGMA_A)
        if hist and beta:
            n = sum(1 for p in hist.get(k, []) if hav(q[0], q[1], p[0], p[1]) <= GATE)
            if n: s += math.log(1.0 + beta * n)
        scored.append((s, k, d))
    scored.sort(key=lambda t: (-t[0], t[2]))
    return [k for _, k, _ in scored]

def run(scope, sigma, use_clusters, beta, seed=20260920):
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
            hist, firsts = {}, []
            for _ in range(VISITS):
                q = jitter(t["lat"], t["lon"], sigma, rng)
                rk = rank(idx, q, use_clusters, hist, beta)
                firsts.append(rk[0] if rk else None)
                if beta:                     # the user confirms their venue if it is offered
                    hit = next((k for k in rk[:5] if k in tid), None)
                    if hit: hist.setdefault(hit, []).append(q)
            c = {}
            for f in firsts: c[f] = c.get(f, 0) + 1
            per.append(dict(name=t["name"], distinct=len(c), modal=max(c.values()) / VISITS,
                            changed=len(c) > 1,
                            stable_on_truth=(len(c) == 1 and firsts[0] in tid),
                            tail_distinct=len(set(firsts[1:]))))
        out[area] = per
    return out

if __name__ == "__main__":
    print(f"{'ranker':<34}{'area':<13}{'n':>4}{'med distinct':>14}{'modal share':>13}"
          f"{'changed>=1':>12}{'single+correct':>16}")
    cfgs = [("R0 rows, distance  (baseline)", "A", False, 0.0),
            ("R1 clusters, distance",         "B", True,  0.0),
            ("R2 clusters + prior beta=1",    "B", True,  1.0),
            ("R2 clusters + prior beta=4",    "B", True,  4.0),
            ("R2 clusters + prior beta=20",   "B", True, 20.0)]
    for sigma in (10.0, 25.0, 50.0):
        print(f"\n--- sigma = {sigma:.0f} m ---")
        for label, scope, cl, beta in cfgs:
            res = run(scope, sigma, cl, beta)
            for area in ("manchester", "chorlton", "ludlow"):
                p = res[area]; n = len(p)
                print(f"{label:<34}{area:<13}{n:>4}"
                      f"{statistics.median(x['distinct'] for x in p):>14.0f}"
                      f"{statistics.mean(x['modal'] for x in p):>13.2f}"
                      f"{100*sum(x['changed'] for x in p)/n:>11.1f}%"
                      f"{100*sum(x['stable_on_truth'] for x in p)/n:>15.1f}%")
            print()

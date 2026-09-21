# falsestick_fixed.py - falsestick.py with the PYTHONHASHSEED defect fixed.
# The committed falsestick.py is left untouched; this file is the correction.
"""falsestick.py - the price of the sticky prior: the 'user goes next door' case.

The CTO (subscription-sizing-note.md §8.1) and UX both warn that remembering a
choice for a location will confidently offer the wrong pub when the user visits
the one next door. Nobody has measured it. This does.

Protocol: for every ordered pair of sampled venues (V, W) whose true positions are
within NEIGHBOUR_M of each other, the user confirms V ten times, then visits W
twenty times. We measure, on the W visits:
  false-stick@1  V is offered at rank 1
  recall@L of W  W is still offered in the list at all  <- the number that matters,
                 because the design never auto-selects, so the only real harm the
                 prior can do is push the correct neighbour out of the list.
"""
import json, math, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, jitter, stable_seed, SP
from handscores import NOT_A_VENUE, AMBIGUOUS
from stability import SIGMA_A, GATE, RADIUS

NEIGHBOUR_M, PRIMES, VISITS = 100.0, 10, 20

def run(scope, sigma, beta, L, seed=20260920):
    idx = Index(scope); idx.build_clusters()
    truth = json.load(open(os.path.join(SP, "truth.json")))
    key = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    vs = [t for t in truth.values()
          if f"{t['area']}:{t['name']}" not in NOT_A_VENUE | AMBIGUOUS
          and any(m[key] for m in t["matches"])]
    res = {}
    for area in ("manchester", "chorlton", "ludlow"):
        av = [t for t in vs if t["area"] == area]
        fs, rec, pairs = 0, 0, 0
        for V in av:
            for W in av:
                if V is W: continue
                if hav(V["lat"], V["lon"], W["lat"], W["lon"]) > NEIGHBOUR_M: continue
                vid = {idx.cluster[m["id"]] for m in V["matches"] if m[key]}
                wid = {idx.cluster[m["id"]] for m in W["matches"] if m[key]}
                if not vid or not wid or vid & wid: continue   # same cluster: not neighbours
                rng = random.Random(stable_seed(seed, V["name"], W["name"]))
                hist = {}
                for _ in range(PRIMES):        # the user confirms V, ten times
                    q = jitter(V["lat"], V["lon"], sigma, rng)
                    k = sorted(vid)[0]   # FIX: sorted() with a constant key preserved set-iteration
                    # order, which Python salts per process (PYTHONHASHSEED).
                    # See venue-index-nameseach.md §6.
                    hist.setdefault(k, []).append(q)
                for _ in range(VISITS):        # then goes next door, to W
                    q = jitter(W["lat"], W["lon"], sigma, rng)
                    near = idx.near(q[0], q[1], RADIUS)
                    best = {}
                    for d, r in near:
                        c = idx.cluster[r["id"]]
                        if c not in best or d < best[c][0]: best[c] = (d, r)
                    sc = []
                    for c, (d, r) in best.items():
                        s = -(d * d) / (2 * SIGMA_A * SIGMA_A)
                        if beta:
                            n = sum(1 for p in hist.get(c, []) if hav(q[0], q[1], p[0], p[1]) <= GATE)
                            if n: s += math.log(1.0 + beta * n)
                        sc.append((s, c, d))
                    sc.sort(key=lambda z: (-z[0], z[2]))
                    shown = [c for _, c, _ in sc[:L]]
                    pairs += 1
                    if shown and shown[0] in vid: fs += 1
                    if any(c in wid for c in shown): rec += 1
        res[area] = (pairs, 100*fs/pairs if pairs else 0, 100*rec/pairs if pairs else 0)
    return res

if __name__ == "__main__":
    for sigma in (25.0, 50.0):
        print(f"\n=== sigma = {sigma:.0f} m, neighbours within {NEIGHBOUR_M:.0f} m, "
              f"user primed with {PRIMES} confirmations of V, then {VISITS} visits to W ===")
        print(f"{'beta':<8}{'L':<5}{'area':<13}{'W-visits':>10}{'false-stick@1':>16}{'recall@L of W':>16}")
        for L in (5, 20):
            for beta in (0.0, 4.0, 20.0):
                r = run("B", sigma, beta, L)
                for a in ("manchester", "chorlton", "ludlow"):
                    p, f, rc = r[a]
                    if p: print(f"{beta:<8.0f}{L:<5}{a:<13}{p:>10}{f:>15.1f}%{rc:>15.1f}%")
            print()

"""nameseach.py - the typed-name experiment.

venue-index-remediation.md §14.2 item 1: replace the name-search ORACLE in
identity.py with a real FTS5 search driven by independently-sourced query
strings, and see whether the 100% single-identity figure survives.

Part A  per-query-variant retrieval: does FTS5 surface a row that IS this
        venue, within the query radius, inside a list of L?
Part B  the identity-split simulation of identity.py §6.2, unchanged in every
        respect except that the name-search branch calls fts.search() with a
        string from namegen.py instead of being told the answer.

Query-choice policies, pre-registered before the first run:
  random  one variant drawn uniformly per visit   <- HEADLINE
  t1      always the full registered name
  best    the user tries every variant (ceiling)
"""
import json, math, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, jitter, stable_seed, SP
from handscores import NOT_A_VENUE, AMBIGUOUS
from stability import SIGMA_A, GATE, VISITS, RADIUS
import namegen, fts

AREAS = ("manchester", "chorlton", "ludlow")
SCOPE, L_DEFAULT = "B", 20


def scored_truth():
    """The same 134 venues identity.py scores, keyed area:fhrsid."""
    truth = json.load(open(os.path.join(SP, "truth.json")))
    return {k: t for k, t in truth.items()
            if f"{t['area']}:{t['name']}" not in NOT_A_VENUE | AMBIGUOUS}


def hit_table(scope=SCOPE, policy="AND"):
    """{area:fhrsid: {query_text: [(row_id, lat, lon), ...]}} - FTS5 hits,
    no distance filter. Computed once; the radius is applied at query time."""
    q = namegen.all_queries()
    out = {}
    for key, t in scored_truth().items():
        area, fid = key.split(":", 1)
        vs = q[area][fid]["queries"]
        out[key] = {txt: fts.search(txt, scope=scope, policy=policy)
                    for _, txt in vs}
    return out


# ------------------------------------------------------------------ Part A
def part_a(policy="AND", L=L_DEFAULT, scope=SCOPE):
    idx = Index(scope)
    key = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    q = namegen.all_queries()
    hits = hit_table(scope, policy)
    per_kind, per_venue = {}, {}
    for k, t in scored_truth().items():
        area, fid = k.split(":", 1)
        tid = {m["id"] for m in t["matches"] if m[key]}
        if not tid:
            continue                      # no row in scope IS this venue
        per_venue[k] = dict(area=area, any=False, kinds={})
        for kind, txt in q[area][fid]["queries"]:
            near = [(hav(t["lat"], t["lon"], la, lo), rid)
                    for rid, la, lo in hits[k][txt]
                    if hav(t["lat"], t["lon"], la, lo) <= RADIUS]
            near.sort()
            ok = any(rid in tid for _, rid in near[:L])
            per_kind.setdefault(kind, [0, 0])
            per_kind[kind][1] += 1
            per_kind[kind][0] += ok
            per_venue[k]["kinds"][kind] = ok
            per_venue[k]["any"] |= ok
    return per_kind, per_venue


# ------------------------------------------------------------------ Part B
def simulate(sigma, use_clusters=True, beta=4.0, dedupe=True, L=L_DEFAULT,
             namesearch=None, policy="AND", visits=VISITS, scope=SCOPE,
             seed=20260920, hits=None):
    """identity.py's simulate(), with namesearch in
       None | 'oracle' | 'random' | 't1' | 'best'."""
    idx = Index(scope)
    if use_clusters:
        idx.build_clusters()
    key = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    truth = scored_truth()
    q = namegen.all_queries()
    if namesearch in ("random", "t1", "best") and hits is None:
        hits = hit_table(scope, policy)
    out = {}
    for area in AREAS:
        per = []
        for k, t in truth.items():
            if t["area"] != area:
                continue
            fid = k.split(":", 1)[1]
            qv = q[area][fid]["queries"]
            tid = {idx.cluster.get(m["id"], m["id"]) if use_clusters else m["id"]
                   for m in t["matches"] if m[key]}
            rng = random.Random(stable_seed(seed, t["name"], area))
            hist, user, used = {}, {}, []
            for _ in range(visits):
                qp = jitter(t["lat"], t["lon"], sigma, rng)
                near = idx.near(qp[0], qp[1], RADIUS)
                best = {}
                for d, r in near:
                    ck = idx.cluster[r["id"]] if use_clusters else r["id"]
                    if ck not in best or d < best[ck][0]:
                        best[ck] = (d, r)
                cand = [(ck, d) for ck, (d, r) in best.items()]
                for uk, pts in user.items():
                    mlat = sum(p[0] for p in pts) / len(pts)
                    mlon = sum(p[1] for p in pts) / len(pts)
                    cand.append((uk, hav(qp[0], qp[1], mlat, mlon)))
                scoredc = []
                for ck, d in cand:
                    s = -(d * d) / (2 * SIGMA_A * SIGMA_A)
                    if beta:
                        n = sum(1 for p in hist.get(ck, [])
                                if hav(qp[0], qp[1], p[0], p[1]) <= GATE)
                        if n:
                            s += math.log(1.0 + beta * n)
                    scoredc.append((s, ck, d))
                scoredc.sort(key=lambda z: (-z[0], z[2]))
                shown = [ck for _, ck, _ in scoredc[:L]]
                pick = next((ck for ck in shown if ck in tid), None)
                if pick is None:
                    pick = next((ck for ck in shown if ck in user), None)
                if pick is None and namesearch:
                    if namesearch == "oracle":
                        pick = next((ck for ck, _ in cand if ck in tid), None)
                    else:
                        if namesearch == "random":
                            texts = [rng.choice(qv)[1]] if qv else []
                        elif namesearch == "t1":
                            texts = [qv[0][1]] if qv else []
                        else:                       # best: user tries them all
                            texts = [txt for _, txt in qv]
                        seen = {}
                        for txt in texts:
                            for rid, la, lo in hits[k].get(txt, ()):
                                d = hav(qp[0], qp[1], la, lo)
                                if d > RADIUS:
                                    continue
                                ck = idx.cluster.get(rid, rid) if use_clusters else rid
                                if ck not in seen or d < seen[ck]:
                                    seen[ck] = d
                        ranked = [ck for ck, _ in sorted(seen.items(),
                                                         key=lambda z: z[1])][:L]
                        pick = next((ck for ck in ranked if ck in tid), None)
                if pick is None:
                    if dedupe and user:
                        pick = sorted(user, key=lambda uk: min(
                            hav(qp[0], qp[1], *p) for p in user[uk]))[0]
                    else:
                        pick = f"user:{t['name']}:{len(user)}"
                    user.setdefault(pick, []).append(qp)
                hist.setdefault(pick, []).append(qp)
                used.append(pick)
            per.append(dict(name=t["name"], identities=len(set(used)),
                            single=len(set(used)) == 1))
        out[area] = per
    return out


def line(label, res):
    s = f"{label:<40}"
    for a in AREAS:
        p = res[a]
        s += (f"{statistics.median(x['identities'] for x in p):>10.0f}"
              f"{100*sum(x['single'] for x in p)/len(p):>9.1f}%")
    return s


if __name__ == "__main__":
    policy = sys.argv[1] if len(sys.argv) > 1 else "AND"
    print(f"### FTS5 retrieval policy: {policy}\n")

    print("=== Part A — per-variant retrieval of a TRUE row, list of 20, "
          "radius 250 m, scope B ===")
    pk, pv = part_a(policy)
    print(f"{'query variant':<18}{'venues':>8}{'retrieved':>11}{'rate':>9}")
    for kind in sorted(pk):
        ok, n = pk[kind]
        print(f"{kind:<18}{n:>8}{ok:>11}{100*ok/n:>8.1f}%")
    n = len(pv)
    anyok = sum(1 for v in pv.values() if v["any"])
    print(f"{'ANY variant':<18}{n:>8}{anyok:>11}{100*anyok/n:>8.1f}%")
    for a in AREAS:
        sub = [v for v in pv.values() if v["area"] == a]
        print(f"   {a:<15}{len(sub):>8}{sum(1 for v in sub if v['any']):>11}"
              f"{100*sum(1 for v in sub if v['any'])/len(sub):>8.1f}%")

    print("\n=== Part B — identity split, full stack, name search REAL ===")
    for sigma in (10.0, 25.0, 50.0):
        print(f"\n--- sigma = {sigma:.0f} m --- "
              f"{'Manchester':>19}{'Chorlton':>19}{'Ludlow':>19}")
        print(f"{'':<40}" + "".join(f"{'median  %single':>19}" for _ in range(3)))
        h = hit_table(SCOPE, policy)
        print(line("full stack, NO name search (floor)",
                   simulate(sigma, namesearch=None)))
        print(line("+ name search, ORACLE (circular)",
                   simulate(sigma, namesearch="oracle")))
        print(line("+ name search, FTS5 t1 (registered)",
                   simulate(sigma, namesearch="t1", policy=policy, hits=h)))
        print(line("+ name search, FTS5 random  [HEADLINE]",
                   simulate(sigma, namesearch="random", policy=policy, hits=h)))
        print(line("+ name search, FTS5 best-of (ceiling)",
                   simulate(sigma, namesearch="best", policy=policy, hits=h)))

"""nameseach_checks.py - the checks that decide whether Part A/B can be believed.

C1  Is the FTS5 search selective, or a dragnet? Hit-list sizes within radius.
C2  Residual contamination: truth membership required name_sim >= 0.72 against
    the FSA name, and the queries derive from the FSA name. Stratify retrieval
    by that similarity. If the weak-similarity stratum retrieves too, the
    contamination is not carrying the result.
C3  Name-blind truth: redefine "a row that IS this venue" as ANY scope-B row
    within 30 m of the FSA geocode, with no name condition at all, and re-run
    retrieval. Name is then absent from the truth definition entirely.
C4  The hard subset: single-identity rate restricted to the venues that HAVE a
    scope-B row. Venues absent from the dataset pass the metric by creating one
    consistent local venue, which is a correct venue page but not a dataset hit.
C5  Policy and list-length sensitivity.
"""
import json, os, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, name_sim, SP
from stability import RADIUS
import namegen, fts, nameseach
from nameseach import scored_truth, hit_table, simulate, AREAS

SCOPE = "B"
KEY = "in_b"


def c1_selectivity(policy="AND"):
    q = namegen.all_queries()
    hits = hit_table(SCOPE, policy)
    sizes, per_kind = [], {}
    for k, t in scored_truth().items():
        area, fid = k.split(":", 1)
        for kind, txt in q[area][fid]["queries"]:
            n = sum(1 for rid, la, lo in hits[k][txt]
                    if hav(t["lat"], t["lon"], la, lo) <= RADIUS)
            sizes.append(n)
            per_kind.setdefault(kind, []).append(n)
    sizes.sort()
    print(f"C1  FTS5 hits within {RADIUS:.0f} m per typed query "
          f"(scope B = 2,824 rows in the three areas)")
    print(f"    n queries {len(sizes)}   median {statistics.median(sizes):.0f}"
          f"   p90 {sizes[int(.9*len(sizes))]}   max {sizes[-1]}"
          f"   zero-hit {100*sum(1 for s in sizes if s==0)/len(sizes):.1f}%")
    for kind in sorted(per_kind):
        v = sorted(per_kind[kind])
        print(f"      {kind:<16} median {statistics.median(v):>5.0f}"
              f"   p90 {v[int(.9*len(v))]:>4}   max {v[-1]:>4}")
    print("    For comparison, the ORACLE's effective list is every candidate "
          "in radius:")
    idx = Index(SCOPE)
    cs = sorted(len(idx.near(t["lat"], t["lon"], RADIUS))
                for t in scored_truth().values())
    print(f"      distance-only candidates  median {statistics.median(cs):.0f}"
          f"   p90 {cs[int(.9*len(cs))]}   max {cs[-1]}")


def _best_sim(t):
    ms = [m for m in t["matches"] if m[KEY]]
    return max((m["sim"] for m in ms), default=None)


def c2_strata(policy="AND", L=20):
    pk, pv = nameseach.part_a(policy, L)
    truth = scored_truth()
    bands = {"0.72-0.85": [], "0.85-0.95": [], "0.95-1.00": []}
    for k, v in pv.items():
        s = _best_sim(truth[k])
        b = ("0.72-0.85" if s < 0.85 else "0.85-0.95" if s < 0.95 else "0.95-1.00")
        bands[b].append(v["any"])
    print(f"\nC2  Retrieval by the name-similarity that PUT the row in the truth "
          f"set (the residual contamination)")
    print(f"    {'band':<12}{'venues':>8}{'ANY-variant retrieval':>24}")
    for b in ("0.72-0.85", "0.85-0.95", "0.95-1.00"):
        v = bands[b]
        if v:
            print(f"    {b:<12}{len(v):>8}{100*sum(v)/len(v):>23.1f}%")
    allsim = sorted(s for s in (_best_sim(t) for t in truth.values())
                    if s is not None)
    print(f"    similarity distribution: median {statistics.median(allsim):.3f}"
          f"  p25 {allsim[len(allsim)//4]:.3f}  min {allsim[0]:.3f}")


def c3_nameblind(policy="AND", L=20, max_m=30.0):
    """Truth = any scope-B row within max_m of the FSA geocode. No name test."""
    idx = Index(SCOPE)
    q = namegen.all_queries()
    hits = hit_table(SCOPE, policy)
    ok = n = 0
    for k, t in scored_truth().items():
        area, fid = k.split(":", 1)
        tid = {r["id"] for d, r in idx.near(t["lat"], t["lon"], max_m)}
        if not tid:
            continue
        n += 1
        got = False
        for kind, txt in q[area][fid]["queries"]:
            near = sorted((hav(t["lat"], t["lon"], la, lo), rid)
                          for rid, la, lo in hits[k][txt]
                          if hav(t["lat"], t["lon"], la, lo) <= RADIUS)
            if any(rid in tid for _, rid in near[:L]):
                got = True
                break
        ok += got
    print(f"\nC3  Name-blind truth (any scope-B row within {max_m:.0f} m of the "
          f"FSA geocode; name plays NO part in the truth definition)")
    print(f"    venues with such a row: {n};  ANY-variant retrieval "
          f"{100*ok/n:.1f}%  ({ok}/{n})")


def c4_hard_subset(sigma=25.0, policy="AND"):
    truth = scored_truth()
    have = {k for k, t in truth.items() if any(m[KEY] for m in t["matches"])}
    byname = {}
    for k in truth:
        byname.setdefault((truth[k]["area"], truth[k]["name"]), []).append(k)
    h = hit_table(SCOPE, policy)
    print(f"\nC4  Single-identity rate at sigma = {sigma:.0f} m, restricted to "
          f"venues that HAVE a scope-B row ({len(have)} of {len(truth)})")
    print(f"    {'design':<40}{'Manchester':>14}{'Chorlton':>12}{'Ludlow':>10}")
    for label, ns in (("floor: no name search", None),
                      ("oracle (circular)", "oracle"),
                      ("FTS5 t1", "t1"),
                      ("FTS5 random [HEADLINE]", "random"),
                      ("FTS5 best-of", "best")):
        res = simulate(sigma, namesearch=ns, policy=policy,
                       hits=(h if ns in ("random", "t1", "best") else None))
        line = f"    {label:<40}"
        for a in AREAS:
            sub = [x for x in res[a]
                   if any(kk in have for kk in byname[(a, x["name"])])]
            line += f"{100*sum(x['single'] for x in sub)/len(sub):>13.1f}%"
        print(line)


def c5_sensitivity(sigma=25.0):
    h_and = hit_table(SCOPE, "AND")
    h_or = hit_table(SCOPE, "OR")
    print(f"\nC5  Sensitivity at sigma = {sigma:.0f} m "
          f"(single-identity %, Manchester / Chorlton / Ludlow)")
    for lab, pol, h, L in (("AND, L=20 [HEADLINE]", "AND", h_and, 20),
                           ("OR,  L=20", "OR", h_or, 20),
                           ("AND, L=5", "AND", h_and, 5),
                           ("OR,  L=5", "OR", h_or, 5)):
        r = simulate(sigma, namesearch="random", policy=pol, hits=h, L=L)
        print(f"    {lab:<24}" + "".join(
            f"{100*sum(x['single'] for x in r[a])/len(r[a]):>10.1f}%"
            for a in AREAS))


def c6_visits(policy="AND"):
    h = hit_table(SCOPE, policy)
    print("\nC6  P2 non-degradation: single-identity % by visits per venue, "
          "sigma = 25 m, FTS5 random")
    print(f"    {'visits':<10}{'Manchester':>14}{'Chorlton':>12}{'Ludlow':>10}")
    for v in (3, 6, 12, 20, 40):
        r = simulate(25.0, namesearch="random", policy=policy, hits=h, visits=v)
        print(f"    {v:<10}" + "".join(
            f"{100*sum(x['single'] for x in r[a])/len(r[a]):>13.1f}%"
            for a in AREAS))


if __name__ == "__main__":
    c1_selectivity()
    c2_strata()
    c3_nameblind()
    c4_hard_subset()
    c5_sensitivity()
    c6_visits()

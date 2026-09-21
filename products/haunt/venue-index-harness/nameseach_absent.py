"""nameseach_absent.py - the class the ground truth cannot see.

C2 in nameseach_checks.py came back degenerate: every truth match has
name_sim >= 0.909 against the FSA name. So "does name search find a row the
matcher already declared name-similar?" is close to a tautology, and the
retrieval figure in Part A inherits that.

The class that is NOT contaminated is the opposite one: the venues for which
match.py found NO scope-B row at all. If a typed name pulls up a row that a
human reads as the same venue, that is a genuine name-search gain the truth
set could not have granted, because the truth set says there is nothing there.

D1  For each such venue, every FTS5 hit within 250 m, printed for hand reading.
D2  False-pick exposure: how often is the top row of the name-search list NOT
    a true row? The simulation assumes the user never picks a wrong one; this
    says how much work that assumption is doing.
D3  Which venues fail single-identity under the headline configuration.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, SP
from stability import RADIUS
import namegen, fts
from nameseach import scored_truth, hit_table, simulate, AREAS

SCOPE, KEY, L = "B", "in_b", 20


def d1_absent(policy="AND"):
    idx = Index(SCOPE)
    rowinfo = {r["id"]: r for r in idx.rows}
    q = namegen.all_queries()
    hits = hit_table(SCOPE, policy)
    truth = scored_truth()
    absent = [k for k, t in truth.items() if not any(m[KEY] for m in t["matches"])]
    print(f"D1  {len(absent)} scored venues with NO scope-B row in the truth set.")
    print("    FTS5 hits within 250 m of the FSA geocode, for hand reading.\n")
    for k in absent:
        t = truth[k]
        area, fid = k.split(":", 1)
        seen = {}
        for kind, txt in q[area][fid]["queries"]:
            for rid, la, lo in hits[k][txt]:
                d = hav(t["lat"], t["lon"], la, lo)
                if d <= RADIUS:
                    seen.setdefault(rid, (d, []))[1].append(txt)
        print(f"  [{area}] {t['name']!r}")
        if not seen:
            print("      (no FTS5 hit from any variant)")
            continue
        for rid, (d, ts) in sorted(seen.items(), key=lambda z: z[1][0])[:5]:
            r = rowinfo.get(rid, {})
            print(f"      {d:6.1f} m  {r.get('name','?')!r:<44} "
                  f"{str(r.get('cat'))[:22]:<22} via {ts[0]!r}")


def d2_falsepick(policy="AND"):
    idx = Index(SCOPE)
    rowinfo = {r["id"]: r for r in idx.rows}
    q = namegen.all_queries()
    hits = hit_table(SCOPE, policy)
    truth = scored_truth()
    n = top_wrong = nonempty = 0
    examples = []
    for k, t in truth.items():
        tid = {m["id"] for m in t["matches"] if m[KEY]}
        if not tid:
            continue
        area, fid = k.split(":", 1)
        for kind, txt in q[area][fid]["queries"]:
            near = sorted((hav(t["lat"], t["lon"], la, lo), rid)
                          for rid, la, lo in hits[k][txt]
                          if hav(t["lat"], t["lon"], la, lo) <= RADIUS)
            n += 1
            if not near:
                continue
            nonempty += 1
            if near[0][1] not in tid:
                top_wrong += 1
                if len(examples) < 12:
                    examples.append((t["name"], txt,
                                     rowinfo[near[0][1]]["name"], near[0][0]))
    print(f"\nD2  False-pick exposure. Of {nonempty} typed queries that returned "
          f"anything, the nearest returned row is NOT a true row in "
          f"{top_wrong} ({100*top_wrong/nonempty:.1f}%).")
    print("    The simulation assumes the user never picks one of these. "
          "Examples:")
    for nm, txt, got, d in examples:
        print(f"      {nm!r:<34} typed {txt!r:<22} -> {got!r} at {d:.0f} m")


def d3_failures(sigma=25.0, policy="AND"):
    h = hit_table(SCOPE, policy)
    for lab, ns in (("floor (no name search)", None),
                    ("FTS5 random [HEADLINE]", "random"),
                    ("FTS5 t1", "t1")):
        res = simulate(sigma, namesearch=ns, policy=policy,
                       hits=(h if ns else None))
        bad = [(a, x["name"], x["identities"])
               for a in AREAS for x in res[a] if not x["single"]]
        print(f"\nD3  {lab}: {len(bad)} venues fail single-identity "
              f"at sigma = {sigma:.0f} m")
        for a, nm, i in bad:
            print(f"      [{a}] {nm!r} -> {i} identities")


if __name__ == "__main__":
    d1_absent()
    d2_falsepick()
    d3_failures()

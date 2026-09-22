"""nameseach_divergence.py - how different ARE the two names, really?

nameseach_checks.py C2 showed the truth set is defined by near-identical
name_sim, so retrieval conditional on truth membership is partly implied.
This script measures the thing that is NOT implied: the RAW divergence between
the FSA registered string and the Overture string for the same venue, using a
neutral statistic that does no generic-word stripping and no containment
credit -- just lower case, punctuation out, token sets.

If the raw strings diverge a lot and FTS5 still retrieves, the Part A figure
carries information. If they are identical strings, it does not.

E1  raw token-Jaccard distribution, FSA name vs the nearest true Overture row
E2  the cases where the strings genuinely differ, printed in full
E3  adverse reclassification: treat the hand-adjudicated D1 rescues as rows
    that ARE the venue but are NOT retrievable by name, and re-run P1
"""
import json, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import Index, hav, SP
import namegen
from nameseach import scored_truth, hit_table, simulate, AREAS

KEY = "in_b"


def raw_toks(s):
    s = (s or "").lower().replace("’", "").replace("'", "").replace("&", " and ")
    return set(t for t in re.sub(r"[^a-z0-9 ]", " ", s).split() if t)


def e1_e2():
    idx = Index("B")
    info = {r["id"]: r for r in idx.rows}
    truth = scored_truth()
    rows, exact = [], 0
    for k, t in truth.items():
        ms = [m for m in t["matches"] if m[KEY]]
        if not ms:
            continue
        m = min(ms, key=lambda z: z["d"])
        a, b = raw_toks(t["name"]), raw_toks(info[m["id"]]["name"])
        j = len(a & b) / len(a | b) if a | b else 0.0
        rows.append((j, t["name"], info[m["id"]]["name"], m["d"]))
        if a == b:
            exact += 1
    rows.sort()
    js = [r[0] for r in rows]
    print(f"E1  Raw token-Jaccard, FSA string vs nearest true Overture string "
          f"(n = {len(rows)})")
    print(f"    identical token sets: {exact} ({100*exact/len(rows):.1f}%)")
    print(f"    median {statistics.median(js):.2f}   p25 {js[len(js)//4]:.2f}"
          f"   min {js[0]:.2f}   J < 1.0: {sum(1 for x in js if x < 1.0)}"
          f" ({100*sum(1 for x in js if x < 1.0)/len(js):.1f}%)")
    print(f"\nE2  Every venue whose two strings are not token-identical:")
    for j, fsa, ovt, d in rows:
        if j < 1.0:
            print(f"    J={j:.2f}  FSA {fsa!r:<46} OVT {ovt!r:<46} {d:5.1f} m")


# hand adjudication of D1, decided by reading nameseach_absent.txt row by row.
# Listed individually so a reader can disagree item by item.
D1_IS_THE_VENUE = {
    "manchester:1820983": "Areamanchester",        # 'Area', 25.9 m, music_venue - probable
    "manchester:1819352": "Rudy's Pizza Napoletana",  # via the t/as recovery, 13.6 m - clear
}
D1_PROBABLY_NOT = {
    "chorlton:Whalley Range Amateur Football Club": "'Kings Road - Whalley Range AFC' 125.9 m - a ground, uncertain",
    "manchester:Tops Restaurant": "'Tops Buffet City' 171 m - the baseline hand-forced this to a miss",
}


def e3_adverse():
    """Worst case: the two D1 rescues are really present in the index under a
    name the user would not type. They then split between a distance hit and a
    self-created venue. Upper bound on the residual truth-set bias."""
    truth = scored_truth()
    man = [k for k, t in truth.items() if t["area"] == "manchester"]
    n = len(man)
    print(f"\nE3  Adverse reclassification bound.")
    print(f"    Manchester scored venues: {n}")
    print(f"    Hand-adjudicated D1 rescues that are probably the venue: "
          f"{len(D1_IS_THE_VENUE)} (both Manchester)")
    print(f"    If BOTH are really present under a name the user never types, "
          f"and both therefore split,")
    print(f"    the Manchester single-identity rate falls by at most "
          f"{100*len(D1_IS_THE_VENUE)/n:.1f} pp.")
    print(f"    Headline 100.0% -> floor {100 - 100*len(D1_IS_THE_VENUE)/n:.1f}% "
          f"in the worst case.")
    print(f"    Venues where NO variant returned anything within 250 m "
          f"(consistent with genuine absence): see nameseach_absent.txt.")




def e4_stratified(policy="AND", L=20):
    """Retrieval stratified by RAW token-Jaccard -- the stratum that name_sim
    could not discriminate. J < 1.0 means the two strings genuinely differ."""
    import nameseach
    idx = Index("B"); info = {r["id"]: r for r in idx.rows}
    truth = scored_truth()
    pk, pv = nameseach.part_a(policy, L)
    bands = {"J = 1.00 (identical)": [], "0.50 <= J < 1.00": [], "J < 0.50": []}
    per_kind = {}
    for k, v in pv.items():
        t = truth[k]
        m = min((m for m in t["matches"] if m[KEY]), key=lambda z: z["d"])
        a, b = raw_toks(t["name"]), raw_toks(info[m["id"]]["name"])
        j = len(a & b) / len(a | b) if a | b else 0.0
        band = ("J = 1.00 (identical)" if j >= 1.0
                else "0.50 <= J < 1.00" if j >= 0.5 else "J < 0.50")
        bands[band].append(v["any"])
        for kind, ok in v["kinds"].items():
            per_kind.setdefault((band, kind), [0, 0])
            per_kind[(band, kind)][1] += 1
            per_kind[(band, kind)][0] += ok
    print(f"\nE4  ANY-variant retrieval by RAW string divergence")
    print(f"    {'band':<24}{'venues':>8}{'retrieved':>12}")
    for b in ("J = 1.00 (identical)", "0.50 <= J < 1.00", "J < 0.50"):
        v = bands[b]
        if v:
            print(f"    {b:<24}{len(v):>8}{100*sum(v)/len(v):>11.1f}%")
    print(f"\n    per variant, divergent strings only (J < 1.00):")
    kinds = sorted({k for (bd, k) in per_kind})
    for kind in kinds:
        ok = n = 0
        for bd in ("0.50 <= J < 1.00", "J < 0.50"):
            if (bd, kind) in per_kind:
                ok += per_kind[(bd, kind)][0]; n += per_kind[(bd, kind)][1]
        if n:
            print(f"      {kind:<16}{n:>6}{100*ok/n:>9.1f}%")


if __name__ == "__main__":
    e1_e2()
    e3_adverse()
    e4_stratified()

"""namegen.py - realistic query strings, derived from the FSA register ONLY.

THE NON-CIRCULARITY CONTRACT, stated in the code that has to honour it:

  This module reads exactly one field of one file: the `name` field of
  `sample.json`, which holds the Food Standards Agency's registered
  BusinessName for each sampled venue.

  It NEVER reads:
    - any Overture row, name, id or coordinate
    - truth.json, or any match, distance or similarity score
    - harness.name_sim, or any other function used to build the ground truth

  Every rule below is a statement about how the FSA register writes English
  business names and how a phone keyboard renders them. None of them was
  chosen by looking at whether it retrieves anything. The module was written,
  frozen and hashed before the first retrieval was run; if it is ever edited
  after a measurement, the note that quotes it must say so.

Two stages.

STAGE 1 - sign-name recovery. The FSA registers the legal trading entity,
which is documented in venue-index-spike.md §3 limitation 2 as "sometimes not
the sign above the door". These four rules model the four ways that register
writes a name that differs from the shopfront, all four visible in the drawn
sample itself:
  S1  "X also T/as Y" / "X T/A Y"  -> emit BOTH X and Y (either may be the sign)
  S2  "Person - The Y"             -> emit "The Y"; "Chain - Place" -> emit "Chain"
  S3  legal-entity tokens          -> Ltd / Limited / PLC / LLP / Co / Group / UK dropped
  S4  "X @ Y"                      -> emit X

STAGE 2 - typing variants. What a person standing in the pub actually types.
  T1 full        the whole recovered name
  T2 no_article  leading "The" / "Ye Olde" / "Ye" dropped
  T3 head2       first two words
  T4 head1       first word
  T5 longest     the longest word (the memorable one)
  T6 no_generic  trade words and locality names dropped
  T7 prefix4     first four characters of the first word

All variants are normalised the way a keyboard renders them: lower case,
apostrophes dropped, "&" -> "and", other punctuation to space.
"""
import json, os, re, sys

SP = os.path.dirname(os.path.abspath(__file__))

# --- word lists, written here in full so this file is auditable on its own ---
LEGAL = {"ltd", "ltda", "limited", "plc", "llp", "co", "company", "group", "uk",
         "inc", "holdings", "enterprises", "trading"}
# trade words and locality names. Overlaps harness._GENERIC by construction --
# both are lists of ordinary English trade words -- but this one is independent
# of it: it is used to build QUERIES, never to score a match.
GENERIC = {"bar", "cafe", "restaurant", "kitchen", "house", "inn", "tavern",
           "lounge", "pub", "club", "hotel", "bistro", "brasserie", "grill",
           "takeaway", "food", "eatery", "deli", "delicatessen", "coffee",
           "pizza", "buttery", "canteen", "manchester", "chorlton", "ludlow",
           "didsbury", "salford", "street", "road"}
ARTICLES = ("ye olde ", "the ", "ye ")

_TAS = re.compile(r"\b(?:also\s+)?t/?\s?a/?s?\b|\btrading\s+as\b", re.I)


def keyboard(s):
    """What the phone produces: lower case, no apostrophes, & -> and."""
    s = s.lower().replace("’", "").replace("'", "")
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def stage1(raw):
    """Sign-name candidates recovered from one FSA BusinessName."""
    out = []

    def add(s):
        s = s.strip(" -–,.")
        if s and s not in out:
            out.append(s)

    add(raw)
    # S1 trading-as: both sides are plausible sign names
    if _TAS.search(raw):
        for part in _TAS.split(raw):
            add(part)
    # S2 hyphen: "Person - The Y" -> the right side; "Chain - Place" -> the left
    if " - " in raw:
        left, right = raw.split(" - ", 1)
        if right.strip().lower().startswith(("the ", "ye ")):
            add(right)
        else:
            add(left)
    # S4 "@" branch suffix
    if "@" in raw:
        add(raw.split("@", 1)[0])

    # S3 legal-entity tokens, applied to everything gathered so far
    for s in list(out):
        toks = [t for t in keyboard(s).split() if t not in LEGAL]
        add(" ".join(toks))
    return [s for s in out if s.strip()]


def variants(raw):
    """The full frozen variant set for one FSA BusinessName, deduped."""
    seen, out = set(), []

    def add(kind, s):
        s = re.sub(r"\s+", " ", s).strip()
        if len(s) < 2:
            return
        if s in seen:
            return
        seen.add(s)
        out.append((kind, s))

    for cand in stage1(raw):
        k = keyboard(cand)
        if not k:
            continue
        add("T1_full", k)
        na = k
        for a in ARTICLES:
            if na.startswith(a):
                na = na[len(a):]
                break
        add("T2_no_article", na)
        w = na.split()
        if len(w) >= 2:
            add("T3_head2", " ".join(w[:2]))
        if w:
            add("T4_head1", w[0])
            # "the memorable word" means the memorable one. Taking the longest
            # word outright picks the trade suffix for names like "The Bull
            # Hotel" (-> "hotel") and "Athena Greek Taverna" (-> "taverna"),
            # which nobody types. Corrected to the longest NON-generic word.
            # CORRECTION MADE 2026-09-21 BEFORE ANY RETRIEVAL WAS RUN, on the
            # face validity of the rule alone. Hashes of both versions are in
            # venue-index-nameseach.md §2.4.
            pool = [t for t in w if t not in GENERIC] or w
            longest = max(pool, key=len)
            if len(longest) >= 4:
                add("T5_longest", longest)
            add("T7_prefix4", w[0][:4])
        ng = [t for t in w if t not in GENERIC]
        if ng:
            add("T6_no_generic", " ".join(ng))
    return out


def all_queries():
    """{area: {fhrsid: {"fsa_name": str, "queries": [(kind, text), ...]}}}"""
    sample = json.load(open(os.path.join(SP, "sample.json")))
    out = {}
    for area, vs in sample.items():
        out[area] = {}
        for v in vs:
            out[area][str(v["fhrsid"])] = dict(fsa_name=v["name"],
                                               queries=variants(v["name"]))
    return out


if __name__ == "__main__":
    q = all_queries()
    tot = sum(len(x["queries"]) for a in q for x in q[a].values())
    n = sum(len(q[a]) for a in q)
    print(f"{n} venues, {tot} query strings, mean {tot/n:.1f} per venue\n")
    kinds = {}
    for a in q:
        for x in q[a].values():
            for k, _ in x["queries"]:
                kinds[k] = kinds.get(k, 0) + 1
    for k in sorted(kinds):
        print(f"  {k:<16}{kinds[k]:>5}")
    print()
    show = sys.argv[1] if len(sys.argv) > 1 else "ludlow"
    for fid, x in list(q[show].items()):
        print(f"{x['fsa_name']!r}")
        print("     " + " | ".join(f"{k.split('_',1)[1]}={t!r}" for k, t in x["queries"]))
    json.dump(q, open(os.path.join(SP, "queries.json"), "w"), indent=1)

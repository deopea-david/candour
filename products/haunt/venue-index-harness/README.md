# Venue-index measurement harness — Haunt

The measurement harness behind `products/haunt/venue-index-spike.md` (2026-09-18) and
`products/haunt/venue-index-remediation.md` (2026-09-20).

**Why it is here and not in a scratchpad.** The first spike's harness was left in a session
temp directory and **was gone four days later**, which is recorded at §1 of the remediation
note. Rebuilding it consumed the first part of a 113-hour spike. The CTO carries a permanent
regression fixture as **S1** of the remediation decomposition (`subscription-sizing-note.md`
§8.1): *"Without it, no future change to the index can be shown not to have made things worse."*

This directory is that fixture **in draft**. It is the Engineer's working code, preserved so
the numbers in the remediation note can be re-derived by someone who was not in the room.
It has not been reviewed by any other seat and it is not product code.

## Running it

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python duckdb          # pinned at 1.5.5 in both spikes
.venv/bin/python extract.py        # ~50 s, ~430 MB local ovt.duckdb from Overture's public S3
.venv/bin/python build_work.py     # near-area working table
.venv/bin/python fsa.py            # FSA ground truth (live API)
.venv/bin/python sample.py         # seeded stratified draw
.venv/bin/python match.py          # venue -> index row resolution
```

Then any of the measurement scripts. The whole chain is about fifteen minutes on a laptop.

| Script | Measures | Note section |
| --- | --- | --- |
| `counts.py` | baseline/CTO category counts | §2 |
| `hitrate.py` | top-N hit rate by scope | §4 |
| `stability.py` | rank-1 stability, rankers R0/R1/R2 — **the baseline-comparable metric** | §5 |
| `identity.py` | **identity-split simulation** — proposed criterion P1 | §6 |
| `year.py` | identity split vs visits per venue — proposed criterion P2 | §6.3 |
| `falsestick.py` | the "goes next door" test — proposed criterion P3 | §7 |
| `cluster_national.py` | offline near-duplicate clustering, whole index | §5, §9 |
| `size_minimal.py`, `size_shipped.py` | shipped SQLite sizes incl. FTS5 | §12 |

`scopes.py` holds the three category scopes. `handscores.py` holds every hand-adjudication
override, listed individually so a reader can disagree item by item.

## Two things a re-runner must know

1. **Seeding.** `harness.stable_seed()` exists because an earlier version seeded from Python's
   built-in `hash()`, which is salted per process; two runs of one configuration differed by up
   to 6 points. Anything seeded from `hash()` will not reproduce these numbers.
2. **The matcher is the weakest instrument here.** `harness.name_sim()` decides whether two
   names denote the same venue, and the name-search result at §6.2 is circular because the
   simulation uses that same function to decide what a user would type. §14.2 item 1 of the
   remediation note is the experiment that removes the circularity.

## Files

Scripts, plus `sample.json` (the 139-venue seeded draw) and `truth.json` (venue → index-row
resolution with distances and scope membership). `*.txt` are captured run outputs quoted in
the note. `ovt.duckdb` and the built SQLite indexes are **not** committed — they are derived,
large, and `extract.py` rebuilds them.

Data: Overture Maps Places `2026-08-19.0` (CDLA-Permissive-2.0 / Apache-2.0); Food Standards
Agency FHRS API (Crown copyright, Open Government Licence).

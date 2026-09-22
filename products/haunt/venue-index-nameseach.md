# Typed-name experiment — Haunt venue index

**Seat:** Engineer · **Date:** 2026-09-21 · **Commissioned by:** `products/haunt/venue-index-remediation.md` §14.2 item 1 — the one-day experiment that note named as the thing standing between it and a defensible pass
**Baseline:** `products/haunt/venue-index-remediation.md` (Engineer, 2026-09-20) and `products/haunt/venue-index-spike.md` (Engineer, 2026-09-18). Same harness, same Overture release, same FSA ground truth, same seeded sample, same metrics. **Nothing was changed except the one thing under test.**
**Status:** build-gating artifact. **Prepares and flags; does not certify** (Constitution 6.1). Block 4 is the CTO's and only the CTO may lift it; only the CEO may overrule it (Constitution 5.6). Kill/proceed is the CEO's alone (Constitution 5.4).
**Template note:** `pipeline/templates/` has no spike template [E, listed from disk 2026-09-21: `cost-sheet.md`, `decision-record.md`, `dissent-memo.md`, `gate-pack.md`, `idea-brief.md`, `proposal.md`, `requirements.md`, `research-brief.md`, `review-pack.md`]. Structure follows the five items the commission names, plus the verdict and the overturn clause my amended charter requires. The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Everything marked **[E, measured]** is a measurement I ran in this session; the method is stated at the point of use and every script is listed in §11 so a stranger can re-run it. The Overture documentation is **not** re-retrieved here and is attributed to the sessions that did retrieve it. Nothing is cited from memory.

**Method standard:** this note is held to `pipeline/amendment-verification.md` — exhaustive rather than sampled on the load-bearing claim, sources read whole rather than in part, and a clean pass reported as a clean pass when it is the honest one.

---

## 0. Summary and verdict

**The circularity is broken, the measurement clears my own 95% bar, and it does not lift Block 4 — because Block 4's limb (a) as written asks for something this measurement does not touch.**

Seven findings.

1. **The circularity is broken in the two places that matter and not in the third, and I say which.** The query strings are generated from the Food Standards Agency register alone, by a frozen, hashed generator that never reads an Overture name, `truth.json`, or `harness.name_sim` (§2). The retrieval function is a real SQLite **FTS5** prefix search, which shares no code and no notion of similarity with the matcher that built the ground truth (§2.3). **What is not broken is the truth definition** — `match.py` decided which Overture rows *are* each venue using name similarity against the same FSA string — and §5 measures how much that is worth rather than waving at it.
2. **The headline: 100% single-identity in Manchester at σ = 25 m, measured without the oracle.** The circular figure was 100%; the non-circular floor was 81.6%; **the non-circular measured value is 100.0%** under the pre-registered headline policy, **98.0%** under the harshest single-query policy, and **≥95.9%** under an adverse reclassification of every venue my ground truth could have missed. The 81.6–100% range in `venue-index-remediation.md` §8.5 resolves to its top. [E, measured]
3. **Against my pre-registered bar of 95%, the design passes — conditionally, and both conditions are load-bearing.** P1 ≥ 95%: **pass**. P2 ≤ 2 pp: **pass, 0.0 pp**, flat from 3 visits to 40. P4 ≥ 90% at σ = 50 m: **pass at 93.9%** headline, **fail at 89.8%** on the harshest policy — a marginal pass I am reporting as marginal. **The conditions: a twenty-row reachable list, and prefix search rather than whole-string search.** At a five-row list the figure is 93.9% and the bar fails. §7.
4. **Typing the whole registered name is the worst thing a user can do, and four characters is the best.** On the 44 venues whose FSA and Overture strings genuinely differ, typing the full registered name retrieves the right row **50.0%** of the time; typing the first four characters retrieves it **100%** of the time. [E, measured] This is a build instruction, not a statistic: **the search must be incremental and prefix-based.** §4, §5.3.
5. **Block 4 limb (a), as the CTO wrote it, is untouched by this experiment and still fails.** Modal rank-1 share is **0.67** against a bar of 0.8 and top-five recall is **53.1%** against a bar of 80% — the same figures as yesterday, to the digit, because name search does not act on either quantity. §3, §7.1. **I am not going to let a good result on my own bar obscure that.**
6. **The name-search path introduces a hazard the previous note did not have.** On **3.6%** of typed queries that return anything, the nearest returned row is a name-similar *wrong* venue — `Castle Tea Room` 5 m from `Castle Lodge Buttery`, `San Carlo Bottega` 34 m from `San Carlo Gran Cafe` [E, measured]. My simulation assumes the user never picks one. That assumption is doing real work and it is a QA item, not a solved problem. §8.1.
7. **A defect in the committed harness, found by re-running it, and it is the same defect §1 of the previous note records fixing.** `falsestick.py` selects from a Python `set` in a way that is salted per process, so a re-runner gets false-stick figures differing by up to 2 pp in two of three areas. **The published §7 figures are the correct ones** — they reproduce exactly under the fix — but their reproducibility did not hold. A corrected copy is added; the committed original is left untouched for the CTO to take. §9.

**What this means for Block 4.** The previous note could not demonstrate a pass on its own proposed bar because its best number was circular. That reason is now gone. What remains is the question that was always the real one and was never mine: **which bar.** Limb (a) as written still fails; the identity-denominated bar now passes with the conditions at §7.3. Limb (b) is unchanged — prepared at `venue-index-remediation.md` §11, not accepted. **Block 4 is the CTO's. This note hands it a measurement, not a verdict.**

**What would overturn this finding, and where I looked: §10.2.**

---

## 1. What I was asked, and what I did

`venue-index-remediation.md` §14.2 item 1, written by this seat yesterday:

> *"For each of the same 134 venues, take three real sign-names — from the shopfront, the venue's own listing, the FSA registration — and run each against the shipped scope-B index with the actual FTS5 name search rather than my similarity function. … I did not run it because I have no source of sign-names I did not construct myself, and constructing them is exactly the circularity I am trying to escape."*

The commission resolves that by naming the source: **the FSA register, which is already in the harness**. I have no shopfront and no venue listing, so one of the three name sources that sentence asked for is available to me and two are not. **This note therefore runs a narrower experiment than the one I specified**, and §5.6 says exactly what the missing two would have added.

**What I did.** Derived realistic query strings from the FSA `BusinessName` by a frozen rule set; built a real FTS5 index over the scope-B rows; replaced the oracle in `identity.py`'s name-search branch with that search; re-ran the identity-stability and top-N measurements with nothing else changed; and then spent about as long again trying to establish whether the result should be believed, which is §5.

**What I could not do, stated before the numbers rather than after them.** Unchanged from both prior notes and not restated at length: **no device, no `CLVisit` error distribution** — every σ here is an assumption and I report three of them; **no closed-venue detection**, because `operating_status` is populated for 322 of 330,208 UK food-and-drink rows; **no usability testing**, so where I say a user would type something, that is [J] and labelled. §8.3 says whether any of them bears on this particular result.

---

## 2. Breaking the circularity

### 2.1 Why the FSA register is independent of Overture, and the one place it is not

The independence argument is the baseline's and I am not re-deriving it, only re-checking that it still holds. `venue-index-spike.md` §3 establishes it on three grounds: Overture's Places theme is fed by Meta, Microsoft, PinMeTo, Krick, RenderSEO, DAC, BrightQuery, Foursquare and AllThePlaces and *"does not include OpenStreetMap data"*; FSA appears on none of those lists; and every one of the 653 candidate rows that note examined carried `Overture` plus one of `meta`, `Microsoft`, `Foursquare` or `AllThePlaces` as its source, with no FSA-derived provider appearing [E, `venue-index-spike.md` §3, attributed to that session's retrieval of the [Overture Places guide](https://docs.overturemaps.org/guides/places/) and its own measurement — **not re-retrieved by me this session**].

**What I did re-retrieve is the register itself.** The FSA Food Hygiene Rating Scheme API (`https://api.ratings.food.gov.uk/Establishments`, `x-api-version: 2`) returned, on **2026-09-21**, the same in-radius counts as both prior spikes: **828 / 117 / 48** for Manchester, Chorlton and Ludlow [E, measured, `fsa_check.py`, [FSA FHRS API](https://api.ratings.food.gov.uk/Establishments), Crown copyright, Open Government Licence]. And — the check that actually matters for this experiment — **all 139 sampled venues are still in the register today, with byte-identical `BusinessName` values to the ones in the committed `sample.json`** [E, measured]. The strings this experiment queries with are the strings a statutory register holds right now, verified at primary this session, not strings I wrote.

**The one place the independence does not hold, stated here rather than buried in §5.** FSA is independent of Overture as a *data source*. It is **not** independent of my *ground truth*, because `match.py` used name similarity between the FSA string and the Overture string to decide which rows are the venue. That is a real residual and §5.2 measures it.

### 2.2 The generator, and why the process is not circular

`namegen.py` is the whole of the query derivation. **It reads exactly one field of one file: the `name` field of `sample.json`.** It never opens `ovt.duckdb`, never reads `truth.json`, never imports `harness.name_sim`, and never sees a match, a distance or a similarity score. That is a property a reader can check in thirty seconds by reading the imports, and it is the reason the output is not circular: **nothing in the generator has any way of knowing what would make a query succeed.**

**Stage 1 — sign-name recovery.** The FSA registers the legal trading entity, which `venue-index-spike.md` §3 limitation 2 documents as *"sometimes not the sign above the door"*. Four rules model the four ways the register writes a name that differs from the shopfront, all four visible in the drawn sample itself:

| Rule | Pattern | Example from the sample |
| --- | --- | --- |
| **S1** | `X also T/as Y` → emit **both** X and Y | `Rudy's Pizza Limited also T/as Rudy's Home Bake Kitchen` |
| **S2** | `Person - The Y` → emit `The Y`; `Chain - Place` → emit `Chain` | `Natalie White - The Compasses`; `Subway - Chorlton` |
| **S3** | drop legal-entity tokens — Ltd, Limited, PLC, LLP, Co, Company, Group, UK | `The Beer House Chorlton (Ltd)`; `Taste at No.1 LTD` |
| **S4** | `X @ Y` → emit X | `Subway @ EG On The Move` |

**Stage 2 — typing variants**, from each stage-1 candidate: `T1_full` the whole name; `T2_no_article` with a leading *The* / *Ye Olde* / *Ye* dropped; `T3_head2` the first two words; `T4_head1` the first word; `T5_longest` the longest non-generic word; `T6_no_generic` with trade words and locality names dropped; `T7_prefix4` the first four characters of the first word. All normalised the way a phone keyboard renders them: lower case, apostrophes dropped, `&` → `and`, other punctuation to space.

**Result: 139 venues, 491 distinct query strings, mean 3.5 per venue** [E, measured, `namegen.py`]. The full set is committed as `queries.json` so a reader can disagree string by string.

**Why this is not circular, in one paragraph a stranger can check.** A circular measurement is one whose success is entailed by its own construction. The previous note's was: `identity.py` awarded the user a hit whenever any row that *is* the venue was within the query radius, which is the oracle answer, granted for free. Here, success requires a specific string — produced by rules that never saw the index — to retrieve a specific row through a tokeniser and a prefix operator that know nothing about the FSA. The generator has no gradient towards success; **29.8% of the generated queries return nothing at all** (§5.1), which is the simplest possible demonstration that it was not tuned to succeed.

### 2.3 The retrieval function, and why FTS5 is not `name_sim`

`fts.py` builds an in-memory SQLite **FTS5** table over the 2,824 scope-B rows in the three sample areas, tokenised `unicode61 remove_diacritics 2`, and searches it as a shipped implementation would: every query token as a prefix term, **AND**ed. Hits are then filtered to the 250 m query radius and ranked by distance, exactly as the distance path is, and the user picks from the first twenty.

FTS5 is the CTO's own choice, already inside row 5 of `android-and-stack-note.md` §3.2, and its bundle cost is already measured at `venue-index-remediation.md` §12 [E, attributed, not re-derived here]. It shares no code with `harness.name_sim`, has no concept of token Jaccard, no containment rule, no generic-word list and no distance-graded acceptance. Two strings that `name_sim` scores at 1.0 can miss entirely under FTS5 and do: `Beech Inn` scores 1.0 against `Beech Road Cafe` under `name_sim`, because both reduce to the single distinctive token *beech* once trade words are stripped, and an AND-of-prefixes query for `beech inn` does not retrieve `Beech Road Cafe` at all.

**A second policy, `OR`-of-prefixes, is reported as a sensitivity** (§7.2). It is not straightforwardly the optimistic one: `OR` on `the spread eagle` returns **367** rows because of the article, against **1** for `AND` [E, measured]. A design that ORs must rank, and ranking is a design choice this note does not make.

### 2.4 The one correction I made to the generator, and when

`T5_longest` originally took the longest word outright. On reading the generated strings — **and before any retrieval had been run** — I saw it produced `hotel` for `The Bull Hotel` and `taverna` for `Athena Greek Taverna`, which nobody types. I changed it to the longest **non-generic** word.

I record this because the correction is exactly the kind of thing that is invisible later and decisive now. **It was made on the face validity of the rule alone, with no measurement in existence to tune it towards.** Both versions are hashed:

| Version | SHA-256 of `namegen.py` | Queries generated |
| --- | --- | --- |
| As first written | `47fc37c823f7c9e008cdc6e8c80e5b8f34d4e12ef6a1fd9763082c9a2377d15d` | 511 |
| Corrected, frozen, used for everything below | `c000883721a8e8126e6ba7900291f495984049cbeaa636355f8c73cd7d0cdea9` | 491 |

**No other edit was made to the generator after the first retrieval was run.** The correction cuts *against* the result — it removes 20 query strings, and the ones it removes are ones that would have failed — so a reader who thinks the correction was self-serving should note that the uncorrected version would have produced a *lower* per-query retrieval rate and a *higher* count of variants, and that the headline simulation policy draws uniformly from the variant set. I would rather state the direction than argue the motive.

---

## 3. What reproduces before anything changes

Nothing below is new. It is here because a measurement that is not comparable to the one it claims to supersede is not a measurement of anything.

**[E, measured this session. Overture `2026-08-19.0` re-extracted from the public S3 bucket, DuckDB 1.5.5, same bbox and tooling.]**

| Figure | `venue-index-remediation.md` | This session | Match |
| --- | --- | --- | --- |
| All places in UK bbox | 3,325,607 | **3,325,607** | exact, third session running |
| `truth.json` — the 139-venue venue→row resolution | — | **byte-identical** to the committed file | exact |
| FSA in-radius counts, Manchester / Chorlton / Ludlow | 828 / 117 / 48 | **828 / 117 / 48** | exact, live API, three days later |
| Top-five hit rate, Manchester, scope B, perfect fix | 53.1% | **53.1%** | exact |
| Modal rank-1 share, Manchester, σ = 25 m, R2 β = 20 | 0.67 | **0.67** | exact |
| Modal rank-1 share, Manchester, σ = 25 m, R0 baseline | 0.31 | **0.31** | exact |
| Single-identity, Manchester, σ = 25 m, **full stack without name search** | 81.6% | **81.6%** | exact |
| Single-identity, Manchester, σ = 25 m, **oracle name search** | 100.0% | **100.0%** | exact |
| Single-identity, Manchester, σ = 50 m, oracle | 98.0% | **98.0%** | exact |

**The 81.6% floor and the circular 100% are the two numbers this note is measuring between, and both reproduce to the digit.** Everything in §6 is therefore directly comparable to them.

**Reproducibility discipline.** `nameseach.py` was run three times in separate processes under `PYTHONHASHSEED` 0, 1 and 7 and the outputs diff byte-for-byte, and identically to the unseeded run [E, measured]. That check exists because the previous note records an irreproducibility defect of exactly this kind, and because §9 records that one instance of it survived in the committed harness.

---

## 4. Part A — does a typed name retrieve the right row?

**Method.** For each of the **101** scored venues that have at least one scope-B row the ground truth says *is* that venue: run every generated query through FTS5, keep hits within 250 m of the venue's FSA position, rank by distance, and ask whether a true row appears in the first twenty. Venues with no scope-B row are excluded here — name search cannot retrieve what is not there — and are handled separately at §5.4.

**[E, measured, `nameseach.py`. Scope B, radius 250 m, list of 20, AND-of-prefixes. Denominators are query *instances*: a venue can carry two `T1_full` strings where stage 1 recovered a trading name as well as a registered one.]**

| Query variant | What the user typed | Instances | Retrieved | Rate |
| --- | --- | --- | --- | --- |
| `T1_full` | the whole registered name | 104 | 79 | **76.0%** |
| `T2_no_article` | without the leading *The* | 32 | 26 | 81.2% |
| `T3_head2` | the first two words | 29 | 23 | 79.3% |
| `T4_head1` | the first word | 79 | 76 | **96.2%** |
| `T5_longest` | the memorable word | 16 | 15 | 93.8% |
| `T6_no_generic` | trade and locality words dropped | 9 | 6 | 66.7% |
| `T7_prefix4` | **four characters** | 76 | 75 | **98.7%** |
| **ANY variant** | | **101 venues** | **100** | **99.0%** |
| — Manchester | | 36 | 35 | 97.2% |
| — Chorlton | | 34 | 34 | 100.0% |
| — Ludlow | | 31 | 31 | 100.0% |

**The finding inside this table is not the 99%.** It is the spread between 76.0% and 98.7%: **the longer and more official the string a user types, the less likely it is to find their pub.** A user who types the name on their hygiene certificate fails a quarter of the time; a user who types four letters fails once in eighty. §5.3 shows this effect is concentrated exactly where it should be if it is real — on the venues whose two names actually differ.

---

## 5. Should this be believed? The contamination analysis

This is the part of the note I would read first if someone else had written it.

### 5.1 The search is not a dragnet

If a typed query returned most of the neighbourhood, retrieving a true row would be no achievement — it would be the oracle wearing a tokeniser. It does not.

**[E, measured, `nameseach_checks.py` C1. 470 typed queries against 2,824 scope-B rows in the three areas.]**

| | Median | p90 | Max | Returned nothing |
| --- | --- | --- | --- | --- |
| **FTS5 hits within 250 m per typed query** | **1** | 1 | 24 | **29.8%** |
| Distance-only candidates within 250 m (what the oracle effectively saw) | **61** | 215 | 264 | — |

A typed query returns a median of **one** row where the distance path returns **sixty-one**. Nearly a third of queries return nothing at all. **The search is sixty times more selective than the thing it replaces**, which is what makes a hit informative rather than automatic.

### 5.2 Where the circularity is *not* broken, and the check that failed to reassure me

I intended to stratify retrieval by the `name_sim` score that put each row in the truth set, on the theory that the weak-similarity stratum near the 0.72 threshold would be the uncontaminated one. **That check came back degenerate and I am reporting it as a failed check rather than quietly dropping it.**

**[E, measured, `nameseach_checks.py` C2.]** The similarity distribution over the 101 matched venues is **median 1.000, p25 1.000, minimum 0.909**. There is no weak stratum. The 0.72 threshold in `match.py` never binds: `name_sim` strips generic trade words and then credits token containment at 0.95, so it collapses to something close to *"shares its distinctive token"* and is near-binary in practice.

**So the honest statement of the residual is stronger than the one I made yesterday, not weaker.** `venue-index-remediation.md` §6.4 said the matcher and the simulation shared a similarity function. The sharper version is: **the ground truth's definition of "this row is this venue" is, in effect, "this row shares the venue's distinctive name token."** A venue present in Overture under a materially different name is not in the truth set at all — it is counted as ABSENT. My queries derive from the FSA string. **The population this experiment measures is therefore selected for name agreement, and the direction of that bias is optimistic.**

Three things are done about it, in increasing order of how much they are worth: §5.3 finds the stratum `name_sim` could not see; §5.4 goes looking in the class the truth set declares empty; §5.5 bounds the damage.

### 5.3 The stratum that does carry information: raw string divergence

`name_sim` cannot discriminate, but the **raw strings** can. Measured with a neutral statistic — lower case, punctuation out, token sets, no generic-word stripping, no containment credit — the FSA string and the nearest true Overture string are:

**[E, measured, `nameseach_divergence.py` E1. n = 101.]**

| | |
| --- | --- |
| Token sets **identical** | 57 (**56.4%**) |
| Token sets **differ** | **44 (43.6%)** |
| Raw token-Jaccard | median 1.00, p25 **0.60**, min **0.00** |

So on nearly half the sample the two strings genuinely differ — and they differ in exactly the ways `venue-index-remediation.md` §6.4 worried about. A sample of what the register and the map call the same premises [E, measured, full list in `nameseach_divergence.txt`]:

| FSA registered name | Overture name | Apart |
| --- | --- | --- |
| `Lane 7` | `Lane7` | 14.9 m |
| `Subway @ EG On The Move` | `Subway` | 4.9 m |
| `Wagamama` | `Wagamama Manchester St Peters Square` | 61.9 m |
| `The Sedge Lynn` | `The Sedgelynn` | 11.4 m |
| `Trof Cafe` | `The Trof` | 15.0 m |
| `The Beeswing Wine Bar & Kitchen` | `The Beeswing` | 19.1 m |
| `Natalie White - The Compasses` | `The Compasses` | 6.3 m |
| `Corbiere's Wine Bar` | `Corbieres` | 7.1 m |
| `The Bowling Green Hotel` | `Bowling Green Chorlton` | 138.0 m |
| `Church Inn` | `The Church Inn` | 7.8 m |

**Retrieval on that divergent stratum is the number that carries information** [E, measured, `nameseach_divergence.py` E4]:

| Raw divergence | Venues | ANY-variant retrieval |
| --- | --- | --- |
| J = 1.00 — identical token sets | 57 | 100.0% |
| 0.50 ≤ J < 1.00 | 29 | **100.0%** |
| J < 0.50 — substantially different strings | 15 | **93.3%** |

And per variant, **on the divergent venues only** — this is the table I would put in front of whoever writes the search:

| Variant | Instances | Retrieved |
| --- | --- | --- |
| `T1_full` — the whole registered name | 44 | **50.0%** |
| `T2_no_article` | 15 | 66.7% |
| `T3_head2` | 13 | 53.8% |
| `T4_head1` — the first word | 36 | 91.7% |
| `T5_longest` | 9 | 88.9% |
| `T6_no_generic` | 4 | 25.0% |
| `T7_prefix4` — **four characters** | 35 | **100.0%** |

**Read that as the build instruction it is.** Where the two names differ, typing the whole official name is a coin flip and typing four letters never failed in this sample. A whole-string or exact-match name search would throw away most of the benefit this note measures. **The search must be incremental and prefix-based**, and that finding does not depend on the contested truth definition at all — it is a comparison *within* the contaminated population, so the contamination cancels.

### 5.4 The class the ground truth declares empty

The contamination's real cost is invisible venues: present in Overture under a name my matcher rejected, so recorded as ABSENT. I went looking for them by hand, which is the only instrument available.

**Method.** For each of the **33** scored venues with no scope-B truth row, print every FTS5 hit from every variant within 250 m, and read them [E, measured, `nameseach_absent.py` D1; full output in `nameseach_absent.txt`]. **Twenty-one returned nothing from any variant**, which is consistent with genuine absence. Of the twelve that returned something, my adjudication, listed individually so a reader can disagree item by item:

| Venue | Retrieved row | Verdict |
| --- | --- | --- |
| `Rudy's Pizza Limited also T/as Rudy's Home Bake Kitchen` | `Rudy's Pizza Napoletana`, 13.6 m, via the stage-1 trading-as recovery `rudys pizza` | **Is the venue.** A genuine rescue the truth set could not grant |
| `Area` | `Areamanchester`, 25.9 m, `music_venue`, via `area` | **Probably the venue** |
| `Whalley Range Amateur Football Club` | `Kings Road - Whalley Range AFC`, 125.9 m | Uncertain — a ground, 126 m away |
| `Tops Restaurant` | `Tops Buffet City`, 171 m | **Not the venue.** The baseline hand-forced exactly this match to a miss |
| The remaining eight | `ludlow` → five Ludlow restaurants; `manchester` → five Manchester bars; `coffee` → five coffee shops; `street`, `do`, `bar`, `choc`, `factory` similar | **Not the venue.** Generic-token dragnets |

**Two genuine rescues out of thirty-three.** That is a small, real, non-circular gain — and note *which* two: one comes from the trading-as rule, i.e. from modelling the FSA's own naming artefact, which is the part of the generator that had the most reason to be useful and the least reason to work by accident.

**It also produces the finding at §8.1**, because eight of those twelve are a user typing a generic word and getting a list of the neighbourhood.

### 5.5 The bound

Suppose both probable rescues are venues that really are in the index under a name the user would never type. They would then split between a distance hit and a self-created venue, and fail the single-identity metric. Both are in Manchester, which scores 49 venues.

**Worst case: the Manchester single-identity figure falls by 2/49 = 4.1 pp, from 100.0% to 95.9%** [E, measured, `nameseach_divergence.py` E3]. **That is still above the 95% bar.** It is the tightest bound I can put on the residual contamination, and it is a bound, not an estimate: it assumes every case I adjudicated as a rescue is instead a failure.

### 5.6 What a real sign-name source would have added, since I still do not have one

The experiment I specified yesterday wanted three name sources per venue. I have one. **What the missing two would test is the class §5.2 describes and §5.4 can only sample by hand**: a venue whose shopfront says something the register does not. `The Sedge Lynn` / `The Sedgelynn` and `Trof Cafe` / `The Trof` show that class exists inside the FSA-to-Overture divergence; what I cannot see is the part of it that lies outside both. **Photographing or listing thirty shopfronts in one of the three areas would settle it**, it is an afternoon, and it is the first item in §10.2.

---

## 6. Part B — the identity measurement, without the oracle

**Method.** `identity.py`'s simulation of `venue-index-remediation.md` §6.2, **unchanged in every respect** — same 20 visits, same Gaussian jitter, same seeds, same scope B, same clustering, same confirmation prior at β = 4, same name-dedupe, same twenty-row list, same never-auto-select model — except that the name-search branch calls FTS5 with a generated string instead of being handed the answer.

**Three query-choice policies, pre-registered before the first run:**

- **`random`** — one variant drawn uniformly per visit. **The headline.** It is the neutral choice: it neither assumes a persistent user nor a fixed habit.
- **`t1`** — the user always types the full registered name. **The harshest single policy**, and per §4 the worst-performing one.
- **`best`** — the user tries every variant until one works. The ceiling.

**[E, measured, `nameseach.py`. Single-identity % per area; median distinct identities per venue was 1 in every row except where stated.]**

| Design | Manchester | Chorlton | Ludlow |
| --- | --- | --- | --- |
| **σ = 10 m** | | | |
| Full stack, no name search (floor) | 93.9% | 100.0% | 100.0% |
| + name search, **oracle** (circular) | 100.0% | 100.0% | 100.0% |
| + name search, **FTS5 `t1`** | 100.0% | 100.0% | 100.0% |
| + name search, **FTS5 `random`** — headline | **100.0%** | 100.0% | 100.0% |
| **σ = 25 m** — the case Block 4 exists for | | | |
| Full stack, no name search (floor) | **81.6%** | 97.9% | 100.0% |
| + name search, **oracle** (circular) | **100.0%** | 97.9% | 100.0% |
| + name search, **FTS5 `t1`** | **98.0%** | 97.9% | 100.0% |
| + name search, **FTS5 `random`** — headline | **100.0%** | 97.9% | 100.0% |
| + name search, **FTS5 `best-of`** | 100.0% | 97.9% | 100.0% |
| **σ = 50 m** | | | |
| Full stack, no name search (floor) | 34.7% (median 2) | 83.0% | 76.3% |
| + name search, **oracle** (circular) | 98.0% | 97.9% | 100.0% |
| + name search, **FTS5 `t1`** | **89.8%** | 97.9% | 94.7% |
| + name search, **FTS5 `random`** — headline | **93.9%** | 97.9% | 94.7% |
| + name search, **FTS5 `best-of`** | 100.0% | 97.9% | 100.0% |

**The headline, stated plainly: at σ = 25 m in a dense city centre the non-circular figure is 100.0%, identical to the oracle.** The 81.6–100% range resolves to its top, and it does so under the *neutral* policy, not the generous one — the harshest single policy still gives 98.0%.

**Why `random` beats `t1`, because it looks wrong and is not.** Over twenty visits the user only needs a typed name to work **once**: that confirmation enters the prior, the prior raises that venue in the distance-ranked list thereafter, and the name path is never needed again. A user who varies what they type gets twenty independent attempts with different strings; a user who types the same failing string gets one attempt twenty times. **The bootstrapping problem §5.2 of the previous note identified is solved by the first success, not by the average one.** That is a property of the design, not of my policy choice, and it is why the name path matters more than its per-query hit rate suggests.

**The hard subset.** Venues absent from Overture pass the single-identity metric by consistently creating one local venue, which is a correct venue page but not a dataset hit. Restricted to the **101 venues that do have a scope-B row** [E, measured, `nameseach_checks.py` C4, σ = 25 m]:

| Design | Manchester | Chorlton | Ludlow |
| --- | --- | --- | --- |
| Floor, no name search | **75.0%** | 97.1% | 100.0% |
| Oracle (circular) | 100.0% | 97.1% | 100.0% |
| FTS5 `t1` | 97.2% | 97.1% | 100.0% |
| FTS5 `random` — headline | **100.0%** | 97.1% | 100.0% |

**The headline is not being carried by the absent venues.** On the harder subset the floor is lower (75.0%) and the result is the same.

**The one Chorlton failure, named.** Chorlton's 97.9% is a single venue, `Beech Inn`, and it fails for a reason that is an artefact of the ground truth rather than of the design: `identity.py` builds its truth set directly from `truth.json` and does **not** apply the `FALSE_MATCH` overrides that `hitrate.py` applies, so `Beech Inn` is credited with two rows — the real pub at 96.6 m and `Beech Road Cafe` at 31.2 m, which the baseline hand-adjudicated as a wrong match. The user "correctly" picks either, and the metric records a split. **Honouring the hand adjudication takes Chorlton to 100.0%** [E, measured]. I did not change it, because changing it would break comparability with the 81.6% floor, and because the artefact makes the metric harsher rather than softer. It is recorded so nobody reads 97.9% as a design property.

---

## 7. Against the pre-registered 95% bar

### 7.1 First: Block 4 limb (a), as the CTO wrote it, is unchanged and still fails

> *"the spike passes if the modal rank-1 share in a dense city centre exceeds 0.8 at σ = 25 m and top-five recall exceeds 80%."* [`subscription-sizing-note.md` §8.2, §11]

| Limb | Bar | Yesterday | **Today** | Result |
| --- | --- | --- | --- | --- |
| Modal rank-1 share, Manchester, σ = 25 m | > 0.80 | 0.67 | **0.67** | **FAIL** |
| Top-five recall, Manchester | > 80% | 53.1% | **53.1%** | **FAIL** |

**Identical to the digit, because name search acts on neither quantity.** It changes what happens when the distance-ranked list fails; it does not reorder that list and it does not lengthen it. **Nothing in this note is an argument that limb (a) as written has been met, and the good result at §7.2 must not be read as one.**

### 7.2 The bar I pre-registered, and the result against it

The bar is mine, from `venue-index-remediation.md` §8.4, written before this measurement existed and while I did not know whether I could clear it. I am bound by it as written.

**[E, measured. Scope B, clustered, β = 4, twenty-row list, headline `random` policy.]**

| # | Criterion | Threshold | Yesterday's honest range | **Measured today** | Result |
| --- | --- | --- | --- | --- | --- |
| **P1** | Single-identity rate, dense centre, σ = 25 m, ≥ 20 visits | **≥ 95%** | 81.6–100%, straddling | **100.0%** (t1: 98.0%; adverse bound: ≥95.9%) | **PASS** |
| **P2** | P1 at 40 visits must not fall more than 2 pp below P1 at 3 visits | ≤ 2 pp | — | **0.0 pp** | **PASS** |
| **P3** | Recall of a neighbour within 100 m must be within 2 pp of the prior-disabled design | ≤ 2 pp | 0.0 pp | **0.0 pp** (75.0% with and without, Manchester, L = 20) | **PASS** |
| **P4** | Single-identity rate at σ = 50 m | ≥ 90% | — | **93.9%** headline; **89.8%** on `t1` | **MARGINAL PASS** |

**P2 in full** [E, measured, `nameseach_checks.py` C6, σ = 25 m, headline policy] — single-identity % by visits per venue, against the as-specified design's collapse from 30.6% to 2.0%:

| Visits per venue | 3 | 6 | 12 | 20 | 40 |
| --- | --- | --- | --- | --- | --- |
| Manchester | 100.0% | 100.0% | 100.0% | 100.0% | **100.0%** |
| Chorlton | 97.9% | 97.9% | 97.9% | 97.9% | 97.9% |
| Ludlow | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

**Flat, non-circularly, from three visits to forty.** P2 was the criterion I said I would fight for if I could keep only one, and it is the one the oracle was least likely to be flattering, because the oracle's advantage does not grow with use.

**P4 is a marginal pass and I am reporting the margin, not the pass.** 93.9% headline against a 90% bar is comfortable; 89.8% on the harshest single policy is a fail by 0.2 pp. The honest summary is that at σ = 50 m the design depends on the user varying what they type, and I have no evidence about whether real users do.

### 7.3 The two conditions, which are not optional

**[E, measured, `nameseach_checks.py` C5, σ = 25 m, single-identity %.]**

| Configuration | Manchester | Chorlton | Ludlow |
| --- | --- | --- | --- |
| **AND, twenty-row list** — headline | **100.0%** | 97.9% | 100.0% |
| OR, twenty-row list | 100.0% | 97.9% | 100.0% |
| **AND, five-row list** | **93.9%** | 95.7% | 97.4% |
| OR, five-row list | 91.8% | 97.9% | 94.7% |

1. **The list must be long, or typing must reach a long list.** At five rows the headline falls to 93.9% and **P1 fails**. This is the same conclusion `venue-index-remediation.md` §7 and §9.4 reached from a different direction, and it is now the binding constraint on the pass rather than a recommendation. The resolution §9.4 sketched — a short list by default with typing as the path to the long one — is supported by these numbers, and it is the UX seat's and the PM/BA's to make, not mine.
2. **The search must be prefix-based, not whole-string.** §5.3: on divergent names, four characters retrieves 100% and the full registered name retrieves 50.0%. A search implemented as exact or whole-string matching would not deliver the result in §6 and the bar would not be met.

**Neither condition costs anything the CTO has not already scoped.** FTS5 prefix queries are the ordinary use of FTS5; the list length is a UI constant.

### 7.4 I passed a bar I wrote, which is the situation that deserves the most suspicion

`venue-index-remediation.md` §8.2 records that I set the 0.8 rank-1 bar, failed it, and proposed a different bar — and that I could not clear myself of the charge that the substitution was convenient. **Today I have cleared the substituted bar.** That makes the charge worse, not better, and the only useful response is to make the result checkable rather than to argue about my motives:

- **The bar was published before this measurement existed**, in a committed file, with its justification, and I have not touched it.
- **The pass does not depend on the substitution.** The floor it improves on — 81.6% — and the oracle it matches — 100% — are both in the published note, and this measurement lands on the oracle.
- **The result against the bar I did *not* substitute is reported first**, at §7.1, and it is a fail.
- **The adverse bound at §5.5 assumes I am wrong about every case I adjudicated**, and still passes.
- **Everything is re-runnable in about fifteen minutes** (§11), including by someone who thinks the generator is rigged: `namegen.py` is 180 lines, half of them comment, and reads one field of one file.

**If the PM/BA, UX and QA decline the substitution and hold me to the 0.8 rank-1 share, the answer remains that the remediation failed.** That was true yesterday and it is true today. What has changed is only this: the reason I gave for being unable to demonstrate a pass on the proposed bar no longer exists.

---

## 8. What remains unmeasured, and whether it bears on this result

### 8.1 A new hazard this note introduces, which the previous one did not have

**[E, measured, `nameseach_absent.py` D2.]** Of **304** typed queries that returned anything, the nearest returned row is **not** a true row in **11 — 3.6%**. The examples are not abstract:

| Venue | Typed | Nearest returned row | Apart |
| --- | --- | --- | --- |
| `Castle Lodge Buttery` | `castle` | `Castle Tea Room` | **5 m** |
| `Chorlton Metro Cafe` | `chorlton` | `Wilbraham Bierhaus - Chorlton's Pop up Christmas Bar` | **4 m** |
| `San Carlo Gran Cafe` | `san carlo` | `San Carlo Bottega` | 34 m |
| `Victoria Tap` | `victoria` | `Hipster Burgers MCR Victoria` | 72 m |
| `Bar Pop` | `bar` | `Iconic Bar` | 21 m |
| `Afflecks & Brown` | `afflecks` | `Definitely Maybe Bar Afflecks` | 117 m |

**My simulation assumes the user never picks one of these**, because `identity.py` models the user as picking their own venue whenever it is in the list. That assumption was in the 81.6% floor too, so §6's comparison is fair — but the *absolute* level in §6 and §7 is optimistic by however often a real person, standing outside at 11pm, picks `Castle Tea Room` instead of `Castle Lodge Buttery` five metres away. **I cannot measure that without a user.** [J]

**Two things follow, and they belong to other seats.**
- **QA:** the false-pick rate is a testable acceptance criterion and should be one. A name-search result list must be tested for near-miss confusability, not only for recall.
- **UX:** §5.4 shows the other half of the same problem — typing a generic word (`ludlow`, `coffee`, `bar`, `manchester`) returns a list of the neighbourhood, because the index name contains the locality. A search screen that shows five unrelated cafés when the user types four letters is a worse experience than no search screen, and the mitigation — show distance and category prominently, suppress results that match only on a locality or trade token — is a design decision I am flagging, not making.

### 8.2 The generic-token dragnet, quantified

The one query variant that performs badly, `T6_no_generic` at 66.7% and 25.0% on divergent names, performs badly for an instructive reason: it is the variant most likely to reduce to a single common word. `T4_head1`'s maximum hit count is 24 rows and `T7_prefix4`'s is 20 [E, measured, C1] — both from generic first words. **A four-character prefix is excellent on average and occasionally returns twenty rows**, which is another reason the list has to be able to be long.

### 8.3 The standing limits, and whether they bear on this result

| Limit | Bears on this result? |
| --- | --- |
| **No device, no real `CLVisit` error distribution.** Every σ here is an assumption. | **Yes, decisively — and less than before.** σ = 25 m is where the bar is set and the design passes; at σ = 50 m it passes marginally; at σ = 10 m everything passes. **The important change is that the name path is the one lever whose value *rises* as the location signal worsens**: at σ = 50 m it takes Manchester from 34.7% to 93.9%, a 59-point swing, against 18 points at σ = 25 m [E, §6]. A design that leans on name search is less sensitive to the number nobody has measured, which is an argument for it that does not depend on knowing the number. It remains the highest-value missing fact about this product. |
| **Closed venues are undetectable.** `operating_status` is populated for 322 of 330,208 UK food-and-drink rows [E, prior sessions; 323 in my re-extract]. | **Yes, and it cuts against name search specifically.** A closed venue's row stays in the index and stays *findable by name* — indeed name search will surface a closed venue more reliably than distance ranking would, because the name still matches. Nothing here detects that, and a venue page that keeps offering a pub that shut in 2025 is a defect this measurement cannot see. §10.2 item 3. |
| **No usability testing.** | **Yes.** §8.1 is entirely an assumption about what a person picks from a list. |
| **Three areas, 139 venues, 134 scored.** | **Yes, on resolution.** This sample separates 80% from 95%. It does not separate 98.0% from 100.0%, and I draw no conclusion at that resolution — §7.2's P1 pass rests on the gap to 95%, not on the gap between the policies. |
| **No shopfront or venue-listing name source.** | **Yes.** §5.6. |

---

## 9. A defect in the committed harness

Found by re-running it, reported because the previous note's §1 makes a point of this class of failure and it would be dishonest to let an instance of it stand.

**`falsestick.py` line 45** selects a cluster with `sorted(vid, key=lambda c: 0)[0]`. A sort with a constant key is stable, so it returns the first element in **set-iteration order** — and Python salts string hashing per process. The false-stick column therefore moves between runs: **Chorlton 65.6% or 63.8%, Ludlow 53.0% or 54.7%, depending on `PYTHONHASHSEED`** [E, measured, seeds 0/1/2]. Manchester is unaffected, and the `recall@L` column — the number the §7 finding of the previous note actually turns on — is stable.

**The published figures are the correct ones.** With the defect fixed (`sorted(vid)[0]`), the output reproduces the committed `falsestick.txt` byte-for-byte and is identical under every hash seed [E, measured]. So §7 of `venue-index-remediation.md` stands as written, including the 57.5% false-stick and 75.0%/75.0% recall figures that P3 rests on, which I have re-verified this session.

**What I did and did not do.** I added `falsestick_fixed.py` and left the committed `falsestick.py` untouched, because the harness is the CTO's S1 deliverable in draft and silently editing a published instrument is worse than flagging it. **This is a flag to the CTO, not a block — the Engineer holds none.** The general point is the one the previous note already made and this makes concrete: a regression fixture that is not itself tested for reproducibility is not a fixture. **A `PYTHONHASHSEED`-sweep should be part of S1's own acceptance**, and it costs one line of CI.

---

## 10. Verdict, and what would overturn it

### 10.1 The verdict Block 4 turns on

**Does the remediated design lift Block 4? No — and the reason has moved.**

**Limb (a), as written.** Modal rank-1 share **0.67** against 0.8; top-five recall **53.1%** against 80%. Unchanged, still failing, and untouched by this experiment. §7.1.

**Limb (a), on the identity-denominated bar this seat proposed.** **P1 100.0% against 95%, P2 0.0 pp, P3 0.0 pp, P4 93.9% marginal** — measured without the oracle, with two stated conditions (twenty-row reachable list, prefix search) and one bounded residual (≤ 4.1 pp). §7.2, §7.3. **The measurement the previous note said would settle this has settled it in favour of the design.**

**Limb (b).** Unchanged. `venue-index-remediation.md` §11 restates the five schema criteria as six testable acceptance criteria with schema preconditions. **A criterion drafted by the Engineer is not a criterion in the requirements document.** Prepared; not met; not mine to meet.

**So the honest one-line answer to the commission's question: the remediated design does everything I claimed for it yesterday, and the claim is no longer circular — but whether that lifts Block 4 depends entirely on which bar is in force, and that was never my decision.** Open question 5 of `subscription-sizing-note.md` §12 belongs to the **PM/BA with UX and QA**, Block 4 belongs to the **CTO**, and kill/proceed belongs to the **CEO** under Constitution 5.4. What has changed since yesterday is that all three now have a number instead of a range.

**The one thing I would put in front of the CEO if only one line survived:** the index as specified produces a venue page that holds a single identity for **2.0%** of dense-centre venues after forty visits; the remediated design holds one for **100%**, flat from three visits to forty, measured without the assumption that flattered yesterday's figure, and its decisive component is a search box the CTO has already paid for.

### 10.2 What would overturn this finding, and where I looked

*(Required by `roles/engineer.md` as amended: a negative finding carries a block's duty. §7.1's fail and §9's defect are the negative findings here; the rest is a pass, and a pass carries the same obligation to say what would break it.)*

**Overturned by any of these:**

1. **Thirty real shopfront names, from one of the three areas.** §5.6. This is the experiment I specified yesterday and still cannot fully run: FSA gives me the register's name, not the sign's. **If shopfronts diverge from the register more than the register diverges from Overture, the 43.6% divergence rate at §5.3 is an undercount and the retrieval figures fall.** An afternoon with a phone camera in Chorlton settles it. I looked for a second name source in the data I have — the sample's `postcode` field, the Overture `src` provenance list, the FSA business-type classification — and none of them carries a trading name.
2. **A false-pick measurement that comes back badly.** §8.1. The whole of §6 assumes the user never picks the name-similar wrong venue five metres away. **If a usability test shows people do, the single-identity figures are optimistic by that rate and P1 may fail.** This is the assumption I would attack first if I were the Skeptic, and it is the one I cannot test without a person.
3. **Closed venues.** §8.3. Name search surfaces a closed pub *better* than distance ranking does. Nothing in this note or either prior one can detect one, and a stable venue identity pointing at a shut pub is a stable wrong answer. **If a closure-signal source exists — FSA deregistration diffs are the obvious candidate and I did not test them — it changes the junk picture for the name path specifically.**
4. **A usage model that moves the 95% threshold.** Unchanged from yesterday and still open: §8.4's "40 venues, 100 visits a year" is mine and labelled [J]. I looked again this session for any Candour artifact carrying one and there is still none.
5. **Someone re-running `namegen.py` with different but equally defensible rules and getting a materially lower figure.** The rules are a model of how people type and I did not test alternatives. **The strongest version of this objection is that seven variants per venue is generous** — and §6's `t1` row is the answer to it: one variant, the worst-performing one, still gives 98.0%.

**Where I looked, so a reader can check I looked in the right places:**

- **The whole dataset again.** 3,325,607 rows re-extracted from Overture's public bucket for the third session running, with `truth.json` rebuilt from source and confirmed byte-identical to the committed file.
- **The register, live, at primary.** All 139 sampled venues re-checked against the FSA API this session: none deregistered, no `BusinessName` changed.
- **Both directions of the contamination question.** I measured what the coupling is worth (§5.2, and reported the check that failed), found a stratum where it cancels (§5.3), went looking in the class the truth set declares empty (§5.4), and bounded the damage under the assumption that every judgment of mine is wrong (§5.5).
- **Three query-choice policies and two retrieval policies and two list lengths and three values of σ and five visit counts**, rather than the one configuration that gives the best number.
- **The harness itself, as a thing that might be broken** — which is how §9 exists.
- **My own previous note, treated as a claim to be checked** — including re-verifying the 81.6% floor and the 100% oracle it is measured between, and correcting its account of the circularity at §5.2 in the direction that makes it worse.
- **Where I did *not* look:** I did not visit a venue; did not photograph a sign; did not run anything on a phone; did not measure `CLVisit`; did not test a closure signal; did not test OSM or any supplementary dataset; did not re-retrieve the Overture documentation (the prior notes' retrievals are attributed, not re-cited); did not hand-adjudicate the national clustering; and did not test ranking the name-search results by relevance rather than distance, which is a real design variable I left alone because changing two things at once measures neither.

---

## 11. Reproduction and evidence register

**Everything below was retrieved or measured on 2026-09-21. Nothing is cited from memory.**

**Added to `products/haunt/venue-index-harness/`.** Per the commission I reused the committed harness and **did not modify any committed original**. Everything new is an addition:

| Script | What it does | Section |
| --- | --- | --- |
| `namegen.py` | **the query generator** — FSA-only, frozen, hashed at §2.4 | §2.2, §4 |
| `fts.py` | real SQLite **FTS5** index over scope B and the retrieval policies | §2.3 |
| `nameseach.py` | **the experiment** — Part A per-variant retrieval, Part B identity split with real name search | §4, §6 |
| `nameseach_checks.py` | C1 selectivity · C2 the failed contamination check · C3 name-blind truth · C4 hard subset · C5 policy/list sensitivity · C6 the P2 curve | §5.1, §5.2, §6, §7.2, §7.3 |
| `nameseach_absent.py` | D1 the absent class, hand-read · D2 false-pick exposure · D3 which venues fail | §5.4, §8.1 |
| `nameseach_divergence.py` | E1/E2 raw string divergence · E3 the adverse bound · E4 retrieval by divergence | §5.3, §5.5 |
| `falsestick_fixed.py` | `falsestick.py` with the `PYTHONHASHSEED` defect corrected | §9 |
| `fsa_check.py` | live FSA re-retrieval, written to `fsa_recheck.json` so `fsa.json` is not overwritten | §2.1, §3 |
| `queries.json` | all 491 generated query strings, so a reader can disagree string by string | §2.2 |
| `*.txt` | captured run outputs quoted in this note | all |

Committed scripts re-run unmodified to establish comparability: `extract.py`, `build_work.py`, `match.py`, `hitrate.py`, `stability.py`, `identity.py`, `falsestick.py`. A section was **appended** to the harness `README.md`; nothing in it was altered.

**Re-run order:** `extract.py` → `build_work.py` → `match.py` → `nameseach.py` → `nameseach_checks.py` → `nameseach_absent.py` → `nameseach_divergence.py`. About fifteen minutes on a laptop, of which the Overture extract is fifty seconds. `ovt.duckdb` is derived and not committed.

**Reproducibility.** `nameseach.py` produces byte-identical output under `PYTHONHASHSEED` 0, 1 and 7 and unseeded [E, measured]. Anything re-run from a harness that seeds from Python's built-in `hash()`, or that uses the unfixed `falsestick.py`, will not reproduce these numbers — see §9.

**Data sources**

- **Overture Maps Places**, release `2026-08-19.0`, `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/` — CDLA-Permissive-2.0 / Apache-2.0 depending on source. Extract re-materialised **2026-09-21**; 3,325,607 rows in 49.6 s.
- **[Food Standards Agency, Food Hygiene Rating Scheme API](https://api.ratings.food.gov.uk/Establishments)** (`x-api-version: 2`), retrieved **2026-09-21** — Crown copyright, Open Government Licence. Returned 828 / 117 / 48 in-radius pubs and restaurants, matching both prior spikes, and confirmed all 139 sampled `BusinessName` values unchanged. **This is the query source and it is the single most load-bearing external retrieval in this note.**
- **[Overture Maps — Places guide](https://docs.overturemaps.org/guides/places/)** — **not retrieved this session.** Every claim resting on it (the provider list, the absence of OSM, the duplicate and junk-rate statements, the GERS churn warning) is attributed to `venue-index-spike.md` §3/§11 and `venue-index-remediation.md` §10/§13, which retrieved it on 2026-09-18 and 2026-09-20 respectively. Flagged rather than re-cited, per the evidence standard's prohibition on citing from memory.

**Figures travelling from other Candour artifacts, attributed and not re-derived by me**

- `products/haunt/venue-index-remediation.md` §6.2, §6.4, §7, §8.1–§8.5, §12, §14.2 — the 81.6% floor, the circular 100%, the P1–P4 bar, the false-stick protocol, the FTS5 bundle cost, and the commission for this experiment. The floor, the oracle and the P3 figures were re-derived here; the size figures were not.
- `products/haunt/venue-index-spike.md` §3, §4.3 — the FSA independence argument and the FSA naming limitations. Re-checked at source for currency (§2.1); the provider-list argument is attributed, not re-retrieved.
- `products/haunt/subscription-sizing-note.md` §8.1, §8.2, §11, §12 — Block 4 and both limbs, the S1 regression fixture, open questions 5 and 6.
- `products/haunt/feasibility-note.md` §2, §2.6, §3, §5 — the index specification under test, the no-server/no-backfill facts.
- `products/haunt/ux-note.md` §2.2, §2.3 — never auto-select; merge, sticky choice, rename.
- `products/haunt/android-and-stack-note.md` §3.2 — FTS5 already inside row 5.
- Apple `CLVisit` accuracy — **not retrieved by anyone, still.** §8.3.

**Looked for and did not find**

- **A second name source per venue.** §5.6, §10.2 item 1. The sample carries a postcode and a business type and no trading name; Overture's `src` column carries provider names, not venue names.
- **Any Candour artifact carrying a usage model.** Third time of asking by this seat; still none.
- **Any published `CLVisit` horizontal-accuracy figure.** Unchanged.

**Related-party disclosures.** None.

---

## 12. Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | Created under `venue-index-remediation.md` §14.2 item 1. **Breaks the name-search circularity** by generating query strings from the FSA register alone, through a frozen hashed generator that never reads Overture, and retrieving with a real FTS5 prefix search rather than the matcher that built the ground truth. **Resolves the 81.6–100% range to 100.0%** at σ = 25 m in a dense centre (98.0% on the harshest policy, ≥95.9% under adverse reclassification). **Passes the pre-registered P1 ≥ 95%, P2 ≤ 2 pp and P3 ≤ 2 pp; marginal on P4.** Reports **two binding conditions** — a twenty-row reachable list and prefix rather than whole-string search — and the finding that typing the full registered name retrieves a divergently-named row only 50.0% of the time against 100% for four characters. **Reports that Block 4 limb (a) as written is untouched and still fails at 0.67 / 53.1%.** Records the contamination check that came back degenerate and states the residual more harshly than the previous note did. **Raises a new hazard**: 3.6% of typed queries put a name-similar wrong venue first. **Flags a `PYTHONHASHSEED` defect in the committed `falsestick.py`**, confirms the published figures are nonetheless correct, and adds a fixed copy without touching the original. External source retrieved 2026-09-21: FSA FHRS API. **Not a certification.** |

---

*Prepared by the Engineer seat under `roles/engineer.md` as amended. This note prepares and flags; it does not certify (Constitution 6.1). The Engineer holds no block: Block 4 is the CTO's, only the CTO may lift it, and only the CEO may overrule it (Constitution 5.6). The pass criterion is open question 5 and belongs to the PM/BA with UX and QA. Kill/proceed is the CEO's alone (Constitution 5.4), and nothing in this note pretends otherwise.*

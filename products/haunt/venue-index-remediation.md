# Venue-index remediation spike — Haunt

**Seat:** Engineer · **Date:** 2026-09-20 · **Commissioned by:** `products/haunt/subscription-sizing-note.md` §8.2 and §11 (**Block 4**), sized there at 3 weeks / 113 h
**Baseline:** `products/haunt/venue-index-spike.md` (Engineer, 2026-09-18). This note is the remediation of that note's verdict and reuses its ground truth, its sample and its metrics so the numbers are comparable.
**Status:** build-gating artifact. **Prepares and flags; does not certify** (Constitution 6.1). Block 4 is the CTO's and only the CTO may lift it; only the CEO may overrule it (Constitution 5.6). Kill/proceed is the CEO's (Constitution 5.4).
**Template note:** `pipeline/templates/` has no spike template. Structure follows the six items the commission names, plus the verdict and the overturn clause my amended charter requires. The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Everything marked **[E, measured]** is a measurement I ran in this session; the method is stated at the point of use and every script is listed in §13 so a stranger can re-run the chain. Retrieved documents carry their links and were retrieved **2026-09-20**. Nothing is cited from memory.

---

## 0. Summary and verdict

**Verdict: the remediation does NOT lift Block 4, and I am not going to claim it does.** It fails limb (a) on the numbers limb (a) actually names. It also produces, on a different metric, the best result in either spike — and I think that metric is the right one. Both of those statements are true at once, and the gap between them is a question about the bar, which is **open question 5** and belongs to the PM/BA with UX and QA, not to me.

Eight findings.

1. **The baseline's working material was gone and I rebuilt it from scratch.** The previous session's scratchpad no longer exists on this machine. I re-extracted Overture, re-retrieved the FSA ground truth and rebuilt every script. **The rebuild reproduces the baseline to the unit on eleven independent figures** — 3,325,607 extracted rows, 2,900,349 named at confidence ≥ 0.5, all four category sub-counts, 302,820 food-and-drink, 209,570 null-taxonomy, 1,022 `inn` rows, and the FSA counts 828 / 117 / 48 — and reproduces its headline hit rate and instability measurements within sampling noise. §1, §2.
2. **Widening the category scope does not fix the dense city centre, and the measurement contradicts what both the baseline and the CTO expected of it.** The baseline called it *"the most useful thing in this spike"* and the CTO sized it as S2. Measured: in Manchester the top-three rate goes **40.8% → 38.8%** and the median candidate count goes **164 → 185**. Every venue it recovers also becomes a row in front of somebody else's answer. It is a real gain in a small market town (Ludlow top-three **73.7% → 81.6%**) and a wash-to-negative where people actually go out. §4.
3. **Spatial clustering of near-duplicate rows does almost nothing for stability.** Modal rank-1 share in Manchester at σ = 25 m: **0.31 → 0.30**. The instability is not duplicates of the same pub; it is *different pubs* inside the location error. Merge is still required — for the reason the UX seat gave — but it is not the identity fix. §5.
4. **The user's own confirmation history, used as a ranking prior, is a real fix and is not sufficient alone.** It lifts Manchester modal rank-1 share from **0.31 to 0.67** at σ = 25 m. That is still under the CTO's 0.8. §5.
5. **The metric everyone has been using is the wrong one, and I can now show it rather than assert it.** Rank-1 churn is a proxy. The thing that corrupts a venue page is **how many distinct Candour venue identities one real pub accumulates**. Measured directly: as specified, at σ = 25 m in Manchester, a pub accumulates a **median of 5 identities over 20 visits and 4.1% of pubs keep a single one**. Worse, **it compounds with use** — 30.6% single-identity at 3 visits per venue, **2.0% at 40**. The product degrades exactly as the user accumulates the history that is supposed to be the product. §6.
6. **The full remediation stack fixes that metric — and its headline number is overstated by an amount I can bound but not measure.** Widened scope + clustering + confirmation prior + a 20-row list + **name search on the "isn't listed" path** gives **100% single-identity in Manchester at σ = 25 m, 98.0% at σ = 50 m**, flat from 3 visits to 40. The single largest contributor is the name search, which the CTO already carries as FTS5 inside row 5. **But my simulation decides a typed name matches an index row using the same similarity function that built the ground truth, so that 100% is circular and is an upper bound. The non-circular floor is 81.6%.** One day's work closes the gap. §6, §8.5, §14.2 item 1.
7. **The "user goes next door" hazard the CTO and UX both named is real at rank 1 and harmless in outcome — because the design never auto-selects.** With the prior on, a previously-confirmed neighbour takes rank 1 on **57.5%** of visits to the pub next door. But recall of the correct neighbour at a 20-row list is **75.0% with the prior and 75.0% without it** [E, measured]. The prior costs nothing in correctness and a scroll in presentation. **This is conditional on two things being requirements, not preferences: never auto-select, and a list long enough to absorb a wrong first row.** §7.
8. **Size does not constrain any of this.** The widened index is **26.8 MB on disk / 13.7 MB gzipped**, against 23.8 / 12.0 for the baseline scope — **+12.6%** on a 4 GB build limit. The permissive scope that adds every null-taxonomy row is 43.0 MB, and it is the one scope I recommend against, on precision rather than size. §12.

**What this means for Block 4.** Limb (a) asks for **modal rank-1 share > 0.8 and top-five recall > 80%** at σ = 25 m in a dense city centre. I measured **0.67 and 53.1%**. That is a fail on both, and §8 reports it as a fail before it argues anything. §8 then argues that limb (a) measures list position when the block is about identity, proposes a bar on identity instead, and hands the choice to the seats that own it. Limb (b) — the five schema criteria in the requirements and in the schema — I have restated as testable acceptance criteria at §11, but a criterion I have written is not a criterion the PM/BA has accepted, so limb (b) is prepared and not satisfied.

**What would overturn this verdict, and where I looked: §14.**

---

## 1. A finding about this spike's own inputs, stated first

The commission told me my working material was on disk from the first spike, at a named path, and to check it was intact and reuse it rather than re-download the Overture extract.

**It is not there.** The session directory `.../e9c108bc-1975-46bd-9dae-0fbe12d4a0bd/scratchpad/` does not exist. I searched the filesystem for each named artefact by name — `ovt.duckdb`, `uk_places.parquet`, `results_*.json`, `query.py`, `sample.py`, `match.py`, `stability.py`, `recall_noise.py`, `occupancy.py`, `tradeoff.py` — across `/private/tmp`, `/tmp`, `/var/folders` and the user's home directory. The only hit was an unrelated file of the same name inside a Python package cache. **The working material of the first spike is gone.** [E, measured — filesystem search, 2026-09-20]

So I rebuilt it. That cost the first part of this spike and it produced something worth having: an independent reproduction of the baseline, described at §2, rather than a continuation of it.

**This is the second time in four days that a Candour measurement has lived only in a session scratchpad.** The CTO already named the consequence — *"The spike built one and it lives in a session scratchpad. Without it, no future change to the index can be shown not to have made things worse"* [E, `subscription-sizing-note.md` §8.1] — and put a permanent regression fixture at the top of the spike decomposition as S1. **S1 is not optional and it is not a nice-to-have; it is the difference between this spike being repeatable and this spike being repeated.** Every script behind this note is listed in §13 and they belong in the product repository, not in `/tmp`. I am raising this to the CTO and the PM/BA as a scope item, not building through it.

One defect in my own rebuild, found and fixed mid-spike and recorded because it bears on whether anyone can trust a re-run: my first simulation harness seeded its random number generator from Python's built-in `hash()` of a tuple of strings, which is **salted per process**. Two runs of the same configuration differed by up to 6 percentage points. It is fixed (`harness.stable_seed()`, an MD5-derived seed), and **every number in this note comes from the fixed version, verified by running the identity simulation twice in separate processes and diffing the output byte-for-byte** [E, measured].

---

## 2. The rebuild, and what it reproduces

Method: DuckDB 1.5.5 with `httpfs` and `spatial`, reading `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/*.parquet` anonymously, filtered on `bbox.xmin BETWEEN -8.65 AND 1.77 AND bbox.ymin BETWEEN 49.86 AND 60.86` — the same release, bbox, tooling and tool version the baseline and `feasibility-note.md` §2 name. 3,325,607 rows materialised locally in 52 s.

**[E, measured this session. "Baseline" is `venue-index-spike.md`; "CTO" is `feasibility-note.md` §2.3 as corrected.]**

| Measure | Baseline / CTO | This session | Match |
| --- | --- | --- | --- |
| All places in UK bbox | 3,325,607 | **3,325,607** | exact |
| Named, confidence ≥ 0.5 | 2,900,349 | **2,900,349** | exact |
| — `categories.primary = 'pub'` | 42,407 | **42,407** | exact |
| — `cafe` | 33,215 | **33,215** | exact |
| — `restaurant` | 22,886 | **22,886** | exact |
| — `coffee_shop` | 19,875 | **19,875** | exact |
| `taxonomy.hierarchy[1] = 'food_and_drink'`, named, conf ≥ 0.5 | 302,820 | **302,820** | exact |
| Named rows at conf ≥ 0.5 with **no taxonomy at all** | 209,570 | **209,570** | exact |
| `cat_primary = 'inn'`, named, conf ≥ 0.5 — all under `lodging` | 1,022 | **1,022** | exact |
| FSA pubs + restaurants in radius: Manchester / Chorlton / Ludlow | 828 / 117 / 48 | **828 / 117 / 48** | exact |
| Seeded stratified draw per area | 50 / 48 / 41 = 139 | **50 / 48 / 41 = 139** | exact |
| `operating_status` populated, UK food-and-drink | 322 | **323** | −1 row |
| Shipped index size, minimal schema | 23.3 MB / 11.3 MB gz | **23.8 MB / 12.0 MB gz** | same order |

Eleven figures to the unit, including the ground-truth counts from a live statutory API two days later. The one-row difference on `operating_status` and the 2% difference on gzipped size are of no consequence and are recorded rather than smoothed. **The baseline's measurements were made correctly, and this note builds on them rather than re-litigating them.**

**What is reproduced on the headline metrics** (scope A = the index exactly as `feasibility-note.md` §2 specifies it):

| | Baseline | This session |
| --- | --- | --- |
| Top-three hit rate, all areas, perfect fix | 53.0% | **50.7%** |
| Top-five hit rate, all areas | 58.3% | **61.2%** |
| Rank-1 hit rate, all areas | 34.1% | **35.8%** |
| Manchester top-three | 47.9% | **40.8%** |
| Median candidates within 250 m, Manchester | 171 | **164** |
| Manchester σ = 25 m: median distinct rank-1 venues over 20 visits | 10 | **9** |
| Manchester σ = 25 m: mean modal rank-1 share | 0.27 | **0.31** |
| Manchester σ = 25 m: venues whose rank 1 changed at least once | 100.0% | **100.0%** |

[E, measured. n = 134 scored venues here against the baseline's 132.]

**The differences are sampling noise and one methodological difference I am naming rather than burying.** The baseline hand-adjudicated all 653 returned candidate rows. I hand-adjudicated the 139-venue match list (§3) but scored the returned lists with an automated matcher. The baseline recorded that its own automated matcher disagreed with its hand adjudication on 15 of 139 cases in both directions, so **my hit rates carry roughly that much uncertainty and should not be read to a resolution finer than a few points.** Nothing in this note turns on a few points of hit rate; the findings that matter are 0.31 versus 0.67, and 4.1% versus 100%.

---

## 3. Ground truth and the matcher — what I changed and why

**Source: the Food Standards Agency's Food Hygiene Rating Scheme open API** (`https://api.ratings.food.gov.uk/Establishments`, `x-api-version: 2`, retrieved 2026-09-20) [E]. Same source, same three areas, same radii, same seeded stratification (`random.seed(20260918)`, up to 25 `Pub/bar/nightclub` and up to 25 `Restaurant/Cafe/Canteen` per area) as the baseline, and it returns the same counts. All four limitations the baseline names — address-derived geocodes, legal trading names, premises nobody goes out to, and FSA being fresher than an Overture release — apply here unchanged and are not restated.

**The matcher is mine and it is the weakest instrument in this note.** A first version, thresholded at 0.62 on a name-similarity score, matched `Lion's Den` to `Giovanni's Deli` and `Tops Restaurant` to `Tops Buffet City` 171 m away. I tightened it: locality words and generic trade words (`bar`, `cafe`, `manchester`, `chorlton`, …) are stripped before comparison; a containment match is only credited when the shorter name carries two distinctive tokens or one of six or more characters; and a weaker name match is only accepted when the row is also within 150 m. I then **read the resulting 139-row match list by hand** and recorded every override in `handscores.py`, individually, so a reader can disagree item by item:

- **Excluded, not venues a person goes out to:** `Addleshaw Goddard` (a law firm's staff canteen), `Manchester Civil Justice Centre` (court canteen), `Monkey Mania` (soft play), `Working Together (Ludlow) Ltd Cafe` (a disability-services community café). The last two are the same exclusions the baseline made.
- **Excluded, ambiguous:** `3 Church Street` (an FSA record whose business name is its address — the baseline excluded this one too), `The Chorlton Green` (matches `Chorlton Green Brasserie` 78 m away; I could not establish whether they are the same premises).
- **Forced to a miss, automated match judged wrong:** `Beech Inn` → `Beech Road Cafe` 31 m away (a café, not the pub); `Luna` → `Luna Manchester`, a clothing shop 366 m away; `San Carlo Gran Cafe` → `San Carlo - Manchester`, a different branch of the same group 398 m away.
- **Reported but not excluded,** as the baseline did: the four sports and social clubs (`South West Manchester Cricket Club`, `Whalley Range Amateur Football Club`, `West Didsbury & Chorlton AFC`, `The Ludlow Club`).

**134 venues scored** of 139 drawn.

**One piece of independent confirmation worth recording.** The baseline diagnosed specific venues as lost to the category filter and named them. My rebuilt matcher, run against the widened scopes, recovers precisely those venues and no others by that route: `Church Inn` (7.8 m, `inn` under `lodging`), `The Charlton Arms` (97.0 m, `inn`), `Vine & Juniper` (1.9 m, `liquor_store` under `shopping`), `Grosvenor Casino` (12.0 m, `casino` under `arts_and_entertainment`) all enter at scope B; `The Ludlow Club` (21.8 m) and `South West Manchester Cricket Club` (4.3 m) are null-taxonomy rows and enter only at scope C. **The baseline's diagnosis of the category defect was exactly right.** §4 is about what fixing it is worth, which is a different question and has a different answer.

---

## 4. Candidate 1 — widening the category scope. It works where it is not needed.

### 4.1 The three scopes

| Scope | Definition | Named rows at conf ≥ 0.5 |
| --- | --- | --- |
| **A** | `taxonomy.hierarchy[1] = 'food_and_drink'` — the index exactly as `feasibility-note.md` §2 specifies it | 302,820 |
| **B** | A **or** an explicit allow-list of 32 `cat_primary` values Overture files outside that hierarchy but which are plainly going-out venues: `inn`, `casino`, `social_club`, `comedy_club`, `dance_club`, `music_venue`, `karaoke`, `theatre`, `cinema`, `stadium_arena`, `bowling_alley`, `pool_billiards`, `liquor_store`, … (full list in `scopes.py`) | **336,103** (+11.0%) |
| **C** | B **or** every named row carrying **no taxonomy at all** — the 209,570 rows invisible to any hierarchy filter | **545,673** (+80.2%) |

### 4.2 Top-N hit rate by scope, at a perfect location fix

**[E, measured. n = 134. Radius 250 m, ordered by great-circle distance, exactly as the baseline queried it.]**

| Scope | Area | n | Rank 1 | Top 3 | Top 5 | Median candidates in 250 m |
| --- | --- | --- | --- | --- | --- | --- |
| **A** | Manchester | 49 | 20.4% | **40.8%** | 51.0% | **164** |
| **B** | Manchester | 49 | 20.4% | **38.8%** | 53.1% | **185** |
| **C** | Manchester | 49 | 20.4% | **38.8%** | 49.0% | **241** |
| **A** | Chorlton | 47 | 25.5% | 42.6% | 61.7% | 32 |
| **B** | Chorlton | 47 | 23.4% | 40.4% | 61.7% | 34 |
| **C** | Chorlton | 47 | 23.4% | 42.6% | 59.6% | 42 |
| **A** | Ludlow | 38 | 68.4% | **73.7%** | 73.7% | 52 |
| **B** | Ludlow | 38 | 73.7% | **81.6%** | 81.6% | 56 |
| **C** | Ludlow | 38 | 73.7% | **84.2%** | 84.2% | 63 |
| **A** | **All** | 134 | 35.8% | 50.7% | 61.2% | — |
| **B** | **All** | 134 | 36.6% | 51.5% | **64.2%** | — |
| **C** | **All** | 134 | 36.6% | 53.0% | 62.7% | — |

### 4.3 The finding, which corrects my own baseline and the CTO's sizing

The baseline called replacing the category filter *"the most useful thing in this spike"* and estimated it *"recovers 16% of misses"*. The CTO carried it as **S2**, half a week, and `subscription-sizing-note.md` §2.3 accepted the diagnosis as its own defect: *"An index for a British going-out journal that excludes everything called something-Inn is excluding pubs by name morphology."*

**The diagnosis was right and the remedy does not do what either of us expected of it.** In the dense city centre — the case Block 4 exists for — the top-three rate **falls**, from 40.8% to 38.8%, and the permissive scope C falls further on top-five, from 51.0% to 49.0%. [E, measured]

The mechanism is arithmetic, not subtle: **every venue the wider scope recovers is also a row placed in front of somebody else's answer.** The median Manchester query already returns 164 candidates within 250 m; scope B makes it 185 and scope C makes it 241. The top five is a 1-in-33 slice of what is nearby at scope A and a 1-in-48 slice at scope C. Recovering `Grosvenor Casino` costs every other venue on that block a place in the queue.

**Where it does help it helps a lot, and the split is by density.** Ludlow's top-three rate goes 73.7% → 81.6% → 84.2%, because in a market town the recovered venue is not competing with 200 neighbours. Chorlton is flat.

**This confirms, by measurement, the thing the CTO wrote without a measurement behind it** [E, `subscription-sizing-note.md` §8.2]: *"This is not a data problem that more data fixes; it is a precision-and-ranking problem, and adding rows makes it worse."* It is the correct reading of §8 of the baseline, and it applies to the category fix that the same note carried as S2.

**What I recommend, and it is a recommendation not a finding:** ship **scope B**. Not because it improves the dense case — it does not — but because it is where the recovered venues *are* real going-out venues, it costs 12.6% of index size (§12), and a British going-out journal that cannot represent `The Church Inn` is wrong in a way a user will notice and name, independent of any hit-rate statistic. **Do not ship scope C.** Its 209,570 null-taxonomy rows buy 2.6 points of Ludlow top-three and cost 47% more candidates in Manchester, 80% more index, and the only two venues it uniquely recovers in my sample are a cricket club and a members' club. [J, grounded in the [E] table above]

**Scope choice is not what lifts Block 4 and never was.** The baseline said so — *"it is not on its own sufficient"* — and §5 and §6 say what is.

---

## 5. Candidates 2 and 3 — clustering and the confirmation prior, on the baseline's own metric

This section uses **exactly the metric the baseline used at its §5.2**, so the numbers are comparable: 20 simulated visits per venue, an isotropic Gaussian offset of σ on the query point, and the distribution of which candidate takes rank 1.

**Three rankers.** `R0` is the shipped design: raw distance over index rows. `R1` merges near-duplicate rows into logical venues offline and ranks the clusters. `R2` adds the user's own confirmation history as a prior, scoring each candidate cluster *c* at query point *q* as

> **−d(c,q)² / 2σ_a² + log(1 + β·n_c(q))**

where σ_a = 25 m is the ranker's assumed position error, n_c(q) counts previous confirmations of *c* made within 150 m of *q*, and β is the prior's strength. β = 0 reduces R2 to R1. The simulation is **sequential**: the prior accumulates only when the user actually confirms, and the user only confirms when their venue is offered.

### 5.1 Results at σ = 25 m

**[E, measured. n as shown. Scope B for R1/R2, scope A for R0 so it reproduces the baseline.]**

| Ranker | Area | Median distinct rank-1 venues | Mean modal rank-1 share | Rank 1 changed ≥ once |
| --- | --- | --- | --- | --- |
| **R0** rows, distance *(= baseline)* | Manchester | **9** | **0.31** | **100.0%** |
| R1 clusters, distance | Manchester | 9 | **0.30** | 100.0% |
| R2 clusters + prior, β = 1 | Manchester | 5 | 0.58 | 100.0% |
| R2 clusters + prior, β = 4 | Manchester | 5 | 0.64 | 91.8% |
| R2 clusters + prior, β = 20 | Manchester | 4 | **0.67** | 91.8% |
| R0 | Chorlton | 6 | 0.46 | 91.5% |
| R2, β = 20 | Chorlton | 2 | 0.80 | 76.6% |
| R0 | Ludlow | 6 | 0.51 | 84.2% |
| R2, β = 20 | Ludlow | 2 | 0.85 | 55.3% |

### 5.2 Two findings, one of them negative

**(a) Clustering does not fix stability. 0.31 → 0.30.** [E, measured]

This is a negative finding on one of the four candidates the commission named, and it is worth being precise about why, because the reason also tells the PM/BA something useful. Offline clustering absorbs **2.02% of rows nationally** at scope B (336,103 rows → 329,321 clusters) and **3.6% in the three sample areas** [E, measured, `cluster_national.py`] — consistent with the baseline's hand-confirmed floor of ≥2.9% of city-centre rows being one half of a duplicate pair. So the duplicates are real, and they are simply not the thing that moves rank 1. **In a dense centre, the candidate that displaces your pub is another pub, not another copy of your pub.** Merge remains necessary for the reason the UX seat gave — a duplicate silently splits an accumulated record — and §6 measures how much of that harm clustering actually removes. It is not the identity mechanism.

**(b) The confirmation prior is the first thing in either spike to move the number, and it stalls short of the bar.** 0.31 → 0.67 in Manchester, and the curve is flat above β ≈ 4: pushing the prior harder stops helping.

**Why it stalls, because the mechanism matters more than the number.** The prior can only accumulate from confirmations, and the user can only confirm when their venue is in the list. In Manchester the venue is in the top five about half the time. So **the prior cannot help you hold on to a venue you could never find in the first place** — it is a stabiliser, not a locator. Raising β cannot fix a bootstrapping problem; only putting the venue in the list can, which is what §6 does.

**Against the CTO's limb (a) threshold of 0.8, measured on the metric limb (a) names: 0.67. Fail.** Stated here, plainly, before §8 argues about whether 0.8 of this quantity is the right thing to ask for.

---

## 6. The number that actually decides the venue page

### 6.1 Why a new metric, and why it is not goalpost-moving

Rank-1 churn is a proxy for a harm, and the harm is specific: `ceo-product-inputs.md` §1 makes the venue page *"probably the product, not a feature"*, and the UX seat described the failure as *"a user picks 'The Eagle' (provider A) in March and 'The Eagle' (provider B) in June… the product now believes the user visited two places once each rather than one place twice"* [E, `ux-note.md` §2.3].

Notice what that description contains: **the user's pick.** The design never auto-selects — that is a requirement under Article 4, not a preference [`ux-note.md` §2.2] — so rank 1 is not what creates a venue identity. **The user's choice is.** A design can have a wandering rank 1 and a perfectly stable identity, if the right venue is reliably *in the list* and the user reliably picks it.

So I measured the harm directly: **across 20 simulated visits to one real pub, how many distinct Candour venue identities does the journal accumulate?** One identity is a correct venue page. More than one is a split history, permanently, with no server and no backfill.

**The simulation models the specified design honestly**, including its escape hatches: the list is offered and never pre-selected; the user picks their own pub if it is shown; the user's own previously-created venues are offered alongside index rows; and if nothing matches, the user takes the "this venue isn't listed" path and creates a local venue. Variants toggle the widened scope, offline clustering, the prior, a name-dedupe rule on the "isn't listed" path, list length, and name search.

### 6.2 The result

**[E, measured. σ = 25 m. Median distinct identities per pub over 20 visits, and the share of pubs keeping exactly one.]**

| Design | Manchester | Chorlton | Ludlow |
| --- | --- | --- | --- |
| | median · % single | median · % single | median · % single |
| **As specified** (scope A, rows, distance, list of 5) | **5 · 4.1%** | 3 · 27.7% | 3 · 34.2% |
| + widened scope B | 5 · 0.0% | 3 · 27.7% | 3 · 34.2% |
| + offline clustering | 5 · 0.0% | 3 · 27.7% | 3 · 34.2% |
| + confirmation prior, β = 4 | 2 · 40.8% | 1 · 61.7% | 1 · 63.2% |
| + name-dedupe on "isn't listed" | 1 · 57.1% | 1 · 72.3% | 1 · 71.1% |
| + list length 10 | 1 · 61.2% | 1 · 85.1% | 1 · 92.1% |
| + list length 20 | 1 · 81.6% | 1 · 97.9% | 1 · 100.0% |
| **+ name search on "isn't listed"** | **1 · 100.0%** | 1 · 97.9% | 1 · 100.0% |

At σ = 50 m the same full stack gives **98.0% / 97.9% / 100.0%**; at σ = 10 m, **100% / 100% / 100%** [E, measured].

### 6.3 The finding that should worry the CEO most, and it is about the as-specified design

**The split compounds with use.** The same metric, varying how many visits a venue receives [E, measured, σ = 25 m, `year.py`]:

| Visits per venue | As specified — % keeping one identity | Remediated (full stack) |
| --- | --- | --- |
| | Manchester · Chorlton · Ludlow | Manchester · Chorlton · Ludlow |
| 3 | **30.6%** · 53.2% · 52.6% | 100.0% · 97.9% · 100.0% |
| 6 | 14.3% · 46.8% · 42.1% | 100.0% · 97.9% · 100.0% |
| 12 | 6.1% · 29.8% · 36.8% | 100.0% · 97.9% · 100.0% |
| 20 | 4.1% · 27.7% · 34.2% | 100.0% · 97.9% · 100.0% |
| 40 | **2.0%** · 25.5% · 34.2% | 100.0% · 97.9% · 100.0% |

**Read that as a product statement** [I, from the [E] above]: the index as specified does not merely produce a venue page that is sometimes wrong. **It produces a venue page that gets worse the more the user uses the product** — because every additional visit is another chance to land on a new row, and the splits never heal. The user's local, the place they go most, is the page that ends up most fragmented. That is the exact inverse of what `ceo-product-inputs.md` §1 describes the feature as being for, and it is a stronger statement of the harm than the baseline's 100% rank-1 churn, because it is denominated in the thing the user sees.

The remediated line is flat. That is the property to buy.

### 6.4 Which component does the work, and the honest caveat on the biggest one

The decisive component is the **name search on the "isn't listed" path** — when the user types a name because nothing in the list matched, the index is searched **by name** within the query radius rather than only by distance. It takes Manchester from 81.6% to 100% at σ = 25 m, and from 34.7% to 98.0% at σ = 50 m [E, measured]. It is also, of the whole stack, the component the CTO has already paid for: **FTS5 name search is inside row 5 of `android-and-stack-note.md` §3.2** [E, `subscription-sizing-note.md` §8.1], and the CTO's S-row already asks for *"a search path for the dense case"*.

**Now the caveat, and it is the single biggest piece of optimism in this note.** My simulation decides that the user's typed name matches an index row using the *same name-similarity function* that built the ground truth. So name search succeeds, by construction, whenever my matcher found a match at all. In reality the user types what is on the sign and the index carries what a provider supplied, and FSA carries the legal trading entity — three names for one pub. **The measured 100% is therefore an upper bound on what name search delivers, and the real figure is lower by an amount I did not measure and cannot estimate from this data.** [J]

What I can say without that assumption: **name search converts a location problem into a name problem, and a name problem is one the user can solve and a location problem is not.** A user standing in The Eagle knows the word "Eagle". They do not know that their visit centroid landed 31 m north-east. Every other lever in the table above asks the location signal to do better; this one stops asking. That argument does not depend on my matcher, and it is why I would build it first even at a lower measured yield.

**What overturns it:** typing three real sign-names per venue against the shipped index for a sample of the same 134 venues and measuring the match rate directly. That is under a day's work and it is item 1 in §14.

---

## 7. The price of the sticky prior — the "goes next door" test

Both the CTO and the UX seat named this hazard and neither could measure it. The CTO: *"at 50 m a Manchester cluster holds around forty venues, so a shortcut would confidently offer the wrong pub when the user goes next door"* [E, `subscription-sizing-note.md` §8.1]. The baseline agreed and imposed the constraint that sticky choice must **raise** a venue in the list and **never pre-select** one.

**Protocol.** For every ordered pair of sampled venues (V, W) whose true positions are within 100 m of each other, the user confirms V ten times, then visits W twenty times. On the W visits I measure how often V takes rank 1 (**false-stick**) and how often W is offered at all (**recall of the correct neighbour**) — the second being the one that decides whether anything bad actually happens, because the design never auto-selects.

**[E, measured. σ = 25 m, scope B, clustered. 280 / 1,600 / 2,760 neighbour visits.]**

| List length | β | Area | False-stick @1 | **Recall of the correct neighbour** |
| --- | --- | --- | --- | --- |
| 20 | 0 | Manchester | 2.5% | **75.0%** |
| 20 | 4 | Manchester | **57.5%** | **75.0%** |
| 20 | 20 | Manchester | 67.1% | 75.0% |
| 20 | 0 | Chorlton | 4.7% | 98.9% |
| 20 | 4 | Chorlton | 65.6% | **98.7%** |
| 20 | 0 | Ludlow | 3.0% | 99.5% |
| 20 | 4 | Ludlow | 53.0% | **99.4%** |
| **5** | 0 | Manchester | 2.5% | 30.7% |
| **5** | 4 | Manchester | 57.5% | **30.0%** |

**Finding: the hazard is real at rank 1 and costs nothing in correctness, provided two things are requirements rather than preferences.** With the prior on, the pub you went to last week takes first place on **57.5%** of your visits next door — the CTO and UX were right about the behaviour. But the correct neighbour is still offered on **75.0%** of those visits with the prior and **75.0%** without it: at a 20-row list the prior's cost is **zero, to the resolution of this measurement**, and at a 5-row list it is **0.7 percentage points**. The prior reorders the list; it does not evict the answer. [E, measured]

**The two conditions, stated as the requirements they need to be:**

1. **Never auto-select.** Already required by `ux-note.md` §2.2 on Article 4 grounds (a pre-selected candidate is a pre-ticked box). **This measurement adds an independent, non-constitutional reason for the same rule**: it is what converts a 57.5% wrong-first-row rate into a scroll rather than a corrupted venue page. If the design ever auto-selects, the prior becomes the most dangerous component in the stack instead of the most useful.
2. **The list must be long enough to absorb a wrong first row.** At five rows, dense-centre neighbour recall is 30% with or without the prior — the list is too short for the prior's cost to even be visible against its own inadequacy. The prior is safe at 20 rows. **It is not safe to ship the prior and keep the five-row list.**

**This answers open question 6 of the baseline's §9.2 in the direction the UX seat wanted, with a number attached**, and it converts "sticky choice must be a ranking input, never a shortcut" from a design opinion into a measured constraint.

---

## 8. The pass/fail bar Block 4 requires

Block 4(a) says the spike must pass *"a pass criterion agreed with the PM/BA, UX and QA **before** the spike runs"*, and the CTO's own note lists that criterion as **open question 5**, unowned and unset: *"A spike whose bar is set afterwards is not a test."*

**That sentence applies to me.** I have now measured, and anything I say about the bar is said by someone who knows the answers. I am therefore going to do three things in a fixed order: report the result against the bar as it stands, say why I think it is the wrong bar, and hand the choice to the seats that own it.

### 8.1 First: the result against the CTO's proposed bar, as written

> *"the spike passes if the modal rank-1 share in a dense city centre exceeds 0.8 at σ = 25 m and top-five recall exceeds 80%."* [`subscription-sizing-note.md` §8.2, §11]

| Limb | Bar | Baseline measured | **This spike, best configuration** | Result |
| --- | --- | --- | --- | --- |
| Modal rank-1 share, Manchester, σ = 25 m | > 0.80 | 0.27 | **0.67** | **FAIL** |
| Top-five recall, Manchester | > 80% | 51.9% | **53.1%** (perfect fix, scope B) | **FAIL** |

**The remediation fails the bar as written, on both limbs.** It roughly doubles one of them and barely moves the other. Whatever else this note argues, that is the answer to the question as it was asked, and it is recorded before the argument rather than after it.

### 8.2 The bar I would have set before measuring — and I do not have to reconstruct it, because I wrote it down

The obvious objection to anything in §8.3 is that I am an engineer who missed a target and then proposed a different target. **That objection is stronger than it looks, and the reason is that the 0.8 figure is mine.**

`venue-index-spike.md` §10.2, item 3, written by this seat two days ago and **before any of the measurements in this note existed**:

> *"If a non-positional tie-breaker takes the modal rank-1 share from 0.27 to above ~0.8 in a dense centre, the splitting mechanism largely closes and merge becomes a safety net rather than a necessity. I did not test any such signal and I am not claiming one works."*

The CTO did not invent the bar in §8.2 of its note. **It adopted mine.** So the pre-registration the commission asks me to reconstruct exists in the public record, it is unambiguous, it is in my own hand, and **I failed it: 0.67 against my own ~0.8.**

**What I got wrong, specifically.** The sentence contains an embedded assumption I did not notice I was making: that *"the splitting mechanism"* is rank-1 churn. It is not. I had measured rank-1 churn because it was the thing I could measure without simulating a user, and I then wrote the bar in the units of my instrument rather than in the units of the harm. §6 is what happens when the harm is measured directly, and it shows the two quantities come apart: a design can sit at 100% single-identity with a modal rank-1 share well under 0.8, because a shifting cast of neighbours trades places above a venue that is nonetheless reliably in the list and reliably picked.

**Is the difference justified or convenient? Partly the first, and I cannot fully clear myself of the second.**

- **Justified:** that rank-1 share and identity stability come apart is a fact about the world, established by a measurement nobody had run, not a preference. Had I known it on 18 September I would have written the bar in identity units then, and §6.3's compounding finding would have made P2 obvious.
- **Not fully cleared:** I discovered that fact while failing the bar, and there is no way for me to prove I would have reached the same view had I passed it. **The evidence standard's re-derivation clause does not help here either** — it covers arithmetic and claims about what a named clause requires, and explicitly does not extend to interpretation, on the grounds that a second agent pass inherits the first pass's reading. A second seat re-reading my argument is not independent evidence that my argument is right.

**So I am not asking to be trusted on this, and §8.5 gives the seats that own the decision a way not to trust me.**

### 8.3 Why the bar measures the wrong quantity

Two objections, both grounded in measurements in this note rather than in preference.

**(a) Both limbs are denominated in list position, and the block is about identity.** Block 4's own statement of what fails cites Condition 8.6 — *"a venue page must never show '3 visits, average 3.8' when the true figures are 11 and 4.2"* — which is a statement about a venue's accumulated record, not about what sat in row 1 or row 5. Under a design that never auto-selects, rank 1 does not create a venue identity; the user's pick does. §6 measures a design at **100% single-identity** in Manchester whose modal rank-1 share is well under 0.8, because the prior is putting the right venue in the list reliably while a shifting cast of neighbours trades places above it. **A bar of 0.8 on rank-1 share would fail that design, and the venue page it produces is correct.**

**(b) "Top-five recall > 80%" bars a design constant the evidence does not support.** The baseline's own §5.3 curve showed recall@5 of 51.9% against recall@20 of 92.5% in Manchester, and the CTO's §8.1 already records that *"Five rows is a design constant that the measurement does not support."* A bar that fixes the list at five and then demands 80% recall from it is asking the index to overcome a UI choice that the same note has already abandoned. §7 shows the list has to be long for an independent reason anyway.

### 8.4 The bar I propose, and the justification the commission asked for

**Proposed, for the PM/BA to set with UX and QA — not for me to set** [J, with the mechanism grounded in the [E] of §6 and §7]:

| # | Criterion | Threshold | Measured on the full stack |
| --- | --- | --- | --- |
| **P1** | **Single-identity rate** in a dense city centre at σ = 25 m: the share of venues that accumulate exactly **one** Candour venue identity across ≥ 20 simulated visits | **≥ 95%** | **100%** |
| **P2** | **Non-degradation with use**: P1 measured at 40 visits per venue must not fall more than **2 pp** below P1 at 3 visits per venue | ≤ 2 pp | **0.0 pp** |
| **P3** | **The prior must not evict the neighbour**: recall of the correct venue on a visit to a venue within 100 m of a previously-confirmed one must be within **2 pp** of the same design with the prior disabled | ≤ 2 pp | **0.0 pp** |
| **P4** | Single-identity rate at **σ = 50 m** — the reduced-accuracy case | ≥ 90% | **98.0%** |
| — | Top-N hit rate, junk rate, duplicate rate, rank-1 share | **report-only, not pass/fail** | see §4, §5 |

**Why these, in terms of what a user experiences over a year of use** — which is what the commission asked for, and which requires an explicit usage model, so here is one, labelled as the estimate it is. Take a moderately social user recording **roughly 100 visits a year across roughly 40 distinct venues**, weighted towards a handful of locals in a dense centre [J, my assumption; no Candour artifact carries a usage model and I did not find one to cite].

- **As specified, at σ = 25 m in a city centre: 2–4% of venues keep a single identity.** So after a year, **about 39 of those 40 venue pages are wrong**, and the median venue is split five ways. The user's local, visited 40 times, reads as five separate pages claiming eight visits each. Nothing in the product tells them; there is no server and no backfill; and the feature the CEO called the product is, in the CEO's own words about a different failure, *"silently wrong."*
- **At P1 = 95%: about 2 of 40 venue pages are wrong in year one**, and P2 says that does not grow to 20 by year five.
- **Why 95% and not 99%.** The residual failure is the one data error a user can actually see and repair: two pages with the same name. Merge exists, and it is user-facing and reversible (§9). A bar that demands near-perfection from the index is buying, at high cost, something the merge affordance already covers cheaply. **Why not 80%:** at 80%, eight of forty pages are wrong, the user hits the defect often enough to distrust the feature, and merge stops being a repair and becomes a chore — which is the point at which an honest product should not be charging for "an accurate per-venue history."
- **Why P2 exists at all, and it is the criterion I would fight for if I could only keep one.** §6.3 is the finding that a single-shot metric cannot see. A design can pass P1 at three visits and fail catastrophically at forty. **The CTO already wrote the general form of this lesson about its own open question 4** — *"I specified a single-shot metric for a longitudinal feature"* [E, `subscription-sizing-note.md` §2.2]. P2 is that lesson written as a test, and it costs nothing to run once the harness exists.
- **Why P3 exists.** Without it, the cheapest way to pass P1 is a prior so aggressive it pins one venue per location forever, which produces a perfectly stable and frequently wrong journal. P3 is the guard that makes P1 unhackable, and §7 shows a compliant design already satisfies it with room to spare.

**P1–P4 are all measurable on the harness in §13, today, in about ten minutes.** That is deliberate: a bar that requires new instrumentation is a bar that gets deferred.

### 8.5 How to check me, and what happens if you decline the substitution

Because §8.2 means my judgment on this is compromised by construction, here is the part that does not depend on it.

**The pass at P1 = 100% rests entirely on the one component whose measurement I have already flagged as an upper bound.** §6.4 states that name search succeeds in my simulation whenever my own matcher found a match, because both use the same similarity function — a genuine circularity. **The non-circular floor is the row above it in §6.2: the full stack without name search, at 81.6% single-identity in Manchester.** [E, measured]

So the honest range for the remediated design in a dense centre at σ = 25 m is **81.6% to 100%**, and **P1's threshold of 95% sits inside that range.** I cannot tell you which side of it the real design lands on, and the experiment that would tell you is item 1 of §14 and costs under a day.

**Three consequences, and they are the reason §14's verdict reads as it does:**

1. **On the CTO's bar as written, the remediation fails.** §8.1.
2. **On my own proposed bar, I cannot demonstrate a pass** — only a range that straddles it. A bar I proposed and cannot clear with a non-circular measurement is not a bar I am clearing.
3. **If the PM/BA, UX and QA decline the substitution entirely and hold me to the 0.8 rank-1 share I wrote on 18 September, that is a defensible decision and the answer is simply that the remediation failed.** I would not argue with it. What I would ask is that the decision be recorded as a choice between two bars, with §6.3's compounding measurement in front of whoever makes it, rather than as a default.

---

## 9. Sticky choice, merge and rename-in-place — specified for requirements

The UX seat put all three in MVP scope [`ux-note.md` §2.3] and the CTO confirmed they are **re-scoped, not added** — already inside row 5 of `android-and-stack-note.md` §3.2 [E, `subscription-sizing-note.md` §8.1]. The commission asks me to specify them concretely and to say from measurement whether they are sufficient.

**The measured answer to the sufficiency question is: they are not sufficient, and identity must be solved upstream of them.** §6's table is the evidence: adding clustering (which is what makes merge tractable) to the as-specified design leaves Manchester at **0.0% single-identity**. Sticky choice on its own gets it to 40.8%. The three features become adequate only once the venue is reliably *in the list* — which is the name-search and list-length work, and which sits upstream of all three. **Merge, sticky choice and rename are the repair layer. They cannot be the identity layer, and the baseline's framing of merge as "necessary regardless" is confirmed while its implicit hope that the three together would be enough is not.**

### 9.1 Sticky choice

- **It is a ranking input and never a selection.** Score contribution `+ log(1 + β·n)` where `n` is the number of prior confirmations of that venue made within **150 m** of the current query point, β ≈ 4. β above ~4 buys nothing measurable (§5.1).
- **The distance gate is part of the feature, not a tuning constant.** Without it, a venue confirmed in Manchester competes in Ludlow. 150 m is the value measured here; it is settable.
- **It never pre-selects, never collapses the list, and never hides an alternative.** §7 is the evidence that this rule is what makes the feature safe: with it, a 57.5% wrong-first-row rate costs zero correctness; without it, the same 57.5% is a corrupted journal.
- **A previously-chosen venue is marked as such in the row** ("you chose this here before"), because a row that is first for a reason the user cannot see is a row the user cannot audit.
- **It requires the list length of §9.4.** Shipping sticky choice on a five-row list is the one combination the measurements say not to build.

### 9.2 Merge

- **User-facing, reversible, reachable from any venue's detail screen**, as the UX seat specified: "this is the same place as…".
- **Two layers, and they are different things.** (i) **Offline clustering at index build time** collapses near-duplicate rows — within 60 m and name-similarity ≥ 0.70 — into one logical venue shipped as a `cluster_id`. Nationally this absorbs **6,782 of 336,103 rows, 2.02%** [E, measured]; in the three sample areas, 3.6%. (ii) **User merge** handles everything clustering cannot see, which is most of it: the baseline hand-confirmed pairs like `Manchester Weatherspoons Picadilly` / `Wetherspoon` at name-similarity 0.49, which no safe automatic threshold will ever join.
- **Offline clustering must be conservative and it must be auditable.** It is applied to rows the user has not yet seen; a wrong automatic merge is worse than a duplicate, because it silently fuses two real pubs into one page and the user has no reason to suspect it. The 0.70/60 m parameters are measured, not settled, and QA should test the false-merge rate directly.
- **A user merge is a durable row, not a derived state.** See §10, criterion 5.

### 9.3 Rename in place

- **The user's name for a venue outranks the dataset's, permanently and across refreshes** (§10, criterion 4).
- **Rename does not create a new identity** — it edits the Candour-owned row. This matters for §6: a rename that forked the identity would reintroduce the split it is meant to prevent.
- **The renamed name is what name search matches against**, alongside the dataset name. This is a small line with a real effect: it is how the user's own vocabulary ("the Eagle", not "The Eagle Free House Ltd") becomes the thing that finds their pub next time.

### 9.4 The fourth item, which is not in MVP scope and the measurements say should be

**List length and the name-search path.** §6 shows these are the two largest contributors to identity stability, larger than any of the three MVP features. `ux-note.md` §2.2 designed the confirmation row for recognition at a glance, and twenty rows of a dense high street is not a glance — **this is a genuine conflict between two correct design goals and I am flagging it rather than resolving it**, because it is the UX seat's and the PM/BA's to resolve. The shape of a resolution the measurements support: a short list by default, with the "isn't listed" affordance in the search field as UX already specified, so that **typing is the path to the long list** rather than scrolling being it. On these numbers that combination gets most of the benefit, because the name search is doing the work and the twenty-row list is mostly a proxy for "the venue was reachable at all".

---

## 10. The refresh hazard — the schema rule

The commission calls this *"the cheapest thing to do now and the most expensive to retrofit."* The baseline raised it, the UX seat raised it first [`ux-note.md` §2.3], and the CTO adopted it as an architectural constraint and made it limb (b) of Block 4 [E, `subscription-sizing-note.md` §2.4].

**The rule, in one line:**

> **A dataset refresh must never mutate a venue row already referenced by a user's visit.**

**Re-retrieved evidence that this is a live hazard and not a hypothetical** [all E, verbatim — [Overture Maps Places guide](https://docs.overturemaps.org/guides/places/), retrieved **2026-09-20**, this session, not taken from the baseline's quotation of it]:

- *"Better matching also improves GERS ID consistency over time, because a place is less likely to split into (or merge from) multiple identities as source data shifts."* — so identities do split and merge across releases, by Overture's own account.
- *"Note that the July 2026 release itself re-matches the corpus with the new pipeline, so users should expect a one-time elevated level of GERS ID churn in that release; subsequent releases benefit from the more stable matching."* — **a release one month before the one Haunt is built on deliberately churned GERS IDs corpus-wide.** This is new to the Candour record; no artifact carries it.
- The same page's taxonomy change summary: **2,108 categories repathed** (*"Critical: Hierarchy-dependent processing (e.g., aggregation) must be updated to reflect the new paths, especially in areas like `food_and_drink`"*), **482 reparented**, **407 renamed**, **209 added**, **80 removed** (*"Users must use the provided 'redirect' rules to map old category IDs to active categories"*). The baseline reported the repath/rename/remove figures; the reparent and add figures are also confirmed here.
- *"Places is known to contain duplicates, a high junk rate, and low property completeness. The confidence score… does not address duplicates or property completeness."*

**So between two releases, a row referenced by a user's 2027 visit can change its name, its position, its category, its hierarchy path and its GERS ID; an upstream merge can fuse two of the user's venues; an upstream split can fork one.** With no server, no telemetry and no backfill, any of those is **permanent, silent and undiscoverable by Candour**.

**What the CTO's existing commitment does and does not cover.** `feasibility-note.md` §3 commits that *"venue identity is a Candour-owned local row"* carrying the GERS ID *"as an attribute, never as the only handle."* That settles the **identifier**. It says nothing about the **fields**, and §11 is the part that does.

**One addition of my own, which the baseline did not have and which the re-retrieved quote above forces:** because Overture itself warns that a release can churn GERS IDs corpus-wide, **the GERS ID must not be the join key for reconciliation either.** A refresh that matches local rows to new dataset rows by GERS ID alone will mis-join precisely in the release where churn is highest. Reconciliation must match on position and name as well, and must treat a GERS-ID change as a signal to ask rather than a signal to update.

---

## 11. The five schema criteria, restated as acceptance criteria

`venue-index-spike.md` §9.3 stated five criteria in prose. Block 4(b) requires them *"in the requirements document and in the schema, not in a backlog."* Restated below as testable acceptance criteria the PM/BA can lift directly, each with the test that demonstrates it. **These are prepared, not accepted: limb (b) is satisfied when the PM/BA has written them and the schema implements them, not when I have drafted them.**

**Schema preconditions** (without these, none of AC-1..5 is testable):
- Table `venue`: Candour-owned local row. Columns include `venue_id` (local, stable, never derived from any dataset identifier), `display_name`, `lat`, `lon`, `category`, `name_source` ∈ {`dataset`, `user`}, `gers_id` (nullable attribute), `cluster_id` (nullable attribute), `first_referenced_at` (nullable).
- Table `venue_ref`: the referenced-ness fact. A visit's reference to a venue is a row here. **`venue.first_referenced_at IS NOT NULL` is the definition of "referenced" and it is set once and never cleared.**
- Table `venue_merge`: durable user merges, `(surviving_venue_id, absorbed_venue_id, merged_at)`.
- Table `refresh_proposal`: pending, reviewable changes from a refresh, with a `declined_at` column.

| # | Acceptance criterion | How QA tests it |
| --- | --- | --- |
| **AC-1** | **On first reference, the venue row is copied, not pointed at.** At the moment a visit first references a venue, `display_name`, `lat`, `lon` and `category` are written into the `venue` row from the index, and `first_referenced_at` is set. The row is thereafter self-sufficient: **rendering a venue page must not read the shipped index at all.** | Reference a venue; delete the shipped index file; assert the venue page renders identically, including name, position and category. |
| **AC-2** | **A refresh may add unreferenced rows and update unreferenced rows. It may never write to a referenced row.** Enforced in the schema, not in application code: a trigger or equivalent rejects any `UPDATE` to `venue` originating from the refresh path where `first_referenced_at IS NOT NULL`. | Reference venue X; run a refresh whose payload renames, moves and re-categorises X and changes its GERS ID; assert X is byte-identical afterwards and that the attempted write was rejected rather than skipped silently. |
| **AC-3** | **Changes to referenced rows are offered, never applied, and declining is the default.** A refresh that would have changed a referenced row writes a `refresh_proposal` instead. Proposals are inert: **if the user never opens the review surface, nothing changes, ever, including across subsequent refreshes.** No proposal auto-applies after any period. Declining is recorded so the same change is not offered repeatedly. | Reference X; run two refreshes proposing a rename; never open the review surface; assert X unchanged and exactly one open proposal. Decline it; run a third refresh; assert no new proposal for the same change. |
| **AC-4** | **A user's rename always outranks the dataset, permanently and across refreshes.** Once `name_source = 'user'`, no refresh may alter `display_name` and **no refresh may even propose a name change** — the question has been answered. | Rename X; run a refresh carrying three successive different upstream names; assert `display_name` unchanged and zero name proposals raised, across all three. |
| **AC-5** | **User merges survive refreshes, including a refresh that re-splits the upstream records the merge joined.** The merge is a durable row in `venue_merge`, not a derived property of the index. Re-clustering at refresh time may never dissolve a user merge, and a refresh that splits an upstream record must not fork a merged Candour venue. | Merge A and B; run a refresh in which the upstream rows behind A and B are re-split into three records with new GERS IDs; assert one surviving venue, all visits attached, and history intact. |
| **AC-6** *(added by this spike)* | **Reconciliation may not join on the GERS ID alone.** Matching local rows to refreshed dataset rows uses position and name in addition to `gers_id`; a changed or vanished `gers_id` on a referenced row raises a proposal, never an update. | Run a refresh in which every GERS ID in the payload is regenerated but names and positions are unchanged; assert zero duplicate venues created and zero referenced rows mutated. |

**AC-6 is new and is the one I would add to the CTO's list**, on the re-retrieved evidence at §10 that Overture churned GERS IDs corpus-wide one release before the one this product is built on.

**Cost now: part of the schema, effectively free.** Cost later: unavailable. There is no server, no telemetry and no backfill (`feasibility-note.md` §2.6, §5), so this is not a defect that can be fixed after ship — it is, as the CTO put it, *"a defect that cannot be detected after ship."*

---

## 12. Size and bundle impact

The CTO's architecture ships the index inside the app, so any scope widening is a bundle cost. The commission asks for the number.

**[E, measured. SQLite built to the CTO's stated minimal schema — name, category, lat/lon rounded to 1e-5, indexed on `(lat, lon)` — then with the attributes and the index the remediated design actually needs. `VACUUM`ed; gzip level 6.]**

| Scope | Rows | Minimal schema | + GERS + `cluster_id` | **+ FTS5 name index** |
| --- | --- | --- | --- | --- |
| **A** — as specified | 302,820 | 23.8 MB / 12.0 gz | 36.5 / 21.1 | **43.3 MB / 24.3 gz** |
| **B** — widened, recommended | 336,103 | 26.8 MB / 13.7 gz | 40.8 / 23.8 | **48.5 MB / 27.4 gz** |
| **C** — plus null-taxonomy | 545,673 | 43.0 MB / 22.4 gz | 65.8 / 38.7 | **78.7 MB / 45.1 gz** |

**Three figures, in the order they matter.**

1. **Widening the category scope costs +12.6% of index size** on the minimal schema (23.8 → 26.8 MB), for **+11.0% more rows**. On the fully-specified schema it is 43.3 → 48.5 MB, **+12.0%**. This is the answer to the commission's question and it is not a constraint on any decision here.
2. **The remediation's real bundle cost is not the scope — it is the FTS5 name index, and I am flagging it because it is mine.** Going from the CTO's minimal schema at scope A (23.8 MB) to the remediated shipped schema at scope B (48.5 MB) is **+104%, slightly more than a doubling**, and roughly half of that increase is the name index and the two added attributes rather than the extra rows. **The component I recommend most strongly in §6 is also the one that costs the most bundle.** That trade should be visible to the CTO and the CFO rather than discovered at build.
3. **Scope C costs 78.7 MB** — 3.3× the as-specified index — and §4 shows it makes the dense case worse. It is the one scope I recommend against, and size is the second reason, not the first.

**Does this constrain anything?** On the CTO's own framing, no: `subscription-sizing-note.md` §2.1 records that the competing size figures *"are a rounding error against Apple's 4 GB build limit"* [E, CTO's figure, attributed and not independently retrieved by me]. 48.5 MB is a larger rounding error than 23.3 MB and it is still a rounding error. **Constitution 1.5 is satisfied either way and I want to be explicit about why rather than waving at it:** the index ships inside the binary and is queried on-device, so the marginal *running* cost of every figure in this table is **£0** — no hosting, no egress, no per-query cost. The cost of the widening is download size and disk on the user's phone, once per app update.

**One honest caveat on the gzip column.** App Store delivery re-compresses the binary with its own pipeline; my gzip figures are a like-for-like comparison between scopes, not a prediction of the download delta a user sees. [J]

---

## 13. Reproduction and evidence register

**Everything below was retrieved or measured on 2026-09-20. Nothing is cited from memory.**

**This harness is the CTO's S1 deliverable in draft form, and I have not left it where the last one was lost.** §1 records that the baseline's equivalent vanished with its session. Every script below, plus the seeded sample and the venue→row resolution, is committed at **`products/haunt/venue-index-harness/`** with a README that says how to re-run the chain — about fifteen minutes on a laptop, of which the Overture extract is fifty seconds. The derived `ovt.duckdb` and the built SQLite indexes are not committed; `extract.py` rebuilds them.

**I am flagging that as a scope decision I took rather than asked for.** `CLAUDE.md` documents `products/[slug]/` as holding a product's code, so it is within the documented structure, and §1's argument that this must not live in `/tmp` would have been hollow if I had then left it in `/tmp`. It is the Engineer's working code, unreviewed by any other seat, and it is not product code. **If the CTO or the PM/BA would rather it were not in the repository yet, deleting the directory costs nothing and loses nothing this note depends on** — every number here is reproducible from the scripts as listed.

| Script | What it does | Section |
| --- | --- | --- |
| `extract.py` | UK bbox extract from Overture `2026-08-19.0` via DuckDB 1.5.5 + `httpfs` over the public S3 bucket → `ovt.duckdb` | §2 |
| `counts.py` | reproduces the baseline's and the CTO's category counts | §2 |
| `scopes.py` | the three scope definitions, including the 32-value out-of-hierarchy allow-list | §4 |
| `build_index.py`, `build_work.py` | scope row counts; the near-area working table | §4 |
| `size_minimal.py`, `size_shipped.py` | shipped SQLite sizes: minimal schema, +GERS/+`cluster_id`, +FTS5 | §12 |
| `fsa.py` | FSA Food Hygiene Rating Scheme ground truth for the three areas | §3 |
| `sample.py` | seeded stratified draw, `random.seed(20260918)` | §3 |
| `harness.py` | distance, name matching, offline clustering, jitter, **`stable_seed()`** | all |
| `match.py`, `handscores.py` | venue→row resolution and the hand adjudication overrides, listed individually | §3 |
| `hitrate.py` | top-N hit rate by scope at a perfect fix | §4 |
| `stability.py` | rank-1 stability, rankers R0/R1/R2, σ ∈ {10, 25, 50} — **the baseline-comparable metric** | §5 |
| `cluster_national.py` | offline near-duplicate clustering over the whole scope-B index | §5, §9 |
| `identity.py` | **the identity-split simulation** — the metric at §6 and criterion P1 | §6 |
| `year.py` | identity split as a function of visits per venue — criterion P2 | §6.3 |
| `falsestick.py` | the "goes next door" test — criterion P3 | §7 |

**Reproducibility note.** `identity.py` was run twice in separate processes and the outputs diffed byte-for-byte after the `stable_seed()` fix (§1). Anything re-run from an earlier copy of this harness that seeds from Python's built-in `hash()` will not reproduce these numbers.

**Data sources**

- **Overture Maps Places**, release `2026-08-19.0`, `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/` — CDLA-Permissive-2.0 / Apache-2.0 depending on source. Extract re-materialised 2026-09-20.
- **[Overture Maps — Places guide](https://docs.overturemaps.org/guides/places/)**, retrieved **2026-09-20, this session** — re-retrieved rather than carried from the baseline's quotation. Load-bearing verbatim passages, all used at §10: GERS identity split/merge *"as source data shifts"*; the **July 2026 corpus-wide GERS churn** warning; the taxonomy change summary (2,108 repathed, 482 reparented, 407 renamed, 209 added, 80 removed, hierarchy changes *"Critical… especially in areas like `food_and_drink`"*); *"Places is known to contain duplicates, a high junk rate, and low property completeness"*; *"it does not address duplicates or property completeness"*; the undermatching discussion (*"especially when records are more than 100 meters apart or have only moderately similar names"*); *"The theme does not include OpenStreetMap data."*
- **[Food Standards Agency, Food Hygiene Rating Scheme API](https://api.ratings.food.gov.uk/Establishments)** (`x-api-version: 2`), retrieved 2026-09-20 — Crown copyright, Open Government Licence. Returned the same in-radius counts as the baseline two days earlier: 828 / 117 / 48.

**Figures travelling from other Candour artifacts, attributed and not re-derived by me**

- `products/haunt/venue-index-spike.md` (my own baseline) — reproduced independently at §2 rather than carried; where it is quoted it is quoted as a prior claim, including the pre-registered 0.8 bar at §8.2.
- `products/haunt/subscription-sizing-note.md` §2, §8, §11, §12 — Block 4 and both its limbs, the S1–S3 decomposition, the 113 h sizing, the 4 GB build limit, open questions 5 and 6.
- `products/haunt/feasibility-note.md` §2, §2.6, §3, §5 — the index specification under test, the data-layer commitment, and the no-server/no-backfill facts.
- `products/haunt/ux-note.md` §2.2, §2.3 — never auto-select, merge/sticky/rename, the dataset-refresh hazard.
- `proposals/haunt/ceo-product-inputs.md` §1 — the venue page as the product.
- Apple `CLVisit` accuracy — **not retrieved by anyone, still.** Every σ in this note is an assumption, not a measurement. §14 item 2.

**Looked for and did not find**

- **Any Candour artifact carrying a usage model** — visits per year, distinct venues per user — against which §8.4's "year of use" justification could be tested. I supplied one and labelled it [J]. It is the weakest premise under the choice of 95% rather than some other number, and a real one would firm up or move that threshold.
- **Any published figure for `CLVisit` horizontal accuracy in dense urban settings.** The baseline looked and did not find one; the CTO records the same absence for battery. It remains the single highest-value missing fact about this product.

**Related-party disclosures.** None.

---

## 14. Verdict, and what would overturn it

### 14.1 The verdict

**Block 4 is not lifted. I prepared the evidence for both limbs and neither is satisfied.**

**Limb (a) — the spike passes a pre-agreed bar.** Three findings, in descending order of how much they depend on my judgment:

1. **Against the bar as written — modal rank-1 share > 0.8 and top-five recall > 80% at σ = 25 m in a dense city centre — the remediation measures 0.67 and 53.1%. It fails, on both limbs.** This finding depends on no judgment of mine at all. §5, §8.1.
2. **Against the bar I propose instead, I cannot demonstrate a pass either.** The 100% single-identity figure rests on the name-search component, whose measurement is circular by construction (§6.4). The non-circular floor is **81.6%**; my proposed threshold is 95%; **the true value lies somewhere in 81.6–100% and I cannot say which side of the threshold it falls.** §8.5.
3. **And the bar I propose is a bar I substituted after failing one I had written myself.** §8.2. I have given the owning seats the grounds to decline the substitution, and if they do, the answer is simply (1).

**Limb (b) — the five schema criteria in the requirements document and in the schema.** §11 restates them as six testable acceptance criteria with the schema preconditions they need and the tests that demonstrate them, and adds **AC-6** on GERS-ID churn that the criteria did not previously cover. **But a criterion drafted by the Engineer is not a criterion in the requirements document.** Limb (b) is satisfied when the PM/BA has written these and the schema implements them. It is prepared. It is not met.

**What I am explicitly not saying, because the commission asked for it as a possibility and it is not what I found.** I am **not** reporting that the index cannot hold a stable venue identity at acceptable cost. The measurements point the other way: a design exists that holds a single identity for 81.6–100% of dense-centre venues, it is flat from three visits to forty, it costs **+12.6% of index size** for the scope and roughly a doubling for the full shipped schema at £0 marginal running cost, and **its largest single component is a name search the CTO has already scoped and paid for inside row 5.** The honest summary is that **the remediation is close, its headline number is overstated by an amount I have bounded but not measured, and one day's work would settle it.** That is a different report from "this cannot be done", and the CEO should not receive the second when the evidence supports the first.

**What I am also not saying:** anything about kill or proceed. That is the CEO's under Constitution 5.4. Block 4 is the CTO's under 5.6 and only the CTO may lift it; the Engineer holds no block and this note claims none.

**The one thing I would put in front of the CEO if only one line survived:** the index *as currently specified* produces a venue page that **gets worse the more the product is used** — 30.6% of dense-centre venues hold a single identity after three visits, 2.0% after forty [E, §6.3]. The CTO was right to pre-declare Block 4, and it was right for a reason stronger than the one it gave.

### 14.2 What would overturn this finding, and where I looked

*(Required by `roles/engineer.md` as amended: a negative finding carries a block's duty.)*

**Overturned by any of these:**

1. **The typed-name experiment. Under one day, and it is the single item standing between this note and a defensible pass.** For each of the same 134 venues, take three real sign-names — from the shopfront, the venue's own listing, the FSA registration — and run each against the shipped scope-B index with the actual FTS5 name search rather than my similarity function. That replaces the circular 100% in §6.2 with a measured figure and resolves the 81.6–100% range in §8.5 and §14.1. **If it lands above 95%, limb (a) is met on the proposed bar and only the choice of bar is left to argue about.** I did not run it because I have no source of sign-names I did not construct myself, and constructing them is exactly the circularity I am trying to escape.
2. **Real `CLVisit` accuracy materially better than σ = 25 m.** Still the highest-value missing fact, still unmeasured by anyone, still budgeted (`feasibility-note.md` §8 item 3 asks for a real-week battery measurement during build — **measure accuracy on the same run**). At σ = 10 m the as-specified design already holds a single identity for 59.2% of Manchester venues against 4.1% at σ = 25 m [E, §6.2], and much of this note's urgency dissolves. At σ = 50 m it is 0.0% and the case is worse than stated. **Every number here is a function of a parameter nobody has measured**, which is why §6.2 and §8.4 report three values of it rather than one.
3. **A false-merge measurement that comes back badly.** §9.2 recommends offline clustering at 60 m / 0.70 name-similarity on the strength of it absorbing 2.02% of rows nationally. I did **not** hand-adjudicate those 6,782 national merges — I hand-confirmed only that the parameters reproduce the baseline's hand-confirmed duplicate rate in three areas. **If QA finds that those parameters fuse distinct pubs at a material rate, clustering must be loosened or dropped**, and since §5.2 shows it contributes almost nothing to stability, dropping it costs little. This is a negative finding waiting to be made about a recommendation of mine, and I would rather name it than have it found.
4. **A usage model that makes 95% the wrong threshold.** §8.4's "40 venues, 100 visits a year" is mine and is labelled [J]. A real one — from a comparable product, or from the CEO's own judgment about who this is for — could move P1 in either direction, and the threshold is the part of §8.4 I hold most loosely. The *mechanism* arguments (P2's compounding, P3's unhackability) do not depend on it.

**Where I looked, so a reader can check I looked in the right places:**

- **The whole dataset again, from the source, not from the baseline's summary of it.** 3,325,607 rows re-extracted from Overture's public bucket and re-counted against eleven of the baseline's and the CTO's figures (§2).
- **Three index scopes built and measured end to end**, not argued about: row counts, shipped sizes with three schema variants, hit rate, stability and identity split for each.
- **Five ranking and interaction designs**, each measured on the same ground truth and the same simulated visits: raw distance, clustered, three strengths of confirmation prior, name-dedupe, three list lengths, and name search.
- **Both directions of the sticky-prior question.** I measured what it buys (§5, §6) *and* what it costs on the neighbour case the CTO and UX warned about (§7), because a lever measured only where it helps is a lever not measured.
- **Overture's own documentation, re-retrieved this session** rather than carried from the baseline — which is how the July 2026 GERS-churn warning, absent from every Candour artifact, reached AC-6.
- **My own baseline, treated as a claim to be checked rather than a foundation** — including finding that its most confident recommendation (the category fix) does not help the case that matters, and that its pre-registered bar was written in the wrong units by me.
- **Where I did *not* look:** I did not visit a venue; did not run anything on a phone; did not measure `CLVisit`; did not test OSM or any hybrid or supplementary dataset; did not hand-adjudicate the national clustering; did not test opening-hours or time-of-day ranking signals (the CTO's S3 names them and the confirmation prior turned out to dominate, so I spent the budget there); and did not obtain independent sign-names, which is item 1 above and the reason this note stops where it does.

---

## 15. Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | Created under `subscription-sizing-note.md` §8.2/§11 (**Block 4**). Rebuilt the lost measurement harness from source and **reproduced the baseline on eleven figures to the unit**. Measured three category scopes, three rankers, offline clustering, the confirmation prior, list length and name search. **Introduces the identity-split metric** and the finding that the as-specified index degrades with use (30.6% → 2.0% single-identity, 3 → 40 visits). **Measures the "goes next door" hazard for the first time** and finds it costs zero correctness at a 20-row list. **Records that the 0.8 rank-1 bar was written by this seat before measuring, and that this seat failed it**, then proposes an identity-denominated bar while giving the owning seats grounds to decline the substitution. **Verdict: Block 4 is NOT lifted**, on limb (a) as written, on the proposed replacement bar (range straddles the threshold), and on limb (b) (prepared, not accepted). Names the one-day experiment that would settle it. Adds **AC-6** on GERS-ID churn from documentation re-retrieved this session. External sources retrieved 2026-09-20. **Not a certification.** |

---

*Prepared by the Engineer seat under `roles/engineer.md` as amended. This note prepares and flags; it does not certify (Constitution 6.1). The Engineer holds no block: Block 4 is the CTO's, only the CTO may lift it, and only the CEO may overrule it (Constitution 5.6). The pass criterion is open question 5 and belongs to the PM/BA with UX and QA. Kill/proceed is the CEO's alone (Constitution 5.4), and nothing in this note pretends otherwise.*

# Venue-index spike — Haunt

**Seat:** Engineer · **Date:** 2026-09-18 · **Commissioned by:** `decisions/2026-09-16-haunt-gate.md`, **Condition 2** (Skeptic objection O5; CTO open question 4; re-specified per `products/haunt/ux-note.md` §2.4)
**Status:** build-gating artifact. Conditions 1–3 must complete **before requirements are signed off**. **Prepares and flags; does not certify** (Constitution 6.1). Kill/proceed remains the CEO's (Constitution 5.4).
**Template note:** `pipeline/templates/` has no spike template. Structure follows the four metrics Condition 2 names, plus the verdict and overturn clause my charter requires. The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Everything marked **[E, measured]** is a measurement I ran in this session; the method is stated at the point of use and the working scripts are listed in §11 so a stranger can re-run them. Retrieved documents carry their links. Nothing here is cited from memory.

---

## 0. Summary and verdict

**Verdict: the index as specified in `feasibility-note.md` §2 is NOT shippable as the venue source for a product whose core value is an accurate per-venue history. It is close enough to be worth fixing rather than abandoning, and the fixes are in the query layer and the schema, not in the dataset.**

Six findings.

1. **The CTO's extract reproduces exactly.** Same release, same bounding box, same tooling: **3,325,607** places in the UK bbox and **2,900,349** named at `confidence >= 0.5` — both to the unit. Four of the CTO's category sub-counts also match to the unit. The size claim holds too (23.3 MB / 11.3 MB gzipped on my schema). **The measurement the feasibility note made, it made correctly.** §2.
2. **Correctness is a different matter. Measured top-N hit rate over 132 real UK venues: 34.1% at rank 1, 53.0% in the top three, 58.3% in the top five.** In a dense city centre the top-three rate is **47.9%**; in a small market town it is **68.4%**. The CTO's spike question was "how often is the right venue in the top three?" The answer is: about half the time, and worse where people actually go out. §4.
3. **Those figures are the best case, because they assume a perfect location fix.** Re-run with a 25 m Gaussian error on the query point — modest for a `CLVisit` centroid — and the probability that a *findable* venue is in the top five on any given visit falls to **51.9%** in the city centre. Compounded, roughly **28%** of dense-city-centre visits would present the correct venue in the top five. §5.
4. **The junk rate is low and this is a genuine pass.** Hand-adjudicated over a random 100 of the 410 distinct candidate rows: ~2% clear junk. An independent check against the Food Standards Agency register found only **1.7%** of candidate rows with no registered food business of any name within 100 m. **Overture's confidence score is doing the job Overture says it does.** §7.
5. **The duplicate rate *inside a single top-five list* is also low (5.1% of lists) — and that metric understates the harm the UX seat identified.** The mechanism that splits a venue page is *temporal*, not within-list: the same pub, visited twice, resolving to two different rows. Measured directly, at 25 m query error **100% of city-centre venues had their rank-1 candidate change across 20 simulated visits**, with a median of **10 distinct venues** taking first place. §6.
6. **The instrument the Skeptic named is the wrong one to blame, and the measurement says so.** Of 55 misses, `confidence >= 0.5` caused **2**. The **category filter** caused **9**, including a systematic class: British pubs that Overture files as `inn` under **`lodging`**, outside the food-and-drink slice entirely. The Skeptic is right that confidence cannot address duplicates — Overture's own documentation says so, and I re-retrieved it — but the filter that is actually losing venues in this extract is the category scope. §4.3.

**What this means for the gate's conditions.** The UX seat's MVP asks — **merge, sticky choice, rename in place** — are supported by the measurements, though not all for the reasons given. And the hazard the UX seat raised that nobody has specified (**a dataset refresh must not mutate venue rows already referenced by a user's visit**) is, on these numbers, the single cheapest thing in this document and the most expensive one to retrofit. §9.

**What would overturn this verdict, and where I looked: §10.** It is short, concrete, and three of the four items are cheap to test.

---

## 1. What I was asked, what I did, and what I could not do

Condition 2 asks four questions: top-N hit rate, duplicate rate in the top five, junk rate in the top five, and a coverage sanity check. It says the result may kill the product and that this is the point.

**What I did.** I rebuilt the CTO's extract from the same Overture release, built it into the same SQLite shape, constructed an independent ground-truth sample of real UK venues from a statutory register, and queried the index by coordinate exactly as the app would — bounding box on the `(lat, lon)` index, then exact distance ordering, then top N.

**What I could not do, stated before the numbers rather than after them:**

- **I have no device and no `CLVisit` data.** I cannot measure the real distribution of visit-centroid error. Instead of inventing one, I report every figure at a perfect fix *and* under three stated Gaussian error levels (10 / 25 / 50 m), so the reader can locate the truth on a curve rather than take my word for a point. [J]
- **I cannot reliably detect a closed venue.** My junk rate is therefore a **lower bound**. The nearest thing to a closure signal in the data — Overture's `operating_status` — is populated for **322 of 330,208** UK food-and-drink rows, 0.098% [E, measured]. There is no dataset signal for closure and I could not construct a good proxy for one.
- **No usability testing.** I am measuring what the index returns, not what a person does with it. Where I say a list is unusable, that is [J] and labelled.
- **Three areas, 139 sampled venues.** That is enough to separate 50% from 90%. It is not enough to separate 53% from 58%, and I do not draw conclusions at that resolution.

---

## 2. Reproducing the CTO's extract

Method: DuckDB 1.5.5 with `httpfs` and `spatial`, reading `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/*.parquet` anonymously, filtered on `bbox.xmin BETWEEN -8.65 AND 1.77 AND bbox.ymin BETWEEN 49.86 AND 60.86` — the release, bbox and tooling the feasibility note names. 3,325,607 rows materialised locally in 59 s.

| Measure | `feasibility-note.md` §2.3 | This session | Match |
| --- | --- | --- | --- |
| All places in UK bbox | 3,325,607 | **3,325,607** | exact |
| Named, confidence ≥ 0.5 | 2,900,349 | **2,900,349** | exact |
| — of which `categories.primary = 'pub'` | 42,407 | **42,407** | exact |
| — `cafe` | 33,215 | **33,215** | exact |
| — `restaurant` | 22,886 | **22,886** | exact |
| — `coffee_shop` | 19,875 | **19,875** | exact |
| Food-and-drink category match | 346,184 | 330,208 named / **302,820** named at conf ≥ 0.5 | **not reproducible** |

[E, measured this session — DuckDB over the public Overture S3 bucket, release `2026-08-19.0`.]

**The one line that does not reproduce, and why it matters a little.** The note's headline figure of 346,184 is not recoverable from the note, because the note does not state the category predicate behind it. Filtering on the release's own taxonomy (`taxonomy.hierarchy[1] = 'food_and_drink'`) gives 302,820 at the same name-and-confidence filter — 12.5% fewer. I am not asserting the CTO's number is wrong; I am recording that **the note does not carry enough of its own method for a second seat to re-derive it**, which is what Condition 6 of the decision record asks packs to be capable of. Everything in this spike therefore runs on the taxonomy filter and says so. The difference does not move any conclusion here: nothing below turns on 12% of the row count.

**Size, briefly, because the note's claim is checkable and it checks out.** Built to the CTO's stated minimal schema (name, category, lat/lon at 1e-5, indexed on `(lat, lon)`): **23.3 MB on disk, 11.3 MB gzipped**, for 302,820 rows [E, measured]. Against the note's 21.3 MB / 10.8 MB for 346,184 rows. Same order, same conclusion. **Size is settled and is not the question.** §0 of the feasibility note was right about this.

**Two columns in this release the feasibility note does not mention, both relevant here:** `operating_status` (99.9% null in the UK food-and-drink slice, §1 above) and `basic_category` (a ~280-label flattening of the taxonomy, which turns out to be the better filter — §9.1).

---

## 3. The ground truth, and its limitations — stated loudly, as instructed

**Source: the Food Standards Agency's Food Hygiene Rating Scheme open API** (`https://api.ratings.food.gov.uk/Establishments`, retrieved 2026-09-18) [E]. Every food business in the UK must be registered with its local authority, so the register is a statutory census of operating premises with a business name, an address, a business-type classification and a geocode.

**Why this source and not another.** It is the most independent ground truth available to me:

- **It is independent of the dataset under test.** Overture's Places theme is fed by Meta, Microsoft, PinMeTo, Krick, RenderSEO, DAC, BrightQuery, Foursquare and AllThePlaces, and *"does not include OpenStreetMap data"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/), retrieved 2026-09-18]. FSA is on none of those lists. Every one of the 653 candidate rows I examined carried `Overture` plus one of `meta`, `Microsoft`, `Foursquare` or `AllThePlaces` as its source — no FSA-derived provider appeared [E, measured].
- **It is a register of *currently operating* businesses**, which is the property the junk question actually asks about, and which Overture's own `operating_status` field cannot supply here.
- **It is not a map product**, so it has no incentive to agree with one.

**Now the limitations, which are real and which cut in identifiable directions:**

1. **FSA geocodes are address-derived and carry their own error.** Measured directly: for the 77 venues I resolved, the median disagreement between the FSA geocode and the matched Overture coordinate was **12.0 m**, p75 17.0 m, p90 37.8 m, max 137.9 m [E, measured]. So my query point is not the venue's true position; it is *an* independent estimate of it. **This makes the hit rates in §4 a fair test rather than a rigged one** — a perfect query point would flatter the index — but it also means §4's "zero noise" case already contains ~12 m of median error, and the §5 noise figures stack on top of that.
2. **FSA registers the legal trading entity, which is sometimes not the sign above the door.** Examples from my own sample: `"Natalie White - The Compasses"`, `"Pong & Puck also T/as Bar Hutte and The Beach Club"`, `"Taza Catering T/A Eat Meat Steakshop"`. Where the registered name is a company rather than a venue, my matcher will score a miss that a human would not. I hand-reviewed every one of the 139 cases to catch this; of the 29 "absent" verdicts, **4** looked like legal-entity artefacts and the remaining 25 looked like genuine dataset gaps. That residual inflates my miss rate by at most ~3 percentage points. [E, measured; the adjudication is [J] applied case by case and is recorded in `handscores.py`.]
3. **FSA's business types include premises nobody "goes out" to.** `Restaurant/Cafe/Canteen` catches workplace canteens and bookshop cafés. I excluded 5 such cases by hand (a WeWork barista station, a Waterstones café, a meditation centre, a soft-play centre, a disability-services community café) and named every exclusion in §4.2 so the reader can disagree with me item by item.
4. **FSA is fresher than an Overture release.** A venue that opened in 2026 is registered immediately and may not have reached any of Overture's providers. This is not a flaw in the test — it *is* the currency risk a journal carries — but it means some of my "absent" verdicts are "absent yet", not "absent forever".

**Sample construction** [E, measured]. Three contrasting areas, chosen because the CTO's earlier work and the research brief both record that density varies enormously between them:

| Area | Character | Radius | FSA pubs/bars/nightclubs + restaurants/cafés in radius | Sampled |
| --- | --- | --- | --- | --- |
| Manchester city centre (53.4808, −2.2426) | dense city centre | 0.5 mi | 828 | 50 |
| Chorlton-cum-Hardy (53.4425, −2.2790) | suburb | 0.75 mi | 117 | 48 |
| Ludlow (52.3681, −2.7185) | small market town | 1.0 mi | 48 | 41 |

Sampling was random within each area, stratified to take up to 25 `Pub/bar/nightclub` and up to 25 `Restaurant/Cafe/Canteen` per area, seeded (`random.seed(20260918)`) so the draw is reproducible. **139 venues drawn; 132 scored; 7 excluded or marked ambiguous and named individually in §4.2.**

**The honest summary of all of that:** this ground truth is independent of the dataset under test, which is the property that matters most, and it is imprecise in position and occasionally wrong in name, which biases my measured hit rate **downward by a few points**. It does not bias it downward by twenty.

---

## 4. Metric 1 — top-N hit rate

### 4.1 Method

For each ground-truth venue: take its FSA coordinate, query the shipped index (`name IS NOT NULL AND confidence >= 0.5 AND taxonomy.hierarchy[1] = 'food_and_drink'`) for every row within 250 m, order by great-circle distance, take the top five. **I then read all 653 returned candidate rows myself** and adjudicated, for each venue, whether the correct venue appeared at rank 1, in the top three, in the top five, or not at all — rather than trusting a name-similarity matcher. (I ran one as a first pass; it disagreed with my adjudication on 15 of 139 cases in both directions, which is why the published numbers are the hand ones.)

Where the answer was "not at all", I searched the **entire** 3.3 M-row UK extract — every category, every confidence value — within 500 m for a name-similar row, in order to classify *why* the miss happened.

### 4.2 Results

**[E, measured this session. n = 132 scored venues.]**

| Area | n | Rank 1 | Top 3 | Top 5 | Miss |
| --- | --- | --- | --- | --- | --- |
| Manchester city centre | 48 | 9 (**18.8%**) | 23 (**47.9%**) | 26 (**54.2%**) | 22 (45.8%) |
| Chorlton (suburb) | 46 | 12 (**26.1%**) | 21 (**45.7%**) | 25 (**54.3%**) | 21 (45.7%) |
| Ludlow (small town) | 38 | 24 (**63.2%**) | 26 (**68.4%**) | 26 (**68.4%**) | 12 (31.6%) |
| **All** | **132** | **45 (34.1%)** | **70 (53.0%)** | **77 (58.3%)** | **55 (41.7%)** |

Median candidate count within 250 m: **171** in the city centre, 34 in the suburb, 42 in the small town [E, measured]. The dense case is not a harder version of the sparse one; it is a different problem — the top five is a 1-in-34 slice of what is nearby.

**Excluded from scoring, named individually so the reader can disagree:** `WeWork Barista Station`, `Waterstones` (Arndale), `Kadampa Meditation Centre Manchester`, `Monkey Mania` (soft play), `Working Together (Ludlow) Ltd Cafe` — not venues a person goes out to. Marked **ambiguous** and excluded: `Parkway Sandwich Bar` (two index rows named "Parkway lounge"/"ParkWay Lounge" 9 m apart — probably the same premises renamed, and I could not establish it), `3 Church Street` (an FSA record whose business name is its address). **Reported separately rather than excluded:** four sports and social clubs (`South West Manchester Cricket Club`, `Whalley Range Amateur FC`, `West Didsbury & Chorlton AFC`, `The Ludlow Club`). All four missed; all four for the same reason (§4.3). Dropping them raises the all-areas top-five rate from 58.3% to **60.2%** — it does not change the conclusion.

### 4.3 Why the misses happen — and the correction this makes to the framing I was given

Every miss was classified by searching the whole 3.3 M-row extract [E, measured]:

| Cause | n | What it means |
| --- | --- | --- |
| **ABSENT** | 29 (52.7%) | No name-similar row anywhere within 500 m, in any category, at any confidence. The venue is not in Overture. |
| **POS** | 15 (27.3%) | The correct row **is** in the shipped index but ranked out by distance. Measured offsets: 23–100 m for eleven of them; 220, 355 and 390 m for three (`Pizza Hut Restaurants`, `Rain Bar`, `Wingstop` — Overture rows placed in the wrong part of the city). |
| **CAT** | 9 (16.4%) | The row exists within 500 m but sits **outside the food-and-drink slice**. |
| **CONF** | 2 (3.6%) | The row exists in the food-and-drink slice within 500 m but at `confidence < 0.5`, so the filter removed it. |

**The Skeptic's objection is correct about the instrument and the measurement relocates the damage.** Overture's documentation, which I re-retrieved rather than taking second-hand, says: *"Confidence measures existence only, whether the record describes a real place rather than junk, and is independent of other attributes such as `operating_status`"*, and *"Places is known to contain duplicates, a high junk rate, and low property completeness. The confidence score (above) is the primary tool for filtering potential junk data; it does not address duplicates or property completeness"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/), retrieved 2026-09-18]. So `confidence >= 0.5` cannot be cited as a duplicate control, and the gate was right to say so.

But **`confidence >= 0.5` cost 2 misses out of 55, and the category scope cost 9** — and the category losses are systematic rather than random:

- **`Church Inn` (Ludlow) sits at 7.9 m, classified `inn` under `lodging`.** So does `The Charlton Arms` at 96.7 m. **Overture files 1,022 UK rows as `inn`, every one of them under `lodging`, entirely outside the food-and-drink slice** [E, measured]. A great many British pubs are called something-Inn and are classified accordingly. An index for a going-out journal that excludes them is excluding pubs by name morphology.
- **`Grosvenor Casino` (Manchester) sits at 12.2 m as `casino` under `arts_and_entertainment`.** `Vine & Juniper` (Ludlow) at 2.1 m as `liquor_store` under `shopping`. `Frog & Bucket Comedy Club` — a comedy club with a bar — is not in the slice.
- **Four venues sat within 25 m with a null category entirely** (`South West Manchester Cricket Club` at 4.7 m; `The Ludlow Club` at 21.7 m; `Cha Cha Chai Chorlton` at 12.6 m; `West Didsbury & Chorlton AFC` at 161.7 m). **209,570 named UK rows at `confidence >= 0.5` carry no taxonomy at all** [E, measured] — they are invisible to any hierarchy-based filter.

**This is a fixable finding and I am recording it as the most useful thing in this spike.** Nine of 55 misses — 16% — are a filter-design defect, not a dataset defect. §9.1 states the fix and what it costs.

---

## 5. The number the venue page actually depends on: stability under location error

§4 assumes the app queries at the venue's own position. It will not. `CLVisit` delivers a dwell-cluster centroid with a `horizontalAccuracy`, and the CTO's note records that visit monitoring also operates under **reduced accuracy** when the user declines precise location [E — `feasibility-note.md` §1.1, citing [Apple, `startMonitoringVisits()`](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits())].

**I have no measurement of real `CLVisit` error and I will not invent one.** Instead: re-run each query 20 times with an isotropic Gaussian offset at σ = 10, 25 and 50 m, and report the curve.

### 5.1 Does the correct venue stay in the list?

**Mean probability that the correct venue appears in the top five on a given simulated visit, conditional on it being findable at all (n = 77)** [E, measured]:

| Area | σ = 10 m | σ = 25 m | σ = 50 m |
| --- | --- | --- | --- |
| Manchester city centre | 84.2% | **51.9%** | 23.5% |
| Chorlton (suburb) | 95.4% | **79.0%** | 56.6% |
| Ludlow (small town) | 98.7% | **87.7%** | 74.0% |

Compounding with §4.2 — the chance a real visit to a real venue presents the right answer in the top five, at σ = 25 m:

- **Manchester city centre: ≈ 28%**
- **Chorlton: ≈ 43%**
- **Ludlow: ≈ 60%**

### 5.2 Does the *same* venue come first twice?

This is the venue-page question, and it is the one nobody has measured. Over 20 simulated visits to the same venue [E, measured]:

| Area | σ | Median distinct venues taking **rank 1** | Mean share held by the modal one | Venues whose rank 1 changed at least once |
| --- | --- | --- | --- | --- |
| Manchester | 10 m | 4 | 0.52 | 95.8% |
| Manchester | 25 m | **10** | 0.27 | **100.0%** |
| Chorlton | 25 m | 6 | 0.47 | 89.1% |
| Ludlow | 25 m | 5 | 0.54 | 81.6% |
| Manchester | 50 m | 15 | 0.16 | 100.0% |

**Read that as a product statement** [I, from the [E] above]: in a dense city centre, the nearest venue to a `CLVisit` centroid is a *different venue on essentially every visit*. Whatever the picker shows first, it is not stable across visits to the same pub. The UX seat's instruction that the design must **never auto-select** [`ux-note.md` §2.2] is not a style preference; on these numbers an auto-selecting design would produce a venue history that is close to noise. **Confirmed, and confirmed more strongly than the UX seat could have known without this measurement.**

### 5.3 The design lever, so the PM has a curve rather than a verdict

Recall at list length N, σ = 25 m, conditional on findability [E, measured]:

| Area | @1 | @3 | @5 | @10 | @20 | @50 |
| --- | --- | --- | --- | --- | --- | --- |
| Manchester city centre | 12.9% | 36.0% | 51.9% | **77.3%** | **92.5%** | 100% |
| Chorlton | 30.8% | 59.8% | 79.0% | 94.4% | 99.8% | 100% |
| Ludlow | 51.3% | 78.1% | 87.7% | 98.1% | 100% | 100% |

**A longer list is a real and cheap fix for recall, and it makes the picker worse.** Twenty rows of a dense high street is a scroll, not a glance, and the UX note designed the confirmation row for recognition-at-a-glance [`ux-note.md` §1.2]. The honest framing for the PM/BA is: *the index can find the venue if the UI is allowed to be a search screen rather than a five-row list.* That is a product decision, not an engineering one, and it belongs with the UX seat and the CEO. I am flagging it, not deciding it.

---

## 6. Metric 2 — duplicate rate in the top five

The UX seat asked for this specifically and said it matters more than the hit rate, because *"a duplicate splits a user's accumulated record silently, forever, with no server to repair it"* [`ux-note.md` §0.2]. The CEO's product inputs raise the stakes: the venue page is *"probably the product, not a feature"* [`proposals/haunt/ceo-product-inputs.md` §1].

### 6.1 The literal metric, measured

**Duplicate pairs appearing within a single top-five list: 7 lists of 137 = 5.1%** [E, measured; every flagged pair hand-adjudicated]. The confirmed ones:

| List | The pair | Apart | Source datasets |
| --- | --- | --- | --- |
| Manchester, "Wetherspoons" | `Manchester Weatherspoons Picadilly` / `Wetherspoon` | 7.4 m | meta / meta |
| Manchester, "English Lounge" | `English Lounge Manchester` / `English Lounge` | 2.6 m | AllThePlaces / meta |
| Manchester, "Rosa's Thai" | `One Eight Six` / `186` | ~10 m | meta / meta |
| Manchester, "Grand Central" | `The Terrace at The Refuge` / `The Refuge` | 14.9 m | meta / meta |
| Chorlton, ×2 lists | `Jamstreet Bar 209 Upper Chorlton Road` / `Jam Street Café` | 16.7 m | meta / Foursquare |
| Chorlton, "Parkway" | `Parkway lounge` / `ParkWay Lounge` | 9.3 m | meta / Foursquare |

**Taken at face value, 5.1% is a pass.** I do not think the reader should take it at face value, and §6.2 says why.

### 6.2 Why 5.1% understates the harm, and the number that does not

Two reasons the within-list rate is the wrong lens.

**(a) The top five is a ~20 m window in a dense centre, so most duplicates are too far apart to co-occur.** Searching the index itself rather than the returned lists, in an 800 m radius around Manchester city centre — 1,314 index rows — my detector flagged 48 name-similar pairs within 60 m, of which I hand-confirmed **19 as true duplicates**: `The Stage Door`/`The Stage Door`, `G-A-Y Manchester`/`G-A-Y`, `REM Bar`/`The Rem Bar`, `Fumo`/`Fumo`, `Black Sheep Coffee`/`Black Sheep Coffee`, `Creams Cafe Manchester Arndale`/`Creams Cafe Manchester Arndale`, `Gong Cha Market Street`/`Gong cha`, `Caffè Nero`/`Caffe Nero Group Ltd.`, `Starbucks Coffee`/`Starbucks`, `J D Wetherspoon`/`J D Wetherspoon Plc`, `Wright's Fish & Chip Shop`/`Wright's Fish and Chips`, `The Village Chippy`/`Village Fish & Chip Shop`, `Ocean Tr235ure`/`Ocean Treasure`, `Hansford's`/`Cafe Manchester by Hansfords`, `Oak Street Cafe`/`Oak Street Cafe Bar`, `GMEX Table Table`/`The Bishopsgate Table Table`, `English Lounge`/`English Lounge Manchester`, `Churchills`/`Bistro Bistro @ Churchills`, `The Restaurant Bar and Grill`/`Restaurant Bar and Grill at John` [E, measured + hand-adjudicated]. That is **≥38 of 1,314 rows (≥2.9%) being one half of a duplicate pair, and it is a floor**: my detector needs name similarity ≥ 0.70, so it cannot see `Manchester Weatherspoons Picadilly` ↔ `Wetherspoon` (0.49), `One Eight Six` ↔ `186`, or `Jam Street Café` ↔ `Jamstreet Bar 209 Upper Chorlton Road`, all of which I found by eye. **Overture says the same thing about its own pipeline:** it *"suffered from undermatching, cases where two records for the same place were not recognized as duplicates, especially when records are more than 100 meters apart or have only moderately similar names"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/), retrieved 2026-09-18].

**(b) The splitting mechanism the UX seat described is temporal, and §5.2 measures it directly.** A user does not need two rows in one list to split their history. They need the *ranking* to differ between March and June. At σ = 25 m in a city centre that happens **100% of the time**, with a median of ten different venues taking first place across twenty visits. Where two of those ten are duplicates of the same pub, the split follows automatically — and the user is choosing honestly from an honest list each time.

**So: the duplicate rate in the top five is 5.1%, and it is not the number that should decide anything.** The number that should is 100% rank-1 instability plus ≥2.9% index-level duplication. The first makes *merge* necessary regardless; the second makes it necessary even for a perfectly stable picker.

**Recorded as a disagreement with the metric as specified, not with the seat that specified it.** The UX seat asked for the right thing for the right reason and named the exact harm; the measurable proxy it chose happens to be the insensitive one. I would not have known that without running it either.

---

## 7. Metric 3 — junk rate in the top five

**Definition used:** a candidate is junk if it is not a real, currently-operating, user-recognisable venue at approximately the returned location. I classified on **positive indicators only** — unfamiliarity is not evidence.

**Two independent measurements, both pointing the same way.**

**(a) Hand adjudication.** Random 100 of the 410 distinct rows that appeared in any top five (seeded, `random.seed(31337)`), each read with its category, confidence, source datasets and nearest FSA registration [E, measured + [J] adjudication]:

- **~2 clear junk** (`G-Spot`, a gay bar in a town of 11,000 with no corroboration at any radius, confidence 0.57; `renae`, confidence 0.58, no corroboration).
- **~4–6 uncertain or stale** — chiefly rows carrying a superseded name for a real premises (`The Smithfield Social` where FSA registers `Thomas Street Social LTD` 5 m away; `D'Grand Restaurant` where FSA has `Koreana Restaurant` 34 m away) and one truncated name (`Restaurant Bar and Grill at John` — the street is John Dalton Street).
- **The other ~92 were real venues**, most of them corroborated by an FSA registration of the same name within 40 m.

**(b) An independent occupancy test.** For each of the 410 distinct candidate rows, is there *any* FSA-registered food business within 50 m / 100 m? A currently-operating food or drink venue in the UK is a registered food business, so a row with no registered premises anywhere near it is likely closed, imaginary, or misplaced [E, measured]:

| Area | No FSA premises within 50 m | within 100 m |
| --- | --- | --- |
| Manchester city centre | 1 / 210 (0.5%) | 0 / 210 (0.0%) |
| Chorlton | 10 / 119 (8.4%) | 4 / 119 (3.4%) |
| Ludlow | 10 / 81 (12.3%) | 3 / 81 (3.7%) |
| **All** | 21 / 410 (5.1%) | **7 / 410 (1.7%)** |

The seven orphans at 100 m: `Bowling Green Chorlton`, `Little Seedlings Baby and Toddler Group` (a toddler group classified `cafe`), `Bar M60`, `World Peace Cafe`, `Costa` (Ludlow), `The Kingfisher`, `Ludlow Brewing Co` — of which at least four are real venues whose Overture coordinate is simply offset. So 1.7% is itself an over-count.

**Finding: the junk rate in the top five is low — on the order of 2%, and below 5% on any reading. This is a clean pass and I am reporting it as one.** The CTO's `confidence >= 0.5` filter is doing precisely the job Overture documents it for, and the UX seat's worry that *"the list is embarrassing on first run"* [`ux-note.md` §2.4] is not borne out. The list's problem is that the right answer is often not in it — not that the wrong answers are absurd.

**Two honest caveats.** (i) **Closed venues are invisible to me**, so this is a lower bound; `operating_status` is null for 99.9% of the slice and cannot help. (ii) I found a handful of clearly-miscategorised rows in the wider index that would reach a user — `Piccadilly Cars` (a taxi firm) classified `restaurant`; `MERKUR Slots - Manchester Deansgate` classified `chicken_wings_restaurant`; `Chinatown Manchester` and `Pekan Cina Manchester`, two rows 1.7 m apart for a *district* rather than a venue [E, measured]. These are rare enough not to move the rate and real enough that a user will eventually see one.

---

## 8. Metric 4 — coverage sanity check

The research brief records OSM at **84,326** UK pubs/bars/clubs/restaurants against a licensed-premises universe of roughly **99,000** (CGA by NIQ, December 2025, via two outlets reporting one paywalled report — *single origin*, as `feasibility-note.md` §2.3 flags).

The equivalent Overture subset, named at `confidence >= 0.5`, using the release's `basic_category` flattening [E, measured]:

| | Count |
| --- | --- |
| `basic_category = 'bar'` (pub, bar, cocktail bar, wine bar, gastropub, Irish pub, sports bar, …) | **68,897** |
| `basic_category IN ('bar','restaurant')` — the OSM-equivalent scope | **187,098** |
| For reference: OSM pub+bar+nightclub+restaurant | 84,326 |
| For reference: UK licensed premises (CGA/NIQ, Dec 2025, single origin) | ~98,914 |

**Finding: Overture is not coverage-deficient. It is coverage-*excessive* — roughly 2.2× OSM and 1.9× the licensed-premises universe on the closest comparable scope** [I, from the [E] counts above]. The excess is only partly explained: `basic_category = 'restaurant'` legitimately contains unlicensed restaurants and cafés that are not licensed premises, so the ratio is directional rather than a defect count. But the direction is unambiguous, and combining it with §4 gives the finding that matters:

> **The index holds roughly twice as many rows as there are licensed premises in the country, and still fails to surface the right venue in 42% of cases.** That is not a recall problem that more data fixes. It is a precision-and-ranking problem, and adding rows makes it worse, because every extra row in a dense centre is another thing in front of the answer.

The feasibility note's conclusion that *"neither open dataset looks materially deficient for UK 'going out'"* [`feasibility-note.md` §2.3] is **correct on coverage and does not transfer to correctness**. The idea that an offline dataset means *worse coverage* was the wrong worry; the right one was always *worse disambiguation*, and nobody had measured it.

---

## 9. What the numbers mean for the design

### 9.1 The cheap fixes, in the order I would do them

**(a) Replace the category filter. ~half a day; recovers 16% of misses.** [J, high confidence, grounded in §4.3]
The `taxonomy.hierarchy[1] = 'food_and_drink'` predicate is losing pubs classified as `inn` under `lodging` (1,022 UK rows), casinos, comedy clubs, social clubs, and everything with a null taxonomy (209,570 named UK rows at conf ≥ 0.5). Replace it with an explicit allow-list built on `basic_category` **plus** a named set of out-of-hierarchy categories (`inn`, `casino`, `social_club`, `comedy_club`, …) **plus** a rule for null-taxonomy rows near the user. This grows the index — §2 shows the whole thing is 23 MB, so size does not constrain the decision (Constitution 1.5 is satisfied either way: the marginal running cost is still £0).

**(b) Stop ranking on raw distance alone.** [J] At σ = 25 m in a city centre, distance ordering is close to a random draw from the block (§5.2). Anything that breaks the tie non-positionally — dwell duration against opening hours, category against time of day, the user's own history — improves stability. I have not measured any of these and I am not recommending one; I am recording that **the current ranking is the measured weak point** and that `confidence` must not be the tie-breaker, because Overture says it measures existence and nothing else (§4.3).

**(c) Make list length a settable number, not a constant of 5.** §5.3 is a curve the PM/BA should choose a point on with the UX seat, and the choice differs by density.

### 9.2 The UX seat's three MVP asks — supported, with one correction

| UX ask (`ux-note.md` §2.3) | My measurement | Verdict |
| --- | --- | --- |
| **Merge venues** | ≥2.9% of city-centre index rows are one half of a confirmed duplicate pair, a floor (§6.2); Overture documents undermatching as a known pipeline weakness | **Supported. MVP.** The UX seat asked whether merge could wait. On these numbers it cannot. |
| **Sticky choice** | 100% rank-1 instability at σ = 25 m in a city centre; median 10 distinct rank-1 venues over 20 visits (§5.2) | **Supported, and it is the highest-value item — but it must be built as a *ranking* input, not as a shortcut.** The UX seat called it *"the single highest-value interaction in the whole product"*. My measurement says that is right and adds a constraint the note does not carry: at 50 m a Manchester cluster contains ~40 venues, so "remember the choice for this cluster and offer it first" will confidently offer the wrong pub when the user goes next door. Sticky choice must **raise** previously-chosen venues in the list, never pre-select one — which is also what Article 4 requires (`ux-note.md` §2.2: a pre-selected candidate is a pre-ticked box). |
| **Rename in place** | 29 of 55 misses are absent rows; several confirmed cases of Overture carrying a superseded trading name (§7) | **Supported. MVP.** |
| CTO's **"this venue isn't listed"** path | 22% of all sampled venues (29/132) are absent from Overture entirely | **Necessary and, as the UX seat said, not sufficient.** At a 22% absence rate this is not an edge case — it is one visit in five in the suburb and small-town samples, and it must be a first-class path, not a fallback at the bottom of a list. |

### 9.3 The hazard nobody has specified, and it is the cheapest line in this document

The UX seat raised it and no artifact has turned it into a requirement [`ux-note.md` §2.3, "A fourth hazard nobody has written down: dataset refresh"]:

> **A dataset refresh must not mutate venue rows already referenced by a user's visit.**

**The measurements make this concrete rather than theoretical.** Overture's own documentation states that *"a place whose records are conflated consistently keeps the same GERS ID from release to release, while inconsistent conflation causes identities to split or merge as source data shifts"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/), retrieved 2026-09-18], and the same page documents a taxonomy overhaul in this release cycle that **repathed 2,108 categories, renamed 407 and removed 80**, with hierarchy changes called out as *"Critical"* and *"especially in areas like `food_and_drink`"* [E, verbatim, same source]. So between two releases, a row referenced by a user's 2027 visit can change its name, its position, its category, its hierarchy path and its GERS ID — and a merge upstream can make two of the user's venues into one, or a split can make one into two.

The CTO's data-layer commitment already points the right way — *"venue identity is a Candour-owned local row"* carrying the GERS ID *"as an attribute, never as the only handle"* [`feasibility-note.md` §3]. **That commitment is necessary and not sufficient**, because it settles the *identifier* and says nothing about the *fields*. The requirement I would have the PM/BA write, stated as acceptance criteria:

1. **On first reference, the venue row is copied, not pointed at.** The moment a visit references a venue, the user-visible name, coordinate and category are frozen into the Candour-owned row. The GERS ID remains an attribute.
2. **A refresh may add unreferenced rows and update unreferenced rows. It may never write to a referenced row.**
3. **Changes to referenced rows are offered, never applied** — an explicit, optional, reviewable action the user can decline, and declining is the default.
4. **A user's rename always outranks the dataset, permanently and across refreshes.**
5. **User merges survive refreshes**, including a refresh that re-splits the upstream records the merge joined.

**Cost now: part of the schema, effectively free.** Cost later: there is no server, no telemetry and no backfill (`feasibility-note.md` §2.6, §5), so a refresh that corrupts referenced rows is **permanent, silent, and undiscoverable by Candour**. The CEO's product inputs make the venue page the product's only surviving differentiator; this is the mechanism by which a data release quietly rewrites it.

**This is a flag, not a block.** My charter gives me no blocking power (`roles/engineer.md`); I am raising it to the owning seats — PM/BA for the acceptance criteria, CTO for the architectural constraint — rather than building through it, which is what my charter requires instead.

### 9.4 One item for the CFO, unprompted

The CTO's post-launch model carries *"venue dataset refresh (re-run pipeline, ship with app update) ~0.5 day/month"* [`feasibility-note.md` §6.4, tagged [J]]. §9.3 turns a refresh from a re-extract into a **reconciliation** — diffing GERS identities across releases, detecting upstream splits and merges, and preparing a reviewable change set that respects user renames and merges. That is a different job with a different cost, and it recurs monthly for the life of the product. **Condition 1's re-derivation should be told about it**, on the same basis that `ceo-product-inputs.md` requires the CFO to be told about session segmentation before it runs rather than after.

---

## 10. Verdict, and what would overturn it

### 10.1 The verdict

**The offline Overture-derived index is not shippable as specified, as the venue source for a product whose core value is an accurate per-venue history.**

The case, in three lines:

- At a perfect location fix it surfaces the right venue in the top five **58.3%** of the time, and **54.2%** in a dense city centre [E, §4.2].
- At a 25 m query error — modest for a visit centroid — the compound figure for a dense city centre is **≈ 28%** [E, §5.1].
- The rank-1 candidate for the same venue changes on **100%** of dense-centre venues across twenty simulated visits [E, §5.2], which is the mechanism that splits a venue page, and there is no server and no backfill to repair it.

**This is a "not yet", not a "never", and the distinction is load-bearing.** The two metrics that would have been fatal came back clean: **junk is ~2%** (§7) and **coverage is nearly 2× the licensed-premises universe** (§8). The failure is in the query layer — category scoping (16% of misses, §4.3), distance-only ranking (§5.2), and a fixed list of five (§5.3) — plus a 22% genuine absence rate that the "isn't listed" path already anticipates. Those are things Candour controls.

**What I am explicitly *not* saying.** I am not saying the product should be killed. That is the CEO's decision under Constitution 5.4 and nothing in this note pretends otherwise. What I am saying is narrower and firmer: **requirements should not be signed off against the index as `feasibility-note.md` §2 specifies it**, because the version measured here would ship a venue page that is quietly wrong, in the one feature the CEO identified as the product [`ceo-product-inputs.md` §1]. A revised index specification with §9.1's fixes, re-measured against the same ground truth, is a cheap next step — the harness in §11 re-runs in about ten minutes — and it is the honest route to a sign-off.

### 10.2 What would overturn this finding, and where I looked

*(Required by `roles/engineer.md` as amended: a negative finding carries a block's duty.)*

**Overturned by any of these:**

1. **A category filter rebuilt per §9.1(a), re-measured, showing a top-five rate above ~80% in the dense case.** This is the most likely of the four and it is half a day's work. 16% of misses are category-scoping, so the ceiling this alone can reach is roughly 58% → 67% at zero noise; **it is not on its own sufficient**, which is why it is listed first and alone is not enough.
2. **Real `CLVisit` accuracy materially better than σ = 25 m.** Every figure in §5 is a function of that number and I could not measure it. If real visit centroids land within ~10 m, the dense-centre recall@5 goes from 51.9% to 84.2% and the verdict weakens considerably. **This is the single highest-value missing fact in this note**, it needs a phone and two weeks, and it is already budgeted — `feasibility-note.md` §8 item 3 asks the Engineer to measure battery over a real week during build. **Measure accuracy on the same run.** I looked for a published figure in Apple's `CLVisit` and `startMonitoringVisits()` documentation via the CTO's retrieved citations and found none; the CTO records the same absence for battery.
3. **A ranking signal that restores rank-1 stability.** §5.2 is the finding that makes the venue page unsafe. If a non-positional tie-breaker takes the modal rank-1 share from 0.27 to above ~0.8 in a dense centre, the splitting mechanism largely closes and merge becomes a safety net rather than a necessity. I did not test any such signal and I am not claiming one works.
4. **A different or supplementary dataset closing the 22% absence rate.** I did not test one. OSM is the obvious candidate — 38,555 UK pubs and 7,424 bars [E, `feasibility-note.md` §2.3] — and it carries **ODbL share-alike**, which the CTO records as a commitment *"the gate should make knowingly rather than inherit by accident"* [`feasibility-note.md` §2.2]. That is a licence decision, not mine.

**Where I looked, so a reader can check I looked in the right places:**

- **The dataset itself, in full.** The complete UK bbox extract of Overture Places `2026-08-19.0` — 3,325,607 rows — materialised locally and queried directly. Not a sample, not a summary, not someone else's count.
- **The whole 3.3 M-row extract for every single miss.** Each of the 55 misses was searched across every category and every confidence value within 500 m before being classified, which is how the CAT and CONF distinction in §4.3 exists at all.
- **Three contrasting areas**, chosen for density contrast rather than convenience, with 132 hand-adjudicated venues and all 653 returned candidate rows read individually.
- **Both directions of the filter question.** I built the index twice — with and without `confidence >= 0.5` — so the filter's cost is measured rather than argued.
- **Overture's own documentation, re-retrieved this session** rather than taken from the Skeptic's or the UX seat's quotation of it, including the confidence-score section, the conflation and undermatching discussion, and the taxonomy change summary.
- **An independent statutory register** (FSA FHRS) for ground truth, whose independence from Overture's provider set I verified against the `sources` column of every candidate row.
- **Where I did *not* look:** I did not visit a venue, did not run the code on a phone, did not test OSM or a hybrid index, and did not test any alternative ranking function. Each of those is named in §10.2 as a route to overturning this, and none of them is expensive.

---

## 11. Reproduction and evidence register

**Everything below was retrieved or measured on 2026-09-18. Nothing is cited from memory.**

**Measurements taken this session** *(working scripts and intermediate data in the session scratchpad; each is a short single-purpose file and the whole chain re-runs in ~10 minutes on a laptop)*:

| Script | What it measures | Section |
| --- | --- | --- |
| `extract.py` | UK bbox extract from Overture `2026-08-19.0` via DuckDB 1.5.5 + httpfs over the public S3 bucket | §2 |
| `build_index.py` | SQLite indexes, with and without the confidence filter; on-disk and gzipped sizes | §2 |
| `fsa.py`, `sample.py` | FSA ground truth retrieval and seeded stratified sampling | §3 |
| `query.py`, `diag.py`, `handscores.py` | top-5 queries, whole-extract miss diagnosis, hand adjudication | §4 |
| `stability.py`, `recall_noise.py`, `tradeoff.py` | rank-1 instability and recall@N under Gaussian query error | §5 |
| `dupjunk2.py`, `dupdensity.py` | duplicate pair detection within lists and index-wide | §6 |
| `junksample.py`, `occupancy.py` | junk adjudication sample and the FSA occupancy test | §7 |

**Data sources**

- Overture Maps Places, release `2026-08-19.0`, `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/` — CDLA-Permissive-2.0. Bucket listing confirming the release, and the extract itself, retrieved 2026-09-18.
- [Overture Maps — Places guide](https://docs.overturemaps.org/guides/places/), retrieved 2026-09-18 — confidence score semantics (*"Confidence measures existence only… independent of other attributes such as `operating_status`"*); known quality issues (*"duplicates, a high junk rate, and low property completeness… it does not address duplicates or property completeness"*); conflation and undermatching; the taxonomy change summary; *"The places theme does not include OpenStreetMap data"*.
- [Food Standards Agency, Food Hygiene Rating Scheme API](https://api.ratings.food.gov.uk/Establishments) (`x-api-version: 2`), retrieved 2026-09-18 — ground-truth establishments for the three sample areas. Crown copyright, Open Government Licence.

**Figures travelling from other Candour artifacts, attributed and not re-retrieved by me**

- `products/haunt/feasibility-note.md` §2.3, §2.4, §3, §6.4 — the CTO's counts, sizes, OSM Overpass figures, data-layer commitments and refresh cost. I re-derived §2.3's and §2.4's numbers independently (§2 above); I did not re-run the Overpass query.
- `products/haunt/ux-note.md` §0, §1.2, §2.1–§2.4 — the duplicate/merge/sticky/rename findings and the dataset-refresh hazard.
- `research/haunt-brief.md` — the OSM 84,326 figure and the ~99,000 licensed-premises denominator (CGA by NIQ via two outlets reporting one paywalled report; **single origin**, flagged in the feasibility note and flagged again here).
- `proposals/haunt/ceo-product-inputs.md` §1 — the venue page as the product.
- Apple `CLVisit` / `startMonitoringVisits()` behaviour — [E, retrieved by the CTO seat 2026-09-09]; I did not re-retrieve, and nothing in this note depends on a detail beyond what §5 states.

---

*Prepared by the Engineer seat under `roles/engineer.md`. This note prepares and flags; it does not certify (Constitution 6.1). It holds no block — the Engineer has none — and the requirements sign-off it bears on is the PM/BA's and the CEO's. Condition 2 of `decisions/2026-09-16-haunt-gate.md` says the spike's result may kill the product and that this is the point. The result is above; the decision is not mine.*

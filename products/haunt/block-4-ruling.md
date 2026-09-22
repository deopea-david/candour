# Block 4 — ruling

**Seat:** Chief Technology Officer · **Date:** 2026-09-21 · **Status:** Ruling on a block this seat declared. **Prepares and flags; does not certify** (Constitution 6.1). Kill/proceed is the CEO's alone (Constitution 5.4). Only the CEO may overrule a block (Constitution 5.6).

**Block declared at:** `products/haunt/subscription-sizing-note.md` §11 (CTO, 2026-09-19).
**Evidence before me:** `products/haunt/venue-index-spike.md` (Engineer, 2026-09-18), `products/haunt/venue-index-remediation.md` (Engineer, 2026-09-20), `products/haunt/venue-index-nameseach.md` (Engineer, 2026-09-21).
**Decisions bearing on it:** `decisions/2026-09-16-haunt-gate.md` Condition 2, Condition 8.6, D3, D8.

**Template note:** `pipeline/templates/` holds nine files and none of them is a ruling [E, listed from disk 2026-09-21: `cost-sheet.md`, `decision-record.md`, `dissent-memo.md`, `gate-pack.md`, `idea-brief.md`, `proposal.md`, `requirements.md`, `research-brief.md`, `review-pack.md`]. Structure follows the five questions put to this seat, plus the overturn clause my amended charter requires. The deviation is stated rather than made silently. §6 is written in the requirements template's own units so the PM/BA can lift it.

**Method.** Held to `pipeline/amendment-verification.md` §1: **exhaustive, not sampled, on the load-bearing claims**; sources read whole rather than in part; **a clean pass reported as a clean pass when it is the honest one**. Every external source in §5 was retrieved at primary by this seat this session rather than carried from the CGO's or the Engineer's retrieval of it. Evidence tagged per `pipeline/evidence-standard.md`.

---

## 0. The ruling, before the working

**Block 4 STANDS, on limb (b) alone. Limb (a) is discharged. What remains is achievable before a build, is measured in days of writing rather than weeks of measurement, and needs no overrule.**

Six answers.

1. **Limb (a) — discharged, on a corrected specification, and the correction is of my own error.** As I wrote it, limb (a) demanded a modal rank-1 share above 0.8 and top-five recall above 80%. Those measure **list position**. The block's own stated grounds — Condition 8.6, *"derived views never lie about the user's own life"* — are about **identity**. I wrote the bar in the units of the instrument that existed on 18 September rather than in the units of the harm I was blocking. That is my defect, not the Engineer's, and it is the reason limb (a) as written is unliftable by any design that is actually correct. §3.2.

2. **On the quantity the block is actually about, the design passes, non-circularly.** 100.0% single-identity in a dense city centre at σ = 25 m; 98.0% under the harshest single-query policy; **≥95.9% on an adverse bound that assumes every judgment call the Engineer made went against it**; flat from three visits to forty; no eviction of the neighbour. Against the as-specified index's **2.0% after forty visits**. [E, `venue-index-nameseach.md` §6, §7.2]

3. **Limb (b) — not met, and it is the whole of what is left.** Limb (b) requires the five schema criteria to be *"in the requirements document and in the schema, not in a backlog."* They are in a spike note, drafted by a seat that holds no authority to put them anywhere. There is no requirements document. **A criterion in an engineer's note is a good idea; a criterion in the requirements document is a thing QA can fail a build on.** §2.2.

4. **The bar question is settled here, because it is my block and the misspecification was mine.** The governing quantity is **identity, not list position**. The 0.8 rank-1 threshold is **withdrawn as a pass criterion and retained as a reported metric**. P1–P4 as the Engineer pre-registered them are adopted as limb (a), **with a fifth criterion I am adding that the Engineer did not propose**, so the substitution is not a pure relaxation. The *threshold values* remain the PM/BA's with UX and QA, per open question 5, and if they move one the block re-tests against the moved one. §3.

5. **D8 answers the silent-corruption finding in part and relocates it in part, and D8's own text overclaims on this.** D8 records that *"D8's mitigations meet that reservation."* They do not meet it; they **shrink it and change its character**. The residual is the rate at which a user confirms the wrong row, which the Engineer's simulation sets to **zero by assumption** while measuring two hazards that say it will not be zero: a name-similar wrong venue first on **3.6%** of typed queries, and the confirmation prior putting last week's pub first on **57.5%** of visits next door. That is my disagreement, stated once, in writing. §4.3. **The answer the CVO's reservation actually has is not D8 — it is that a user-made error is visible and repairable where a coordinate-made one is not**, and that answer costs a requirement: merge and rename must be MVP and reachable. §4.4.

6. **Both technical questions: the CVO's answer to the CEO is right on the first, and I recommend against the second on cost rather than on licence.** A spatial index cannot improve accuracy — SQLite's own documentation says an R\*Tree *"does not normally provide the exact answer but merely reduces the set of potential answers"* [E, retrieved this session]. Venue footprints are a real mechanism that fires on a **minority** of draws at the error model this whole spike runs on, add a second silent-corruption surface, and are bought against a metric that already passes. **And the licence objection is not the reason** — Overture Buildings is ODbL and would be a share-alike accident, but Microsoft's UK building footprints are CDLA-Permissive-2.0, so a permissive route exists and the recommendation must stand on its own merits. It does. §5.

**What the CEO would be overruling if he overruled this, stated plainly as question 5 asks:** not a measurement, not a spike, not a doubt about whether the venue page can work. He would be overruling *"write the schema rules down before you write the schema."* §2.3 says what that costs.

---

## 1. What I was asked, what I did, and what I could not do

**Asked:** rule on Block 4; settle which bar governs; assess D8 on the merits; answer two technical questions; and say what goes in the requirements document, or what an overrule would be overruling.

**What I did.** Read `constitution.md` v1.3 in full from disk; `roles/cto.md` as amended; `pipeline/evidence-standard.md` v1.1; `decisions/2026-09-16-haunt-gate.md` in full — all 395 lines, Conditions 1–10, Corrections C1–C6, decisions D1–D8; the three Engineer spike notes in full; `pipeline/amendment-verification.md`; `products/haunt/compliance-note.md` §2 on the licence surface; `products/haunt/android-and-stack-note.md` §3.2 and §5 on the spatial index; and my own `subscription-sizing-note.md` §11 where the block was declared. Retrieved four external sources at primary this session (§9).

**What I could not do, stated before the conclusions rather than after them.**

- **I did not re-run the harness.** I read the Engineer's method, its own contamination analysis, its adverse bound and its stated failures, and I checked that its numbers are internally consistent with the two prior notes they claim to supersede. That is verification of an argument, not independent measurement. Per `pipeline/evidence-standard.md`, re-derivation by a second agent seat *"does not extend to interpretation, because a second pass inherits the first pass's reading."* **The 100.0% is the Engineer's measurement and I am relying on it**, with the reliance named.
- **Nobody has measured `CLVisit` accuracy.** Every σ in every note is an assumption. This is still the single highest-value missing fact about this product, it has been named as such in three consecutive notes, and it **cannot be obtained before a build** because it needs the app on a phone. §8 makes it a standing condition with teeth rather than a flag.
- **There is no usability evidence and no user.** §4's entire analysis of D8's residual is reasoning from measured hazards to an unmeasured rate. It is tagged accordingly.
- **I did not open a footprint dataset.** §5.2's technical answer is derived from the error model the spike itself uses, and §5.2 says what would overturn it and what it would cost to find out.

---

## 2. The ruling, limb by limb

Block 4 as declared has two limbs and I wrote that neither alone suffices. That stands. Each is ruled on separately.

### 2.1 Limb (a) — DISCHARGED, on a corrected specification

**What limb (a) said:**

> *"The §8.2 remediation spike returns a **modal rank-1 share above 0.8 at σ = 25 m in a dense city centre and top-five recall above 80%**, on the Engineer's own harness and ground truth, against a pass criterion agreed with the PM/BA, UX and QA **before** the spike runs."* [E, `subscription-sizing-note.md` §11, read from disk 2026-09-21]

**Against that text, the design fails and has never stopped failing:** modal rank-1 share **0.67** against 0.8, top-five recall **53.1%** against 80% — identical to the digit across both post-baseline notes, because name search acts on neither quantity [E, `venue-index-nameseach.md` §7.1; `venue-index-remediation.md` §8.1]. The Engineer reported that unprompted, first, before its own good result, and refused to let the good result obscure it. That is the behaviour this pipeline is supposed to produce and it deserves recording.

**I am nonetheless discharging limb (a), because the text above is a defective specification of my own block, and §3 sets out why on grounds that do not depend on the result.** The short form: the block's stated grounds are Condition 8.6 and *"unsustainable by design"*, both of which are about the **identity a venue page accumulates**; the bar is denominated in **which row sat in position one**; and the two quantities are now measured to come apart in both directions. A bar that fails correct designs and passes dangerous ones is not a bar.

**On the corrected specification, limb (a) is met.** [E, `venue-index-nameseach.md` §7.2, measured without the oracle]

| # | Criterion | Threshold | Measured | Result |
| --- | --- | --- | --- | --- |
| P1 | Single-identity rate, dense centre, σ = 25 m, ≥ 20 visits | ≥ 95% | **100.0%** headline · 98.0% harshest policy · **≥95.9% adverse bound** | **PASS** |
| P2 | P1 at 40 visits within 2 pp of P1 at 3 visits | ≤ 2 pp | **0.0 pp** | **PASS** |
| P3 | Neighbour recall within 2 pp of the prior-disabled design | ≤ 2 pp | **0.0 pp** (75.0% with and without) | **PASS** |
| P4 | Single-identity rate at σ = 50 m | ≥ 90% | **93.9%** headline · **89.8%** harshest policy | **MARGINAL PASS** |
| P5 | *(added by this ruling — a requirements criterion, ruled under limb (b))* | — | — | §3.4 |

**Three properties of that pass that I checked rather than accepted.**

1. **The comparison is to a published floor, not to a fresh claim.** The 81.6% non-circular floor and the 100.0% circular oracle were both published on 2026-09-20, before the measurement that landed between them, and both reproduce to the digit in the later session [E, `venue-index-nameseach.md` §3]. A result that lands on a pre-published ceiling is a checkable claim.
2. **The pass survives the Engineer's own adversarial treatment of it.** §5.5's bound assumes every venue it adjudicated as a rescue is instead a failure: **95.9%, still above 95%**. §6's `t1` row uses the single worst-performing query policy: **98.0%**. The pass does not depend on the generous reading.
3. **P4 is reported as marginal and I am not upgrading it.** 89.8% at σ = 50 m under `t1` is a fail by 0.2 pp. §8 carries it as a standing condition rather than smoothing it into the pass.

**Limb (a) is discharged. It is not discharged forever** — §8 states the two measurements that re-engage it.

### 2.2 Limb (b) — NOT MET, and it is the whole of what is left

**What limb (b) said:**

> *"The five acceptance criteria at `venue-index-spike.md` §9.3 — copy-on-reference; refresh may write only to unreferenced rows; changes to referenced rows offered and never applied, declining by default; user renames outrank the dataset permanently; user merges survive a re-split — are **in the requirements document and in the schema**, not in a backlog."* [E, `subscription-sizing-note.md` §11]

**Status: prepared, not met.** `venue-index-remediation.md` §11 restates them as six testable acceptance criteria — AC-1 through AC-6 — with four schema preconditions (`venue`, `venue_ref`, `venue_merge`, `refresh_proposal`) and the QA test that demonstrates each. **AC-6 is new** and the Engineer added it on evidence nothing in this repository carried: Overture's own documentation warns that its July 2026 release *"re-matches the corpus with the new pipeline, so users should expect a one-time elevated level of GERS ID churn"* — one release before the one Haunt is built on [E, `venue-index-remediation.md` §10, quoting the Overture Places guide retrieved by that seat 2026-09-20; **attributed, not re-retrieved by me**]. So a reconciliation that joins on GERS ID alone mis-joins precisely where churn is highest. That is a real addition and I adopt it.

**The Engineer's own statement of why this does not discharge the limb is correct and I am not softening it:** *"A criterion drafted by the Engineer is not a criterion in the requirements document."*

**Why this is a real architectural constraint and not a procedural hostage.** I tested it the way my charter requires — by asking what happens if it is skipped:

- AC-2's rule (a refresh may never write to a referenced row) is enforceable in the schema by a trigger and **unenforceable afterwards**. Once a shipped refresh has mutated referenced rows on a user's device, there is no server, no telemetry and no backfill (`feasibility-note.md` §2.6, §5), so Candour cannot identify which devices are affected, which rows moved, or what they said before.
- AC-5 and the `venue_merge` table make a user's merge a **durable fact** rather than a derived property of the index. Retrofitting that after visits exist means reconstructing merges that were never recorded.
- **This is the definition of an architectural constraint under my charter: cheapest now, unavailable later.** It is the same reasoning that made me carry it as limb (b) in the first place, and nothing since has weakened it.

### 2.3 The ruling, and exactly what lifts it

**BLOCK 4 STANDS.** It stands on limb (b) and on nothing else.

**What lifts it — one thing, fully specified:**

> **A requirements document for Haunt, signed off, containing: AC-1 through AC-6 and the four schema preconditions at `venue-index-remediation.md` §11; the three D8 constraints as acceptance criteria; and the five additions at §6 of this ruling. Verbatim or better — a PM/BA is free to write them more tightly, not more loosely.**

**Is that achievable before a build rather than after? Yes, and it is the first thing a build does.** Constitution 5.1 defines the build phase as *"requirements → architecture → build → verification"*, so writing requirements is not blocked by a block on build commencement — it is the route through it. Gate Condition 2 already places the spike *"before requirements are signed off"*, which is the same sequencing. **The work is drafting, by the PM/BA with UX and QA, from source material that already exists in two published spike notes. It needs no measurement, no device, no spike and no new evidence.** I estimate it at **2–4 days** of PM/BA time including UX and QA review [J], against the 2,090-hour build it gates.

**A clarification of my own block's scope, recorded because without it the block is circular.** *"Build commencement"* in Block 4 means **requirements sign-off and any code written against the venue index**. It does not and never meant the drafting of requirements, which is the act that lifts it. I am stating this as a clarification rather than a change because limb (b) always presupposed a requirements document it could be written into, and a block that forbids the only thing that could lift it would be a block I had no business declaring.

**No overrule is needed and I would advise against one.** Under Constitution 5.6 the CEO may overrule any block and the record would carry it. But an overrule here buys a few days at the price of the one defect class this architecture cannot recover from, and the CEO would be overruling a requirement to write down rules the build has to implement regardless. **The efficient path and the safe path are the same path, which is not always true and is worth saying when it is.**

### 2.4 Blocks 1, 2 and 3 — status, so this ruling is not mistaken for a general clearance

- **Block 1** (an architecture persisting places-API venue records): **avoided, not lifted.** Unchanged. Re-engages on any architecture touching a places API.
- **Block 2** (Android MVP resting on undocumented OEM behaviour): **engaged**, and D1's two-platform decision keeps it engaged. Lifted only by the published device-matrix spike with a pre-agreed minimum capture rate and a measured gap-detection accuracy. **Nothing in this ruling touches it, and it is the larger of the two live blocks by build risk.**
- **Block 3** (JavaScript in the visit-recording path, extended to the entitlement read): **engaged.** Unchanged.

**This ruling disposes of one block of four. Two remain live.**

---

## 3. Which bar governs — settled here

Open question 5 of `subscription-sizing-note.md` §12 records the pass criterion as unowned and unset, assigned to *"PM/BA with UX and QA, before it runs."* The spike has now run twice. Pre-registration by those seats is no longer available and pretending otherwise would be a fiction. This section settles what can be settled and says precisely what remains theirs.

### 3.1 Who decides, and what I am not taking

**Mine, because they are properties of my own block:** which *quantity* limb (a) is denominated in, and whether the 0.8 threshold survives. The block is mine under Constitution 5.6, its grounds are mine, and the defect is mine. A seat that will not correct its own specification when the specification is shown to measure the wrong thing is not holding a block, it is holding a position.

**Not mine, and I am leaving it with the seats open question 5 named:** the *threshold values*. P1's 95%, P2's and P3's 2 pp, P4's 90%. Those are judgments about how often a venue page may be wrong before the product stops being honest about what it sells, and that is a product question with an Article 4 surface, not an architecture question. **The PM/BA with UX and QA may confirm them or move them in the requirements document. If a threshold moves, limb (a) re-tests against the moved one, and I will re-rule rather than treat this discharge as spent.**

**A genuine pre-registration does exist, and it is worth being precise about.** Both bars were published before the measurement that tested them:

| Bar | Published | Tested by | Author knew the answer? |
| --- | --- | --- | --- |
| Modal rank-1 > 0.8 | `venue-index-spike.md` §10.2, 2026-09-18 | `venue-index-remediation.md`, 2026-09-20 | No — and it **failed** it |
| P1–P4 | `venue-index-remediation.md` §8.4, 2026-09-20 | `venue-index-nameseach.md`, 2026-09-21 | **No** — its own honest range was 81.6–100%, straddling the 95% threshold it set |

The second row is what pre-registration is for. The Engineer set a threshold inside a range it could not resolve, said so, said which way it would rule if the measurement landed low, and then cleared it. **That is not a moved goalpost; it is a goalpost planted in fog.**

### 3.2 Why the original bar was wrong, on grounds that do not depend on the result

This is the part I have to get right, because correcting a bar I set, in the direction that permits a build the CEO wants, on evidence produced by the seat that asked for the correction, is exactly the move Article 9 exists to be suspicious of. So the argument below uses only the block's own text and published numbers, and does not require anyone to take the Engineer's word.

**(a) The block's grounds are denominated in identity. The bar is denominated in list position.** Block 4's statement of what fails cites Condition 8.6 verbatim — *"a venue page must never show '3 visits, average 3.8' when the true figures are 11 and 4.2"* [E, `decisions/2026-09-16-haunt-gate.md` Condition 8.6]. That is a statement about a venue's accumulated record. Nothing in it is about row one or row five. **The bar and the ground it serves are in different units, and I did not notice.**

**(b) The bar is under-inclusive: it fails designs that are correct.** Measured: a design at modal rank-1 share **0.67** holds a single identity for **100%** of dense-centre venues [E, `venue-index-nameseach.md` §6, §7.1 — the same run, the same configuration]. Under a design that never auto-selects, rank 1 does not create a venue identity; the user's pick does. A shifting cast of neighbours can trade places above a venue that is reliably in the list and reliably chosen. **Limb (a) as written would fail that design, and the venue page it produces is right.**

**(c) The bar is over-inclusive: it passes designs that are dangerous.** This is the half the Engineer did not make and it is the one that settles it for me. Take the confirmation prior to β → ∞. The previously-confirmed venue pins to rank 1 at that location permanently; modal rank-1 share goes to ~1.0 and **clears my bar comfortably**. The resulting journal is perfectly stable and confidently wrong every time the user goes next door — and the measurement says that case is not rare: at β = 4 the prior already puts last week's pub first on **57.5%** of neighbour visits [E, `venue-index-remediation.md` §7]. **A bar that a maximally dangerous design passes by construction is not measuring safety.** P3 exists precisely to catch this and the rank-1 bar has no equivalent.

**(d) The second limb bars a UI constant the evidence already abandoned.** *"Top-five recall above 80%"* fixes the list at five rows and then demands the index overcome that choice. Recall@5 in Manchester is 51.9% against recall@20 of 92.5% [E, `venue-index-spike.md` §5.3], my own §8.1 already recorded that *"five rows is a design constant the measurement does not support"*, and **D8 has since decided a twenty-row reachable list.** The bar contradicts a CEO decision taken after it was written.

**Grounds (a) and (c) are sufficient on their own and neither cites the 100%.**

### 3.3 Disposition of the rank-1 bar

**The 0.8 modal-rank-1 threshold is WITHDRAWN as a pass criterion and RETAINED as a reported metric.** Withdrawn because of §3.2. Retained because it is a genuine diagnostic of how hard the distance path is working, it is free to compute on the existing harness, and it is the number that told us the baseline was unsafe. **Every future measurement of this design reports it. No future measurement passes or fails on it.**

**If anyone declines the substitution, the answer is not that the remediation failed.** That was the Engineer's honest offer and it was the right offer for a seat that holds no block. It is not available to me, because I am the one who wrote the bar in the wrong units. **Declining the correction would mean holding a build to a threshold that the block's own stated grounds do not support, that a correct design cannot clear, and that a dangerous design clears trivially.** I will not do that and I do not think another seat should be asked to.

### 3.4 The bar that governs, and the criterion I am adding

**Limb (a) of Block 4 is hereby specified as:**

> **P1** Single-identity rate in a dense city centre at σ = 25 m, ≥ 20 simulated visits: **≥ 95%**.
> **P2** P1 at 40 visits per venue falls no more than **2 pp** below P1 at 3 visits per venue.
> **P3** Recall of the correct venue on a visit within 100 m of a previously-confirmed one is within **2 pp** of the same design with the confirmation prior disabled.
> **P4** Single-identity rate at σ = 50 m: **≥ 90%**.
> **Reported, not pass/fail:** modal rank-1 share, top-N hit rate, junk rate, duplicate rate.

**And I am adding a fifth, which the Engineer did not propose, so that the substitution is not a pure relaxation.** It is a requirements criterion, so it is ruled under **limb (b)** and is written into §6 as R-5:

> **P5 — the residual must be repairable by the user, on-device, without Candour.** P1–P4 all inherit the simulation's assumption that the user never picks the wrong row. That assumption is unmeasured and two measured hazards say it will be violated (§4.2). The design must therefore make a wrong confirmation **visible and undoable**: a venue page enumerates the visits that compose it; a visit can be reattached to a different venue; merge is reachable from the venue page and is reversible; rename is reachable and permanent. **Test, without a user:** confirm the wrong venue on a simulated visit; assert the visit can be moved, the two venues merged, the merge undone, and no visit, note or rating lost, entirely on-device.

**Why P5 and not a demand for a measured false-pick rate.** A false-pick rate needs a person using a built app. Demanding it before build commencement would be a block nothing could lift before a build, which my charter forbids me to declare. **P5 is the criterion that makes an unmeasured error rate survivable rather than the criterion that measures it.** The measurement itself belongs to QA at pre-release and is written into §6 as R-6.

### 3.5 The test I applied to myself

My charter: *"You fail by missing real problems, and you fail equally by manufacturing objections where none exist."* And Article 9 is a document about a company naming its own gaming vectors. So:

**Would I have made this substitution if the number had come back at 70%?** Yes — and the block would then be standing on limb (a) as well, harder than it stands today, because the corrected bar is *stricter* than the original in the case that matters. At 70% single-identity the design fails P1 outright, where the original bar would still have been arguing about rank-1 share. **The substitution is separable from the outcome, which is the only defence of a substitution that is worth anything.**

**Is the discharge doing work the CEO's preference would have done anyway?** The CEO's stated position is that this is not a blocker and is improvable in flight. **I am not adopting that position.** §4.3 disagrees with a sentence of D8 in writing; §2.3 keeps the block standing against the stated wish to start building; §8 attaches two conditions that can re-engage limb (a) after it has been discharged. A discharge that arrives with a disagreement, a standing block and two re-engagement triggers attached is not deference.

---

## 4. D8 on the merits

The question put to me is the right one: does moving identity from the coordinate to a confirming user **answer** the silent-corruption finding, or **relocate** it — for instance to the user who confirms quickly and wrongly? My answer is that it does both, that the two parts are separable, and that D8's own text claims more than the evidence supports.

### 4.1 What D8 genuinely fixes, and it is structural rather than cosmetic

The baseline failure is not that the app is sometimes wrong. It is that the app is wrong **systematically and independently on every visit**, so errors accumulate monotonically and never heal:

| Visits per venue | Dense-centre venues keeping one identity, index as specified |
| --- | --- |
| 3 | 30.6% |
| 12 | 6.1% |
| 40 | **2.0%** |

[E, `venue-index-remediation.md` §6.3, measured]

**That is a failure whose severity is a function of how much the customer uses the product.** The user's local — the place they go most, the page the product exists to produce — is the page that ends up most fragmented. Under Condition 8.6 and Article 1.3 that is not a quality issue, it is a product that lies about the customer's own life in proportion to their loyalty to it.

**Requiring a human confirmation attacks that at the mechanism.** The coordinate does not know which pub the user is standing in; the user does. Conditioning identity on a signal that carries information the coordinate lacks converts a systematic error into one that fires only when the human is wrong. **That is a real structural improvement and I am not going to damn it with qualifications.** It is also, on the measurements, the largest single lever available: the remediated line in the table above is **100.0% at every visit count** [E, `venue-index-nameseach.md` §7.2].

### 4.2 What it relocates, with the numbers

The Engineer is explicit that its simulation *"models the user as picking their own venue whenever it is in the list"* — the false-pick rate is **set to zero by assumption** [E, `venue-index-nameseach.md` §8.1]. Three measured findings say that assumption will be violated, and none of them is abstract:

1. **Name-similar wrong venue first.** Of 304 typed queries returning anything, the nearest returned row is not a true row in **11 — 3.6%**. `Castle Tea Room` **5 m** from `Castle Lodge Buttery`; `Wilbraham Bierhaus - Chorlton's Pop up Christmas Bar` **4 m** from `Chorlton Metro Cafe`; `San Carlo Bottega` 34 m from `San Carlo Gran Cafe` [E, `venue-index-nameseach.md` §8.1, measured].
2. **The prior puts the wrong pub first next door.** With the confirmation prior at β = 4, a previously-confirmed venue takes rank 1 on **57.5%** of visits to a venue within 100 m of it, in the dense case [E, `venue-index-remediation.md` §7, measured].
3. **Generic tokens return the neighbourhood.** Eight of twelve retrievals in the absent-venue class were a user typing a common word — `ludlow`, `coffee`, `bar`, `manchester` — and getting five unrelated premises, because index names carry the locality [E, `venue-index-nameseach.md` §5.4].

**Now the part that matters for the CVO's reservation.** A wrong confirmation has the same two properties the CVO named: **there is no server, no telemetry and no backfill, so Candour cannot detect it and cannot repair it.** A user who confirms `Castle Tea Room` gets a venue page that is wrong, gets no signal that it is wrong from the product, and Candour never learns. **So D8 does not eliminate silent, permanent corruption. It changes its cause, reduces its rate by an amount nobody has measured, and leaves its character intact from Candour's side.**

### 4.3 The sentence in D8 that overclaims — my disagreement, in writing, once

D8 records:

> *"The CVO's reservation, recorded once: the corruption the spike measured is **silent and permanent** — there is no server, no telemetry and no backfill, so a wrong identity cannot be detected or repaired after shipping. **D8's mitigations meet that reservation** by moving identity from the coordinate to the user."* [E, `decisions/2026-09-16-haunt-gate.md` D8, read from disk 2026-09-21]

**"Meet that reservation" is too strong, and this is my one disagreement, stated once as my charter requires.**

Moving identity from the coordinate to the user **relocates** the source of error; it does not restore detectability or repairability *by Candour*, which is what the CVO's sentence is about. A wrong identity created by a confirming user is exactly as invisible to Candour as one created by a coordinate. **What actually changes is not Candour's position; it is the user's** — and that is a good and sufficient answer, but it is a different answer, and D8 does not make it. §4.4 makes it.

I record this because Constitution 1.3 requires us to say what a thing cannot do, the decision record publishes on 2026-10-16, and **a record that claims a reservation was met when it was shrunk is the kind of small inaccuracy Corrections C1 through C6 exist because of.** The remedy is one clause, not a reopening: D8's disposition of the CVO's reservation should read that the mitigations *reduce the corruption and move it to a source the user can see and repair*, conditional on §6's R-5. **The decision itself is unaffected and I am not asking for it to be reopened.** This is a flag to the CGO and the CVO for the pre-publication pass, not a block — my block reaches architecture, not the drafting of a decision record.

### 4.4 The answer the CVO's reservation does have, and what it costs

There is an asymmetry the CVO's framing does not capture and D8 reaches for without naming.

**A coordinate-made error is invisible to everyone. A user-made error is invisible to Candour but visible to the user.** The baseline's corruption is undetectable precisely because it produces plausible-looking fragments with correct names — five pages all called "The Eagle", each claiming eight visits, each internally consistent. Nothing looks wrong. But a user who confirmed `Castle Tea Room` and then opens a venue page headed *Castle Tea Room* containing their visits to the Buttery **can see that it is wrong**, because they know where they went.

**So the honest answer to the CVO is: on this architecture, "repairable by Candour" was never available and is not the standard. "Repairable by the person who holds the data" is available, and it is the standard this product can actually meet** — which is, incidentally, the same logic that makes the zero-network architecture defensible in the first place.

**That answer is not free. It costs three requirements, and without them it is not available:**

- **The repair must exist.** Merge, rename and visit-reattachment, at MVP, reachable from the venue page. §6 R-5. The Engineer's `venue-index-spike.md` §9.2 already ruled merge and rename **MVP rather than deferrable**, on the measured duplicate rate; visit-reattachment is my addition and follows from D8 making the user the source of identity.
- **The error must be visible.** A venue page that shows an aggregate without showing what composes it gives the user nothing to check. Condition 8.6 already forbids derived views that misstate; §6 R-5 makes enumerability the mechanism by which a user can tell.
- **The repair must be reversible.** A merge that cannot be undone converts a repair attempt into a second, worse corruption.

### 4.5 D8's three constraints — assessed, and one tension named

D8 attaches three constraints from the measurements. **All three are correct, all three are load-bearing, and all three are in §6.**

| D8 constraint | Measured basis | My assessment |
| --- | --- | --- |
| **Twenty-row reachable list** | At five rows the headline falls to 93.9% and **P1 fails**; at twenty it passes [E, `venue-index-nameseach.md` §7.3]. Independently, neighbour recall at five rows is 30.0% against 75.0% at twenty [E, `venue-index-remediation.md` §7] | **Correct and binding.** Note it is *"reachable"*, not *"displayed"* — the Engineer's §9.4 and the UX seat's recognition-at-a-glance goal are both satisfied by a short default list where **typing is the path to the long one**. That resolution is supported by the numbers and is the UX seat's to make. |
| **Prefix matching, not whole-string** | On the 44 venues whose registered and displayed names genuinely differ: full registered name **50.0%**, four characters **100%** [E, `venue-index-nameseach.md` §5.3] | **Correct, and it is the most robust finding in the whole exercise** — it is a comparison *within* the contaminated population, so the contamination cancels. It does not depend on the contested ground truth at all. |
| **Never auto-select** | 3.6% of typed queries put a name-similar wrong venue first; the prior puts last week's pub first on 57.5% of neighbour visits [E, as §4.2] | **Correct, and it now has three independent grounds**: Article 4 (a pre-selected candidate is a pre-ticked box, `ux-note.md` §2.2), the 57.5% false-stick measurement, and the 3.6% name-similar hazard. |

**The tension I have to name, because D8 contains both halves of it.** D8 says *"selection one easy action"*; D3 says *"a notification may prompt confirmation."* Put together without care, those specify a notification offering **one tap to accept the default** — and the default is the row the two measurements above say is wrong 3.6% and 57.5% of the time in the cases that matter.

**The distinction that resolves it, and it belongs in the requirements document:** *easy* must mean **low-friction choice**, not **low-friction assent**. One action to select any row on a list the user has seen is exactly right. One action to accept a suggestion **without the alternatives having been presented** converts the measured wrong-first rate directly into corrupted venue pages, and does it through the interaction that is hardest to notice.

**This is a flag to UX and the PM/BA, not a block.** It engages Article 4's dark-pattern list and the UX seat's own §2.2, and the UX seat holds the release block on Article 4 grounds — not me. I am recording it because the measurement that makes it concrete is in my domain and the seat that owns the rule should not have to find it.

---

## 5. The two technical questions the CEO raised

### 5.1 Would a proper spatial index — R\*Tree, geohash, S2 — improve accuracy?

**No. The CVO's answer to the CEO is correct, and here is the primary source rather than my agreement.**

SQLite's own documentation for the R\*Tree module [E, verbatim — https://www.sqlite.org/rtree.html, retrieved 2026-09-21 by this seat]:

> *"An R-Tree is a special index that is designed for doing range queries."*
> *"An R\*Tree index does not normally provide the exact answer but merely reduces the set of potential answers from millions to dozens."*
> *"the R\*Tree index is used to narrow a search down to a list of candidate objects and then more detailed and expensive computations are done on each candidate to find if the candidate truly meets the search criteria."*

**That is the whole answer.** An R\*Tree is a candidate-narrowing structure sitting *in front of* a refinement predicate; it does not change the predicate. Geohash and S2 are the same class by a different construction — space-filling-curve keys that bucket points so a proximity query examines fewer of them. **All three change which rows you examine. None changes which row is nearest.** And the venue is not being missed because the search is slow; it is being missed because the query point is in the wrong place. Nothing indexed on the venues can know that.

**Two refinements the answer should carry, because "no" on its own is less useful than it looks.**

1. **A badly built spatial index can make accuracy *worse*, and this is the failure mode to guard against.** Cell-based schemes — geohash prefixes, S2 cell IDs, or the integer grid-cell column already specified — lose true neighbours that sit across a cell boundary from the query point, unless the query deliberately unions the **neighbouring** cells. That is the classic geohash edge bug and it costs recall, which is the quantity this whole exercise is about. **The existing design already handles it:** `android-and-stack-note.md` §3.2 specifies *"an integer grid-cell column (quantised lat/lng) with a plain B-tree index and a **9-cell neighbourhood query**"* [E, read from disk 2026-09-21]. The nine cells are the fix. **It must stay in the requirements document** — §6 R-7 — because it looks like a performance detail and is not.
2. **Nothing needs buying for speed either, which is a Constitution 1.5 point.** The shipped scope-B index is 336,103 rows [E, `venue-index-remediation.md` §12] and every query is on-device against a local SQLite file with £0 marginal running cost. A B-tree on a quantised grid cell is adequate at that size [J, high confidence]. **So the open question carried since `android-and-stack-note.md` §5 item 3 — whether R\*Tree is available in `expo-sqlite` — is now answerable without a spike: it does not matter.** The grid-cell approach is sufficient, portable across all three implementations, and does not depend on an unverified `customBuildFlags` path. **I am closing that open question on those grounds** and recording it in §8 as a finding rather than leaving a spike budgeted for a decision that does not need one.

**What would overturn this.** A measurement showing the venue query is a latency or battery problem at 336,103 rows on a low-end Android device. I have not measured it; nobody has; and if it were true the remedy would still be a speed remedy, not an accuracy one. **Where I looked:** SQLite's R\*Tree documentation at primary; `android-and-stack-note.md` §3.2 and §5; `subscription-sizing-note.md` §8.1 and open question 8; all three spike notes for any claim that the search layer rather than the query point was losing venues — `venue-index-spike.md` §10.1 attributes the failure to *"the query layer — category scoping, distance-only ranking, and a fixed list of five"*, and none of those three is an indexing structure.

### 5.2 Would venue footprints rather than point coordinates improve accuracy? — the technical half

**The mechanism is real. It fires on a minority of visits at the error model this entire exercise runs on, it is not an identity answer even when it fires, and it adds a silent-corruption surface of its own. I recommend against buying it now, on cost rather than on licence.**

**(a) How often the mechanism fires. This is arithmetic and a second seat should re-derive it** (gate Condition 6). Every σ in every spike note is an isotropic Gaussian offset applied to the true position [E, `venue-index-spike.md` §5]. For such an offset, the probability that a draw lands within radius *r* of the true position is `1 − exp(−r²/2σ²)`. At **σ = 25 m**:

| Distance from true position | Probability the fix lands inside it |
| --- | --- |
| within 10 m | **7.7%** |
| within 15 m | **16.5%** |
| within 20 m | **27.4%** |

A terraced city-centre pub occupies something in the region of 8–15 m of frontage [J, my estimate, unmeasured]. **So at the error model the bar is set at, the fix lands inside the correct building on roughly one visit in six to one in four, and outside it the rest of the time.** The CEO's intuition — *"a fix 20 m off can still fall inside the right building"* — describes a case that genuinely happens; it is not the common case. On the majority of visits a containment test returns the **wrong** building, or no building, and the design is back where it started.

**(b) Containment is not identity, and in the dense case it is furthest from identity.** Where footprints would most help — a dense high street — is exactly where **one building holds several venues**: a pub with a restaurant above it, a converted mill with eight units, a shopping centre. Containment then returns a **set**, and the set still has to be resolved by name. **That is the job the name search already does, at 100.0% single-identity.** Footprints would be bought to hand the disambiguation problem to the component that already solves it.

**(c) It creates a new silent-corruption surface, of exactly the class limb (b) exists to prevent.** Overture Places positions are provider-supplied and the same documentation warns of *"duplicates, a high junk rate, and low property completeness"* [E, quoted in `venue-index-remediation.md` §10 from the Overture Places guide, retrieved by that seat 2026-09-20; attributed]. Overture Places carries **no building linkage**, so Candour would perform the point-in-polygon join itself, at index-build time, and bake the result into the shipped binary. **A place point 30 m off its true building joins to the wrong polygon permanently, before any user sees it, with no server and no backfill to correct it.** That is the refresh hazard again, in a new place, and it would be inherited rather than chosen.

**(d) It is bought against a metric that already passes.** P1 is met at 100.0% at σ = 25 m and 93.9% at σ = 50 m. **Constitution 1.5 — *"Cheap to run, cheap to buy. Operating cost discipline is an ethical obligation, because our customers pay our costs"* — and my charter's instruction to justify anything that raises cost both point the same way.** The costs are real: a second national dataset in the bundle (Microsoft added 1.5M UK structures in a single update [E, §5.3]), a point-in-polygon step in the build pipeline, and a **second refresh cadence with its own churn**, on top of the Overture reconciliation the Engineer's §9.4 already told the CFO was under-costed.

**What would overturn this, and it is cheap.** The existing harness holds real venue positions and simulated fixes; adding a containment predicate over a footprint extract for the three sample areas and re-running P1 is **about a day** [J]. **If it returned a materially higher P1 at σ = 50 m — the case where the current design is marginal — footprints would become worth costing properly.** I did not run it, and I am not asking for it now, because it would be spent improving a number that already clears its bar while limb (b) is the thing actually holding up a build. **Where I looked:** the three spike notes for any footprint or building-linkage experiment (none exists — `venue-index-spike.md` §10.2 item 4 and `venue-index-remediation.md` §14.2 name supplementary datasets as untested, and neither tested one); `feasibility-note.md` §2 for the dataset decision; Overture's attribution page at primary for whether a permissive footprint source exists inside Overture (it does not).

### 5.3 Venue footprints — the licence half, answered alongside

**Retrieved at primary by this seat this session rather than carried from the CGO's retrieval** [E — https://docs.overturemaps.org/attribution/, retrieved 2026-09-21]:

| Theme | Licence |
| --- | --- |
| **Places** | **CDLA Permissive 2.0** (plus Apache 2.0 for the Foursquare portion, CC0 for AllThePlaces) |
| **Buildings** | **ODbL** — *"© OpenStreetMap contributors. Available under the Open Database License"* |
| Base, Divisions, Transportation | **ODbL** |

**The CGO's theme boundary is confirmed by my own retrieval** (`compliance-note.md` §2.5), and it is the same accident that note names for the Divisions theme, arriving by a different door.

**What ODbL would actually require** [E, verbatim — https://opendatacommons.org/licenses/odbl/1-0/, retrieved 2026-09-21]:

> *"Any Derivative Database that You Publicly Use must be only under the terms of: This License; A later version of this License similar in spirit to this License; or A compatible license."*
> Derivative Database *"means a database based upon the Database, and includes any translation, adaptation, arrangement, modification, or any other alteration of the Database or of a Substantial part of the Contents."*

So joining Overture Buildings into the shipped venue index makes that index a Derivative Database and obliges Candour to publish it under ODbL. **That is survivable and arguably welcome under Article 8's open-source preference — but `feasibility-note.md` §2.2 is right that it is *"a commitment the gate should make knowingly rather than inherit by accident"*, and it would be inherited by accident here, because nobody proposing footprints would be thinking about a licence.**

**But the licence is not the reason to decline, and I want to be explicit about that, because a CTO who lets a licence objection carry an argument the technical analysis already settles is doing the thing `pipeline/evidence-standard.md` was rewritten to catch.**

**A permissive footprint source exists and the record does not carry it.** Microsoft's GlobalMLBuildingFootprints is released under **CDLA Permissive 2.0** — *"This data is licensed by Microsoft under the CDLA Permissive 2.0"* — and covers the United Kingdom [E — https://github.com/microsoft/GlobalMLBuildingFootprints, retrieved 2026-09-21. **Single source, and it is the publisher's own repository** — flagged under `pipeline/evidence-standard.md`, which is the same class of single-origin claim as Apple's rules being published only by Apple]. **That is the same licence family as Overture Places and would create no share-alike obligation.**

**So the honest disposition of the licence question is:**

1. **Overture Buildings is closed to Haunt on the current architecture** unless the CEO decides knowingly to ship the index under ODbL. That is a Constitution 5.4 and Article 8 decision, not mine.
2. **A permissive route exists**, so *"footprints are ODbL"* is not a sufficient answer to the CEO and I am not giving him one.
3. **The recommendation against footprints therefore stands entirely on §5.2 — mechanism frequency, identity, corruption surface and cost.** It does not need the licence and does not lean on it.
4. **Constitution 6.1 applies to any of this if it is ever revisited:** *"third-party licence terms whose interpretation determines a product's architecture or cost"* receive *"review by qualified human professionals"* before launch. The Microsoft licence claim above is single-origin, I have not read that dataset's full terms, and **it must not anchor an architecture decision on my say-so.** Owner: CGO, with launch bar L1.

---

## 6. What must be in the requirements document — the lift, written for the PM/BA

**This section is the lift for Block 4.** When the items below are in a signed-off requirements document, the block lifts. I will confirm in writing against this list rather than re-argue it.

**Nothing here is new evidence.** Every item is lifted from a published spike note, a CEO decision, or this ruling's §3.4 and §4.4. The PM/BA may write them more tightly, not more loosely, and should write them in the template's own units (`pipeline/templates/requirements.md`).

### R-1 · The six schema acceptance criteria and their preconditions — **this is limb (b)**

Lift **AC-1 through AC-6** and the four schema preconditions verbatim from `venue-index-remediation.md` §11. In summary, with the reason each is unavailable later:

| | Criterion | Why it cannot wait |
| --- | --- | --- |
| **AC-1** | On first reference the venue row is **copied, not pointed at**; a venue page renders with the shipped index deleted | Defines the boundary between Candour's data and a third party's |
| **AC-2** | A refresh may add and update **unreferenced** rows only; **enforced in the schema** (trigger), never in application code | Unenforceable once a shipped refresh has mutated devices |
| **AC-3** | Changes to referenced rows are **offered, never applied**; proposals are inert; declining is the default and is remembered | No server exists to undo an auto-applied change |
| **AC-4** | A user's rename outranks the dataset permanently, and a refresh may not even **propose** a name change afterwards | The question has been answered; re-asking it is the dark-pattern route to un-answering it |
| **AC-5** | User merges are durable rows, surviving a refresh that re-splits the upstream records | A merge reconstructed from a derived index is not a merge |
| **AC-6** | Reconciliation may **not** join on GERS ID alone; a changed or vanished GERS ID raises a proposal, never an update | Overture churned GERS IDs corpus-wide one release before the one this product builds on |

Schema preconditions: tables `venue` (with `venue_id` never derived from a dataset identifier, `name_source ∈ {dataset, user}`, `gers_id` nullable attribute, `first_referenced_at` set once and never cleared), `venue_ref`, `venue_merge`, `refresh_proposal` (with `declined_at`).

### R-2 · The three D8 constraints, as acceptance criteria

1. **A twenty-row reachable candidate list.** *Reachable*, not necessarily displayed: a short default list with typing as the path to the long one satisfies this and satisfies the UX seat's recognition-at-a-glance goal. **At five reachable rows P1 fails at 93.9% and the design does not meet its bar** [E, `venue-index-nameseach.md` §7.3]. QA tests the reachable length, not the visible one.
2. **Name search is incremental and prefix-based, not whole-string or exact.** A four-character prefix retrieves the right row 100% of the time on divergent names; the full registered name retrieves it 50.0% [E, §5.3]. **An exact-match implementation does not deliver the measured result and the bar is not met.**
3. **Never auto-select, in any surface.** No pre-selected candidate; no confirmation accepted without the alternatives having been presented; **and this binds the notification path specifically** (§4.5). *Easy* means low-friction **choice**, not low-friction **assent**.

### R-3 · The confirmation prior, with its guard

Nearest-first ranking weighted by the user's own prior confirmations at that location (D3), at the measured strength. **The prior must raise a venue in the list and must never pre-select one.** Guard: P3 — neighbour recall within 2 pp of the prior-disabled design. Without the guard, the cheapest way to satisfy an identity bar is a prior so aggressive it pins one venue per location forever, which is a perfectly stable and confidently wrong journal.

### R-4 · The near-miss and generic-token hazards, designed against

Grounded in the 3.6% wrong-first rate and the generic-token dragnet (§4.2). The measurements support, and I recommend, that a name-search result row shows **distance and category prominently**, and that results matching **only** on a locality or a generic trade token are demoted or suppressed [E mechanism, `venue-index-nameseach.md` §8.1, §5.4]. **The specific design is the UX seat's**; what the requirements document owes is that the hazard is named and answered rather than discovered at pre-release.

### R-5 · P5 — the residual is repairable by the user, on-device *(added by this ruling)*

- A venue page **enumerates the visits that compose it**. (Also the mechanism by which Condition 8.6's honesty duty is checkable by the person it protects.)
- A visit can be **reattached** to a different venue.
- **Merge** is reachable from the venue page and is **reversible**.
- **Rename** is reachable and permanent (AC-4).
- **MVP, not backlog.** `venue-index-spike.md` §9.2 already ruled merge and rename MVP on the measured duplicate rate; reattachment and reversibility are added here because D8 makes the *user* the source of identity, and a design that makes a person responsible for an outcome and gives them no way to correct it is not an honest design.
- **Test, without a user:** confirm the wrong venue; move the visit; merge the two venues; undo the merge; assert no visit, note or rating lost, entirely on-device.

### R-6 · Two measurements that belong to QA and the build, not to this block

- **A false-pick acceptance criterion.** Name-search result lists are tested for **near-miss confusability**, not only for recall. The 3.6% figure is the fixture. **Owner: QA**, at pre-release.
- **Real `CLVisit` accuracy, measured on a device.** Already budgeted — `feasibility-note.md` §8 item 3 asks for a real-week battery measurement during build; **measure horizontal accuracy on the same run.** **Owner: Engineer**, during build. §8 makes this a standing condition with a defined consequence.

### R-7 · The spatial index is a grid cell with a nine-cell neighbourhood query

Not a performance note. **The neighbourhood union is what stops the index losing true neighbours across a cell boundary**, and it is the one way an indexing choice can damage recall (§5.1). It is already specified at `android-and-stack-note.md` §3.2 and must survive into requirements rather than be optimised away as a detail.

### R-8 · Carried forward from Condition 7, unchanged and still owed

The in-app **"Data sources and licences"** screen carrying the full CDLA-Permissive-2.0 text, the full Apache-2.0 text, the unaltered Foursquare OS Places `NOTICE.txt` and a modification notice; the same texts in the export README; and **"Delete my backup"** as a launch requirement. Gate Condition 7. **Half a day now, expensive after the schema and settings tree exist** — the same economics as R-1, which is why it sits here rather than in a backlog. **This is not part of Block 4's lift** and is recorded so it is not lost between artifacts.

---

## 7. Running cost, and what this ruling does to the cost sheet

My charter requires every recommendation that raises cost to be justified, and Constitution 1.5 makes it a customer-facing obligation rather than a preference.

**Marginal running cost of everything in this ruling: £0.** The index ships inside the binary and is queried on-device. No hosting, no egress, no per-query cost, at any user count. That is unchanged from the gate and is the property that makes this architecture defensible in the first place.

**What does move, and where it lands:**

| Item | Effect | Owner |
| --- | --- | --- |
| **FTS5 name index + scope B + attributes** | Shipped index **23.8 MB → 48.5 MB**, roughly a doubling [E, `venue-index-remediation.md` §12]. Download size and phone disk, once per update. Still a rounding error against Apple's 4 GB limit | CFO — visible, not discovered at build |
| **Reconciliation, not re-extraction** | The monthly refresh becomes a diff-and-propose job under AC-1..AC-6. The Engineer raised this with the CFO unprompted (`venue-index-spike.md` §9.4) and it is **not** priced in the 0.5 day/month the feasibility note carries | CFO, in the Condition 1 re-derivation |
| **R-5 (merge / rename / reattach / undo)** | Merge, sticky choice and rename are **already inside row 5** of `android-and-stack-note.md` §3.2 [E, `subscription-sizing-note.md` §8.1]. **Reattachment and merge-undo are not.** I size them at **2–4 days** on top [J] and I am flagging rather than absorbing them, per the practice this seat adopted at §6.2 of the sizing note | CFO and PM/BA |
| **R\*Tree spike** | **Removed.** §5.1 closes `android-and-stack-note.md` §5 item 3 without a spike: the grid-cell approach is sufficient and accuracy does not depend on it. One day recovered | CTO — closed here |
| **Footprints** | **Not recommended.** §5.2. A second national dataset, a point-in-polygon build step and a second refresh cadence, against a metric that already passes | — |

**Net: the two additions are small and one budgeted spike is cancelled.** Nothing in this ruling moves the 2,090-hour build total materially, and I am not re-opening it here.

---

## 8. Standing conditions — what re-engages limb (a) after it has been discharged

A discharge that cannot be reversed by evidence is not a finding, it is a permission slip. Limb (a) is discharged on measurements that rest on two unmeasured parameters. **Both are named here with a defined consequence, so that re-engagement is automatic rather than a matter of anyone's appetite.**

**S-1 · Measured `CLVisit` accuracy (R-6).** Every figure in every spike note is a function of a σ nobody has measured. The design passes at σ = 25 m and is **marginal** at σ = 50 m — 93.9% headline, **89.8% under the harshest query policy, a fail by 0.2 pp against P4** [E, `venue-index-nameseach.md` §7.2].

> **If the measured median horizontal accuracy of real `CLVisit` centroids in a dense city centre is materially worse than 25 m, limb (a) re-engages and Block 4 re-declares.** The remedy at that point would be design work, not a new dataset — the name path is the one lever whose value *rises* as the location signal worsens (it takes Manchester from 34.7% to 93.9% at σ = 50 m [E, §8.3]), so a worse signal argues for leaning harder on it, not for abandoning the approach. **But it is a re-test, not a formality.**

**S-2 · The false-pick rate (R-6).** P1 through P4 all inherit the assumption that the user never picks the wrong row. R-5 makes the residual repairable; it does not make it small.

> **If QA's near-miss testing returns a false-pick rate that would take P1 below 95% on the same sample, limb (a) re-engages.** The arithmetic is available: on 49 scored Manchester venues, each percentage point of P1 is half a venue, and the bound at §5.5 of the nameseach note shows the mechanism.

**S-3 · Any weakening of R-5.** If merge, rename, reattachment or merge-undo leaves MVP scope, **§4.4's answer to the CVO's reservation fails with it**, because that answer depends entirely on the user being able to see and repair what Candour cannot. **That would re-engage the block on limb (b), and I am recording it now so the dependency is not rediscovered by whoever proposes the cut.**

**Not standing conditions, recorded so the distinction is clear:** the shopfront-name gap (`venue-index-nameseach.md` §5.6), the closed-venue problem (§8.3), and the untested national clustering parameters (`venue-index-remediation.md` §14.2 item 3). All three are real, all three are QA and build-phase items, and **none of them is a reason not to start.** The closed-venue one deserves a line of its own because the remediation makes it *worse*: name search surfaces a closed pub **more** reliably than distance ranking does, because the name still matches. `operating_status` is populated for 322 of 330,208 UK food-and-drink rows [E, `venue-index-nameseach.md` §8.3], so nothing in the dataset detects it. **A stable identity pointing at a pub that shut in 2025 is a stable wrong answer, and R-5's rename and merge are the only repair the architecture has.** Flag to PM/BA and QA.

---

## 9. What would overturn this ruling, and where I looked

*(Required by `roles/cto.md` as amended: a negative finding carries a block's duty, and so does a discharge.)*

**The negative findings here are §2.2 (limb (b) not met), §4.3 (D8's disposition overclaims), §5.1 (a spatial index cannot help) and §5.2 (footprints not recommended). The discharge at §2.1 carries the same obligation.**

**This ruling is overturned by any of:**

1. **A demonstration that the identity metric is itself circular or gameable in a way §5 of the nameseach note did not catch.** I relied on the Engineer's contamination analysis without re-running the harness, and I said so at §1. **The strongest attack is that the ground truth's definition of "this row is this venue" collapses to "shares the venue's distinctive name token" — the Engineer's own §5.2 says so — and the queries derive from the same string.** The adverse bound at 95.9% is the Engineer's answer; **if someone shows that bound is constructed too generously, P1's pass is the first thing to fall.** This is what I would attack if I were the Skeptic and it is item 1 for that seat.
2. **Thirty real shopfront names from one of the three sample areas.** The FSA register gives the registered name, not the sign. If shopfronts diverge from the register more than the register diverges from Overture, the 43.6% divergence rate is an undercount and the retrieval figures fall. **An afternoon with a phone camera settles it**, and it is the Engineer's own item 1.
3. **S-1 or S-2 firing.** §8.
4. **A footprint measurement in the existing harness returning a materially higher P1 at σ = 50 m.** §5.2. About a day. It would not change the ruling on Block 4 — limb (b) is unaffected — but it would change my recommendation against footprints, and I would say so.
5. **A qualified human review under Constitution 6.1 finding that the Microsoft footprint licence claim at §5.3 is wrong.** Single source, the publisher's own repository, not read in full. It is flagged rather than relied upon, and nothing in the ruling depends on it — but it is in the record and an error in the record is an error.

**Where I looked, so a reader can check I looked in the right places:**

- **`constitution.md` v1.3 in full**, from disk, including the Definitions, Article 1.5, Article 4, Article 5.1–5.6, Article 6.1, Article 9 and Article 10 — not from memory of an earlier version, and it has been amended twice since this seat last read it.
- **`decisions/2026-09-16-haunt-gate.md` in full** — 395 lines: Conditions 1–10 including 8.1–8.6, Corrections C1 through C6, and the CEO decisions log D1 through D8. D3 and D8 read whole, in place, rather than through another seat's summary of them.
- **All three Engineer spike notes in full**, including the sections that run against their own conclusions: `venue-index-spike.md` §10.2, `venue-index-remediation.md` §8.2 and §8.5 (where that seat argues against its own substitution), and `venue-index-nameseach.md` §5 (the contamination analysis), §7.4 and §9 (a defect in its own committed harness).
- **My own `subscription-sizing-note.md` §11, treated as a claim to be checked rather than as authority** — which is how §3.2 exists. The finding that limb (a) is misspecified is a finding against this seat.
- **Both directions of the bar question.** §3.2(b) shows the bar failing a correct design; §3.2(c) shows it passing a dangerous one. A bar tested only where it is too strict is a bar not tested.
- **Retrieved at primary this session, independently of the CGO's and the Engineer's retrievals:** SQLite's R\*Tree documentation; Overture's attribution and licensing page; the Open Data Commons ODbL 1.0 text; Microsoft's GlobalMLBuildingFootprints repository.
- **`pipeline/evidence-standard.md` and `pipeline/amendment-verification.md`** for the method standard this ruling is held to, including the rule that a second agent seat's re-reading of an *interpretation* is not independent verification — which is why §1 names what I relied on rather than claiming to have checked it.
- **Where I did *not* look:** I did not re-run the harness; did not open a footprint dataset; did not run anything on a phone; did not measure `CLVisit`; did not read the Microsoft dataset's full terms; did not re-retrieve the Overture Places guide (the Engineer's 2026-09-20 retrieval is attributed, not re-cited); did not test OSM or any supplementary dataset; and did not reopen Blocks 1, 2 or 3, which remain as recorded at §2.4.

---

## 10. Evidence register

**Retrieved at primary by this seat, 2026-09-21:**

| # | Source | Used for |
| --- | --- | --- |
| 1 | [SQLite R\*Tree module](https://www.sqlite.org/rtree.html) | §5.1 — an R\*Tree narrows candidates and does not supply the exact answer |
| 2 | [Overture Maps — attribution and licensing](https://docs.overturemaps.org/attribution/) | §5.3 — Places = CDLA Permissive 2.0; Base, Buildings, Divisions, Transportation = ODbL |
| 3 | [Open Data Commons ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) | §5.3 — the share-alike obligation and the definition of a Derivative Database |
| 4 | [Microsoft GlobalMLBuildingFootprints](https://github.com/microsoft/GlobalMLBuildingFootprints) | §5.3 — CDLA Permissive 2.0, UK covered. **Single source, publisher's own repository — flagged** |

**Read from disk this session (repository):** `constitution.md`; `roles/cto.md`; `pipeline/evidence-standard.md`; `pipeline/amendment-verification.md`; `pipeline/templates/` (listed); `pipeline/templates/requirements.md`; `decisions/2026-09-16-haunt-gate.md`; `products/haunt/subscription-sizing-note.md`; `products/haunt/venue-index-spike.md`; `products/haunt/venue-index-remediation.md`; `products/haunt/venue-index-nameseach.md`; `products/haunt/android-and-stack-note.md` §3.2, §5; `products/haunt/compliance-note.md` §2.

**Attributed, not re-retrieved by me:** the Overture Places guide (Engineer's retrievals of 2026-09-18 and 2026-09-20, including the July 2026 GERS-churn warning at AC-6); the FSA FHRS API (Engineer, 2026-09-21); all measurements in the three spike notes.

**Not verified and relied upon, named at §1:** the Engineer's harness measurements. I checked the argument, the internal consistency across three notes, and the two figures it claims to reproduce. **I did not re-run it, and a second agent pass over its reasoning would not be independent verification if I had** (`pipeline/evidence-standard.md`).

**Re-derivation owed under gate Condition 6:** §5.2(a)'s Rayleigh arithmetic — `1 − exp(−r²/2σ²)` at σ = 25 m for r = 10, 15, 20 m — is the only arithmetic in this ruling and should be recomputed by a seat other than this one. Every claim that a named clause requires or forbids something quotes the clause in the same passage, per the same condition: Constitution 1.5, 5.1, 5.4, 5.6, 6.1 and Article 8; gate Conditions 2, 6, 7 and 8.6; ODbL §4.4 and its Derivative Database definition.

---

## 11. Disposition, in one table

| Question put to this seat | Answer | Whose it is now |
| --- | --- | --- |
| **1. Rule on Block 4** | **STANDS, on limb (b) alone.** Limb (a) discharged. **Lifts on:** a signed-off requirements document containing R-1 through R-5 and R-7. **Achievable before a build: yes** — it is the build's first step, 2–4 days of drafting [J] | **PM/BA** with UX and QA to write it; **CTO** to confirm the lift in writing |
| **2. Which bar governs** | **Settled here, because the misspecification was mine.** Identity, not list position. Rank-1 withdrawn as a pass criterion, retained as reported. **P1–P4 adopted; P5 added.** *Threshold values* remain open question 5's owners' — move one and limb (a) re-tests | **CTO** on the quantity; **PM/BA with UX and QA** on the thresholds |
| **3. Does D8 answer or relocate the finding** | **Both, and they separate.** It fixes the coordinate-driven failure structurally. It relocates the residual to an unmeasured user-confirmation error rate that Candour still cannot see or repair. **D8's "meet that reservation" overclaims** — one clause, flagged for the pre-publication pass. The reservation's real answer is that a user-made error is *visible and repairable by the user*, and that answer costs R-5 | **CGO / CVO** for the record wording; **PM/BA** for R-5 |
| **4a. Spatial index and accuracy** | **The CVO is right. It cannot.** Primary source at §5.1. A badly built one can hurt recall; the nine-cell neighbourhood query already specified is the guard. **The R\*Tree spike is closed without running it** | **CTO** — closed |
| **4b. Footprints** | **Not recommended, on cost and corruption surface rather than licence.** Mechanism fires on ~8–27% of draws at σ = 25 m; containment is not identity in the dense case; it bakes a new silent join error into the bundle; and it is bought against a metric that passes. **A permissive source exists, so the licence is not the reason.** Testable in the harness in a day if anyone wants the number | **CTO**; **CGO** + Constitution 6.1 if ever revisited |
| **5. Requirements, or what an overrule overrules** | **§6.** And if overruled: not a measurement and not a doubt about the venue page — *"write the schema rules down before you write the schema."* **No overrule is needed and I advise against one** | **CEO** under Constitution 5.6 |

**This ruling prepares and flags. It does not certify** (Constitution 6.1). Kill/proceed remains the CEO's alone (5.4), and Blocks 1, 2 and 3 are untouched — **Block 2, on the Android device matrix, is now the larger live block by build risk.**

---

## 12. Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | Created. **Rules on Block 4: STANDS on limb (b) alone; limb (a) DISCHARGED** on a corrected, identity-denominated specification, with the misspecification recorded as this seat's own defect. **Settles open question 5's quantity** and withdraws the 0.8 rank-1 threshold as a pass criterion, retaining it as reported. **Adds P5**, a repairability criterion the Engineer did not propose, so the substitution is not a pure relaxation. **Assesses D8 on the merits and disagrees once, in writing**, with its claim to have met the CVO's reservation. **Answers both of the CEO's technical questions at primary**, confirming the CVO's spatial-index answer and recommending against footprints on cost rather than licence — while recording that a permissive footprint source exists, which the record did not carry. **Closes `android-and-stack-note.md` §5 item 3 (R\*Tree in `expo-sqlite`) without a spike.** Specifies the lift as eight requirements items, R-1 through R-8. Attaches three standing conditions that re-engage the block. External sources retrieved 2026-09-21. **Not a certification.** |

# Dissent memo — Haunt (gate)

**Date:** 2026-09-10 · **Author:** The Skeptic · **Published unedited in the decision record.**

**Artifacts reviewed cold, from disk:** `constitution.md`, `roles/skeptic.md`, `pipeline/evidence-standard.md`, `pipeline/templates/dissent-memo.md`, `proposals/haunt/idea-brief.md`, `proposals/haunt/proposal.md`, `research/haunt-brief.md`, `products/haunt/cost-sheet.md`, `products/haunt/feasibility-note.md`. I also read `research/scouts/scout-2026-09-01-skeptic-cull.md` and `research/scouts/scout-2026-09-01.md`, which the pack cites as load-bearing but which the gate's reading list omitted (see §Verification, "Reading-list gap").

---

## Verdict

**Serious concerns. None fatal to a KILL decision; one fatal to the PROCEED branch as currently specified.**

This is a good pack — the best-evidenced discovery this company has produced, and the CTO's measured Overture work is a genuine piece of engineering rather than an estimate dressed as one. Its recommendation to kill is, in my judgement, the honest reading of its own evidence. **My dissent is not that the kill is wrong.** It is that:

1. The single number the proposal instructs the gate to "stare at" is arithmetically wrong, and the one proceed-criterion derived from it is set roughly 40% below the break-even it claims to represent. A landing-page test calibrated at the stated threshold could pass and still authorise a build that cannot cover its own benchmarked labour. **If the CEO's decision is anything other than KILL, this pack is not fit to support it.**
2. The cost model was written before the feasibility note, contradicts it on the largest single cost in every model, and was never re-derived.
3. The CFO asked, in writing, that Article 8 designation be "a live option at the gate rather than a rhetorical one." The proposal does not answer it. The kill is argued entirely on grounds that Article 8 designation dissolves.

None of those change the direction of travel. All three change what the decision record will be able to say it considered.

---

## The strongest case against, argued to win

Every objection is tiered and states what dissolves it.

### [FATAL — to the PROCEED branch only] O1. The number the gate is told to stare at is wrong, and the proceed threshold is set ~40% too low

The proposal's pricing table reads:

| Model | Honest price | Volume to cover benchmarked labour (3 yr) |
| --- | --- | --- |
| One-off purchase | £14.63 | ~1,480 sales |
| Free + lifetime unlock (9:1) | £29.59 | ~715 unlocks |
| Free + subscription | £3.21–£4.88/yr | ~1,480 subscribers held 3 years |

It then says: *"The number the gate should stare at: ~1,480 sales at £14.63."*

**Every row of that table pairs an Overture-offline price with a Mapbox-Permanent volume.** The proposal took the four-column comparison from `cost-sheet.md` §10 — which is explicitly computed *"at 5,000 users, iOS-only, typical usage, **Mapbox Permanent Geocoding**"* — swapped the price column for the Overture column (correct, since the architecture changed to Overture), and left the volume column untouched.

Recomputed on the cost sheet's own stated method (`net per sale = shelf ÷ 1.20 × 0.85 = 70.83% of shelf`; three-year benchmarked labour, iOS-only, £24,532):

| Model | Price stated | Volume stated | Volume actually implied |
| --- | --- | --- | --- |
| One-off | £14.63 | ~1,480 | **~2,370 sales** |
| Lifetime unlock (9:1) | £29.59 | ~715 | **~1,170 unlocks** (plus ~10,530 free users) |
| Subscription | £4.88/yr × 3 | ~1,480 | **~2,370 subscribers held 3 years** |

The cost sheet's own §6 table contradicts the proposal on the same page it was drawn from: at a £14.99 shelf price it gives **2,310 sales**, not 1,480.

**Why this is fatal to the proceed branch rather than merely embarrassing.** The proposal names exactly one falsifier: *"a UK landing-page test converting at a rate implying a base above ~1,500 buyers at £14.63."* That threshold is derived from the wrong cell. The correct threshold on the pack's own numbers is **~2,370**, and once O2 is applied, **~2,550–2,660**. A test designed to clear 1,500 that clears 1,500 would be reported as a pass and would authorise a 16–19 week build that, at that volume, does not pay its founder the benchmark Constitution 2.1 requires it to publish. Article 2.1's closing sentence exists to stop precisely this: *"unpaid effort never fakes a low price."*

*What dissolves this:* a corrected table, and a proceed threshold restated at the recomputed break-even. If someone shows me that 24,532 ÷ (14.63 × 0.7083) = 1,480, I withdraw the objection entirely. It equals 2,367.

### [SERIOUS] O2. The cost model predates the feasibility note, contradicts it, and was never re-derived

`cost-sheet.md` states its own status plainly: *"Haunt has no requirements document, no CTO feasibility note and no research brief yet"* (§0 preamble), and §3 is headed *"Effort assumptions — the weakest part of this model"* with *"There is no CTO feasibility note yet. These are my estimates, not engineering's, and they are the input most likely to be wrong."* Its §13 gap table names the owner of the fix: *"Build and maintenance hours are CFO guesses, not engineering estimates | The largest single cost in every model | Owner: CTO feasibility note."*

The CTO then answered. `feasibility-note.md` §6.1 sizes the recommended iOS-only, offline-index MVP at **16–19 focused solo weeks**. The CFO's model assumes **450 hours ≈ 12 weeks full-time**. On the same 37.5h basis and the same £32.71/hour benchmark:

| Source | Build hours | Build cost |
| --- | --- | --- |
| CFO (used throughout the pack) | 450 | £14,719 |
| CTO §6.1, low | 600 | £19,626 |
| CTO §6.1, high | 712.5 | £23,306 |

That is **+33% to +58% on the largest line in every model**, and nothing downstream was recomputed. Carrying it through the cost sheet's own method, Overture offline, 5,000 buyers:

- shelf price £14.63 → **£16.31–£17.56**
- sales to cover benchmarked labour → **~2,550–2,660**

So the proposal's "~1,480" is not 60% low; it is **72–80% low**.

The loop is visible inside the pack: the CFO asked the CTO for the number, the CTO supplied it, and no one closed it. A pack whose stated virtue is that the gate *"can argue about numbers instead of adjectives"* must have numbers that survive being added up.

*What dissolves this:* a CFO revision using CTO §6.1 hours that leaves price and volume materially unchanged, or a stated reason why the two seats' week is not the same week.

### [SERIOUS] O3. The Article 8 branch was requested as a live option and disposed of without argument

The CFO wrote (`cost-sheet.md` §9), flagged as judgment: *"if the research brief comes back confirming the idea brief's own objection 1 — that Google Maps Timeline already ships the local-only pitch free — then the commercial case for Haunt is thin regardless of pricing shape, and the choice is between killing it and designating it… I am flagging that it should be a live option at the gate rather than a rhetorical one."*

The research brief came back confirming exactly that. The condition the CFO named was met.

The proposal carries Article 8 as a fourth row in a price table and nowhere else. Its "What we are explicitly NOT building" section does not mention it. Its kill criteria do not mention it. And **every one of the five kill criteria is a reason about charging**: no differentiated product to sell, a free incumbent, a small paying base, a fragile paid behaviour, no acquisition channel to buy customers through. The CFO's §9 argues in terms that meet that head-on — *"Everything difficult in sections 5 through 8 of this document is an artifact of trying to charge for it"* — and the proposal never replies.

I want to be precise, because this is the objection most likely to be misread as advocacy. **I am not arguing for Article 8 designation.** I think it probably fails, and I think it fails for a reason the pack has the evidence for and never states: *Article 8 dissolves the pricing problem and leaves the demand problem untouched.* A free, open-source, self-hostable Haunt still competes with a free Google Maps that ships on-device Timeline plus 4,000-character private notes on both platforms, and with Arc, which is nearly free at the margin for anyone already paying for it. Designation would commit £14,719 of unrecovered build plus £4,989/year of benchmarked labour, indefinitely, drawn from a waterfall that currently contains £0, for a product whose *demand* is what discovery found wanting. That is the argument. **It is missing from the pack, and a decision record that kills Haunt without making it will not show that the option was actually considered.**

*What dissolves this:* one written paragraph in the proposal (or the CEO's decision record) disposing of Article 8 on demand grounds rather than by omission.

### [SERIOUS] O4. "No network calls of any kind" is not literally true, and the pack already told us what happens to narrow-true privacy claims

The proposal's product description: *"**No network calls of any kind.**"* Its architecture section: *"the narrow, hedged claim is no longer needed: nothing leaves the device, with no caveat."*

Its own "not building" section, four pages later: *"Platform-mediated, user-opt-in crash reporting only."*

Those are reconcilable — the *app* opens no socket; the *operating system* transmits a crash log, and only for users who opted in at OS level. That is a defensible engineering position and the CTO's §5 handles it carefully and well. But it is **a narrow, technically-true claim with a third-party exception**, which is structurally the same shape as the claim the research brief spent §5 dissecting:

> DuckDuckGo's position was that it *"essentially had no choice to accept Microsoft's terms."* That is a *true, narrow, accurate* explanation. It did not work. — `haunt-brief.md` §5

The brief's own conclusion was: *"for a product whose entire value proposition is a privacy promise, a disclosed exception is read as the promise being false, and being right about the details does not help."* The pack diagnosed the honesty problem, declared it dissolved by the offline architecture, and then reintroduced a smaller instance of it in the copy without noticing. The research analyst saw this coming (§10, red flag 8): *"Haunt should expect to do the same and say so, rather than promise a purity no shipping competitor maintains."* The proposal promises the purity.

I verified the comparator myself: Arc Timeline 4's App Store privacy declaration lists **Diagnostics (Crash Data, Performance Data)** as collected. Haunt would be in the same position and would be claiming otherwise.

*What dissolves this:* marketing copy that states the platform-diagnostics exception at the same prominence as the promise, or a build that ships with crash reporting off and says so.

### [SERIOUS] O5. The venue-index evidence proves size, not correctness — and the spike that would prove correctness moved from "before the gate" to "before any build"

The CTO's measurement is the strongest artifact in the pack and I do not want to undersell it: 346,184 UK food-and-drink venues, 21.3 MB indexed, 10.8 MB compressed, CDLA-Permissive-2.0, built rather than estimated. The "bundle size" objection is dead and deserves to be.

But size is not the failure mode. I retrieved Overture's guide myself today and it says two things the pack quotes one of:

- *"Places is known to contain duplicates, a high junk rate, and low property completeness"* — quoted in the pack.
- The confidence score *"does not address duplicates or property completeness"* — **not quoted in the pack**, and the CTO's filter is `named, confidence ≥ 0.5`. The filter used is explicitly the wrong instrument for the risk named.

Second, the denominators are not read sceptically. The CTO's own trade cross-check puts Britain at **~98,914 licensed premises**. Overture's UK food-and-drink match is **346,184** — 3.5× that universe, and ~4× OSM's comparable pub+bar+nightclub+restaurant total of 84,326. The CTO reads the large number as reassurance (*"Neither open dataset looks materially deficient"*). It is at least as consistent with the duplicate-and-junk rate Overture warns about. Both readings are available from a count; neither is settled by one.

Third, and this is the part that matters procedurally: the CTO's own open-questions table sets the fix as *"Overture UK data quality as a user experiences it — how often is the right venue in the top three candidates? | Owner: Engineer, 2-day spike **before the gate**."* The research brief independently called a UK-specific coverage measurement *"the single highest-value missing fact in the brief."* The proposal relocates it to *"supporting probes the CTO wants **before any build**."* **A pre-gate condition set by the seat that owns the architecture was relaxed to pre-build without a written reason.**

On a kill this is moot. On the proceed branch it is the difference between a shippable product and one whose most visible failure — *"this app doesn't know where I am"* — is unmeasured.

*What dissolves this:* run the 2-day spike. It is cheap, it was already scoped, and it was already promised for this moment.

### [SERIOUS] O6. The benchmark that anchors every published number is still a single secondary source, flagged twice, never upgraded

Every price, every volume, every break-even in this pack is `£56,914 × hours`. Constitution 2.2 makes that benchmark the anchor of every number Candour publishes. Its provenance is one secondary page citing ONS ASHE Table 14.

This was flagged by me on 2026-09-01 (*"I did not retrieve the ONS table itself and this figure should be upgraded before anyone relies on it"*) and again by the CFO on 2026-09-09 (*"It should be upgraded to a primary ONS citation before any cost sheet is published, and I am not going to keep re-flagging it in later documents; it needs fixing once"*).

It has now been relied on by two seats across four artifacts and a gate, and it has not been fixed. `pipeline/evidence-standard.md` is unambiguous: *"A load-bearing [K] claim must be upgraded to [E] or explicitly downgraded before a gate relies on it."*

I attempted the upgrade myself rather than merely re-flagging (see Verification). The result is partial: the ONS dataset exists, the 2025 provisional edition and April 2025 reference period match the secondary source exactly, so the citation is real and not fabricated — but **the figure itself lives only inside a downloadable spreadsheet I could not open, so it remains unconfirmed at primary.** This is a case where the honest report is "the citation checks out; the number does not, yet."

*What dissolves this:* someone downloads ASHE Table 14 (2025 provisional, released 23 October 2025) and confirms £56,914, or every price in every Candour cost sheet is restated as a range until they do.

### [SERIOUS] O7. The CGO has had no part in a gate the Constitution makes it responsible for; no UX seat has looked at this at all

Constitution 5.5: *"Every pipeline phase concludes with a review pack and demo presented to the CEO in the boardroom, **compiled by the Chief Governance Officer**."* Constitution 5.6 gives the CGO the block on gate passage.

The proposal records: *"⚠️ **Not obtained — the CGO has not been commissioned and this is a gap in the pack.**"* It frames this as one missing regulatory input. It is structurally larger than that: the seat that compiles gate packs and holds the gate block has not been engaged in this gate.

I cannot tell from the artifacts whether the CGO is invoked downstream of me — my charter has me running *"before the CEO sees the pack,"* which is consistent with a CGO step after this memo. So I am not alleging a breach; I am recording that **the CEO must not receive this pack without confirmation that the CGO step happened**, and that on the proceed branch the CGO's two named questions are live and one of them (whether storing a venue name on the user's own device constitutes Candour caching) is a legal question that Constitution 6.1 may reserve to a qualified human.

Separately and with no such ambiguity: **no UX seat has assessed this product.** The proposal says so. Article 4 makes WCAG 2.1 AA a requirement without exception, and the UX seat holds a release block on Article 4 and accessibility grounds. Discovery commissioned research, cost and feasibility, and did not commission UX. On a kill, harmless. On a proceed, a seat with a block has been skipped at the only stage where its input is cheap.

*What dissolves this:* confirmation that the CGO runs before the CEO sees the pack, and a UX commission on the proceed branch.

### [SERIOUS] O8. The ceiling argument is weaker than the proposal presents, and kill criterion 3 should not carry a tick

The proposal's kill criterion 3: *"The category leader's decade-long UK base is in the hundreds of ratings. ✅ 164."*

The research brief's own evidence ledger, J3: *"Ratings-to-installs multipliers (1:50–1:200) are a guess and should not be used for sizing."* Its §9 then uses them for sizing (*"Applying any of the usual ratings-to-installs heuristics… puts Arc's paying UK base plausibly in the low thousands at most"*), hedged with *"the ceiling argument stands without the conversion."*

I do not think it does, unaided. Without a conversion, "164 GB ratings" tells you Arc has few *reviewers*, not few *customers* — and Arc's price card, which I verified today (£4.99/mo · £44.99/yr · £179.99 lifetime), means a base in the low four figures is a solid one-person business. That is not a rebuttal of the kill; it is a warning that the kill is being ticked off against a metric the analyst who produced it disclaimed. The analyst was right to name the falsifier (*"a developer statement of subscriber numbers"*) and right that nobody has one.

**The kill still stands on criteria 1, 2, 4 and 5, all of which I verified and none of which depend on this arithmetic.** Criterion 3 should be recorded as unproven rather than ticked, so that if the CEO ever revisits Haunt he is not revisiting a fact that was never established.

*What dissolves this:* any retrieved figure for Arc's actual paying base, in either direction.

### [FRICTION] O9. Two of five artifacts still carry the superseded anti-drift date

The clock correction to **2026-10-07** is right, it was raised by the Research Analyst against its own interest, and I endorse the literal reading of 5.2 for the reason given: delivering early must not buy slack.

But `cost-sheet.md` line 4 still says *"the gate on **2026-10-28**"* and `feasibility-note.md`'s closing line still says *"due 2026-10-28 per the anti-drift rule."* Two of five artifacts carry a date the pack has ruled superseded. Constitution 5.2 is the rule this company says binds the founder above all; its deadline should not appear twice, wrong, in the same folder. **27 days remain.**

*What dissolves this:* two edits and a CGO record.

### [FRICTION] O10. The cost sheet's own sensitivity note does not reproduce

`cost-sheet.md` §5: *"Adding £4,000 of build to that column moves the 5,000-buyer price from £14.63 to about £26."* On the sheet's own method, +£4,000 of build at 5,000 buyers gives **£16.00**. £25.75 is the +£4,000 figure at **2,500** buyers.

This one errs *against* the product, so it is harmless to the decision. I record it because it is the same transposition family as O1, from the same seat, and two independent instances make it a habit rather than a slip. **Nobody in this pipeline re-derives another seat's arithmetic**, and the pack's whole claim to authority is arithmetic.

### [FRICTION] O11. Support labour is modelled on two incompatible bases and nobody reconciled them

The CFO models support per-user (£1.23/paying user/yr). The CTO models it as a fixed **~2 hours/week** (≈£3,402/yr at the benchmark). At 5,000 users the CFO's line is higher; at the volumes that actually decide this (1,000–2,500 buyers) the CFO's line is **£1,230–£3,075/yr against the CTO's £3,402 fixed**. The direction of the discrepancy is the same as O2 — the pack understates cost exactly where the decision is closest.

### [FRICTION] O12. 16.5% is *below* the ~20% target, not "inside" it

The proposal: *"16.5% effective margin, inside the ~20% target."* Constitution 2.1 targets *"approximately 20% over published costs"*, with deviations *"permitted but must be justified in writing on the cost sheet."* The CFO does justify it, well and at length (§5) — commission passed through at zero markup, because *"charging the customer a margin on Apple's fee is not something I could defend to a sceptical reader."* I agree with that reasoning.

But it is a **justified deviation**, not compliance, and the cost sheet's §12 records *"Deviation from target: none proposed"* while carrying it. It also interacts with the pack's own finding that no model funds a reserve at plausible volumes, which Constitution 2.3 puts first in the waterfall. Choosing the lower of two defensible margin treatments in a product that already cannot fund a reserve is a real choice, and it should be recorded as one. It is already CEO decision #3 in the pack, which is the right place for it — it just needs the honest label.

---

## Load-bearing assumptions and the evidence for each

| Assumption | Evidence quality | If wrong, then… |
| --- | --- | --- |
| Arc Timeline 4 matches the MVP on every axis but venue ratings | **[E], verified by me today, but single-origin (vendor's own App Store listing, product page, support forum). Nobody installed the app.** The brief's own named falsifier — "Arc's notes are per-trip not per-venue" — I tested and it **does not hold**: bigpaua.com/arcapp attaches notes to places and makes "Notes & Photos" searchable for locations. Criterion 1 is stronger than the brief claimed. | Kill criterion 1 fails; Haunt's residual product is larger than "Arc plus a star rating" |
| Google Maps concedes the privacy pitch and ships the notes layer free on both platforms | **[E], verified verbatim today.** On-device Timeline, optional encrypted backup, 4,000-character notes per place. Both Google's own origin — corroboration is unavailable and arguably unnecessary; Google is the authority on Google. | Kill criterion 2 fails |
| The category ceiling is low | **[I] from rating counts, resting on a multiplier the analyst himself disclaimed (J3).** See O8. | Kill criterion 3 fails; the market may support a one-person business, which is what Candour is |
| Writing is a minority behaviour (14% of Letterboxd logs) | **[E] arithmetic on Letterboxd's own published 2024 figures**, corroborated today. Sound as arithmetic. As a *transfer* to venue journalling it is [I] across product categories, and the brief says so. | Kill criterion 4 weakens; the value-add is less fragile than assumed |
| No acquisition channel exists | **[I] from [E] on App Store search dominance (2020 data, dated) plus the deliberate closure of the sharing layer.** Weakest evidence, strongest agreement across seats, and consistent with this company's own prior finding that reach is the binding constraint. | Kill criterion 5 fails |
| Commercial places APIs cannot hold the record the product exists to hold | **[E], verified verbatim today** on Google's own developer policies. The architecture pivot is correctly grounded. | The online variant returns; the cost model changes entirely |
| The Overture offline index is fit for UK nightlife | **[E] on counts and licence (verified). [I], contested, on quality — see O5.** The instrument used (confidence ≥ 0.5) explicitly does not address the named risk (duplicates, completeness). | The product's most visible failure mode is unmeasured |
| Build is £14,719 / 450 hours | **[J], superseded by the CTO's [J] of 16–19 weeks, never reconciled.** See O2. | Every price and volume in the pack is 12–20% and 72–80% out respectively |
| Labour benchmark £56,914 | **[E, single secondary source], twice flagged, never upgraded.** Citation confirmed real today; figure unconfirmed at primary. | Every published number moves |
| Android is not viable at MVP | **[E], verified verbatim today** (Awareness API deprecated, "as early as January 2027", "no direct replacement"). The strongest-reasoned section in the pack. | Half the UK market returns, at 12–17 weeks plus a support tax |

---

## Who could this harm; who will hate it; who isn't in the room

- **Android users — 48.51% of the UK market, verified today.** Explicitly forfeited. The CTO's reasoning is correct and honest, and he correctly escalated the *word* — "in scope of the promise" downgraded to "an intention, gated on a published spike." Nobody in this pipeline speaks for them, and the discipline that "we will not claim it until it works" needs to survive the first month of low sales, which is exactly when it will be tested.
- **Users with accessibility needs.** No UX seat has looked at this product at any stage. WCAG 2.1 AA is an Article 4 requirement, budgeted at one week in the CTO's sizing, and unassessed by the seat that holds the block. On the proceed branch this is the cheapest gap in the pack to close and the most expensive to discover late.
- **Users who lose their backup passphrase.** By design, irrecoverably. The CTO handled this better than most commercial products would — plain statement, no scare modal, no pre-ticked box, local store survives — and named the dark-pattern trap correctly. I raise it only so the decision record shows it was chosen rather than inherited.
- **A privacy-attentive buyer who later reads Haunt's App Privacy declaration.** See O4. The person most likely to buy this product is the person most likely to check, and the claim they will check is the absolute one.
- **Arc's developer.** A one-person business that has shipped for a decade, into which Candour would enter with, on the pack's own account, a star rating as the differentiator. Nothing in the Constitution forbids competing. But "who could this harm" is a question my charter requires me to answer, and the honest answer includes him — and Article 1.1's test, *would they recommend it unprompted*, is not obviously met by a product whose reason to exist is a feature gap in someone else's app.
- **The people who would have to be reached.** This company's prior Skeptic memo (2026-09-01) recorded, as a finding *"fatal to the method, not to any one idea"*, that **"the binding constraint on this company is reach, not ideas."** It recommended that no further candidate be assessed until that was written down. Haunt was then taken through a full research brief, cost model and feasibility note, and arrives at a gate whose kill recommendation is, in substance, that finding rediscovered at the cost of three discovery artifacts. I record this without blame — the analysis produced real assets, including a reusable UK venue index — but Constitution 5.2 exists *"to force building over perpetual planning,"* and a pipeline that re-derives its own unanswered structural finding one product at a time is a way of planning perpetually while every individual clock runs on time.

---

## Why we might abandon this in six months

These apply only if the CEO proceeds. Each is visible today, which is the point of listing them.

1. **The landing-page test passes at 1,500 and the product still cannot pay for itself.** The mechanism is O1. This is the most likely failure and it is a failure of instrumentation, not of the market.
2. **The Overture top-three-candidate spike fails after the build has started**, because it was moved from pre-gate to pre-build (O5). "This app doesn't know where I am" is unrecoverable as a first impression.
3. **`startMonitoringVisits` battery cost turns out to be user-visible.** Apple publishes no figure; the CTO refuses to invent one and requires a two-week field measurement. Correct — and it means the central promise is unverified until roughly week 14 of a 16–19 week build.
4. **Arc adds venue ratings in a point release.** It shipped a notes improvement in v1.4.0. The differentiator is one release away from gone, from a developer already working in that area.
5. **Apple ships private place ratings in Maps**, which the research brief judged *"about two afternoons of Google product work wide"* for the equivalent gap at Google. The same is true of Apple.
6. **Support cost exceeds both seats' estimates**, because a zero-telemetry background-location app on a fleet of devices Candour cannot inspect is the worst possible support surface, and the two seats modelling it disagree about its shape (O11).

---

## Evidence verification report

Per `pipeline/evidence-standard.md`. All retrievals below were performed by me on **2026-09-10**. Nothing in this memo is cited from memory.

### Sampling statement

The pack contains **32 tagged [E] citations in the research brief, ~35 links in the feasibility note's evidence register, and ~20 in the cost sheet**, with overlap. I attempted **16 retrievals**, selected as: **every citation I judged load-bearing to the kill recommendation or to an objection in this memo** (13), plus **3 chosen to test the pack's weakest self-flagged claims** (the labour benchmark's secondary source, the ONS primary behind it, and the vendor product page behind the Arc feature claims). Foursquare and Mapbox citations were **not** sampled: they are load-bearing only to the online-API architecture, which the proposal drops entirely, and both were already flagged unverified by the seats that used them.

### Retrieved and checked — claim vs. source

| # | Claim as stated in the pack | Result |
| --- | --- | --- |
| 1 | Arc Timeline 4 App Store copy; £4.99/mo · £44.99/yr · £179.99 lifetime; 6 GB ratings; notes on timeline items | **Exact.** All four privacy sentences verbatim. Prices, rating count, developer, v1.6.1 confirmed. **Additional finding the pack uses correctly:** App Privacy declares Diagnostics (Crash Data, Performance Data) collected. **No venue rating feature found** — the claimed gap is real. |
| 2 | Google, 12 Dec 2023: Timeline saved on device; optional encrypted backup; 3-month default retention | **Exact**, all three quotes verbatim, date confirmed. |
| 3 | Google Maps notes up to 4,000 characters per place | **Exact** ("Notes can be up to 4,000 characters"). **Partial:** the *list-privacy* half of the claim is not on the page I retrieved; the brief cites a second URL for it, which I did not retrieve. Immaterial — Google Maps private lists are not in dispute. |
| 4 | Google: "must not pre-fetch, cache, or store Places API content"; place ID "exempt… store place ID values indefinitely" | **Exact**, both verbatim. |
| 5 | Overture Places: CDLA-Permissive-2.0 + Apache-2.0, no OSM data, ~74m records; "duplicates, a high junk rate, and low property completeness" | **Exact.** **Additional finding the pack omits and O5 turns on:** the confidence score *"does not address duplicates or property completeness."* |
| 6 | Letterboxd 2024: ~500m ratings, 96.4m reviews, 701m logged, 6.8m lists | **Confirmed**, verbatim, but the source returned HTTP 403 on direct fetch; I confirmed via search index of the same page. **Same origin — not independent corroboration.** The 14% arithmetic checks out. |
| 7 | Apple Small Business Program: 15% under $1m proceeds | **Exact**, plus the threshold-crossing and re-qualification clauses. |
| 8 | Google Places pricing: Nearby Search (Pro) $32.00/1,000 with 5,000 free; Place Details (Essentials) $5.00/1,000 with 10,000 free | **Exact.** |
| 9 | Awareness API: "as early as January 2027", "There is no direct replacement" | **Exact**, both verbatim. |
| 10 | StatCounter UK, Aug 2026: iOS 51.47% / Android 48.51% | **Exact.** Single source, as the CTO flagged. |
| 11 | Apple Developer Program $99/year | **Confirmed.** This **resolves a live disagreement inside the pack**: the CFO tagged it [E], the CTO tagged it *"[K, high confidence] pending CFO verification."* The CFO was right. |
| 12 | Labour benchmark £56,914 (25th/75th: £42,289/£75,794) via payprecision.co.uk citing ASHE Table 14, 2025 provisional, April 2025 reference period | **The secondary page says exactly what the CFO says it says.** |
| 13 | The ONS primary behind #12 | **Partial upgrade.** The ASHE Table 14 dataset exists; the 2025 provisional edition (released 23 October 2025) and April 2025 reference period match. **The figure itself is only inside a downloadable spreadsheet and is not on the page.** So: citation real, number still unconfirmed at primary. See O6. |
| 14 | Arc's notes attach to places; no ratings; iOS-only | **Verified on the vendor's own product page.** Notes and photos attach to places and activities; "Notes & Photos" is searchable for locations — **the research brief's own named falsifier for kill criterion 1 does not hold**. No rating system mentioned. **Upgrade to K2:** the brief could only cite a *competitor's* blog for "Arc has no Android version"; the vendor's own product page offers an iOS App Store link only. Still not a positive vendor statement, but better than the brief's flag suggests. |

### Unverifiable with my tooling — flagged, not assumed good

| # | Citation | Why |
| --- | --- | --- |
| 15 | Google Maps Platform Terms of Service (`cloud.google.com/maps-platform/terms`) §3.2.3(a)(iii) "copy and save business names", (b) No Caching, (d) No Re-Creating Google Products, (e) No Use With Non-Google Maps | **Retrieval truncated; I could not confirm these verbatim.** Mitigation: the *substance* — that names may not be stored and place IDs may — is confirmed at #4 on Google's own developer policies. **The (d) "No Re-Creating Google Products" clause, which both the analyst and the CTO flag as the sharpest legal exposure, is therefore unverified by me.** Moot on the recommended architecture; load-bearing if any online route ever returns. |
| 16 | All Apple developer documentation cited by the CTO — `startMonitoringVisits()`, `CLVisit`, `requestAlwaysAuthorization()`, Energy Efficiency Guide, MetricKit, crash-report guidance | **Not retrievable — Apple's docs render client-side and returned no content.** These are the technical foundation of the iOS recommendation. I record them as **unverified by the Skeptic**, not as unsound: they are consistent, specific, quoted with API signatures, and match well-established platform behaviour [K, high confidence, mine]. **A seat with an Apple developer account should confirm the two quotes the recommendation actually rests on** — relaunch-after-termination, and the energy-ladder ranking — before any build. |

### Independence findings

- **Arc — the single most load-bearing fact in the pack (kill criterion 1) — rests entirely on one origin: the vendor.** App Store listing, product page, privacy policy and support forum are all Big Paua. Nobody installed the app. The pack's *own* stated falsifier for this criterion was untested until I tested the retrievable half of it today. £4.99 buys a month of the actual product and would settle it completely.
- **Google Timeline claims (E1/E2/E3) are all Google-origin.** The brief flags E2 as not independent of E1. This is acceptable — Google is the authority on Google's own product — but it means kill criterion 2 rests on the incumbent's marketing about the incumbent's product, and no one has inspected the app's network traffic (the brief names this as the falsifier and assigns it to the CTO; it was not done).
- **Letterboxd (kill criterion 4)** is one origin, corroborated only by outlets restating it. One source.
- **The UK licensed-premises denominator** used by the CTO to validate coverage is **two outlets reporting one paywalled CGA report** — the CTO flags this correctly as single-origin.
- **StatCounter, dontkillmyapp, the retention benchmarks, the hobbyist Overture comparison, the willingness-to-pay survey** are each single-source, and each is flagged as such by the seat that used it. The pack's independence hygiene is genuinely good; my finding is about *Arc*, where the flagging is thinner than the reliance.

### Load-bearing [K] challenged

1. **`£56,914` labour benchmark** — challenge stands, twice-flagged, unresolved. See O6. **Upgrade or downgrade before the CEO relies on any price in this pack.**
2. **Apple UK merchant-of-record / VAT position** — the CFO tags it *"[K, high confidence, unverified]"* and notes it *"affects the shelf price by 20%."* Not upgraded. On the kill branch, moot. On the proceed branch, no shelf price may be published until it is [E].
3. **Apple Developer Program $99** — CTO tagged [K] pending verification; **now [E], verified by me.** Resolved.
4. **K2, "Arc has no Android version"** — **partially upgraded** by me: the vendor's own product page offers iOS only. Still no positive vendor statement.
5. **K4, "journalling retention is famously bad"** — remains unverified and the analyst correctly refused to invent data. It does not appear in the proposal's kill criteria, which is the right call. **The CEO should not carry it into the decision as though it were evidence.**

### Arithmetic re-derivation

I re-derived the pack's pricing arithmetic from the cost sheet's own stated formulae rather than accepting any table. Two independent transposition errors surfaced (O1, O10) and one unreconciled input (O2). The method itself reproduces cleanly — the cost sheet's £14.63 recomputes to £14.65 on my working — so the errors are in *which cell was carried forward*, not in the model. **That is the more worrying kind, because the model is what got reviewed.**

### Reading-list gap (not steering — recorded for the auditor)

The gate's reading list omitted `research/scouts/scout-2026-09-01-skeptic-cull.md` and `research/scouts/scout-2026-09-01.md`. Both are cited as load-bearing inside the pack: the cost sheet's §1 labour-treatment argument (CEO decision 1) is a reply to them, and the research brief's §9 pricing cross-check builds directly on the cull memo's §4. A reader given only the listed files cannot audit either. **I retrieved both myself and they say what the pack says they say.** I record the gap so the decision record notes that the pack's CEO-level definitional decisions have upstream documents.

### Steering detected in this memo's invocation

**None.** The invocation was the gate slug, the file list, my charter, and a process instruction to write incrementally. No summary, no opinion, no framing, no "should be fine," no expected conclusion. It also explicitly invited a steering report, which is the right way round. This is a clean invocation as `roles/skeptic.md` defines it, and I record it as such.

**Two things inside the artifacts that a cold reader should notice, since they are steering of a legitimate kind:**

1. `proposal.md` opens with a boxed **"CVO recommendation: KILL"** above any evidence. The CVO is entitled — required, even — to recommend. But a pack that states its conclusion in the first screen and its arithmetic on the fourth invites the reader to check the arithmetic less carefully. Given O1, that is not hypothetical.
2. The kill criteria are presented as a **✅ checklist** with all five already ticked. Three of the five (1, 2, 4) I verified and they hold. One (5) is an inference the seats agree on. **One (3) is ticked against a metric the analyst who produced it disclaimed for exactly this use.** A tick renders a contested inference as a settled fact, and it does so in the section a busy reader reads first.

Neither is misconduct. Both are the ordinary gravity of a pack written by a seat that has reached a conclusion, and naming that gravity is what this seat is for.

---

## Constitutional concerns (including inconvenient ones)

**Where the pack complies, and deserves the credit:**

- **1.5 / 2.1** — running cost of £83/year fixed and £0/user is real, verified at its two components, and structural rather than disciplinary. This is the first Candour candidate where the cheapness claim is architecture.
- **4 (minimum data / export)** — the CTO's schema-is-the-export design, import-at-MVP, and user-readable diagnostic bundle with a build-failing redaction test are better than the Article requires. **An under-sold consequence nobody states:** on the zero-network architecture Candour almost certainly never becomes a controller of journal data at all, which removes most of the UK GDPR surface rather than merely complying with it. That is a genuine strength the pack leaves on the table.
- **1.3 / 4 (no unsubstantiable claims)** — the CTO's insistence on downgrading "Android is in scope of the promise" to an intention, and on refusing a battery claim until measured, is the Constitution working as designed. So is the CFO's advance block on any free tier that gates entries already written, and the CVO's endorsement of it.
- **5.3** — the CVO recorded the Research Analyst's disagreement on the sharing layer and *accepted it in full, against the CVO's own earlier position*, with the reason stated. The CTO's platform disagreement was recorded and accepted. That is the dissent institution functioning.
- **5.2** — the clock correction moved the deadline **21 days earlier**, against the pipeline's own convenience, raised by the seat that benefited from the looser reading. That is the rule binding the people it is meant to bind.

**Where it does not, or not yet:**

1. **Evidence standard, verification clause.** A load-bearing single-source benchmark, flagged twice, has reached a gate unupgraded. This is now a pattern across two documents and nine days. (O6)
2. **Constitution 5.5.** The CGO has not compiled this pack. Confirm the step exists before the CEO reads it. (O7)
3. **Article 4 / 5.6.** The UX seat, which holds a release block on Article 4 and accessibility grounds, has had no involvement. (O7)
4. **Article 2.1.** A justified deviation below the 20% target is recorded as "no deviation." (O12)
5. **Article 8.** A designation the CFO asked to be live at this gate is disposed of by omission. (O3)
6. **Article 1.3.** The headline claim is more absolute than the pack's own architecture supports. (O4)
7. **Constitution 5.2, in spirit.** Two of five artifacts still publish the superseded deadline. (O9)

**The inconvenient one, which is about the company and not about Haunt.** My predecessor memo of 2026-09-01 recorded a finding it called *"fatal to the method, not to any one idea"* — that Candour's cost-plus pricing rule is anti-scale, and that the binding constraint is reach rather than ideas — and asked that no further candidate be assessed until that was written down. It has not been written down. Haunt then consumed a research brief, a cost model and a feasibility note to arrive at a kill whose substance is that same finding. Constitution 5.3 requires dissent to be *answered in writing*, and while a scouting memo is not a gate memo, **the practical effect of leaving it unanswered is that the company will pay for this discovery again on the next candidate.** I raise it once, here, as my charter requires, and will not repeat it outside the annual audit.

---

## What would soften this dissent

Concretely, and in the order that matters:

1. **Correct the pricing table and restate the proceed threshold.** ~2,370 sales at £14.63 on the CFO's build hours; ~2,550–2,660 on the CTO's. This alone converts O1 from fatal-to-proceed to nothing.
2. **Re-run the cost model on the CTO's 16–19 weeks**, reconcile the two support bases, and publish the revision. Dissolves O2 and O11.
3. **Answer Article 8 in one written paragraph** — on demand grounds, which the pack has the evidence for. Dissolves O3. I expect the answer to be "no," and the record should show it was an answer.
4. **Restate the marketing claim** as "the app makes no network calls; platform crash reporting, if you have it switched on, still applies" — at the same prominence as the promise. Dissolves O4.
5. **Run the 2-day Overture top-three-candidate spike before the gate concludes**, as the CTO originally specified. Dissolves O5. It is two days and it was already scoped.
6. **Upgrade the ONS benchmark to primary, once, for the company.** Dissolves O6 permanently, for every cost sheet Candour will ever publish.
7. **Confirm the CGO step; commission UX on the proceed branch.** Dissolves O7.
8. **Untick kill criterion 3** and record it as unproven. Dissolves O8. If anyone wants to prove it instead: £4.99 buys a month of Arc, which would also close the last single-origin gap under kill criterion 1.
9. **Fix the two stale dates.** Dissolves O9.

**And a note on what would *not* soften it.** None of the above is an argument for building Haunt. Having done the checks, I think the CVO's recommendation is right and I would not manufacture a case against it to look independent. The product exists, the free incumbent concedes the pitch, the differentiating behaviour is the minority behaviour, and there is no channel. **Where I differ is that the pack currently supports a kill more securely than it supports anything else — including the cheap test it proposes — and it does not say so.** The safest reading of this pack is: kill it, keep the venue index, and settle the three standing definitional questions and the reach question while nothing is at stake. That last part is the most valuable thing in the folder and it is the part with no deadline attached to it.

---

*Prepared under `roles/skeptic.md`. This memo prepares and flags; it does not certify, and it carries no block by design (Constitution 5.6). Kill / proceed / park is the CEO's decision alone (Constitution 5.4), due **2026-10-07** (Constitution 5.2). Honest limitation, restated as my charter requires: I am the same model, run by the same person, as every other seat in this pack. These procedures replicate the structural conditions of independence; they do not create it.*

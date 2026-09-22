# Gate pack — Haunt

**Compiled by:** Chief Governance Officer (Constitution 5.5) · **Presented to:** CEO, in the boardroom · **Date:** 2026-09-10
**Slug:** `haunt` · **Phase concluding:** discovery (spark → research brief → cost model → feasibility → seat notes → proposal)
**Decision due:** **2026-10-07** (Constitution 5.2). **27 days remaining.**
**CGO position on gate passage:** **I do not block.** One block engages **only if the decision is PROCEED in either form** — see §5.4. Three conditions, restated in §5.

> **Template note.** `pipeline/templates/review-pack.md` is written for a build-phase review with a demo. This is a decision gate, so the template's "What this phase set out to do vs what it did", "Demo", "Seat reports", "Constitution & compliance status", "Open dissent and unresolved flags" sections are preserved and mapped (§2, §3, §9, §8, §6), and the sections a gate needs and the template lacks — options, consolidated blocks, evidence health, anti-drift, reserved decisions — are added. The deviation is stated rather than made silently. The template's final section, "Recommended next step", is **deliberately left empty**: the CGO enforces process and compiles; the decision is the CEO's alone (Constitution 5.4).

> **Evidence convention for this document.** I performed **no new retrieval** in compiling this pack. Every `[E]` below travels from a named artifact, retrieved by a named seat on a named date, and I say which. Where I state a judgment of my own it is tagged `[J]`; where I reason from other seats' tagged premises it is `[I]`. Document mechanics — counts of blocks, which file says what, arithmetic — are untagged per `pipeline/evidence-standard.md`. **Nothing in this pack is certified. Agent reviews prepare and flag (Constitution 6.1).**

---

# 1. Page one — what the CEO is deciding

*If you read only this page, you have the decision. It is deliberately not a summary of the recommendation; it is a summary of the disagreement.*

**The thing.** Haunt is a private, on-device journal of the places you go: iOS watches for you settling somewhere, asks "were you here?", and on confirmation puts the visit on a timeline you can annotate and rate. Discovery changed the architecture: the venue name now comes from a bundled offline index derived from Overture Places (**346,184 UK food-and-drink venues, 21.3 MB indexed, 10.8 MB compressed, permissively licensed** — the CTO built and weighed it rather than estimating it [E, CTO, measured 2026-09-09]), so the app makes no venue lookups at all. Fixed running cost is **£83/year** plus an ICO charge nobody has priced. iOS only; Android is an intention gated on a spike, not a promise.

**The recommendation in front of you is KILL, and it is the CVO's own.** He sparked the idea and is recommending against it. He also asks you to discount his recommendation, because the Skeptic found a real arithmetic error at the centre of his case and a material omission that happened to favour his own conclusion.

**What makes KILL look right** — the first three verified verbatim by the Skeptic on 2026-09-10; the fourth is an inference every seat agrees on:

1. **The product already exists.** Arc Timeline 4 (iOS, shipped 12 April 2026) matches the MVP on every axis but venue ratings, and its own App Store copy is close to Haunt's privacy promise verbatim. The research brief named its own falsifier for this — that Arc's notes might attach to *trips* rather than *venues* — and the Skeptic tested it: **it does not hold.** Arc attaches notes to places.
2. **The free incumbent conceded the privacy pitch in December 2023.** Google Timeline is on-device with optional encrypted backup, free, both platforms — plus private lists with 4,000-character notes per place. The notes layer the CVO thought was the residual is largely conceded too.
3. **The differentiating behaviour is the minority behaviour.** On Letterboxd's own 2024 figures, **14% of logs carry any writing** — with an audience. Haunt removes the audience and sells the writing.
4. **There is no acquisition channel and no budget to buy one**, by design, now doubly so with the sharing layer closed. *(This one is not measured: it rests on 2020 App Store data the Skeptic calls the weakest evidence in the pack and the strongest agreement across seats.)*

**What argues against the recommendation, and none of it is decoration:**

- **A fourth option was left out of the pack, and its omission favoured the recommendation.** The CFO asked in writing that **Article 8 non-profit designation** be *"a live option at the gate rather than a rhetorical one"*, and named the condition that would make it live: the research brief confirming Google already ships the local-only pitch free. **The brief confirmed exactly that.** The CVO's proposal argued the kill almost entirely on economics that designation dissolves, and disposed of designation by not listing it. It is restored in §3.3 at full strength, including the part the CVO disagrees with.
- **The strongest argument for designation is a Constitution 1.1 argument, not a money one.** 1.1's test is whether people would recommend it unprompted. A genuinely zero-network, open-source, self-hostable location journal is the kind of thing the privacy community does recommend unprompted; a £14.63 paid app competing with 164 UK ratings is not.
- **One of the five kill criteria should not be ticked.** Criterion 3 ("the category leader's decade-long UK base is in the hundreds of ratings — 164") converts a rating count into a user base using a multiplier the Research Analyst who produced it **explicitly disclaimed for this use**. The Skeptic: without the conversion, 164 ratings tells you Arc has few *reviewers*, not few *customers* — and at £4.99/mo · £44.99/yr · £179.99 lifetime, a base in the low four figures is a solid one-person business. **Candour is a one-person business.** The proposal downgrades the criterion in prose and still shows it as ✅. It should be recorded as **unproven**.
- **The compliance position is the best this company has designed, and it cuts against the kill.** On the zero-network architecture Candour is **neither controller nor processor** of journal data (household exemption); it is party to no third-party data terms; and Article 7.2's open-sourcing promise is deliverable in full with no carve-out. **The regulatory case for killing Haunt is nil.** If it dies, it must die on market evidence, and the decision record should say so — so nobody in two years mistakes a demand judgment for a compliance judgment and reopens it on the wrong grounds. *(This is my own finding, and I record that it argues against the seat recommendation.)*
- **The most load-bearing fact in the pack rests on one origin: the vendor.** Everything known about Arc comes from Big Paua's own App Store listing, product page, privacy policy and support forum. **Nobody installed the app.** £4.99 buys a month of it and would settle kill criterion 1 completely.
- **There is a documented trust injury to trade on.** Google's on-device Timeline migration destroyed real users' history and Google declined to say how many were affected. Timeline is also opt-in, off by default, and defaults to deleting after three months — so most people hold no long archive.

**What the Skeptic actually said, both halves, because both belong here:**

> *"Its recommendation to kill is, in my judgement, the honest reading of its own evidence. **My dissent is not that the kill is wrong.**"*

and, on the same page:

> *"The CFO asked, in writing, that Article 8 designation be 'a live option at the gate rather than a rhetorical one.' The proposal does not answer it. The kill is argued entirely on grounds that Article 8 designation dissolves."* — an omission it calls *"the worst kind: the one that happens to favour the author's recommendation."*

and, decisively for anything that is not a kill:

> *"If the CEO's decision is anything other than KILL, this pack is not fit to support it."*

That last sentence is the governing constraint on this gate. The proposal's single falsifier was set ~40% below the break-even it purported to represent; it has been corrected to **~2,700 buyers**, but the cost model underneath it **has still never been re-derived on the CTO's build hours**. A PROCEED today would be a PROCEED on a cost model whose largest line is 33–58% understated.

**What this pack cannot tell you, stated so you are not misled by its length:**

- Nobody has measured whether the offline index finds the right UK pub (the CTO's own 2-day spike was set for *before the gate* and was moved to *before any build*, **without a written reason**).
- Nobody has run a usability test, seen a prototype, or spoken to a user.
- Nobody has measured the battery cost of the capture API; Apple publishes no figure and the CTO refused to invent one.
- Nobody installed Arc.
- The labour benchmark that anchors **every price, volume and break-even in this pack** is a single secondary source, flagged three times by two seats, and still unconfirmed at primary.

**Your four options** (full statements, commitments, foreclosures and conditions in §3):

| | Option | In one line |
|---|---|---|
| **A** | **KILL** | Stop. Keep the venue index. Settle the standing definitional questions while nothing depends on the answer. |
| **B** | **PROCEED** (commercial) | Authorise a UK landing-page test calibrated at **~2,700 buyers**, plus two CTO spikes, before any build — and a re-derived cost sheet before either. |
| **C** | **PROCEED UNDER ARTICLE 8 DESIGNATION** | Permanent, irreversible. £14,719 unrecovered build plus **£4,989/year indefinitely**, from a waterfall holding **£0**. Deletes every pricing and Article 4 question in the pack. |
| **D** | **PARK** | Requires a **written reason and a revisit date** (5.2). The CVO argues against it; nobody else has argued for it. |

**Not on the table today: a price.** The cost model predates the feasibility note, contradicts it on the largest single cost, omits the ICO charge, and carries two arithmetic defects the Skeptic re-derived. No shelf price may issue from it in its current state.

**One company-level finding, which is not about Haunt.** The Skeptic's memo of 2026-09-01 recorded, as a finding *"fatal to the method, not to any one idea"*, that **the binding constraint on this company is reach, not ideas**, and asked that no further candidate be assessed until that was written down. It has not been. Haunt then consumed a research brief, a cost model, a feasibility note, a compliance note and a UX note to arrive at a kill whose substance is that finding rediscovered. Every individual clock ran on time. **A pipeline that re-derives its own unanswered structural finding one product at a time is a way of planning perpetually while every deadline is met.** Whatever you decide about Haunt, that finding is still owed an answer in writing.

---

# 2. What this phase set out to do, and what it did

**Commissioned at spark (2026-09-09).** The CEO closed four scope forks and left money open. Discovery was commissioned to close six research questions (a)–(f), model three pricing shapes side by side, and answer a set of technical feasibility questions.

**What it produced.** All of it, plus two artifacts nobody commissioned at spark:

| Artifact | Seat | Date | Status |
|---|---|---|---|
| `proposals/haunt/idea-brief.md` | CVO | 2026-09-09 | Complete. Corrected 2026-09-09 on the anti-drift date. |
| `research/haunt-brief.md` | Research Analyst | 2026-09-09 | Delivered **21 days early**. Carries a CVO-added citation challenge at §7.3 (2026-09-10). |
| `products/haunt/cost-sheet.md` | CFO | 2026-09-09 | **Written before the feasibility note existed. Never re-derived against it.** |
| `products/haunt/feasibility-note.md` | CTO | 2026-09-09 | Complete. Includes measured artefacts, not estimates. |
| `products/haunt/compliance-note.md` | CGO | 2026-09-10 | Complete. Does not block; three conditions. **Stale on one point — see §8.3.** |
| `products/haunt/ux-note.md` | UX / Design Lead | 2026-09-10 | Complete. Seven would-be release blocks. **Commissioned only at gate preparation.** |
| `proposals/haunt/dissent-memo.md` | The Skeptic | 2026-09-10 | **Published unedited.** Twelve objections, one fatal to the PROCEED branch. |
| `proposals/haunt/proposal.md` | CVO | 2026-09-09, corrected 2026-09-10 | Recommends KILL. Carries the ⚠ correction blocks (§8.1). |

**What discovery actually changed, and it is the most useful thing it produced.** The spark assumed an online venue lookup with a disclosed privacy caveat and treated a fully-offline build as an expensive fallback. **Both halves were wrong**, and both were corrected by measurement and by retrieval rather than by argument:

- The online route is **not legally available** for a permanent journal. Google's terms permit indefinite storage of a `place_id` and nothing else; venue names are Google Maps Content [E, CTO §2.1 / Research Analyst §7.1, retrieved 2026-09-09]. Foursquare's paid API is the same shape, and its own usage guidelines regulate *"local-device caching"* by name — 24 hours for Enterprise, **none at all for Pay-as-you-go** [E, CGO §1.1, retrieved 2026-09-10]. Apple's clause is ambiguous and Apple's own DTS engineer declined to interpret it and told the developer to hire a lawyer [E, CGO §1.1, thread 807656].
- The offline route is **small, free and permissively licensed**, and it is roughly build-neutral, because it deletes as much work as it adds.

**Three things discovery did not do**, and they matter to §5 and §7: it did not run the CTO's own pre-gate venue-quality spike; it did not commission UX until the gate was being prepared; and it did not re-derive the cost model after the feasibility note landed.

---

# 3. The four options

Constitution 5.2 names three outcomes — kill, proceed, park. **Article 8 designation is a distinct form of proceed** with different commitments, different foreclosures and a different irreversibility, so it is presented separately rather than folded into PROCEED. That is a compilation decision by this seat and I state it as one.

## 3.1 Option A — KILL

**What it commits Candour to.** Stopping. A public decision record within 30 days (Article 3). Nothing else.

**What it forecloses.** Nothing permanently — a kill is not a bar on revisiting, though the evidence will not improve by waiting and Arc will not get smaller. It does forfeit the specific window in which the CVO, CFO, CTO, UX and Skeptic seats all hold this material in front of them at once.

**Seat conditions attached:** none. No seat blocks a kill. The Skeptic holds no block by design (5.6), and its memo says the kill is the honest reading of the pack's own evidence.

**What the record must still carry on this branch** (CGO):
1. A written answer to the Article 8 option (§3.3) on **demand** grounds, not by omission. The Skeptic expects the answer to be "no" and says *"the record should show it was an answer."*
2. The statement that Haunt died on market evidence and **not** on compliance grounds (§1, and compliance note §8.3).
3. A disposition on the **salvage**: the measured UK venue index is a genuine reusable asset, and republishing it is itself a redistribution carrying CDLA-Permissive-2.0 §2.1 and Apache-2.0 §4 obligations (compliance note §2.6).
4. The three standing definitional decisions (§7), which outlive Haunt.
5. An answer, or a scheduled answer, to the reach finding of 2026-09-01.

## 3.2 Option B — PROCEED (commercial)

**What it commits Candour to.** In sequence, and the sequence is the point:

1. **A re-derived cost sheet** on the CTO's 16–19 focused weeks (600–712.5 h, £19,626–£23,306) rather than the CFO's 450 h / £14,719, with the two support bases reconciled and the ICO charge added. Nothing downstream is trustworthy until this exists.
2. **A UK landing-page test** calibrated at **~2,700 buyers** — the top of the honest range, chosen because *"a falsifier that flatters the idea is not a falsifier."* This is the only pre-build spend the CVO would authorise. Spending real money is a 5.4 decision.
3. **Two CTO spikes**: the 2-day Overture top-three-candidate spike (which the UX seat asks be re-specified to report four metrics — top-3 hit, duplicate rate, junk rate, miss rate), and a measured battery cost for `startMonitoringVisits` over a real week.
4. Only then, a **16–19 focused-week iOS build**, of which the central promise (battery cost) is unverified until roughly week 14.

**What it forecloses.** Android at MVP, and roughly half the UK market at launch (iOS 51.47% / Android 48.51% [E, CTO, StatCounter, single source, Aug 2026]). Any online places API — dropped from the architecture rather than shipped and retrofitted; re-adding one is a gate-level change, not a feature. Any sharing, social or public layer — and the compliance note asks that this be recorded as a **gate-level commitment**, so adding one later requires a fresh gate and a fresh Skeptic memo rather than a product decision made by whoever is looking at retention numbers in eighteen months.

**Seat conditions attached:** the heaviest set. All of §4, in particular: CGO conditions 1–3 (§5), the CFO's Article 4 launch block, all seven UX would-be release blocks, and both CTO blocks. **Plus the CGO's conditional block under 5.3 (§5.4): six Skeptic objections remain unanswered in writing, and 5.3 requires the dissent to be answered, not acknowledged, before a proposal is approved.**

**The honest description of this branch.** You would be authorising a cheap test whose threshold is derived from a model that has not been corrected, to decide whether to build a product that already exists on the platform you would ship on, against a free incumbent on both platforms, with no acquisition channel.

## 3.3 Option C — PROCEED UNDER ARTICLE 8 DESIGNATION

**Restored at full strength. The CVO omitted it; the Skeptic identified the omission as favouring the CVO's own recommendation. It is stated here as the CFO stated it, not as the CVO would prefer it.**

**What it commits Candour to** (CFO, cost sheet §9):

- **£14,719 of unrecovered build labour** (more, on the CTO's hours: £19,626–£23,306), plus **£4,989/year indefinitely** — maintenance £3,271, community support £1,635, Apple £73, domain ~£10 — funded from the Article 2.3 waterfall, **which currently holds £0, because no Candour product has ever earned anything.**
- **Zero distribution, permanently.** Article 8 designation is **permanent and irreversible** for that product. It can never be sold; it may only be transferred to an asset-locked body, and Article 7.2 governs any shutdown.
- An open-source and self-hostable posture, **decided per initiative at its gate and recorded with reasons** (Article 8) — so that decision is itself owed at this gate if you designate.
- Honest description, in the CFO's own terms: **one full build and about £5k/year of benchmarked founder labour, forever, with no recovery mechanism.**

**What it buys** (CFO): *"it deletes the pricing question, the free-tier question, the Article 4 cap question, the store-commission question, the adverse-selection question, and the 'can we honestly promise lifetime support' question."* The per-user API cost also goes to zero under bring-your-own-key, because the meter moves to the user. The CFO's summary sentence, which the CVO never answered: ***"Everything difficult in sections 5 through 8 of this document is an artifact of trying to charge for it."***

**The CFO's argument at its strongest:** designation is the only structure in which ***"we cannot beat free, and we are not going to pretend we can"*** is a coherent thing for Candour to say **and still ship the product**.

**The Article 1.1 argument, which is the real one** (surfaced by the CVO as the strongest case against his own position, and endorsed by nobody as a recommendation): 1.1 judges products by whether people would recommend them unprompted. A genuinely zero-network, open-source, self-hostable location journal — **which neither Arc nor Google offers**, since Arc's own App Privacy declaration lists Diagnostics as collected — is exactly the kind of thing that gets recommended unprompted. A £14.63 paid app with 164 competing ratings is not. Designation converts the one surviving differentiator from a thin commercial edge into a coherent public-good pitch.

**What it forecloses.** Everything, permanently, for this product: no sale, ever; no distribution, ever; no route back to a commercial model. It also commits an **unincorporated brand with £0 income** to an irreversible perpetual cost. And the UX seat notes it removes every dark-pattern surface in the pricing analysis, because there is no conversion to engineer.

**The case against it, from the two seats who made it:**

- **The CVO** (stated as a position, not a finding): designation answers the *money* objection completely and does not touch kill criteria 1, 2 or 4. The product still exists (Arc), a free incumbent still ships it on both platforms (Google), and the differentiating behaviour is still a minority behaviour. *"Giving away a product that is already available free is not obviously better than not building it."*
- **The Skeptic**, who is explicit that this is not advocacy: *"I am not arguing for Article 8 designation. I think it probably fails, and I think it fails for a reason the pack has the evidence for and never states: **Article 8 dissolves the pricing problem and leaves the demand problem untouched.**"* A free, open-source Haunt still competes with a free Google Maps and with Arc, which is nearly free at the margin for anyone already paying for it. **But:** *"It is missing from the pack, and a decision record that kills Haunt without making it will not show that the option was actually considered."*

**Seat conditions attached:** the UX would-be release blocks B1, B3, B4, B5, B6, B7 still apply (B2 — the pricing-cap block — falls away with the price). The CGO's licence-surface and backup-deletion conditions still apply, and the salvage/redistribution obligations in compliance note §2.6 bind harder, since the whole thing is redistributed. The CTO's Block 1 still applies. Article 8's own requirement that the open-source/self-hostable decision be **recorded with reasons at the gate** becomes a live obligation the same day.

## 3.4 Option D — PARK

**Constitution 5.2: "Park" requires a written reason and a revisit date.** A park without both is not a park; it is drift, and 5.2 exists to prevent exactly that.

**What it commits Candour to.** A written reason and a date, both public in the decision record within 30 days (Article 3). If parked, the anti-drift clock does not simply restart — the reason must name what will have changed by the revisit date that makes the answer different.

**What it forecloses.** Nothing formally. In practice it forecloses the cheap version of every remaining test: the Skeptic's £4.99 Arc install, the 2-day venue spike, the one-morning benchmark upgrade, the five-person usability test — all of which are cheaper than parking and re-reading this folder in three months.

**Seat conditions attached:** none, except the 5.2 formal requirements above.

**The argument against, from the CVO:** *"Parking a question this thoroughly answered is the drift 5.2 exists to prevent. The evidence will not improve by waiting, and Arc will not get smaller."*

**The argument for, which no seat has made and which I record so the option is real rather than decorative** [J, CGO]: the two facts that would most change this decision — whether the offline index finds the right UK pub, and whether Arc's paying base is four figures or three — are both cheap, both unmeasured, and both currently scheduled for *after* a decision that depends on them. A park of **two weeks** with those two measurements named as its reason, and a revisit date inside the 2026-10-07 deadline, is a coherent use of the clock rather than an evasion of it. A park of three months is not.

---

# 4. Every block, would-be block and condition, in one table

Consolidated from five seats. **Nothing except row G4 can halt this gate**: the CGO holds the gate block (5.6), and everything else is either pre-declared for a later stage or a condition attached to a decision. Each row states the clause, what lifts it, and **when it actually engages**.

| # | Seat | Block / condition | Clause cited | When it engages | What lifts it | Status today |
|---|---|---|---|---|---|---|
| **G1** | CGO | **UX seat involvement on any PROCEED.** *(Restated — see §8.3: my compliance note wrote this before `ux-note.md` existed and is stale.)* Restated: the discovery-stage UX assessment now exists; what remains is that the UX seat's seven would-be blocks become **acceptance criteria at requirements stage**, and that UX runs at build and pre-release. | Art. 4 (WCAG 2.1 AA, dark patterns); 5.6 | **At the decision.** The decision record must name it on any PROCEED. | The decision record naming UX involvement at requirements, build and pre-release as a condition of PROCEED. | **Live.** Original form partly discharged by `ux-note.md` (2026-09-10). |
| **G2** | CGO | **The marketing claim is corrected before the CEO decides.** The pack rests its only surviving differentiator on this claim, and CRA 2015 s.36 makes App Store description copy a **term of the contract**, not copy. | Art. 1.3, Art. 4 (honest marketing); CRA 2015 s.36 [E, CGO, retrieved 2026-09-10] | **At the decision.** | The substantiable wording appearing in the proposal. | **Met** — the proposal's second ⚠ correction of 2026-09-10 carries it. **Residual defect recorded at §8.4:** the product-description headline still hedges ("no network calls in normal operation"), which the same analysis defeats. |
| **G3** | CGO | **Licence surface and backup deletion written into the requirements document.** In-app "Data sources and licences" screen carrying the full CDLA-Permissive-2.0 text, the full Apache-2.0 text, the unaltered Foursquare OS Places NOTICE.txt, and a modification notice; same texts in the export README; **"Delete my backup" as a launch requirement.** | CDLA-Permissive-2.0 §2.1; Apache-2.0 §4(a)(b)(d); FSQ NOTICE; Constitution Art. 4 (minimum data / deletion) [E, CGO, retrieved 2026-09-10] | **At requirements**, on either PROCEED branch. Cheap now, expensive after the schema and settings tree exist. | The items appearing as acceptance criteria. | **Not met.** Half a day of work. |
| **G4** | **CGO** | **CONDITIONAL BLOCK ON GATE PASSAGE — engages only on PROCEED (Option B or C).** Six of the Skeptic's twelve objections are **not answered in writing** anywhere in the pack: O2 (cost model never re-derived), O5 (pre-gate spike relocated to pre-build with no written reason), O6 (labour benchmark), O10 (cost sheet §5 sensitivity arithmetic), O11 (two incompatible support bases), O12 (a justified margin deviation recorded as "none proposed"). | **Constitution 5.3** — *"Approving a proposal requires responding to the dissent in writing, not merely outvoting it."* | **At the decision**, and **only** if the decision approves the proposal. A KILL is not an approval; a PARK is not an approval. | A written response to those six objections, in the proposal or in the decision record, before PROCEED is recorded. Only the CEO may overrule, and the overrule is recorded publicly (5.6). | **Live on the PROCEED branches. Not engaged on KILL or PARK.** |
| **G5** | CGO | **The labour benchmark is upgraded to primary, or every figure derived from it is restated as a range**, before any landing-page test is calibrated and before any price is published. | `pipeline/evidence-standard.md` — *"A load-bearing [K] claim must be upgraded to [E] or explicitly downgraded before a gate relies on it"*; Constitution 2.2, 3 | **Pre-test and pre-publication** on the PROCEED branches. Moot on KILL. | Someone downloads ONS ASHE Table 14 (2025 provisional, released 23 Oct 2025) and confirms £56,914 — one morning, once, for every cost sheet this company will ever publish. | **Not met.** Flagged three times by two seats since 2026-09-01. |
| **T1** | CTO | **Any architecture that persists places-API venue records in the local journal.** | Google Maps Platform ToS 3.2.3(b) + Service Specific Terms A.3, 14.3; Constitution 1.5, Art. 7.2 [E, CTO §2.1, retrieved 2026-09-09] | **At architecture / build commencement.** Not engaged on the MVP as proposed, which touches no places API. | A dataset whose licence permits permanent local retention (Overture / FSQ OS Places / OSM under ODbL); **or** Mapbox Permanent Geocoding with terms verified against the cost model; **or** written provider confirmation. **CGO note:** the third limb is a deferral mechanism, and on the Apple precedent it is unlikely to succeed. | Pre-declared. Not engaged. |
| **T2** | CTO | **An Android MVP whose capture reliability rests on undocumented OEM behaviour.** | Constitution 1.3 and Art. 4 — no claims we cannot substantiate [E, CTO §1.2(f), retrieved 2026-09-09] | **If and when Android is proposed.** Not engaged — Android does not ship at MVP. | A published device-matrix spike over ≥2 real weeks on at least Pixel, Samsung and Xiaomi, with a minimum capture rate agreed with PM/BA and QA **before** the spike runs. | Pre-declared. Not engaged. **Related live rule:** Android may not be marketed before that spike. |
| **F1** | CFO | **Launch-blocking Article 4 finding: any free tier that restricts access to entries the user has already created.** The CFO's formulation: *"That is not a paywall. That is a hostage, and the hostage is being held on the victim's premises."* | Constitution Art. 4 (*"at any time, at no charge and with no penalty"*, dark patterns) and Art. 1.2 (lock-in) | **At requirements** (the moment a tier is designed) and **at launch**. | A cap that restricts only *future creation* or *metered lookups*, with complete export available at every tier at all times. **But see §6.4: the metered-lookup basis no longer exists on the offline architecture.** | Pre-declared. **Three seats hold it:** CFO first, CVO endorsed, CGO records its own block on the same facts, UX records it as B2. |
| **F2** | CFO | **A lifetime unlock combined with a metered per-lookup API.** *"The one combination this cost sheet says Candour must not ship."* | Constitution 2.1 (unfunded perpetual liability); Art. 4 (no drip pricing / no later billing) | **At pricing / launch**, only if any metered API returns. | An unmetered venue source, **or** a plainly-stated, pre-purchase fair-use cap on automatic lookups. | Moot on the MVP as proposed. Live the moment T1's architecture returns. |
| **U-B1** | UX | Any notification that fires to bring the user back into the app on a cadence the user did not set — confirm-queue prompts, digests, "you haven't written in N days", a default-on badge count. | Art. 4 — *"no engagement mechanics designed to exploit compulsion"* | **Release.** Design decisions that determine it are made at **requirements**. | Notifications off by default; every type user-enabled; frequency and time user-chosen; one-tap off inside the app; the authorization-loss carve-out capped at **one notification per state transition**. | Pre-declared. |
| **U-B2** | UX | A free tier, trial expiry or subscription lapse that restricts reading, editing or exporting entries the user already wrote. | Art. 4 and Art. 1.2 | **Release**; determined at **requirements**. | The product degrades to a full read/write/export journal in every unpaid state. | Pre-declared. Same facts as F1. |
| **U-B3** | UX | **Any function reachable only by interacting with the map** — confirming a visit, choosing a venue, opening or editing an entry, rating. | WCAG 2.1 SC 1.1.1 (A) and SC 2.5.1 (A) [E, UX, retrieved 2026-09-10] | **Release** — but this is the **one architectural item**: list-first vs map-first must be settled **before any screen is built**. | A list route to every map function, demonstrated by QA completing the full core loop with VoiceOver and with Voice Control, screen untouched. | Pre-declared. **Cheapest possible moment is requirements; retrofit is the expensive shape.** |
| **U-B4** | UX | Rating, capture state or other information encoded by colour alone; text or pins over map tiles without a controlled contrast surface. | WCAG 2.1 SC 1.4.1 (A), 1.4.3 (AA), 1.4.11 (AA) [E, UX] | **Release.** | Every rating readable in greyscale and present as text; measured contrast evidence for pins and map labels against the worst-case tile in both map styles. | Pre-declared. |
| **U-B5** | UX | Timeline rows that clip, truncate the venue name, or lose actions at the largest Dynamic Type sizes. | WCAG 2.1 SC 1.4.4 (AA) [E, UX] | **Release.** | Screenshots of every primary screen at the largest accessibility text size with no loss of content or function. | Pre-declared. |
| **U-B6** | UX | A design in which losing the backup passphrase also loses the on-device journal. | Art. 4 (export at any time, no penalty) and Art. 1.3 | **Release**; determined at **data-layer design**. | The local store remains readable and exportable independent of the backup key — the CTO's stated design, made an acceptance criterion rather than an intention. | Pre-declared. Currently an intention, not a criterion. |
| **U-B7** | UX | In-app or store copy asserting that nothing ever leaves the device. | Art. 4 (honest marketing) and Art. 1.3 | **Release**; determined at **copy sign-off**. | The corrected wording used verbatim in store copy, onboarding and the backup flow, plus a Privacy screen showing the live state of both transmission paths. **CGO correction: this must be read against the SECOND correction of 2026-09-10 (which catches the iCloud backup), not the first (which caught only crash reporting). The UX note quotes the superseded version — see §8.5.** | Pre-declared. |

**Two things the UX seat explicitly declines to block on, and records the asymmetry rather than smuggling it in:** Reduce Motion (SC 2.3.3 is **AAA** in WCAG 2.1) and a pasteable, non-memorised recovery key (SC 3.3.8 is AA in WCAG **2.2**, not 2.1). Both are recommendations under the Constitution's stated baseline. **This is the concrete cost of a gap in the Constitution itself** — see §9.2 and the reserved decision at §7.11.

**Count, for the record:** 2 CTO pre-declared blocks · 7 UX would-be release blocks · 1 CFO launch-blocking finding (+1 conditional) · 3 CGO conditions (+2 added by this pack, one of them a conditional block). **Live at this gate: G1, G2, G4, G5. Everything else engages at requirements, build, or release.**

---

# 5. CGO position on gate passage (Constitution 5.6)

## 5.1 The power, stated before I say whether I am using it

5.6 and `roles/cgo.md` give the CGO a block on **gate passage**, for *"constitutional breach, unanswered dissent, or missing compliance evidence."* My charter constrains how I may use it: *"Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it — a block is a checklist item failing, never a feeling of unease."* Only the CEO may overrule, and the overrule is recorded publicly.

## 5.2 I do not block gate passage

There is no constitutional breach to cite against a decision, because nothing has been built. Every red item in my compliance register is a *design* defect in an unbuilt product — a licence screen not specified, a deletion path not drawn, a claim not yet printed where a customer can read it. Blocking a gate for defects that build has not yet had the chance to introduce would be a block on a feeling of unease, which my own charter forbids.

## 5.3 The three conditions from my compliance note, restated and re-scoped

- **Condition 1 (G1) — restated.** My note said *"no UX seat has assessed this"* and made a UX commission the condition. **`products/haunt/ux-note.md` was written four minutes before my note and I did not have it.** I record my own artifact as stale rather than let it stand (§8.3). The condition is restated: on any PROCEED, the decision record names UX involvement at **requirements, build and pre-release**, and the seven would-be blocks become acceptance criteria at requirements stage.
- **Condition 2 (G2) — met.** The proposal carries the corrected claim. A residual defect is recorded at §8.4, not as a block.
- **Condition 3 (G3) — unmet, and cheap.** Licence surface and backup deletion into the requirements document on either PROCEED branch.

## 5.4 One block I am adding, which engages only on PROCEED

> **BLOCK (conditional). Constitution 5.3: *"No proposal passes a gate without a Skeptic memo attached… Approving a proposal requires responding to the dissent in writing, not merely outvoting it."***
>
> The dissent memo is attached and unedited, so the first limb is satisfied. The second is not. The CVO answered O1, O3, O4 and O7 in writing and in place, marked ⚠, and the Skeptic's O8 and O9 have been substantially discharged. **Six objections have received no written response anywhere in the pack: O2, O5, O6, O10, O11, O12.** Their subject matter is not incidental — it is the cost model, the missing spike, the benchmark under every number, two arithmetic defects and a margin deviation recorded as no deviation.
>
> **This block does not engage on KILL or PARK**, because neither is an approval of the proposal. It engages if you decide PROCEED in either form.
>
> **What lifts it:** a written response to those six, in the proposal or in the decision record, before PROCEED is recorded. Four of the six are one paragraph each. O2 and O6 are the two that cost real work — and they are the two that everything else in the pack is standing on.

## 5.5 One thing I want on the record as *not* being a condition

**I am not requiring qualified human legal review before launch on the MVP as proposed** (Constitution 6.1). I could have; it would have looked cautious and cost the company money for nothing. On the zero-network architecture there is no licence to interpret, no personal data held at scale, and no payment instrument touched. **The trigger is real and it is not pulled here. If the architecture changes to include any places, geocoding or map-data API, it is pulled, and no agent — including me — can un-pull it.** One genuinely arguable trigger is flagged for you rather than resolved: 6.1 lists *"payments"*, and I read it narrowly (Apple is merchant of record; Candour touches no payment instrument). If you read it broadly, a professional review of the App Store commercial terms is required before launch and nobody has priced it (§7.15).

---

# 6. The disagreements on the record

Consolidated so a reader sees where the seats do **not** agree. Two disagreements were raised and accepted; five are open; twelve Skeptic objections sit outside the seat structure entirely, because the Skeptic negotiates nothing and holds no block by design.

## 6.1 Research Analyst vs CVO — the sharing layer · **RESOLVED, in the Analyst's favour**

The idea brief kept the door open to a later sharing layer and asked whether it would be wanted. The Analyst disagreed in writing: *"the sharing layer is the only growth mechanism this product could ever have, so the option will be exercised for company reasons and then justified with user reasons. Article 1.1 judges products by unprompted recommendation, not by engineered referral."* Evidence: zero requests for sharing or ratings in Arc's feature-request thread — **one self-selected thread**, which the Analyst flagged loudly as the weakest evidence in the brief while it was doing real work.

**The CVO accepted it in full, against his own earlier position, and closed the door rather than leaving it ajar** — and expressly did not rest the decision on the single thread. **The Skeptic records this as the dissent institution functioning.** The CGO asks that closure be recorded as a **gate-level commitment**, so reopening it requires a fresh gate and a fresh Skeptic memo (compliance note §3.7).

## 6.2 CTO vs CVO — Android as promise or intention · **RESOLVED, in the CTO's favour**

The idea brief recorded *"Both iOS and Android are in scope of the promise."* The CTO put a disagreement in writing: *"Being in scope of an intention is fine. Being in scope of a promise is not, and the word matters under Article 1.3."*

**Accepted and corrected in the proposal:** Android is an aspiration contingent on a published device-matrix spike, and **it may not be marketed before that spike runs.** The Skeptic verified the underlying evidence verbatim (Awareness API deprecated, *"as early as January 2027"*, *"no direct replacement"*) and calls it the strongest-reasoned section in the pack. **What nobody in this pipeline speaks for: the 48.51% of the UK market being forfeited** — and the discipline of "we will not claim it until it works" has to survive the first month of low sales, which is exactly when it will be tested.

## 6.3 UX vs CTO — three items · **OPEN**

1. **The "this venue isn't listed" path is necessary and not sufficient** (feasibility §2.6). Absence is the benign failure; **duplication is the malignant one.** A user picks "The Eagle" (provider A) in March and "The Eagle" (provider B) in June: the product now believes two places, once each, rather than one place twice — and every downstream feature that gives this product its long-term value, including the rating history that is its sole surviving differentiator, is **silently wrong, with no server, no telemetry and no backfill to repair it.** UX asks that **merge, sticky choice and rename-in-place be MVP scope, not polish**, plus a fourth hazard nobody had written down: **a dataset refresh must not change a user's 2027 diary in 2029** — referenced venue rows freeze; refreshes touch unreferenced rows only.
2. **The one-week standalone accessibility line** (feasibility §6.1) is *"an audit, not the work."* Accessibility is a constraint on the timeline UI, the picker, the map and the backup flow — four other rows in the same table. UX asks the standalone line be deleted and the effort distributed with per-feature acceptance criteria.
3. **The periodic recovery-code reminder** (feasibility §4.2) should be replaced by an always-visible Backup status row, because a recurring prompt is the pattern UX §1 rules out.

**No CTO response exists.** The feasibility note predates the UX note by a day.

## 6.4 UX vs CFO — the basis for a free tier · **OPEN, and it is a real hole**

The CFO's compliant free-tier design — *"unlimited entries, unlimited history, unlimited editing, unlimited export, forever. Capped automatic venue lookups"* — was justified entirely by cost alignment: *"it caps a metered service Candour pays for per use, not the customer's access to the customer's own words."*

**The architecture then changed and the meter disappeared.** UX: *"Delete the meter and the justification goes with it. The cap would then restrict a feature that costs Candour nothing per use, which means the paywall no longer describes a cost — and 'the paywall sits precisely on the cost' was the entire argument for its compliance."* UX walks every remaining candidate cap and finds only one survivor (automatic capture paid, manual entry free), which itself carries an App Store 5.1.1(ii) trap — a free tier must not request `Always` location for a feature it cannot use.

**The CGO concurs and goes one step further** (compliance note §4.4): on the MVP as proposed **there is no cost-aligned free tier available at all**, because there is no marginal cost to align one to. What remains compliant is narrow and worth stating exactly:

> **Permitted:** a trial limited in *time* or in *future creation*, disclosed before the user writes anything, after which everything already written remains readable, editable and exportable forever, at no charge.
> **Not permitted:** any limit on reading, editing, or exporting entries the user has already created — in any tier, at any price, ever.

**And a finding three seats now hold jointly:** UX concludes Shape C (free + subscription) **cannot be built without a dark pattern** — if a lapse locks the journal it is the history-window cap with a clock on it; if it does not, nothing makes anyone renew. There is no third branch. The CFO independently concluded a subscription is *justifiable under 2.1 and not viable as a business at the price 2.1 permits*.

## 6.5 UX vs CVO — design cannot rescue the writing thesis · **OPEN AND UNANSWERED**

The UX seat's honest answer, stated as a finding rather than a preference: ***"There is no design that makes private writing stick, and I do not believe an Article 4-compliant one exists."*** Every mechanism that reliably drives journalling habit — streaks, badges, reminder notifications on by default, "you haven't written in 5 days", completion meters, loss framing on expiry, a social layer — is named or covered by Article 4's prohibitions. What remains is *"a nice place to write, that never asks you to."*

Two consequences the gate must hold:

- **The rating is the product; the note is a field on it.** So the proposal's honest residual description ("Arc, plus a star rating") has to carry the entire commercial case **on the star rating alone**.
- **Candour will never know whether this worked.** The architecture forbids analytics, rightly. "Does the writing habit survive?" is a question this company has **structurally disabled itself from answering after launch.** It can only be answered before the build, by talking to people, and it has not been.

**The UX seat says explicitly: "the gate should not be left believing that a UX pass will rescue the writing thesis. It will not."** The proposal lists the UX note as an attachment and **responds to none of its findings**. That is recorded as a pack deficiency at §8.2, not as a block.

## 6.6 CGO's four disagreements · **OPEN (three), one now under challenge**

Stated once each in `compliance-note.md` §8.6. None changes a decision; all change a document.

1. **With the CTO.** `feasibility-note.md` §2.2 records Overture Places under CDLA-Permissive-2.0 as *"Attribution required."* **CDLA-Permissive-2.0 contains no attribution clause at all** — the requirement that existed in 1.0 was deliberately removed. The real obligation is §2.1 (**the licence text must travel with the shipped data**), and the real *attribution* obligation comes from the **Apache-2.0** Foursquare-contributed portion, which the note does not carry through to any design requirement. The pack is wrong in both directions and the errors happen to cancel into roughly the right behaviour — *"but a compliance register that records the wrong obligation will, at some later point, be used to justify the wrong design."*
2. **With the CVO.** The first corrected claim still asserted *"The app makes no network calls of its own"* while the architecture uploads to CloudKit. **Corrected in the proposal on the same day** by the second ⚠ block. Substantially resolved; residual at §8.4.
3. **With the CFO.** The £83/year fixed running cost **omits the ICO annual charge**, which follows from Candour being a controller of support and TestFlight data. Small, real, and on a document Article 3 makes public. **I could not retrieve the tier amount** (ICO returned HTTP 403 twice) and I will not quote a figure from memory.
4. **With the Research Analyst.** `haunt-brief.md` §7.3 attributes an Apple caching quotation to forum thread 114220. **I fetched that thread and the passage is not in it.** Under the evidence standard this is the offence the standard treats most seriously, and I recorded it even though it changes nothing — *"because a standard enforced only when the conclusion is wrong is not a standard."* **This is now carried on the brief itself as a CVO-added ⚠ challenge dated 2026-09-10, with the Analyst's text unaltered.** See §10.3.

## 6.7 The Skeptic against the proposal — twelve objections, with status

The memo is published unedited at `proposals/haunt/dissent-memo.md`. **Nothing in this pack rewrites it, and no seat may.** Status column is mine.

| # | Tier | Objection, in one line | Status at this gate |
|---|---|---|---|
| **O1** | **FATAL to PROCEED** | The pricing table pairs Overture prices with Mapbox volumes; the single proceed-criterion is ~40% below the break-even it claims to represent. | **Answered and corrected in place.** Table → ~2,370 / ~1,170 / ~2,370; threshold restated at **~2,700**, at the top of the honest range. |
| **O2** | SERIOUS | The cost model predates the feasibility note, contradicts it on the largest line (+33–58%), and was never re-derived. | **Not answered.** Acknowledged in the proposal's prose; **the cost sheet's own tables still run on 450 hours throughout.** → **G4.** |
| **O3** | SERIOUS | Article 8 was requested as a live option and disposed of by omission. | **Answered.** Restored at full strength (§3.3) and disposed of on demand grounds by both CVO and Skeptic. |
| **O4** | SERIOUS | *"No network calls of any kind"* is not literally true, and the pack already told us what happens to narrow-true privacy claims. | **Answered twice.** Dissolving condition is a build-stage copy commitment, carried by U-B7 and CGO §6. Residual at §8.4. |
| **O5** | SERIOUS | The venue-index evidence proves size, not correctness — and the spike that would prove correctness moved from *before the gate* to *before any build*, **without a written reason**. Overture's confidence score *"does not address duplicates or property completeness"*, and the filter used is `confidence ≥ 0.5`. | **Not answered. Spike not run.** UX independently asks it be re-specified to four metrics. → **G4.** |
| **O6** | SERIOUS | The labour benchmark anchoring every published number is a single secondary source, flagged twice, never upgraded. | **Not answered, not fixed.** Now flagged three times. → **G4, G5.** |
| **O7** | SERIOUS | The CGO had no part in a gate the Constitution makes it responsible for; no UX seat had looked at this at all. | **Discharged.** This pack is the 5.5 step; `ux-note.md` exists. Residual → **G1**. |
| **O8** | SERIOUS | The ceiling argument is weaker than presented; kill criterion 3 should not carry a tick. | **Partly.** Downgraded in prose to *"directional, not measured"*; **the ✅ remains on the criterion.** This pack records criterion 3 as **UNPROVEN** (§1, §9.3). |
| **O9** | FRICTION | Two of five artifacts still carried the superseded 2026-10-28 deadline. | **Fixed on disk.** Both `cost-sheet.md` and `feasibility-note.md` now carry dated corrections. Recorded at §11. |
| **O10** | FRICTION | The cost sheet's own §5 sensitivity note does not reproduce (£26 stated; £16.00 on its own method at 5,000 buyers). Errs *against* the product, so harmless to the decision — recorded because it is *"the same transposition family"* from the same seat, and **"nobody in this pipeline re-derives another seat's arithmetic."** | **Not answered; still uncorrected on disk.** → **G4.** |
| **O11** | FRICTION | Support labour is modelled on two incompatible bases — CFO £1.23/paying user/yr, CTO a fixed ~2 h/week (≈£3,402/yr) — and the discrepancy runs the same direction as O2: **the pack understates cost exactly where the decision is closest.** | **Not answered.** → **G4.** |
| **O12** | FRICTION | 16.5% is *below* the ~20% target, not "inside" it. The CFO justifies it well; Constitution 2.1 makes that a **justified deviation**, and the cost sheet records *"Deviation from target: none proposed"* while carrying it. | **Not answered; both cost sheet and proposal still say "inside".** → **G4**, and it is CEO decision §7.13. |

**And the Skeptic's two observations about the pack's own gravity**, which a cold reader should have: the proposal states its conclusion in the first screen and its arithmetic on the fourth, *"which invites the reader to check the arithmetic less carefully — and given O1, that is not hypothetical"*; and the kill criteria are presented as a ✅ checklist with all five pre-ticked, one of them against a metric its own author disclaimed. Neither is misconduct; both are the ordinary gravity of a pack written by a seat that has reached a conclusion.

**The Skeptic's steering report:** *"None."* The invocation was the gate slug, the file list, its charter and a process instruction — no summary, no opinion, no expected conclusion. Recorded as a clean invocation.

## 6.8 Where the seats agree, which is also information

Every seat that looked at it — CTO, CFO, CGO, UX, Skeptic — independently concluded that **the offline architecture is the right one**, on separate grounds: licence (CTO, CGO), cost (CFO), honesty of the claim (CVO, CGO), Article 7.2 deliverability (CGO), and works-in-a-basement (CTO). And **three seats reached the free-tier read-cap prohibition independently** before anyone designed anything. That is the cheapest possible moment for those findings, and it is worth noticing that the process produced them.

---

# 7. Decisions reserved to the CEO that this pack surfaces (Constitution 5.4)

5.4: *"The following are never automated: kill/proceed decisions, spending real money, pricing changes, anything affecting user data policy, and release to real users. Agents prepare; the founder decides."* Seventeen items below. Some are due today; most are due only on a PROCEED branch; **three are due today regardless of what you decide about Haunt, because they will recur on every cost sheet this company ever publishes.**

*Item numbers are stable identifiers, not an order of business — they are grouped below by **when each falls due**, so the sequence jumps.*

**Due today, whatever you decide:**

**7.1 — The gate decision itself.** KILL / PROCEED / PROCEED UNDER ARTICLE 8 DESIGNATION / PARK. 5.2 and 5.4. Due **2026-10-07**. A PARK requires a written reason **and** a revisit date. A PROCEED requires a written response to the dissent (5.3) — see G4.

**7.13 — The three standing definitional decisions.** These are not Haunt questions. They are Article 9 / Article 11 territory, because they change what the published number *means*, and the CFO asked that they be settled *"now, while no live price depends on the answer."*

  - **(a) How build labour is costed** — capital amortised over a **published** supported life (this pack's treatment, at 3 years) or year-one operating cost. The CFO sides with amortisation and attaches three conditions that make it honest rather than convenient: **the amortisation period must equal a published support commitment**; unamortised build must be written off publicly on discontinuation (Art. 7.2's closing cost sheet); and **the period, once published, may not be lengthened** — lengthening it lowers published cost, which under 2.3.3.1 ratchets the price down permanently, "a one-way move that looks generous and is actually a way of hiding an overrun." **Adopt the three conditions together or reject the treatment entirely.** If adopted, it changes the meaning of the defined term **"Cost"** and therefore needs a **public amendment under Article 11**, not a footnote.
  - **(b) Whether the labour benchmark is salary or full employment cost.** £56,914 is a *salary*. A real employer also pays employer's NI and pension, roughly **+15–18%** [K, CFO, not retrieved]. Constitution 2.2 names "the median UK software developer salary" as the default, so the bare salary was used. **Moves every number Candour publishes by 15–18%.**
  - **(c) Whether store commission earns margin or is passed through at cost.** Passed through here, giving a **16.5%** effective margin; taking 20% on the commission too gives 20.0% and a **~4% higher price**. The CFO recommends pass-through *"because charging the customer a margin on Apple's fee is not something I could defend to a sceptical reader"* — and I agree with that reasoning. **But the Skeptic is right that 16.5% is a justified deviation *below* the ~20% target, not compliance with it, and Constitution 2.1 requires deviations to be justified in writing on the cost sheet.** The cost sheet currently records *"Deviation from target: none proposed"* while carrying one. Whichever way you decide, the label has to change.

**7.14 — The salvage.** The measured UK venue index (346,184 venues, Overture release `2026-08-19.0`) is a genuine reusable asset and the CVO asks it survive a kill. **Publishing it is itself "sharing Data" under CDLA-Permissive-2.0 §2.1 and a redistribution under Apache-2.0 §4**, so the licence texts, the Foursquare NOTICE and a modification notice must travel with it. The salvage is legal and I support it; it is not obligation-free.

**Due only on a PROCEED branch:**

**7.2 — Article 8 designation** (Option C). **Permanent and irreversible.** Zero distribution forever; never saleable; transferable only to an asset-locked body. Article 8 reserves designation to the CEO in a published decision record.

**7.3 — If designated: the open-source and self-hostable decision.** Article 8: *"encouraged wherever possible, **decided per initiative at its gate and recorded with reasons**."* It is a decision, not a default, and it falls due the same day designation does. The CTO also flags the related choice of whether an ODbL-licensed derived index is *desirable* rather than merely permitted.

**7.4 — Authorising the UK landing-page test.** Spending real money (5.4). Calibrated at **~2,700 buyers**. The CVO calls it *"the only pre-build spend I would authorise."* **G5 applies:** the threshold is a function of the labour benchmark, so the benchmark must be upgraded or the threshold stated as a range before the test is calibrated — otherwise you will be measuring against a number nobody has confirmed.

**7.5 — Authorising the two CTO spikes.** The 2-day Overture top-three-candidate spike (re-specified to four metrics per UX) and a measured battery cost for `startMonitoringVisits` over a real week. The Skeptic notes the first was *already scoped and already promised for this moment*.

**7.6 — Pricing shape and price.** A 5.4 decision and **not available today.** The cost model must be re-derived first (O2, O11, ICO line, O10). For orientation only, at 5,000 users on the offline index: one-off **£14.63** (CFO hours) or **£16.31–£17.56** (CTO hours); lifetime unlock **£29.59** at 9:1; subscription **£3.21–£4.88/yr**, which the CFO calls justifiable and not a business, and which UX says cannot be built without a dark pattern.

**7.7 — iOS-only at MVP, or both platforms.** Roughly **doubles** the break-even volume (iOS-only 3-yr benchmarked labour £24,532; both platforms £44,157) and forfeits ~48.5% of the UK market either way you look at it. Both the CTO and CFO recommend iOS-only. **The CTO is explicit that this is the CEO's price to pay, not his.**

**7.8 — Whether a free tier exists at all.** It roughly **triples** the honest unlock price at realistic conversion (£46.22 at 19:1 vs £14.63 straight purchase), and on the offline architecture **the only compliant basis for one has disappeared** (§6.4). Three seats hold a block on the tempting version.

**7.9 — The App Privacy label: declare Crash Data, or take "Data Not Collected".** A **user-data-policy decision under 5.4.** Apple's rules would arguably let Haunt declare Data Not Collected, which would be visibly stronger than Arc (whose own declaration lists Crash **and** Performance Data). **The CGO recommends declaring anyway**, because *"over-declaring costs one line in a label; under-declaring means the label says 'Data Not Collected' while the marketing copy truthfully tells the user Apple receives crash diagnostics"* — and a sceptical reader who notices will conclude Candour took the flattering option. The CVO endorses this. **It costs a differentiator and buys a label that agrees with the sentence.**

**7.10 — Whether Candour receives crash reports at all.** The alternative honest disposition: decline the Xcode Organizer entirely and rely solely on the user-initiated diagnostic export, making "Data Not Collected" unarguable. The CTO gives a real reason not to (Jetsam events matter for a background-location app and are exactly the gap Layer 3 exists to cover), so the CGO does not recommend it — **but it is a user-data-policy decision and should be made deliberately rather than inherited from the CTO's diagnosis design.**

**7.11 — Move the accessibility baseline from WCAG 2.1 AA to 2.2 AA.** An **Article 11 amendment**, and a **strengthening** one under 11.2, so it is not a weakening amendment. Requested by the UX seat, put to you by the CGO as the charter requires. **The concrete cost of not doing it:** WCAG 2.1 AA contains **no touch-target criterion** (2.5.5 is AAA; 2.5.8 arrives at AA only in 2.2) and **no accessible-authentication criterion** (3.3.8 is AA only in 2.2). So under the Constitution as written, a Candour product could conform to the letter of Article 4 with targets too small for a shaky hand, and the UX seat **cannot block** a recovery-key field that refuses paste — on the highest-stakes, permanently-unrecoverable screen in the product. This is not a Haunt request: it is cheaper to fix in the Constitution once than to argue at every gate.

**7.12 — EU storefront disposition.** The European Accessibility Act is not UK law and bites only if Haunt is sold into EU storefronts; the **microenterprise services exemption** is available (fewer than 10 persons, ≤ €2m), but the products/services boundary for an app is not something an agent can resolve. **Two cheap dispositions, and the CGO asks you pick one at the gate rather than discover it at submission:** restrict storefront availability to the UK at launch, or accept the residual and rely on the exemption.

**7.15 — The reading of Constitution 6.1's "payments" trigger.** Narrow (handling payment instruments — which Candour does not, since Apple Distribution International is merchant of record) or broad (any product that charges money). **The CGO reads it narrowly and says so, while refusing to quietly adopt the reading that creates less work for that seat.** If you read it broadly, a professional review of the App Store commercial terms is required before launch and **nobody has priced it.**

**7.16 — Release to real users.** 5.4, at the far end of the build branch. Recorded here only so the chain is visible.

**7.17 — Any overrule of any block in §4.** 5.6: only the CEO may overrule, and **every overrule is recorded, with reasons, in the public decision record.**

**And one item that is not a 5.4 decision but is owed in writing:** the Skeptic's 2026-09-01 finding that the binding constraint on this company is **reach, not ideas**. It asked that no further candidate be assessed until it was written down; it has not been; Haunt is what that costs. 5.3 requires dissent to be answered in writing, and the practical effect of leaving this one unanswered is that **the company pays for this discovery again on the next candidate.**

---

# 8. Where this pack is deficient (CGO)

My charter says a block is a checklist item failing, not a feeling of unease. The same discipline applies to criticism: each item below names the artifact, the defect, and who owns the fix.

**8.1 — The proposal's own count of its corrections is off, and the count matters because it is how a reader audits the pack.** The preamble says *"five correction blocks."* On disk there are **five ⚠-headed blocks** carrying **six distinct corrections**: the volume-table block contains both the transposition fix (~1,480 → ~2,370) **and** a second, separately-substantive correction absorbing the CTO's build hours (£16.31–£17.56, ~2,550–2,660). Counting blocks gives five; counting corrections gives six. *Owner: CVO — say which is being counted.*

**8.2 — The proposal does not respond to the UX note.** It lists `ux-note.md` as an attachment with *"seven would-be release blocks specified with lifting conditions"* and **responds to none of its findings** — including the finding that goes to the heart of the recommendation (design cannot make private writing stick without breaking Article 4, so the case rests on the star rating alone) and the finding that two of the three modelled pricing shapes are not cleanly buildable on the chosen architecture. The UX note is not the dissent memo, so 5.3 is not engaged; the charter norm that *"disagreement is a deliverable"* is. *Owner: CVO.*

**8.3 — My own compliance note is stale, and I record it rather than let it stand.** `compliance-note.md` §5 and register entry **C22** say *"No UX assessment exists"* and make a UX commission the condition of my non-block. `products/haunt/ux-note.md` was written **four minutes earlier** and I did not have it. The substance of the condition survives — UX involvement at requirements, build and pre-release — but its stated form is wrong. Restated at **G1**. *Owner: CGO (me). Fix: amend §5.3 and C22 of the compliance note when it is next updated; the register is meant to be updated at every phase end, not rewritten.*

**8.4 — The claim sentence has been corrected twice and the product-description headline still hedges.** The proposal's opening line reads *"**No network calls in normal operation**"* with a pointer to the corrected wording below. A user-enabled backup running inside the app **is** normal operation. The substantiable claim exists, is drafted, and appears later in the same document; the headline should simply be it. *This is the fourth iteration of the same pattern in one pack — claim stated absolutely, exception found, claim narrowed, narrowed claim has its own exception.* As the CGO wrote in the compliance note: **the fix is not another edit — it is to write the claim from the architecture rather than from the marketing instinct, once, and then hold it.** *Owner: CVO.*

**8.5 — The UX note's B7 lifting condition points at superseded wording.** It quotes *"The app makes no network calls of its own"* as "the corrected wording of 2026-09-10". That was the **first** correction; the **second** correction, later the same day, catches the iCloud backup that the first one missed. **B7 must be read against the second version**, or the block's own lifting condition would license the claim it exists to prevent. *Owner: UX, at requirements stage.*

**8.6 — The UX note's internal count and one citation.** §9 hands off *"the six B-items in §7"*; §7 lists **seven** (B1–B7). And §4.3 attributes the CFO's support model as *"2% contact rate/yr × 30 min"* — that is the CFO's **free-tier** line; the **paying-user** line is 5% × 45 min (£1.23/user/yr). The UX point stands unaffected (a key-loss contact is not the average contact and should be modelled separately), but the citation is to the wrong row. *Owner: UX.*

**8.7 — Kill criterion 3 still carries a ✅.** The proposal downgrades it in prose to *"directional, not measured"* and says the Skeptic was right to flag it. **The tick remains, in the section a busy reader reads first.** The Skeptic asked that it *"be recorded as unproven rather than ticked, so that if the CEO ever revisits Haunt he is not revisiting a fact that was never established."* **This pack records it as UNPROVEN.** *Owner: CVO.*

**8.8 — The cost sheet is not currently publishable, and Article 3 would make it public.** Four defects compound: the build hours (O2), the two support bases (O11), the missing ICO charge, and the §5 sensitivity arithmetic (O10) — plus the "no deviation" label (O12). Every one of them runs in the direction that **flatters** the product except O10. *Owner: CFO. Nothing in this pack should be read as a price until this is redone.*

**8.9 — The pre-gate spike was relocated without a written reason.** The CTO's own open-questions table set it as *"Engineer, 2-day spike **before the gate**"*; the research brief independently called a UK coverage measurement *"the single highest-value missing fact in the brief."* The proposal moved it to *"before any build."* Moot on a kill; on a proceed it is the difference between a shippable product and one whose most visible failure — *"this app doesn't know where I am"* — is unmeasured. *Owner: CVO to state the reason, or Engineer to run it.*

**8.10 — The gate reading list omitted two load-bearing documents.** `research/scouts/scout-2026-09-01-skeptic-cull.md` and `research/scouts/scout-2026-09-01.md` are cited inside the pack as load-bearing — the cost sheet's labour-treatment argument (CEO decision 7.13a) is a reply to them, and the research brief's §9 pricing cross-check builds on the cull memo §4 — and a reader given only the listed files can audit neither. The Skeptic retrieved both and reports they say what the pack says they say. **They are added to the reading list at §13.** *Owner: CGO — fixed here.*

**8.11 — The most load-bearing fact in the pack has never been checked against the product itself.** Everything known about Arc is vendor-origin. **£4.99 buys a month of it.** *Owner: whoever the CEO asks. It would settle kill criterion 1 and close the last single-origin gap in the same purchase.*

---

# 9. Constitution and compliance status (CGO)

## 9.1 Article by article

| Article | Status | Basis |
|---|---|---|
| **1.1 Genuinely helpful** | **Fails, on the CVO's own reading.** The test is unprompted recommendation; the audience is small, already served, and mostly served for free. **The counter-reading is at §3.3** and it is the strongest argument for Article 8 designation. | Proposal; research brief §§2–4, 8–9 |
| **1.2 No exploitation** | Met by design, and defended in advance: three seats hold a block on the read-cap that would breach it. | Cost sheet §8.2; compliance §4.4; UX §7 B2 |
| **1.3 Honest by default** | **Met better by this architecture than by the sparked one, and repeatedly mis-stated in the copy.** Two corrections, one residual hedge (§8.4). | Proposal ⚠ blocks; compliance §6 |
| **1.5 / 2.1 Cheap to run** | **Met structurally, not by discipline** — £83/year fixed, £0/user, no hosting line, no database line. **Subject to the missing ICO charge.** | Cost sheet §4.1; compliance §3.3 |
| **2.1 Pricing** | No price set — reserved to the CEO. Effective margin 16.5%, which is a **justified deviation below** the ~20% target, currently labelled "none proposed". Hard cap of 30% not approached. | Cost sheet §5, §12; dissent O12 |
| **2.2 Extraction rule** | Not engaged — no compensation drawn, no distribution contemplated. Related-party disclosures: **none**. | Cost sheet §11 |
| **2.3 Waterfall** | **Relevant and adverse:** none of the four models generates a reserve at plausible volumes, and 2.3 puts reserve top-up first. At 1,000–5,000 users Haunt does not clear its own benchmarked labour. | Cost sheet §12; proposal |
| **3 Transparency** | Decision record due within 30 days whatever you decide. Cost sheet publishable **only after re-derivation** (§8.8). | Art. 3; §8.8 |
| **4 Product ethics** | **Data collection near-nil by construction; export designed and exceeded (import at MVP).** Live hazards: any free-tier cap on already-written entries (three blocks); **no backup-deletion path designed** (C15); accessibility unbuilt and now assessed at concept level; marketing claim corrected twice. | Compliance §§3.5, 4.4, 5; UX §7 |
| **5.1 Pipeline** | Followed. Every stage produced a written artifact. | §2 |
| **5.2 Anti-drift** | **On time.** Deadline **2026-10-07**, moved 21 days *earlier* against the pipeline's own convenience. 27 days remain. §11. | §11 |
| **5.3 Mandatory dissent** | **Memo attached and published unedited. Six objections unanswered in writing** → conditional block G4 on the PROCEED branches only. | §5.4, §6.7 |
| **5.4 Human decision points** | Seventeen items surfaced and reserved. **No agent in this pack recommends a decision to you except the CVO, who is entitled to and who asks you to discount his.** | §7 |
| **5.5 Reviews** | **This document is that step.** Demo: §12 — and there is almost nothing to demonstrate. | §12 |
| **5.6 Blocks** | Two CTO, seven UX, one CFO (+1 conditional), three CGO conditions plus one conditional CGO block. **Consolidated at §4.** | §4 |
| **6.1 Limits of agent authority** | **Qualified human legal review: NOT required on the MVP as proposed** — no licence to interpret, no personal data at scale, no payment instrument. **Unavoidably required on any architecture touching a places API.** One arguable trigger left to the CEO (§7.15). | Compliance §1.5, §8.2 |
| **7.2 Discontinuation** | **Deliverable in full on this architecture, with no embarrassing carve-out** — CDLA and Apache impose notice conditions, not publication bars. On a Google Places architecture it could not be: a journal of opaque `place_id` strings is neither open-sourceable as a working product nor exportable in a form that survives shutdown. | Compliance §2.6 |
| **8 Non-profit initiatives** | **A live option, restored at §3.3.** No licence conflict either way. If designated, the open-source decision falls due the same day (§7.3). | §3.3; compliance §2.6 |
| **9 / 11 Gaming and amendments** | Two items are Article 11 territory: the labour-treatment definition (7.13a) and the WCAG baseline (7.11, strengthening). | §7 |
| **10 Honesty of this document** | Observed: every seat states what it could not close, and this pack states where it is deficient (§8). | §8 |

## 9.2 Two gaps in the Constitution itself, surfaced by this product

1. **The accessibility baseline is short of what Article 4 evidently intends.** WCAG 2.1 AA carries **no touch-target minimum** and **no accessible-authentication criterion**; both arrive at AA in 2.2. The live cost here is concrete: the UX seat can recommend but **cannot block** a recovery-key field that refuses paste, on the one screen in this product where a mistake is permanently unrecoverable by design. → **7.11**, a strengthening Article 11 amendment.
2. **"Meet WCAG 2.1 AA" is not a self-executing instruction for a native iOS app.** WCAG is a standard for **web content**; the bridge is **WCAG2ICT**, which W3C itself says *"necessitates some interpretation."* If nobody writes down what it means here, it gets discharged by whatever the engineer happened to do, and *"verify WCAG 2.1 AA"* is not a testable acceptance criterion. **Operative target to record: WCAG 2.1 AA as interpreted by WCAG2ICT for non-web software, implemented through Apple's accessibility APIs.** One line in the requirements document; it makes QA's job possible.

## 9.3 The finding this gate should be proudest of, and the one it should be least comfortable with

**Proudest.** UK law would permit a clearly-signposted free tier that shows only the last 30 days of a user's own journal. **Candour's constitution forbids it.** As the compliance note puts it: *"'we didn't do the legal thing because our own rules forbid it' is the most valuable sentence a governance document can produce, and it is worth nothing if it is not written down when it happens."* **I ask that it go in the decision record explicitly**, whichever way you decide.

**Least comfortable.** Kill criterion 3 is **recorded here as UNPROVEN**, not ticked. It rests on converting 164 GB App Store ratings into a user base with a multiplier the Analyst who produced it disclaimed for exactly this use. **The kill still stands on criteria 1, 2, 4 and 5**, all of which the Skeptic verified and none of which depend on that arithmetic. But a pack that ticks a contested inference as a settled fact, in the section a busy reader reads first, is a pack that will be misremembered.

---

# 10. Evidence health of this pack

## 10.1 The Skeptic's verification result

Per `pipeline/evidence-standard.md`, the Skeptic verifies at gates. Its report, from `dissent-memo.md`:

- **Population:** ~32 tagged `[E]` citations in the research brief, ~35 links in the feasibility note's evidence register, ~20 in the cost sheet, with overlap.
- **Attempted: 16 retrievals**, all performed on 2026-09-10, selected as **every citation judged load-bearing to the kill recommendation or to an objection in the memo (13), plus 3 chosen to test the pack's weakest self-flagged claims.**
- **Checked and confirmed: 14.** Results ranged from "exact, verbatim" (Arc's App Store copy and price card; Google's Timeline announcement; Google's caching and place-ID clauses; the Awareness API deprecation; Apple's Small Business Program; Google Places pricing; StatCounter) to two **findings the pack had missed**: Overture's confidence score *"does not address duplicates or property completeness"* (which O5 and the UX note both turn on), and Arc's App Privacy declaration listing Diagnostics as collected (which the pack then used correctly).
- **Blocked by tooling: 2, flagged rather than assumed good.**
  - **#15 — Google Maps Platform Terms §3.2.3(a)(iii), (b), (d), (e).** Retrieval truncated. The *substance* is confirmed independently at #4 on Google's own developer policies, but the **(d) "No Re-Creating Google Products"** clause — which both the Analyst and the CTO flag as the sharpest legal exposure — is **unverified**. Moot on the recommended architecture; load-bearing the moment any online route returns. **The CGO hit the identical failure** (two truncated fetches). **Three seats have now quoted these clauses and two of us could not retrieve them directly.**
  - **#16 — all Apple developer documentation cited by the CTO** (`startMonitoringVisits()`, `CLVisit`, `requestAlwaysAuthorization()`, Energy Efficiency Guide, MetricKit, crash-report guidance). Not retrievable — Apple's docs render client-side. Recorded as **unverified by the Skeptic, not as unsound**. **The UX seat independently hit the same wall.** *"A seat with an Apple developer account should confirm the two quotes the recommendation actually rests on — relaunch-after-termination, and the energy-ladder ranking — before any build."*
- **Arithmetic re-derivation:** the Skeptic re-derived the pricing arithmetic from the cost sheet's own stated formulae rather than accepting any table. **The model reproduces cleanly** (£14.63 recomputes to £14.65); **two independent transposition errors surfaced (O1, O10) and one unreconciled input (O2).** Its conclusion is the uncomfortable one: *"the errors are in which cell was carried forward, not in the model. That is the more worrying kind, because the model is what got reviewed."*

## 10.2 Independence

The pack's independence hygiene is genuinely good — nearly every single-origin claim is flagged by the seat that used it. **The exception is the one that matters most:**

- **Arc — the single most load-bearing fact in the pack (kill criterion 1) — rests entirely on one origin: the vendor.** App Store listing, product page, privacy policy, support forum: all Big Paua. **Nobody installed the app.** The pack's own stated falsifier for this criterion was untested until the Skeptic tested the retrievable half of it.
- **Google Timeline (criterion 2)** is entirely Google-origin. Acceptable — Google is the authority on Google's product — but no one has inspected the app's network traffic, which the brief names as the falsifier and assigns to the CTO. It was not done.
- **Letterboxd (criterion 4)** is one origin. The Skeptic confirmed it via a search index after the page returned 403; **the UX seat's re-retrieval on 2026-09-10 also returned 403.**
- **The UK licensed-premises denominator** the CTO uses to sanity-check coverage is two outlets reporting **one paywalled CGA report**, flagged by the CTO.
- **StatCounter, dontkillmyapp, the retention benchmarks, the hobbyist Overture comparison, the willingness-to-pay survey** (vendor-authored, with a commercial interest in the answer) are each single-source and each flagged.

## 10.3 The challenged citation at `research/haunt-brief.md` §7.3

The brief attributes the Apple caching clause — *"Map Data may not be cached, pre-fetched, or stored by You or Your Application… other than on a temporary and limited basis"* — to Apple Developer Forums threads **114220** and 116695. **The CGO fetched thread 114220 and the passage is not in it**; the only licence text quoted there is the definition of "Apple Maps Service".

**This is now marked on the brief itself, in a ⚠ block added by the CVO on 2026-09-10, with the Analyst's text unaltered.** That is the right handling: *"it is marked here rather than quietly repaired, because quiet repair is how a fabricated citation becomes an established fact."*

**Weight to give it:** the standard treats a citation without a retrieval behind it as its most serious offence. **But none of §7.3 is load-bearing to this gate** — the MVP touches no Apple map API — and the section's **conclusion** (Apple's terms are unresolved and Apple declines to resolve them) is independently corroborated by the CGO's own retrieval of thread 807656, where an Apple DTS engineer declines to interpret the clause and tells the developer to consult a lawyer. **The conclusion survives; the specific quotation does not, until re-retrieved.** *Owner: Research Analyst, to re-retrieve or withdraw. Nothing in this pack cites §7.3's quotations.*

## 10.4 The single-source benchmark under every number

**`£56,914 × hours` is the anchor of every price, every volume and every break-even in this pack**, and Constitution 2.2 makes it the anchor of every number Candour publishes. Its provenance is **one secondary page citing ONS ASHE Table 14**.

Flag history — **three flags, two seats, ten days:**

| Date | Seat | What was said |
|---|---|---|
| 2026-09-01 | Skeptic | *"I did not retrieve the ONS table itself and this figure should be upgraded before anyone relies on it."* |
| 2026-09-09 | CFO | *"It should be upgraded to a primary ONS citation before any cost sheet is published, and I am not going to keep re-flagging it in later documents; it needs fixing once."* |
| 2026-09-10 | Skeptic (O6) | Attempted the upgrade rather than merely re-flagging. **Partial result:** the ASHE dataset exists, the 2025 provisional edition and April 2025 reference period match the secondary source exactly — *"so the citation is real and not fabricated"* — but **the figure itself lives only inside a downloadable spreadsheet the tool could not open. Citation checks out; the number does not, yet.** |

**The standard is unambiguous:** *"A load-bearing [K] claim must be upgraded to [E] or explicitly downgraded before a gate relies on it."* The pack flags the weakness thoroughly, which is disclosure — but it still publishes point figures rather than ranges, which is neither the upgrade nor the explicit downgrade the standard asks for. **On a KILL this is harmless. On either PROCEED branch it is condition G5**, because the landing-page threshold you would be authorising is a function of this number. *"Someone downloads ASHE Table 14 and confirms £56,914, or every price in every Candour cost sheet is restated as a range until they do."*

## 10.5 The CFO / CTO build-estimate mismatch, and how much of it the CVO's correction absorbs

| Source | Build hours | Build cost @ £32.71/h |
|---|---|---|
| **CFO — used throughout the cost sheet** | 450 (≈12 weeks FT) | **£14,719** |
| **CTO §6.1, low** (16 focused weeks) | 600 | **£19,626** |
| **CTO §6.1, high** (19 focused weeks) | 712.5 | **£23,306** |

**+33% to +58% on the largest single line in every model.** The loop is visible inside the pack: the cost sheet's own §13 gap table names the owner (*"Build and maintenance hours are CFO guesses, not engineering estimates | The largest single cost in every model | Owner: CTO feasibility note"*); the CTO answered; **nobody closed it.**

**What the CVO's correction absorbs:** the proposal now states the carried-through consequence in prose — shelf price £16.31–£17.56, break-even ~2,550–2,660, an honest range of **~2,400–2,700**, £14.63 described as *"a floor, not a price"* — and sets the proceed threshold at the **top** of that range, which is the right instinct: *"a falsifier that flatters the idea is not a falsifier."*

**What it does not absorb — and this is the part that matters:**

1. **The cost sheet itself is unrevised.** Every table in §§5, 6, 7, 8 and 10 still runs on 450 hours. The artifact Article 3 would make public is the one that is wrong.
2. **The support bases are still unreconciled (O11).** CFO £1.23/paying user/yr against CTO a fixed ~2 h/week ≈ £3,402/yr. At 5,000 users the CFO's line is higher; **at the 1,000–2,500 volumes that actually decide this, the CFO's line is £1,230–£3,075 against the CTO's £3,402 fixed.** The discrepancy runs the same direction as the build mismatch: **the pack understates cost exactly where the decision is closest.**
3. **The ICO annual charge is still missing** from the £83/year figure, and the amount is still unretrieved.
4. **The §5 sensitivity note still does not reproduce** (O10).
5. **The margin is still labelled "no deviation"** while carrying one (O12).

**Net effect on the number the gate was told to stare at:** the original ~1,480 was **72–80% low**. The corrected ~2,400–2,700 is stated honestly in prose and is **not yet derived by anything.** *"A pack whose stated virtue is that the gate can argue about numbers instead of adjectives must have numbers that survive being added up."*

## 10.6 What the pack itself says it could not close

Recorded together, because "we could not verify X" is a finding, not a failure — and there are twenty-two of them across five artifacts. The ones with teeth: **UK-specific venue coverage** (commissioned, not answered, and the brief calls it the single highest-value missing fact); **Apple's licence text at source**; **Foursquare's caching rules for the core Places API** (the page retrieved is titled for the Personalization APIs, and the CGO flags that the scope inference is its own, not the page's); **how many people use Letterboxd's private diary mode** (the number that would actually settle §4); **any direct evidence of how users read "local storage + venue lookup"**; **journalling-app retention data**; **the ICO tier amount**; **the post-DUAA PECR reg. 6 exemptions**; and **no usability testing of any kind** — no prototype, no participants, no observation, which the UX seat names as the highest-value missing fact in its own note and which is *cheaper than the landing-page test the proposal already contemplates.*

---

# 11. Anti-drift status (Constitution 5.2) — recorded, as the proposal asks

> ## **Kill / proceed / park decision on `haunt` is due 2026-10-07.**
> ## **27 days remain** as of this pack's date, 2026-09-10.

**The date moved 21 days earlier, and here is why.**

| | |
|---|---|
| **Originally recorded** | **2026-10-28**, in `proposals/haunt/idea-brief.md`, computed as four weeks from the research brief's *scheduled due date* of 2026-09-30. |
| **Now recorded** | **2026-10-07** — four weeks from the brief's *delivery*. |
| **The rule** | 5.2: the decision is due *"within 4 weeks **of its research brief**."* The brief exists. On a literal reading the clock runs from the artifact, not from a date in a plan. |
| **Who raised it** | **The Research Analyst**, unprompted, in the brief's own opening note — **against its own interest**, having delivered 21 days early. *"I am not the seat that rules on this, and I raise it rather than assume the more comfortable answer."* |
| **Who accepted it** | The CVO, in the proposal: *"The Research Analyst was right to challenge it. Corrected, 21 days earlier. Delivering early does not buy slack."* |
| **The CGO confirms the earlier date** | 5.2's own words are that the rule exists *"to force building over perpetual planning"*, and **5.2 already forecloses the argument in the other direction**: where a brief is *late*, *"the decision clock starts at its due date regardless."* **A rule that refuses to let lateness extend the clock cannot coherently let earliness extend it.** |

**Two consequences worth stating.**

1. **This is 5.2 binding the people it is meant to bind.** The clock moved *against* the pipeline's convenience, raised by the seat that would have benefited from the looser reading. The Skeptic endorses it for the same reason.
2. **The stale dates are now fixed.** The Skeptic's O9 recorded that `cost-sheet.md` and `feasibility-note.md` still published 2026-10-28. **Both now carry dated corrections (CVO, 2026-09-10), and no figure in either depends on the date.** All five artifacts now agree. **O9 discharged.**

**Clock discipline going forward:** if the decision is PARK, 5.2 requires a written reason **and** a revisit date, and the reason must name what will have changed by that date. A park does not reset this clock; it schedules the next one.

---

# 12. Demo (Constitution 5.5)

5.5 requires a review pack **and a demo**. I have to be plain: **at a discovery gate for an unbuilt product there is almost nothing to demonstrate, and pretending otherwise would be theatre.** There is exactly one demonstrable artifact, and it is worth ten minutes of your time:

- **The measured UK venue index.** Overture Places release `2026-08-19.0`, UK bounding box, extracted via DuckDB: **346,184 food-and-drink venues, 21.3 MB as an indexed SQLite file, 10.8 MB compressed**, CDLA-Permissive-2.0. The CTO **built and weighed it** rather than estimating it. It is the strongest artifact in the pack, it kills the "bundle size" objection outright, and — per the CVO's salvage note — **it is a genuine reusable Candour asset whichever way you decide.** Ask to see the file and the query.
- **What the index cannot yet show you, and this is the demo's honest limitation:** whether the *right* venue is in it and findable. 346,184 is **3.5×** the CTO's own trade cross-check of ~98,914 UK licensed premises and ~4× OSM's comparable total. The CTO reads the large number as reassurance. The Skeptic notes it is *at least as consistent* with the duplicate-and-junk rate Overture warns about — and that the filter used (`named, confidence ≥ 0.5`) is **explicitly the wrong instrument for that risk**, since Overture states the confidence score *"does not address duplicates or property completeness."* **Both readings are available from a count; neither is settled by one.** The 2-day spike settles it. It has not been run.

**Nothing else in this pack has been built, tested, seen by a user, or installed.** That includes the competitor the entire kill recommendation rests on.

---

# 13. Attachments and reading list

Required under 5.3 and 5.5. **All paths absolute.**

**The pack (read in this order):**

1. `/Users/davidparrish/Documents/candour/proposals/haunt/gate-pack.md` — this document
2. `/Users/davidparrish/Documents/candour/proposals/haunt/dissent-memo.md` — **the Skeptic's, published unedited. Read it second, not last.**
3. `/Users/davidparrish/Documents/candour/proposals/haunt/proposal.md` — CVO, recommends KILL; carries the ⚠ correction blocks of 2026-09-10
4. `/Users/davidparrish/Documents/candour/research/haunt-brief.md` — Research Analyst; **§7.3 carries a CVO-added citation challenge**
5. `/Users/davidparrish/Documents/candour/products/haunt/cost-sheet.md` — CFO; **not currently publishable (§8.8)**
6. `/Users/davidparrish/Documents/candour/products/haunt/feasibility-note.md` — CTO; contains the measured artefacts and both pre-declared blocks
7. `/Users/davidparrish/Documents/candour/products/haunt/compliance-note.md` — CGO; **stale on one point, see §8.3**
8. `/Users/davidparrish/Documents/candour/products/haunt/ux-note.md` — UX; seven would-be release blocks
9. `/Users/davidparrish/Documents/candour/proposals/haunt/idea-brief.md` — CVO, the spark and the scope forks closed at it

**Added by the CGO, because the pack cites them as load-bearing and the gate's reading list omitted them (§8.10):**

10. `/Users/davidparrish/Documents/candour/research/scouts/scout-2026-09-01-skeptic-cull.md` — the cost-structure argument the cost sheet §1 replies to, and the basis of the research brief's §9 pricing cross-check. **Also the origin of the unanswered reach finding.**
11. `/Users/davidparrish/Documents/candour/research/scouts/scout-2026-09-01.md`

**The two or three links the decision actually turns on**, which the evidence standard asks the CEO to open personally rather than take from an agent:

- Arc Timeline 4 on the GB App Store — the product this is competing with, its copy and its price card: `https://apps.apple.com/gb/app/arc-timeline-4/id6740688708`
- Google's own Timeline announcement, 12 Dec 2023 — the incumbent conceding the privacy pitch: `https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/`
- Letterboxd's 2024 year in review — the 14% number: `https://letterboxd.com/journal/2024-year-in-review/` *(returned HTTP 403 to two seats; the Skeptic confirmed it via a search index of the same page)*

**Where the decision record goes:** `/Users/davidparrish/Documents/candour/decisions/`, using `/Users/davidparrish/Documents/candour/pipeline/templates/decision-record.md`, **published within 30 days** (Article 3). Its "Written response to the dissent memo" section is not optional on a PROCEED — see G4 — and *"noted" is not a response.*

---

# 14. Recommended next step

**Deliberately blank.**

The CGO enforces process and compiles; it does not recommend a gate outcome, and this pack has been written so that you can reach any of the four with the same information in front of you. The one recommendation I do make is procedural and is stated as a block: **if the decision is PROCEED in either form, six Skeptic objections must be answered in writing first (G4), and the cost model must be re-derived before any threshold calibrated from it is used to authorise anything.**

Kill / proceed / proceed-under-Article-8 / park is yours alone (Constitution 5.4), due **2026-10-07**.

---

*Compiled by the Chief Governance Officer under Constitution 5.5, `roles/cgo.md`, and `pipeline/evidence-standard.md`. No retrieval was performed in compiling this pack; every `[E]` travels from a named artifact and a named seat, on a named date. This pack prepares and flags; it does not certify (Constitution 6.1). The Skeptic's memo is published unedited and nothing here revises it. Honest limitation, restated as the Skeptic restates it: every seat in this pack is the same model, run by the same person. These procedures replicate the structural conditions of independence; they do not create it.*

# Proposal — Haunt

**Date:** 2026-09-09 · **Author:** CVO · **Status:** awaiting gate

> ## ⏱ Anti-drift deadline (Constitution 5.2): kill / proceed / park by **2026-10-07**
>
> The research brief was commissioned and delivered on 2026-09-09. 5.2 counts four weeks "of its research brief," so the clock runs from delivery. The idea brief originally recorded 2026-10-28 — computed from the brief's *due* date — and the Research Analyst was right to challenge it. Corrected, 21 days earlier. Delivering early does not buy slack. **CGO to record the date and the reason.**

> ## CVO recommendation: **KILL** — with four options before the CEO, not three
>
> I sparked the discovery on this and I am recommending against it. Discovery solved the technical problem and confirmed the market problem. The one finding that would overturn it is named in "Success and abandonment criteria" so the gate can test it rather than argue about it.
>
> **Read this document with the Skeptic's memo open** (`dissent-memo.md`, published unedited). It found a real arithmetic error at the centre of my case and a material omission that happened to favour my own recommendation. Both are corrected in place and marked ⚠ — five correction blocks, all dated 2026-09-10, none of them cosmetic. The corrected arithmetic **strengthens** the case for kill; the restored omission **weakens** it. I have not adjusted my recommendation to account for either, and the CEO should discount it accordingly.
>
> **The fourth option is PROCEED UNDER ARTICLE 8 DESIGNATION**, which I wrongly left out of the original pack. It is set out in full in "Success and abandonment criteria" below, with the strongest case for it that I can make — including the part I disagree with.

---

## What we're proposing to build (smallest honest version)

An iOS app that watches for the user stopping somewhere, asks "were you here?", and — on confirmation — records the visit on a private timeline the user can annotate and rate. **Your timeline, notes and ratings never leave your device unless you switch on backup; if you do, an encrypted copy goes to your own iCloud under a passphrase we never see. The app makes no other network calls.** Venue names come from a bundled offline index derived from Overture Places; anything missing is typed by hand. *(Third and final correction of this sentence, 2026-09-10 — the CGO recorded the previous hedge, "no network calls in normal operation", as a residual defect at gate-pack §8.4, because the same analysis that defeated the first two wordings defeats a hedge. CRA 2015 s.36 makes App Store description copy a term of the contract, not marketing.)* Storage is a local SQLite file; export is a documented JSON+CSV zip; backup is optional, encrypted under a user-held passphrase, to the user's own iCloud, with Candour holding no key.

That shape is not what was sparked, and the change is the most useful thing discovery produced. The spark assumed an online venue lookup with a disclosed privacy caveat, and treated a fully-offline build as an expensive fallback. **Both halves of that assumption were wrong**, and they were corrected by measurement rather than argument:

- The online route is **not legally available** for this product. Google's terms permit permanent storage of a `place_id` and nothing else; venue names are Google Maps Content and may not be cached [E, CTO §2.1 / research §7.1]. A journal that still shows "The Eagle, Cambridge" in 2031 must re-query on every render, which breaks offline reading and makes the bill scale with *reading* the diary. Foursquare's paid API has the same shape. Apple's clause is ambiguous enough that an Apple engineer on Apple's own forum declined to interpret it and suggested asking a lawyer [E, research §7.3].
- The offline route is **small, free and permissively licensed**. The CTO built it rather than estimating it: Overture Places 2026-08-19.0, UK bounding box, via DuckDB → **346,184 food-and-drink venues, 21.3 MB as an indexed SQLite file, 10.8 MB compressed**, CDLA-Permissive-2.0 [E, measured this session]. Build effort is roughly neutral against the online variant, because it deletes as much work as it adds — no API keys, no network error states, no cache eviction, no rate limiting, no privacy-boundary explainer to design.

So the "honesty problem" the idea brief said had to be solved first **substantially dissolved — but not completely, and I overstated it.**

> **⚠ Correction, 2026-09-10 — CVO overstatement, caught by the Skeptic at gate.** This paragraph originally read "nothing leaves the device, with no caveat." That is not literally true. The architecture still includes platform-mediated, opt-in crash reporting (§ "What we are explicitly NOT building"), which is a transmission — user-authorised, routed to Apple rather than Candour, and carrying no journal content, but a transmission. Having spent a section congratulating the architecture for retiring a narrow-true claim, I then wrote a narrow-true claim of my own. **The substantiable version is: "Your timeline, notes and ratings never leave your device. The app makes no network calls of its own. If you opt in to Apple's crash reporting, Apple receives crash diagnostics — never your journal."** That is still a stronger claim than any competitor makes, and Article 4 requires it be the one we make.

> **⚠ Second correction to the same sentence, 2026-09-10 — caught by the CGO, hours after the first.** The wording immediately above is **also wrong.** It catches crash reporting and misses the larger exception sitting in our own architecture: **the opt-in encrypted iCloud backup is a network call the app makes.** "The app makes no network calls of its own" is false the moment a user turns backup on. The substantiable claim is:
>
> > *"Your timeline, notes and ratings never leave your device unless you switch on backup. If you do, an encrypted copy goes to your own iCloud — encrypted with your passphrase, which we never see. The app makes no other network calls. If you opt in to Apple's crash reporting, Apple receives crash diagnostics — never your journal."*
>
> **That I got this wrong twice, in a pack whose central boast is honest claims, is the finding — not the wording.** Both errors ran the same direction: toward a cleaner sentence than the architecture supports. The CGO further recommends Candour **declare crash data on the App Privacy label** even though Apple's rules arguably exempt it, because it costs a differentiator and buys a label that agrees with the sentence. I endorse that. It also works in a basement bar, on the Tube, and in aeroplane mode — which is where a night out actually happens.

**iOS only.** Android does not ship at MVP, and not because Android is hard: the specific thing this product needs — the OS saying "the user has been sitting somewhere a while" — has no supported first-party equivalent. iOS has `startMonitoringVisits()`, current and able to relaunch a terminated app. Android's nearest equivalent, the Awareness Fence API, is deprecated with shutdown "as early as January 2027" and no direct replacement; geofences are pre-registered and capped at 100, which solves the opposite problem, since Haunt must notice venues it does not yet know about [E, CTO §1]. That forfeits roughly half the UK market (51.5% iOS / 48.5% Android) and the gate should see that cost plainly.

## Who it serves and the problem evidence

*(Full detail: [`research/haunt-brief.md`](../../research/haunt-brief.md).)*

**The product exists.** Arc Timeline 4 (Big Paua, iOS) shipped on 12 April 2026. Its own App Store copy: *"All data stored on your device. Optional iCloud backup to your private iCloud account. No accounts, no sign-ups, no data shared with third parties. Export your data anytime in standard JSON format"* [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708]. Automatic visit and place detection, a places tab with visit history, notes on timeline items. £4.99/mo · £44.99/yr · £179.99 lifetime. **The gaps the analyst could find were venue ratings and Android.** Haunt's honest remaining description is "Arc, plus a star rating, on Android" — and this proposal has just dropped Android.

**The free incumbent conceded the privacy pitch two and a half years ago.** Google's own announcement of 12 Dec 2023: *"soon your Timeline will be saved right on your device"*, with optional backup *"encrypt[ed] so no one can read it, including Google"* [E — https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/]. Google Maps also ships private lists with **4,000-character notes per place**, free, on both platforms [E]. The notes layer I had identified as the surviving residual is largely conceded too.

**The differentiating behaviour is the minority behaviour.** Letterboxd's own 2024 figures: 701m films logged, ~500m ratings, 96.4m reviews [E]. **14% of logs carry writing — with an audience.** Haunt removes the audience and sells the writing.

**The market ceiling is low.** The category leader, on the easier platform, after ~10 years, with the strongest possible privacy story, has **425 US and 164 GB App Store ratings** [E]. Swarm — free, corporate-backed — has 417 GB ratings. The analyst declined to convert these into a market size and said so; the ceiling argument stands without the conversion.

**What pushes the other way, and I will not bury it:** Google's Timeline migration destroyed real users' history and Google would not say how many were affected [E] — there is a documented trust injury to trade on. Timeline is opt-in, off by default, and defaults to deleting after three months, so most people hold no long archive. The paid incumbent is one person shipping sporadically. And **no competitor has solved the venue-name licence problem cleanly** — Arc's own App Privacy declaration lists crash and performance data as collected [E], so even the strictest local-first incumbent in this category does not maintain the purity a zero-network Haunt would.

That last point is the single honest differentiator that survived discovery: **not "local-first" — which is now table stakes — but literally no outbound calls at all.** It is real. It is also thin, and it is a claim about architecture rather than a benefit anyone has asked for.

## How it makes money honestly

*(Full detail: [`products/haunt/cost-sheet.md`](../../products/haunt/cost-sheet.md).)*

Fixed running cost is **£83/year** — Apple Developer Program (£73.08) plus a domain. No hosting line, no database line. Constitution 1.5 is satisfied by architecture rather than by discipline, and on the offline architecture the per-user API cost is **£0.00**. This is the first candidate on the backlog where "cheap to run" is structural.

At 5,000 users, iOS-only, offline venue index, cost + 20% with store commission passed through at zero markup (**16.5% effective margin — a justified deviation *below* the ~20% target, not "inside" it; see O12 below**, and far inside the 30% cap):

| Model | Honest price | Volume to cover benchmarked labour (3 yr) |
| --- | --- | --- |
| **One-off purchase** | **£14.63** | **~2,370 sales** |
| Free + lifetime unlock (9:1) | £29.59 | **~1,170 unlocks** |
| Free + subscription | £3.21–£4.88/yr | **~2,370 subscribers held 3 years** |
| Article 8 non-profit | £0 | n/a — £14,719 unrecovered build + £4,989/yr |

> **⚠ Correction, 2026-09-10 — CVO error, caught by the Skeptic at gate.** The volumes above originally read ~1,480 / ~715 / ~1,480. Those were wrong. I built this table by taking the *price* column from the offline-Overture architecture and leaving the *volume* column from the CFO's §10 table, which is computed on Mapbox pricing (£23.41). Cheaper product, same volumes — arithmetically impossible, and the CFO's own §6 contradicted me on the page I drew from (£14.99 → 2,310 sales). Corrected above: `£24,532 ÷ (shelf ÷ 1.20 × 0.85)`.
>
> **The error was not cosmetic.** It flowed into the single falsifier this proposal offers the gate, which is corrected in "Success and abandonment criteria" below.
>
> **And it is probably still optimistic.** The CFO wrote before the CTO note existed and asked engineering for a build number; the CTO answered 16–19 focused weeks against the CFO's assumed 12, and nobody re-derived. Carried through, the honest price becomes **£16.31–£17.56** and break-even **~2,550–2,660 sales**. Against that, my original "~1,480" was 72–80% low. **Treat ~2,400–2,700 as the honest range and £14.63 as a floor, not a price.** A re-derived cost sheet is a condition on any PROCEED.

**On your subscription question — I was wrong and the CFO corrected me.** My idea brief said a subscription could not be justified under 2.1 because there is no recurring cost to take 20% of. There are four genuine recurring costs, and the CFO made the case rather than assuming it. But the honest subscription price is **£3.21–£4.88 a year**. It is justifiable and it is not a business, and it falls further as the build amortises because 2.3.3.1 ratchets prices down. A one-off purchase is the honest structure here.

**On your free-tier cap — there is a compliant design, and it is not an entry cap.** Cap the automatic venue *lookups* (the only thing that costs money per use) and leave entries, history, editing and export unlimited forever. That aligns the paywall exactly with the cost. Any cap on reading entries already written — "last 30 days free" especially — is an Article 4 breach and the CFO records it as a launch-blocking defect: Haunt's software would be refusing to display a file on the customer's own hardware that Candour has never seen. **Note that on the offline architecture there is no per-lookup cost at all, so the only compliant basis for a free tier disappears with it.**

**The number the gate should stare at: ~2,370 sales at £14.63 — and realistically ~2,400–2,700** once the CTO's build estimate replaces the CFO's assumption. Against a category leader with 164 UK ratings after a decade, with no ads, no data, no social graph, no viral loop, and a 20% margin that cannot fund acquisition. No pricing structure in the cost sheet rescues that if the volume is unreachable — the CFO says so directly, and I agree. The correction makes the case for kill stronger, not weaker, which is precisely why it needed catching by someone other than me.

**Also on the record:** none of the four models generates a reserve at plausible volumes. Constitution 2.3 puts reserve top-up first in the waterfall, and at 1,000–5,000 users Haunt does not clear its own benchmarked labour.

## Constitution check

- **Article 1 fit.** 1.5 is met structurally (£83/yr fixed, £0/user). 1.3 is met *better* by the offline architecture than by the sparked one — the claim becomes unconditional. **1.1 is where it fails:** the test is whether people would recommend it unprompted, and the evidence says the audience is small, already served, and mostly served for free.
- **Article 2 pricing plan.** One-off purchase, £14.63 inc. VAT at 5,000 users on the offline index, 16.5% effective margin. No deviation proposed. Cost sheet published at launch and annually per Article 3.
- **Article 4 risks.** Data collection is near-nil by construction and export is nearly free if the format is chosen at the start (~3–5 days now, a multi-week retrofit later). Two live hazards: (i) any free-tier cap that gates entries already written — CFO blocks it, I endorse the block; (ii) marketing Android before a device-matrix spike, which would be a claim we cannot substantiate. **Accessibility: not yet assessed — no UX seat has looked at this, and WCAG 2.1 AA is a gate requirement, not a build afterthought.**
- **Regulatory exposure (CGO input).** ✅ **Obtained 2026-09-10** — `products/haunt/compliance-note.md`. The CGO does **not block**, subject to three conditions. Headlines: the caching question is **deferred, not avoided** (Foursquare's own guidelines expressly regulate *on-device* caching more tightly, not less); **Constitution 6.1 qualified human legal review is not required for the zero-network MVP, and is unavoidable for any architecture that touches a places API**; Candour is **neither controller nor processor** of journal data (household exemption) but **is** a controller of support and TestFlight data, which means an **ICO annual charge missing from the cost sheet's £83/year**; Apple Distribution International is merchant of record, closing the CFO's unverified VAT assumption. It also found **the pack had CDLA backwards** — CDLA-Permissive-2.0 has no attribution clause at all, and the real obligation comes from the Apache-2.0 Foursquare portion, which no in-app licences surface currently satisfies. Half a day of work, but currently unmet.

## What we are explicitly NOT building

- **Any sharing, social, or public layer — and I am closing this door rather than leaving it ajar.** The Research Analyst disagreed with me on the record and I am accepting the disagreement in full, for the reason they gave: the sharing layer is the only growth mechanism this product could ever have, so the option would be exercised for company reasons and then justified with user reasons. Article 1.1 judges products by unprompted recommendation, not by engineered referral. They also found zero requests for sharing or ratings in Arc's feature-request thread — one self-selected thread, which they flagged loudly, and which I am not resting the decision on. The reasoning stands without it.
- **Android at MVP.** The CTO asked that "both platforms are in scope of the promise" be restated as *intention*, not promise. **Accepted, and corrected here:** Android is an aspiration contingent on a published device-matrix spike, and it may not be marketed before that spike runs.
- **Any online places API.** Dropped from the architecture entirely rather than shipped and retrofitted.
- **Analytics or bundled telemetry SDKs.** Platform-mediated, user-opt-in crash reporting only, plus a user-initiated, user-readable diagnostic export with a build-failing test that journal text can never enter it.
- **Fully-automatic capture.** Nothing enters the timeline without confirmation.

## Success and abandonment criteria

**We kill this if** — and every one of these is already true today:

1. A shipping product matches the MVP on every axis but ratings. ✅ Arc Timeline 4 — and **stronger than the research brief claimed.** The brief named its own falsifier for this criterion (that Arc's notes might attach to *trips* rather than *venues*, which would leave a venue-journal gap). The Skeptic tested it at gate: it does not hold. Arc attaches notes to places.
2. A free incumbent ships the privacy pitch and the notes layer on both platforms. ✅ Google Maps.
3. The category leader's decade-long UK base is in the hundreds of ratings. ✅ 164 — **but see the caveat.** The rating count is retrieved [E]; converting it into a user base needs a ratings-to-installs multiplier that the Research Analyst explicitly disclaimed as a guess for this use. **This criterion is directional, not measured**, and the Skeptic was right to flag that I pre-ticked it as though it were measured. It should carry less weight than criteria 1, 2 and 4, which rest on retrieved fact.
4. The differentiating behaviour is a minority behaviour even where an audience rewards it. ✅ 14%.
5. There is no acquisition channel and no budget to buy one. ✅ By design, now doubly so with sharing closed.

**We would proceed if** the ceiling argument in research §9 is wrong — specifically, a **UK landing-page test** converting at a rate implying a base above **~2,700 buyers**.

> **⚠ Correction, 2026-09-10 — CVO error, caught by the Skeptic at gate.** This threshold originally read "~1,500 buyers at £14.63", inherited from the arithmetic error corrected above. It was **37–44% below the break-even it purported to represent**, so a test calibrated at it could have *passed* and authorised a build that cannot pay its own benchmarked labour — the exact outcome Article 2.1's labour rule exists to prevent. I am setting the replacement at the **top** of the honest range (~2,700, the CTO-adjusted figure) rather than the bottom, because a falsifier that flatters the idea is not a falsifier. That is the one fact that would overturn this, it is cheap, and it is the only pre-build spend I would authorise. Two supporting probes the CTO wants before any build: a 2-day spike on whether the right venue lands in Overture's top three candidates, and a measured battery cost for `startMonitoringVisits` over a real week.

### The fourth option I omitted, restored at full strength

> **⚠ Omission, 2026-09-10 — CVO error, caught by the Skeptic at gate.** The CFO asked in writing that Article 8 designation be *"a live option at the gate rather than a rhetorical one"*, and named the condition that would make it live: the research brief confirming that Google Maps Timeline already ships the local-only pitch for free. **The research brief confirmed exactly that.** The condition was met, the option went live, and my proposal disposed of it by leaving it out of the options — while arguing the kill largely on economics that designation dissolves. That is the worst kind of omission: the one that happens to favour the author's recommendation. The Skeptic was right to call it and I am not going to bury the correction in a footnote.

**PROCEED UNDER ARTICLE 8 DESIGNATION** is a fourth thing the CEO may decide today. Stated as the CFO stated it, not as I would prefer it:

- **What it costs:** £14,719 of unrecovered build labour, plus **£4,989/year indefinitely**, funded from the Article 2.3 waterfall — which currently holds **£0**, because no Candour product has ever earned anything. Designation is **permanent and irreversible**. Honest description: one full build and about £5k/year of benchmarked founder labour, forever, with no recovery mechanism.
- **What it buys:** it deletes the pricing question, the free-tier question, the Article 4 cap question, the store-commission question, the adverse-selection question, and the "can we honestly promise lifetime support" question. Per the CFO: *everything difficult in sections 5 through 8 of the cost sheet is an artifact of trying to charge for it.* The per-user API cost also goes to zero, because bring-your-own-key moves the meter to the user.
- **The CFO's argument, verbatim in substance:** designation is the only structure in which *"we cannot beat free, and we are not going to pretend we can"* is a coherent thing for Candour to say **and still ship the product**.

**Why I still recommend kill over designation — stated as a position, not a finding.** Designation answers the *money* objection completely. It does not touch kill criteria 1, 2 or 4: the product still exists (Arc), a free incumbent still ships it on both platforms (Google), and the differentiating behaviour is still a minority behaviour. Giving away a product that is already available free is not obviously better than not building it, and Article 8 designation would commit an unincorporated brand with £0 income to an irreversible perpetual cost.

**The strongest case against my position, which the CEO should weigh properly:** Article 1.1's test is whether people would recommend it unprompted, and a genuinely zero-network, open-source, self-hostable location journal is exactly the kind of thing the privacy community *does* recommend unprompted — where a £14.63 paid app with 164 competing ratings is not. Designation would also convert the one surviving differentiator (literally no outbound calls, which neither Arc nor Google offers) from a thin commercial edge into a coherent public-good pitch. If Haunt is worth existing at all, designation is the structure in which that is true. **That argument is not mine and I do not endorse it — but it is a real argument and it deserved to be in the pack from the start.**

**What I am not recommending: park.** Parking a question this thoroughly answered is the drift 5.2 exists to prevent. The evidence will not improve by waiting, and Arc will not get smaller.

**Salvage worth keeping regardless of the decision.** The measured Overture-derived UK venue index — 346,184 venues, 21.3 MB, permissively licensed, reusable offline — is a genuine asset produced by this discovery, and it is exactly what any future Candour product needing venue naming without a network would otherwise have to rediscover. It should survive the kill.

## Attachments required before gate

- [x] Research brief — `research/haunt-brief.md` (delivered 2026-09-09)
- [x] Cost model (CFO) — `products/haunt/cost-sheet.md`
- [x] Feasibility note (CTO) — `products/haunt/feasibility-note.md`
- [x] **CGO regulatory note** — `products/haunt/compliance-note.md` (2026-09-10); does not block, three conditions attached
- [x] **UX / Article 4 note** — `products/haunt/ux-note.md` (2026-09-10); seven would-be release blocks specified with lifting conditions
- [ ] **Dissent memo (Skeptic)** — attached unedited at `/gate`, before the CEO sees the pack (Constitution 5.3)

**Standing decisions this pack puts to the CEO (Constitution 5.4), which outlive Haunt:** how build labour is costed (capital amortised over a *published* supported life — this pack's treatment — or year-one operating cost); whether the labour benchmark is salary or full employment cost (±15–18% on every number); and whether store commission earns margin or is passed through at cost (±4% on every price, passed through here). These will recur on every cost sheet this company publishes, and settling them now — while no live price depends on the answer — is the honest moment.


---

## CVO response to the Skeptic's dissent (Constitution 5.3)

Written 2026-09-10, after the CGO recorded a conditional block (G4) noting that six of the Skeptic's twelve objections had no written response anywhere in the pack. 5.3 requires the dissent to be **answered**, not acknowledged.

**Why I am answering these even though I recommend KILL.** A KILL is not an approval, so G4 does not engage on my own recommendation. Leaving the six unanswered would therefore have cost me nothing and would have fenced off the two PROCEED options — narrowing the CEO's choice to the one I argued for, through inaction rather than argument. That is the same failure mode the Skeptic already caught once in this pack (the omitted Article 8 option). Once is an error; twice, after it has been named, would be a pattern. **All four options must be equally available on the merits when this reaches the CEO.**

O1, O3, O4 and O7 are answered in place above, marked ⚠. O8 and O9 the CGO records as substantially discharged. The remaining six:

**O2 — the cost model predates the feasibility note, contradicts it on the largest line, and was never re-derived. CONCEDED IN FULL, and it is the most consequential of the six.** The CFO assumed 450 build hours and said in writing that engineering should supply the real number. The CTO supplied it — 16–19 focused weeks — and nobody re-derived anything. My arithmetic correction above carries the CTO hours through the *prose*; the Skeptic is right that **the cost sheet's tables still run on 450 hours throughout**, and a corrected sentence sitting above uncorrected tables is worse than either alone, because a reader takes the tables. **Position: no number in `cost-sheet.md` may be read as a price, and Article 3 would make that sheet public. A re-derived cost sheet on CTO hours is a hard condition on Options B and C, and it is not satisfiable today.** Owner: CFO.

**O6 — the labour benchmark anchoring every published number is a single secondary source, flagged twice, never upgraded. CONCEDED, and it is not a Haunt problem.** £56,914 anchors every figure in this pack and will anchor every cost sheet this company ever publishes under Article 2.1 and Article 3. The Skeptic attempted the primary itself and got a partial upgrade — the ONS ASHE citation is real and the reference period matches, so it is **not fabricated**, but the figure lives inside a spreadsheet the tooling could not open. That is the honest status: verified as a citation, unverified as a number. **Position: retrieving the ASHE primary is a precondition of publishing any cost sheet under Article 3, on any product — not of deciding Haunt.** It has now been flagged by two seats on three occasions, which is two occasions too many. Owner: CFO, as standing company work.

**O5 — the venue-index spike moved from before the gate to before any build, with no written reason. CONCEDED; the omission was mine.** The CTO called it a cheap, high-value spike to run *before* the gate; I relocated it to pre-build and gave no reason, because I had none. The evidence proves the index is 21.3 MB and 346,184 rows — that is size, not correctness — and Overture's own docs say the confidence score "does not address duplicates or property completeness", so the `confidence ≥ 0.5` filter is the wrong instrument for the risk. UX independently found the sharper version of this: silent duplicates split accumulated visit counts and ratings, corrupting the only surviving differentiator, with no server and no backfill. **Position: the spike is unrun, so no PROCEED may rest on the venue index being correct. Re-specified per UX to report duplicate rate and junk rate in the top five, not top-three hit rate alone.**

**O10 — the cost sheet's §5 sensitivity arithmetic does not reproduce. CONCEDED.** It errs *against* the product, so it does not move the decision. It is recorded because the Skeptic's framing is the point and I accept it: this is the same transposition family as my own O1 error, from a different seat, and **nobody in this pipeline re-derives another seat's arithmetic.** Two transposition errors in one pack, caught only because one seat re-derived from stated formulae rather than reading tables, is a process finding about Candour, not about Haunt. Folded into the O2 re-derivation. Owner: CFO.

**O11 — support labour is modelled on two incompatible bases. CONCEDED.** CFO £1.23/paying user/year against CTO a fixed ~2 hours/week (≈£3,402/year). At 5,000 users the CFO's line is higher; **at the 1,000–2,500 volumes that actually decide this, the CFO's line is £1,230–£3,075 against the CTO's £3,402 fixed.** The Skeptic's observation that this runs the same direction as O2 is the part that matters: **the pack understates cost exactly where the decision is closest.** Owner: CFO and CTO jointly, in the O2 re-derivation.

**O12 — 16.5% is below the ~20% target, so it is a justified deviation, and the cost sheet records "none proposed". CONCEDED, and this one is a constitutional labelling error rather than an arithmetic one.** Article 2.1 permits deviation from the ~20% target with written justification on the cost sheet. The CFO's justification (passing store commission through at zero markup rather than earning margin on Apple's cut) is, in my view, the *right* call and honestly argued — which is exactly why it should be recorded as what it is. Labelling a deviation "no deviation" defeats the purpose of requiring the justification to be written down, and Article 9 lists mislabelling as a gaming vector against this company. **I repeated the error in this proposal and have corrected my own wording above.** Owner: CFO, to relabel on the cost sheet.

**Summary of my response:** I concede all six. Four are corrections owed by the CFO; O5 is an omission of mine now stated with its reason; O6 is standing company work that outlives this product. **None of the six changes my recommendation — but O2, O5 and O11 all run in the direction of making the product look better than it is, and a CEO minded to PROCEED should know that the pack he would be proceeding on is, on those three points, flattering.** That cuts against my own recommendation being safe to trust for the opposite reason: a kill supported by flattering numbers is still the right answer if the flattering numbers already fail.

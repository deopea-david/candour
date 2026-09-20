# Subscription sizing note — Haunt

**Seat:** Chief Technology Officer · **Date:** 2026-09-19
**Commissioned by:** `decisions/2026-09-16-haunt-gate.md`, **Condition 9.8(b)** — *"the CTO must size the subscription-mechanics increment, which is not in the 1,330 hours, and answer whether 220 h/yr maintenance holds to year five."*
**Status:** technical note. Amends `products/haunt/feasibility-note.md` and `products/haunt/android-and-stack-note.md` where it says so. Feeds the CFO's re-derivation and the PM/BA's requirements. **Prepares and flags; does not certify** (Constitution 6.1). Kill/proceed and price remain the CEO's (Constitution 5.4).

**Template note:** `pipeline/templates/` has no template for a sizing note. This follows the house shape set by `android-and-stack-note.md` — answers first, decomposition second, blocks and open questions last. The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md` v1.1. Everything marked **[E]** was retrieved during this session on **2026-09-19** and the link travels with the claim. Nothing is cited from memory. **Every effort figure is [J]** — my estimate, not evidence — and the unit is stated at §10 rather than left to be inferred, because the Skeptic's O2 found that a missing unit conversion was the whole of a 33–58% discrepancy.

---

## 0. The answers, before the working

**The headline the CEO should read first, because it is not a sizing detail:** the seven items in this commission add more hours than the entire iOS-only MVP the gate originally looked at. **Build goes from 1,330 hours to a point estimate of 2,090 hours (+57%), and fixed annual maintenance from 220 h/yr to 360 h/yr (+64%).** On a five-year published support commitment those two changes move the annual cost basis by roughly **1.6×**, and the CFO's compliant band at 99p — 3,122 to 4,988 subscribers — translates upward with it. **The CFO's own sensitivity table in `pricing-ladder-model.md` §9.1 tops out at "+250 h build, +40 h/yr fixed". There is no row in it for what I am returning.** §10.

Seven answers, in the order commissioned.

1. **StoreKit 2 subscription mechanics: 3.5–5.5 focused weeks (131–206 h).** Implementable in full on a zero-network architecture, including session-granularity entitlement. **The CGO's flag F2 is answered YES with a caveat that matters more than the answer:** renewal and expiry dates *are* available on-device, but StoreKit's local transaction cache is populated by a prior online sync — *"To get the latest transactions the device will need internet access but it does cache data locally"* [E, Apple Commerce engineer]. So the entitlement layer must persist its own last-verified interval and be able to say **"unknown"** as distinct from **"unentitled"**. §3.

2. **The Price-Tier-0 trial (guideline 3.1.1): I cannot confirm it is available to Haunt, and the distinction I owe my charter is that this is a permission question, not a capability question.** Technically it is buildable, and better than UX supposed — the trial's start date is recoverable from the Price-Tier-0 non-consumable's own `purchaseDate` in `currentEntitlements`, which survives reinstall, needs no server, no DeviceCheck and no covert identifier. What I could not establish is that Apple permits it to an app that also sells auto-renewable subscriptions: the guideline's permission is addressed to *"Non-subscription apps"* [E, verbatim], the mechanism Apple points at for managing it (*"Receipts and DeviceCheck"* [E, verbatim]) requires a server Candour does not have, and **two public developer questions asking exactly this have zero replies.** §4. **Recommendation: build the trial behind one state machine with two triggers (≈0.25 week), so the answer changes a configuration rather than a design.**

3. **DMCCA R1–R5: 1.75–2.75 focused weeks (66–103 h)**, all local, collecting nothing. **The proportionate-refund duty is confirmed out of scope of this estimate and of any estimate** — it is not a build item, no build creates it, and it belongs to the Constitution 6.1 legal review at launch bar **L1**. §5.

4. **The read-only lapse state: 2–3 focused weeks (75–113 h).** Guideline 5.1.2(i) is satisfiable, and one technical fact shapes the design: **iOS provides no API by which an app can relinquish its own `Always` grant.** Stopping is something the app does; revoking is something only the user can do. So the honest implementation is *stop monitoring, show the live state, and give the Settings path in words.* §6.

5. **Session segmentation and the venue page: 5–7 focused weeks (188–263 h). The CVO's schema constraint is CONFIRMED, with one amendment that is not a quibble:** sessions derived and recomputable is right, and it is only coherent if three things *are* durable rows — the user's overrides, the entitlement intervals, and the capture-gap records. **A derived view cannot be recomputed truthfully against a history it does not carry.** §7.

6. **Venue-index remediation: 4–6 focused weeks of build (150–225 h), plus a 3-week (113 h) pre-build spike carried separately because it may return "don't".** This is new work that appears in no estimate in this repository. §8.

7. **Does 220 h/yr hold to year five? No, and not close. My answer is 288–441 h/yr, point estimate 360.** The single largest cause is not the OS releases the question named — it is that the Engineer's spike converts a dataset *refresh* into a dataset *reconciliation*, which recurs for the life of the product. §9. **What would overturn this, and where I looked: §9.4.**

**Blocks.** Blocks 1, 2 and 3 are unchanged and restated at §11. **I pre-declare Block 4** — build commencement on the venue index as `feasibility-note.md` §2 specifies it — with the checklist item it fails and what lifts it. I do **not** block on cost or scope; that is a flag, and the seats it belongs to are the CFO (uncosted launches) and the CEO (5.4).

---

## 1. What I was asked, what I did, and what I could not do

Condition 9.8(b) asks two questions. The commissioning brief adds five more, and every one of them is work that post-dates the estimate it is being measured against. I have therefore **re-based the whole estimate rather than appending to it**, because a list of increments bolted onto a table decomposed before a subscription existed is exactly the shape that produced the Skeptic's O2.

**What I did.** Read the current state of the Constitution (v1.2), my own amended charter, the evidence standard, the decision record in full including Conditions 1–10 and Corrections C1–C4, the Engineer's venue-index spike, and the CFO, CGO and UX pricing artifacts. Retrieved Apple's StoreKit 2 documentation, the App Store Review Guidelines, Apple's upcoming-requirements page, Google Play's target-API requirements and Expo's changelog **at source this session**. Re-derived the hour figures from weeks with the conversion stated.

**What I could not do, stated before the numbers rather than after them:**

- **I have not written a line of this app.** Every hour figure is [J]. They are "focused solo weeks" in the same unit as `android-and-stack-note.md` §3, and they carry the same warning: calendar is not effort, and rows involving store review carry weeks of waiting that are not hours worked.
- **I could not settle the 3.1.1 trial question.** It is answerable in App Store Connect and through App Review's pre-submission channel and it is not answerable from published text. §4 states exactly how far I got.
- **I could not verify the local-notification authorization requirement at source this session** — the documentation page returned 404. It is tagged [K] at §5.3 and carried as an open question.
- **I did not re-run the Engineer's measurements.** §2 accepts them, including the one that contradicts my own note.
- **I did not price variable support.** The CFO's contact-rate basis stands, amended at §9.3, and the circularity warning in `android-and-stack-note.md` §3.4 is unchanged: break-even is a fixed point, not a division.

---

## 2. The venue spike, answered first — including where it corrects me

`products/haunt/venue-index-spike.md` (Engineer, 2026-09-18) reproduces my extract exactly on five of six measures and does not reproduce the sixth. I take the corrections in the order that matters least to most.

### 2.1 The 346,184 figure: conceded, and the defect is mine

The spike reports 330,208 named / **302,820** named at confidence ≥ 0.5 against my 346,184, and says the number is *"not recoverable from the note, because the note does not state the category predicate behind it."*

**That is correct and I concede it without qualification.** The defect is not that my number was wrong — I cannot now establish whether it was, because I did not write down the predicate that produced it. **The defect is that it was unre-derivable**, which is precisely what Condition 6 exists to prevent, and it is the same failure class as the Skeptic's O2 finding about my missing week-to-hour conversion: in both cases the estimate may have been fine and the *method* was not on the page. Two occurrences, one seat, same shape.

**`feasibility-note.md` §2.3 and §2.4 are corrected in place**: the food-and-drink count is **302,820** at `taxonomy.hierarchy[1] = 'food_and_drink'`, named, confidence ≥ 0.5, on release `2026-08-19.0` [E, Engineer's measurement, `venue-index-spike.md` §2, which I accept rather than re-run]. **Nothing downstream moves.** Size was 21.3 MB / 10.8 MB on my count and 23.3 MB / 11.3 MB on the spike's; both are a rounding error against Apple's 4 GB build limit and both support the same conclusion, which the spike states plainly: *"Size is settled and is not the question."*

### 2.2 The finding that does move things

Three measurements, which I treat as the operative facts for everything below [E, Engineer's measurements, `venue-index-spike.md` §§4–6]:

- Top-three hit rate **53.0%** overall, **47.9%** in a dense city centre, at a perfect location fix.
- At σ = 25 m query error, the compound probability of the right venue appearing in the top five in a dense city centre is **≈ 28%**.
- **At σ = 25 m, 100% of city-centre venues had their rank-1 candidate change across 20 simulated visits, median 10 distinct venues taking first place.**

**The third is the one that matters and it is the one nobody had asked for.** The gate's Condition 2 asked for hit rate, duplicate rate and junk rate. Duplicate rate came back at 5.1% — a pass — and the spike's §6.2 is right that the metric is the insensitive one. **The splitting mechanism is temporal, not within-list**, and no metric anyone specified would have caught it.

**What I want on the record, because it is a finding about this company and not about Haunt:** my open question 4 in `feasibility-note.md` §8 asked *"how often is the right venue in the top three candidates?"* That was the right question and it was **not sufficient**, because a venue page is not built from one lookup — it is built from the same lookup repeated over years. I specified a single-shot metric for a longitudinal feature. The Engineer found the gap by measuring something nobody asked for. **That is the behaviour the evidence standard is trying to buy, and it should be said that it worked.**

### 2.3 The `confidence >= 0.5` filter is exonerated and I am not taking the credit

Of 55 misses, the confidence filter caused **2**; the category filter caused **9**, including 1,022 UK rows Overture files as `inn` under `lodging` [E, Engineer]. The Skeptic was right that confidence cannot address duplicates — Overture says so itself — and wrong about where the damage was. **But my `food_and_drink` predicate is the instrument that was actually losing venues, and it is mine.** An index for a British going-out journal that excludes everything called *something*-Inn is excluding pubs by name morphology. §8 sizes the fix.

### 2.4 The hazard the spike calls cheapest now and most expensive to retrofit

> **A dataset refresh must never mutate venue rows already referenced by a user's visit.**

`feasibility-note.md` §3 committed that *"venue identity is a Candour-owned local row"* carrying the GERS ID *"as an attribute, never as the only handle."* **The spike is right that this is necessary and not sufficient: it settles the identifier and says nothing about the fields.** Overture's own documentation records that a taxonomy overhaul in this release cycle *"repathed 2,108 categories, renamed 407 and removed 80"* and that inconsistent conflation *"causes identities to split or merge as source data shifts"* [E, Engineer's retrieval].

**I adopt the spike's five acceptance criteria as an architectural constraint, not a recommendation**, and they are the subject of Block 4 at §11. With no server, no telemetry and no backfill, a refresh that corrupts referenced rows is **permanent, silent and undiscoverable by Candour** — and it corrupts the one feature the CEO identified as the product.

---

## 3. Item 1 — StoreKit 2 subscription mechanics

### 3.1 The CGO's flag F2, answered at source

`subscription-compliance-note.md` §4.3 rests items 3–5 of its minimum compliant implementation on a claim it tagged **[K], not retrieved**: that StoreKit 2 exposes entitlement and renewal information locally. It is F2 in that note's flag table and it is mine to close. **It is closed, and the answer is yes with a caveat.**

**What is available on-device:**

- `Transaction.currentEntitlements` — *"A sequence of the latest transactions that entitle a customer to Apple In-App Purchases and subscriptions"*, emitting *"a transaction for each non-consumable Apple In-App Purchase"* and *"the latest transaction for each auto-renewable subscription that has a RenewalState of `subscribed` or `inGracePeriod`"*; *"Products that the App Store has refunded or revoked don't appear in the current entitlements"* [E, verbatim — [Apple, `Transaction.currentEntitlements`](https://developer.apple.com/documentation/storekit/transaction/currententitlements), retrieved 2026-09-19].
- `Transaction.expirationDate` — *"The date the subscription expires or renews"* [E, verbatim — [Apple](https://developer.apple.com/documentation/storekit/transaction/expirationdate), retrieved 2026-09-19].
- `Product.SubscriptionInfo.RenewalInfo` — *"provides information about the next subscription renewal period"*, carrying `renewalDate`, `willAutoRenew`, `expirationReason`, and a `signedDate` recording *"the date that the App Store signed the JWS renewal information"* [E, verbatim — [Apple](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo), retrieved 2026-09-19].
- Apple states plainly that no restore step is normally needed: *"In regular operations, there's no need to call `AppStore.sync()`. StoreKit automatically keeps up to date transaction information and subscription status available to your app. When users reinstall your app or download it on a new device, the app automatically has all transactions available to it upon initial launch"* [E, verbatim — [Apple, `AppStore.sync()`](https://developer.apple.com/documentation/storekit/appstore/sync()), retrieved 2026-09-19].

**The caveat, which is the engineering content of this answer.** Apple's own Commerce engineer, answering the offline question directly: *"To get the latest transactions the device will need internet access but it does cache data locally and new transactions are pushed to the device when online, so could be up to date when it goes offline"* [E, verbatim — [Apple Developer Forums thread 706450](https://developer.apple.com/forums/thread/706450), accepted answer from an App Store Commerce Engineer, retrieved 2026-09-19].

> **So: the data is local, the cache is remotely populated, and a cache that has never synced is indistinguishable from an unentitled customer.** [I, from the two [E] quotes above]

**That is not a footnote on a product that advertises working in a basement.** It produces three requirements that must be in the requirements document rather than discovered at build:

1. **The entitlement layer persists its own record.** On each successful verification, write the transaction's `productID`, `purchaseDate`, `expirationDate` and `signedDate` into the local store as an **entitlement interval**. Offline evaluation reads that, not StoreKit.
2. **"Unknown" is a first-class state, distinct from "unentitled".** An app that has never completed a StoreKit sync must not conclude the customer has not paid. It must conclude it does not yet know, and **resolve in the customer's favour for capture while never taking money** — capture continues under a previously verified, unexpired interval; nothing is ever hidden either way, because Condition 9.7 removed the only mechanism that could hide anything.
3. **Restore stays behind a button.** *"Calling `AppStore.sync()` displays a system prompt that asks users to authenticate with their App Store credentials. Call this function only in response to an explicit user action"* [E, verbatim, same source]. A "Restore purchases" control is therefore required and must never fire at launch — which is also the fix the forum thread names for an empty cache.

### 3.2 Session-granularity entitlement, and why it is cheaper than it sounds

The brief is right that this breaks Condition 8.6 if got wrong, and right that segmentation did not exist when 8.6 was written. **8.6 says derived views must compute over the complete set of the user's entries "or state plainly on their face that they are partial."** A session is a derived view. A session that straddles an entitlement boundary contains visits captured automatically before the boundary and nothing after it — so it is partial, **and partial in a way the user cannot see**, because the missing visits were never recorded to be missing.

Two things follow, and the second is the useful one.

**(a) Entitlement must be stored as intervals over time, not as a boolean.** "Are they subscribed?" is the wrong question to ask a journal. The right one is "was capture entitled at 23:40 on 14 March?" — and that is answerable only from a table of intervals, which §3.1 requires anyway for offline evaluation. **The two requirements are the same table.**

**(b) The mechanism that makes a straddling session honest already exists in the estimate.** `android-and-stack-note.md` §1.6 added **capture-gap detection and a timeline gap surface** (row 4, 1–1.5 weeks) so the product could say *"Haunt wasn't running between 14:10 and 19:40. Anything you did then isn't here."* **An entitlement lapse is a capture gap with a different cause.** So a session straddling a lapse renders with the gap it already knows how to render, the venue page's aggregates carry the same partiality statement, and 8.6 is satisfied by a surface built for Android's OEM problem.

**I want that recorded as a result rather than a convenience.** The gap surface was added because Android forced a better design, and it now discharges a constitutional requirement created by a pricing decision made three weeks later. **The design was right for a reason that had not happened yet**, and it is the strongest argument in this note for spending money on honesty surfaces early.

**What is genuinely new, and sized below:** stamping each visit with the entitlement interval in force at its `arrivalDate`; deriving session partiality from the intervals plus the gap records; and making the entitlement table readable by the native capture modules (§3.3).

### 3.3 Block 3 stands, and it extends

`android-and-stack-note.md` §4, Block 3: **JavaScript in the visit-recording path.** Unchanged, and now with a second limb.

The Swift module receives a `CLVisit` on a relaunched, terminated app and must decide, *before writing*, whether automatic capture is currently entitled. **If that decision requires booting Hermes to ask a JavaScript entitlement service, the block engages** — the product's central promise would depend on the slowest part of the stack at the moment the OS is least willing to give us time.

> **The entitlement interval table is part of the SQLite contract, written by the StoreKit layer and read by the Swift and Kotlin capture modules. JavaScript is never in the path of deciding whether to record a visit, any more than it is in the path of recording one.**

This makes the shared SQLite file a contract between **four** consumers rather than three (`android-and-stack-note.md` §2.2). That is a real cost and it is in row A5 below. It is also the correct design under any stack: the entitlement question is asked at the coldest possible moment, so its answer must be the cheapest possible read.

### 3.4 Decomposition — item 1

| # | Workstream | Weeks |
| --- | --- | --- |
| A1 | Product configuration: three auto-renewable tiers in one subscription group, the pay-once non-consumable, the trial artefact, App Store Connect metadata, localisation, tax and availability | 0.5 |
| A2 | Entitlement service: `currentEntitlements`, `Transaction.updates` listener, `VerificationResult` handling, grace period and billing retry, refund/revocation, **the interval store and the "unknown" state** (§3.1) | 1–1.5 |
| A3 | Session-granularity evaluation: per-visit entitlement stamping, session partiality derived from intervals plus gap records (§3.2) | 0.5–1 |
| A4 | Purchase surfaces: plans sheet with four tiers, purchase flow and error states, **Restore Purchases** behind an explicit action, `AppStore.showManageSubscriptions(in:)` deep link — *"Presents the App Store sheet for managing subscriptions"*, iOS 15+ [E, verbatim — [Apple](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)), retrieved 2026-09-19] | 1–1.5 |
| A5 | The fourth consumer of the SQLite contract: native-readable entitlement table, migration ownership, WAL/one-writer discipline across Swift, Kotlin, JS and the StoreKit layer (§3.3) | 0.5 |
| A6 | Trial state machine with two triggers (§4.5), trial status surfaces per `ux-note-pricing.md` §2.3 States 1–3 | 0.5–1 |
| A7 | StoreKit test configuration, sandbox matrix, subscription-state simulation, QA fixtures for expiry/grace/revoke/restore/reinstall-offline | 0.5–1 |
| | **Total** | **3.5–5.5** |
| | **In hours at 37.5 h/week** | **131–206** |

**Point estimate 4.5 weeks / 169 hours.**

**What I am explicitly not claiming.** I am not claiming StoreKit 2 is hard — it is markedly simpler than the original API and Apple has removed most of the receipt-validation work that made subscriptions expensive in 2019. **The cost here is not StoreKit. It is that this product asks StoreKit a question it is not designed to answer offline, from a native context, about a moment in the past.** Take away any one of those three and A2, A3 and A5 collapse to about a week between them.

---

## 4. Item 2 — Apple's Price-Tier-0 trial, and the question my charter makes me ask

The UX seat recommends **Route B** — a free time-based trial under guideline 3.1.1 rather than an auto-renewable introductory offer — because an introductory offer *"charges by inaction"* and triggers a DMCCA renewal cooling-off duty. It records the obstruction honestly and assigns it to me: *"Whether an app selling both auto-renewable subscriptions and a paid-once unlock may use the 3.1.1 trial is not determinable from the guideline text I retrieved"* [`ux-note-pricing.md` §2.1].

I retrieved the guideline myself rather than taking the quotation second-hand. **The UX seat's quotation is exact.**

### 4.1 What the guideline says, in full

> *"Non-subscription apps may offer a free time-based trial period before presenting a full unlock option by setting up a Non-Consumable IAP item at Price Tier 0 that follows the naming convention: 'XX-day Trial.' Prior to the start of the trial, your app must clearly identify its duration, the content or services that will no longer be accessible when the trial ends, and any downstream charges the user would need to pay for full functionality. **Learn more about managing content access and the duration of the trial period using Receipts and DeviceCheck.**"*
>
> [E, verbatim — [Apple, App Store Review Guidelines, 3.1.1 In-App Purchase](https://developer.apple.com/app-store/review/guidelines/), retrieved 2026-09-19]

And, in the same guidelines, the two sentences that frame the problem from the other side:

> *"Subscriptions may be offered alongside à la carte offerings (e.g. you may offer a subscription to an entire library of films as well the purchase or rental of a single movie)."*
> *"Auto-renewable subscription apps may offer a free trial period to customers by providing the relevant information set forth in App Store Connect."*
>
> [E, verbatim — same source, guideline 3.1.2(a), retrieved 2026-09-19]

### 4.2 Reading them together

**The permission at 3.1.1 is addressed to *"Non-subscription apps."* Haunt's ladder contains three auto-renewable subscriptions, so on the plain words Haunt is not one.** 3.1.2(a) expressly blesses selling a subscription alongside an à la carte purchase — which is the pay-once tier — and then routes subscription apps' trials to App Store Connect, which is Route A.

**So the plain reading is that Route B is not available to Haunt.** [I, from the two [E] quotes] I am not going to present that as the answer, for a reason my charter now names explicitly.

### 4.3 The charter question, answered: is nobody doing it, or does the platform merely not hand it to me?

> *"If I conclude something cannot be done, have I established that **nobody is doing it** — or only that the platform does not hand it to me?"* [`roles/cto.md`, as amended]

Here the two come apart, and separating them is most of the value of this section.

**Capability: Route B is buildable, and better than the UX seat assumed.** UX §2.6 worries that *"on a zero-network architecture a locally-tracked trial resets when the app is deleted and reinstalled"*, and warns — correctly and importantly — that the natural fix is a covert persistent identifier, which is *"the largest single reputational and Article 4 exposure in this whole pricing exercise."*

**That worry is largely answered by Route B's own mechanism, and nobody has noticed.** The Price-Tier-0 trial is a **non-consumable in-app purchase**. Apple's documentation states that `currentEntitlements` emits *"a transaction for each non-consumable Apple In-App Purchase"* [E, verbatim, §3.1], and that *"when users reinstall your app or download it on a new device, the app automatically has all transactions available to it upon initial launch"* [E, verbatim, §3.1]. So:

> **The trial's start date is the `purchaseDate` of the "14-day Trial" non-consumable. It is recorded by Apple against the customer's Apple ID, restored automatically on reinstall and on a new device, readable on-device, and it requires no server, no DeviceCheck, no Keychain trick and no identifier of any kind.** [I, from the [E] above]

Apple's own pointer at 3.1.1 is to *"Receipts and DeviceCheck"* — and **DeviceCheck is not available to Candour**: *"After you use the `DCDevice` class to generate an ephemeral token that identifies a device, **your server** uses HTTP `POST` commands to send requests to the query and update endpoints"* [E, verbatim — [Apple, Accessing and modifying per-device data](https://developer.apple.com/documentation/devicecheck/accessing-and-modifying-per-device-data), retrieved 2026-09-19]. A zero-network product has no server to run that from. **The half of Apple's suggested mechanism Candour can use is the half that works, and it is the better half** — the receipt/transaction route is per-Apple-ID rather than per-device, which is both more durable and less invasive.

**Recorded as a correction to a live recommendation, not as a criticism:** `ux-note-pricing.md` §2.6's recommendation ("accept the leak, do not build the counter-measure") is **still right** and its second and third reasons are untouched. Its first reason — that Route A solves the problem and Route B does not — is wrong. **Route B solves it too, and by the same mechanism Apple already provides.** That strengthens Route B rather than weakening it, which is the direction that runs against my own inability to confirm Route B is permitted, and is why it is here rather than in a footnote.

**Permission: I could not establish that anybody is doing it, and I could not establish that nobody is.** Where I looked:

- The App Store Review Guidelines in full, retrieved this session — 3.1.1 and 3.1.2(a) are the only two places the question is addressed, and they do not meet.
- Apple Developer Forums, two threads asking this exact question. Thread 678747: *"What's the meaning of 'non-subscription apps'? Does it mean that I am not eligible to offer a free trial period IAP item (Non-Consumable item at price 0)?"* — **0 replies, 1 participant** [E, [thread 678747](https://developer.apple.com/forums/thread/678747), retrieved 2026-09-19]. Thread 725860, a developer asking how to configure a non-consumable trial at all — **0 replies** [E, [thread 725860](https://developer.apple.com/forums/thread/725860), retrieved 2026-09-19].
- A search for a shipped app combining both. **I found no retrievable example, and I also found no retrievable rejection.** The search engine's own summary asserted that Apple forbids the combination; **I am not citing that, because it is a generated summary with no source behind it and citing it would be exactly the fabrication this company's evidence standard treats as its most serious offence.**

> **The honest finding: the question is asked in public, by more than one developer, and Apple has not answered it in any source I could retrieve. That is not the same as a prohibition, and I will not report it as one.**

### 4.4 What would overturn this, and how cheap it is

*(Required by my charter as amended: a negative finding carries a block's duty.)*

**Overturned by any of:**

1. **Configuring a Price-Tier-0 non-consumable named "14-day Trial" in App Store Connect on an app that already has a subscription group.** If App Store Connect refuses the configuration, the answer is no and it cost twenty minutes. If it accepts it, the answer is *probably* yes and App Review is the remaining risk.
2. **An App Review pre-submission enquiry.** Free, and it is the channel designed for exactly this.
3. **A single retrievable shipped example.** One App Store listing showing both purchase types settles it.
4. **Published guidance or a forum answer from Apple.** None exists that I could find; one may appear.

**Cost of finding out: under half a day, entirely calendar rather than effort.** It is the cheapest determinative test in this whole pack and it should be run before the trial is specified, exactly as the UX seat asked.

### 4.5 The recommendation that makes the answer cheap either way

Do not wait for the answer and do not bet on it.

> **Build one trial state machine with two triggers.** The state machine is: *trial active until date D → trial ended → read-only unless entitled.* Route A supplies D from the introductory offer's expiry; Route B supplies D from the Price-Tier-0 non-consumable's `purchaseDate` plus fourteen days. **Everything downstream of D — the three status surfaces, the expiry banner, the read-only transition, the venue page's partiality — is identical.**

Cost of the abstraction: **≈0.25 week**, inside row A6. Cost of not having it, if the store answer arrives after the trial is built: a rebuild of the purchase and status layers.

**My recommendation between the routes, as this seat's judgment [J]:** **Route B if permitted.** The UX seat's grounds are sound and one of them is mine to add — Route A's charge-by-inaction is the event that drags the whole DMCCA renewal-cooling-off machinery into the product (`subscription-compliance-note.md` §5.2: *"A renewal cooling-off period opens the day the first 99p is taken"*), **including the proportionate refund Candour has no mechanism to pay.** Route B has no renewal, so it has no relevant renewal and no cooling-off. **The cheapest way to avoid an obligation you cannot discharge is not to create the event that triggers it.** That is an architectural argument, not a marketing one, and it is why I am recording a preference rather than staying neutral.

---

## 5. Item 3 — DMCCA requirements R1–R5, and the refund that is not mine to size

### 5.1 Confirmed: dischargeable without collecting anything

The CGO's design at `subscription-compliance-note.md` §4.3 is **buildable exactly as written**, on this architecture, collecting nothing. I confirm it with the one dependency it flagged now closed (§3.1, F2). The persistent notices surface is an append-only table in the same SQLite store as everything else, included in the Condition 8.3 export by construction rather than by a second code path, and its entries are written from renewal dates the device already holds.

**One clarification the CGO could not make and I can.** §4.3 item 4 says notices are written *"from renewal dates read on-device"*. **They must be written from the *persisted entitlement interval*, not from a live StoreKit query**, for the reason at §3.1: a live query on an unsynced or offline device returns nothing, and a reminder notice that silently does not fire because the user was on a plane is worse than no design at all. The scheduler reads the local interval table; StoreKit updates that table when it can.

### 5.2 Decomposition — item 3

| # | Requirement | What it is | Weeks |
| --- | --- | --- | --- |
| C1 | **R1** — Schedule 23 Parts 1 and 2 mapped onto App Store metadata and the first-run disclosure screen, merged with Condition 8.1 rather than built twice | Mostly content and one screen; the merge with 8.1 is the saving | 0.5 |
| C2 | **R2** — persistent, append-only in-app notices surface: schema, UI, export inclusion, never auto-clearing, never dismissible into nothing | The real increment | 0.5–1 |
| C3 | **R3** — notice scheduling from the persisted interval table, paired local notification, **and a fallback for users who decline notification permission** (§5.3) | Scheduling logic plus a permission branch | 0.5–1 |
| C4 | **R4** — plainly-labelled cancellation control deep-linking to `AppStore.showManageSubscriptions(in:)`, with no retention offer, no confirm-shaming, no friction | Hours of code; the acceptance criteria are the work and they are the PM/BA's | 0.25 |
| C5 | **R5** — the CTO answers F2 before R2 and R3 are estimated | **Discharged by §3.1 of this note.** No hours | 0 |
| | **Total** | | **1.75–2.75** |
| | **In hours at 37.5 h/week** | | **66–103** |

**Point estimate 2.25 weeks / 84 hours.**

### 5.3 One constraint the CGO's design does not yet carry

The CGO's answer to the weakest limb of "durable medium" — s.280(a), *"addressed personally to the consumer"* — is a **local notification paired with the persistent record**. That is the right answer and it has a hole in it.

**A local notification cannot be delivered unless the user has granted notification authorization** [K, high confidence — I could not retrieve Apple's `requestAuthorization(options:)` page this session; it returned 404, and this is carried as an open question at §12]. The UX seat has independently retrieved App Store guideline **4.5.4**, that *"push notifications must not be required for the app to function"* [E, retrieved by the UX seat 2026-09-18, `ux-note-pricing.md` §9 — travelling from another artifact, attributed, not re-retrieved by me]. Condition 8.4 additionally forbids *"expiry notifications"*, and the UX seat's reconciliation at §2.4 permits a statement of *when money will be taken* but not a statement of *what you will lose*.

**Three consequences for requirements, and the third is the one that will be got wrong:**

1. **Notification permission must be optional and requested in context**, at the point the first subscription is purchased, with the reason stated. Not at first run, and never as a gate.
2. **The persistent notices surface must be able to carry the duty alone.** If the user declines notifications, R2 is the whole of the compliance story and must be built to stand on its own — which is why R2 is sized above R3 and not below it.
3. **The paired notification's content is a charge-date disclosure, not a loss warning**, per the UX seat's test. Under Route B there is no charge date, so there is nothing to notify and the whole branch falls away — **a further argument for Route B that is neither mine nor UX's but the statute's.**

### 5.4 The proportionate refund: confirmed out of scope, and not by preference

> **Confirmed. The proportionate-refund duty is not in this estimate, is not sizeable, and must not appear on the CFO's cost sheet as a build line.**

The reason is not scope management. It is that **no build creates a refund mechanism on this architecture**, and the fact that decides it is already on file and retrieved by another seat: *"Candour cannot process a refund. There is no mechanism. Refund requests go to Apple, are decided by Apple against Apple's criteria"* [E, `compliance-note.md` §4.1, quoted at `subscription-compliance-note.md` §5.2], with Apple's Schedule 2 §6.3 confirming the only route is Apple refunding and Candour reimbursing [E, retrieved by the CGO 2026-09-18].

There is one thing StoreKit gives an app here and it is not a refund: `Transaction.beginRefundRequest` starts an **Apple-adjudicated** request, and refunded or revoked products simply *"don't appear in the current entitlements"* [E, verbatim, §3.1]. **That is a route for the customer to ask Apple, not a mechanism for Candour to pay.** Building it is worth doing — it is a courtesy and it costs hours, not weeks, and it belongs in row A4 — but **it must not be represented to anyone as discharging a statutory proportionate-refund duty**, and I am recording that here so it cannot be later.

**This is a Constitution 6.1 question and it sits at launch bar L1, with flag F3, exactly where the CGO put it.** I have nothing to add to that seat's analysis and I am not going to add weight to it by restating it — *"seats repeating one another's concern do not multiply into independent blocks"* (`roles/cto.md`). **What I can say from this seat, and it is the only thing I can usefully say: the engineering answer to F3 is that there isn't one.** If the human review concludes the duty falls on Candour, the options are commercial or structural — not technical — and the CEO should know before requirements are signed that no amount of build budget moves this line.

---

## 6. Item 4 — the read-only lapse state, and guideline 5.1.2(i)

### 6.1 What "read-only" means technically, given Condition 9.7

Condition 9.7 as amended: *"On lapse the product becomes read-only: automatic capture stops, everything already written stays visible, and manual entry may continue. Nothing is ever hidden."*

**That is the cheapest post-lapse state that exists, and it is cheap for a structural reason worth naming.** Every other candidate requires the read path to know about entitlement. This one does not: **the journal's read path has no entitlement dependency at all.** Queries are unfiltered, aggregates are unpartitioned, the export is one code path, and there is no second result set anywhere. The CFO's window model priced the two-result-set aggregate; on this shape it does not exist.

**So the entitlement dependency in the whole product reduces to three places:** the capture module's decision to record a visit (§3.3), the composer's decision to offer automatic versus manual entry, and the notices/status surfaces. **Everything else is entitlement-blind, and requirements should say so as a positive constraint**, because the natural drift during build is for an entitlement check to creep into a query, and once one is there the export diverges from the app and Condition 8.3 breaks silently. **QA's diff test (`ux-note-pricing.md` §1.5 item 2) is the check that catches it and it should run on every build, not at pre-release.**

### 6.2 Manual entry: partly new scope, and I am flagging it rather than absorbing it

`feasibility-note.md` §2.6 specifies a **"this venue isn't listed" path** — a user-entered venue name attached to a visit the OS detected. **That is not the same thing as manual entry of a visit.** A lapsed user has no OS-detected visit to attach anything to; they need to create a visit from nothing: date, time in, time out, venue (from the index or typed), notes, rating, and a session it belongs to.

**On the current decomposition that composer does not exist.** Row 6 of `android-and-stack-note.md` §3.2 is *"Timeline UI, entry editing, notes, ratings, search"* — editing an existing entry, not authoring one. **Condition 9.7 makes the manual composer the entire product in the unpaid state**, and the decision record says so in terms: *"a lapsed user retains a free manual journal indefinitely."*

> **A composer that is the whole of the free product cannot be a text field at the bottom of an empty state.** It has to be good, because it is what the trial converts *from* and what a lapsed user is left *with* — and because it is the 5.1.2(i) path for a user who refuses location entirely (§6.3).

Sized at 0.5–1 week in D2 below. **I record it as a scope addition rather than absorbing it into row 6, because absorbing it is how an estimate stops being re-derivable — which is the defect §2.1 already convicts me of once.**

### 6.3 Guideline 5.1.2(i), and the API that does not exist

The guideline, retrieved in full this session:

> *"Your app may not require users to enable system functionalities (e.g. push notifications, location services, tracking) in order to access functionality, content, use the app, or receive monetary or other compensation, including but not limited to gift cards and codes."*
>
> [E, verbatim — [Apple, App Store Review Guidelines, 5.1.2(i)](https://developer.apple.com/app-store/review/guidelines/), retrieved 2026-09-19. **The UX seat's corrected citation number is confirmed: this sentence is at 5.1.2(i).** Its earlier 5.1.1(ii) was wrong, as that seat found and reported.]

**Read against the read-only state, this cuts two ways and only one of them has been written down.**

**(a) The direction already recorded:** an unpaid state must never request `Always` location for a feature it cannot use. Satisfiable, and cheap: the permission request is attached to the capture capability, and the capture capability does not exist in the unpaid state, so the request is never reachable. The honest consequence UX names — *"upgrading from an unpaid state means a fresh permission grant mid-purchase… a worse funnel and an honest one"* — is unavoidable and correct.

**(b) The direction nobody has written down, and it is the stronger reading of the sentence:** *"may not require users to enable system functionalities… in order to access functionality, content, use the app."* **Haunt must be fully usable with location services denied outright, in every tier including a paid one.** A subscriber who revokes location must not find a broken app or a nagging one. That makes the manual composer (§6.2) not merely the free product but **a permanent first-class path in the paid product**, and it makes "capture is off, here is why, here is what you can still do" a state the app must render well rather than an error.

**The API constraint that shapes all of this:** there is no iOS API by which an app relinquishes its own location authorization [K, high confidence; flagged at §12]. `stopMonitoringVisits()` stops the app *using* the grant; only the user can remove it, in Settings. **So the app cannot make its own claim true by fiat — it can only stop, say so, and show the user the door.** That is why the three requirements the UX seat sets at §2.5 are the right ones and why the *third* (the Privacy screen showing live state) is load-bearing rather than decorative: on a product with no server, a claim the user can check is the only kind of claim that is worth anything.

### 6.4 Decomposition — item 4

| # | Workstream | Weeks |
| --- | --- | --- |
| D1 | Lapse transition: verifiable capture teardown on iOS (`stopMonitoringVisits`) and Android (foreground-service stop), entitlement-driven, idempotent, surviving app relaunch and device restart | 0.25–0.5 |
| D2 | **Manual visit composer** as a first-class path (§6.2), including session assignment and venue selection from the index | 0.5–1 |
| D3 | The three unpaid-state surfaces: `ux-note-pricing.md` §2.3 States 1–3, the Privacy screen's live capture state, the permission-revoke instructions | 0.75–1 |
| D4 | Full-function-with-location-denied path (§6.3(b)), in every tier | 0.25 |
| D5 | QA fixtures for the entitlement boundary: expiry, grace period, billing retry, revoke, refund, restore, reinstall-while-offline, and the export diff | 0.25–0.5 |
| | **Total** | **2–3** |
| | **In hours at 37.5 h/week** | **75–113** |

**Point estimate 2.5 weeks / 94 hours.**

**What this buys, stated because it is the answer to Apple's 3.1.2(a):** *"If you offer an auto-renewable subscription, you must provide ongoing value to the customer"* [E, verbatim — App Store Review Guidelines 3.1.2(a), retrieved 2026-09-19]. The subscription sells the capture engine, the maintained venue index and the five-year support commitment. **The maintained index only becomes an honest answer to 3.1.2(a) once §8's reconciliation work exists** — an index that is shipped once and never reconciled is not "maintained", it is "bundled". **That is an argument for spending §8's money that is independent of the spike's correctness finding**, and it is worth the CEO seeing both arguments land on the same line.

---

## 7. Item 5 — session segmentation and the venue page

### 7.1 The CVO's schema constraint: confirmed, with one amendment

> **CVO:** *"Sessions must be **derived**, not stored as immutable facts… If sessions are persisted as first-class immutable rows, every future improvement to the segmentation algorithm either corrupts existing history or cannot be applied to it. Derived-and-recomputable means the algorithm can be improved for the life of the product. **This is the single most consequential line in this document** and it costs nothing to get right now."* [`proposals/haunt/ceo-product-inputs.md` §2]

**Confirmed. It is correct, it is the right call, and the CVO is right about why.** It is the same argument I made at `feasibility-note.md` §3 about venue identity, applied one level up, and it is right for the same reason: **the thing that must survive is the user's record, not our interpretation of it.** Visits are observations; sessions are an opinion about them; an opinion stored as a fact cannot be corrected.

**The amendment, and it is not a quibble.** "Derived, never stored" is a slogan that will be implemented literally and will then be wrong in three specific ways. **A derived view can only be recomputed truthfully against a history it carries.** Three things must be durable rows, and the CVO's own document already names the first:

1. **User overrides** (`ceo-product-inputs.md` §2.2, already stated): merges, splits and renames of sessions, persisted separately from the algorithm's output and surviving recomputation. **This is the hard part of the whole workstream**, because re-attaching an override to a recomputed grouping requires the grouping to have an identity that is stable under a changed algorithm. The design that works is to anchor an override to the **visits** it concerns, not to the session it produced — an override is a constraint on segmentation ("these two visits are the same night", "these two are not"), and the segmenter takes constraints as input. **Specified that way, overrides are inputs rather than patches, and recomputation is free.** Specified any other way, this is where the bugs live for the life of the product.
2. **Entitlement intervals** (§3.2). A session recomputed in 2031 must know whether capture was entitled in 2027, or its partiality statement will be a guess.
3. **Capture-gap records** (`android-and-stack-note.md` §1.6). Same reason. A gap is an observation about the world, not a derivation — it cannot be recovered later from anything.

**And one permission, which the literal reading forbids and should not:** a **memoisation cache** of computed sessions is fine and will be necessary for a growing journal, provided it is rebuildable from (visits + overrides + intervals + gaps) and is discarded on any algorithm change. **Cache is not storage.** The test the PM/BA should write: *delete the cache, recompute, and the user sees exactly what they saw before — including every correction they ever made.*

**Recorded as a confirmation with a clarification, not a challenge.** The CVO asked the right question and got the right answer; what it could not know is that the constraint has three dependencies that did not exist when it was written, two of which (entitlement, gaps) arrived with the subscription decision three days later.

### 7.2 "Home" is an inference, and the architecture has a view on it

`ceo-product-inputs.md` §2.3 requires the home inference to be visible and editable rather than silent. **Agreed, and one technical addition.** The home location must be a **user-editable row in the store, not a value recomputed on the fly** — because a user who corrects it is making an assertion about their own life, and an assertion that gets silently recomputed away next month is the same defect as a session override that does not survive. **It is an override, and it belongs in the override table at §7.1(1).** This is also the answer to the transparency point: a row the user can see and edit is a row the export carries, which makes the inference inspectable rather than merely disclosed.

### 7.3 The venue page, and what the spike does to it

The CEO's input: the venue page is *"probably the product, not a feature"*, and the CVO's read is that it is Letterboxd's film page applied to a pub.

**The spike is the reason this workstream cannot be sized without §8.** A venue page is an aggregate over a venue identity. The spike measures that identity as unstable on **100% of dense-centre venues across twenty visits** [E, Engineer]. **An aggregate over an unstable identity is not a feature with a bug in it; it is a feature that does not exist.** So the venue page's hours below assume §8's remediation lands; if it does not, these hours buy a screen that is confidently wrong.

**Condition 8.6 applies to this screen more than to any other**, and on the MVP as decided it is nearly free: nothing is hidden, so aggregates are complete and say nothing about partiality — **except** where a session or a stretch of history straddles a capture gap or a lapse, which is exactly the case §3.2 handles. **The venue page therefore needs one partiality surface, driven by the same intervals and gap records, and not a second result set.**

### 7.4 Decomposition — item 5

| # | Workstream | Weeks |
| --- | --- | --- |
| E1 | Segmentation algorithm: boundary detection, home-location inference (visible, editable, stored as an override), gap-awareness, parameterisation for later improvement | 1.5–2 |
| E2 | **The override model** (§7.1): constraint-based overrides anchored to visits, merge and split, survival across recomputation, the memoisation cache and its rebuild test | 1–1.5 |
| E3 | Session UI and its integration with the confirm queue — confirming one night with four venues rather than four visits (`ceo-product-inputs.md` §2, the connection the CVO drew) | 1–1.5 |
| E4 | **Venue page**: venue as a first-class aggregate entity, ratings rollup, visit history, notes, the 8.6 partiality surface, and query performance over a store that grows for five years | 1.5–2 |
| | **Total** | **5–7** |
| | **In hours at 37.5 h/week** | **188–263** |

**Point estimate 6 weeks / 225 hours.**

**One saving the CVO identified and I am confirming with hours behind it.** Specifying segmentation and the confirm queue *together* rather than separately is worth roughly **0.5–1 week** against building them apart, because the queue's bulk-confirm affordance and the session's grouping are the same data structure viewed twice. That saving is already inside E3. **It disappears if the PM/BA writes them as two requirements in two places**, which is precisely what `ceo-product-inputs.md` asked not to happen.

---

## 8. Item 6 — venue-index remediation: new work, sized here for the first time

### 8.1 What is already in the 1,330 hours, and what is not

Honesty about double-counting, because the whole value of a re-based estimate is that it does not quietly add the same row twice. **Row 5 of `android-and-stack-note.md` §3.2 (venue index, 4–5 weeks) already contains:** the extract pipeline, the bundled `.db` asset, the grid-cell spatial index and FTS5 name search, category mapping, confidence filtering, **duplicate merge, sticky choice, rename-in-place**, and the "not listed" path.

**What row 5 does not contain, because it was written before anything had been measured:**

| Not in row 5 | Why it is now required |
| --- | --- |
| A **measurement harness** as a permanent regression fixture | The spike built one and it lives in a session scratchpad. Without it, no future change to the index can be shown not to have made things worse. |
| A **rebuilt category scope** and its re-measurement | 16% of misses are my `food_and_drink` predicate (§2.3). Row 5's "category mapping" assumed the predicate was right. |
| A **ranking layer beyond raw distance** | Row 5 assumed distance ordering. At σ = 25 m in a dense centre, distance ordering is *"close to a random draw from the block"* [E, Engineer, §9.1(b)]. |
| **Copy-on-reference** venue rows and refresh **reconciliation** | Row 5 and `feasibility-note.md` §6.4 assumed a refresh is *"re-run pipeline, ship with app update"*. It is not, once a user's visit references a row. |
| A **search path** for the dense case | The spike's recall curve shows recall@20 of 92.5% against recall@5 of 51.9% in Manchester [E, Engineer, §5.3]. Five rows is a design constant that the measurement does not support. |

**Sticky choice, merge and rename-in-place are *re-scoped*, not added.** They are in row 5 and they stay there. The spike changes one thing about them and it belongs in requirements rather than in hours: **sticky choice must raise a previously-chosen venue in the ranking and must never pre-select one** — at 50 m a Manchester cluster holds around forty venues, so a shortcut would confidently offer the wrong pub when the user goes next door [E, Engineer, §9.2], and a pre-selected candidate is a pre-ticked box under Article 4 in any case.

### 8.2 Carried separately: a 3-week remediation spike that may return "don't"

The spike's verdict is *"not yet, not never"*, and it names its own most likely overturning test: a rebuilt category filter, re-measured, **and says that alone is insufficient** — the ceiling it can reach is roughly 58% → 67% at zero noise. The finding that actually condemns the venue page is rank-1 instability, and **nobody has tested whether any ranking signal fixes it.**

> **Recommendation: carry a 3-week (113 h) venue-index remediation spike as a separate pre-build line, on the same terms as the Android capture spike — because it may return "don't", and that is the point.**

| # | Spike content | Weeks |
| --- | --- | --- |
| S1 | Re-establish the Engineer's harness as a runnable fixture: FSA ground truth, seeded sampling, hit-rate, rank-1 stability and recall@N under stated query error | 1–1.5 |
| S2 | Rebuild the category scope (allow-list on `basic_category`, named out-of-hierarchy categories including `inn`, a rule for the 209,570 null-taxonomy rows) and re-measure | 0.5 |
| S3 | First-pass non-positional ranking (dwell duration against opening hours, category against time of day, prior user choice as a ranking input) and measure the modal rank-1 share | 1–1.5 |
| | **Total** | **2.5–3.5, carried at 3** |
| | **In hours** | **113** |

**The pass/fail criterion must be agreed with the PM/BA, UX and QA *before* the spike runs**, exactly as Block 2 requires for Android. My proposal, for them to accept or change: **the spike passes if the modal rank-1 share in a dense city centre exceeds 0.8 at σ = 25 m and top-five recall exceeds 80%.** The spike measured 0.27 and 51.9%. **A spike that returns "we could not get past 0.5" is a real input to a Constitution 5.4 decision and is worth 113 hours to know before spending 2,000.**

**Note what the spike's own finding already tells us about the answer.** Junk is ~2% and coverage is nearly twice the licensed-premises universe [E, Engineer, §§7–8]. **This is not a data problem that more data fixes; it is a precision-and-ranking problem, and adding rows makes it worse.** Everything in S2 and S3 is in the layer Candour controls, which is why I think the spike is worth running rather than treating the verdict as final.

### 8.3 Decomposition — item 6, build portion

Assumes the spike passes. If it fails, these hours do not arise and a different conversation does.

| # | Workstream | Weeks |
| --- | --- | --- |
| F1 | Productionise the ranking layer: the signal set the spike validated, tie-breaking that is never `confidence` (Overture documents it as measuring existence only), settable list length, the search path for dense areas | 1–1.5 |
| F2 | **Copy-on-reference schema** and the spike's five acceptance criteria (§9.3): freeze name/coordinate/category on first reference; refresh may add and update **unreferenced** rows only; changes to referenced rows are *offered*, never applied, declining is the default; user renames outrank the dataset permanently; user merges survive a refresh that re-splits upstream | 1.5–2 |
| F3 | **Refresh reconciliation tooling**: GERS identity diff across releases, upstream split/merge detection, generation of a reviewable change set that respects user renames and merges, and the harness re-run as a release gate | 1–1.5 |
| F4 | "This venue isn't listed" promoted to a first-class path rather than a fallback — at a **22% genuine absence rate** [E, Engineer, §9.2] this is one visit in five in suburb and small-town samples | 0.5–1 |
| | **Total** | **4–6** |
| | **In hours at 37.5 h/week** | **150–225** |

**Point estimate 5 weeks / 188 hours.**

### 8.4 The item for the CFO the spike raised unprompted, confirmed

`venue-index-spike.md` §9.4 tells the CFO that my *"~0.5 day/month"* refresh line becomes a reconciliation. **Confirmed, and it is the largest single component of my answer to Condition 9.8(b).** §9.2 carries it.

**One recommendation that saves money and is safer, not a trade-off between the two.** The 0.5 day/month figure assumed **monthly** refreshes. Once a refresh is a reconciliation, monthly is both expensive and wrong: every refresh is an opportunity for upstream identity churn to reach a user's history, and Overture's own documentation records that identities *"split or merge as source data shifts"* [E, Engineer's retrieval]. **Refresh quarterly, not monthly.** Four reconciliations a year at roughly 2.5 focused days each is **60–100 h/yr**, against 45 h/yr for twelve naive re-extracts — and it reduces the number of times the hazard at §2.4 is given a chance to fire by two thirds. The cost of quarterly rather than monthly is staleness in a dataset whose own currency risk the spike already measured as real but not fast-moving. **This is my recommendation as this seat [J]; the staleness/cost trade is the PM/BA's and UX's to accept.**

---

## 9. Item 7 — does 220 h/yr hold to year five? Condition 9.8(b), answered

### 9.1 The answer

> **No. It does not hold, and the shortfall is not marginal. My revised figure is 288–441 hours a year of fixed maintenance, point estimate 360 — an increase of 47% to 79%, and 64% at the point estimate.**
>
> **And the dominant cause is not the OS releases the question named.**

Condition 9.8(b) frames the risk as *"roughly five iOS and five Android major releases"*. That framing is reasonable and it is not where the money is. The OS rows in my existing table were broadly right. **What is wrong with 220 h/yr is that it was built for a product with a bundled dataset, no subscription, no regulatory surface and no published support commitment — and Haunt now has all four.**

### 9.2 The revised table, line by line, with what changed

**Unit: focused solo hours per year. [J] throughout.**

| Item | Old (`android-and-stack-note.md` §3.4) | **New** | What changed |
| --- | --- | --- | --- |
| Venue index: refresh → **reconciliation**, quarterly not monthly | 45 | **60–100** | The spike converts a re-extract into a GERS diff, split/merge detection, a reviewable change set respecting user renames and merges, and a harness re-run as a release gate (§8.4). Quarterly cadence limits it to four events a year. |
| iOS annual OS release compatibility | 37.5 | **37.5–45** | Broadly unchanged, widened. Apple's minimum-SDK requirement makes it non-optional (§9.3). |
| Android annual OS release + Play policy | 37.5 | **37.5–56** | Google Play's target-API requirement is an annual, hard-dated forcing function, and Android's background-location and foreground-service rules have changed materially in 8.0, 10, 11, 12 and 14 (§9.3). |
| Expo SDK / React Native major upgrades | 37.5–75 | **75–112.5** | The old row prices roughly one upgrade a year. Expo's own changelog shows SDK 56 (2026-05-21), SDK 57 (2026-06-30) and SDK 58 beta (2026-09-15) [E]. Two majors a year at ~37.5 h each is the honest figure, and skipping them is not free (§9.3). |
| OEM regression chasing | 30–45 | **30–45** | Unchanged. |
| Source-map retention and symbolication | 7.5 | **7.5** | Unchanged. |
| **Subscription and store-mechanics upkeep** | — | **15–30** | **New.** Annual price review and republished cost sheet (Article 2.1), the year-six ~32% step-down, StoreKit and App Store Connect churn, and certificate/signing changes of the kind Apple has already run once on receipts. |
| **Regulatory upkeep** | — | **10–20** | **New.** The s.277 regulations and DBT guidance land **after** launch on the Government's stated January 2027 date; Schedule 23 Part 3's prescribed notice content is set by regulations not yet made; L2 requires dated re-retrieval. Front-loaded into years 1–2. |
| **Accessibility re-verification** | — | **15–25** | **New, and it was an omission.** WCAG 2.2 AA was distributed into build rows and carried annually **nowhere**. System fonts, Dynamic Type scales and VoiceOver behaviour change with each OS release, on two platforms, in React Native. Constitution Article 4 makes this a standing obligation, not a launch task. |
| **Total** | **195–247 (point 220)** | **288–441 (point 360)** | **+47% to +79%; +64% at the point** |

### 9.3 Why "skip a year" is not available — the forcing functions, retrieved

The natural objection to any maintenance estimate is that a solo operator can simply not do it in a lean year. **On these two platforms that option does not exist**, and I retrieved the reason rather than asserting it.

- **Apple:** *"Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26"*, in force since **28 April 2026** [E, verbatim — [Apple, Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/), retrieved 2026-09-19]. Apple has run this cycle annually. **The consequence is that a single bug fix after the annual deadline requires the year's toolchain and SDK anyway** — so the OS-compatibility work is not deferred by skipping a release, it is deferred to the next time anything at all needs shipping.
- **Google:** from **31 August 2026**, *"New apps and app updates must target Android 16 (API level 36) or higher"*, and *"Existing apps must target Android 15 (API level 35) or higher to remain available to new users on devices running Android OS higher than the app's target API level"* [E, verbatim — [Android, Target API level requirements for Google Play apps](https://developer.android.com/google/play/requirements/target-sdk), retrieved 2026-09-19]. **Falling behind does not cost a release; it costs new users.**
- **Expo:** two stable SDK majors inside six weeks in mid-2026 and a third in beta by September [E, [Expo changelog](https://expo.dev/changelog), retrieved 2026-09-19]. Old SDKs are supported by EAS for a while and not forever, and Apple's annual SDK floor forces a native rebuild regardless. **The Expo upgrade tax is the direct and honest cost of the stack the CEO asked for, as `android-and-stack-note.md` §3.4 already said — it was simply priced for one upgrade a year rather than two.**

**And one thing five years does that three years does not.** An ageing React Native application does not get cheaper to upgrade; it gets dearer, because the gap between the app's dependency set and the current one widens every time an upgrade is deferred, and because four local native modules must be re-verified against each new SDK. **So a flat 360 h/yr is a five-year average, not a floor that decays.** Years 1–2 carry the regulatory front-load and the post-launch defect tail; years 4–5 carry an older codebase. I have deliberately not modelled a decay.

### 9.4 What would overturn this finding, and where I looked

*(Required by `roles/cto.md` as amended: a negative finding carries a block's duty. This is a negative finding about a number that sits under every price in the CFO's model, so it gets the full treatment.)*

**Overturned by any of these, in descending order of likelihood:**

1. **A decision to ship the venue index once and never reconcile it.** This is the largest line and it is the only one that is genuinely optional. It would cut 60–100 h/yr to near zero — and it would make the "maintained venue index" half of the subscription's Apple 3.1.2(a) ongoing-value claim unsubstantiable, and would leave the §2.4 hazard permanently armed. **It is a coherent choice and it is the CEO's, not mine. If it is taken, it must be taken in writing, because it changes what the subscription sells.**
2. **iOS-only.** Reverting to a single platform removes the Android OS/Play row (37.5–56), most of OEM regression (30–45), and — per `android-and-stack-note.md` §2.7 — the whole rationale for React Native, which removes the Expo upgrade row (75–112.5) and the source-map row (7.5). **That is 150–221 h/yr, roughly half of the total**, and it is by far the largest lever available on this number. I record it as arithmetic, not as a recommendation; the platform decision was the CEO's and was made on other grounds.
3. **Measured evidence that Expo majors can be taken annually rather than twice yearly at no compounding cost.** I could not find an Expo-published support-window policy and I looked; the changelog cadence is what I have.
4. **A shorter published support commitment.** Three years instead of five removes two years of the tail — but the Definitions permit shortening, never lengthening, and `pricing-ladder-model.md` §8.2 shows the monthly and paid-once tiers have **no overlapping compliant band at all** at three years. **This lever exists and pulling it breaks the ladder.**

**Where I looked:**

- **My own prior table, line by line**, rather than applying a multiplier to its total. Three of the nine rows are new; two are unchanged; four moved.
- **Both platforms' published forcing functions, retrieved at source this session** — Apple's upcoming-requirements page and Google Play's target-API page, quoted above. I did not take either from memory, and the Android figure in particular I would have got wrong from memory.
- **Expo's own changelog**, for cadence, rather than a recollection of it.
- **The Engineer's spike §9.4**, which raised the reconciliation cost unprompted and is the reason the largest line moved.
- **The CGO's launch bars L1 and L2**, for the regulatory row, which is the only row with a dated external trigger.
- **Where I did not look:** I did not survey comparable solo-operator apps' actual maintenance hours, and I do not know of a published source that would let me. **That is the single biggest weakness in this estimate and I am naming it rather than letting the table's precision imply a confidence it does not have.** Every figure here is [J] from one seat's judgment, and it has never been tested against a real year of anything.

### 9.5 Support: the fixed floor also moves

`android-and-stack-note.md` §3.4 sets a fixed support floor of **78 h/yr (1.5 h/week)** and keeps the CFO's contact-rate basis for the variable part. **The floor moves; the variable basis stands.**

A subscription creates a support category that a one-off purchase does not have and that a zero-network product handles blind: *"I paid and it says I haven't"*, restore failures on a new device, trial confusion, cancellation questions, and — the one with no good answer — an empty `currentEntitlements` on a device that has not synced (§3.1). **Every one of those is diagnosed without a server, without an account and without the ability to look anything up.**

> **Revised fixed support floor: 100–130 h/yr, point estimate 115.** The variable component keeps the CFO's contact-rate basis unchanged, with the circularity warning from §3.4 intact: **break-even is a fixed point, not a division.**

---

## 10. The one revised total, for the CFO to re-derive from

### 10.1 The unit, stated before the numbers

> **One focused solo week = 37.5 hours.** All figures below are **focused solo hours** on that conversion. Same unit as `android-and-stack-note.md` §3, stated again here because the Skeptic's O2 found that an unstated conversion was the entire 33–58% discrepancy between my weeks and the CFO's hours, and an estimate whose unit lives in another document is an estimate waiting to be misread.
>
> **Calendar is not effort.** Store review, the 14-day/12-tester Play closed test, the Android capture spike's two real weeks, the venue spike's measurement runs and any App Review pre-submission enquiry carry waiting that is not hours worked. **The PM/BA models the calendar; it is longer than the hours suggest, and materially longer than it was.**

### 10.2 Build — the revised figure

| | Weeks | Hours |
| --- | --- | --- |
| **Base: two-platform React Native build** (`android-and-stack-note.md` §3.1) | 31–40 | 1,163–1,500 |
| **+ Item 1** — StoreKit 2 subscription mechanics (§3.4) | 3.5–5.5 | 131–206 |
| **+ Item 3** — DMCCA R1–R4 (§5.2) | 1.75–2.75 | 66–103 |
| **+ Item 4** — read-only lapse state (§6.4) | 2–3 | 75–113 |
| **+ Item 5** — session segmentation and the venue page (§7.4) | 5–7 | 188–263 |
| **+ Item 6** — venue-index remediation, build portion (§8.3) | 4–6 | 150–225 |
| **Increment subtotal** | **16.25–24.25** | **609–909** |
| **REVISED BUILD TOTAL** | **47.25–64.25** | **1,770–2,410** |
| **Point estimate** | **55.75** | **2,090** |

> ### **The figure for the CFO: 1,770–2,410 focused solo hours of build. Point estimate 2,090 hours.**
>
> **Against the 1,330 hours currently in the model: +33% to +81%, and +57% at the point estimate.**

**Plus, carried separately as pre-build lines because either may return "don't build":**

| Spike | Weeks | Hours |
| --- | --- | --- |
| Android capture-reliability spike (Block 2, unchanged) | 2 | 75 |
| **Venue-index remediation spike** (Block 4, new — §8.2) | 3 | 113 |
| **Total carried separately** | **5** | **188** |

**A treatment point for the CFO, because it bears on the Definitions.** `pricing-ladder-model.md` amortises **£45,957.55**, which is 1,405 h × £32.71 — i.e. it folded the 75-hour spike into capital. That is right *if the spike passes and the build proceeds*. **If a spike returns "don't", its hours are not capital; they are a first-year expense, because there is no supported life to amortise them over.** With two spikes now in play, the treatment should be stated on the cost sheet rather than assumed.

### 10.3 Ongoing — the revised figures

| | Old | **New** | Basis |
| --- | --- | --- | --- |
| Fixed annual maintenance | 195–247 (point 220) | **288–441 (point 360)** | §9.2 |
| Fixed annual support floor | 78 | **100–130 (point 115)** | §9.5 |
| Variable support | CFO's contact-rate basis | **Unchanged** | iOS 5% × 45 min; Android 12% × 60 min, plus a subscription uplift the CFO should set |

### 10.4 What this does to the annual cost basis — indication only

**This arithmetic is [I] from [J] premises, which makes the whole of it [J]. It is an indication of direction and magnitude. It is not a price, it is not a band, and it must not be quoted as either.** Condition 6 requires arithmetic to be re-derived by a seat other than its author, and **the seat that owns these numbers is the CFO.** I show the working so it can be re-derived rather than re-guessed.

At the CFO's confirmed £32.71/hour benchmark, on a five-year published supported life, excluding variable support and the £83/yr cash costs:

| | Capital (build + spikes) | Amortised per year (÷5) | Fixed maintenance | Fixed support | **Annual hours** | **At £32.71** |
| --- | --- | --- | --- | --- | --- | --- |
| **Current model** | 1,405 h | 281.0 | 220 | 78 | **579** | **£18,939** |
| **This note** | 2,278 h | 455.6 | 360 | 115 | **930.6** | **£30,440** |
| | | | | | **×1.61** | **×1.61** |

**Three consequences, stated as direction rather than as numbers the CFO has not derived:**

1. **The band's *position* moves; its *width* does not.** The compliant band is bounded below by cost recovery and above by Article 2.1's 30% cap, and both bounds scale with cost at a fixed price. The CFO's 3,122–4,988 at 99p has a width of 1.60×; **that ratio is unchanged, and the whole band translates upward by roughly the cost multiple — indicatively to the order of 5,000–8,000 subscribers.** Condition 9.3's finding that *"a discount curve deeper than roughly 10% has no subscriber count at which every tier is simultaneously compliant"* is unaffected, because it too is a ratio.
2. **Condition 9.4's year-six step-down gets larger, not smaller.** The cut at the amortisation cliff is the amortised build leaving the cost base, and the amortised build has grown by 62%. A larger share of the cost base falls away on a single calculable date, so the step is steeper than ~32%. **Apple performs it automatically on the installed base and, on its own operational documentation, does not offer the option to preserve the higher price** — the ratchet runs one way and it now runs further.
3. **The CFO's sensitivity table has no row for this.** `pricing-ladder-model.md` §9.1 models *"+150 h build, +20 h/yr fixed"* and *"+250 h build, +40 h/yr fixed"*. **I am returning +759 h build and +140 h/yr fixed.** That is not a correction of the CFO — the table said explicitly that the increments were *"[J] increments, stated so the CTO can replace them"*, which is exactly the right way to have written it. **It is a statement that the placeholder and the estimate are in different ranges, and that Condition 1's re-derivation must therefore run again on these figures before any price is published.**

### 10.5 The disagreement I am putting in writing, once

*(Constitution 1.6 and the universal charter clause: disagreement is a deliverable.)*

**I am not disputing the decision to build Haunt.** The gate recorded a PROCEED on a stated non-commercial reason, that was the CEO's under 5.4, and `android-and-stack-note.md` §3.6 already recorded my view that *"doubling a build that was never justified commercially does not change the decision's logic; it changes its size."* **That remains my view and nothing in this note is a re-argument of it.**

**What I am putting in writing is narrower, and it is about sequence.** Since the gate, this product's scope has grown in four separate increments, in four separate documents, each of them individually reasonable and none of them re-based against the others: the Android decision (+64%), the session and venue-page inputs (unsized until today), the subscription ladder (unsized until today), and the venue-index remediation the spike made necessary (unsized until today). **The build has roughly trebled since the figure the gate looked at, and no single document has ever shown all of it in one place. This is that document.**

> **My concern, recorded once: a build estimated at 55.75 focused solo weeks is, for a part-time operator, multiple calendar years — and the five-year support commitment at Condition 9.2 starts on the launch date, not on the start date. A product that takes two calendar years to build and then carries a contractual five-year life is a seven-year commitment made in year zero, on a stack whose upgrade cadence is twice a year.**

**That is not a block and I am not dressing it as one.** It is not an architecture failing a checklist; it is a scope and sequencing judgment, and the seats that own it are the **CFO** (whose block covers uncosted launches) and the **CEO** (5.4). **The cheapest response is not to cut quality — it is to cut platform.** §9.4 item 2 shows that reverting to iOS-only removes roughly half the ongoing burden and, per `android-and-stack-note.md` §2.7, the stack rationale with it. **I raise it once, here, with the arithmetic attached, and I will not raise it again.**

---

## 11. Blocks — restated, and one new

My charter: *"Can block: Build commencement — for architectures that are unsustainable, needlessly expensive, or insecure by design. Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it — a block is a checklist item failing, never a feeling of unease."*

**Block 1 — an architecture that persists places-API venue records in the local journal.** Unchanged. **Avoided, not lifted**, by the zero-network architecture, and it re-engages on any architecture that touches a places API. Nothing in the subscription decision touches it.

**Block 2 — an Android MVP whose capture reliability rests on undocumented OEM behaviour.** Unchanged and **engaged**, per `android-and-stack-note.md` §4. Lifted by the published device-matrix spike with a pre-agreed minimum capture rate **and a measured gap-detection accuracy**.

**Block 3 — JavaScript in the visit-recording path.** Unchanged and **extended** by §3.3 of this note: the extension is that the *entitlement decision* taken at visit delivery is also in that path, and must also be a native read from the SQLite contract. *Lifted by:* a capture design in which the Swift and Kotlin modules read entitlement and write visits directly, and JavaScript reads later.

### Block 4 — NEW, pre-declared: build commencement on the venue index as specified

*Declared now, before a build is proposed, so it cannot look invented later.*

**What fails.** `decisions/2026-09-16-haunt-gate.md` **Condition 2** commissioned the spike and said *"its result may kill the product; that is the point of running it."* The spike's verdict is that the index as `feasibility-note.md` §2 specifies it is **not shippable as the venue source for a product whose core value is an accurate per-venue history** [E, Engineer, §10.1]. Two specific criteria fail:

1. **Condition 8.6** — *"Derived views never lie about the user's own life… A venue page must never show '3 visits, average 3.8' when the true figures are 11 and 4.2."* At σ = 25 m, **100% of dense-centre venues had their rank-1 candidate change across 20 simulated visits, median 10 distinct venues taking first place** [E, Engineer, §5.2]. A venue page built on that identity produces exactly the figures 8.6 forbids, and produces them *silently*, because the user chose honestly from an honest list each time.
2. **My own charter's "unsustainable by design."** With no server, no telemetry and no backfill (`feasibility-note.md` §2.6, §5), a dataset refresh that mutates a venue row already referenced by a user's visit is **permanent, silent and undiscoverable by Candour**. That is not a defect that can be fixed after ship; it is a defect that cannot be detected after ship.

**What lifts it — both limbs, and neither alone:**

- **(a)** The §8.2 remediation spike returns a **modal rank-1 share above 0.8 at σ = 25 m in a dense city centre and top-five recall above 80%**, on the Engineer's own harness and ground truth, against a pass criterion agreed with the PM/BA, UX and QA **before** the spike runs. *(Measured today: 0.27 and 51.9%.)*
- **(b)** The five acceptance criteria at `venue-index-spike.md` §9.3 — copy-on-reference; refresh may write only to unreferenced rows; changes to referenced rows offered and never applied, declining by default; user renames outrank the dataset permanently; user merges survive a re-split — are **in the requirements document and in the schema**, not in a backlog.

**What does not lift it:** a longer candidate list alone (it raises recall and makes the picker worse — the Engineer's §5.3 curve is a trade, not a fix); the category-filter rebuild alone (the Engineer's own §10.2 says its ceiling is 58% → 67% at zero noise and that it *"is not on its own sufficient"*); or a commitment to fix it post-launch, which on this architecture is not available.

**What this block is not.** It is **not** a block on the product, on the subscription, on the price or on the gate's PROCEED. **Kill/proceed is the CEO's under Constitution 5.4 and nothing here pretends otherwise.** It blocks one thing: starting the build against the index as currently specified. **The Engineer, whose charter gives it no block, flagged this to the owning seats and asked the CTO to carry it as an architectural constraint. This is me carrying it.**

---

## 12. Open questions this note did not close, and who owns them

| # | Question | Owner | Why it matters |
| --- | --- | --- | --- |
| 1 | **Whether Apple permits the 3.1.1 Price-Tier-0 trial to an app that also sells auto-renewable subscriptions.** Configure it in App Store Connect; ask App Review pre-submission | **CTO / CGO**, before the trial is specified | Decides Route A vs Route B, and with it whether the DMCCA renewal-cooling-off machinery and the unpayable proportionate refund enter the product at all (§4) |
| 2 | **Whether a local notification requires user authorization, and what the app does when it is declined.** Apple's `requestAuthorization(options:)` page returned 404 this session; tagged **[K], not retrieved** | **Engineer**, ≤1 hour | Load-bearing for R3's answer to the *"addressed personally"* limb of "durable medium" (§5.3) |
| 3 | **Whether iOS offers any API by which an app relinquishes its own location authorization.** Tagged **[K], high confidence: it does not** | **Engineer**, ≤1 hour | If I am wrong, the unpaid state can be made honest by construction rather than by instruction (§6.3) |
| 4 | **Whether `currentEntitlements` can be empty on a device that has synced but is now offline**, as distinct from one that has never synced | **Engineer**, in the field-test row | Decides how conservative the "unknown" state must be (§3.1) |
| 5 | **The pass criterion for the venue-index remediation spike** | **PM/BA with UX and QA**, before it runs | Block 4(a). A spike whose bar is set afterwards is not a test |
| 6 | **Whether to refresh the venue index quarterly rather than monthly** — a staleness-versus-cost-and-safety trade | **PM/BA and UX**, on my recommendation | 60–100 h/yr versus 45, and two thirds fewer opportunities for the §2.4 hazard to fire (§8.4) |
| 7 | **Whether the "maintained venue index" claim survives if reconciliation is cut** | **CEO**, in writing if taken | §9.4 item 1. It is the largest lever on the maintenance number and it changes what the subscription sells under Apple 3.1.2(a) |
| 8 | Carried forward, unchanged and still open: **measured battery cost** of `CLVisit` and of the Android foreground service; **which KDF** at which parameters (**CSO**); **R-Tree in `expo-sqlite`**; **install DayTrace** | As recorded at `android-and-stack-note.md` §5 | None is closed by this note and none should be assumed closed because a newer note exists |

---

## 13. Evidence register

**Every link below was retrieved on 2026-09-19 during the session that produced this note. Nothing is cited from memory.** Sources carried from `feasibility-note.md` (2026-09-09), `android-and-stack-note.md` (2026-09-16) and other seats' artifacts are cited there with their own retrieval dates and are attributed in place rather than re-claimed here.

**StoreKit 2 — on-device entitlement and renewal information**
- [Apple — `Transaction.currentEntitlements`](https://developer.apple.com/documentation/storekit/transaction/currententitlements) — *"A sequence of the latest transactions that entitle a customer…"*; non-consumables included; `subscribed` and `inGracePeriod` only; refunded and revoked products excluded
- [Apple — `Transaction.expirationDate`](https://developer.apple.com/documentation/storekit/transaction/expirationdate) — *"The date the subscription expires or renews"*; iOS 15+
- [Apple — `Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo) — `renewalDate`, `willAutoRenew`, `expirationReason`, `signedDate`, device verification
- [Apple — `Product.SubscriptionInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo) — `status`, `status(for:)`, `isEligibleForIntroOffer`, `introductoryOffer`
- [Apple — `Transaction`](https://developer.apple.com/documentation/storekit/transaction) — *"Your app doesn't create transaction objects. Instead, StoreKit automatically makes up-to-date transactions available to your app"*; `updates`, `all`, `latest`
- [Apple — `AppStore.sync()`](https://developer.apple.com/documentation/storekit/appstore/sync()) — *"In regular operations, there's no need to call AppStore.sync()… the app automatically has all transactions available to it upon initial launch"*; the authentication prompt; explicit user action only
- [Apple — `AppStore.showManageSubscriptions(in:)`](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)) — *"Presents the App Store sheet for managing subscriptions"*; iOS 15+; not supported in macOS
- [Apple Developer Forums, thread 706450](https://developer.apple.com/forums/thread/706450) — **App Store Commerce Engineer, accepted answer:** *"To get the latest transactions the device will need internet access but it does cache data locally and new transactions are pushed to the device when online, so could be up to date when it goes offline."* **This is the load-bearing citation for §3.1 and it is an Apple staff answer on an Apple property, not a blog.**

**App Store Review Guidelines**
- [Apple — App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — **3.1.1** in full, including *"Non-subscription apps may offer a free time-based trial period… Non-Consumable IAP item at Price Tier 0… 'XX-day Trial'"* and the pointer to *"Receipts and DeviceCheck"*; **3.1.2(a)** in full, including *"you must provide ongoing value to the customer"*, *"Subscriptions may be offered alongside à la carte offerings"* and *"Auto-renewable subscription apps may offer a free trial period… by providing the relevant information set forth in App Store Connect"*; **5.1.2(i)** in full, including *"Your app may not require users to enable system functionalities…"* — **confirming the UX seat's corrected citation number**
- [Apple Developer Forums, thread 678747](https://developer.apple.com/forums/thread/678747) — a developer asking *"What's the meaning of 'non-subscription apps'?"* — **0 replies**
- [Apple Developer Forums, thread 725860](https://developer.apple.com/forums/thread/725860) — a developer asking how to configure a non-consumable trial — **0 replies**
- [Apple — Set up introductory offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions/) — three offer types; *"3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year"*; *"each person is only eligible to redeem one introductory offer per subscription group"*

**DeviceCheck**
- [Apple — Accessing and modifying per-device data](https://developer.apple.com/documentation/devicecheck/accessing-and-modifying-per-device-data) — *"After you use the DCDevice class to generate an ephemeral token… **your server** uses HTTP POST commands to send requests to the query and update endpoints"*; authentication key in a JWT. **A server is required; Candour has none.**

**Platform forcing functions for maintenance (§9.3)**
- [Apple — Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) — *"Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26…"*, in force since 28 April 2026
- [Android — Target API level requirements for Google Play apps](https://developer.android.com/google/play/requirements/target-sdk) — from 31 August 2026, new apps and updates must target API 36+; *"Existing apps must target Android 15 (API level 35) or higher to remain available to new users…"*; extension to 1 November 2026
- [Expo — Changelog](https://expo.dev/changelog) — SDK 56 (2026-05-21), SDK 57 (2026-06-30), SDK 58 beta (2026-09-15)

**Candour artifacts read from disk this session, in full**
`constitution.md` v1.2 (Definitions; Articles 1, 2.1, 2.3, 3, 4, 5.2, 5.4, 5.6, 6.1, 7.2, 9, 10, 11); `roles/cto.md` as amended; `pipeline/evidence-standard.md` v1.1; `decisions/2026-09-16-haunt-gate.md` in full including Conditions 1–10 as amended and Corrections C1–C4; `products/haunt/venue-index-spike.md` in full; `products/haunt/feasibility-note.md` in full; `products/haunt/android-and-stack-note.md` in full; `products/haunt/subscription-compliance-note.md` in full; `products/haunt/ux-note-pricing.md` §§1–2 and §9; `products/haunt/pricing-ladder-model.md` §§8–9 and §12; `proposals/haunt/ceo-product-inputs.md` in full.

**Looked for and did not find**
- **Any retrievable example of an iOS app shipping both auto-renewable subscriptions and a Price-Tier-0 "XX-day Trial" non-consumable**, and equally **any retrievable rejection for doing so**. A search-engine summary asserted a prohibition; **it is not cited, because it carries no source and citing it would be fabrication under `pipeline/evidence-standard.md`.**
- **Any Apple statement on whether `currentEntitlements` is populated on a device that has synced and is now offline**, as distinct from one that has never synced.
- **Any published Expo SDK support-window policy** stating how long EAS supports an older SDK.
- **Any published benchmark for solo-operator annual maintenance hours** against which §9's estimate could be tested. **This is the largest weakness in this note and it is named at §9.4.**

**Related-party disclosures.** None. Nothing in this note contemplates a payment to the founder, family or any affiliated entity.

---

## 14. Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | Created under **Condition 9.8(b)**. Sizes the subscription-mechanics increment and answers the maintenance question: **220 h/yr does not hold to year five; the revised figure is 288–441, point 360.** Returns **one revised build total of 1,770–2,410 hours, point 2,090**, plus 188 hours of separately-carried pre-build spikes, with the unit stated. **Closes the CGO's flag F2** on on-device renewal dates, at source. **Confirms the CVO's derived-sessions constraint with one amendment** (overrides, entitlement intervals and capture-gap records must be durable rows). **Confirms the proportionate-refund duty out of scope of any build estimate** and leaves it at launch bar L1. **Concedes the venue spike's finding that the 346,184 food-and-drink figure is unre-derivable and corrects `feasibility-note.md` §2.3 to 302,820.** **Corrects `ux-note-pricing.md` §2.6's first reason** — Route B's trial start is recoverable from the non-consumable's own `purchaseDate` and needs no covert identifier. **Records a negative finding on the 3.1.1 trial as a permission question rather than a capability question**, with what would overturn it and where I looked. **Pre-declares Block 4** on the venue index as specified. **Records one disagreement, on scope sequencing, once.** External sources retrieved 2026-09-19. **Not a certification.** |

---

*Prepared by the CTO seat under `roles/cto.md`. This note prepares and flags; it does not certify (Constitution 6.1). Price is the CEO's under 5.4 and the cost model is the CFO's under Condition 1; every figure here is an input to their work and none of it is a price. Condition 6 requires the arithmetic above to be re-derived by a seat other than its author before it anchors anything.*

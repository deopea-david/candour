# Window conversion model and re-derived cost model — Haunt

**Seat:** Chief Financial Officer · **Date:** 2026-09-17
**Commissioned by:** the open item at the foot of `decisions/2026-09-16-haunt-gate.md` — *"Still open after C2… C1-O5: no conversion model exists for the visibility window… **Owner: CEO and CFO, at the pricing decision that Condition 9 already reserves.**"*
**Also discharges:** Condition 1 of that record (re-derivation on CTO hours; O10 sensitivity arithmetic; O11 support reconciliation; O12 margin relabelling; ICO annual charge).

**Status: not a published cost sheet, and not a price.** Two bars stand between this document and Article 3 publication, and both are named in §7. Under Constitution 5.4 the price is the CEO's; under Condition 9 of the decision record it is not available until this work is done. This document is that work; it is not the decision.

**Supersedes** the tables in `products/haunt/cost-sheet.md` §§3–10 in their entirety. That document ran every figure on 450 build hours and on iOS only. Both premises are gone. Its §2 (retrieved input prices) and §11 (related-party disclosures) survive; its §2.2–§2.3 places-API material is **moot**, because the zero-network architecture removed the meter. A correction banner is owed on that file and is listed in §7.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Every price and benchmark below was retrieved on **2026-09-17** during the session that produced this note, except where a retrieval date is given for an earlier session. Nothing external is cited from memory. Every constitutional claim quotes the clause it relies on, in the same passage, per that standard's *"Claims about our own rules"*.

---

## 0. The answers, before the arithmetic

1. **C1-O5 holds. The visibility window is commercially inert, and the arithmetic is not close.** At any one-off unlock price between £15 and £30, the free tier's break-even conversion rate has an **asymptotic floor of 4.9%–11.4%** — the rate it needs *even if the free tier were to buy infinite extra reach* — because free users cost real support labour and the architecture has no zero-marginal-cost to hide behind. At a plausible reach multiple of 3–5× it needs **24%–41%**. The retrieved industry median for freemium download-to-paid is **2.1%** [E]. The window is short by a factor of between 2 and 20, and that is before any of Conditions 8.1–8.6 are applied. Applying them takes the achievable rate *down*, not up. §1.

2. **Every clause the CEO adopted to make the window honest is a clause that makes it convert less.** 8.5 lets the engaged user keep everything free and uncapped; 8.4 forbids telling anyone the window is coming; 8.3 hands the unconverted user a complete free export; 8.6 keeps the aggregates honest so there is less to lose. This is not a criticism of those clauses — they are right. It is the finding: **the compliant version of this mechanism and the commercial version of it are different mechanisms.** §1.5.

3. **Two of the Skeptic's three relocation routes remain open**, and one of them is open in a way nobody has noticed: 8.2's ratchet as clarified binds *tightening after launch*, but nothing binds *narrowness at launch*. And 8.2's ratchet is a one-way valve that can only ever make the window weaker, never stronger — so the mechanism's permitted evolution runs entirely against its own commercial purpose. §2.

4. **The re-derivation moves the numbers by roughly 4×, not 70%.** On the CTO's 1,330 build hours plus the 75-hour Android spike, two platforms, with variable support solved as the fixed point the CTO asked for, break-even at £14.99 is **~10,600 sales over three years**, against the **~2,400–2,700** recorded in the decision record the CEO signed. The CTO's own order-of-magnitude indication (~7,100) reproduces exactly once variable support is excluded; adding it back is the other 50%. §3.6.

5. **Subscription breaches Article 2.1's new cumulative test at a tenure of about four years** — not the seven the CEO's product-inputs note estimated — and it does so while every individual financial year is compliant. The breach point is structural: **amortisation period plus roughly one year, at every scale I modelled.** It is also entirely fixable, by one act Candour is already required to perform. §4.

6. **My recommendation is that Haunt ships with no free tier, no visibility window and no subscription.** That is a finding, not a failure of imagination, and §5 states what would overturn it and where I looked. I also name one alternative shape the retrieved data supports and that nobody in this pipeline has modelled: a **free download behind a hard paywall**, which converts at 10.7% against freemium's 2.1% [E] and contains no read-cap of any kind. It is not mine to approve — it changes the shape Condition 9 records as decided, and it has an Article 4 question attached that belongs to UX and the CGO. §5.3.

---

## 1. What the window is for, in numbers

### 1.1 The question, stated as something arithmetic can answer

The Skeptic's objection is that nobody has said what the window is *for*. The commercial claim implicit in any free tier is a single proposition:

> *Giving the product away to more people, and converting some of them, produces more contribution than selling it to fewer people at a price.*

That proposition has exactly two unknowns: the **reach multiple** the free tier buys (call it *r* — how many free installs you get for each sale you would otherwise have made) and the **conversion rate** (*c*). Everything else is cost, and the cost is now known. So the honest form of C1-O5's question is: **given r, what c does the free tier need to break even against a plain one-off purchase?**

I answer that, then ask what *c* the window can structurally deliver, then compare. The two numbers do not meet.

### 1.2 The break-even conversion rate

Definitions, all from §3 below:

| Symbol | Meaning | Value |
|---|---|---|
| *p* | Net proceeds per sale = shelf ÷ 1.20 × 0.85 | 0.70833 × shelf |
| *S_paid* | Support cost of a paying user over the supported life | **£3.459** |
| *S_free* | Support cost of a non-converting free user over the supported life | **£0.922** |
| *m* | Net contribution per paying user = *p* − *S_paid* | varies with price |
| *r* | Free installs per foregone paid sale | **unknown — see 1.3** |

Setting the two designs' contribution equal and solving for *c*:

```
c*  =  ( m + r·S_free )  /  ( r · ( m + S_free ) )
```

Two sanity checks before the table. At *r* = 1 (the free tier buys no extra reach at all) the formula returns *c* = 100%, which is right — every free user who would have bought and now does not is pure loss. And if free users were costless (*S_free* = 0), the formula collapses to *c* = 1/*r*, the familiar freemium rule of thumb. **Haunt's free users are not costless**, and that is what makes the rest of this section come out the way it does.

**Break-even conversion rate, by unlock price and reach multiple:**

| Shelf price (inc. VAT) | *r* = 2 | *r* = 3 | *r* = 5 | *r* = 10 | *r* = 20 | *r* → ∞ (the floor) |
|---|---|---|---|---|---|---|
| £9.99 | 60.2% | 46.9% | 36.3% | 28.3% | 24.3% | **20.3%** |
| £14.99 | 55.7% | 40.9% | 29.1% | 20.3% | 15.8% | **11.4%** |
| £19.99 | 54.0% | 38.6% | 26.3% | 17.1% | 12.5% | **7.9%** |
| £24.99 | 53.0% | 37.4% | 24.9% | 15.5% | 10.8% | **6.1%** |
| £29.99 | 52.5% | 36.6% | 23.9% | 14.4% | 9.7% | **4.9%** |
| £49.99 | 51.4% | 35.2% | 22.2% | 12.5% | 7.7% | **2.8%** |

### 1.3 The floor is the finding, and it is a structural property of this architecture

Notice the last column. As *r* → ∞ the expression tends to `S_free / (m + S_free)` — a **hard floor** below which the break-even conversion rate cannot fall however much reach the free tier buys. At £14.99 that floor is **11.4%**. At £29.99 it is **4.9%**.

The floor exists because a free Haunt user is not free. On a server-backed SaaS product the classic freemium argument is that free users cost fractions of a penny, so the break-even conversion rate is essentially 1/*r* and any reach uplift pays for itself. **Haunt has no server, so it has no fractions of a penny.** Its marginal cost per user is a human being answering an email about a background-location failure on a device Candour does not have, blind, with no telemetry — at £0.615 per free user per year blended across platforms (§3.3). That is the single most counter-intuitive number in this analysis and it was already in the cost sheet at §8.1, where it was attributed to the metered places API. The API is gone. **The finding survived the architecture that produced it**, because it was never really about the API.

**What *r* actually is, nobody knows, and that is itself a finding.** No seat has produced any evidence for the reach multiple a free Haunt tier would buy. The gate pack does not contain one; the research brief does not contain one; the CEO's product inputs do not contain one. The entire commercial case for a free tier rests on a number that has never been written down anywhere in this pipeline. I am not going to invent it. What I can say is that the answer does not depend on it: **the floor row holds for every value of *r*.**

### 1.4 What the window can structurally deliver

Against a break-even of 4.9%–11.4% at best:

**The retrieved benchmark.** Median download-to-paid conversion at day 35 is **2.1% for freemium apps and 10.7% for hard-paywall apps** — "Hard paywalls convert 5x better than freemium (10.7% vs. 2.1%)" [E, [RevenueCat, State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/), retrieved 2026-09-17; **single source**, and it is a subscription-app dataset, so it does not cover paid-up-front listings at all — flagged]. The prior year's edition reports 2.18% and 12.11% on the same split [E, [RevenueCat 2025](https://www.revenuecat.com/state-of-subscription-apps-2025/), retrieved 2026-09-17] — **same origin, therefore one source, not two**, per the independence rule in `pipeline/evidence-standard.md`.

**Haunt's free tier would sit at the bottom of that distribution, not the middle**, for three reasons that are specific to it and all point the same way. It has no acquisition channel (idea brief objection 6). It has no telemetry, so it cannot find, segment or target the users who are close to converting — the entire apparatus by which freemium products lift 2.1% toward 10%. And its conversion event is *paying to un-hide things the user already wrote*, against a product that hands them a complete free export on request under 8.3.

**But the decisive argument needs no benchmark at all.** Write the window's own conversion as a product of three shares of the free base:

```
c_window  =  R(N)  ×  (1 − f)  ×  k
```

- **R(N)** — the share of the free base still using Haunt when the window bites at month *N*. This is a ceiling nothing can raise: a user who has stopped opening the app cannot be converted by something that happens inside it.
- **f** — the share of surviving users who have favourited comprehensively. **Condition 8.5** guarantees that *"any entry the user can currently see can be marked to keep"* and **Condition 8.4** guarantees *"no cap on how many entries may be marked."* For a user engaged enough to still be present at month *N*, *f* is high by construction. Every such user the window would have converted, 8.5 has already excused.
- **k** — the share of the remainder who notice, and who prefer paying to exporting. **Condition 8.4** forbids *"no countdown UI, no expiry notifications, no streaks, no badges, no 'N memories expiring' prompts"* and requires that *"the window passes silently"*; the C1-O11 clarification permits only *"static, in-context disclosure."* **Condition 8.3** gives the alternative away: *"Export always contains **every** entry — aged-out, unfavourited and unpaid alike — free, immediate, machine-readable, in every tier."*

Now the retention ceiling. Retrieved day-30 retention benchmarks: **median 4% across all categories**, with strong performers at **5–8%**; the closest adjacent categories are Productivity (median 8%, strong 12–18%) and Health/Fitness (median 5%, strong 8–12%) [E, [UXCam, Mobile App Retention Benchmarks](https://uxcam.com/blog/mobile-app-retention-benchmarks/), retrieved 2026-09-17, citing AppsFlyer *State of App Marketing 2025*, Adjust *Mobile App Trends 2026* and data.ai *State of Mobile 2026*; **single retrieved page**, though it aggregates three underlying datasets — I did not retrieve those three at source and do not claim to have]. Month-12 retention is not published on that page; retention curves flatten but do not rise, so **R(12 months) ≤ R(30 days)** is a safe bound and the only one I need [I, from the [E] above].

**Put the bound together.** For a 12-month window to clear even the most generous break-even — the 4.9% infinite-reach floor at a £29.99 unlock — you need:

```
R(12mo) × (1 − f) × k  ≥  0.049
```

with R(12mo) ≤ 0.08 even for a strong performer in an adjacent category. That requires *f* ≈ 0 and *k* ≈ 1 **simultaneously**: nobody favourites anything, and everybody who loses something pays rather than exports. Conditions 8.5 and 8.3 exist precisely to make those two things false.

At a realistic reach multiple the arithmetic is not close. At £29.99 and *r* = 5 the requirement is **23.9%** against a ceiling of **8%**, and the ceiling assumes *f* = 0 and *k* = 1.

### 1.5 Verdict on C1-O5

> **The objection holds. The visibility window, as governed by Conditions 8.1–8.6, is commercially inert. It cannot clear its own break-even at any window length, any price in the plausible band, and any reach multiple including an infinite one.**

The Skeptic's compositional argument — engaged users keep everything free, disengaged users never notice, so the mechanism collects from neither — is correct, and the arithmetic adds a third finding the memo did not have: **even the middle band it identified is capped by a retention ceiling that no design can lift**, because the window's only possible victims are users still present months after install, and that is a small number in every category anyone measures.

The memo asked to be shown a model rather than be right. This is the model. It says the memo is right.

**The corollary that matters more than the verdict.** C1-O5 offered an alternative to a conversion model: *"or an explicit statement that the window is not a conversion mechanism, in which case the record should say what it is for."* On this arithmetic that is now the only available answer, and it is not a comfortable one, because the window has no other purpose. It does not reduce cost — there is no meter (§3.4). It does not improve the product; Condition 8.6 exists specifically to stop it degrading the product. It adds an Article 4 surface, six binding acceptance criteria, a permission-tier complication in the capture flow, and a class of support case ("where did my entries go?") that the paid product does not have. **A mechanism with a cost and no benefit is not a pricing question; it is scope to delete.**

---

## 2. Where the pressure relocates if the window is inert

The Skeptic named three routes. One is now closed. I take them in order, then make the point that matters more than any of them.

### 2.1 Route 1 — friction on the favouriting gesture. **OPEN.**

Condition 8.4 as clarified on 2026-09-17 draws its line at interruption: *"What 8.4 forbids is **interruption and urgency**: anything that reaches for the user's attention, or counts down."* Condition 8.5 requires only that *"any entry the user can currently see **can** be marked to keep."*

Neither reaches interaction cost. A keep-gesture buried four taps deep inside an overflow menu, offered one entry at a time with no bulk action, satisfies 8.5 on its face and deploys none of 8.4's named mechanics. It would also be the single most effective thing anyone could do to raise *f* → low and therefore raise conversion, which is exactly why it is the route pressure takes first.

**Constitutional cost, with the clause quoted.** Article 4 requires *"no dark patterns: no false urgency, no confirm-shaming, no pre-ticked boxes, no deliberately buried settings, no engagement mechanics designed to exploit compulsion."* A keep-gesture made deliberately expensive is a **deliberately buried setting** in function if not in form, and it is an engagement mechanic in the precise sense the clause names: a design whose purpose is to make the user's own effort the currency.

**This is not my block and I say so.** Per my charter as amended — *"You may **block** only on the grounds your charter names"* — Article 4 is outside the CFO's blocking scope, which covers *"unpriced or uncosted launches"* (Constitution 5.6). **The seat that holds it is UX**, and the decision record already says so at C2.6: the UX seat's B2 release block *"engages on any design breaching Article 4 or Conditions 8.1–8.6 — expressly including friction placed on the keep-gesture."* I record this as a **flag** with the arithmetic attached, so that when it is proposed the seat that can stop it already has the number showing why it was proposed.

### 2.2 Route 2 — the definition of "visible". **PARTLY OPEN, and the open half is the one nobody has noticed.**

Condition 8.2 as clarified on 2026-09-17 (C1-O12) now states: *"the ratchet binds the window's **scope as well as its number.** Holding '12 months' constant while redefining what falls inside it — what counts as an entry, as visible, or as within the window — is a tightening, and is forbidden on the same terms as shortening the number."*

That closes narrowing **after** launch. It says nothing about narrowness **at** launch, and it cannot: a ratchet has to start somewhere, and wherever it starts is where it locks. So the pressure does not have to wait eighteen months. It can be applied once, in the requirements document, by whoever writes the sentence defining what "visible" means — and once written, 8.2 makes that definition permanent and unchallengeable, which is a protection running in the wrong direction.

**Constitutional cost.** Article 1.3 — *"**Honest by default.** Pricing, capability, and limitations are stated plainly. We say what a product cannot do."* — and Condition 8.1's requirement that *"the limit, the window, and what happens at its end are stated in plain language… before the user writes anything."* A definition of "visible" narrow enough to convert is a definition that is hard to state in plain language in a store listing, and the plain-language test is the practical check on it.

**What would close it, and it is cheap:** the requirements document defines "visible" **once, exhaustively and affirmatively** — search results, venue pages, map pins, session summaries, exports, aggregates — rather than by exclusion, and 8.2's ratchet then locks a definition that was written in the open rather than assembled by omission. That is a PM/BA instruction, not a new condition, and it costs a paragraph.

### 2.3 Route 3 — the derived and aggregate layer. **CLOSED.**

Condition 8.6 closes it, and closes it properly: *"Aggregate and derived views… compute over the **complete** set of the user's entries, or state plainly on their face that they are partial. **Ratings and notes attached to hidden sessions still count.**"* I have no residual concern and record that as a clean pass. The clause was the Skeptic's and it is the most valuable single sentence in Condition 8.

There is a cost consequence worth naming since no one has: **8.6 makes the window strictly more expensive to build than no window at all.** Every aggregate query must carry two result sets or a partiality banner, on a schema where sessions are derived rather than stored (per `proposals/haunt/ceo-product-inputs.md` §2). The CTO's 1,330 hours do not contain a line for it, because the window was not in scope when the decomposition was written. **Deleting the window therefore returns hours; it does not merely avoid adding them.** I have not attempted to size that and it is the CTO's to size, but it should not be assumed to be zero.

### 2.4 The point that outranks the three routes

> **A mechanism that only works when someone degrades it is an argument against having the mechanism.**

The arithmetic in §1 and the audit in §2.1–2.3 compose into one statement: **the compliant window converts nobody, and the versions that convert are the versions Candour has pre-committed not to ship.** Building it anyway does not produce a revenue mechanism. It produces a *standing temptation* with revenue attached — a piece of shipped machinery whose only remaining use is the use that is forbidden, sitting in the codebase for the whole of the product's life, requiring nothing but a single sentence in a future requirements document to activate.

Article 9 is the clause that speaks to this. It commits: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* The vector here is not in the Article 9 table, and it is general rather than specific to Haunt: **shipping a compliant mechanism whose non-compliant variant is a one-line change, and whose compliant variant has no commercial purpose.** The honest disposal of it is not a new condition policing the variant. It is not shipping the mechanism.

**And a sequencing point the CEO should hold onto.** The Skeptic wrote that this pipeline's Candour of eighteen months' time *"inherits a rulebook whose hard edges are export (8.3) and the ratchet (8.2)… and whose soft edges are everything C1-O4, C1-O5, C1-O11 and C1-O12 identify."* The moment the soft edges are tested is the moment revenue is needed, which is the moment the arithmetic in §1 will be rediscovered by someone under pressure, who will reach the same conclusion I have — that the window cannot pay — and will then have exactly two options. One is deleting a shipped feature. The other is Route 1. **Deleting it now costs nothing; deleting it then costs a feature and an argument.**

---

## 3. Re-derivation on the CTO's hours — Condition 1

Condition 1 requires that *"the cost model is re-derived by the CFO on the CTO's build hours (O2), reconciling the two support bases (O11), correcting the §5 sensitivity arithmetic (O10), relabelling the margin as a justified deviation (O12), and adding the **ICO annual charge** the CGO found missing from the £83/year fixed cost."* All five are below. **§1 of this document does not rest on §3** — the break-even conversion rates move with price, and §1's floor row and retention ceiling hold at every price in the band — but Condition 1 is owed regardless and is discharged here.

### 3.1 Retrieved inputs

All retrieved **2026-09-17** unless stated.

| Item | Figure | Tag |
|---|---|---|
| GBP/USD spot, 16 Sept 2026 | **1.33821** ("The GBP/USD exchange rate fell to 1.3380 on September 16, 2026") | [E] [tradingeconomics.com](https://tradingeconomics.com/united-kingdom/currency) |
| Apple Developer Program membership | **$99/year** | [E] [developer.apple.com/programs](https://developer.apple.com/programs/) |
| Google Play developer registration | **"US$25 one-time registration fee"** — retrieved from **Google's own support page**, not a secondary source | [E] [support.google.com](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en) |
| ICO data protection fee, Tier 1 (micro organisations) | **£52/year**; *"You have a maximum turnover of £632,000… or no more than 10 members of staff"*; *"If you choose to pay your fee by direct debit, you will receive an automatic discount of £5"* → **£47 by direct debit** | [E] [ico.org.uk](https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/) |
| ICO fee exemptions | Exempt only if processing is **solely** for: staff administration; advertising, marketing and PR; accounts and records; not-for-profit purposes; personal/family/household affairs; public register; judicial functions; or without automated systems | [E] [ico.org.uk/…/exemptions](https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/exemptions/) |
| Apple App Store Small Business Program commission | 15% for developers up to $1m prior-year proceeds | [E, retrieved 2026-09-09, carried forward] [developer.apple.com](https://developer.apple.com/app-store/small-business-program/) |
| Google Play service fee, UK, from 30 June 2026, new installs | 10% service + 5% billing on first $1m annually | [E, retrieved 2026-09-09, carried forward] [support.google.com](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) |
| UK standard VAT | 20% | [E, retrieved 2026-09-09, carried forward] [gov.uk](https://www.gov.uk/vat-rates) |
| Expo EAS free tier | $0/month, 15 iOS + 15 Android builds, EAS Submit included | [E, retrieved by CTO 2026-09-16] [expo.dev/pricing](https://expo.dev/pricing) |

**Two flags carried forward unchanged, both load-bearing, both twice-flagged already.** Under `pipeline/evidence-standard.md` — *"**Twice-flagged is escalated.** A load-bearing claim flagged as unverified on two separate occasions must be resolved, or formally accepted in writing by the CEO, before it may anchor a third artifact"* — this is that third artifact for both, and I state the position rather than flagging a fourth time:

1. **The £32.71/hour labour benchmark.** I attempted the primary ONS retrieval again this session and **failed again**: the ASHE bulletin for April 2025 provisional (published 23 October 2025) confirms the release and reference period but carries the occupational breakdown in a linked spreadsheet the tooling cannot open [E, [ONS ASHE latest bulletin](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/latest), retrieved 2026-09-17]. Condition 5 stands unclosed. **Consequence, stated as my charter's blocking ground rather than as a preference: no figure in this document may be published under Article 3 until it closes**, and if it never closes the benchmark must be replaced with one that can be retrieved. Every number below scales linearly with it.
2. **Apple's UK merchant-of-record / VAT position.** Still unconfirmed on an Apple page. It moves every shelf price by 20%. Ex-VAT and shelf figures are shown separately throughout so the reader can see precisely which number the assumption moves.

### 3.2 Build labour — the O2 correction

The cost sheet ran every table on **450 hours, iOS only**. Both premises are superseded: the CEO has directed Android into scope, and the CTO has produced an engineering estimate. The figure the CTO asks me to use [E, `products/haunt/android-and-stack-note.md` §3.1, retrieved from disk 2026-09-17]:

> *"Two-platform React Native / Expo build: 1,160–1,500 hours. Point estimate 1,330 hours. Plus 75 hours (2 focused weeks) for the Android capture-reliability spike required by Block 2 — carried as a separate pre-build line, because it may return 'don't build.'"*

At 37.5 h/week, and at the £32.71/hour benchmark:

| | Hours | At £32.71 |
|---|---|---|
| Build, low | 1,160 | £37,943.60 |
| **Build, point estimate** | **1,330** | **£43,504.30** |
| Build, high | 1,500 | £49,065.00 |
| Android capture-reliability spike (Block 2) | 75 | £2,453.25 |
| **Capitalised total, point estimate** | **1,405** | **£45,957.55** |
| *Capitalised total, range* | *1,235–1,575* | *£40,396.85–£51,518.25* |

**I carry the spike inside the capitalised figure and say why, because the CTO asked for it outside.** His reason is sound — it may return "don't build", and a spike that kills the product should not be buried in a build line. But for the purpose of *pricing a product that ships*, the spike is money spent to ship it and a customer's honest price includes it. Both treatments appear above so the reader can take either. If the spike returns "don't", the £2,453 is written off under Article 7.2's closing cost sheet, not recovered from anyone.

**The amortisation treatment, and a new obligation on Candour that comes with it.** Constitution v1.2 Definitions now settle what the cost sheet left open: *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year… Three conditions bind that treatment: the amortisation period must equal a **published** support commitment to customers; any unamortised remainder is written off publicly on discontinuation (7.2); and the period may be shortened, never lengthened. **Absent a published support commitment, build labour is a first-year operating cost.**"*

Every figure below amortises over **three years**. That is only lawful under the clause above if Candour **publishes a three-year support commitment**. It has not. So: **a three-year support commitment for Haunt is now a prerequisite of this cost model, not a nicety** — and if the CEO will not publish one, the correct treatment reverts to charging the entire £45,957.55 to year one, which would put the honest first-year price out of any plausible market. I recommend the commitment be published, product-level and dated ("Haunt is supported until [launch + 3 years]"), for three reasons: it is what the Constitution now requires in exchange for the treatment; it is the honest answer to the UX seat's §6.1 warning against the word "lifetime"; and it bounds the support liability in §3.3, which would otherwise run past the revenue.

### 3.3 Support and maintenance — the O11 reconciliation

The Skeptic found the CTO and me modelling support on incompatible bases. The CTO conceded the ambiguity and gave his half [E, `android-and-stack-note.md` §3.4]: *"my '~2 hours/week' was a fixed founder-attention floor, and the CFO's contact-rate model is a variable per-user cost. They are different things and **they add**. Neither replaces the other."*

**I accept that reconciliation in full, and it is the right one.** The two figures were never alternatives. Below is the joint basis, which supersedes both originals.

**Fixed, independent of user count:**

| Item | Hours/year | At £32.71 | Source |
|---|---|---|---|
| Maintenance, two platforms, React Native (point estimate; range 195–247) | **220** | **£7,196.20** | CTO §3.4 [J] |
| Support floor — inbox, store and policy churn, reproducing reports, diagnostic-bundle loop | **78** | **£2,551.38** | CTO §3.4 [J] |
| **Total fixed labour** | **298** | **£9,747.58/yr** | |

**Variable, per user per year:**

| Basis | Hours/user/yr | At £32.71 | Source |
|---|---|---|---|
| iOS paying — 5% contact rate × 45 min | 0.0375 | **£1.2266** | CFO original, accepted by CTO |
| **Android paying — 12% × 60 min** | 0.1200 | **£3.9252** | **CTO §3.4 amendment** [J] |
| iOS free — 2% × 30 min | 0.0100 | **£0.3271** | CFO original |
| Android free — scaled on the same 3.2× multiple the CTO applied to paying users | 0.0320 | **£1.0467** | [I, from the CTO's [J]] |

**Platform mix.** Blended figures below use **60% iOS / 40% Android** [J]. I have no evidence for this split and I am not going to pretend to; it is a judgment, it is stated so it can be argued with, and §3.6 shows what moves if it is wrong. Blended: **paying £2.3060/user/yr; free £0.6150/user/yr.**

**The Android support rate is the largest single change in this re-derivation after the build hours, and it deserves to be seen on its own.** At 12% × 60 minutes, an Android buyer costs **£3.93 a year** in support. At a £14.99 shelf price the net proceeds of that sale are £10.62. **Three years of support for one Android buyer is £11.78 — more than the entire net proceeds of their purchase.** That is not a rounding item; on a per-customer three-year commitment it makes Android buyers loss-making at £14.99 outright, and it is the arithmetic reason §3.2 recommends a product-level rather than per-customer support commitment.

**Exposure window.** Under a product-level three-year commitment with sales arriving uniformly across it, the average buyer receives **1.5 years** of support inside the window. So:

- **S_paid** (a buyer, over the supported life) = 1.5 × £2.3060 = **£3.459**
- **S_free** (a non-converting free user) = 1.5 × £0.6149 = **£0.922**

These are the values §1 uses. Under the alternative reading — three years of support *per customer from their purchase date* — both double, break-even volumes rise by roughly 35%, and support costs continue for two years after the amortisation window has closed and revenue has stopped. **Which reading governs is a CEO decision and it is not cosmetic**, because the Definitions now tie the amortisation period to the published commitment. I recommend the product-level reading and §3.2 says why.

**A cost I have not included, and am naming rather than burying:** a visibility window generates its own support category — *"where did my entries go?"* — that a plain purchase does not. It would raise *S_free* specifically, and therefore raise every break-even conversion rate in §1.2 above what is shown. I have not sized it. **The omission errs in the window's favour**, which is the direction an honest omission should err in a document recommending against it.

### 3.4 Fixed non-labour costs, including the ICO charge the CGO found missing

| Item | Cost | Notes |
|---|---|---|
| Hosting | **£0.00** | No server. Structural, not disciplinary. |
| Database | **£0.00** | All state on the user's device. |
| Places / venue API | **£0.00** | **The entire metered-API analysis in `cost-sheet.md` §2.2–§2.3, §4.2 and §5 is moot.** The zero-network architecture with a bundled Overture dataset removed the meter, and with it the heavy-user adverse-selection problem, the unbounded per-read liability, and the reason the old §5 had four columns. |
| Apple Developer Program | **£73.98/yr** | $99 ÷ 1.33821 [E] |
| Google Play registration | **£18.68 one-off** | $25 ÷ 1.33821 [E]. **CTO open question 7 is closed**: retrieved from Google's own page, not the secondary source the CTO flagged. |
| **ICO data protection fee, Tier 1** | **£52.00/yr** | [E]. £47 by direct debit; I carry £52 as the prudent figure. **See the finding below.** |
| Domain + static landing/support page | **~£10/yr** [J] | .com renewal still not retrieved; immaterial at <0.02% of total. |
| Crash/analytics tooling | **£0.00** | Deliberately absent (Article 4 data minimisation). The cost reappears as support labour in §3.3. |
| Expo EAS | **£0.00** | Free tier sufficient [E, CTO §2.4]. Contingency: Starter at $19/month = **£170.38/yr** if monthly builds exceed 15 per platform. Not a line item; a named trigger. |
| **Total fixed recurring** | **£135.98/yr** | vs. the £83/yr the old sheet carried |

**Finding on the ICO charge, which is not simply "add £52".** The CGO is right that the old £83 figure omitted it, and it is added. But whether Haunt owes it is genuinely open, and I have retrieved the clause rather than assuming. The ICO exempts organisations processing personal data **solely** for a closed list of purposes including *"accounts and records"* and *"advertising, marketing and public relations"* [E, retrieved above]. On the zero-network architecture Candour holds no journal data at all — the CGO's own gate finding is that *"on this architecture Candour is neither controller nor processor of journal data"* [E, `decisions/2026-09-16-haunt-gate.md`, retrieved from disk]. Apple and Google are merchants of record, so Candour may not even hold customer payment details. **What is left is the support inbox**, which receives user-written descriptions of failures and is very unlikely to stay inside "accounts and records".

So the honest position: **the fee is probably owed, on account of the support inbox rather than the product**, I carry it at £52, and **the determination belongs to the CGO, not to me.** I flag one thing so nobody spends money resolving it: at £52 against a three-year cost base of £75,627, this is **0.2%**. It is not worth an hour of anyone's time to be right about, and I record that plainly rather than performing diligence proportionate to nothing.

**A second finding the CGO's correction surfaced, which is larger than the £52 and which no seat has raised.** Both the Apple Developer Program fee and the ICO charge are **company** costs, not Haunt costs. Constitution 2.1: *"Margins are per product, never averaged across the portfolio: each product's customers get that product's honest number, and no customer subsidises another product unknowingly."* That clause protects against cross-subsidy in one direction; the mirror problem is charging one product 100% of a cost that will serve several. Article 9's first named loophole is *"Inflating costs to raise the allowable price (2.1)."* **Allocating the whole of a shared fee to the only product that exists today is that loophole running by default rather than by intent** — and it becomes a live overcharge the moment Candour ships a second app, because the price set today does not come back down on its own. I recommend the CEO settle the allocation rule **now**, while it costs nothing to settle: my proposal is that shared fees are split equally across live products at each annual republication, with Haunt carrying 100% while it is alone and its cost sheet saying so on its face. That is one sentence in the requirements document and it forecloses the vector before it opens.

### 3.5 Three-year cost base, and the honest one-off price

**Pricing arithmetic, stated so a second seat can re-derive it (Condition 6):**
- Store commission is a **cost of sale passed through at zero markup**: `ex-VAT price = (other costs × 1.20) ÷ 0.85`
- `shelf price = ex-VAT × 1.20`, so `shelf = other costs × 1.694118`
- `net proceeds per sale = shelf ÷ 1.20 × 0.85 = shelf × 0.708333`
- Check: 1.694118 × 0.708333 = 1.2000 exactly.

**Three-year fixed cost (F), two platforms:**

| Component | Point estimate | Low | High |
|---|---|---|---|
| Build + spike (capitalised, amortised over 3 yrs) | £45,957.55 | £40,396.85 | £51,518.25 |
| Fixed labour × 3 yrs (maintenance + support floor) | £29,242.74 | £26,789.49 | £31,892.25 |
| Fixed non-labour × 3 yrs | £407.94 | £407.94 | £407.94 |
| Google Play registration (one-off) | £18.68 | £18.68 | £18.68 |
| **F** | **£75,626.91** | **£67,612.96** | **£83,837.12** |

*Reconciliation with the CTO's own indication:* he computed £75,200 for build + spike + fixed maintenance + fixed support at the same rate [E, §3.6 of his note]. My £75,627 is his figure plus £427 of fixed non-labour he did not carry. **It reproduces.**

**Honest one-off shelf price, by cohort size,** at cost + 20% with commission passed through, `cost per buyer = F/B + S_paid`:

| Buyers over 3 yrs (B) | Cost per buyer | Ex-VAT price | **Shelf (inc. VAT)** |
|---|---|---|---|
| 250 | £305.97 | £431.95 | **£518.34** |
| 1,000 | £79.09 | £111.65 | **£133.97** |
| 2,500 | £33.71 | £47.59 | **£57.11** |
| 5,000 | £18.58 | £26.24 | **£31.48** |
| 10,000 | £11.02 | £15.56 | **£18.67** |
| 25,000 | £6.48 | £9.15 | **£10.98** |
| **Floor (infinite buyers)** | **£3.46** | **£4.88** | **£5.86** |

The floor row is no longer the finding it was in the old §5 — with the API meter gone, the floor is only support labour, and it is comfortable. **The finding has moved to the top of the table.** At any cohort Candour has evidence for, the honest price is not a consumer app-store price. The old sheet's comparable figure at 5,000 buyers on the offline index was £14.63; it is now **£31.48**, and that is the whole consequence of Android plus the CTO's real hours.

### 3.6 Break-even volume, solved as the fixed point the CTO asked for

The CTO flagged the trap [E, §3.4]: *"variable support scales with sales, and sales are what break-even is solving for. Break-even is a fixed point, not a division. Solving it by assuming a cohort and dividing will understate it."*

He is right, and the fixed point has a closed form, so no iteration is needed. Total contribution must equal F:

```
B × ( shelf × 0.708333  −  S_paid )  =  F        →        B*  =  F / ( shelf × 0.708333 − 3.459 )
```

| Shelf (inc. VAT) | Net per sale | Contribution per sale | **B\* (point est.)** | B\* (low F) | B\* (high F) |
|---|---|---|---|---|---|
| £9.99 | £7.08 | £3.62 | **20,907** | 18,692 | 23,177 |
| £14.99 | £10.62 | £7.16 | **10,564** | 9,445 | 11,711 |
| £19.99 | £14.16 | £10.70 | **7,068** | 6,319 | 7,835 |
| £24.99 | £17.70 | £14.24 | **5,310** | 4,747 | 5,887 |
| £29.99 | £21.24 | £17.78 | **4,253** | 3,802 | 4,714 |
| £39.99 | £28.33 | £24.87 | **3,041** | 2,719 | 3,371 |
| £49.99 | £35.41 | £31.95 | **2,367** | 2,116 | 2,624 |

**Three things the CEO should take from this table, in order of how much they change the picture.**

1. **The decision record's break-even is out by a factor of about four.** It records *"~2,400–2,700 sales over three years"* and the CEO decided PROCEED against that number. At £14.99 the figure is now **~10,600**. The record is not yet published (Article 3 deadline 2026-10-16), so this is correctable in the open before anyone reads it — but it is a material change to a decision's stated basis, and under Constitution 5.4 the CEO is entitled to revisit the decision on it. I am not asking him to; I am recording that the basis moved and that he is the only person who can decide whether it matters.

2. **The CTO's ~7,100 indication reproduces, and the gap to 10,600 is entirely variable support.** 75,627 ÷ £10.62 = **7,121** if variable support is ignored; ÷ £7.16 = **10,564** once it is not. He explicitly flagged that his figure was *"before variable support, which pushes it up"*. It pushes it up by **48%**, and the Android contact rate is most of it.

3. **Platform mix sensitivity.** At 100% iOS, S_paid falls to £1.84 and B\* at £14.99 is **8,616**. At 100% Android it rises to £5.89 and B\* is **15,988**. The 60/40 assumption is doing real work and it is a guess. **A cheap way to test it exists and is already mandatory:** the Play Console's 12-tester closed-test gate [E, retrieved by CTO 2026-09-16] is the first real contact with an Android audience, and the CTO is right to call it *"the cheapest available test"* of whether reach exists at all.

### 3.7 O10 — the §5 sensitivity arithmetic, located and corrected

I re-derived the whole of the old §5 from its own stated formulae. **The tables reproduce**; the failure is in one sentence of prose beneath them, and the Skeptic was right that it errs against the product.

> **Old text, `cost-sheet.md` §5:** *"Adding £4,000 of build to that column moves the 5,000-buyer price from £14.63 to about £26."*

£4,000 spread over 5,000 buyers is **£0.80 per buyer**. Cost per buyer goes from £8.6361 to £9.4361; × 1.694118 = **£15.99**. Not £26. To reach £26 would require roughly **£33,600** of additional build, not £4,000 — the stated figure is out by more than 8×.

Every other §5 and §6 figure reproduces to the penny against its stated inputs, including the floor row (£6.23 Overture, £15.01 Mapbox Permanent, £32.57 Foursquare, £62.42 Google) and the whole of §6's break-even table. **So the defect is a single unchecked sentence, not a broken model** — which is precisely the Skeptic's process finding at O10 and Condition 6: nobody re-derived it, including its author. The correction is recorded here and a banner is owed on §5 (§7 below). The section is superseded in any case, because the metered-API columns no longer exist.

### 3.8 O12 — the margin, relabelled as Article 2.1 now requires

The old §12 read: *"**Deviation from target:** none proposed."* That is the constitutional labelling error the Skeptic found, and Constitution v1.2 now states the rule explicitly rather than leaving it to inference:

> *"Prices target a margin of approximately **20% over published costs**… **A deviation in either direction is a deviation** — a margin below target is recorded and justified like any other, never labelled as no deviation. As a hard backstop, **no product's margin may exceed 30%**."* (Article 2.1)

**Corrected entry, which supersedes `cost-sheet.md` §12:**

> **Margin:** 16.5% over total published cost including store commission.
> **Deviation from the ~20% target: YES — a deviation of 3.5 percentage points below target.**
> **Justification (required in writing by Article 2.1):** store commission is treated as a cost of sale passed through at zero markup rather than a cost that earns margin. Taking 20% on Apple's and Google's fee as well would yield exactly 20.0% and a shelf price about 4% higher. Candour charges the customer nothing for collecting the platform's fee, and the deviation is the price of that choice. The alternative treatment is arithmetically available and is not being taken.
> **Direction of the deviation: against Candour, in the customer's favour.** Recorded because Article 9 names redefinition *"in the customer's favour"* as no defence — the direction is not the point, the labelling is.

### 3.9 What the re-derivation did *not* include, stated rather than assumed

`proposals/haunt/ceo-product-inputs.md` requires that this re-derivation be told about the venue page and session segmentation before it runs. It was, and neither is in the CTO's hours:

- **Session segmentation** (CEO input §2) — *"Not yet assessed by any seat. No effort estimate exists."* The CTO's 1,330 hours do not contain it.
- **The venue page** (CEO input §1) — partially covered by decomposition row 5 (venue index) and row 6 (timeline UI), but the aggregate/rating layer that makes it *"Letterboxd's film page applied to a pub"* is not separately sized, and Condition 8.6 puts a second cost on it if a window exists (§2.3).

**Neither is in any number above.** Both are net additions to F. **This is therefore a floor on cost, not a central estimate**, and every break-even in §3.6 is a floor on volume. That is the honest description and it is the direction the CEO should read the table in.

---

## 4. The cumulative margin test — Article 2.1 as amended

### 4.1 The clause, and a finding about it before any numbers

> *"Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit **against the cost of serving them**. A recurring price whose every individual year is compliant can still breach this document over a decade, and the cumulative test is what catches it."* (Constitution v1.2, Article 2.1)

**A finding I owe before I model it, because it determines whether the clause does anything at all.** Cumulative margin is a weighted average of annual margins **when both are computed on the same cost measure**. A weighted average of quantities each ≤ 30% is itself ≤ 30%. So on a single cost measure the cumulative test is mathematically implied by the annual test and can never bite. **The clause is non-redundant only because its two tests use different cost measures**, and the amended text says so without drawing attention to it:

- the **annual** test measures against the *product's* cost that financial year — which includes build labour amortised across everyone in the base that year;
- the **cumulative** test measures against *"the cost of serving **them**"* — one customer, over their life, in which a one-off build is paid for **once**.

That distinction is the whole clause, and it is load-bearing. **If "the cost of serving them" is read as "their pro-rata share of the product's annual cost", the cumulative test is a no-op and Article 2.1 gained a sentence that constrains nothing.** I flag this to the CGO as an interpretive question that should be settled in writing before any recurring price is published — and I flag it **as a flag, not a block**: interpreting the Constitution is the CGO's seat, not mine, and `pipeline/evidence-standard.md` is explicit that *"a process that answers an interpretive failure by adding agent passes is prescribing more of what already failed."* I model the incremental reading below because it is the only one on which the clause means anything.

### 4.2 The model

Steady state, two platforms, *N* subscribers, build amortised over three years per §3.2.

**Product cost per subscriber per year (the annual test's measure):**
- Years 1–3: `[45,957.55/3 + 7,196.20 + 2,551.38 + 135.98] / N + 2.306` = `25,202.74/N + 2.306`
- Year 4+: `[7,196.20 + 2,551.38 + 135.98] / N + 2.306` = `9,883.56/N + 2.306`

**Cumulative cost of serving one subscriber to tenure *t* (the cumulative test's measure):**
`(build share, charged once) + t × (their share of fixed running cost + variable support) + t × commission`

| | N = 1,000 | **N = 2,500** | N = 5,000 |
|---|---|---|---|
| Build share, charged once | £45.96 | **£18.38** | £9.19 |
| Annual incremental cost (running + support) | £12.19 | **£6.26** | £4.28 |
| Product cost/yr, years 1–3 | £27.51 | **£12.39** | £7.35 |
| Product cost/yr, year 4+ | £12.19 | **£6.26** | £4.28 |
| Honest shelf price, years 1–3 | £46.60 | **£20.99** | £12.45 |
| Honest shelf price, year 4+ | £20.65 | **£10.60** | £7.26 |

### 4.3 The breach, and when it happens

**The scenario is exactly the one the clause describes**, and it requires no bad faith from anyone. Candour keeps improving Haunt. New build work in years 4–6 is capitalised and amortised over the next three years, re-entering the product's annual cost base at roughly the rate the original build left it. The product's annual cost per subscriber therefore stays near its years-1–3 level, the price stays near £20.99, and **every single financial year passes the annual test at 16.5%.** No cost sheet is wrong. No deviation is unjustified. Nothing is hidden.

Meanwhile, the subscriber who joined at launch and never left has paid their share of v1's build **once, in years 1–3, in full** — and from year 4 the cost of serving them is £6.26 a year while the price is £20.99.

Cumulative margin at tenure *t*, against `Σ ex-VAT price` over `Σ (cost of serving them, including commission)`:

| Tenure | N = 1,000 | **N = 2,500** | N = 5,000 |
|---|---|---|---|
| 1 year | −39.3% | −35.9% | −31.0% |
| 2 years | −5.3% | −3.2% | −0.6% |
| 3 years | **+16.5%** | **+16.5%** | **+16.5%** |
| 4 years | +31.6% | +29.7% | +27.5% |
| 5 years | +42.7% | +39.2% | +35.1% |
| 7 years | +58.0% | +52.0% | +45.0% |
| 10 years | +71.8% | +63.1% | +53.5% |
| **30% cap breached at tenure** | **3.9 yrs** | **4.0 yrs** | **4.3 yrs** |

> **Answer to the CEO's question: a long-tenure subscriber breaches the 30% cumulative cap at a tenure of approximately four years, while every individual financial year remains compliant at 16.5%.**

**The result is structural, not scale-dependent, and that is what makes it worth knowing.** The breach point is **the amortisation period plus roughly one year**, at every scale I modelled, and the reason is visible in the table: cumulative margin sits at exactly the annual margin at *t* = 3, because that is where the build share is fully allocated and the two cost measures coincide. Every year after that adds revenue at near-full margin against a cost base that has lost its largest line. **Amortisation is what creates the breach, and the breach arrives one year after it ends.** Candour will be able to predict the date of it on the day Haunt launches.

Note also the first two rows: a subscriber who leaves in year 1 or year 2 leaves Candour at a **loss** on them, at every scale. The subscription is not a smooth annuity; it is a three-year cost recovery followed by a cliff in both directions.

### 4.4 The fix, which Candour is already required to perform

If the price steps down to the year-4 honest figure (£10.60 at N = 2,500) when the build finishes amortising, cumulative margin stabilises at **16.5% at every tenure to infinity.** Fully compliant, permanently, with no further mechanism.

And that step-down is not a new obligation. Article 2.1 already requires cost sheets *"reviewed and republished at least **annually** and at every price change"*; Article 2.3's waterfall already makes *"Price reductions for existing customers"* the first call on the remainder after reserve and distributions. **The cumulative test does not add a duty. It puts a number on the one that already existed, and names the year it falls due.**

So the honest statement to the CEO is: **the cumulative test is satisfiable, cheaply, by one act that is already owed — but it is satisfiable only by an act that must actually be performed, in year 4, by someone who by then has a revenue line depending on not performing it.** That is the shape of the risk and it is worth writing down now, in a document dated 2026, rather than discovering in 2030.

### 4.5 Dual pricing — the crossover, which bites three years before the margin cap does

`proposals/haunt/ceo-product-inputs.md` §3 records the hazard as *"At £4.88/year a subscriber passes the £29.59 lifetime price in year seven."* On the re-derived numbers, on consistent assumptions, it is much worse than year seven — and the old figure compared a year-4+ subscription price against a years-1–3 lifetime price, which is not a like-for-like comparison.

Like-for-like, at N = B = 2,500, for a customer present from launch for three years:
- **Lifetime unlock**, launch-day buyer: cost £37.17 → shelf **£62.97**
- **Subscription**, three years at £20.99: **£62.97**

They are identical, as they must be — the same customer, the same cost, the same margin. Which gives the crossover exactly:

> **A subscriber overtakes the lifetime buyer at precisely the amortisation period: three years to the day. Every year after that, they pay again for something the lifetime buyer has finished paying for.**

At the honest year-4 price of £10.60 the excess accumulates more slowly, but it accumulates: by year ten the subscriber has paid **£137.17** against the lifetime buyer's **£62.97**, for the same software on the same phone.

**This is not caught by Article 2.1** — the cumulative test measures against cost, not against what a different customer paid, and at the stepped-down price the subscriber's own margin is a compliant 16.5%. **It is caught by Article 1.3** — *"**Honest by default.** Pricing, capability, and limitations are stated plainly"* — and, if the two prices are presented side by side with the crossover unstated, arguably by Article 4's *"plain-language pricing with no hidden fees."* A customer choosing between £20.99/year and £62.97 once is choosing without the one fact that decides it: **they break even at three years, and the store will not tell them.**

**If the CEO wants dual pricing anyway, the condition is cheap and I would attach it:** the pricing screen states the crossover tenure in plain words — *"If you keep this for more than three years, buying once costs less"* — which is an unusual thing for a company to print, is true, and is the only version of dual pricing I can see surviving Article 1.3. My recommendation, though, is §5.

---

## 5. Recommendation

My charter requires a recommendation with a reason rather than a menu. Here it is, in one sentence, and then the reason.

> ### Ship Haunt as a single one-off purchase. No free tier, no visibility window, no subscription, no dual pricing.

### 5.1 The reason

**Four independent findings point the same way, and no finding in this document points the other way.**

1. **The window cannot pay for itself at any price, any length, or any reach multiple**, because the break-even conversion rate has a floor of 4.9%–11.4% that free-user support labour puts there, and the window's reachable population is capped by a retention ceiling of single-digit percentages. §1.
2. **The free tier's cost is real and its benefit is unevidenced.** £0.62 per free user per year is a number; the reach multiple *r* is a number nobody in this pipeline has ever written down. Spending a known cost to buy an unknown benefit is the transaction Constitution 1.5 exists to discourage: *"Operating cost discipline is an ethical obligation, because our customers pay our costs."* Every free user's support cost is carried by a paying user.
3. **The only versions of the window that convert are the versions Candour has pre-committed not to ship**, which makes building it an act of leaving a temptation in the codebase with a revenue number attached to it. §2.4.
4. **Subscription breaches the cumulative cap at four years and overtakes the lifetime price at three**, and both are avoidable only by acts of restraint scheduled for a year when the restraint will be expensive. §4.

**And a fifth, which is not arithmetic and which I flag as my judgment rather than a finding [J]:** the free tier's only purpose here was ever to let a buyer test whether the venue index knows their local pub before paying. That is a real problem — the UX seat names it at §6.1 — and a crippled free tier is a bad solution to it. The good solution is the one the UX seat already gave: *"saying the coverage number out loud"* in the store description, from Condition 2's spike. **A number in the listing solves the trial problem for £0 and no Article 4 surface.** It is also the only solution that works for a user who has not installed anything yet.

### 5.2 Saying the plain thing plainly

The task asked whether my answer is that no free tier should exist on this product. **It is, and I am not hedging it.** Haunt is a product with a high build cost, no acquisition channel, a support cost per user that is unusually high because the architecture is unusually honest, and a break-even of ten thousand sales. A free tier makes every one of those four things worse and improves none of them. The reason the free tier keeps being discussed is not that a model supports it; it is that free tiers are what apps have. **Candour's whole proposition is not doing a thing because it is what is done.**

I record one thing against my own recommendation, because a clean recommendation with an unstated weakness is the failure mode my charter names: **the CEO's decision to build Haunt was explicitly not a commercial decision** — *"I quite like this idea for myself personally and if I can release it and it makes a bit of money then I am happy with that"* — and a recommendation optimising commercial outcome is answering a question he did not ask. If the honest objective is "exists, is good, and is sold honestly", then a free tier's *commercial* failure is not decisive on its own, and the argument that survives is §2.4's: not that the window does not pay, but that it is a mechanism whose working form is forbidden. **That argument holds under either objective, and it is the one I would put weight on.**

### 5.3 One shape nobody has modelled, surfaced rather than recommended

The retrieved data contains one finding I would be withholding if I left it out. **Hard-paywall apps — a free download with payment required before use — convert at a 10.7% median against freemium's 2.1%** [E, RevenueCat 2026]. That is five times better than a free tier, and it contains **no read-cap of any kind**: nothing of the user's is ever hidden, because the user cannot write anything until they have paid. Conditions 8.1–8.6 would have nothing to govern.

Economically it is the purchase the CEO has already decided on. The differences are that a free listing gets materially better store discovery than a paid one, and that it puts the coverage-and-trial problem inside the app where a "see what we know near you" screen can answer it before payment.

**I am not recommending it, for three reasons, and they are all about other seats' scopes.** It changes the *shape* Condition 9 records as decided, which is a Constitution 5.4 decision and therefore the CEO's alone. It raises a genuine Article 4 question — whether a free download that demands payment on first open is *"drip pricing"* — which belongs to UX and the CGO and which I am not competent to answer. And it interacts with App Store 5.1.1(ii), which the UX seat already flagged in a different context. **It is on the table, with a number attached, and it is theirs to assess.**

### 5.4 What follows from this document, in order

1. **CEO** — decide whether the window survives §1. If it does not, delete Conditions 8.1–8.6 from the requirements scope and record the deletion in the open, in the same publication as the decision record (due 2026-10-16). Conditions 8.2 and 8.3 are worth keeping as standing product rules on their own merits even with no window to govern.
2. **CEO** — publish a three-year support commitment, or the amortisation treatment in §3.2 is unavailable and build labour reverts to a first-year operating cost.
3. **CEO** — note that the break-even his PROCEED rested on has moved from ~2,400–2,700 to ~10,600, and decide whether that changes anything. §3.6.
4. **CGO** — settle the reading of *"the cost of serving them"* in Article 2.1 (§4.1), and the ICO exemption determination (§3.4).
5. **CEO** — settle the shared-cost allocation rule before a second product exists (§3.4).
6. **CFO (me)** — the ONS ASHE primary retrieval, which is company work and which bars Article 3 publication of any Haunt price until it closes.

---

## 6. What would overturn these findings, and where I looked

Required by the universal charter clause as amended: *"**Negative findings carry the same duty as blocks.** Any finding that something is infeasible, prohibited, unaffordable or not worth doing must state (a) what evidence or change would overturn it, and (b) where you looked. A negative finding with neither is an opinion wearing a finding's clothes."*

### 6.1 What would overturn the finding that the window is commercially inert (§1)

**Any one of these, and I would withdraw it:**

1. **A measured month-*N* retention figure for Haunt above roughly 15%.** The entire ceiling argument is `c_window ≤ R(N)`. If Haunt retains 15%+ of installs at the window's length, the arithmetic changes shape. **How this could be obtained is itself a finding:** the product promises no telemetry, so this cannot come from instrumentation without breaking the promise. It could come from a paid research panel, or from an explicit opt-in cohort, and both are real money the CEO would be spending to answer this question. That cost should be compared against simply deleting the window.
2. **Evidence of a reach multiple above about 20** — a free tier buying more than twenty free installs for each foregone sale. Even then the floor (§1.3) binds: at £14.99 the break-even never falls below 11.4%. So this overturns the *r*-dependent columns but not the finding.
3. **A materially lower free-user support cost.** *S_free* is the sole cause of the floor. If the Android contact rate proves far below the CTO's 12% × 60 min, or if a free tier that cannot use automatic capture generates far fewer cases than a paying one, the floor falls. **This is the most likely of the three to be true**, and it is measurable in the Play closed test and TestFlight at no additional cost. At *S_free* = £0.20 the floor at £14.99 falls from 11.4% to 2.7%, which is within touching distance of the 2.1% benchmark — so this one genuinely matters and I am not dismissing it.
4. **A conversion benchmark from an independent second source** materially above RevenueCat's 2.1%, for consumer apps with no acquisition channel. My benchmark is single-origin and I have flagged it as such twice.

**What would *not* overturn it:** a higher unlock price. The floor falls with price (2.8% at £49.99), but §3.5 shows the honest price at any evidenced cohort is already at the top of the band, and the volumes in §3.6 fall as price rises only because break-even falls — not because more people buy.

### 6.2 What would overturn the cumulative-margin finding (§4)

1. **A CGO determination that "the cost of serving them" means the customer's pro-rata share of the product's annual cost.** On that reading the clause is a no-op and there is no breach at any tenure. §4.1 explains why I think that reading empties the clause, but the interpretation is not mine to make.
2. **A commitment to step the price down at the amortisation cliff**, which fully resolves it (§4.4) and which Candour arguably already owes under 2.3.3.1.
3. **A different amortisation period.** The breach tenure is period + ~1 year. A one-year period moves it to year two; the Definitions permit shortening, never lengthening.

### 6.3 Where I looked

**Retrieved from disk this session, in full:** `constitution.md` (v1.2 — Definitions, Articles 1, 2.1, 2.3, 3, 4, 5.2, 5.4, 5.6, 6.1, 7.2, 9, 10, 11); `roles/cfo.md`; `pipeline/evidence-standard.md`; `decisions/2026-09-16-haunt-gate.md` including Conditions 1–10 and Corrections C1 and C2 in full; `products/haunt/cost-sheet.md` in full including both correction banners on §8.2; `products/haunt/android-and-stack-note.md` in full; `proposals/haunt/ceo-product-inputs.md` in full; `pipeline/templates/` (directory listing — **no template exists for this artifact type**, so it is structured as a cost-model note and the deviation is stated here rather than made silently); `products/haunt/ux-note.md` §6 in full including the C2.6/C2.7 banner; `proposals/haunt/dissent-memo-c1.md` — C1-O5 in full, plus C1-O6, C1-O11, C1-O12 and the harms, abandonment and verification sections.

**Retrieved externally this session:** ICO data protection fee and exemptions pages (both, at ICO); Apple Developer Program; Google Play registration fee **at Google** rather than the secondary source the CTO flagged; GBP/USD spot; RevenueCat *State of Subscription Apps* 2026 and 2025 (same origin, counted as one source); UXCam retention benchmarks; ONS ASHE latest bulletin (**attempted and failed** on the occupational figure).

**Looked for and did not find:**
- Any statement, anywhere in the Haunt pack, of the reach multiple a free tier would buy. `proposals/haunt/proposal.md`, `idea-brief.md`, `gate-pack.md`, `ceo-product-inputs.md`, `ux-note.md` §6, the decision record and both dissent memos. **Absent, not merely unverified** — no seat has ever written one down.
- Any statement of what the visibility window is *for*. This is C1-O5's own finding and I confirm it independently: the window's commercial purpose is not stated in any artifact in this repository.
- A definition of *"lock-in"* or of the ICO's treatment of a support inbox — the first absent from the Constitution (the CGO checked this at C2.8 and I did not duplicate the search), the second not determinable from the ICO's published exemption list without a facts-specific judgment that Constitution 6.1 puts with a qualified human.
- A retention figure beyond day 30 in any retrieved source. Month-6 and month-12 benchmarks are not published on the page I retrieved, which is why §1.4's argument is built on a bound rather than a point estimate.

### 6.4 Blocks and flags, labelled per the amended charter

**Blocks held:** one, and it is not new. *No Haunt price may be published under Article 3 until the ONS ASHE labour benchmark is retrieved at primary* (Condition 5; my charter's *"launch of any pricing not backed by a published cost sheet"*). **What lifts it:** the primary retrieval, or a CEO decision in writing to adopt a different, retrievable benchmark.

**Blocks not held, stated so silence cannot be read as consent:** I hold **no block** on the visibility window, on a free tier, or on dual pricing. My charter's blocking power covers *"unpriced or uncosted launches"* and *"any proposal without a credible cost model"*, and neither reaches Article 4 or product shape. §5 is a **recommendation**; §1 and §4 are **findings**; §2.1 is a **flag**, and the seat that holds the corresponding block is **UX**, whose B2 release block the decision record records at C2.6 as engaging *"expressly including friction placed on the keep-gesture."* This is the same distinction C1.3 and C2.6 corrected against this seat once already, and I am not repeating it.

---

## 7. Corrections owed elsewhere, and what this seat could not establish

**Correction banners owed** (visibly, in place, and in the same publication as the decision record — due **2026-10-16** — for the reason the Skeptic gave at §4 of `dissent-memo-c1.md`: a consequential correction landing after publication no longer describes what happened):

| File | What is owed |
|---|---|
| `products/haunt/cost-sheet.md` §§3–10 | Superseded in full by §3 of this document: 450 hrs → 1,405; iOS-only → two platforms; the metered-API columns are moot on the zero-network architecture. |
| `products/haunt/cost-sheet.md` §5 | The O10 correction: the *"about £26"* sentence is wrong and the right figure is **£15.99**. §3.7. |
| `products/haunt/cost-sheet.md` §12 | The O12 relabelling. §3.8 supplies the replacement text. |
| `products/haunt/cost-sheet.md` §1 | The labour-treatment question is **no longer open** — Constitution v1.2's Definitions settled it, adopting this seat's treatment together with all three of its conditions. The section should say so and point at the clause. |
| `products/haunt/cost-sheet.md` §14 | Decisions 1 and 4 are decided (Definitions; CEO directed Android). Decision 5 is answered by §1 and §5 of this document. Decisions 2 and 3 remain open. |

**What this seat could not establish:**

| Gap | Why it matters | Owner |
|---|---|---|
| ONS ASHE Table 14 at primary — **attempted again this session, failed again** | Anchors every number in this document and in the company | CFO; bars Article 3 publication |
| Apple's UK merchant-of-record / VAT position | Moves every shelf price by 20% | CFO / CGO |
| The reach multiple *r* — **never written down by any seat** | The only input the free-tier case depends on | Research Analyst / CEO |
| Month-6 and month-12 retention for this category | Converts §1.4's bound into a point estimate | Unobtainable without telemetry or paid research; see §6.1 |
| iOS/Android platform mix | Moves break-even at £14.99 between 8,616 and 15,988 | Testable free in the Play 12-tester closed test |
| Effort for session segmentation and the venue-page aggregate layer | Both are net additions to F; every break-even above is a floor | CTO |
| Whether the ICO fee is owed at all | £52/yr, i.e. 0.2% of the cost base — **not worth resolving**, stated so nobody spends money on it | CGO |
| Whether a visibility window generates its own support category | Raises *S_free*, raises every break-even in §1.2 | Omitted; errs in the window's favour |

---

## 8. Related-party disclosures

**None.** No payment to the founder, family or any affiliated entity is contemplated in this model. All founder labour is costed at the published external benchmark and is currently unpaid and undrawn; it appears here as cost because Constitution 2.1 requires *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

---

## Change log

| Date | Change |
|---|---|
| 2026-09-17 | Created. Discharges the open C1-O5 item and Condition 1 of `decisions/2026-09-16-haunt-gate.md`. External prices retrieved 2026-09-17. Supersedes `products/haunt/cost-sheet.md` §§3–10, §12. **Not a published cost sheet and not a price.** |

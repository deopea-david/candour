# Cost sheet — Haunt — v2 (pre-requirements)

**Seat:** Chief Financial Officer · **Date:** 2026-09-20
**Status:** **Intended for publication under Constitution 2.1 and Article 3.** Written for a sceptical customer first and the CEO second. It is not yet published, and it is not a price: pricing is a Constitution 5.4 decision and belongs to the CEO alone.

**Supersedes** `products/haunt/cost-sheet.md` in full, and supersedes `products/haunt/pricing-ladder-model.md` §§2–9 and `products/haunt/window-conversion-model.md` §3 on every number. Where this sheet corrects one of my own earlier findings, it says so in place and names the error rather than quietly restating it (§16.2).

**What changed since those documents:** the CEO settled two decisions (D1, two platforms; D2, a published support commitment), the CTO returned a re-based engineering estimate that is 57% larger than the one every prior price rested on, and the Engineer's venue-index spike created work nobody had costed. **This sheet is the first document in this repository that shows the whole cost of Haunt in one place.**

**Template note:** `pipeline/templates/cost-sheet.md` assumes a monthly hosting-shaped cost table and a single price. Haunt has no hosting and four price tiers, so this sheet keeps the template's required elements — itemised costs, related-party disclosures, price, margin, deviation and justification, change log — and adds the sections a subscription needs. The deviation from the template is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md` v1.1. Every external figure was **retrieved 2026-09-20** unless a different date is given; nothing external is cited from memory. Every constitutional claim quotes the clause it relies on in the same passage, per that standard's *"Claims about our own rules"*. Where a statement is this seat's professional judgment rather than a requirement, it says so, per *"A seat's heuristic is not an article."*

---

## 0. The answers, before the arithmetic

**A. The cost base is 1.60× larger.** On the CTO's revised figures — build **2,090 h** (range 1,770–2,410), pre-build spikes **188 h**, fixed maintenance **360 h/yr**, fixed support floor **115 h/yr** — Haunt's annual published cost on a five-year life is **£30,579.57**, against **£19,075.07** in the last model. The CTO's indication of *"roughly 1.61×"* re-derives exactly: **1.6031×**. §2, §6.

**B. The supported life does not change three of the four prices. It changes the number of subscribers at which they are honest.** This is the single most useful thing in this sheet and it was not visible until the life was modelled as a variable. Monthly **99p**, quarterly **£2.59** and yearly **£9.89** are the honest prices at **two, three and five years alike**. What moves is the volume at which they are honest — **15,577 / 11,922 / 8,998 subscribers** — and the pay-once price, **£19.49 / £28.99 / £48.49**. §5.

**C. Two years does not make Haunt unaffordable. It makes the volume worse by 73% and puts an irreversible 30% price cut in month 25.** At two years, 99p recovers its cost at 11,027 subscribers and is exactly honest at 15,577; the sustained acquisition rate needed rises from 1,225 to **2,121 new subscribers every month for the whole life**. Nothing here is arithmetically impossible. It is a materially harder version of a target the discovery pack already found unreachable. §5, §12.

**D. My recommendation on the period is three years, and the reason is deliverability, not arithmetic.** Five years is the best number in this sheet on every commercial measure and the worst on the only measure that is not a number: whether Candour will actually do 360 hours a year of maintenance, on two platforms, for five years, starting after a build the CTO sizes at 55.75 focused solo weeks. Three years is the longest period for which the promise and the funded work plausibly coincide. §5.6, §14.

**E. D2's definition does not fully match what 360 h/yr funds, and the gap is the security limb.** D2 promises that *"security and defect fixes are made."* The CTO's nine maintenance rows contain OS-compatibility work, venue-index reconciliation, Expo upgrades, OEM regression chasing, subscription upkeep, regulatory upkeep and accessibility re-verification. **There is no row for security patching, and no row for defect fixes that are not OS- or OEM-driven.** Two of D2's three limbs are funded; the third is not. §4.

**F. The pay-once tier carries a real 18.4% discount and it is cost-anchored, not marketing.** At five years: **£48.49**, against £59.40 of monthly payments. That closes UX's block **B11** on its own terms — there is now a saving, so a saving may be stated. It also moves the crossover **inside** the supported life: a monthly subscriber overtakes the pay-once price at **49 months**, not 60. That is an Article 1.3 disclosure before it is a margin question, and the sentence that discloses it is drafted at §9. §7, §9.

**G. Discounts deeper than ~10% do not collapse the band. My own earlier finding was wrong, and Condition 9.3 carries the error.** The prior model priced tier discounts from a cost saving (avoided billing events) and then did not apply that saving to the tiers' cost of service. Corrected, the blended band at an 18.4% pay-once discount is **1.69×** — wider than the 1.42× the prior model reported for a ladder half as deep. The band closes at roughly **41%**, not 25%. §6.3.

**H. The Article 2.1 cumulative-lifetime question is closed on the arithmetic and changes no price.** I modelled *"the cost of serving them"* both ways. The two readings produce **identical** cumulative margins at every tenure at or beyond the supported life, which is the only region where the test binds — and in every case the **annual** test breaches first, by five years. The determination is still owed by the CGO, but it is no longer a bar on publishing a price. §8.

**I. The Article 9 shared-fee question is closed with a proposed rule.** Shared company fees are allocated equally across live products at each annual republication; Haunt carries 100% while it is the only product, and this sheet says so on its face. At **0.42% of the annual cost base** this is a governance fix, not a money fix, and it is worth making now precisely because it is cheap. §13.

**J. The honest reach number has moved from 19,500–33,000 to 50,000–85,000 distinct subscribers** on a five-year life, and the reason is two-thirds cost and one-third a longer window. **The pay-once tier needs 6,701 distinct buyers.** *(On the three years I recommend: 58,426 distinct subscribers or 8,927 pay-once buyers — fewer people in total, in a shorter window, so the sustained acquisition rate is worse: 1,623 a month against 1,225. §5.1.)* On a product whose binding constraint is reach, the pay-once tier is between four and eleven times more efficient than the subscription depending on the period — 4.4× at two years, 6.5× at three, 11× at five. That, not margin, is the strongest commercial argument in this document. §12.

**L. The Constitution's "shortened, never lengthened" ratchet is flawed and I agree with the CVO on both counts, with a third of my own.** Shortening is the **price-raising** direction and is permitted without justification; lengthening is the price-lowering direction and is forbidden outright — which runs against Article 2.1's justification requirement and Article 2.3.3.1's preference for price reductions to existing customers. My third count: the Definitions' *"must equal"* tie, read with CRA 2015 s.36(3), **freezes the period in both directions once it is published and sold against**. Replacement wording is drafted. **This is a one-shot, pre-launch decision and the CEO should know that before making it.** §5.5.

**K. My standing block is maintained in a narrowed form, and it is one step from lifting.** No Haunt price publishes under Article 3 without a complete cost sheet behind it. This sheet is complete on everything within my charter except one input: the supported life is the CEO's to set, and the pay-once price and the volume figures are undetermined until he sets it. **The block lifts the moment the period is published.** §16.

---

## 1. What this cost sheet is, in plain words

Candour publishes what a product costs, itemised, including the founder's labour valued at a published market rate whether or not he is actually paid. Constitution 2.1: *"Every product publishes a **cost sheet**: hosting, tooling, support, third-party services, and a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

Three things follow that a reader is entitled to know up front.

**Haunt has not been built.** Every figure below is an estimate of a cost not yet incurred, and the largest of them — 2,278 hours of build labour — is one engineer's judgment, not a measurement. The CTO says so in his own words: *"it has never been tested against a real year of anything."* [E, `products/haunt/subscription-sizing-note.md` §9.4, read from disk 2026-09-20]

**Nobody has been paid anything.** The £74,513 of build labour below is the market value of work the founder will do himself and is not currently drawing. It appears as a cost because the Constitution's Definitions require it: *"labour valued at a published market benchmark whether or not it is actually paid."* If Haunt never covers that number, the gap will be published, not hidden.

**Haunt has no server, so it has no per-user infrastructure cost.** Hosting is £0.00 and that is structural, not disciplinary. The journal lives on the customer's own device. The cost of Haunt is almost entirely one person's time.

---

## 2. Itemised cost

### 2.1 The labour benchmark

| | |
|---|---|
| **Benchmark** | **£32.71 per hour worked** |
| Source | ONS *Annual Survey of Hours and Earnings*, Table 14.7a, SOC 2020 code **2134** (*Programmers and software development professionals*), full-time, UK, 2025 provisional: **median gross annual pay £56,914** [E, [ONS ASHE Table 14](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupation4digitsoc2010ashetable14), retrieved at primary 2026-09-18, release date 2025-10-22; carried forward from `pricing-ladder-model.md` §1 and not re-retrieved this session] |
| Derivation | £56,914 ÷ 1,740 hours actually worked = £32.71 |
| Why hours worked, not paid hours | Constitution 2.2 names the benchmark as *"the median UK software developer salary, **adjusted for hours actually worked**"*. ONS also publishes a median gross **hourly** figure of £29.58, which divides by *paid* hours including statutory leave. The Constitution's wording selects the derived figure. The ONS hourly column is recorded here so a reader can see the difference was noticed and disposed of rather than overlooked. |
| Precision | ONS coefficient of variation on this median is **2.7%**, inside ONS's own *"CV <= 5%… Estimates are considered precise"* band [E, ASHE Table 14.7b, row 2134] |

**Every figure in this sheet scales linearly with £32.71.** It is a single-source figure by nature — there is one ONS — but it was retrieved at primary from the publisher, which is the strongest form available. Gate Condition 5 required exactly this and is discharged.

### 2.2 One-off build labour (capital)

Constitution v1.2, Definitions: *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year… the amortisation period must equal a **published** support commitment to customers… **Absent a published support commitment, build labour is a first-year operating cost.**"*

| Item | Low | **Point** | High | Source |
|---|---|---|---|---|
| Two-platform build (iOS + Android, React Native) | 1,770 h | **2,090 h** | 2,410 h | CTO, `subscription-sizing-note.md` §10.2 [J] |
| Android capture-reliability spike (CTO Block 2) | 75 h | **75 h** | 75 h | CTO, §10.2 [J] |
| Venue-index remediation spike (CTO Block 4, new) | 113 h | **113 h** | 113 h | CTO, §8.2 [J] |
| **Total hours** | **1,958 h** | **2,278 h** | **2,598 h** | |
| **At £32.71** | **£64,046.18** | **£74,513.38** | **£84,980.58** | |
| Google Play one-off registration | £18.66 | **£18.66** | £18.66 | $25 ÷ 1.33951 [E] |
| **Capitalised total** | **£64,064.84** | **£74,532.04** | **£84,999.24** | |

**Unit, stated because an unstated one caused a 33–58% discrepancy in this pack once already:** one focused solo week = **37.5 hours**. 2,278 hours is **60.75 focused solo weeks**. For a part-time operator that is multiple calendar years, and the CTO has recorded that as a concern in writing (§10.5 of his note). It is his to raise and the CEO's to weigh; I carry it into §12 because it is what makes the reach number bind.

**Both spikes are inside the capitalised figure, and the treatment is stated rather than assumed.** The CTO asks that they be carried outside, because either may return *"don't build"*. His reason is sound. But for the purpose of pricing a product that **ships**, a spike is money spent to ship it, and an honest price to a customer includes it. **If a spike returns "don't", its hours are not capital — there is no supported life to amortise them over — and they are written off publicly under Article 7.2 rather than recovered from anyone.** The range row above lets a reader take either treatment.

### 2.3 Fixed annual operating cost

Independent of how many customers there are.

| Item | Low | **Point** | High | Basis |
|---|---|---|---|---|
| Maintenance labour — OS releases, Expo/React Native upgrades, venue-index reconciliation, OEM regressions, subscription and store mechanics, regulatory upkeep, accessibility re-verification | 288 h | **360 h** | 441 h | CTO §9.2 [J] |
| Support floor — inbox, store and policy churn, reproducing reports, entitlement and restore cases | 100 h | **115 h** | 130 h | CTO §9.5 [J] |
| **Fixed labour** | **388 h** | **475 h** | **571 h** | |
| **At £32.71** | **£12,691.48** | **£15,537.25** | **£18,677.41** | |
| Apple Developer Program | £73.91 | **£73.91** | £73.91 | $99/yr ÷ 1.33951 [E, [developer.apple.com/programs](https://developer.apple.com/programs/); FX [E, [tradingeconomics.com](https://tradingeconomics.com/united-kingdom/currency), GBP/USD 1.33951, 18 Sep 2026] |
| ICO data protection fee, Tier 1 | £52.00 | **£52.00** | £52.00 | [E, [ico.org.uk](https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/), retrieved 2026-09-20: Tier 1 £52; *"maximum turnover of £632,000… or no more than 10 members of staff"*; £47 by direct debit — **£52 carried as the prudent figure**] |
| Domain and static support page | £10.00 | **£10.00** | £10.00 | [J] — .com renewal not retrieved; immaterial at 0.03% of the base |
| Hosting | **£0.00** | **£0.00** | **£0.00** | No server. |
| Database | **£0.00** | **£0.00** | **£0.00** | All state on the customer's device. |
| Venue / places API | **£0.00** | **£0.00** | **£0.00** | Bundled offline dataset. No metered API, no per-read cost, no heavy-user penalty. |
| Crash and analytics tooling | **£0.00** | **£0.00** | **£0.00** | Deliberately absent (Article 4 data minimisation). The cost reappears above as support labour, because a product that collects no diagnostics is harder to support. |
| Build infrastructure (Expo EAS) | **£0.00** | **£0.00** | **£0.00** | Free tier sufficient [E, CTO, retrieved 2026-09-16]. Named trigger: Starter at $19/month ≈ £170/yr if monthly builds exceed 15 per platform. |
| **Total fixed annual** | **£12,827.39** | **£15,673.16** | **£18,813.32** | |

**On the ICO fee.** Whether Haunt owes it is genuinely open. The ICO exempts organisations processing personal data **solely** for a closed list of purposes [E, [ico.org.uk exemptions](https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/exemptions/), retrieved 2026-09-17, carried forward]. On this architecture Candour holds no journal data at all, and Apple and Google are merchants of record, so Candour may not hold payment details either. What is left is the support inbox, which receives customer-written descriptions of failures. **The fee is probably owed on account of the inbox rather than the product.** It is carried at the full £52. At 0.17% of the annual cost base it is not worth an hour of anyone's time to be right about, and that is recorded plainly rather than performing diligence proportionate to nothing. The determination belongs to the CGO.

### 2.4 Variable cost, per subscriber per year

This is the only cost that scales with customers, and on a product with no server it is entirely support labour.

| Component | Hours/subscriber/yr | At £32.71 | Basis |
|---|---|---|---|
| iOS subscriber — 5% annual contact rate × 45 min | 0.0375 | £1.2266 | CFO original, accepted by CTO |
| Android subscriber — 12% × 60 min | 0.1200 | £3.9252 | CTO amendment [J] |
| **Blended at 60% iOS / 40% Android** | **0.0705** | **£2.3060** | Platform mix is **[J]** — no evidence exists; §15.4 |
| **Subscription billing uplift** | per billing event | **£0.1090/event** | [J] — 1% of billing events generate a 20-minute contact |

**The subscription uplift, which the CTO asked me to set and which I am setting here.** A one-off purchase has one billing event. A subscription has one per renewal, and each is an occasion for a support contact — *"why was I charged"*, *"how do I cancel"*, a billing retry, a grace period. At £0.1090 per event:

| Tier | Billing events per year | **Variable cost per subscriber-year** |
|---|---|---|
| Monthly | 12 | **£3.6140** |
| Quarterly | 4 | **£2.7420** |
| Yearly | 1 | **£2.4150** |
| Pay once | 0 after purchase | **£2.3060** |

**Three things about this number, because it is load-bearing and it was not load-bearing before.**

1. **It is the same parameter that funds the ladder's discount.** In the prior model, £0.1090 was used only to size how much cheaper a longer commitment is to serve. It was decorative there and it is structural here, because the CEO's decision at C3.0 — that the pay-once tier carries a real discount — requires a real cost saving behind it. **If this number is zero, there is no cost-anchored discount, the pay-once tier returns to exactly 60 × 99p, and UX's block B11 bites again.** The discount and the cost base must run on the same figure or the cost sheet and the pricing page describe different products.
2. **I have not moved it because the answer became inconvenient.** £0.1090 is the central case I published on 2026-09-18, before it mattered to the band. Sensitivity at £0.0000, £0.0545 and £0.3271 is at §6.4.
3. **There is a double-count risk and I am naming it rather than netting it out.** The CTO raised the *fixed* support floor from 78 to 115 h/yr partly for cancellation questions, which also appear in my billing-event basis. The overlap is small in absolute terms and I carry both, which errs **against** the product. That is the direction an honest overlap should err in.

**A free (lapsed, read-only) user costs £0.6150/year** on the same basis — carried forward from `window-conversion-model.md` §3.3. Condition 9.7 means every lapsed subscriber becomes one of these permanently, and that cost is real and is carried.

### 2.5 The whole cost base, on a five-year supported life

| | Low | **Point** | High |
|---|---|---|---|
| Capitalised build, amortised over 5 years | £12,812.97/yr | **£14,906.41/yr** | £16,999.85/yr |
| Fixed annual operating cost | £12,827.39/yr | **£15,673.16/yr** | £18,813.32/yr |
| **Annual fixed cost `A`** | **£25,640.36** | **£30,579.57** | **£35,813.17** |
| **Total published cost over five years** | **£128,201.78** | **£152,897.83** | **£179,065.83** |
| Plus, per subscriber per year | £2.31 – £3.61 depending on tier | | |

**Against the prior model's £19,075.07: ×1.6031.** The CTO's indication of *"roughly 1.61×"* re-derives. Condition 6 requires arithmetic to be re-derived by a seat other than its author; this is that re-derivation, and on this figure it confirms him.

### 2.6 What is deliberately not in this sheet

- **The proportionate-refund duty under the DMCCA.** It is not a build item and no build creates one: Candour has no refund mechanism, refunds are adjudicated and paid by Apple, and `Transaction.beginRefundRequest` starts an Apple-adjudicated request rather than a Candour-funded one [E, CTO §5.4, quoting Apple documentation retrieved 2026-09-19]. **It is a launch bar (L1) requiring qualified human legal review under Constitution 6.1, not a line item.** If that review concludes the duty falls on Candour, the options are commercial or structural, not technical, and no amount of build budget moves the line.
- **Marketing and acquisition spend.** There is none, and that is the most consequential absence in this document. §12.
- **Any cost of a permanent free tier.** Condition 9.7 removed the read-cap; a lapsed user retains a free manual journal, whose support cost is carried at §2.4.

---

## 3. How a price is computed from these costs

Stated in full so a reader can reproduce every number below with a calculator, and so a second seat can re-derive it (gate Condition 6).

**Article 2.1:** *"Prices target a margin of approximately **20% over published costs**… **A deviation in either direction is a deviation**… As a hard backstop, **no product's margin may exceed 30%**, regardless of justification."*

Let `N` be the number of subscribers, `A` the annual fixed cost, and `s` the tier's variable cost per subscriber-year.

```
Cost of serving one subscriber for a year:     C(N) = A/N + s
Shelf price (what the customer pays, inc VAT): V
Ex-VAT price:                                  P = V / 1.20
Store commission (Apple 15%, Google 10%+5%):   0.15 × P
Net proceeds to Candour:                       0.85 × P

margin(N) = ( 0.85·P − C(N) ) ÷ ( C(N) + 0.15·P )
```

**Candour's pricing rule: commission is a cost of sale passed through at zero markup.** So the honest shelf price is

```
V = C(N) × 1.20 × 1.20 ÷ 0.85 = C(N) × 1.694118
```

**Check, for re-derivation:** at `V = 1.694118 × C` the margin expression returns **16.504%**. ✔

### 3.1 The deviation, recorded as Article 2.1 requires

> **Margin: 16.50% over total published cost including store commission.**
> **Deviation from the ~20% target: YES — 3.50 percentage points below target.**
> **Justification, in writing as Article 2.1 requires:** Candour takes no margin on the 15% that Apple and Google charge. Taking 20% on the platform's fee as well would yield exactly 20.0% and a shelf price about 4% higher. **The customer is charged nothing for the service of collecting the platform's fee, and this deviation is the price of that choice.** The alternative treatment is arithmetically available and is not being taken.
> **Direction: against Candour, in the customer's favour.** Recorded as a deviation anyway. Article 9 names *"Quietly weakening the rules"* as a gaming vector and the direction is not a defence — a deviation labelled "no deviation" is the error, whichever way it points. This is the correction the Skeptic's objection **O12** required and it is now made on the face of the sheet rather than in a model.

**A second deviation is created by rounding** to the store's available price points, and it is recorded per tier at §7.3.

### 3.2 What the price is *not* a function of

**There is no hosting cost, so there is no volume discount hiding anywhere.** Haunt's cost is one person's time. That has an uncomfortable consequence a customer should see stated plainly rather than discover: **the price depends almost entirely on how many people buy it.** Below, the same product at the same quality costs £4.83 a month to serve at 1,000 subscribers and 87p at 12,000. Candour does not get to choose which of those is true, and neither does the customer.

---

## 4. Does D2's promise match what the money buys? — checked, and it does not, on one limb

**D2, as recorded:** *"for five years from launch the app continues to run on then-current iOS and Android, security and defect fixes are made, and the bundled venue index is refreshed. **What is not promised: new features.** The definition is deliberately matched to what the CTO's 360 h/yr actually funds."* [E, `decisions/2026-09-16-haunt-gate.md`, CEO decisions log, read from disk 2026-09-20]

I was asked to check that the definition and the money describe the same thing. **They do on two limbs of three.** The CTO's nine maintenance rows, mapped onto D2's three promises:

| D2 promise | Rows that fund it | Hours/yr (low–high) | Funded? |
|---|---|---|---|
| *"continues to run on then-current iOS and Android"* | iOS OS-release compatibility; Android OS release + Play policy; Expo/React Native major upgrades; OEM regression chasing; source-map retention | 187.5 – 266 | **Yes.** Each is a hard-dated external forcing function the CTO retrieved at source: Apple's minimum-SDK requirement, Google Play's target-API requirement, and Expo's observed two-majors-a-year cadence [E, CTO §9.3, retrieved 2026-09-19] |
| *"the bundled venue index is refreshed"* | Venue index: refresh → reconciliation, quarterly | 60 – 100 | **Conditionally.** See below. |
| *"security and defect fixes are made"* | — | **0** | **No.** |
| *(not promised: new features)* | Subscription/store upkeep; regulatory upkeep; accessibility re-verification | 40 – 75 | n/a — these are compliance upkeep, not features |

### 4.1 The security limb is unfunded

There is **no row for security patching** in the CTO's table, and no row for defect fixes that are not OS-driven or OEM-driven. The nearest candidates do not cover it: *OEM regression chasing* is Android-device-specific; *source-map retention and symbolication* is diagnosis, not repair; and the support floor's *"reproducing reports, diagnostic-bundle loop"* is triage, not fixing. The CTO's own §9.3 notes that *"years 1–2 carry the regulatory front-load and the post-launch defect tail"* — acknowledging the defect tail exists while giving it no line.

**Why this matters more than a missing row usually would.** D2 is not marketing. CRA 2015 s.36(3) makes pre-contract information about a product's characteristics a term of the contract [E, [CRA 2015 s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36), retrieved by the CGO 2026-09-17, read from `compliance-note.md` §4.2; **travelling from another artifact, attributed, not re-retrieved by me**]. *"Security and defect fixes are made"* will be a contractual promise to every customer, and a React Native application with four local native modules and two SDK majors a year has a real dependency-CVE surface.

**This is a flag, not a block.** Sizing it is the CTO's, not mine. What I can do is price the consequence, and it is not large:

| Un-named security / defect-fix line | Annual cost base `A` | 99p is honest at |
|---|---|---|
| +0 h/yr (as the CTO's table stands) | £30,579.57 | 8,998 |
| +30 h/yr | £31,560.87 | 9,287 |
| +45 h/yr | £32,051.52 | 9,431 |
| +60 h/yr | £32,542.17 | 9,575 |
| +90 h/yr | £33,523.47 | 9,864 |

> **Finding: the security limb costs between 3% and 10% on the volume the price needs. It does not change any recommendation in this sheet. It should still be named, because a promise with no hours behind it is how a five-year commitment turns into a five-year apology.**

**What would resolve it:** the CTO adding a named security-and-defect row to §9.2, at whatever size he judges; or the CEO narrowing D2's wording to what the existing rows fund. **Either is fine. Leaving the sentence and the table disagreeing is not.**

### 4.2 The venue-index limb is contingent on a spike that has not run

The 60–100 h/yr that funds *"the bundled venue index is refreshed"* is reconciliation work created by the Engineer's spike. The CTO carries a separate 113-hour pre-build spike (his Block 4) specifically because **it may return "don't"** — his proposed pass criterion is a modal rank-1 share above 0.8 at 25 m query error and top-five recall above 80%, against measured values of **0.27** and **51.9%** [E, CTO §8.2, on the Engineer's measurements, `venue-index-spike.md` §§5–6, retrieved 2026-09-19].

**If that spike fails, D2's third limb has nothing to promise.** The CTO puts the same point commercially: *"an index that is shipped once and never reconciled is not 'maintained', it is 'bundled'"* — and a bundled index is a weaker answer to Apple's guideline 3.1.2(a) ongoing-value requirement than the subscription is being sold on.

> **Recorded for the CEO: D2 was published before the spike that funds one third of it has run. If the spike returns "don't", D2's wording must change before launch, and a published commitment is harder to change than an unpublished one.** The cheapest sequence is to run the spike before publishing D2's exact wording; the spike is 113 hours against a 2,278-hour build.

---

## 5. The supported life, modelled as a variable

**Why this section exists.** D2 published five years. The CEO has since disclosed that the five-year figure was **reverse-engineered from the pay-once price** — 99p × 12 × 5 = £59.40 — rather than derived from any judgment about what he is willing to support, and has asked whether two years is viable.

**He is right to reopen it, and the ordering he names is the one the Constitution implies.** Constitution v1.2, Definitions: *"the amortisation period must equal a **published** support commitment to customers"*. The clause makes the commitment the input and the accounting the consequence. **Deriving the commitment from a price that was itself derived from the commitment is circular**, and the circularity was mine to notice: `pricing-ladder-model.md` §8.2 presented *"the CEO's own arithmetic names the period"* as a happy discovery, when what it actually showed is that two numbers chosen together agree with each other. I record that as my error rather than his.

### 5.1 The three lives, side by side

All figures at the point-estimate cost base. `N*` is the subscriber count at which 99p per month is **exactly** the honest price under Candour's pricing rule.

| | **L = 2 years** | **L = 3 years** | **L = 5 years** |
|---|---|---|---|
| Amortised build per year | £37,266.02 | £24,844.01 | £14,906.41 |
| **Annual fixed cost `A`** | **£52,939.18** | **£40,517.17** | **£30,579.57** |
| **Total published cost over the life** | **£105,878.36** | **£121,551.52** | **£152,897.83** |
| 99p recovers its cost at | 11,027 subscribers | 8,439 | **6,369** |
| **99p is exactly honest at `N*`** | **15,577** | **11,922** | **8,998** |
| 99p hits the 30% hard cap at | 21,038 | 16,101 | 12,152 |
| Band width (cost recovery → cap) | 1.908× | 1.908× | 1.908× |
| **Monthly price** | **£0.99** | **£0.99** | **£0.99** |
| **Quarterly price** | **£2.59** | **£2.59** | **£2.59** |
| **Yearly price** | **£9.89** | **£9.89** | **£9.89** |
| **Pay-once price** | **£19.49** | **£28.99** | **£48.49** |
| Pay-once saving vs monthly over the life | 18.0% | 18.7% | 18.4% |
| Crossover (monthly overtakes pay-once) | 20 months | 29 months | 49 months |
| **Amortisation cliff falls at** | **month 25** | **month 37** | **month 61** |
| **Size of the cut at the cliff** | **30.3%** (99p → 69p) | **30.3%** (99p → 69p) | **20.2%** (99p → 79p) |
| Margin in the first post-cliff year if the price is *not* cut | +62.2% | +54.4% | +44.7% |
| Distinct subscribers needed at 5.2-month tenure | 50,892 | 58,426 | 73,493 |
| **Sustained acquisition rate needed** | **2,121/month** | **1,623/month** | **1,225/month** |
| Distinct pay-once buyers needed | 11,517 (480/month) | 8,927 (248/month) | **6,701 (112/month)** |

### 5.2 The finding that was not visible until the life was a variable

> **The supported life does not set the price. It sets the number of customers at which the price is honest.**

Monthly, quarterly and yearly are **the same three numbers at two years, three years and five years**. That is not a coincidence and the algebra says why: the honest price is `(A/N + s) × 1.694118`, and lengthening the life lowers `A` while the price is held at 99p — so what moves is `N`, not `V`. The pay-once tier is the only one whose *price* moves, because it is the only tier that buys a period rather than a unit of time.

**What this means for the decision, in one sentence:** choosing the supported life is not choosing what Haunt costs a customer per month. It is choosing how many customers Haunt needs before 99p is a price Candour can defend.

### 5.3 Two years, in plain numbers

**Is Haunt unaffordable at a compliant margin on a two-year commitment? No.** It is more expensive at every volume, and at the volumes this company has evidence for the honest price stops being a consumer app-store price sooner.

Honest **monthly** price, by subscriber count and supported life:

| Subscribers | **L = 2** | **L = 3** | **L = 5** |
|---|---|---|---|
| 1,000 | £7.98 | £6.23 | £4.83 |
| 2,000 | £4.25 | £3.37 | £2.67 |
| 3,000 | £3.00 | £2.42 | £1.95 |
| 4,000 | £2.38 | £1.94 | £1.59 |
| 6,000 | £1.76 | £1.46 | £1.23 |
| 8,000 | £1.44 | £1.23 | £1.05 |
| 9,000 | £1.34 | £1.15 | **£0.99** |
| 12,000 | £1.13 | **£0.99** | £0.87 |
| 15,577 | **£0.99** | £0.88 | £0.79 |

**Read the left-hand column honestly.** A two-year commitment does not price Haunt out of existence. At 4,000 subscribers the honest price is £2.38 a month, which is an ordinary price for a consumer app and would be entirely publishable. **What two years does is take 99p specifically off the table at any volume below about 11,000.** If the CEO wants 99p, five years is the cheapest way to have it; if he wants two years, 99p is not the price and something between £1.30 and £2.40 is.

**And the counter-intuitive part, which is the more important half.** A two-year life is a **cheaper product in total** — £105,878 against £152,898, because it buys three fewer years of maintenance — and a **dearer product per year**. The build does not shrink; the number of years it is spread over does.

### 5.4 The cliff is the real argument against two years

At two years the amortisation cliff falls in **month 25**, and the cut is **30.3%**. Three facts make that worse than it sounds:

1. **It is not optional.** If the price is not cut, the realised margin in the first post-cliff year is **+62.2%**, more than twice a cap that Article 2.1 says applies *"regardless of justification"*.
2. **It lands on existing customers and cannot be undone.** Apple's own documentation: *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. **You don't have the option to preserve the higher price for existing subscribers.**"* [E, [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions), retrieved 2026-09-20]. Article 2.3.3.1 wants exactly that, and the store enforces it.
3. **It arrives while the product is still being acquired.** Haunt's own model needs sustained monthly acquisition for the whole of the supported life. A two-year life asks Candour to take a permanent 30% revenue cut per subscriber at the halfway point of its own acquisition programme.

**Five years is the only one of the three lives where the cut is smaller (20.2%) rather than larger, and it is smaller for a reason worth stating:** at five years the build is a smaller share of what each subscriber costs to serve, so less falls away when it goes.

### 5.5 "Shortened, never lengthened" — the clause challenged, and this seat's answer

**The clause, quoted.** Constitution v1.2, Definitions: *"Three conditions bind that treatment: the amortisation period must equal a **published** support commitment to customers; any unamortised remainder is written off publicly on discontinuation (7.2); and **the period may be shortened, never lengthened**."*

**The CEO has questioned this clause directly, and the CVO — who drafted it — now believes it is flawed on two counts. I was asked whether I agree. I do, on both, and I add a third that neither has named.**

*(Recorded because this sheet's own drafting history is short and the error is instructive: an earlier draft of this section asserted that shortening is "customer-favourable" because "the build leaves the cost base sooner, the price falls sooner." **That is wrong, and the CVO's second count is what exposes it.** Shortening compresses the same build into fewer years, which raises the annual charge and therefore the price. The cliff arrives sooner; the price on the way there is higher. I had the direction backwards and I am not going to bury the correction in a rewrite.)*

#### The first count — it punishes honest under-promising, and the cost falls on early customers

Commit to two years honestly, find in year three that you can support five, and the rule blocks the extension from reaching the price.

**Stated precisely, because the loose version overstates it.** Nothing in the Constitution stops Candour from *doing* five years of support after publishing a two-year commitment; more support is always permitted. What the ratchet blocks is **re-amortising the build over the longer life**. So the build is fully recovered by month 24 at the higher two-year price, and from month 25 the price drops to the post-cliff figure.

**Who actually loses is the early customer, and the number is calculable.** At `N` = 8,998:

| | Honest monthly price, years 1–2 | Years 3–5 |
|---|---|---|
| Two years declared, support later extended to five | **£1.341** | £0.756 |
| Five years declared at the outset | £0.990 | £0.990 |

> **A customer who bought in year one of an honestly-under-promised two-year commitment faces an honest price £4.21 a year higher than the same customer would have faced had the true life been declared — £8.42 over two years — for a product that turned out to have the longer life anyway. There is no mechanism to give it back.** Article 2.3.3.1 sends price reductions to *existing* customers, which reaches those still subscribed and not those who have already churned — and on Haunt's evidenced tenure of five to eight months, most of them will have.

**One qualification a sceptical reader will reach for, so it is made here rather than left to be caught.** That £8.42 is a difference in the **honest** price, which is what this cost sheet publishes. Whether a customer actually pays it depends on what Candour charges: if the monthly price is held at 99p regardless of the period — which is the CEO's anchor — the customer's bill is identical and the difference appears instead as a deeper recorded deviation below target and a higher subscriber count before the price is defensible. **The harm is real in either case; under-promising either overcharges the customer or under-recovers the founder's labour, and the cost sheet shows which.**

**So the ratchet makes the customer-adverse error the permitted one and the customer-favourable correction the forbidden one.** That is the CVO's point and it is right.

#### The second count — the permitted direction is the price-raising one

**Shortening raises prices. Lengthening lowers them.** Declared at the outset, at `N` = 8,998: two years gives an honest £1.341 a month, three years £1.146, five years £0.990. Shortened *mid-life* it is worse still — publish five years, shorten to three at the end of year two, and the unrecovered £44,719 must be recovered in a single remaining year, taking the honest price to **£1.458 a month**, a 47% increase, before it falls off a cliff twelve months later.

> **The Constitution permits the price-raising direction without any justification at all, and forbids the price-lowering direction outright. Article 2.1 requires that every deviation from the margin target be justified in writing; Article 2.3.3.1 makes price reductions for existing customers the first call on the waterfall's remainder. The ratchet as drafted runs against both.**

**Agreed, without reservation. This is the stronger of the CVO's two counts** and it is the one I had backwards.

#### The third count, which is mine — the "must equal" tie freezes the period in *both* directions after launch

The Definitions tie the two periods: *"the amortisation period **must equal** a published support commitment to customers."* Now combine that with CRA 2015 s.36(3), which makes pre-contract information about a product's characteristics a term of the contract:

- **Lengthening** the amortisation is barred by the ratchet.
- **Shortening** the amortisation requires shortening the published commitment to keep the two equal — and a published commitment is contractual, so it cannot be shortened for customers who have already bought.
- **Breaking the tie** (shortening the accounting while keeping the promise) makes the periods unequal, which removes the amortisation treatment altogether and sends the whole remaining build to expense — the worst outcome of the three.

> **So once a period is published and sold against, it is frozen in both directions. The only exit is discontinuation under Article 7.2.** The practical consequence for the CEO is the one that matters: **this is a one-shot, pre-launch decision.** Before launch the period is free to choose. After the first sale it is not choosable at all, and no amount of later evidence about what Candour can actually support will change the price a customer is paying.

#### What the clause gets right, and should keep

Its purpose is named in Correction C3.3(b): *"Declaring a long supported life flatters the cost base, raising the compliant margin at any subscriber count, and is then discontinued early."* **That vector is real and the ratchet does close it.** Any replacement must keep it closed, and the exposing numbers C3.3(b) already names — the published recovered-to-date figure, and the published commitment date against the actual discontinuation date — are the right instruments.

**The defect is not that the clause guards against something imaginary. It is that it guards in one direction and treats the opposite direction as though it were the same act.**

#### Drafted replacement wording

For the CGO to take, amend or reject. **This is an Article 11 amendment either way, and Article 11 amendments belong to the CEO on the CGO's advice. I flag; I do not block.** It would be a **strengthening** and should be labelled as one.

> *The amortisation period equals the product's published support commitment, and a change to either is a change to both. Changes are governed as follows.*
>
> ***(a) Lengthening is permitted*** *where all three of the following hold: the published support commitment is lengthened by at least the same amount; the change is published together with the amount of build labour recovered to date; and the resulting price reduction is applied to existing customers first, under 2.3.3.1. A lengthening meeting all three is a strengthening and is labelled as such under 11.2. A lengthening meeting fewer is prohibited.*
>
> ***(b) Shortening is permitted only before the product's first sale under the published period, or by discontinuation under 7.2.*** *Shortening compresses the same build cost into fewer years, which raises the annual charge and therefore the price, and it shortens a promise that is a term of the customer's contract. It is not the safe direction and it is not permitted without justification.*
>
> ***(c)*** *Any unamortised remainder is written off publicly on discontinuation (7.2).*
>
> ***(d)*** *A product's period is declared before launch and published with its first cost sheet. Where a commitment is later extended under (a), every cost sheet from that point states the original period, the extended period, and the build labour recovered to date.*

**What (a) costs Candour, so it is not adopted on the assumption that it is free.** Permitting lengthening reopens C3.3(b) unless the three conditions bind, and the one doing the work is the recovered-to-date figure: a company that lengthens in order to lower its annual charge must publish how much of the build it has already recovered, so a reader can see whether the extension is real or an accounting move. **That is the same instrument Article 9 already relies on everywhere else — name the number that exposes the vector, then publish it.**

**And if it is not amended, the practical advice for Haunt is unchanged and is now better grounded:** publish the period you will genuinely honour, before launch, because the Constitution as drafted gives you no way back from either direction afterwards.

### 5.6 The pay-once tier loses its anchor — what it becomes

At five years the pay-once tier had an accidental elegance: £59.40 was exactly 60 × 99p. **That anchor is gone at any other life, and the CEO's own decision at C3.0 removed it at five years too** — a tier priced at exactly 60 × 99p saves nothing, which is why UX blocked the savings claim at **B11**.

The honest pay-once price is not an anchor at all. It is the cost of serving a pay-once customer for the supported life, priced by the same rule as every other tier:

| | L = 2 | L = 3 | L = 5 |
|---|---|---|---|
| Honest pay-once price | £19.33 | £28.99 | £48.32 |
| **Charged (nearest grid point)** | **£19.49** | **£28.99** | **£48.49** |
| Per supported-year | £9.75 | £9.66 | £9.70 |
| Against monthly over the same period | £23.76 | £35.64 | £59.40 |
| **Saving** | **18.0%** | **18.7%** | **18.4%** |
| Crossover | 20 months | 29 months | 49 months |

**The saving is ~18% at every life, because it is the same cost saving — twelve avoided billing events a year — expressed over a different number of years.** That is a genuinely reassuring result: the pay-once tier is not an artefact of the five-year number, and it survives the period decision intact.

**Does a pay-once tier still make sense at two years? On the arithmetic, yes — emphatically.** It needs **11,517 distinct buyers spread over 24 months (480 a month)** against the subscription's **2,121 a month**. On a product whose binding constraint is reach, that is a 4.4× advantage at two years and an 11× advantage at five. It is the best instrument in the ladder at every life.

**On honesty, at two years, no — not under that name.** Three things bite at once:

1. **"Pay once" for a product supported for two years invites precisely the reading UX's B11 blocks.** At five years, *"you may never pay again"* is substantially true for most buyers. At two, "pay once" and "prepay two years" are the same thing, and only one of them is an honest label.
2. **The crossover falls at 20 months of a 24-month life.** The tier pays back with four months to spare. That is a narrow enough margin that the pricing screen would have to carry it in body text, and a reader who does the arithmetic would reasonably ask why it is called "once".
3. **Correction C3.2's asymmetry is at its sharpest.** The pay-once buyer does not participate in the cliff cut. At two years a buyer in month 20 prepays through month 44 at the pre-cut rate, on a date when Candour **already knows** the price falls 30% in month 25. That sentence has to appear on the screen, and at two years I do not think it can be written in a way a customer would call fair.

> **This seat's judgment [J]: at a two-year life the tier should be named for its period — *"Two years, paid up front — £19.49"* — not "Pay once". At three years it is borderline and I would still name the period. At five years "Pay once" is defensible, because five years is long enough that the label and the reality substantially coincide, and because UX's stated lift for B11 (the tier named "Pay once", the supported date in body text on the same screen as the price) then does its job.**

---

## 6. The compliant band

**Reference case: the five-year life published at D2.** Every figure below moves with the period exactly as §5.1 shows; the *structure* does not.

### 6.1 Why a fixed price does not have a margin

Because build labour is amortised and dominates, most of Haunt's cost is fixed and is divided across however many subscribers exist. So `C(N) = A/N + s` falls as `N` rises, and **the same price earns a different margin at every subscriber count.**

| Subscribers | 2,000 | 4,000 | **6,369** | 8,000 | **8,998** | 10,000 | **12,152** | 15,000 | 20,000 |
|---|---|---|---|---|---|---|---|---|---|
| Cost of serving one, per year | £18.90 | £11.26 | £8.42 | £7.44 | **£7.01** | £6.67 | £6.13 | £5.65 | £5.14 |
| Realised margin at 99p/month | −51.4% | −22.3% | **0.0%** | +11.0% | **+16.5%** | +21.4% | **+30.0%** | +38.7% | +49.4% |

| Reference point | Subscribers |
|---|---|
| Cost recovery — the founder's benchmarked labour is exactly covered | **6,369** |
| **Candour's pricing rule (16.50%, commission passed through at zero markup)** | **8,998** |
| The ~20% Article 2.1 target | 9,705 |
| **The 30% hard cap, which admits no justification** | **12,152** |
| **Band width** | **1.908×** |

**Read both ends honestly.** Below 6,369 subscribers Candour sells below its own published cost. Article 2.1 permits that with written justification — *"deviations are permitted but must be justified in writing on the cost sheet"* — but it is a deviation, and what it means concretely is that the founder's benchmarked labour is not being recovered. Above 12,152 the price must come down, and Article 2.3.3.1 sends the reduction to existing customers first.

### 6.2 Band width is analytic, and it is not what the CTO expected

Width depends only on the price and the variable cost, never on the fixed cost:

```
width = ( 0.708333·V − s ) ÷ ( 0.516026·V − s )
```

The CTO's indication was that *"the band's position moves; its width does not"*, at 1.60×. **On his own stated basis — variable support unchanged — that is exactly right**: at `s` = £2.3060 the band is **5,006 – 7,996**, width **1.597×**, which reproduces both his 1.60× and his *"of the order of 5,000–8,000 subscribers"* to the digit. Condition 6's re-derivation confirms him.

**Where it moves is the one input he handed to me.** He wrote *"plus a subscription uplift the CFO should set"*. Setting it at §2.4 raises the monthly tier's variable cost from £2.3060 to £3.6140, which raises the position **and** widens the band to **1.908×**, because `s` appears in both the numerator and the denominator of the width expression. **So the width is invariant to the build estimate and sensitive to the support estimate.** That is the honest correction to his indication, and it runs against the product, not for it.

### 6.3 Correction — discounts do not collapse the band, and Condition 9.3 carries my error

**Condition 9.3 of the decision record states:** *"At 25% off, 1.05×, which is not a band. A discount curve deeper than roughly 10% has no subscriber count at which every tier is simultaneously compliant."* That finding is mine, from `pricing-ladder-model.md` §2.3. **It is wrong, and the defect is a method error rather than an arithmetic one.**

**What I did.** I justified each tier's discount by the billing events it avoids — *"what a longer commitment saves is billing events"* — and then computed every tier's band using **the same variable support cost for all tiers**. A tier cannot both cost less to serve (for the purpose of setting its price) and cost the same to serve (for the purpose of testing its margin). **The discount was funded from a saving the model then declined to carry.** With the saving carried, the discounted tier's floor barely moves, because its revenue and its cost fall together.

The same table, computed both ways, on the current cost base, against the monthly tier's 30% ceiling of 12,152:

| Yearly tier's discount | Floor, **common `s`** (my error) | Floor, **tier-specific `s`** (correct) | Blended width, corrected |
|---|---|---|---|
| 0% | 5,097 | 5,097 | 2.384× |
| 10% | 6,320 | 5,928 | 2.050× |
| **16.75% (the proposed ladder)** | **7,222** | **6,662** | **1.824×** |
| 25% | 8,720 | 7,848 | 1.548× |
| 30% | 10,048 | 8,799 | 1.381× |
| 40% | 14,168 | 11,610 | 1.047× |
| 45% | — | 13,817 | **0.880× — no band** |

> **Corrected finding: the blended band closes at a discount of roughly 41%, not 25%. A discount that is exactly cost-anchored costs the band almost nothing; a discount deeper than its cost anchor costs it roughly 1.4 percentage points of floor per point of excess.**

**Two consequences and I am not softening either.**

1. **Condition 9.3 of a decision record due for publication on 2026-10-16 contains a finding of mine that is wrong.** It must be corrected in the open before publication, not silently superseded. The owner of the record is the CGO and the classification is the CGO's to propose; **from this seat it is a CORRECTION — the statement was false when written, not superseded by a change of mind.** §16.3.
2. **The second arithmetic correction is smaller and travels with it.** `pricing-ladder-model.md` §3.2 computed each tier's discount as the cost saving divided by the *shelf price*, giving 7.34% and 10.10%. The cost saving must be passed through the pricing rule — a saving of £0.872 a year lowers the shelf by £0.872 × 1.694118 = £1.477, not £0.872. The correct cost-anchored discounts are **12.4%, 17.1% and 18.7%**, not 7.3%, 10.1% and 11.0%. **This is the third arithmetic error found in this pack by re-derivation and the second of mine.** Condition 6 exists because of exactly this, and it worked.

### 6.4 Sensitivity — what moves the band, in order of size

At 99p/month, five-year life, point cost base unless stated:

| What moves | Cost recovery at | 30% cap at |
|---|---|---|
| **Base case** (`A` = £30,579.57) | **6,369** | **12,152** |
| Build alone at the CTO's low, 1,958 h capitalised | 5,933 | 11,320 |
| Build alone at the CTO's high, 2,598 h capitalised | 6,805 | 12,984 |
| **Whole cost base at the low end** (build *and* fixed labour low; `A` = £25,640.36) | **5,341** | **10,189** |
| **Whole cost base at the high end** (`A` = £35,813.17) | **7,460** | **14,232** |
| Billing-event cost `e` = £0 (the CTO's unchanged variable basis) | 5,006 | 7,996 |
| `e` = £0.0545 (0.5% of events × 20 min) | 5,606 | 9,645 |
| **`e` = £0.3271 (2% × 30 min)** | **14,003** | **never — the cap is unreachable** |
| Security/defect line added at +45 h/yr (§4.1) | 6,676 | 12,737 |
| 100% iOS (variable support falls to £2.53) | 5,200 | 8,504 |
| 100% Android (variable support rises to £5.23) | 9,611 | 34,084 |

**Two of these deserve a reader's attention more than the rest.**

**The billing-event assumption is now the largest single uncertainty in this sheet**, ahead of the build estimate. At `e` = £0.3271 — two per cent of renewals generating a half-hour contact — a monthly subscriber costs more to serve than 30% of what they pay, so **the hard cap becomes unreachable at 99p and the price can never be non-compliant upward.** That is not a comfortable finding; it means the model's answer at the top end is sensitive to a parameter nobody has measured. It is measurable free in App Store Connect within 90 days of launch.

**The platform mix is doing real work and it is a guess.** 60/40 is [J] and always has been — no seat in this pipeline has ever had evidence for it. At 100% iOS the band is 5,200 – 8,504; at 100% Android it is 9,611 – 34,084, because an Android subscriber costs £5.23 a year to support against an iOS subscriber's £2.53. **The band is nearly twice as wide and almost twice as high on Android alone, and the CEO has just committed to both platforms.** This is testable free in the Play Console's mandatory 12-tester closed test before a penny of price is published.

---

## 7. The ladder

### 7.1 How each tier's price is derived

Every tier is priced by the **same rule** — cost of serving that tier, times 1.694118 — at the **same subscriber count**. That is what "a real discount on the same curve" means arithmetically, and it is what Correction C3.0 asked for.

At the five-year reference `N*` = 8,998, where `A/N` = £3.3985:

| Tier | Variable cost `s` | Cost of service per year | Honest price per year | Honest price per billing period |
|---|---|---|---|---|
| Monthly | £3.6140 | £7.0125 | £11.880 | **£0.9900/month** |
| Quarterly | £2.7420 | £6.1405 | £10.403 | **£2.6007/quarter** |
| Yearly | £2.4150 | £5.8135 | £9.849 | **£9.8488/year** |
| Pay once | £2.3060 | £5.7045 | £9.664 | **£48.320 once** |

**The discount is made of one thing and it is not generosity.** Apple and Google charge the same percentage regardless of billing period; there is no hosting; the product is identical in every tier. **What a longer commitment saves is billing events**, and nothing else. That is why the curve is *concave* — monthly to quarterly avoids 8 events a year, quarterly to yearly avoids 3 more, yearly to pay-once avoids 1. A ladder that accelerated, giving bigger discounts for longer commitments, would not be describing any cost Candour has.

### 7.2 The rounding rule, applied

**Apple's UK price grid, retrieved at source this session** [E, [Apple, *App Store Pricing Update*](https://www.apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf), "United Kingdom (GBP)", text-extracted from the PDF, retrieved 2026-09-20]:

- **Price steps:** £0.10 from £0.29 to £9.99 · £0.50 from £0.49 to £49.99 · £1 from £0.99 to £199.99 · £5 from £4.99 to £499.99 · £10 from £9.99 to £999.99 · £100 from £99.99 to £9,999.99 · £1,000 from £999.99 to £11,999.99
- **Supported conventions:** X.99 (£0.99–£11,999.99) · X.00 (£1–£10,000) · X.90 (£0.90–£99.90) · X.95 (£0.95–£49.95)

**The rule (proposed as a standing published Candour convention, not a Haunt one):**

> 1. The honest price is computed first, to the penny, from the published cost sheet at the stated margin. **That figure is published on the cost sheet regardless of what is charged.**
> 2. The charged price is the **nearest available conventional price point to the honest price, in either direction.** Where two are equidistant, the **lower** is taken.
> 3. **The nearest point is never taken if it would carry the margin above 30%.** Article 2.1's backstop admits no justification and a rounding convention is not one. Where the nearest point breaches, the next point **down** is taken.
> 4. Every rounding is recorded on the cost sheet: honest price, charged price, displacement in pence and per cent, and the realised margin at the charged price.
> 5. The rule applies identically to increases and decreases and is never re-selected per instance.

**Clause 2 is the whole of the correction to the CEO's "always round up".** Applied at every republication across a product's life, always-upward is a standing, invisible margin uplift that no cost sheet would ever show as a deviation, because each individual instance is too small to argue with. A symmetric rule has an expected displacement of approximately zero across many republications; an always-upward rule has an expected displacement of half a step, every time, for ever. **That is the structure Article 9's *"Quietly weakening the rules"* row exists to catch.** On the CEO's own worked example the nearest conventional point to £75.40 is **£75.00**, not £75.99.

**Its effect on this ladder, per tier:**

| Tier | Honest price | Nearest points available | **Charged** | Displacement | Effect on margin |
|---|---|---|---|---|---|
| Monthly | £0.9900 | £0.99, £1.00, £0.95, £0.90, £1.09 | **£0.99** | **0.00%** | none — lands exactly on a point |
| Quarterly | £2.6007 | £2.59, £2.69, £2.49, £2.79 | **£2.59** | **−0.41%** | 16.50% → **16.11%** |
| Yearly | £9.8488 | £9.89, £9.90, £9.79, £9.95, £9.99 | **£9.89** | **+0.42%** | 16.50% → **16.91%** |
| Pay once | £48.3205 | £48.49, £48.00, £47.99, £47.95, £47.90 | **£48.49** | **+0.35%** | 16.50% → **16.84%** |

> **The rule's maximum effect is half the local step: ±5p at the monthly tier (±5.1%), ±5p at the yearly tier (±0.5%), ±50p at the pay-once tier (±1.0%). On this ladder the realised effect is between −0.41% and +0.42%, and it is not all in the same direction — which is the point of a symmetric rule.**

**Why this is not housekeeping at the monthly tier.** At `N` = 9,705, one 10p step spans this:

| Monthly price | £0.79 | £0.89 | **£0.99** | £1.09 | £1.19 |
|---|---|---|---|---|---|
| Realised margin | −0.6% | +9.9% | **+20.0%** | +29.8% | +39.2% |

> **One available price step covers the entire distance from Article 2.1's target to within 0.2 percentage points of the hard cap. At a 99p price point, Apple's price grid has lower resolution than Candour's constitution.**

Three consequences: rounding is the **dominant** determinant of margin at the monthly tier, ahead of every cost assumption in this sheet; **clause 3 is load-bearing, not belt-and-braces**, because a single upward round can carry the product through the cap in one move; and **Haunt cannot be priced accurately at a monthly cadence** — the quarterly and yearly tiers have four and twelve times the resolution for the same annual revenue.

**One limit on the rule, stated so it is not assumed.** I retrieved Apple's published GBP step-and-convention grid; I did **not** retrieve the complete list of 800 price points as it appears inside App Store Connect, which Apple does not publish. The tables above should reproduce it, but **the exact nearest point must be confirmed in App Store Connect before any price is published**, and Google Play's GBP grid is a separate list I have not retrieved at primary. Two stores may not offer the same nearest point. §17.

### 7.3 The published prices, and the margin recorded at every tier

**Article 2.1 as amended requires the margin to be recorded at each tier, and a deviation in either direction to be recorded as a deviation.** All four are below target; none is above the cap.

| Tier | **Charged** | Per month | Per year | **Margin at `N*`** | **Deviation from ~20%** | Cause of the deviation |
|---|---|---|---|---|---|---|
| **Monthly** | **£0.99** each month | £0.9900 | £11.88 | **16.50%** | **−3.50 pp** | Store commission passed through at zero markup (§3.1) |
| **Quarterly** | **£2.59** every 3 months | £0.8633 | £10.36 | **16.11%** | **−3.89 pp** | Pass-through (−3.50) + rounding down to the nearest point (−0.39) |
| **Yearly** | **£9.89** each year | £0.8242 | £9.89 | **16.91%** | **−3.09 pp** | Pass-through (−3.50) + rounding up to the nearest point (+0.41) |
| **Pay once** | **£48.49** once | £0.8082 | £9.698 equivalent | **16.84%** | **−3.16 pp** | Pass-through (−3.50) + rounding up to the nearest point (+0.34) |

**Monotonic by construction, not by taste:** £0.9900 > £0.8633 > £0.8242 > £0.8082 per month. Each longer commitment is strictly cheaper per unit time than every shorter one, because each avoids strictly more billing events.

**Blended compliant band across the ladder: 6,701 – 11,332 subscribers (1.69×).** The floor is set by the pay-once tier and the ceiling by the pay-once tier; the monthly tier alone would run 6,369 – 12,152.

**The per-unit table the pricing screen must show** (UX's B12 requires all of it in one view, at equal type size, with no tier pre-selected):

| Tier | Charged | Per month | Per year | Saving vs monthly |
|---|---|---|---|---|
| Monthly | £0.99 each month | **£0.99** | £11.88 | — |
| Quarterly | £2.59 every 3 months | **£0.86** | £10.36 | £1.52 a year — **12.7%** |
| Yearly | £9.89 each year | **£0.82** | £9.89 | £1.99 a year — **16.7%** |
| Pay once | £48.49 once | **£0.81** over five years | £9.70 equivalent | £10.91 over five years — **18.3%** |

*(Savings rounded **down**, never up, per UX's §3.2. Arithmetic re-derivable: 2.59 ÷ 3 = 0.8633; 9.89 ÷ 12 = 0.8242; 48.49 ÷ 60 = 0.8082; 59.40 − 48.49 = 10.91.)*

> **The pay-once tier now genuinely saves money, which is what UX's block B11 required before any saving could be claimed. 18.3% over five years, £10.91 in cash. That claim is substantiable and may be printed.**

---

## 8. The cumulative lifetime margin test — modelled both ways, and closed

**The clause.** Constitution v1.2, Article 2.1: *"Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit **against the cost of serving them**. A recurring price whose every individual year is compliant can still breach this document over a decade, and the cumulative test is what catches it."*

I have flagged twice that *"the cost of serving them"* may make this clause a no-op. The CGO holds the interpretation as a standalone determination due 2026-10-16. **I was asked to model it both ways so the CEO can see whether the answer changes any price. It does not, and here is why.**

### 8.1 The two readings

| | **Reading 1 — incremental** | **Reading 2 — pro-rata** |
|---|---|---|
| What *"the cost of serving them"* means | The share of the one-off build attributable to this subscriber, charged **once**, plus their own years of fixed and variable cost | This subscriber's pro-rata share of **that year's total product cost**, every year they stay |
| Cost after `t` years | `B/N` + `t × (F/N + s)` | `Σ` of each year's `C(N)`, where the build is in the cost base only while it is being amortised |
| Why it might matter | The build is paid for once; after year `L` the subscriber keeps paying and the build has gone | The cumulative test simply replays the annual test |

*(A third reading — that "the cost of serving them" means marginal cost alone, i.e. `s` — is not available. Correction C1.2 already disposed of it: the Definitions define Cost as *"everything it takes to run a product or the company, itemised… and labour valued at a published market benchmark whether or not it is actually paid"*, and Article 9 names redefining "cost" as a gaming vector. On that reading the cumulative margin at five years is **+94.2%**, which is the reductio.)*

### 8.2 The readings coincide exactly where the test binds

Cumulative margin, monthly at a flat 99p with no step-down, `N` = 8,998:

| Tenure | 1 yr | 2 | 3 | 4 | **5 yrs** | 6 | 7 | 10 | **11 yrs** | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Reading 2 (pro-rata)** | 16.50% | 16.50% | 16.50% | 16.50% | **16.50%** | 20.42% | 23.38% | 29.09% | **30.37%** | 31.45% |
| **Reading 1 (incremental)** | −34.54% | −9.86% | +3.10% | +11.09% | **16.50%** | 20.42% | 23.38% | 29.09% | **30.37%** | 31.45% |

> **The two readings produce identical numbers at every tenure at or beyond the supported life, and Reading 1 is strictly *harsher* below it.** They must coincide at `t ≥ L`, because by then the build has been fully allocated under both. **And the test only ever binds upward — a subscriber *"must not, merely by staying, pay materially more"* — so it binds only in the region where the readings agree.**

### 8.3 And in every case the annual test breaches first, by five years

| | Annual 30% cap breached in | Cumulative 30% cap breached at |
|---|---|---|
| L = 2, flat 99p, `N*` = 15,577 | **year 3** | year 4 |
| L = 3, flat 99p, `N*` = 11,922 | **year 4** | year 6 |
| **L = 5, flat 99p, `N*` = 8,998** | **year 6** (margin +44.7%) | year 11 |

> **Determination, from this seat, on the arithmetic only: the interpretation of *"the cost of serving them"* changes no price for Haunt, under either reading, at any supported life. The annual test in Article 2.1 catches the amortisation cliff five years before the cumulative test does, and the cliff is the only mechanism on Haunt's cost shape that makes cumulative margin rise at all.**

**What that does and does not settle.**

- **It settles my open item.** I flagged this twice and it is closed: it is no longer a bar on publishing a price, and it is no longer a reason for me to hold a block. §16.
- **It does not settle the interpretation**, and I am not settling it. The evidence standard is explicit that *"a process that answers an interpretive failure by adding agent passes is prescribing more of what already failed"*, and settling a constitutional definition inside a cost sheet is precisely how a heuristic becomes law. **The determination remains the CGO's, due 2026-10-16, with the CEO deciding.**
- **The clause is not a no-op, but it is nearly one.** On Haunt's cost shape I could not construct a case where the cumulative test binds and the annual test does not. Its real function is rhetorical and it is a good one: it names the year the existing obligation falls due. But **a clause that never binds independently should be known to never bind independently**, rather than carried as a live protection it is not. I record that as a finding about the Constitution, for the CGO's determination to take or leave.

### 8.4 The step-down resolves it completely and permanently

Stepping the price down to the honest post-cliff figure stabilises cumulative margin at exactly the annual margin, at every tenure to infinity:

| Tenure | 1 | 3 | 5 | 6 | 7 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|
| Cumulative margin with the step-down | 16.50% | 16.50% | 16.50% | 16.50% | 16.50% | 16.50% | 16.50% | 16.50% |

**This is not a new duty.** Article 2.1 already requires republication *"at every price change"*; Article 2.3.3.1 already makes *"Price reductions for existing customers"* the first call on the remainder; and Apple performs the reduction on the installed base automatically and does not permit preserving the old price. **The cumulative test does not add an obligation. It names the year the existing one falls due, and the store enforces it.**

### 8.5 The pay-once tier is outside the test, and that is a named gaming vector

A pay-once buyer's cumulative margin **falls** with tenure, because revenue stops and cost does not. At `N*`, five-year life, £48.49:

| Tenure | 1 yr | 3 | **5 yrs** | 6 | 10 |
|---|---|---|---|---|---|
| Cumulative margin | +243.4% | +74.4% | **+16.8%** | +4.6% | −26.3% |

**So the cumulative test never catches a pay-once tier. The *annual* test catches it, in the year of purchase, and hard** — the whole five years of revenue arrives at once. The accounting answer is that pay-once revenue must be **recognised over the supported life**, not in the year of receipt, exactly as the build cost is. **If it is recognised on receipt, the annual margin in the year of purchase is +243% and the cost sheet is not describing anything real.**

**The gaming vector, named rather than used** (Correction C3.3(a) already records it; this is the number that exposes it). A company facing an automatic, unpreservable price cut at the cliff has exactly one lawful escape: push new customers onto pay-once, which sits outside the cumulative test and whose price Apple does not reduce automatically. **The exposing number is the one in the table above: publish the annual margin on every tier, including one-off tiers, at every republication, and the escape is visible the moment it is attempted.** I recommend that row be added to Article 9's table at the next amendment. **This is a flag; Article 11 amendments belong to the CEO on the CGO's advice.**

---

## 9. The crossover — an Article 1.3 problem before it is a margin one

**Article 1.3:** *"**Honest by default.** Pricing, capability, and limitations are stated plainly. We say what a product cannot do."*

| Tier | Per subscriber-year | **Overtakes £48.49 at** |
|---|---|---|
| Monthly £0.99 | £11.88 | **4 years 1 month (49 months)** |
| Quarterly £2.59 | £10.36 | 4 years 8 months |
| Yearly £9.89 | £9.89 | 4 years 11 months |

**This moved because the CEO's decision at C3.0 moved it, and the movement cuts both ways.** At exactly 60 × 99p the crossover fell precisely at the end of the supported life and nobody was worse off on either path — which was clean, and which was also why there was no saving to claim and why UX blocked the claim. **With a real 18.3% discount there is a saving, and the price of having one is that the crossover now falls eleven months *inside* the supported life.**

> **Concretely: a customer who pays monthly and stays for the whole five years Candour has promised to support pays £59.40. The same customer paying once pays £48.49. The monthly customer pays £10.91 more for the identical product.**

**That is not a margin breach** — both tiers are inside the band and both are below target. **It is a disclosure obligation**, and it is the kind that Article 1.3 exists for: the fact decides the choice, neither store will tell the customer, and a customer who works it out later will reasonably feel they were not told.

**The sentence the pricing screen must carry, drafted** (UX reached the same requirement from the design side at `ux-note-pricing.md` §3.2, and the CFO from the cost side — **one requirement, two seats, not two independent findings**):

> *"Paying monthly costs £11.88 a year. Paying once costs £48.49 and covers the whole period we've committed to supporting Haunt — until [date]. If you subscribe monthly and stay the whole time, you'll pay £59.40, which is £10.91 more. Paying once also means there's nothing to cancel, and it keeps working after [date]."*

**And the second sentence, which is the honest half of selling both shapes** (Correction C3.2, UX §3.4):

> *"Paying once means you don't take part in future price cuts. We review this price every year and publish the numbers, and when the build cost finishes being paid off in [month year] the subscription price falls. If you're subscribed, your renewals drop automatically — the App Store doesn't give us the option to keep you on the old price."*

**Both sentences are true, both are checkable against this cost sheet, and I do not think the pay-once tier can be sold honestly next to a subscription without them.**

---

## 10. The amortisation cliff

**What happens.** At the end of the published supported life the amortised build leaves the cost base. Nothing about the product changes; the cost of serving a customer falls by about a third; and Article 2.1's cap makes the price follow.

**At the five-year life, `N` = 8,998:**

| | Years 1–5 | **Year 6 onward** |
|---|---|---|
| Cost of serving one subscriber per year | £7.0125 | **£5.3559** |
| Honest monthly price | £0.990 | **£0.756** |
| **Charged monthly price after rounding** | **£0.99** | **£0.79** |
| Margin if the price is **not** changed | 16.50% | **+44.7% — more than the cap permits** |
| **Size of the cut** | | **20.2%** |

**The whole ladder after the cliff, at the same `N`:**

| Tier | Years 1–5 | **Year 6 onward** | Cut | Margin after |
|---|---|---|---|---|
| Monthly | £0.99 | **£0.79** | 20.2% | 20.78% |
| Quarterly | £2.59 | **£1.90** | 26.6% | 16.55% |
| Yearly | £9.89 | **£7.00** | 29.2% | 15.93% |
| Pay once | £48.49 | **£34.49** | 28.9% | 17.07% |

**The date.** It is **launch + the published supported life**, and Candour can calculate it on the day Haunt launches. It is not calculable today because the launch date is not set: the CTO's 2,090-hour build is 55.75 focused solo weeks, which for a part-time operator is multiple calendar years, and the calendar is the PM/BA's to model. **The cliff date must appear on the pricing screen and on every republished cost sheet from launch onward** — not as a forecast but as a commitment, because Candour will already know it.

**Article 2.3.3.1 lands it on the installed base, and Apple makes it irreversible.** *"Price reductions for existing customers"* is the first call on the waterfall's remainder; Apple's own documentation says existing subscriptions *"will automatically renew at the lower price"* and *"You don't have the option to preserve the higher price for existing subscribers"* [E, retrieved 2026-09-20, cited in full at §5.4]. **The ratchet runs one way and the store enforces the direction Candour's constitution wants.**

**One correction to the CTO's indication, since Condition 6 requires re-derivation and this is a case where it changes the answer.** The CTO's §10.4(2) states that *"Condition 9.4's year-six step-down gets larger, not smaller… the amortised build has grown by 62%. A larger share of the cost base falls away on a single calculable date, so the step is steeper than ~32%."*

**The premise is right and the conclusion does not follow.** The cut's size is set not by the *absolute* build but by the build's share of the cost of serving **one subscriber**, and both the build and the fixed costs grew by almost exactly the same proportion — the amortised build is 48.2% of `A` in the old model and 48.7% in this one. On the CTO's own unchanged variable basis the cut is **32.7%**, essentially unchanged from the 32% in Condition 9.4. **Once the subscription billing uplift is carried, the cut gets *smaller*, to 20.2%**, because a bigger share of each subscriber's cost is variable support, which does not fall away. **The step is not steeper. It is flatter, and the reason is a cost line the CTO asked me to add.**

---

## 11. The two items nobody had costed, now carried

Both were raised by other seats after every prior price was set. Both are in the figures above rather than outside them.

### 11.1 The DMCCA requirements R1–R5

The Digital Markets, Competition and Consumers Act 2024's subscription-contracts regime does not bite on a one-off purchase. **The CEO's subscription revives it.** The CGO determined the commencement date at source — **January 2027**, correcting our own file, which carried "spring 2027" from a stale single-origin briefing [E, `subscription-compliance-note.md` §1.4, GOV.UK press release of 9 August 2026, retrieved by the CGO 2026-09-18].

**The finding that matters commercially: the duties are dischargeable on this architecture without collecting anything.** I had recorded the durable-medium reminder duty as *"possibly the largest unpriced item in this model"* and inferred it would force Candour to collect an email address. **That inference was not supported by the primary source and the CGO corrected it at source**: the Government's own guidance excludes only *"an in-app message/notification **which appears briefly but cannot be retained and revisited**"*, so a persistent, retainable in-app notice is not excluded [E, DBT Annex B Q23, retrieved by the CGO 2026-09-18, `subscription-compliance-note.md` §4.2]. **No email, no account, no server, and Haunt's "collects nothing" claim survives intact.** That correction is the single largest cost item this pack removed rather than added, and it came from a seat correcting me.

**What is carried, sized by the CTO:**

| | Content | Hours |
|---|---|---|
| R1 | Schedule 23 pre-contract information mapped onto App Store metadata and the first-run disclosure screen | 19 |
| R2 | Persistent, append-only in-app notices surface — never auto-clearing, included in the export by construction | 19–37 |
| R3 | Notice scheduling from the persisted entitlement interval table, with a paired local notification and a fallback for customers who decline notifications | 19–37 |
| R4 | Plainly-labelled cancellation control deep-linking to Apple's own Manage Subscriptions, with **no retention offer, no confirm-shaming, no friction** | 9 |
| R5 | Discharged by the CTO's own answer on StoreKit entitlement availability | 0 |
| | **Total** | **66–103 h, point 84 h — £2,747.64 at benchmark** |

**Two things a customer should know about R4 specifically.** Article 4 requires that Candour *"Make cancellation as easy as signup"* and deploy *"no dark patterns… no confirm-shaming"*. On this architecture Candour **cannot** build a save-flow even if it wanted to: with no server it does not learn that a cancellation happened until the entitlement lapses. **The architecture forecloses the dark pattern**, and that is a genuine consequence of the zero-network design rather than a promise to be taken on trust.

**What is not in this number and is not sizeable:** the proportionate-refund duty. §2.6.

### 11.2 Venue-index remediation

The Engineer's spike measured the bundled venue index and found it **not shippable as specified** for a product whose core value is an accurate per-venue history: top-five hit rate 58.3% at a perfect location fix, ≈28% in a dense city centre at a realistic 25 m location error, and — the measurement nobody asked for — **100% of dense-centre venues had their top candidate change across 20 simulated visits, with a median of 10 different venues taking first place** [E, `venue-index-spike.md` §§4–6, Engineer's own measurements, retrieved 2026-09-20].

**Why that is a cost and not a bug.** Gate Condition 8.6 requires that *"Derived views never lie about the user's own life… A venue page must never show '3 visits, average 3.8' when the true figures are 11 and 4.2."* An unstable venue identity produces exactly those figures, silently, because the customer chose honestly from an honest list each time.

| | Content | Hours |
|---|---|---|
| Pre-build spike (CTO Block 4) | Re-establish the measurement harness as a permanent fixture; rebuild the category scope; test whether any ranking signal fixes rank-1 instability | **113** |
| Build | Ranking layer beyond raw distance; **copy-on-reference** venue rows so a dataset refresh can never mutate a row a customer's visit already points at; refresh reconciliation tooling; "this venue isn't listed" promoted to a first-class path at a **22% genuine absence rate** | **150–225, point 188** |
| Annual | Refresh becomes **reconciliation**, quarterly rather than monthly | **60–100/yr, point 80** |
| | **Capital £9,845.71 · annual £2,616.80** | |

**The single cheapest line in the whole pack, and the most expensive to retrofit:** *a dataset refresh must never mutate venue rows already referenced by a customer's visit.* With no server, no telemetry and no backfill, a refresh that corrupts referenced rows is **permanent, silent, and undiscoverable by Candour**. It is in the build figure above because it is in the schema, and putting it in the schema later means migrating every customer's history on a product that cannot see any of it.

**The honest caveat: the build portion assumes the spike passes.** If it does not, these hours do not arise and a different conversation does — one about whether the venue page, which the CEO has called *"probably the product, not a feature"*, can exist at all.

---

## 12. The honest reach number

**This is the number the CEO should read before the price.** Everything above says what Haunt must charge. This says how many people must buy it.

### 12.1 Break-even, over the five-year supported life

Total published cost over five years: **£152,897.83**.

| Tier | Contribution per customer | **What break-even requires** |
|---|---|---|
| **Monthly £0.99** | £0.40008 per subscriber-month | **382,165 subscriber-months** = 6,369 subscribers held continuously for 60 months |
| Quarterly £2.59 | £0.38303 per subscriber-month | 399,182 subscriber-months = 6,653 held continuously |
| Yearly £9.89 | £0.38253 per subscriber-month | 399,697 subscriber-months = 6,662 held continuously |
| **Pay once £48.49** | £22.817 per buyer over five years | **6,701 distinct buyers, cumulative** |

### 12.2 And with churn, which is what actually binds

"Held continuously" is doing all the work in the table above. Subscribers leak, and the number of **distinct people who must ever subscribe** is what a reach-constrained product is really being asked for:

| Average tenure | **Distinct subscribers needed** | **New subscribers every month, sustained for five years** |
|---|---|---|
| 4.5 months (Social & Lifestyle, pessimistic) | **84,926** | 1,415 |
| **5.2 months (Social & Lifestyle, central)** | **73,493** | **1,225** |
| 6.3 months (Travel, central) | 60,661 | 1,011 |
| 7.6 months (Travel, optimistic) | 50,087 | 835 |
| 13.2 months (business-like upper bound) | 28,952 | 483 |
| **Pay once** | **6,701** | **112** |

**On the three-year life recommended at §14, the same table reads: 58,426 distinct subscribers at 5.2-month tenure, 1,623 new subscribers a month sustained for three years, or 8,927 distinct pay-once buyers at 248 a month.** The totals are smaller because the cost base is smaller; the **rates** are worse because the window is shorter. §5.1 carries all three lives.

*(Tenure figures are the retrieved category renewal benchmarks carried forward from `pricing-ladder-model.md` §4.2. **Both the conversion and the renewal benchmarks originate with a single publisher (RevenueCat) and have now been flagged as single-origin in four artifacts.** Under the evidence standard's *"Twice-flagged is escalated"* this is long past escalation and is listed at §17.)*

### 12.3 Has it moved? Yes — by 2.6×

| | Earlier figure | **This sheet** |
|---|---|---|
| Basis | Three-year cost base, £75,626.91 | **Five-year cost base, £152,897.83** |
| Distinct subscribers | **19,483 – 33,012** | **50,087 – 84,926** |

**Two-thirds of the increase is cost and one-third is the longer window**, and a reader should have both stated rather than one. A five-year commitment is not only a bigger number to recover; it is a bigger number recovered over more years, which is why the *monthly acquisition rate* — 1,225 a month — is the figure that actually describes the difficulty, and it is the one that gets **worse** at a shorter life, not better (§5.1: 2,121 a month at two years).

### 12.4 The negative finding, stated as my charter requires

> **Haunt is not unviable at a compliant price. It is unviable at 99p on any reach this company has evidence for — and it is priceable, compliantly and honestly, at between £1.30 and £2.40 a month on volumes it might actually reach.**

The distinction matters and I am not going to blur it. At 4,000 subscribers the honest monthly price on a five-year life is **£1.59**; at 2,000 it is **£2.67**. Both are ordinary consumer app prices, both are fully compliant, both would be publishable with this cost sheet beside them, and neither is 99p. **What the arithmetic rejects is not the product. It is the combination of 99p and a subscriber base in the low thousands.**

**The context that makes this a finding rather than a quibble:** the category leader has **164 UK ratings after a decade** [E, carried forward from the discovery pack; **vendor-origin and never independently verified — Condition 3 was waived and nobody has installed the application**]. Haunt has no acquisition channel, and no seat in this pipeline has ever written down a reach multiple. **1,225 new subscribers every month for sixty consecutive months is not a stretch target against that background; it is a different business.**

**What would overturn this finding** *(required by my charter: a negative finding carries a block's duty)*:

1. **A measured average tenure above about 14 months**, which is where the subscription stops needing more distinct people than a one-off. Measurable free in App Store Connect's subscription reporting within 90 days of launch. The retrieved category medians put Haunt at 5–8 months.
2. **An acquisition channel nobody has written down.** The reach multiple `r` has been absent from every artifact in this repository since the idea brief, and I searched again this session. **Absent, not merely unverified.**
3. **A decision to lead with the pay-once tier**, which needs 6,701 distinct buyers over five years — 112 a month. That is a target this company could plausibly describe. **It is the only route in this document on which the reach constraint stops binding**, and it is §14's recommendation.
4. **A CEO decision to run a deliberate, published, sustained deviation below target**, which Article 2.1 permits with written justification and which would mean accepting that the founder's benchmarked labour is not recovered. That is not a failure of the model; it is the decision the gate already recorded — *"I quite like this idea for myself personally and if I can release it and it makes a bit of money then I am happy with that."*

**Where I looked:** every cost input in §2, re-derived from the CTO's and Engineer's own tables rather than from any prior summary; the retrieved churn and conversion benchmarks; `research/haunt-brief.md`, `proposals/haunt/`, the feasibility note, the Android note, both UX notes and both compliance notes, for a reach multiple or an acquisition channel — **found in none of them**; and the honest-price-by-volume table at §5.3, which is where the finding's "not unviable" half comes from.

**Counter-argument I am obliged to record against my own recommendation.** The pay-once reach advantage is *per person who buys*, not per person who sees the listing. A £48.49 up-front price converts worse than 99p a month, and **nobody has measured by how much, on this product or any other.** If pay-once converts eight times worse than monthly, the advantage disappears entirely. **That is the weakest link in §14 and it is testable in the same 12-tester closed test as everything else.**

---

## 13. The Article 9 shared-fee allocation rule — proposed and closed

**The problem, which is mine and which I raised twice without proposing a fix.** Two of Haunt's cost lines are **company** costs, not Haunt costs: the Apple Developer Program membership (£73.91/yr, which covers every app Candour ever ships) and the ICO data protection fee (£52.00/yr, which is levied on the organisation). Google Play's £18.66 registration is the same. This sheet charges **100% of all three to Haunt**, because Haunt is the only product that exists.

**Why that is a loophole running by default rather than by intent.** Article 9's first named loophole is *"Inflating costs to raise the allowable price (2.1)"*. Article 2.1 says: *"Margins are per product, never averaged across the portfolio: each product's customers get that product's honest number, and no customer subsidises another product unknowingly."* That clause guards against cross-subsidy in one direction. **The mirror problem is charging one product 100% of a cost that will later serve several** — and it becomes a live overcharge the moment Candour ships a second app, because a price set today does not come back down on its own.

**Proposed rule, for the CEO to adopt as a standing company convention:**

> **Shared-cost allocation.** A cost is **shared** if it would be incurred in the same amount were any one Candour product not to exist — company registrations, platform developer memberships, the ICO fee, and company-level tooling. Shared costs are allocated **equally across live products** at each annual republication. A product that launches or is discontinued part-way through a year carries a pro-rated share for the months it was live.
>
> **Three things travel with it.** (1) Every cost sheet states, on its face, the number of live products the allocation was made across and the per-product amount — so a reader can see when it changes. (2) Reallocation happens at the **next annual republication** after a product launches, not at the moment of launch, so allocation never becomes a reason to delay or accelerate a launch. (3) The resulting price reduction for an existing product goes to existing customers first, under Article 2.3.3.1.
>
> **Applied to Haunt today: 1 live product; Haunt carries 100% of £125.91 a year in shared fees, and this sheet says so. On the day a second product ships, Haunt's share falls to £62.96 and its price is reviewed down at the next republication.**

**The honest proportion, so nobody spends more time on this than it is worth.** Shared fees are **0.42% of the annual cost base** (£129.64 of £30,579.57, including the pro-rated Google registration). **This is a governance fix, not a money fix.** It is worth making now precisely because it costs nothing to settle while Haunt is alone, and because Article 9's commitment is explicit: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* Settling it after the second product ships would mean settling it while somebody's price depends on the answer.

**I recommend a corresponding row in Article 9's loophole table:** *"Charging one product 100% of a shared company cost — exposed by every cost sheet stating the number of live products the shared-cost allocation was made across."* **This is a flag; Article 11 amendments belong to the CEO on the CGO's advice.**

---

## 14. Recommendation

My charter requires a recommendation with a reason rather than a menu. There are two decisions on the table and I give one answer to each.

> ### On the period: publish **three years**, dated, product-level, before requirements are signed off.
>
> ### On the price: ship the ladder with the **pay-once tier as the headline** — £28.99 at three years — with monthly at 99p as the convenience tier, quarterly at £2.59, yearly at £9.89, a two-week full-feature trial, and no permanent free tier beyond the read-only lapse state Condition 9.7 already settled.

### 14.1 Why three years, in the order the arithmetic produced it

1. **Because the period should be what Candour will honour, and five years is the number the CEO can least evidence.** 360 hours a year is 9.6 focused solo weeks of maintenance, every year, on two platforms, from one part-time person, starting **after** a build the CTO sizes at 55.75 focused solo weeks. Five years of that is 1,800 hours — most of a second build. The CTO's own caveat is the decisive one: *"it has never been tested against a real year of anything."* **A contractual promise with a five-year lever arm, resting on a judgment with no measured year behind it, is the kind of commitment a company whose brand is candour should be slowest to make.**
2. **Because the cost of over-promising is a public breach and the cost of under-promising is a calculable overcharge — and I have put a number on the second so it is not assumed to be zero.** On a three-year commitment, if Haunt turns out to live five years, the honest price during those three years is £1.146 a month against the £0.990 a five-year declaration would have given — **£5.62 per customer over the three years**, either taken from early customers or absorbed as a deeper deviation below target (§5.5). That is the price of my own caution and I am naming it. **The §5.5 amendment removes it entirely**, because a genuine extension could then be reflected in the price and passed to existing customers under 2.3.3.1. **If the CEO adopts the amendment, three years becomes strictly better than five; if he does not, three years costs £5.62 a head against a risk I judge to be larger.**

3. **Because the promise is contractual, not marketing.** *"Supported until [date]"* is a term of the contract under CRA 2015 s.36(3). **Three years is the longest period I would sign on the evidence in front of me**, and if the work is genuinely being done in year three, a further commitment can be published then — honestly, from a track record rather than from a model. **Under the clause as drafted that later commitment cannot reach the price; under the §5.5 amendment it can, and should.**
4. **Because two years is worse than three on every number and better on none.** It raises the volume at which 99p is honest by 73%, raises the sustained acquisition rate by 73%, and puts an irreversible 30.3% price cut in month 25 of a product whose own model needs uninterrupted acquisition throughout. Its only apparent advantage — a shorter obligation — is largely illusory, because §5.5 shows the period is frozen in **both** directions once it is published and sold against. **Two years buys almost no freedom and costs a permanent cut at the halfway point, plus £8.42 a head taken from early customers if the product turns out to live longer.**
5. **Because the period decision does not change three of the four prices.** Monthly, quarterly and yearly are 99p, £2.59 and £9.89 at two, three and five years alike. **The CEO is choosing the volume at which those prices are honest, and the pay-once price, and nothing else.** That should make the decision easier, not harder, and it was not visible until the life was modelled as a variable.

**What I am recommending against, stated so silence is not read as consent.** **Against** two years, for reason 4. **Against** publishing five years today, for reason 1 — though I would not block it, and if the CEO's own judgment is that he will do the work for five years, his judgment on that question is better than mine and it is his under 5.4. **Against** publishing any period before the venue-index spike runs, because D2's third limb depends on it (§4.2). **Against** the word "lifetime", "forever" or "for life" on the pay-once tier at any period, which is UX's block B11 and which I reach independently from the cost side.

### 14.2 Why the pay-once tier should be the headline

**Because the binding constraint on this product is reach, and pay-once is the only tier that does not lose to it.** 8,927 distinct buyers over three years — **248 a month** — against 1,623 new subscribers a month for the subscription. That is a 6.5× difference at three years and it is the largest single lever in this document, larger than the build estimate, larger than the platform decision, larger than the price itself.

**Three supporting reasons and one honest caveat.**

- **It is the tier with the fewest ways to be dishonest.** Nothing to cancel, no renewal to be surprised by, no cooling-off period, no reminder-notice duty, and — per the CTO — no charge-by-inaction event, which is what drags the whole DMCCA renewal machinery into the product *including the proportionate refund Candour has no mechanism to pay*.
- **It is now genuinely cheaper**, by 18.3% and £10.91 over five years, which is what UX's B11 required before any saving could be claimed.
- **It is the one tier whose price the customer can verify against this cost sheet in a single division.**
- **The caveat, which is real:** a £28.99 up-front price converts worse than 99p a month and nobody has measured by how much. **The reach advantage is per person who buys, not per person who looks.** §12.4.

**Monthly at 99p stays**, because it is the CEO's decision, because it is the tier that makes the product reachable for someone who will not pay £28.99 to try something, and because with a two-week full-feature trial in front of it the funnel is honest. **What I am recommending is which tier leads, not which tiers exist.**

### 14.3 The thing I record against my own recommendation

The same one as the last two times, because it has not stopped being true. **The CEO's decision to build Haunt was explicitly not a commercial decision.** A recommendation optimising commercial outcome is answering a question he did not ask.

**What survives under his actual objective** — that Haunt exists, is good, and is sold honestly:
- **The period recommendation survives**, because it is not about optimisation. It is about whether a contractual promise will be kept, and a company that breaks a published support commitment has damaged the only asset this constitution is building.
- **The pay-once recommendation survives**, because a product that needs 248 buyers a month is a product that might exist in five years and one that needs 1,623 subscribers a month probably is not.
- **The band-width and discount-depth findings do not survive as decision inputs** under his stated objective, and I flag them as the weakest things in this sheet. They are correct and they are optimisation.

---

## 15. What would overturn the findings in this sheet, and where I looked

*(Required by `roles/cfo.md` as amended: a negative finding carries a block's duty.)*

### 15.1 The reach finding (§12) — my strongest negative

Listed in full at §12.4. In short: a measured tenure above 14 months; an acquisition channel nobody has written down; leading with pay-once; or a deliberate published deviation below target.

### 15.2 The cost base (§2)

1. **The billing-event cost `e`.** Now the largest single uncertainty in this sheet, ahead of the build estimate. At `e` = £0 the band falls to 5,006–7,996 and the ladder loses its cost anchor entirely; at `e` = £0.3271 the 30% cap becomes unreachable at 99p. **Measurable free in App Store Connect within 90 days of launch. Until then every figure here rests on one seat's judgment about a support pattern nobody has observed.**
2. **The platform mix.** 60/40 is a guess and always has been. §6.4 shows the band running 5,200–8,504 at 100% iOS and 9,611–34,084 at 100% Android. **Testable free in the mandatory Play 12-tester closed test.**
3. **The build estimate itself.** 1,770–2,410 hours is a ±15% range around a number that has grown from 450 to 1,330 to 2,090 in three weeks, through four separate increments in four separate documents, none re-based against the others until the CTO's note. **The direction of travel has been one way and there is no reason yet to think it has stopped.**
4. **The security/defect line (§4.1)**, unnamed and unsized, worth 3–10% on the volume.
5. **The labour benchmark**, which every figure scales linearly with. Retrieved at primary from ONS; single-origin by nature.

### 15.3 The band-width finding (§6.2)

Width is **invariant to the build estimate** — it is set purely by price and variable support — so no revision to the CTO's hours changes 1.908×. It moves only if `e` or the platform mix moves. That is why position and width are stated separately.

### 15.4 What would *not* overturn anything

- **A higher subscription price.** The floor falls with price, but at any volume this company has evidence for the compliant price is already well above 99p, which is the finding rather than a way around it.
- **The ICO fee determination** (0.17% of the base) or the shared-fee allocation rule (0.42%). Both are governance, not money.
- **A different rounding convention.** ±5p at the monthly tier is large in margin terms and small in every other term.

### 15.5 Where I looked

**Retrieved from disk this session, in full:** `constitution.md` v1.2 (Definitions; Articles 1, 2.1, 2.2, 2.3, 3, 4, 5.2, 5.4, 5.6, 6.1, 7.2, 9, 10, 11); `roles/cfo.md` as amended; `pipeline/evidence-standard.md` v1.1 including *"Claims about our own rules"*; `decisions/2026-09-16-haunt-gate.md` in full — Conditions 1–10, Condition 9 as replaced, Corrections C1–C4 and the CEO decisions log D1–D2; `products/haunt/subscription-sizing-note.md` (CTO) §§2–11; `products/haunt/venue-index-spike.md` (Engineer) §§0, 9–10; `products/haunt/subscription-compliance-note.md` (CGO) §§4, 10; `products/haunt/ux-note-pricing.md` (UX) §§3–4; `products/haunt/pricing-ladder-model.md` and `products/haunt/window-conversion-model.md` in full; `pipeline/templates/cost-sheet.md`.

**Retrieved externally this session (2026-09-20), at primary:** Apple's UK GBP price-step and convention grid (PDF, text-extracted); App Store Connect Help on subscription price changes; the ICO data protection fee page; GBP/USD spot; the Apple Developer Program fee page.

**Carried forward, attributed, and not re-retrieved by me:** the ONS ASHE benchmark (retrieved at primary 2026-09-18); CRA 2015 s.36 (CGO, 2026-09-17); the DMCCA sources (CGO, 2026-09-18); Apple's and Google's forcing-function pages (CTO, 2026-09-19); the Engineer's venue measurements (2026-09-18); App Store guidelines 3.1.2(a) and 5.1.2(i) (CTO and UX).

**Attempted and failed:** Google Play's GBP price grid at primary — the currencies-and-price-ranges page redirects to a supported-locations table that does not render. **The complete 800-point App Store Connect GBP list is not published outside the tool** and must be confirmed there before publication.

**Looked for and did not find:**
- **A reach multiple `r`, or any acquisition channel**, in any artifact in this repository. **Absent, not merely unverified.** Searched again this session.
- **An independent second origin** for either the churn or the conversion benchmark. Both remain RevenueCat.
- **Any published Candour support commitment for any product**, which is why §5 is a decision and not a description.
- **Any measured billing-contact rate**, for this product or any other, which is why `e` is [J].

---

## 16. Blocks and flags, labelled per the amended charter

**My charter's blocking power, quoted so its edges are visible:** *"Can block: Launch of any pricing not backed by a published cost sheet; any proposal without a credible cost model."* It reaches the **price level** and the **cost model**. It does not reach Article 4, Article 9, product shape, or the governance of a decision record — a distinction Corrections C1.3 and C2.6 corrected against this seat once, and I am not repeating it.

### 16.1 The block I hold, narrowed

> **BLOCK — maintained.** *No Haunt price may be published under Article 3, and no price may be set under Constitution 5.4, until the supported life is published.* Constitution v1.2, Definitions: *"the amortisation period must equal a **published** support commitment to customers… **Absent a published support commitment, build labour is a first-year operating cost.**"* Absent a published period, the correct treatment charges the entire £74,532.04 to year one, the annual cost base is **£90,205.20** rather than £30,579.57, and **every price in this sheet is wrong by roughly a factor of three.**
>
> **This is a checklist item failing, not a feeling of unease:** the Definitions name a precondition, the precondition is unmet, and the consequence is arithmetic.
>
> **What lifts it:** the CEO publishing a dated, product-level support commitment — *"Haunt is supported until [date]"* — at two, three or five years. **Any of the three lifts it.** The block is about the *existence* of a published period, not about which one. My recommendation of three years (§14) is a recommendation and is **not** part of the block.

### 16.2 The block I have lifted

> **LIFTED.** The ONS ASHE labour benchmark block (gate Condition 5) is discharged and stays discharged: the benchmark was retrieved at primary on 2026-09-18 and the secondary figure it replaced was exact to the pound. Nothing in my charter now bars publication on evidence grounds.

### 16.3 Flags — concerns outside my blocking scope, each with the seat that holds it

| # | Flag | Seat that holds it |
|---|---|---|
| F1 | **Condition 9.3 of the decision record contains a finding of mine that is wrong** (§6.3): *"At 25% off, 1.05×, which is not a band"* and the ~10% discount threshold. Corrected, the band closes at ~41%. The record publishes 2026-10-16 and **must be corrected in the open before publication.** From this seat the classification is a **CORRECTION** — the statement was false when written | **CGO** (record integrity); classification is the CGO's to propose |
| F2 | **D2's security-and-defect limb has no hours behind it** (§4.1). Either the CTO names a row or the CEO narrows D2's wording | **CTO** to size; **CEO** to decide the wording |
| F3 | **D2 was published before the spike that funds one third of it has run** (§4.2). If the venue-index spike returns "don't", D2's third limb has nothing to promise, and a published commitment is harder to change than an unpublished one | **CEO** (5.4); **CTO** holds Block 4 |
| F4 | **The "shortened, never lengthened" ratchet is flawed on three counts and replacement wording is drafted** (§5.5). It would be a strengthening under Article 11.2 | **CEO** on the **CGO**'s advice (Article 11) |
| F5 | **Two Article 9 loophole rows proposed**: escaping the cumulative test by converting subscribers to one-off buyers (§8.5), and charging one product 100% of a shared company cost (§13) | **CEO** on the **CGO**'s advice (Article 11) |
| F6 | **The pay-once tier must be renamed at a short life** (§5.6). At two years I would not use the words "Pay once" | **UX** (B11 is that seat's block); **CEO** on naming |
| F7 | **Pay-once revenue must be recognised over the supported life, not in the year of receipt** (§8.5), or the annual margin in the year of purchase is +243% and the cost sheet describes nothing real | **CFO** — mine, and it is recorded here as the rule |
| F8 | **The ICO fee determination** remains open at 0.17% of the cost base (§2.3) | **CGO** |
| F9 | **The cumulative-test interpretation** is closed on the arithmetic (§8) and open on the law. Still due 2026-10-16 | **CGO**, with the CEO deciding |

### 16.4 Blocks I do not hold, stated so silence cannot be read as consent

I hold **no block** on: the ladder's shape; the choice of period between two, three and five years; the DMCCA determinations; the venue-index decision; the naming of any tier; or any Article 11 amendment proposed above. **Several of those are things I have argued strongly about in this sheet. Arguing is not blocking, and I am labelling which is which.**

---

## 17. Gaps, corrections owed, and disclosures

### 17.1 What this seat could not establish

| Gap | Why it matters | Owner |
|---|---|---|
| **The billing-event support cost `e`** | Now the largest single uncertainty here, ahead of the build estimate. At £0 the ladder loses its cost anchor; at £0.3271 the 30% cap is unreachable at 99p | **CFO** — measurable free in App Store Connect within 90 days of launch |
| **Average subscriber tenure** | Sets the reach number entirely; the 14-month crossover is the hinge | Measurable free in App Store Connect within 90 days |
| **Churn and conversion benchmarks are both single-origin (RevenueCat)** | Two load-bearing claims, one publisher, **now flagged in four artifacts**. Long past the evidence standard's *"Twice-flagged is escalated"* | **CFO / Research Analyst — escalation is overdue and I am not flagging it a fifth time. It should be resolved or formally accepted in writing by the CEO** |
| **The reach multiple `r` and any acquisition channel** | The only input a commercial case depends on. **Absent from every artifact in this repository**, searched again this session | **Research Analyst / CEO** |
| **iOS/Android platform mix** | Moves the band from 5,200–8,504 to 9,611–34,084 | Testable free in the mandatory Play 12-tester closed test |
| **Google Play's GBP price grid at primary** | The nearest conventional price point may differ between stores | **CFO**, before publication |
| **The complete 800-point App Store Connect GBP list** | Not published outside the tool | **CFO**, in App Store Connect before publication |
| **A security-and-defect maintenance line** | D2 promises it; no row funds it | **CTO** |
| **Whether the venue-index remediation spike passes** | Its build hours, its annual reconciliation, and D2's third limb all depend on it | **CTO** (Block 4) |
| **The launch date** | The amortisation cliff date is launch + the period, and cannot be published until launch is known | **PM/BA** |

### 17.2 Corrections owed elsewhere, visibly and in place

| File | What is owed |
|---|---|
| `decisions/2026-09-16-haunt-gate.md` **Condition 9.3** | The ~10% discount threshold and the *"at 25% off, 1.05×"* figure are **wrong**. §6.3. Owed in the same publication as the record, due 2026-10-16 |
| `decisions/2026-09-16-haunt-gate.md` **Condition 9.4** | *"a ~32% price cut"* and *"realised margin jumps to +62.3%"* are superseded: on this cost base the cut is **20.2%** at five years and the year-six margin is **+44.7%**. §10 |
| `decisions/2026-09-16-haunt-gate.md` **Condition 9.2** | Its reasoning that at three years the monthly and paid-once tiers *"have no overlapping compliant band at all"* was true only while pay-once was priced at exactly 60 × 99p. **C3.0 removed that anchor**, and the tiers now overlap at every period (§5.1). The five-year commitment is still required for the amortisation treatment; it is no longer required for ladder coherence, and one of the three reasons given for it has fallen |
| `products/haunt/pricing-ladder-model.md` §2.3, §3.2 | Both corrections at §6.3: the common-`s` band error and the discount pass-through error |
| `products/haunt/pricing-ladder-model.md` §8.2 | *"The CEO's own arithmetic names the period"* presented a circularity as a discovery. §5 |
| `products/haunt/pricing-ladder-model.md` §9.2 | The email-collection inference is not supported by the primary source. §11.1 |
| `products/haunt/cost-sheet.md` | **Superseded in full by this document.** A banner is owed on its face |
| `products/haunt/window-conversion-model.md` §3 | Superseded on every number by §2 here |
| `products/haunt/subscription-sizing-note.md` §10.4(2) | The step-down does not get steeper; it gets flatter. §10 |

**Three of the nine rows above are corrections to my own prior work, and two of them are arithmetic errors that survived until a re-derivation found them.** Gate Condition 6 exists for exactly this and it is working: the errors in this pack are now being caught before publication rather than after.

### 17.3 Related-party disclosures

**None.** No payment to the founder, to family, or to any affiliated entity is contemplated anywhere in this cost sheet. All founder labour — the whole of the £74,513.38 build figure and the £15,537.25 annual fixed labour — is costed at the published external benchmark, retrieved at primary from the ONS, and is **currently unpaid and undrawn.** It appears here as cost because Constitution 2.1 requires *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)"*, and because the alternative — showing a low cost because nobody is being paid — is the thing Article 9's *"Inflating costs"* row and Article 2.2's *"Being paid is legitimate; being paid opaquely is not"* are jointly written against.

**If Haunt never recovers that labour, this cost sheet will say so at every annual republication.** The gate record already anticipates it: the CEO decided to proceed on a stated non-commercial basis, *"accepting that it may not cover its own benchmarked labour."*

### 17.4 What a sceptical customer should take from this document

1. **Haunt costs what one person's time costs.** There is no server, no data collection, no advertising and no third party being paid. Roughly 95% of the number is labour, valued at a published national median.
2. **The price depends on how many people buy it**, because almost all of the cost is fixed. Candour does not get to choose which point on that curve is true.
3. **The price is committed to falling**, on a date Candour will publish at launch, by about a fifth to a third, automatically, for existing subscribers, whether or not Candour would prefer otherwise by then. The App Store does not permit the alternative.
4. **The margin is below Candour's own target at every tier**, because the store's 15% is passed through without markup.
5. **Nothing here has been built yet, and the largest number in it is an estimate that has grown from 450 hours to 2,278 in three weeks.** That is recorded because a cost sheet whose biggest figure is a forecast should say so on its face.

---

## Change log

| Date | Change |
|---|---|
| 2026-09-20 | **Created.** First complete cost sheet for Haunt on the CTO's revised sizing (`subscription-sizing-note.md`, 2026-09-19) and the Engineer's venue-index spike. Incorporates CEO decisions **D1** (both platforms) and **D2** (published support commitment). Supersedes `cost-sheet.md` in full and `pricing-ladder-model.md` §§2–9. Apple's GBP price grid, App Store Connect price-change mechanics, the ICO fee and GBP/USD retrieved at primary this session; ONS ASHE benchmark carried forward from its primary retrieval of 2026-09-18. **Corrects two arithmetic errors in this seat's own prior work** (§6.3) and one in the CTO's cliff indication (§10). **Not yet published, and not a price: Constitution 5.4 reserves pricing to the CEO.** |
| 2026-09-20 | **Amended before delivery,** on the CEO's disclosure that the five-year figure at D2 was reverse-engineered from the pay-once price rather than from a judgment about what Candour will support. §5 now models the supported life as a **variable at two, three and five years** rather than treating five as given, and §5.5 answers the CEO's and CVO's challenge to the *"shortened, never lengthened"* clause with drafted replacement wording. An earlier draft of §5.5 had the price direction of shortening backwards; **the error is named in place at §5.5 rather than rewritten out.** |

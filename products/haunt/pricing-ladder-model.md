# Pricing ladder model — Haunt

**Seat:** Chief Financial Officer · **Date:** 2026-09-18
**Commissioned by:** the CEO, who has considered and not taken this seat's recommendation of 2026-09-17 (no free tier, no visibility window, no subscription) and has directed that a subscription ladder with a permanent free tier be modelled at full effort.

**Status: not a published cost sheet, and not a price.** Under Constitution 5.4 pricing is the CEO's. This document models what he asked for and states what the model says, including where it says he cannot have it.

**Relationship to prior work.** This document **extends** `products/haunt/window-conversion-model.md`; it does not supersede it. Every cost input below is that document's §3, unchanged, so the two can be read against each other. Where a figure moves, the reason is stated. `products/haunt/cost-sheet.md` §§3–10 and §12 remain superseded by that document, not by this one.

**Template note:** `pipeline/templates/` contains no template for a pricing model (checked this session; the nearest, `cost-sheet.md`, assumes a monthly hosting-shaped cost table and a single price). This document is structured as a pricing note. The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Every external figure was retrieved **2026-09-18** unless a different date is given. Nothing external is cited from memory. Every constitutional claim quotes the clause it relies on, in the same passage, per that standard's *"Claims about our own rules"* — and where I state my own professional judgment rather than a requirement, I say so, per *"A seat's heuristic is not an article."*

---

## 0. The answers, before the arithmetic

1. **Condition 5 is closed and my standing block is lifted.** The ONS ASHE primary retrieval, attempted and failed by two seats on three prior occasions, **succeeded this session.** The £32.71/hour benchmark under every number in this company's models is confirmed at primary, to the pound, and the secondary source that carried it was accurate. §1.

2. **The CEO's two stated numbers are the same number, and they name a five-year support commitment.** 99p/month and £59.40 once produce **identical margins at every subscriber count** — not approximately, exactly — if and only if Haunt's published supported life is **five years**. Against the three-year life the current cost model assumes, the two prices have **no overlapping compliant band at all**: at any volume where 99p/month is lawful, £59.40 is 50–70 points above the Article 2.1 hard cap. The CEO has not chosen a support commitment; his pricing already has. §8.

3. **The compliant band is narrow, and my variable support line widens it far less than hoped.** At 99p/month on a five-year life, the band runs **3,122 subscribers (cost recovery) to 4,988 (the 30% hard cap)** — a factor of **1.60**. Adding the discounted tiers the CEO wants **narrows it further, to 3,523–4,988, a factor of 1.42**, because a discount raises the floor while leaving the ceiling where monthly put it. Every percentage point of discount narrows it again: at two months free on annual it is **1.23×**; at 25% off annual it is **1.05×**, which is not a band. §2, §3.

4. **The re-pricing cadence is the finding the CEO should take away.** Because build labour is amortised and dominates, the compliant band is a function of subscriber count, so **every material change in subscriber count is a price change**, and Article 2.1 requires a republished cost sheet at each one. Concretely: an annual re-pricing for the life of the product, a **step change at the amortisation cliff**, and — because Article 2.3.3.1 makes price reductions for existing customers the first call on the remainder — the cuts land on the **installed base**, not just on new buyers. Apple's mechanics make that automatic and irreversible: *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don't have the option to preserve the higher price for existing subscribers"* [E]. That is good news for compliance and it means the ratchet, once started, cannot be stopped. §2.4.

5. **The inertness finding survives the change to subscription, and it gets worse — by a factor of two to three.** The break-even conversion floor at £14.99 one-off was 11.4%. At 99p/month it is **22% to 37%** depending on churn and on the published supported life — **25.8% central on a three-year life, 36.7% central on the five-year life the ladder actually requires** — against a retrieved freemium median of **2.1%** [E]. Recurring revenue does not rescue the arithmetic because churn caps the average subscriber at **five to eight months** of 70p. The finding turns entirely on tenure, and I say so plainly: a subscriber held for three years would make the subscription *better* than the one-off on this test. The retrieved category data does not support that tenure. §4.

6. **The structural reach argument for recurring revenue does not survive churn — it reverses.** Held continuously, 4,127 subscribers beat 10,564 one-off buyers, and that is the argument. But holding 4,127 continuously for three years at an average tenure of 5.2 months requires **28,568 distinct people to subscribe** — nearly three times the one-off's requirement, not a third of it. For a company whose binding constraint is reach, **the ladder needs more reach than the one-off, not less.** §5.

7. **The rounding rule is not cosmetic at 99p, because Apple's price grid is coarser there than Article 2.1's compliance band.** One 10p step on a monthly price moves realised margin from 9.9% to 20.0% to 29.8%. The entire permitted distance from the ~20% target to the 30% hard cap is **less than one available price point**. The CEO's "always round up" is a systematic bias and the MD is right about it; the honest rule rounds to the nearest point in either direction, and on his own example the nearest point to £75.40 is **£75.00**, not £75.99. §7.

8. **My recommendation is unchanged in substance and narrowed in scope, and I have written it as one sentence with a reason, not a menu.** If the CEO wants a ladder, the model supports exactly one: **no free tier, a two-week full-feature trial, monthly at 99p, a shallow cost-anchored ladder above it, a paid-once tier at £59.40 sold as what it is, and a published five-year support commitment.** The free tier is the part the arithmetic kills, not the ladder. §10.

9. **One new gaming vector, named rather than used, per Article 9.** A lifetime tier converts a recurring price into a one-off payment and thereby moves it **outside the cumulative margin test's scope entirely** — the test constrains what a subscriber pays "merely by staying", and a lifetime buyer does not pay by staying. Selling lifetime is therefore the available route around the year-four step-down. Article 9 commits: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* §6.4.

---

## 1. Condition 5 is closed — the ONS ASHE benchmark, retrieved at primary

My standing block was: *no Haunt price may be published under Article 3 until the ONS ASHE labour benchmark is retrieved at primary* (decision record Condition 5; `window-conversion-model.md` §6.4). It has been attempted and failed three times — by the Skeptic at gate, and by me on 2026-09-09 and 2026-09-17 — each time because the occupational breakdown lives in a spreadsheet the tooling could not open.

**It opened this session.** The ONS dataset landing page carries the archive directly [E, [ONS, *Earnings and hours worked, occupation by four-digit SOC: ASHE Table 14*](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupation4digitsoc2010ashetable14), retrieved 2026-09-18; release date 2025-10-22]. The 2025 provisional archive was retrieved and the relevant cells read directly:

| Measure | SOC 2020 code 2134 — *Programmers and software development professionals*, full-time, UK, 2025 provisional | Source |
|---|---|---|
| **Median gross annual pay** | **£56,914** | [E] ASHE Table 14.7a *"Annual pay - Gross (£) - For full-time employee jobs: United Kingdom, 2025"*, row 2134 |
| 25th / 75th percentile | £42,289 / £75,794 | [E] same table |
| Median gross **hourly** pay | **£29.58** | [E] ASHE Table 14.5a *"Hourly pay - Gross (£) - For full-time employee jobs"*, row 2134 |
| Coefficient of variation on the median | **2.7%** — inside ONS's own *"CV <= 5%… Estimates are considered precise"* band | [E] Table 14.7b, row 2134 |
| Number of jobs | 343,000 (annual pay basis) | [E] Table 14.7a |

**Three findings, in order of how much they change anything.**

**1.1 The secondary source was accurate, to the pound.** `cost-sheet.md` §2.4 carried £56,914, £42,289 and £75,794 from a single secondary page citing ASHE Table 14, 2025 provisional. All three reproduce exactly against the ONS file. **The flag was correct to raise and the number was correct all along.** That is worth recording plainly: the evidence standard's purpose is not to assume secondary sources are wrong, it is to stop a company anchoring on one it has not checked. It was checked; it held.

**1.2 The hours basis survives, and the Constitution settles it rather than my judgment.** ONS publishes a *median gross hourly* figure of £29.58, which is 9.6% below the £32.71 the cost model derives from £56,914 ÷ 1,740 hours. The two measure different things: ONS hourly pay divides pay by **paid** hours, which include statutory leave; £32.71 divides by hours **actually worked**. Constitution 2.2 names the benchmark as *"the median UK software developer salary, **adjusted for hours actually worked**"*. That is the derived figure, not the ONS hourly column. **£32.71/hour stands, and it now rests on a primary retrieval rather than a secondary one.** The ONS hourly column is recorded here so a reader can see that the difference was noticed and disposed of, not overlooked.

**1.3 The block lifts.** Condition 5 is discharged. No Haunt price is barred from Article 3 publication by this seat's benchmark objection any longer. Two other bars remain and are *not* mine to lift: the price itself is a Constitution 5.4 decision, and Apple's UK merchant-of-record position — now **retrieved by the CGO**, who confirmed Apple Distribution International Ltd. as merchant of record for UK users [E, [Apple Media Services Terms and Conditions (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html), retrieved by CGO 2026-09-17, read from `compliance-note.md` §4.1 this session] — means the `[K, unverified]` tag on `cost-sheet.md` §2.1 can also be upgraded. **Both of this document's inherited evidence bars are now closed.** A correction banner is owed on `cost-sheet.md` §2.4 and §13, listed in §12.

**What this does not change.** Every figure below still scales linearly with £32.71. It is now a retrieved figure rather than a relayed one, which is the whole of the difference.

---

## 2. The compliant volume band

This is the finding the MD expected to matter, and it does. It is stated first for 99p/month alone, then for the ladder, then blended.

### 2.1 How the band arises, and why it is a band rather than a price

Build labour is now capital. Constitution v1.2 Definitions: *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year… the amortisation period must equal a **published** support commitment to customers."* Amortised build is a **fixed** annual cost divided across however many subscribers exist. So the cost of serving one subscriber is

```
C(N)  =  A / N   +   s
```

where `A` is the annual fixed cost (amortised build + fixed maintenance + support floor + fixed non-labour), `N` is the subscriber count, and `s` is variable support per subscriber per year (£2.3060 blended 60/40 across platforms, from `window-conversion-model.md` §3.3).

Margin is measured, as throughout Candour's models, **over total published cost including store commission**, with commission passed through at zero markup:

```
P  = shelf ÷ 1.20                  (ex-VAT price)
margin(N)  =  ( 0.85·P − C(N) )  ÷  ( C(N) + 0.15·P )
```

Check, stated so a second seat can re-derive it (Condition 6): at `P = 1.411765·C` the expression returns **16.504%**, reproducing the pass-through margin used in every prior Haunt document. ✔

**A fixed price therefore does not have a margin. It has a margin per subscriber count.** Below some `N` it under-recovers; above another it breaches the 30% hard cap — *"As a hard backstop, **no product's margin may exceed 30%**, regardless of justification"* (Article 2.1). The gap between the two is the compliant band.

### 2.2 The band at 99p/month

Two published supported lives are shown, because §8 establishes that the choice is not yet made and it moves everything.

`A` = amortised build + £9,747.58 fixed labour + £135.98 fixed non-labour.
At **L = 3 years**: A = £25,202.74. At **L = 5 years**: A = £19,075.07.

99p/month → £11.88/year shelf → £9.90 ex-VAT → £8.415 net proceeds.

| | **L = 3 years** | **L = 5 years** |
|---|---|---|
| Cost recovery (margin 0%) | **N = 4,126** | **N = 3,122** |
| 16.5% (the pass-through margin) | N = 5,355 | N = 4,053 |
| **~20% — the Article 2.1 target** | **N = 5,652** | **N = 4,278** |
| **30% — the hard cap** | **N = 6,590** | **N = 4,988** |
| **Width of the band** | **1.60×** | **1.60×** |

**Margin actually realised at 99p/month, L = 5:**

| N | 2,500 | 3,122 | 3,500 | 4,000 | 4,278 | 4,500 | **4,988** | 6,000 | 8,000 |
|---|---|---|---|---|---|---|---|---|---|
| Margin | −13.3% | 0.0% | +7.1% | +15.7% | **+20.0%** | +23.3% | **+30.0%** | +42.0% | +60.3% |

**Read the two ends honestly.** At 2,500 subscribers Candour is selling below its own published cost — permitted under Article 2.1 with written justification (*"A deviation in either direction is a deviation"*), but it is a deviation, and it means the founder's benchmarked labour is not being recovered. At 8,000 subscribers the product is at **60%** and Article 2.1 admits no justification: the price must come down, and 2.3.3.1 sends the reduction to existing customers first.

### 2.3 The band across the ladder, and the fact that discounts narrow it

Each tier has its own band. The **ceiling** is set by the *most expensive* tier per unit time — monthly, which reaches 30% first. The **floor** is set by the *cheapest* tier per unit time — whichever is the deepest discount, because that is the tier that stops recovering cost first.

**At L = 5 years:**

| Tier | Shelf per subscriber-year | Cost recovery | ~20% target | **30% cap** |
|---|---|---|---|---|
| Monthly 99p | £11.88 | 3,122 | 4,278 | **4,988** |
| Quarterly £2.79 (6.1% off) | £11.16 | 3,407 | 4,711 | 5,524 |
| Yearly £10.90 (8.2% off) | £10.90 | **3,523** | 4,890 | 5,748 |
| Yearly £9.90 (two months free, 16.7% off) | £9.90 | **4,053** | 5,726 | 6,806 |
| Paid-once £59.40 over five years | £11.88 | 3,122 | 4,278 | **4,988** |

> **The blended compliant band for the ladder as proposed is N = 3,523 to 4,988 — a factor of 1.42.**

And the effect of discount depth on that width, which is the reasoning §3 needs:

| Deepest tier's discount | Lower bound | Band width |
|---|---|---|
| None (monthly only) | 3,122 | **1.60×** |
| 6.1% (quarterly £2.79) | 3,407 | 1.46× |
| **8.2% (yearly £10.90)** | **3,523** | **1.42×** |
| 16.7% (two months free) | 4,053 | 1.23× |
| 25% | 4,761 | **1.05×** |

**This is the constraint on the discount curve, and it is a real one rather than a stylistic preference.** A deep discount does not merely lower the margin on one tier. It raises the whole ladder's floor while leaving its ceiling untouched, and at 25% off the annual tier there is no subscriber count at which every tier is simultaneously compliant. The CEO's original sketch gave quarterly 33% off; **that ladder has no compliant band at all.**

### 2.4 The re-pricing cadence the CEO is signing up for

The MD asked me to say this plainly, so I will.

**Three separate forces move the price, and all of them move it down.**

**(a) Growth.** The band is a function of N. From the table in §2.2, every 1,000 subscribers added in the 3,000–5,000 range moves realised margin by roughly 8 percentage points. **A product that grows through its band in eighteen months needs a price change in eighteen months.** Article 2.1: *"Cost sheets are reviewed and republished at least **annually** and at every price change."*

**(b) The amortisation cliff.** At the end of the published supported life the build charge leaves the cost base. At L = 5 and N = 4,278 — the point at which 99p is exactly on target — the year-six cost of serving a subscriber falls from £6.765 to **£4.616**, and the realised margin at an unchanged 99p jumps to **+62.3%**, twice the hard cap. The price must fall to roughly **68p** to return to target, and to no more than **74p** to clear the cap at all. That is not a gradual drift; it is a **32% cut falling due on a single date**, and **Candour can calculate that date on the day Haunt launches.**

**(c) The waterfall.** Article 2.3 applies profit *"strictly in this order"* — reserve, then distributions, then *"The remainder, in this order of preference: 1. Price reductions for existing customers"*. On a one-off product that clause has almost nothing to bite on: a past buyer has no ongoing price to reduce. **On a subscription it bites every year, on the whole installed base.**

**What that costs, mechanically, is nothing — and that is the part worth knowing.** Apple's own documentation is explicit: *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. **You don't have the option to preserve the higher price for existing subscribers.**"* [E, [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions), retrieved 2026-09-18]. Increases are the constrained direction — they require consent above published thresholds, and the same page offers the option to *"Keep the current price for existing subscribers"* only on an increase. **The store enforces the direction Candour's constitution wants and forbids preserving the old price.** One future price change may be scheduled at a time, per territory, per billing plan [E, same page].

> **So the honest summary of the cadence: at least one published cost sheet and one price review every year for the life of the product; a step change of roughly a third at the end of the published supported life; and every reduction landing automatically on existing subscribers, irreversibly, whether or not Candour would prefer otherwise by then.**

**The judgment I attach to that, labelled as mine [J] and not as an article:** this is a *good* obligation and a *heavy* one. It is the obligation Candour wrote down in 2.3.3.1 before there was money at stake, and a subscription is the shape that makes it bite. The CEO should decide whether he wants to be performing it annually in 2033, because the mechanism is one-way and the store will not let him undo it.

### 2.5 What the free tier does to the band — and this is where the ladder breaks

A free user costs £0.6150/year in support (`window-conversion-model.md` §3.3). Free users are carried by paying subscribers, so each free:paid ratio adds that cost to every subscriber's cost of service. At 99p/month, L = 5:

| Free : paid | Cost recovery at | 30% cap at | Band |
|---|---|---|---|
| 0 : 1 (no free tier) | 3,122 | 4,988 | 1.60× |
| 1 : 1 | 3,472 | 5,944 | 1.71× |
| 2 : 1 | 3,910 | 7,352 | 1.88× |
| 4 : 1 (20% conversion) | **5,227** | 13,981 | 2.67× |
| 9 : 1 (10% conversion) | **33,232** | never | — |

**The band gets wider and moves out of reach at the same time, and the second effect is the one that matters.** At a 10% conversion rate — five times the retrieved freemium median (§4) — 99p per month **never** recovers its cost below 33,000 paying subscribers, and can **never** breach the 30% cap at any volume, because the free-user support floor sits permanently above the cap's cost. A price that can never reach its target margin is a permanent, published, unfixable deviation below target.

At a realistic 2.1% conversion the ratio is roughly 47:1 and the arithmetic does not produce a number at all: variable support alone (£2.306 + 47 × £0.615 = £31.21/subscriber-year) is **more than three and a half times the £8.415 a subscriber pays.**

> **Finding: a permanent free tier at any evidenced conversion rate is not a pricing question for Haunt. At 99p per month it is arithmetically unaffordable, and the reason is the one this seat found in a different architecture and again in this one — Haunt has no server, so it has no zero marginal cost behind which to hide a free user.**

---

## 3. The monotonic ladder

The CEO has corrected the non-monotonicity himself. This section proposes the curve and states the reasoning, as asked.

### 3.1 What a discount has to be made of

Article 2.1 prices each tier at *"approximately 20% over published costs"*. A discount for longer commitment is defensible under that clause **only to the extent that the longer commitment costs less to serve.** Any discount beyond that is a recorded deviation below target on that tier, permitted — *"deviations are permitted but must be justified in writing on the cost sheet"* — but it is a deviation and it narrows the band (§2.3).

So the question is arithmetic: **what does a longer commitment actually save?**

Not commission — Apple and Google charge the same percentage regardless of billing period. Not hosting — there is none. Not maintenance — the product is identical. **What a longer commitment saves is billing events.** Each renewal is an occasion for a support contact ("why was I charged", "how do I cancel", a billing-retry or grace-period case). Monthly generates 12 a year; quarterly 4; yearly 1; paid-once none after purchase.

Let `e` be the expected support cost per billing event. It is a judgment and I size it as one:

| Assumption | e per event | Annual saving vs monthly: quarterly / yearly / once |
|---|---|---|
| 0.5% of events × 20 min | £0.0545 | £0.44 / £0.60 / £0.65 |
| **1.0% of events × 20 min [J, central]** | **£0.1090** | **£0.87 / £1.20 / £1.31** |
| 2.0% of events × 30 min | £0.3271 | £2.62 / £3.60 / £3.93 |

[J] throughout. I have no measured contact rate for billing events on any Candour product and will not pretend to. The central case is deliberately conservative relative to the 5%/45-minute paying-user contact rate already in the cost model, because a billing event is a narrower trigger than a year of ownership.

### 3.2 The proposed curve

On the central `e`, against monthly's £11.88 per subscriber-year:

| Tier | Cost-anchored discount | Price per unit time | **Proposed shelf** | Effective discount at the rounded price |
|---|---|---|---|---|
| **Monthly** | — (baseline) | £0.99/mo | **£0.99** | — |
| **Quarterly** | 7.34% | £0.9175/mo → £2.7525/qtr | **£2.79** | **6.06%** |
| **Yearly** | 10.10% | £10.681/yr | **£10.90** | **8.25%** |
| **Paid once** | 11.01% (all events avoided) | see §8 | **£59.40** | n/a — see §8 |

Rounding to Apple's retrieved GBP grid, per §7.

**Three properties, and they are the reasoning rather than decoration:**

1. **It is monotonic by construction, not by taste.** 0% < 6.06% < 8.25%. Each longer commitment is strictly cheaper per unit time than every shorter one, because each avoids strictly more billing events. The CEO's requirement is satisfied as a consequence of the cost basis rather than as a constraint imposed on top of it.

2. **It is concave, and that is correct.** The step from monthly to quarterly buys 8 avoided events; quarterly to yearly buys 3 more; yearly to once buys 1. **Diminishing returns on commitment are what the cost actually does**, and a ladder that accelerates — bigger discounts for longer commitment — is not describing any cost Candour has.

3. **It is shallow, and I am not going to pretend otherwise.** Roughly 6% and 8% against a market convention of "two months free" (16.7%). **A ladder with a defensible cost basis at every rung is a ladder that will look mean next to competitors.** That is the honest trade and the CEO should see it stated rather than discovered.

### 3.3 If the CEO wants a deeper ladder

He may have one. Article 2.1 permits it. Two things travel with it and both must be written down:

- **Each discounted tier below target carries its own recorded deviation.** At two months free (£9.90/yr) against a cost base sized for monthly at target, the yearly tier's margin at N = 4,278 is **+2.7%** — a deviation of **17.3 percentage points below target**, which is five times the 3.5pp deviation Candour already records for passing store commission through at zero markup. A deviation that large needs a justification better than "the market does it", and I cannot write one for him.
- **The band narrows to 1.23×** (§2.3), and at 25% it effectively closes.

**My position, as this seat's judgment and not as an article [J]:** the cost-anchored curve is the one I would publish, precisely because the cost sheet and the pricing page then describe the same thing, and a sceptical customer comparing them finds they agree. A 16.7% annual discount requires Candour to publish a cost sheet showing that the annual tier earns 2.7% while the monthly tier earns 20% — which is true, defensible, and reads as arbitrary, because it is arbitrary. This is my test, it belongs to me, and Article 2.1 constrains the price *level* and says nothing about ladder shape. I state it as mine.

---

## 4. Conversion re-run: free → subscription at 99p

**The direct answer the MD asked for: the inertness finding survives the change, and the change makes it worse by roughly a factor of two.** C1-O5 stands. Here is the arithmetic, and then the honest statement of what would flip it.

### 4.1 What changes, and one thing that improves

`window-conversion-model.md` §1.2 derived the break-even conversion rate with a hard floor as reach → ∞:

```
floor  =  S_free  ÷  ( m + S_free )
```

where `m` is the net contribution from one converted user across the supported life. **Three things change under the CEO's pairing**, and only the third helps:

1. **`m` collapses**, because the conversion event is now worth 70p a month for however long the subscriber stays, not £10.62 once.
2. **`S_free` rises**, because a permanent free tier is served for the whole supported life rather than until a purchase — at L = 5 it is 2.5 × £0.615 = **£1.5375** rather than the £0.922 the one-off model used.
3. **The benchmark fits better than it did.** RevenueCat's dataset is a *subscription-app* dataset. In the one-off model I flagged that as a weakness: *"it is a subscription-app dataset, so it does not cover paid-up-front listings at all."* Under the CEO's proposal that objection disappears. **The 2.1% freemium median is now directly on point rather than an approximation**, and the evidential fit of my own argument has improved by his change. I record that because it runs against my conclusion.

### 4.2 Expected tenure, from retrieved renewal data

Contribution per subscriber-month at 99p: net £0.70125 − variable support £0.19217 = **£0.50908**.

Retrieved first-renewal retention for monthly plans, by category [E, [RevenueCat, *Average subscription renewal rates by app category*](https://www.revenuecat.com/blog/growth/average-subscription-renewal-rates-by-app-category), retrieved 2026-09-18; **single origin**, same publisher as the conversion benchmark below — counted as **one source**, per the independence rule]:

> Business 61% · Media & Entertainment 58% · Shopping 58% · Health & Fitness 57% · Utilities 57% · Education 56% · Productivity 54% · **Travel 53%** · Gaming 53% · Photo & Video 48% · **Social & Lifestyle 42%**

Annual plans, first renewal: Travel 40%, Business 40%, Health & Fitness 25%, **Social & Lifestyle 25%**, Productivity 23% [E, same page].

Haunt is a place journal: Travel and Social & Lifestyle are the two candidate categories, and they sit **at the bottom of the monthly distribution**. Beyond the first renewal the page publishes no monthly curve, so I model the tail explicitly: first-renewal rate `r1` [E], then a steady conditional monthly retention `ρ` [J], giving `M = 1 + r1/(1−ρ)` expected paid months.

| Scenario | r1 | ρ | **M (months)** | m = lifetime contribution | **Break-even floor** (L=3) | **Break-even floor** (L=5) |
|---|---|---|---|---|---|---|
| Social & Lifestyle, pessimistic | 0.42 [E] | 0.88 [J] | 4.50 | £2.29 | 28.7% | **40.2%** |
| **Social & Lifestyle, central** | 0.42 [E] | 0.90 [J] | **5.20** | **£2.65** | **25.8%** | **36.7%** |
| **Travel, central** | 0.53 [E] | 0.90 [J] | **6.30** | **£3.21** | **22.3%** | **32.4%** |
| Travel, optimistic | 0.53 [E] | 0.92 [J] | 7.63 | £3.88 | 19.2% | 28.4% |
| Business-like (upper bound, not Haunt's category) | 0.61 [E] | 0.95 [J] | 13.20 | £6.72 | 12.1% | 18.6% |
| *Memo: one-off at £14.99* | — | — | — | *£7.16* | ***11.4%*** | — |
| *Memo: held continuously 36 months* | — | — | 36.00 | *£18.33* | *4.8%* | *7.7%* |

The one-off row reproduces `window-conversion-model.md` §1.3's 11.4% exactly, which is the check that the two models are the same model. ✔

**Against a retrieved freemium download-to-paid median of 2.1%** — *"Hard paywalls convert 5x better than freemium (10.7% vs. 2.1%)"* [E, [RevenueCat, *State of Subscription Apps 2026*](https://www.revenuecat.com/state-of-subscription-apps-2026/), retrieved 2026-09-18; **single source**, and the prior year's edition at 2.18%/12.11% is the **same origin**, therefore not corroboration].

> **Verdict on the re-run: the floor moves from 11.4% to between 22% and 37%, against a 2.1% median. The window was short by a factor of 5 at £14.99 one-off. At 99p/month with a permanent free tier it is short by a factor of 11 to 17.**

### 4.3 Why the lower price point makes it worse rather than better

This is counter-intuitive enough to state on its own. A lower price is normally the thing that lifts conversion. Here it does not help the *break-even* conversion rate, because the floor is a ratio: the free user's cost against the converted user's contribution. Lowering the price shrinks the numerator's denominator without touching the numerator. **A 99p subscription held for five months produces £2.65 of contribution; a free user costs £1.54 to carry for five years.** One converted subscriber pays for **1.7 free users**. At £14.99 one-off, one buyer paid for 7.8.

And the composition argument from `window-conversion-model.md` §1.4 survives unchanged, because Conditions 8.3, 8.4 and 8.5 survive unchanged: **8.5** lets the engaged user keep everything free, **8.4** forbids telling anyone anything is coming, **8.3** hands the unconverted user a complete free export. Those clauses are right and they are conversion-destroying. That finding was not about the price point and is not disturbed by changing it.

### 4.4 What would flip this, stated because it is a real possibility

**The finding turns entirely on tenure, and I will not overstate it.** The bottom memo row is the proof: a subscriber held continuously for 36 months produces £18.33 of contribution and a floor of **4.8%** — *better* than the £14.99 one-off's 11.4%. **If Haunt retained subscribers the way a Business app does, the CEO's pairing would beat my recommendation on this exact test.**

So the honest statement is not "subscription is worse than one-off". It is: **subscription beats one-off if and only if average tenure exceeds roughly 14 months, and the retrieved data for this product's two candidate categories puts it at 5 to 8.** The crossover tenure is the single number the whole comparison rests on, and it is measurable in the first ninety days after launch at zero cost, from App Store Connect's own subscription retention reporting.

---

## 5. Recurring versus one-off on reach

The MD is right that my last model underweighted this, and right that it deserves testing rather than dismissal. Tested, it reverses.

### 5.1 The argument, stated at its strongest

Against a three-year cost base of £75,626.91, the one-off at £14.99 needs **10,564 buyers** (`window-conversion-model.md` §3.6). A subscription at 99p needs far fewer *people*, because each pays repeatedly. For a company whose binding constraint is reach — which every seat that examined it concluded — that is a structural argument, and if it held it would outrank most of what is in this document.

**Held continuously for three years**, the requirement is:

```
subscriber-months required  =  F ÷ contribution per subscriber-month
                            =  75,626.91 ÷ 0.50908  =  148,555 subscriber-months
                            =  4,127 subscribers held for 36 months
```

**4,127 against 10,564. The argument is real and the MD's arithmetic is nearly right.** His ~3,000 omits variable support; on net proceeds alone it is 2,996, and adding the £2.306/subscriber-year support line takes it to 4,127. That correction moves the number by 38% and does not touch the conclusion.

### 5.2 The argument with churn

"Held continuously" is doing all the work. Subscribers are not held for free, and at an average tenure of 5.2 months the *number of distinct people who must ever subscribe* is what the reach constraint actually binds on:

| Scenario | M (months) | **Distinct subscribers required** | vs 10,564 one-off buyers |
|---|---|---|---|
| Social & Lifestyle, pessimistic | 4.50 | **33,012** | 3.1× worse |
| **Social & Lifestyle, central** | 5.20 | **28,568** | **2.7× worse** |
| **Travel, central** | 6.30 | **23,580** | **2.2× worse** |
| Travel, optimistic | 7.63 | 19,483 | 1.8× worse |
| Business-like (upper bound) | 13.20 | 11,254 | 1.07× worse |
| *Held continuously (no churn)* | *36.00* | *4,127* | *2.6× better* |

> **Finding: on the retrieved churn data for this product's categories, the subscription ladder requires between 1.8× and 3.1× more distinct customers than the one-off, not fewer. The structural reach argument for recurring revenue is real in principle and is reversed in fact by Haunt's likely tenure.**

**Note the last two rows against each other.** The argument is not wrong; it is conditional. **The break-even tenure at which the two shapes need the same number of people is about 14 months** — and that is the same threshold §4.4 produced from a completely different calculation, which is the cross-check that both are describing the same underlying fact. Above 14 months the ladder is genuinely better on reach; below it, worse; and the retrieved category medians put Haunt at 5–8.

**One more thing the reach comparison hides, and it runs against the ladder.** The one-off's 10,564 buyers are a *cumulative* count over three years. The subscription's 4,127 is a *simultaneous* count that must be sustained continuously for 36 months — which at 5.2 months' tenure means acquiring roughly **790 new subscribers every month, for three years, without pause.** A product with no acquisition channel (idea brief objection 6) faces a much harder version of its own binding constraint under a subscription than under a one-off, because a one-off's sales accumulate and a subscription's leak.

---

## 6. The cumulative margin test, applied to the ladder

> *"Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit **against the cost of serving them**."* (Constitution v1.2, Article 2.1)

**The interpretive flag from `window-conversion-model.md` §4.1 is carried forward unchanged and unresolved**: the clause is non-redundant only because its two tests use different cost measures — the annual test against the product's cost that year, the cumulative test against *"the cost of serving **them**"*, in which a one-off build is paid for once. **If "the cost of serving them" means a pro-rata share of annual product cost, the clause is a no-op.** That is the CGO's to settle, not mine; I model the incremental reading because it is the only one on which the clause means anything. This is the second artifact to flag it; per the evidence standard's *"Twice-flagged is escalated"*, it should be resolved or accepted in writing before it anchors a third.

### 6.1 Re-test at every tier, at each tier's own honest price

Previously found: breach at ~4.0 years. Re-tested at the 20% target price for each subscriber count, L = 3:

| N | Honest monthly price | 30% cumulative cap breached at |
|---|---|---|
| 2,500 | £1.813 | **4 years** |
| 4,000 | £1.260 | **4 years** |
| 5,000 | £1.075 | **4 years** |
| 7,500 | £0.829 | 5 years |
| 10,000 | £0.706 | 5 years |

**The prior finding holds and is confirmed across the ladder.** Breach arrives at **the amortisation period plus one year**, at every scale and every tier, for the reason §4.3 of the prior document gave: cumulative margin equals the annual margin exactly at t = L, because that is where the build share is fully allocated and the two cost measures coincide; every year after adds revenue at near-full margin against a cost base that has lost its largest line.

At a **fixed** 99p rather than the honest price, the same test at N = 5,000, L = 3:

| Tenure | 1 yr | 2 yrs | 3 yrs | 4 yrs | **5 yrs** | 7 yrs | 10 yrs |
|---|---|---|---|---|---|---|---|
| Monthly 99p | −33.8% | −4.5% | +12.1% | +22.7% | **+30.2%** | +39.8% | +48.1% |
| Quarterly £2.79 | −37.5% | −9.5% | +6.4% | +16.6% | +23.7% | **+33.0%** | +41.0% |
| Yearly £10.90 | −38.8% | −11.3% | +4.3% | +14.4% | +21.4% | **+30.5%** | +38.4% |

**The discounted tiers breach later — at 7 years rather than 5 — which is the one place in this document where a discount helps.** It buys about two years of headroom against the cumulative cap, for the reason that ought to be obvious: they collect less.

### 6.2 The fix, and the fact that it works completely

Stepping the price down to the honest year-(L+1) figure at the amortisation cliff stabilises cumulative margin at exactly the annual margin, **permanently, at every tenure to infinity**:

| N | t=1 | t=3 | t=4 | t=5 | t=10 | t=20 | t=30 |
|---|---|---|---|---|---|---|---|
| 2,500, with step-down | −33.7% | +20.0% | +20.0% | +20.0% | +20.0% | +20.0% | +20.0% |
| 5,000, with step-down | −28.7% | +20.0% | +20.0% | +20.0% | +20.0% | +20.0% | +20.0% |

**This is not a new duty.** Article 2.1 already requires republication *"at every price change"*; 2.3.3.1 already makes *"Price reductions for existing customers"* the first call on the remainder; and §2.4 establishes that Apple performs the reduction on the installed base automatically and does not permit preserving the old price. **The cumulative test does not add an obligation. It names the year the existing one falls due, and the store enforces it.**

### 6.3 Lifetime at £59.40 against the cumulative test

A lifetime buyer's cumulative margin **falls** with tenure, because revenue stops and cost does not:

| N | t=1 | t=3 | t=5 | t=10 |
|---|---|---|---|---|
| 2,500 | +54.4% | +11.0% | −13.3% | −44.0% |
| 5,000 | +136.9% | +68.0% | +30.2% | −16.7% |

So the cumulative test never catches a lifetime tier. **The *annual* test catches it, in the year of purchase, and hard.** At N = 5,000 on a three-year life, £59.40 is a **68% margin** — more than twice the hard cap, which admits no justification.

### 6.4 The gaming vector, named rather than used

The two tables above compose into something Article 9 asks to be told about.

> **A lifetime tier converts a recurring price into a one-off payment, and thereby moves it outside the cumulative margin test's scope entirely.** The clause constrains what a subscriber pays *"merely by staying"*. A lifetime buyer pays nothing by staying. So the one instrument that would otherwise force the year-(L+1) step-down does not reach them — and a Candour under revenue pressure in year four, facing an automatic and unpreservable price cut on its whole subscriber base, has exactly one lawful escape: **push new customers onto lifetime.**

Article 9: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* The vector is not in the table. **I recommend a row be added: *"Escaping the cumulative margin test by converting recurring customers to one-off purchases — exposed by publishing the annual margin on every tier, including one-off tiers, at every republication."***

**This is a flag, not a block.** Amending Article 9 is an Article 11 amendment and belongs to the CEO on the CGO's advice. My charter's blocking power covers *"unpriced or uncosted launches"* and *"any proposal without a credible cost model"* (Constitution 5.6; `roles/cfo.md`), which does not reach Article 9.

### 6.5 Crossover: when a monthly subscriber overtakes the lifetime price

| Tier | Per subscriber-year | £59.40 overtaken at |
|---|---|---|
| Monthly 99p | £11.88 | **5.00 years** (exactly 60 payments) |
| Quarterly £2.79 | £11.16 | 5.32 years |
| Yearly £10.90 | £10.90 | 5.45 years |

**Whether this is an Article 1.3 problem depends entirely on the published supported life, and that is §8.** Against a three-year commitment it is a serious one: a buyer choosing "lifetime" is paying for five years of a product Candour has promised to support for three, and the crossover at which the choice pays back arrives **two years after support ends**. Against a five-year commitment the crossover falls exactly *at* the end of the supported life, and nobody is worse off on either path.

*(For comparison, the prior model's §4.5 found the crossover at exactly the amortisation period — three years — because it compared a subscription against a lifetime price both derived from the same three-year cost base. The CEO's £59.40 is not derived from that base; it is 60 × 99p. The two findings do not conflict; they price different things.)*

---

## 7. The rounding rule

The MD has put the right correction to the CEO and I agree with it. Here is the rule drafted, its maximum effect measured against Apple's actual retrieved grid, and the answer on whether it needs recording as a deviation each time.

### 7.1 The grid, retrieved rather than assumed

Apple publishes the UK price grid [E, [Apple, *App Store Pricing Update*](https://www.apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf), page 17, "United Kingdom (GBP)", retrieved 2026-09-18]:

**Price steps** — £0.10 from £0.29 to £9.99 · £0.50 from £0.49 to £49.99 · £1 from £0.99 to £199.99 · £5 from £4.99 to £499.99 · £10 from £9.99 to £999.99 · £100 from £99.99 to £9,999.99 · £1,000 from £999.99 to £11,999.99

**Supported conventions** — X.99 (£0.99–£11,999.99) · X.00 (£1–£10,000) · X.90 (£0.90–£99.90) · X.95 (£0.95–£49.95)

Supporting context: *"Choose from up to 800 price points by default"*, and *"Initially, the list displays 25 price points that follow the most common pricing convention for each country or region"* [E, [App Store Connect Help, *Set a price*](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/), retrieved 2026-09-18]. Apple's own framing confirms that *"conventional price point"* is a real, defined, retrievable thing and not a matter of taste — which is what makes a published rule possible.

### 7.2 The rule, drafted

> **Candour's price-point convention (proposed as a standing published rule).**
>
> 1. The honest price is computed first, to the penny, from the published cost sheet at the stated margin. **That figure is published on the cost sheet regardless of what is charged.**
> 2. The charged price is the **nearest available conventional price point to the honest price, in either direction.** Where two are equidistant, the **lower** is taken.
> 3. **The nearest point is never taken if it would carry the margin above 30%.** Article 2.1's backstop admits no justification, and a rounding convention is not one. Where the nearest point breaches, the next point **down** is taken.
> 4. Every rounding is recorded on the cost sheet: honest price, charged price, displacement in pence and per cent, and the realised margin at the charged price.
> 5. The rule applies identically to increases and decreases, and is never re-selected per instance.

**Clause 2 is the whole of the correction.** The MD is right that always-upward is a systematic bias: applied at every republication across a product's life it is a standing, invisible margin uplift that no cost sheet would ever show as a deviation, because each individual instance is too small to argue with. On the CEO's own example it is directly demonstrable: the nearest conventional point to **£75.40** is **£75.00** (X.00 convention, 40p below), not £75.99 (59p above). **The CEO's rule would charge 1.3% more than the nearest point, every time, for ever.**

### 7.3 Maximum effect

Bounded by half the local step. Measured against the retrieved GBP grid:

| Band | Step | Max displacement | As a percentage |
|---|---|---|---|
| £0.29 – £9.99 | £0.10 | ±5p | **±17.2% at £0.29**, ±5.1% at £0.99, ±0.5% at £9.99 |
| £10.00 – £49.99 | £0.50 | ±25p | ±2.5% at £10, ±0.5% at £49.99 |
| £50.00 – £199.99 | £1.00 | ±50p | ±1.0% at £50, ±0.25% at £199.99 |

Worked against this ladder's own candidate prices:

| Honest price | Nearest below | Nearest above | **Nearest, either direction** | Displacement |
|---|---|---|---|---|
| £0.87/month | £0.79 | £0.89 | **£0.89** | +2.30% |
| £2.77/quarter | £2.69 | £2.79 | **£2.79** | +0.72% |
| £10.78/year | £10.49 | £10.90 | **£10.90** | +1.11% |
| £37.34 paid once | £37.00 | £37.49 | **£37.49** | +0.40% |
| £59.40 paid once | £59.00 | £59.90 | **£59.00** | −0.67% |
| *£75.40 (the CEO's example)* | *£75.00* | *£75.90* | ***£75.00*** | *−0.53%* |

> **Maximum effect of the rule as drafted: ±5.1% at the monthly tier (±5p on 99p), ±3.9% at the yearly tier, ±0.9% at the paid-once tier — half the local gap, in whichever direction is nearer.**

**Under the CEO's always-upward version the maximum is the *whole* local gap rather than half of it — twice the figures above — and, decisively, it is always in the same direction.** A symmetric rule has an expected displacement of approximately zero across many republications; an always-upward rule has an expected displacement of *half a step, every time, for ever*. Over a product life with an annual republication (§2.4), that is not a rounding convention. It is an undeclared standing margin uplift that no individual cost sheet would ever show as a deviation, because each instance is too small to argue with. **That is precisely the structure Article 9's *"Quietly weakening the rules"* row exists to catch, and the MD is right to have raised it before it was written down rather than after.**

### 7.4 The finding that makes this more than housekeeping

At the monthly tier the grid is coarser than the compliance band. At N = 4,278 (where 99p is exactly on target, L = 5):

| Monthly price | Realised margin |
|---|---|
| £0.79 | −0.6% |
| £0.89 | **+9.9%** |
| **£0.99** | **+20.0%** |
| £1.09 | **+29.8%** |
| £1.19 | +39.2% |

> **One available price step spans the entire distance from the Article 2.1 target to within 0.2 percentage points of the hard cap. At a 99p price point, Apple's price grid has lower resolution than Candour's constitution.**

Three consequences:

1. **Rounding is the dominant determinant of margin at this tier**, ahead of every cost assumption in the model. A 10p step outweighs the Android platform-mix uncertainty, the ICO fee, and the entire fixed non-labour line combined.
2. **Clause 3 of the rule is not belt-and-braces; it is load-bearing.** Without it, a single upward round at the monthly tier can carry the product through the hard cap in one move.
3. **Haunt cannot be priced accurately at a monthly cadence.** The quarterly and yearly tiers have four and twelve times the resolution for the same annual revenue. **This is an argument for making the yearly tier the headline and the monthly tier the convenience**, and it is a pricing-accuracy argument rather than a commercial one.

### 7.5 Standing convention, or a deviation each time?

**Both, and the split is clean.**

- **The rule is a standing published convention.** It is a *method*, published in advance, symmetric in direction, applied identically to every product and every republication. Article 2.1 requires that deviations from the margin target be *"justified in writing on the cost sheet"*; a published symmetric method justified once is not a fresh judgment each time, and re-justifying it per instance would be ceremony. Publishing it once is also strictly stronger, because it removes the discretion — which is what Article 9's *"Quietly weakening the rules"* row is written against.
- **The resulting margin is recorded every time, on every tier.** Article 2.1 requires the margin to be recorded and justified, and §7.4 shows why it cannot be inferred: at the monthly tier the charged price's margin is not approximately the honest price's margin. **What is standing is the rule; what is per-instance is the number.**
- **Clause 3 is absolute and is not a convention at all.** *"no product's margin may exceed 30%, regardless of justification"* — a rounding convention is a justification, and the clause excludes it.

**One thing the rule cannot do, stated so it is not assumed.** I retrieved Apple's published GBP grid; I did **not** retrieve the complete list of 800 price points as it appears inside App Store Connect, which is not published. The step/convention tables above should reproduce it, but **the exact nearest point must be confirmed in App Store Connect before any price is published**, and Google Play's GBP grid is a separate list I could not retrieve at primary this session (Google's currencies-and-price-ranges page redirects to a supported-locations table that did not render). Two stores with different grids may not offer the same nearest point, which is a small, real, unresolved operational item. Listed in §12.

---

## 8. "Lifetime" against the published supported life

This is where the CEO's two numbers meet, and the result is cleaner than I expected.

### 8.1 The Constitution's requirement, quoted

> *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year… Three conditions bind that treatment: **the amortisation period must equal a published support commitment to customers**; any unamortised remainder is written off publicly on discontinuation (7.2); and the period may be shortened, never lengthened. **Absent a published support commitment, build labour is a first-year operating cost.**"* (Constitution v1.2, Definitions)

**Candour has published no support commitment for Haunt.** Every figure in every Haunt model — including all of this one — amortises. **On the clause as written, that treatment is currently unavailable**, and the correct treatment is to charge the entire £45,957.55 to year one, which puts the honest first-year price beyond any consumer market at any volume this company has evidence for. This was recommendation 2 in `window-conversion-model.md` §5.4 and it is unactioned. **It is a prerequisite of the ladder, not a nicety.**

### 8.2 The CEO's own arithmetic names the period

99p × 12 × 5 = £59.40. I tested that against both candidate lives:

**Against a three-year published life:**

| | Cost recovery | 20% target | **30% hard cap** |
|---|---|---|---|
| Monthly 99p | N = 4,126 | N = 5,652 | **N = 6,590** |
| Paid-once £59.40 | N = 2,151 | N = 2,810 | **N = 3,186** |

> **The two bands do not overlap, and they do not come close.** At N = 4,126 — the lowest volume at which 99p/month even recovers its cost — £59.40 is already **+52%**, far through a cap that *"admits no justification"*. At N = 5,000 it is **+68%**. Conversely, at any N where £59.40 is lawful, 99p/month is selling below cost. **Against a three-year commitment the CEO's ladder has no compliant subscriber count at all.**

**Against a five-year published life:**

| N | 2,500 | 3,122 | 3,500 | 4,000 | 4,278 | 4,500 | **4,988** | 6,000 | 8,000 |
|---|---|---|---|---|---|---|---|---|---|
| **99p/month margin** | −13.3% | 0.0% | +7.1% | +15.7% | **+20.0%** | +23.3% | **+30.0%** | +42.0% | +60.3% |
| **£59.40 once, margin** | −13.3% | 0.0% | +7.1% | +15.7% | **+20.0%** | +23.3% | **+30.0%** | +42.0% | +60.3% |

> **Identical. Not approximately — exactly, at every subscriber count.**

This is not a coincidence and the algebra says why. Over five years the cost of serving one customer is `BUILD/N + 5·(FIX/N + s)`, and with a five-year amortisation the monthly tier's five-year cost is `5·((BUILD/5 + FIX)/N + s)` — the same expression. Five years of £11.88 is £59.40. **The CEO has priced a five-year product. He has simply not published the five years.**

### 8.3 What the commitment costs

| | L = 3 years | **L = 5 years** |
|---|---|---|
| Amortised build per year | £15,319.18 | **£9,191.51** |
| Annual fixed cost `A` | £25,202.74 | **£19,075.07** |
| **Total cost base over the life** | **£75,626.91** | **£95,394.03** |
| Compliant band at 99p/month | 4,126 – 6,590 | **3,122 – 4,988** |
| Blended band across the ladder | *no overlap with £59.40* | **3,523 – 4,988** |

**The five-year commitment costs £19,767 more in benchmarked labour and makes the ladder cheaper to run per year.** Both are true: spreading the build over five years lowers the annual charge by £6,128, and running fixed maintenance for two extra years costs £19,767. The band moves **down** by about a quarter, which is the one piece of unambiguously good news in this document — a five-year commitment makes the CEO's price lawful at a lower subscriber count than a three-year one would.

**Three things travel with it, and the CEO should see all three before publishing it:**

1. **It is effectively irrevocable in the customer-facing direction.** The Definitions permit shortening the amortisation *period*; they say nothing about shortening a *support promise already made to customers*, and CRA 2015 s.36 makes pre-contract information about characteristics and functionality a contractual term [E, [CRA 2015 s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36), retrieved by CGO 2026-09-17, read from `compliance-note.md` §4.2 this session]. **"Supported until 2031" is a term of the contract, not marketing.**
2. **Five years is a long time for a background-location app on two platforms.** The CTO's 220 hours/year maintenance estimate was made for a three-year horizon; five years spans five iOS and five Android major releases, each of which historically breaks background-location behaviour. **Whether 220 h/yr holds to year five is the CTO's to answer and it is not answered.** If it does not, every number above moves. Listed in §12.
3. **It answers the UX seat's objection to the word "lifetime" completely.** A dated promise — *"Haunt is supported until [launch + 5 years]"* — is checkable. The word "lifetime" is not.

### 8.4 The name

Even at L = 5, a tier called **"lifetime"** sold against a published five-year support commitment is two public numbers disagreeing, and Article 1.3 says *"**Honest by default.** Pricing, capability, and limitations are stated plainly. We say what a product cannot do."*

**My recommendation on the label, as judgment [J]:** call it what it is. *"Pay once — £59.40. Supported until [date], the same as every other tier. The same as paying 99p a month for the whole of that period, with nothing to cancel."* That sentence is true, it states the crossover Article 1.3 requires (§6.5), and it is the only version I can see surviving a sceptical reader who has both public numbers in front of them.

**And note what it buys.** At L = 5 the crossover falls **exactly at** the end of the supported life (§6.5), which means **no customer is worse off on either path, on Candour's own published promise.** That is an unusually clean thing to be able to print, and it exists only because of the five-year commitment. Under the three-year version, the paid-once buyer's payback arrives two years after support ends, and I would not know how to write the pricing screen honestly.

---

## 9. What the ladder costs that the one-off did not

Every number above uses the **unchanged** cost base from `window-conversion-model.md` §3, which was built for a one-off purchase. **That errs in the ladder's favour**, and the omissions are named rather than buried.

### 9.1 Build and support increments — the CTO's to size, not mine

Subscription mechanics that a one-off unlock does not need: entitlement and lapse state, receipt validation and restore-purchases on an architecture with no server, grace periods and billing retry, a subscription-management screen, the free tier's second permission tier, and — if a visibility window exists — Condition 8.6's requirement that every aggregate carry two result sets or a partiality banner. **None of this is in the CTO's 1,330 hours**, which were decomposed before a subscription was in scope.

Sensitivity, at 99p/month, L = 5 — [J] increments, stated so the CTO can replace them:

| Increment | Cost recovery at | 30% cap at |
|---|---|---|
| None (the base case above) | 3,122 | 4,988 |
| +150 h build, +20 h/yr fixed | **3,390** | 5,415 |
| +250 h build, +40 h/yr fixed, free:paid 4:1 | **6,034** | 16,138 |

**A 150-hour subscription increment — four focused weeks — moves the bottom of the band up by 9%.** That is not fatal on its own and it is not zero, and it should be a real CTO estimate before a price is published rather than a placeholder in a CFO note.

### 9.2 The DMCCA subscription regime, which the one-off avoided and the ladder revives

The CGO recorded this precisely: *"the DMCCA subscription-contracts regime does not bite, both because Haunt is a one-off purchase and because commencement has been pushed to spring 2027… **If the CFO's Model 3 is ever revived, this regime is a material new cost and must be re-priced, not assumed.**"* [E, `products/haunt/compliance-note.md` §4.5, read from disk 2026-09-18]. **The CEO's proposal is that revival.**

Retrieved this session: commencement **spring 2027**; two 14-day cooling-off periods, an initial one and a **renewal** one that triggers after a free or discounted trial ends or after a 12-month-plus contract auto-renews; and reminder notices that must be *"in writing on a durable medium, with their purpose immediately apparent to the consumer"*, where *"email, SMS, and WhatsApp qualify as durable media, but fleeting in-app notifications that cannot be retained do not"* [E, [Osborne Clarke, *UK DMCCA subscription contracts regime to take shape*](https://www.osborneclarke.com/insights/uk-digital-markets-competition-and-consumers-act-subscription-contracts-regime-take-shape), retrieved 2026-09-18; **secondary, law-firm briefing, single underlying origin (the DBT consultation response), not retrieved at source — flagged**].

**Two things follow, and I flag both rather than adjudicating either.**

**(a) A durable-medium reminder obligation may be unservable on this architecture.** Haunt has no server, no account, and no email address; Apple is merchant of record and does not pass the subscriber's email to the developer. Discharging a reminder-notice duty would require Candour to **collect an email address** — a new personal-data collection on a product whose entire proposition is that it collects nothing, which would make Candour a controller, would make the ICO fee certainly rather than probably owed, and would need a new build, a new privacy surface and a new Article 4 assessment. **Whether the duty falls on Candour or on Apple is genuinely open**, and the CGO has already established the fact that decides it: *"the consumer's contract of sale is with Apple, not with Candour"* [E, `compliance-note.md` §4.1]. **This is a CGO determination with a direct and potentially large cost consequence, and it should be made before a subscription is priced, not after.**

**(b) Article 4's cancellation clause starts biting.** The CGO recorded that *"a clause aimed at subscription traps does not bite on a product that is not a subscription — and… the clause **will** bite hard if the CFO's Model 3 (subscription) is ever revived"* [E, `compliance-note.md` §4.3]. It now does.

### 9.3 The two-week free trial

**Which reading I am modelling, and why.** The CEO said "two weeks free on monthly". I model it as a **two-week full-feature introductory free trial on the monthly tier**, not as a standing 3.85% discount, for three reasons:

1. **It is a thing the store actually does, at exactly that duration.** Apple's introductory offers are *"free trial, pay up front, and pay as you go"*, and for a subscription with a 1-Month standard duration the free-trial durations available are *"3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year."* [E, [App Store Connect Help, *Set up introductory offers for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), retrieved 2026-09-18]. **"2 Weeks" is a listed option.** A standing two-weeks-per-year discount has no mechanism on either store.
2. **The other reading breaks the ladder.** A 3.85% standing discount on monthly would put monthly at £11.42/subscriber-year against quarterly's £11.16 — a 2.3% gap, which is inside the rounding rule's own resolution at that tier (§7.3) and destroys the monotonicity the CEO has just asked for.
3. **The compliance note records this exact structure as clean.** *"a **time-limited full-feature trial** is neither a dark pattern nor a read-cap, and remains available… **Permitted:** a trial limited in *time* or in *future creation*, disclosed before the user writes anything, after which everything already written remains readable, editable and exportable forever, at no charge."* [E, `compliance-note.md` §4.4, read from disk 2026-09-18]. That is the CGO's finding, quoted rather than characterised.

**What it costs.** Forgone revenue of half a month's net proceeds per converting trialist (£0.351), plus 14 days of free-rate support for everyone who starts one (£0.024):

| Trial-to-paid rate | Cost per trial start | Cost per converted subscriber | As a share of that subscriber's lifetime contribution (M = 5.2) |
|---|---|---|---|
| 5% | £0.041 | £0.82 | **31.1%** |
| 10.7% (the hard-paywall median) | £0.061 | £0.57 | **21.6%** |
| 20% | £0.094 | £0.47 | 17.7% |
| 40% | £0.164 | £0.41 | 15.5% |

**The trial costs between 15% and 31% of everything a converted subscriber will ever contribute.** That is affordable and it is not small, and it is entirely a function of how little a 99p subscriber is worth. Constraints: one current and one future introductory offer per storefront, and *"Each person is only eligible to redeem one introductory offer per subscription group"* [E, same Apple page].

**The finding that matters more than the cost.** A permanent free tier and a two-week full-feature trial are **competing mechanisms for the same job**, and they do not compose. The trial converts by showing the whole product and taking it away on a date; the free tier converts by withholding part of the product permanently. **A user who has a permanent free tier has no reason to start a trial, and a user who has had the trial has already seen what the free tier is withholding.** Running both means paying for both and getting the conversion behaviour of the weaker one. **If the CEO wants the trial — and the retrieved data says the trial is the better instrument by a factor of five — the free tier is the thing to drop, not the ladder.**

---

## 10. Recommendation

My charter requires a recommendation with a reason rather than a menu.

> ### Publish a five-year support commitment. Ship the ladder with a two-week full-feature trial and **no permanent free tier**: 99p monthly, £2.79 quarterly, £10.90 yearly, £59.40 paid once — renamed — with the price reviewed and republished annually and stepped down at year six.

### 10.1 The reason, in the order the arithmetic produced it

1. **The free tier is the part that fails, and it fails on its own numbers rather than on my preference.** At any evidenced conversion rate, 99p per month cannot recover its cost at any subscriber count (§2.5); the break-even conversion floor is 22–37% against a 2.1% median (§4.2); and a free tier and a trial compete for the same job while the trial converts five times better (§9.3). **This is the same finding as 2026-09-17, reached again from a different price point and a different revenue shape**, which is the only kind of confirmation worth having.
2. **The ladder itself is not the problem, and I have changed my position on it.** On 2026-09-17 I recommended against subscription outright. With the five-year commitment published, the subscription tiers are constitutionally clean: the band is narrow but real, the cumulative test is satisfiable by an act Apple performs automatically, and the paid-once tier at £59.40 is *exactly* consistent with monthly. **My earlier recommendation bundled the subscription with the free tier and the window. Separated, only two of the three fail.** I record the change because a seat that never moves is not being useful.
3. **The five-year commitment is not optional and it is not a formality.** Without it the amortisation treatment is unavailable under the Definitions, the whole build goes to year one, and no ladder is priceable. With it, the CEO's two numbers become the same number and the crossover problem disappears (§8).
4. **The narrow band is survivable; the cadence is the thing to accept deliberately.** 3,523–4,988 subscribers is a 1.42× window, and the honest description is that Candour will be re-pricing Haunt roughly annually for its whole life, with Apple performing the cuts irreversibly (§2.4).

### 10.2 What I am recommending against, and what I am not

**Against:** a permanent free tier, at any cap, on any tier structure. **Against:** discounts deeper than roughly 10%, because they close the band (§2.3). **Against:** the word "lifetime" (§8.4). **Against:** shipping without the CTO's subscription-mechanics estimate and the CGO's DMCCA determination (§9).

**Not against, and stated so silence is not read as consent:** the ladder shape itself; the 99p price point, which is defensible at 3,122–4,988 subscribers; and the £59.40 paid-once tier, which is arithmetically exact at a five-year life.

### 10.3 The thing I record against my own recommendation

The same one as last time, because it has not stopped being true. **The CEO's decision to build Haunt was explicitly not a commercial decision** — *"I quite like this idea for myself personally and if I can release it and it makes a bit of money then I am happy with that"* [E, `decisions/2026-09-16-haunt-gate.md`]. A recommendation optimising commercial outcome is answering a question he did not ask.

**What survives under his actual objective**, which is that Haunt exists, is good, and is sold honestly: the free-tier finding survives, because it is not about optimisation — at a 2.1% conversion rate the free tier's support cost is three and a half times what a subscriber pays, so free users would be carried by a founder who is already not recovering his own benchmarked labour. The ladder survives too. **The discount-depth finding and the band-width finding are commercial-optimisation findings and I flag them as the weakest things in this document under his stated objective.**

### 10.4 What follows, in order

1. **CEO** — publish a support commitment, dated, product-level. Five years if the ladder proceeds. Everything else waits on this.
2. **CEO** — decide the free tier. §2.5 and §4 are the arithmetic; the decision is his under 5.4.
3. **CEO** — adopt or amend the rounding rule (§7.2), which is a company-level convention rather than a Haunt one.
4. **CGO** — the DMCCA reminder-notice determination (§9.2), which may be the largest unpriced item in this document; and the still-unresolved reading of *"the cost of serving them"* (§6), now twice-flagged.
5. **CTO** — the subscription-mechanics build increment, and whether 220 h/yr maintenance holds to year five.
6. **UX** — re-test the finding at §11.2. Not mine.
7. **CEO / CGO** — Condition 9 and the Article 9 amendment at §6.4 and §11.1.

---

## 11. Two scope flags

### 11.1 Condition 9 records the one-off *shape* as decided; a ladder changes the shape

Decision record Condition 9: *"**Pricing is not set by this record.** Price remains a Constitution 5.4 decision, unavailable until Condition 1 completes. **The one-off purchase *shape* is decided; the number is not.**"*

A subscription ladder with a free tier is a change of shape, not of number. That is the CEO's to make under 5.4 — *"pricing changes"* are expressly his — but it **amends a decision record that publishes under Article 3 by 2026-10-16**, and the CVO has already recorded the governance handling: *"Moving to dual pricing changes the shape. That is the CEO's under 5.4, but it amends a record that publishes under Article 3 by 2026-10-16, so it is corrected in the open rather than silently superseded"* [E, `proposals/haunt/ceo-product-inputs.md` §3].

**I flag, and do not block.** My charter's power is *"unpriced or uncosted launches"* and *"any proposal without a credible cost model"* (Constitution 5.6), which does not reach the governance of a decision record. **The seat that holds gate and record integrity is the CGO.** What I record is that the amendment is owed **in the same publication** as the record itself, and that three further amendments now ride on it: the support commitment (§8.1), the Article 9 row (§6.4), and the break-even basis that has already moved from ~2,400–2,700 to ~10,600 and is unactioned from the prior document.

### 11.2 Where this model depends on the UX finding being re-tested — and it is not mine to re-test

The UX seat found: *"**Free + subscription: cannot be built honestly**, because the only thing that makes a lapse matter is locking a journal that sits on the user's own phone"* and *"There is no third branch"* [E, `products/haunt/ux-note.md` §6.3 and §7, read from disk 2026-09-18].

**That finding predates Corrections C1 and C2 and the lapse behaviour the CEO has since settled.** Specifically: C1.1 disposed of the export-clause ground; C2.2 disposed of the Article 1.2 ground; C2.6 records the UX seat's B2 block as *"zero-now, not zero-forever"*; and the CEO's own clarification inside Condition 8.2 settled a **third** branch the UX note said did not exist — *"A lapsed subscription returns the user to the free tier's published window, and entries outside it become hidden — **not deleted**… exportable in full at any time under 8.3, enumerable under 8.5, and restored in full on renewal."* The CVO had also identified a fourth: *"a lapse stops **automatic capture** while everything already written stays readable, editable and exportable forever"* [E, `ceo-product-inputs.md` §3].

**Exactly where my model depends on it, named so the dependency is visible:**

| What in this document | Depends on | If UX's finding is re-tested and **stands** |
|---|---|---|
| The whole subscription ladder (§3), the band (§2), the cadence (§2.4) | A subscription lapse being buildable without a dark pattern | **The ladder is unavailable and this document's §§2–7 are moot.** The paid-once tier survives as a one-off. |
| §9.3's trial | A trial expiry being buildable without a dark pattern | The compliance note already records the trial as clean (§9.3); low dependency. |
| §2.5, §4 (the free-tier findings) | Nothing. They are arithmetic. | **Unaffected.** The free tier fails on cost whether or not it is buildable. |

**I am not re-testing it and I will not.** It is a release block on flows, on Article 4 grounds, held by the UX seat; the evidence standard is explicit that *"a process that answers an interpretive failure by adding agent passes is prescribing more of what already failed"*, and C2.6 already corrected this seat once for reaching outside its charter on exactly this question. **What I record is that the CEO's ladder requires that finding to be re-tested by UX before it can be built, that the grounds it originally rested on have both fallen, and that the lapse behaviour it said did not exist now does.**

---

## 12. What would overturn these findings, and where I looked

Required by the universal charter clause: *"**Negative findings carry the same duty as blocks.** Any finding that something is infeasible, prohibited, unaffordable or not worth doing must state (a) what evidence or change would overturn it, and (b) where you looked."*

### 12.1 The free-tier finding (§2.5, §4) — my strongest negative

**Overturned by any of:**

1. **A measured conversion rate above roughly 12%.** The thresholds are exact and worth stating as such, because they are what a test would be measured against. At 99p/month, L = 5, the free tier's support cost alone puts a floor under the cost of service, so: below **9.1%** conversion the price can never recover its cost at any volume; below **12.1%** it can never reach the ~20% target; above **13.9%** the full band reopens. At 20% conversion (4:1) it runs 5,227–13,981. **This is the cleanest falsifier in the document and it is measurable free**, in the Play Console's mandatory 12-tester closed test and in TestFlight, before a penny is spent on a free tier. The retrieved median is 2.1%, so the test would have to come back at **four to six times** the benchmark — but it is a cheap test and the CEO is entitled to run it rather than take my table for it.
2. **A materially lower free-user support cost.** `S_free` = £0.615/year is the sole cause of the floor and it rests on the CTO's Android contact-rate judgment scaled by mine. At £0.20 the 9:1 band reopens at ~7,500. **This is the most likely of the falsifiers to be true** — a free user who cannot use automatic capture generates far fewer background-location support cases than a paying one, and nobody has measured it. I said this on 2026-09-17 and it remains the strongest argument against my own position.
3. **An independent second source on freemium conversion materially above 2.1%.** My benchmark is single-origin (RevenueCat) and now carries *two* single-origin claims from that publisher — conversion and renewal rates. **Flagged twice in this document and previously twice; this is escalation territory under the evidence standard.**
4. **A measured average tenure above 14 months**, which flips both §4 and §5 simultaneously (§4.4, §5.2). Measurable in App Store Connect's subscription reporting within 90 days of launch.

**What would *not* overturn it:** a higher subscription price (the floor falls with price, but §2.2 shows the compliant price at any evidenced volume is already near the top of the band); a longer free-tier cap; or a larger reach multiple — `r` remains, as of this document, **a number no seat in this pipeline has ever written down**, and I checked again this session.

### 12.2 The band-width finding (§2)

1. **A CGO determination that shared company costs are allocated across products** rather than wholly to Haunt (my §3.4 recommendation of 2026-09-17, unactioned) — immaterial here at 0.2% of the base.
2. **A materially different build estimate.** The band's position, not its width, is proportional to `A`. Width is invariant: it is set purely by the ratio of the 30%-cap cost to the cost-recovery cost, so **no cost estimate changes the 1.60× figure.** That is why I state width separately from position.
3. **A CEO decision to run a deliberate, published, sustained deviation below target** — permitted by Article 2.1 and it would widen the usable range downward at the cost of not recovering benchmarked labour.

### 12.3 The cumulative-margin finding (§6)

Unchanged from `window-conversion-model.md` §6.2, and re-confirmed across all four tiers: a CGO determination on *"the cost of serving them"*; a commitment to the year-(L+1) step-down, which resolves it completely and permanently (§6.2); or a shorter amortisation period.

### 12.4 Where I looked

**Retrieved from disk this session, in full:** `constitution.md` (v1.2 — Definitions, Articles 1, 2.1, 2.3, 3, 4, 5.2, 5.4, 5.6, 6.1, 7.2, 9, 10, 11); `roles/cfo.md` as amended; `pipeline/evidence-standard.md` v1.1 including *"Claims about our own rules"*; `decisions/2026-09-16-haunt-gate.md` in full including Conditions 1–10 and Corrections C1 and C2; `products/haunt/window-conversion-model.md` in full; `products/haunt/cost-sheet.md` in full including both §8.2 correction banners; `products/haunt/compliance-note.md` §§4.1–4.5 in full; `products/haunt/ux-note.md` §§6–7 and the C2.6/C2.7 banner; `proposals/haunt/ceo-product-inputs.md` in full; `pipeline/templates/` (directory listing — no template exists for this artifact type).

**Retrieved externally this session:** ONS ASHE Table 14 2025 provisional, **at primary, tables 14.7a, 14.7b and 14.5a, row SOC 2134** — the retrieval that closes Condition 5; Apple's published GBP price-step and convention grid; App Store Connect Help on price points, on introductory offers, and on subscription price changes; RevenueCat *State of Subscription Apps 2026* and its renewal-rate-by-category companion; Osborne Clarke on the DMCCA subscription regime.

**Attempted and failed:** Google Play's GBP price-range table at primary (the currencies-and-price-ranges support page redirects to a supported-locations table that did not render); Taylor Wessing's DMCCA briefing (HTTP 403); the complete App Store Connect 800-point GBP list (not published outside the tool).

**Looked for and did not find:**
- **Any monthly retention curve beyond the first renewal** in any retrieved source. This is why §4.2's tail is a stated `[J]` parameter rather than a retrieved one, and it is the largest single uncertainty in §§4–5.
- **A reach multiple `r` for a Haunt free tier** — searched the same five artifacts as on 2026-09-17 plus `ceo-product-inputs.md`. **Still absent, not merely unverified.**
- **An independent second origin** for either the conversion or the renewal benchmark. Both are RevenueCat.
- **Any published Candour support commitment for any product.** Absent; §8.1 is the consequence.

### 12.5 Blocks and flags, labelled per the amended charter

**Blocks lifted:** one. *The ONS ASHE benchmark block is discharged* (§1). Nothing in my charter now bars Article 3 publication of a Haunt price on evidence grounds.

**Blocks held:** one, and it is the ordinary standing form of my charter power rather than a new objection. *No price may be published under Article 3 without a cost sheet behind it, and the cost sheet for this ladder is not complete until the support commitment is published (§8.1) — because absent it the Definitions make build labour a first-year operating cost and every figure in this document is wrong by a factor of about three.* **What lifts it:** the published commitment, or a re-derivation on the first-year-expense treatment. This is *"launch of any pricing not backed by a published cost sheet"* (Constitution 5.6; `roles/cfo.md`), on the Constitution's own Definitions, and it is the narrowest form of the point.

**Blocks not held, stated so silence cannot be read as consent.** I hold **no block** on: the free tier (§2.5, §4 are **findings**, and the decision is the CEO's under 5.4); the ladder shape (§11.1 is a **flag**, and the seat is the **CGO**); the lapse design (§11.2 is a **flag**, and the seat is **UX**, whose B2 release block C2.6 records as engaging on any Article 4 or Condition 8.1–8.6 breach); the DMCCA determination (§9.2 is a **flag**, and the seat is the **CGO**); or the Article 9 amendment (§6.4 is a **flag**, and it is an Article 11 matter for the **CEO**). My charter reaches the price level and the cost model. It does not reach Article 4, Article 9, or product shape — a distinction C1.3 and C2.6 corrected against this seat once, and I am not repeating it.

---

## 13. Gaps, corrections owed, and disclosures

### 13.1 What this seat could not establish

| Gap | Why it matters | Owner |
|---|---|---|
| **Monthly retention beyond the first renewal** | Sets `M`, which drives §4 and §5 entirely; the 14-month crossover is the hinge of the whole comparison | Measurable free in App Store Connect within 90 days of launch |
| **Conversion and renewal benchmarks are both single-origin (RevenueCat)** | Two load-bearing claims, one publisher. **Flagged in two documents now** | CFO / Research Analyst — escalation is due |
| **Whether the DMCCA reminder-notice duty falls on Candour or Apple** | Potentially the largest unpriced item here: it may require collecting email addresses on a product that collects nothing | **CGO**, and Constitution 6.1 may put it with a qualified human |
| Subscription-mechanics build increment | Not in the CTO's 1,330 hours; ~150 h moves the band's floor ~10% | **CTO** |
| Whether 220 h/yr maintenance holds to year five | A five-year commitment spans five OS major releases on two platforms | **CTO** |
| Google Play's GBP price grid at primary | The nearest conventional point may differ between stores | CFO, before publication |
| The reach multiple `r` | The only input a free-tier case depends on; never written down by any seat | Research Analyst / CEO |
| iOS/Android platform mix | Moves `s` and therefore the whole band | Testable free in the Play 12-tester closed test |
| Session segmentation and the venue-page aggregate layer | Both are net additions to the cost base; every band above is therefore a **floor** on volume | **CTO** |

### 13.2 Correction banners owed

Owed **visibly, in place, and in the same publication as the decision record (due 2026-10-16)**:

| File | What is owed |
|---|---|
| `products/haunt/cost-sheet.md` §2.4 | The ONS flag is **closed**: the benchmark is retrieved at primary and the secondary figure was exact. §1. |
| `products/haunt/cost-sheet.md` §2.1 and §13 | Apple's UK merchant-of-record position is `[E]`, not `[K, unverified]` — retrieved by the CGO. §1.3. |
| `products/haunt/window-conversion-model.md` §3.1 and §6.4 | Flag 1 and the standing block are discharged. §1. |
| `products/haunt/compliance-note.md` §4.3 and §4.5 | Model 3 is revived; the DMCCA regime and Article 4's cancellation clause now bite. §9.2. |
| `products/haunt/ux-note.md` §6.3 | Flagged for re-test by the UX seat, not corrected by me. §11.2. |
| `decisions/2026-09-16-haunt-gate.md` Condition 9 | The shape has changed; the record needs amending in the open before publication. §11.1. |

### 13.3 Related-party disclosures

**None.** No payment to the founder, family or any affiliated entity is contemplated in this model. All founder labour is costed at the published external benchmark — now retrieved at primary (§1) — and is currently unpaid and undrawn; it appears here as cost because Constitution 2.1 requires *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

---

## Change log

| Date | Change |
|---|---|
| 2026-09-18 | Created, at the CEO's direction, modelling a subscription ladder with a permanent free tier. **Closes Condition 5** of `decisions/2026-09-16-haunt-gate.md` — ONS ASHE retrieved at primary; this seat's standing publication block is lifted. Extends rather than supersedes `window-conversion-model.md`. External prices and benchmarks retrieved 2026-09-18. **Not a published cost sheet and not a price.** |

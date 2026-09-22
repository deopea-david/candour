# Cost sheet — Haunt — v3 (pre-requirements, publishable)

**Seat:** Chief Financial Officer · **Date:** 2026-09-21
**Status: intended for publication under Constitution 2.1 and Article 3.** Written for a sceptical customer first and the CEO second. **It is not a price.** Pricing is a Constitution 5.4 decision — *"The following are never automated: kill/proceed decisions, spending real money, **pricing changes**… Agents prepare; the founder decides"* — and belongs to the CEO alone.

**Supersedes** `products/haunt/cost-sheet-v2.md` in full, and with it `cost-sheet.md`, `pricing-ladder-model.md` §§2–9 and `window-conversion-model.md` §3. Where this sheet corrects one of my own earlier findings it names the error in place rather than quietly restating it (§18).

**What changed since v2, in one paragraph.** Constitution **v1.3** fixed the amortisation period at **three years, company-wide**, decoupled it from any support promise, and added two duties this sheet discharges for the first time: a published **amortisation schedule** (Article 2.1) and a statement **on the face of the sheet** that the period is not a support horizon (Article 4). The CEO decided at **D4** that **Haunt publishes no guaranteed support date**, and at **D7** that the cumulative lifetime margin test binds on the incremental reading with a **minimum notice period** before any price rise. The **PM/BA's requirements document** settled the scope at 139 requirements, and the **CTO's Block 4 ruling** added work and cancelled a spike. This sheet re-derives everything on those.

**Evidence:** tagged per `pipeline/evidence-standard.md` v1.1. Every external figure below was **retrieved at primary on 2026-09-21** in the session that produced this document, with the link travelling with the claim; nothing external is cited from memory. The one exception is stated where it occurs (§3.1) and is attributed. Every constitutional claim quotes the clause it relies on in the same passage, per that standard's *"Claims about our own rules"*. Where a statement is this seat's professional judgment rather than a requirement, it says so, per *"A seat's heuristic is not an article."*

**Template note:** `pipeline/templates/cost-sheet.md` assumes a monthly hosting-shaped cost table and a single price. Haunt has no hosting and four price tiers. This sheet keeps the template's required elements — itemised costs, related-party disclosures, price, margin, deviation and justification, change log — and adds the sections Article 2.1 as amended now requires. The deviation from the template is stated rather than made silently.

---

## 0. The answers, before the arithmetic

**A. My standing block lifts. It is the first sentence because it is the one the pipeline is waiting on.** The block was narrowed at `cost-sheet-v2.md` §16.1 to *"no Haunt price publishes under Article 3 until the period is published… The block is about the existence of a published period, not about which one."* The period is published: Constitution v1.3, Definitions — *"**Standard amortisation period:** **three years (36 months)**, straight-line, in equal monthly amounts"* — recorded at CEO decision **D6** and in `CHANGELOG.md` v1.3. **The checklist item that was failing now passes. I lift the block and I do not replace it with another.** §17.

**B. The cost base is £43,132.09 a year, against v2's three-year figure of £40,517.17 — up 6.4%.** Three things moved it: the Block 4 ruling's new build work, a security-and-defect maintenance line I am now carrying rather than flagging, and **the cost of the AI workforce, which no Candour cost sheet has ever carried and which is now the largest cash line in the company.** §3.

**C. The scope in `requirements.md` does exceed what I last costed, in four ways, and the fourth is the large one.** (1) The Block 4 ruling adds 2–4 days. (2) Five new requirements from the PM/BA are unsized. (3) One regression-fixture requirement may or may not sit inside the CTO's venue rows. (4) **No Haunt cost sheet, including both of mine, has ever costed the non-engineering build labour** — the requirements, the architecture notes, the compliance notes, the UX notes, the cost sheets. The Definitions say Cost is *"everything it takes to run a product or the company, itemised… and labour valued at a published market benchmark whether or not it is actually paid."* That means all labour, not the engineering share. §4.

**D. And Article 2.1 now asks for a number Candour cannot produce.** It requires *"capitalised hours as a share of all hours worked on the product that year."* The numerator is 2,300.5 hours. **The denominator does not exist, because nobody records hours.** This sheet says so on its face rather than printing a ratio computed from a denominator equal to the numerator, which would read as 100% and would be false. §3.3.

**E. The price-cliff figure the PM/BA is blocked on: the cut is 30.3%, the monthly price falls from 99p to 69p, and the date is launch + 36 months.** The 30.3% figure is not in fact missing from the repository — it is at `cost-sheet-v2.md` §5.1 and at Correction **C5.4**, both on the v2 cost base at three years, and it re-derives exactly. What *was* missing is everything around it, and one of those things changes the copy: **the cut is conditional on subscriber count and below about 7,170 subscribers no cut falls due at all.** §8.

**F. That conditionality is a correction to my own work and to three places in the decision record.** Condition 9.4, Condition 9.5, C5.4 and `cost-sheet-v2.md` §10 all present the step-down as automatic. It is not. It is Article 2.1's margin cap falling due, and a cap is only breached at volume. **A pricing screen that promised an unconditional cut would be promising something Candour might not owe, which is the same class of error as promising a support date.** §8.3, §18.

**G. The pay-once price is £28.99, and the discount is real: £6.65 over three years, 18.6% against paying monthly.** That closes UX's block **B11** on its own terms — £59.40 was exactly 60 × 99p and saved nothing; £28.99 against £35.64 saves something a customer can check in one subtraction. The crossover falls at **month 30**, not month 29 as v2 said. §11.

**H. D2's missing hours survive its supersession, and I am now carrying them rather than flagging them.** The promise is gone; the work is not. A React Native app with four native modules and two SDK majors a year has a dependency-CVE surface whether or not anyone promised to patch it. Correction **C5.4** already settled the principle — *"the hours are owed whether or not anything was promised"* — and this sheet is where that becomes a number: **45 h/yr, provisional, £1,471.95, 3.4% of the cost base.** §5.

**I. What D7 costs Candour, modelled rather than asserted: the cumulative-test limb costs nothing, and the notice limb costs about £2,700 per price rise at 90 days, or £5,400 at 180.** The cumulative limb costs nothing because the lever it removes — holding old customers on an old price — is one Apple already denies us: *"You don't have the option to preserve the higher price for existing subscribers."* The notice limb is a timing cost on a price trajectory that points downward. **I recommend Haunt publish 180 days, not 90**, on the CGO's own test, and §10 prices it. §9, §10.

**J. Haunt is not unviable at a compliant price. It is unviable at 99p on any reach this company has evidence for, and the gap is now 6.5×.** The subscription needs **62,197 distinct subscribers — 1,728 a month, every month, for three years**. The pay-once tier needs **9,503 buyers — 264 a month**. At the volumes anyone has evidence for, the honest monthly price is **£2.03 at 4,000 subscribers and £3.55 at 2,000**, both of which are ordinary consumer app prices and neither of which is 99p. §14.

**K. My recommendation is one answer, not a menu: lead with pay-once at £28.99, keep yearly at £9.89, keep monthly at 99p as the try-it tier, and cut the quarterly tier.** Reason: the binding constraint is reach, pay-once is the only tier that does not lose to it, and cutting quarterly removes a rung that costs store configuration, a column and a set of DMCCA renewal-notice cases while changing the compliant band by nothing at all. §15.

**L. The Article 9 shared-fee question is closed with a proposed rule, and it is no longer trivial.** In v2 the shared company fees were £125.91, or 0.42% of the cost base, and I called it *"a governance fix, not a money fix."* With the AI workforce costed, shared fees are **£1,029.77 — 2.4% of the cost base** — and the day a second product ships, Haunt's price is reviewed down. §13.

---

## 1. What this cost sheet is, in plain words

Candour publishes what a product costs, itemised, including the founder's labour valued at a published market rate whether or not he is actually paid. Constitution 2.1: *"Every product publishes a **cost sheet**: hosting, tooling, support, third-party services, and a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

Four things follow that a reader is entitled to know before any number.

**Haunt has not been built.** Every figure below is an estimate of a cost not yet incurred, and the largest of them — 2,300.5 hours of build labour — is one seat's judgment, not a measurement. The CTO says so in his own words: *"it has never been tested against a real year of anything"* [E, `products/haunt/subscription-sizing-note.md` §9.4, read from disk 2026-09-21].

**Nobody has been paid anything.** The £75,249 of build labour below is the market value of work the founder will do himself and is not currently drawing. It appears as a cost because the Constitution's Definitions require it: *"labour valued at a published market benchmark whether or not it is actually paid."* If Haunt never covers that number, the gap will be published, not hidden.

**Haunt has no server, so it has no per-user infrastructure cost.** Hosting is £0.00 and that is structural, not disciplinary. The journal lives on the customer's own device. Roughly **97% of the cost of Haunt is one person's time**, and most of the rest is the cost of the AI seats that help him.

**And the price depends almost entirely on how many people buy it.** Because nearly all the cost is fixed, the same product at the same quality costs £6.60 a month to serve at 1,000 subscribers and 99p at 12,692. Candour does not get to choose which of those is true, and neither does the customer. This sheet shows the whole curve rather than one point on it.

---

## 2. The three years, and what it is not

**Constitution v1.3 requires this section and requires it to be on the face of the sheet.** Article 4: *"A product's standard amortisation period (Definitions) is an accounting convention, is never published as or in place of a support date, and the cost sheet carrying it says so on its face."* Article 2.1 requires *"a statement that the period is a company-wide accounting convention and not a statement about how long the product will be supported."*

> ### The three years this sheet spreads Haunt's build cost over is an accounting convention used by every Candour product. It is not a statement about how long Haunt will be supported, maintained or available, and no commitment of any kind attaches to it.
>
> ### **Haunt commits to no support date.** Candour has decided to say that plainly rather than name a date it might not be able to keep. That decision is recorded at **D4**, in the CEO's own words: *"what if something happens if I am unable to support a product until the date… if I don't have the time or money?"*
>
> ### What you are owed if Haunt ends does not depend on this number. It is fixed by Constitution 7.2: **at least 90 days' notice, full data export free throughout the notice period and for 90 days after shutdown, the code open-sourced where third-party rights allow, and a published closing cost sheet** stating the build capitalised, the amount recovered from customers, and the remainder written off.

**Why the convention is three years rather than a number chosen for Haunt.** Because a period chosen per product is a period chosen to suit that product's price. The full reasoning, including its weaknesses, is published in `CHANGELOG.md` v1.3 item 2 rather than kept in a working paper — including the sentence that matters most: *"three years is a judgment inside a bracket the retrieved evidence does not close."* It is reviewed once, against measured evidence, at the first product's launch plus twelve months, and any change is **prospective only** and can never re-price a customer who has already bought.

---

## 3. Itemised cost

### 3.1 The labour benchmark

| | |
|---|---|
| **Benchmark** | **£32.71 per hour worked** |
| Source | ONS *Annual Survey of Hours and Earnings*, Table 14.7a, SOC 2020 code **2134** (*Programmers and software development professionals*), full-time, UK, 2025 provisional: median gross annual pay **£56,914** |
| Evidence status | [E, [ONS ASHE Table 14](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupation4digitsoc2010ashetable14), **retrieved at primary 2026-09-18**, release date 2025-10-22]. **Carried forward from `pricing-ladder-model.md` §1 and not re-retrieved by me this session** — the figure lives inside a spreadsheet this tooling cannot open, which is the same limit the Skeptic hit at gate objection O6. It is a retrieval from the publisher, recorded in this repository, not a recollection. Gate Condition 5 is discharged and stays discharged |
| Derivation | £56,914 ÷ 1,740 hours actually worked = £32.71 |
| Why hours worked, not paid hours | Constitution 2.2 names the benchmark as *"the median UK software developer salary, **adjusted for hours actually worked**"*. ONS also publishes a median gross **hourly** figure of £29.58, which divides by *paid* hours including statutory leave. The Constitution's wording selects the derived figure, and the difference is recorded here so a reader can see it was noticed and disposed of |
| Precision | ONS coefficient of variation on this median is **2.7%**, inside ONS's own *"CV <= 5%… Estimates are considered precise"* band |

**Every labour figure in this sheet scales linearly with £32.71.** It is single-source by nature — there is one ONS — and that is flagged rather than hidden.

**One benchmark question this sheet does not resolve, and names.** §4.4 adds a line of non-engineering labour — requirements, compliance, design, finance. **A software-developer median is the wrong benchmark for that work**, and using it is a convenience rather than a finding. It is used because it is the only benchmark Candour has published, and because Article 2.2 names one benchmark rather than a schedule of them. **Flagged to the CGO** as a question the second product will force: whether Article 2.2's single benchmark survives a company that does more than one kind of work. [J]

### 3.2 One-off build labour (capital)

**Constitution, Definitions:** *"**One-off build labour is capital, amortised straight-line over the standard amortisation period**, rather than charged wholly to its first year; maintenance and support are operating costs. Labour spent on work that does not ship is not capital: it is an operating cost in the year it is incurred, and where a product is abandoned before release the whole of its build labour is written off publicly in that year."*

| Item | Low | **Point** | High | Source |
|---|---|---|---|---|
| Two-platform build (iOS + Android, React Native) | 1,770 h | **2,090 h** | 2,410 h | CTO, `subscription-sizing-note.md` §10.2 [J] |
| Android capture-reliability spike (CTO Block 2) | 75 h | **75 h** | 75 h | CTO, §10.2 [J] |
| Venue-index remediation spike (CTO Block 4) | 113 h | **113 h** | 113 h | CTO, §10.2 [J] |
| **Block 4 ruling — R-5 visit reattachment and merge-undo** *(new since v2)* | 15 h | **22.5 h** | 30 h | CTO, `block-4-ruling.md` §7 — *"2–4 days on top"* [J] |
| **Total engineering hours** | **1,973 h** | **2,300.5 h** | **2,628 h** | |
| **At £32.71** | **£64,536.83** | **£75,249.35** | **£85,961.88** | |
| Google Play one-off registration | £18.70 | **£18.70** | £18.70 | US$25 ÷ 1.33705 [E, [Google Play Console registration](https://support.google.com/googleplay/android-developer/answer/6112435), retrieved 2026-09-21 — *"There is a US$25 one-time registration fee"*; FX below] |
| **Capitalised total** | **£64,555.53** | **£75,268.05** | **£85,980.58** | |

**Unit, stated because an unstated one caused a 33–58% discrepancy in this pack once already:** one focused solo week = **37.5 hours**. 2,300.5 hours is **61.3 focused solo weeks**. For a part-time operator that is multiple calendar years, and the CTO has recorded that as a concern in writing. The calendar is the PM/BA's (`requirements.md` PLAT-4); the hours are mine.

**The spikes are inside the capitalised figure, and the treatment is stated rather than assumed.** The CTO asks that they be carried outside, because either may return *"don't build"*. His reason is sound, and the Definitions now settle it for him: *"Labour spent on work that does not ship is not capital: it is an operating cost in the year it is incurred."* **So if a spike returns "don't", its hours leave this table and are expensed in the year they are incurred; if it returns "do", they shipped and they are capital.** The range row lets a reader take either treatment.

**One item the Block 4 ruling removes, recorded so a reader can see it was netted rather than ignored.** The CTO cancelled a budgeted R\*Tree spike — *"One day recovered"* [E, `block-4-ruling.md` §7, read from disk 2026-09-21]. That day was carried as an open question, not inside the 2,090-hour total, so **it does not reduce the figure above**. Recording a saving that does not exist would be the mirror of hiding a cost that does.

### 3.3 The amortisation schedule — required by Article 2.1 as amended

**The clause, quoted:** *"Where build labour is capitalised, the cost sheet publishes an **amortisation schedule** — one line per capitalised increment, with its hours, ship date, period, amount amortised to date and remaining balance — together with capitalised hours as a share of all hours worked on the product that year, and a statement that the period is a company-wide accounting convention and not a statement about how long the product will be supported."*

| Increment | Hours | Ship date | Period | Amortised to date | Remaining balance |
|---|---|---|---|---|---|
| **Haunt v1 — the whole MVP build** | **2,300.5 h** (£75,249.35) plus £18.70 Google Play registration | **Not yet set.** The clock starts on **the earlier of Haunt's first sale and its public release**, and is published on the first cost sheet issued after that date and never restated | **36 months** | **£0.00** | **£75,268.05** |

**Why there is one line and not several.** The Definitions provide that *"each capitalised increment runs its own clock from the date it ships, so a later increment never extends, restarts or re-bases an earlier one."* Haunt has shipped nothing, so the whole MVP build is a single increment that will ship on one date. **Every post-launch increment gets its own line here, with its own ship date and its own 36 months, and this table is how a reader checks that a "v2" is a real shipped change rather than a fresh layer opened to offset an expiry** — which is a vector Article 9 now names by that description.

**Date of the first pound of revenue:** none yet. It is published beside the start date at the first republication after launch, because Article 9 requires it: *"The start date is the earlier of first sale and public release, published on the first cost sheet and never restated, **with the date of the first pound of revenue published beside it**."*

#### Capitalised hours as a share of all hours worked — **this sheet cannot publish it, and here is why**

| | |
|---|---|
| Capitalised hours (numerator) | **2,300.5** — engineering only |
| All hours worked on Haunt this year (denominator) | **Not recorded. The figure does not exist.** |
| Ratio | **Cannot be computed** |

**What is actually missing.** Haunt has consumed substantial non-engineering labour — discovery, a gate, a dissent memo, three venue-index spike notes, two compliance notes, two UX notes, an architecture note, a sizing note, a 139-requirement specification, a Block 4 ruling, and three cost sheets including this one. **None of it has ever been recorded in hours, and none of it appears in any cost figure Candour has published.** §4.4 sizes the consequence.

**Why printing a ratio anyway would be worse than printing this.** With the denominator set equal to the numerator the ratio reads **100%**, which would be a false statement dressed as a disclosure, and Article 9's stated purpose for this very number is the opposite: it is the number that exposes *"inflating capitalised build hours, or capitalising work that is really maintenance"*, and it works because it *"trends to zero in steady state."* A ratio computed from a denominator nobody measured exposes nothing.

> **Remedy, with an owner and a date: hours worked on Haunt are recorded from the first day of build, by category, and the ratio is published at the first annual republication. Owner: CEO, as the person doing the hours. Cost: a text file.** Until then this row stays as it is written above, and a reader can see the gap rather than having to find it.

### 3.4 Fixed annual operating cost

Independent of how many customers there are.

| Item | Low | **Point** | High | Basis |
|---|---|---|---|---|
| Maintenance labour — OS releases, Expo/React Native upgrades, venue-index reconciliation, OEM regressions, subscription and store mechanics, regulatory upkeep, accessibility re-verification | 288 h | **360 h** | 441 h | CTO §9.2 [J] |
| **Security patching and non-OS defect fixes** *(new since v2 — see §5)* | 30 h | **45 h** | 90 h | **[J], CFO provisional.** The CTO's nine maintenance rows contain no row for it. The hours are owed regardless of any promise (C5.4). **The CTO owns the real figure** |
| Support floor — inbox, store and policy churn, reproducing reports, entitlement and restore cases | 100 h | **115 h** | 130 h | CTO §9.5 [J] |
| **Fixed labour** | **418 h** | **520 h** | **661 h** | |
| **At £32.71** | **£13,672.78** | **£17,009.20** | **£21,621.31** | |
| **AI tooling — the agent seats** *(new since v2)* | £149.58 | **£897.50** | see note | **Claude Max, from US$100/month = US$1,200/yr ÷ 1.33705.** Floor is Claude Pro billed annually, US$200/yr [E, [Claude pricing](https://claude.com/pricing), retrieved 2026-09-21: *"Pro — Monthly: $20; Annual: $17/month (billed $200 upfront)"*; *"Max — From $100/month"*]. §3.4.1 |
| Apple Developer Program | £74.04 | **£74.04** | £74.04 | US$99/yr ÷ 1.33705 [E, [developer.apple.com/programs](https://developer.apple.com/programs/), retrieved 2026-09-21] |
| ICO data protection fee, Tier 1 | £52.00 | **£52.00** | £52.00 | [E, [ico.org.uk data protection fee](https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/), retrieved 2026-09-21: Tier 1 **£52**, criteria *"maximum turnover of £632,000 for your financial year or no more than 10 members of staff"*, with a **£5 direct-debit discount**. **£52 carried as the prudent figure**] |
| Domain and static support page | £10.00 | **£10.00** | £10.00 | [J] — .com renewal not retrieved; 0.02% of the base |
| Hosting | **£0.00** | **£0.00** | **£0.00** | No server |
| Database | **£0.00** | **£0.00** | **£0.00** | All state on the customer's device |
| Venue / places API | **£0.00** | **£0.00** | **£0.00** | Bundled offline dataset. No metered API, no per-read cost, no heavy-user penalty |
| Crash and analytics tooling | **£0.00** | **£0.00** | **£0.00** | Deliberately absent (Article 4 data minimisation). The cost reappears above as support labour, because a product that collects no diagnostics is harder to support |
| Build infrastructure (Expo EAS) | **£0.00** | **£0.00** | **£0.00** | Free tier sufficient [E, CTO, retrieved 2026-09-16]. Named trigger: Starter at US$19/month ≈ £171/yr if monthly builds exceed 15 per platform |
| **Total fixed annual** | **£14,706.32** | **£18,042.74** | **£22,654.85** | |

**FX:** GBP/USD **1.33705**, 21 September 2026 [E, [Trading Economics, United Kingdom currency](https://tradingeconomics.com/united-kingdom/currency), retrieved 2026-09-21]. Every dollar figure in this sheet uses that one rate and says so. **A rate is a snapshot; it is republished annually with the sheet, and the dollar amounts are what Candour is actually charged.**

#### 3.4.1 The AI workforce is a cost, and it has never appeared on a Candour cost sheet

**This is a new line and it should not have been new.** Constitution Article 10 discloses that *"Candour is operated by its founder together with **AI agents** holding the seats in Article 6, working under written charters. We disclose this because transparency includes how we work."* Article 2.1 requires the cost sheet to itemise *"hosting, **tooling**, support, third-party services"*, and the Definitions require *"everything it takes to run a product or the company, itemised."*

**Eleven agent seats produced every artifact behind this product, and both of my previous cost sheets recorded tooling at £0.00.** That was wrong. It is corrected here rather than at the second product, when somebody's price would depend on the answer.

**How it is carried, and the honesty of the number.** The line is the cost of the subscription that runs the seats. **I do not know which plan Candour is on and I have not assumed one from the inside of a session** — the CEO owns that fact. The point estimate is set at the **top** of the plausible range (Max, from US$100/month), because a cost sheet should err against the product rather than for it, and the low row shows the floor (Pro billed annually). **The retrieved page states Max as *"From $100/month"* with a higher usage tier whose price it does not print; that figure is unretrieved and the high column is therefore open above £897.50, which is flagged rather than guessed.**

**It is a shared company cost, not a Haunt cost**, and §13 proposes the rule that governs it. Today Haunt carries 100% of it because Haunt is the only product there is, and this sheet says so on its face.

### 3.5 Variable cost, per subscriber per year

The only cost that scales with customers, and on a product with no server it is entirely support labour. **Unchanged from v2; the basis is restated so this sheet is self-contained.**

| Component | Hours/subscriber/yr | At £32.71 | Basis |
|---|---|---|---|
| iOS subscriber — 5% annual contact rate × 45 min | 0.0375 | £1.2266 | CFO original, accepted by CTO |
| Android subscriber — 12% × 60 min | 0.1200 | £3.9252 | CTO amendment [J] |
| **Blended at 60% iOS / 40% Android** | **0.0705** | **£2.3060** | Platform mix is **[J]** — no evidence exists; §16.2 |
| **Subscription billing uplift** | per billing event | **£0.1090/event** | [J] — 1% of billing events generate a 20-minute contact |

| Tier | Billing events per year | **Variable cost per subscriber-year** |
|---|---|---|
| Monthly | 12 | **£3.6140** |
| Quarterly | 4 | **£2.7420** |
| Yearly | 1 | **£2.4150** |
| Pay once | 0 after purchase | **£2.3060** |

**Why this parameter matters more than its size suggests.** It is the whole of the cost anchor under the ladder's discounts. **If it is zero, the pay-once tier returns to being a longer subscription at the same price, there is no saving to claim, and UX's block B11 bites again.** I have not moved it since I published it on 2026-09-18, before it mattered to the band, and the sensitivity is at §16.2. **A lapsed, read-only user costs £0.6150/year** on the same basis, and Condition 9.7 makes every lapsed subscriber one of these permanently.

### 3.6 The whole cost base

| | Low | **Point** | High |
|---|---|---|---|
| Capitalised build, amortised over **three years** | £21,518.51/yr | **£25,089.35/yr** | £28,660.19/yr |
| Fixed annual operating cost | £14,706.32/yr | **£18,042.74/yr** | £22,654.85/yr |
| **Annual fixed cost `A`** | **£36,224.83** | **£43,132.09** | **£51,315.04** |
| **Total published cost over three years** | **£108,674.49** | **£129,396.27** | **£153,945.12** |
| Plus, per subscriber per year | £2.31 – £3.61 depending on tier | | |

**Against v2's three-year column (£40,517.17): ×1.0645.** The whole of the increase is the three items v2 did not carry — the Block 4 ruling's hours, the security line, and the AI workforce. **Nothing in the CTO's own estimate has moved.**

### 3.7 What is deliberately not in this sheet

- **The proportionate-refund duty under the DMCCA.** Not a build item and no build creates one: Candour has no refund mechanism and refunds are adjudicated and paid by the stores. **It is launch bar L1 — qualified human legal review under Constitution 6.1** — not a line item, and if that review concludes the duty falls on Candour the options are commercial or structural, not technical.
- **Marketing and acquisition spend.** There is none, and it remains the most consequential absence in this document. §14.
- **Any cost of a permanent free tier.** Condition 9.7 removed the read-cap; a lapsed user retains a free manual journal, whose support cost is carried at §3.5.
- **A support-commitment cost.** There is no support commitment (D4), so there is nothing to cost. **The maintenance hours in §3.4 are not smaller for that reason** — see §5.

---

## 4. Does the settled scope exceed what I last costed? — **yes, in four ways**

The PM/BA's `requirements.md` (2026-09-21) settles the scope at **13 requirement areas and 139 numbered requirements**, and the CTO's `block-4-ruling.md` (2026-09-21) rules on Block 4 and adds work. I was asked to re-derive on the CTO's figures and say plainly whether the settled scope exceeds what v2 costed. **It does. Three of the four gaps are small and named; the fourth is large and is mine.**

### 4.1 The Block 4 ruling — sized by the CTO, carried in full

The ruling adds **R-5: visit reattachment and merge-undo**, sized by the CTO at *"2–4 days on top"* and explicitly flagged rather than absorbed [E, `block-4-ruling.md` §7]. It is in §3.2 at **15–30 h, point 22.5 h (£736.00)**.

**It is not optional, and the ruling says why:** *"If merge, rename, reattachment or merge-undo leaves MVP scope, §4.4's answer to the CVO's reservation fails with it… That would re-engage the block on limb (b)."* **So this is 22.5 hours that buys the lifting of a build block. It is the cheapest money in this document.**

### 4.2 Five requirements from the PM/BA that no CTO row prices

Each is marked in `requirements.md` as new from that seat, or as joining two duties nobody had joined. **I am not sizing another seat's work, and I am not absorbing it into a range and calling it covered.** They are listed so the CTO can price them and so a reader can see they are outstanding.

| # | What it is | Priority in `requirements.md` |
|---|---|---|
| **VEN-13** | The refresh review surface is not a notification and not a queue that accumulates pressure — no count, no badge, no prompt, over a pile that VEN-9 is designed to create | **BLOCKING** |
| **VEN-16** | The product offers merge where it can see a probable duplicate — a name-token similarity pass over the user's *own* venues, statically and without urgency | MUST |
| **VPAGE-6** | Aggregates honest about small numbers — no unqualified "5.0" from one visit | MUST |
| **VPAGE-7** | A static line telling the user what a venue page becomes over a year | MUST |
| **NOT-6** | The price-rise notice mechanism and the DMCCA notices surface are one implementation, not two | MUST |

**My judgment on the size, offered as judgment and not as a figure to build a price on [J]:** four of the five are small; **VEN-16 is not**, because a duplicate-detection pass over the user's own venues is a ranking problem of the same family as the one that produced Block 4. **Owner: CTO, in a single sizing pass, before requirements sign-off.** §4.5 prices the whole set as a sensitivity so the decision is not held up by it.

**One further item I could not place.** **VEN-17** makes the venue-index harness a permanent committed regression fixture with a CI reproducibility sweep — the CTO's own standing item **S1**. It may sit inside the 150–225 h venue-remediation build row or it may not; the row's description names *"refresh reconciliation tooling"* and not a CI fixture. **Asked of the CTO rather than assumed either way.**

**And the requirements document is not finished, which is itself a cost signal, not a criticism.** It reserves **CAP-11…14** for the Block 2 Android spike, **ENT-15…17** for the trial mechanism pending an unanswered Apple guideline 3.1.1 question, and **VEN-20 onward** for the Block 4 ruling. **Three reserved ranges are three sets of requirements that will arrive after this price was computed.** On this product's history — a build estimate that has gone 450 → 1,330 → 2,090 → 2,300.5 hours in four weeks, always in one direction — a reader should weight that.

### 4.3 The Block 4 ruling's second cost item, which is a warning rather than a number

The ruling records that reconciliation *"is **not** priced in the 0.5 day/month the feasibility note carries"* and assigns it to the CFO. **It is priced here and it was priced in v2**: the CTO's revised maintenance table carries venue-index reconciliation at **60–100 h/yr**, replacing the old 45 h/yr refresh row, and that revision is the single largest line in the 288–441 h/yr total. **Discharged, and recorded as discharged so it is not re-raised a third time.**

### 4.4 The fourth gap: **no Haunt cost sheet has ever costed the non-engineering labour**

**The Definitions are not ambiguous about this.** *"**Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and **labour valued at a published market benchmark whether or not it is actually paid**."* Article 2.1 repeats it: *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."* **Neither says "engineering labour".**

**The 2,090 hours are the CTO's estimate of building the thing.** Behind them sit a research brief, an idea brief, a proposal, a gate pack, two dissent memos, a decision record with ten conditions and six corrections, a compliance note, a subscription compliance note, two UX notes, an architecture note, a sizing note, three venue-index spike notes, a Block 4 ruling, a 139-requirement specification, an amortisation proposal, and three cost sheets. **Not one hour of it is in any published Candour number.**

**Why it is a real cost and not an accounting curiosity.** It is labour on work that ships — the requirements document is the thing the build is built from — so under the Definitions it is **capital**, amortised over the same three years, exactly like the engineering. And Article 9's newest concern is the *ratio* of capitalised hours to all hours worked, which cannot be computed while one of the two categories is invisible (§3.3).

**Why I am not putting a number in the table.** Because I would be inventing it. Nobody recorded the hours; the work was done partly by agent seats and partly by the founder reviewing them; and the honest split between the two is not something I can derive from the inside. **What I can do is show what it costs to be wrong about, which is §4.5.**

> **Finding, stated at the strength the evidence supports: every Haunt price Candour has ever modelled, including the ones in this sheet, understates the cost base by the whole of its non-engineering labour. The direction of the error runs against Candour, not against the customer** — an understated cost produces a lower published price and a published margin higher than the true one. **That does not make it acceptable. It makes it the kind of error nobody has an incentive to find, which is exactly the kind Article 9 exists to publish.**

### 4.5 What the unsized work costs, priced as a range so the decision is not held up

Every row is the point cost base of §3.6 with additional **capitalised** hours added. `N*` is the subscriber count at which 99p a month is exactly the honest price.

| Additional capitalised hours | Capital | **Annual cost base `A`** | **`N*` at 99p** | Move |
|---|---|---|---|---|
| **+0** (this sheet's published figure) | £75,268.05 | **£43,132.09** | **12,692** | — |
| +75 h (the five PM/BA requirements, if small) | £77,721.30 | £43,949.84 | 12,932 | +1.9% |
| +150 h | £80,174.55 | £44,767.59 | 13,173 | +3.8% |
| **+300 h** (non-engineering labour, central [J]) | £85,081.05 | £46,403.09 | **13,654** | **+7.6%** |
| +450 h | £89,987.55 | £48,038.59 | 14,135 | +11.4% |

> **The honest summary: the scope has grown since v2, and I have carried everything anyone has sized. What remains uncarried moves the volume the price needs by somewhere between 2% and 11%. That is material and it is not fatal, and it is knowable for the price of a text file.**

---

## 5. D2's missing hours — do they survive the supersession? **Yes, and they are now carried**

**What I found in v2 §4.1, and it stands.** D2 promised *"security and defect fixes are made"*. The CTO's nine maintenance rows contain OS-compatibility work, venue-index reconciliation, Expo upgrades, OEM regression chasing, subscription upkeep, regulatory upkeep and accessibility re-verification. **There is no row for security patching, and no row for defect fixes that are not OS- or OEM-driven.** The nearest candidates do not cover it: OEM regression chasing is Android-device-specific, source-map retention is diagnosis rather than repair, and the support floor's triage is not fixing.

**What has changed.** D2 is superseded by D4. There is no five-year support commitment and no support date at all. **So the contractual exposure is gone: there is no sentence in a customer's contract, under CRA 2015 s.36(3), promising that security fixes are made.**

**What has not changed, and it is the whole answer to the question.** The decision record already settled it, at Correction **C5.4** on Condition 9.8(b): *"The CTO must still size the subscription increment and **the missing security/defect-fix maintenance row — now purely a cost question, no longer also a promise question, and the hours are owed whether or not anything was promised.**"*

> ### The work survives. The promise was never what created the work; a dependency-CVE surface created the work, and it does not care what Candour published.

**Three reasons, in order of weight.**

1. **The hazard is unchanged.** A React Native application with four local native modules and two SDK majors a year has a real dependency-CVE surface. Withdrawing a sentence from a pricing page does not patch a transitive dependency.
2. **Not fixing defects is not a lawful alternative either.** CRA 2015's digital-content provisions require content to be of satisfactory quality, fit for purpose and as described, and they do not depend on a support date being published. **Article 4 is independently engaged**: *"claims we cannot substantiate are claims we do not make."* If Haunt's store copy says the venue index is maintained and the capture engine works, the work behind those claims is owed.
3. **The costing error was always separate from the promise.** A cost sheet that omits real recurring hours understates the honest price whether or not a customer was ever told about them. **That is the error, and it is corrected here.**

**How it is carried.** §3.4 now contains a line — **30 / 45 / 90 h a year, point £1,471.95** — labelled as a **CFO provisional** and not as a CTO figure, because sizing it is the CTO's job and not mine. **I have moved it from a flag to a number because a line flagged twice and carried at zero a third time is the mechanism by which a known gap becomes furniture**, which `pipeline/evidence-standard.md` names in terms: *"Twice-flagged is escalated."* This is the third artifact. It is escalated by being priced.

| Security / defect-fix line | Annual cost base `A` | 99p covers its cost at | 99p is honest at |
|---|---|---|---|
| +0 h/yr (the CTO's table as it stands) | £41,660.14 | 8,677 | 12,258 |
| +30 h/yr | £42,641.44 | 8,882 | 12,547 |
| **+45 h/yr (carried in this sheet)** | **£43,132.09** | **8,984** | **12,692** |
| +60 h/yr | £43,622.74 | 9,086 | 12,836 |
| +90 h/yr | £44,604.04 | 9,291 | 13,125 |

> **The line costs between 0% and 7% on the volume the price needs. It changes no recommendation in this sheet. It is carried anyway, because the alternative is publishing a cost sheet that everyone involved knows is missing a row.**

**What would resolve it properly:** the CTO adding a named security-and-defect row at whatever size he judges, replacing my provisional. **Owner: CTO. Until then the published figure is mine and is labelled as mine.**

---

## 6. How a price is computed from these costs

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

### 6.1 The deviations, recorded as Article 2.1 requires — and there are two, not one

> **Deviation 1 — structural, −3.50 percentage points.**
> **Margin: 16.50% over total published cost including store commission. Deviation from the ~20% target: YES, 3.50 pp below.**
> **Justification, in writing as Article 2.1 requires:** Candour takes no margin on the 15% that Apple and Google charge. Taking 20% on the platform's fee as well would yield exactly 20.0% and a shelf price about 4% higher. **The customer is charged nothing for the service of collecting the platform's fee, and this deviation is the price of that choice.** The alternative treatment is arithmetically available and is not being taken.
> **Direction: against Candour, in the customer's favour.** Recorded as a deviation anyway, because Article 9 names *"Quietly weakening the rules"* as a gaming vector and the direction is not a defence.

> **Deviation 2 — the one that actually describes Haunt, and v2 buried it in a table.**
> **At the subscriber counts this company has evidence for, every price in this sheet runs a deviation of between 19 and 63 percentage points *below* target, and at the low end it does not recover the founder's benchmarked labour at all.**
>
> | Subscribers | 2,000 | 3,000 | 4,000 | 6,000 | **8,984** | 10,000 | **12,692** |
> |---|---|---|---|---|---|---|---|
> | **Realised margin at 99p/month** | **−62.9%** | **−49.2%** | **−37.7%** | **−19.4%** | **0.0%** | +5.2% | **+16.5%** |
>
> **Justification, in writing:** the CEO decided at the gate to proceed on a stated non-commercial basis — *"I quite like this idea for myself personally and if I can release it and it makes a bit of money then I am happy with that"* — *"accepting that it may not cover its own benchmarked labour."* Article 2.1 permits a deviation with written justification and this is it. **Under Constitution 5.4 the decision is the CEO's; under Article 2.1 the number is published either way.**
>
> **Why this is stated as a headline rather than as a footnote.** A cost sheet that reports "16.50%, a 3.50 pp deviation" and leaves the reader to discover that 16.50% only obtains at 12,692 subscribers is doing the thing Article 9's first row names. **The honest sentence is: at any volume Haunt is likely to reach, Candour is selling below its own published cost, on purpose, and publishing the gap.**

**A third deviation is created by rounding** to the stores' available price points, and it is recorded per tier at §7.2.

### 6.2 What the price is *not* a function of

**There is no hosting cost, so there is no volume discount hiding anywhere.** Haunt's cost is one person's time plus the tools that help him. That has an uncomfortable consequence a customer should see stated rather than discover: **the price depends almost entirely on how many people buy it.**

| Subscribers | 1,000 | 2,000 | 3,000 | 4,000 | 6,000 | 8,000 | 10,000 | **12,692** |
|---|---|---|---|---|---|---|---|---|
| **Honest monthly price** | £6.60 | £3.55 | £2.54 | £2.03 | £1.52 | £1.27 | £1.12 | **£0.99** |


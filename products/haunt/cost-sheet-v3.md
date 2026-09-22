# Cost sheet — Haunt — v3 (pre-requirements, publishable)

**Seat:** Chief Financial Officer · **Date:** 2026-09-21 (§§0–6.2) · **completed 2026-09-22** (§§6.2 close–19, and three marked insertions: this line, the §0 addendum and §4.6)
**Name:** the product is **Haunts** (CEO decision **D9**, 2026-09-21), a working name until the three checks at `requirements.md` PLAT-6 pass. §§0–6.2 were drafted before D9 reached this seat and say "Haunt"; they are left as written rather than silently edited. **The customer-facing copy at §12 uses "Haunts".** The slug and file paths stay `haunt`.
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

### Addendum to §0 — written 2026-09-22 with §§7–19, because finishing the arithmetic sharpened four of the answers above

*Inserted, not substituted. Nothing above is withdrawn; where an answer is sharpened, the sharpening is here and in §18.*

**M. The scope has now grown a fifth way (§4.6).** Since §4 counted 139 requirements, `requirements.md` has reached **163**. Sixteen of the new ones — companions, competitor import, the inference screen, the heatmap, the recap and its image, three onboarding items and seven photo items — **are sized by no seat.** On my judgment, for sensitivity only, they move the volume 99p needs by roughly **6–8%**; with everything else still unsized, by about **17%**. **Photos-as-references change no cost line**: storage, backup and hosting stay at £0.00 because Candour holds none of them.

**N. The 30.3% cut (answer E) comes from Candour's own pricing rule. The Constitution on its own requires less (§8.3).** Article 2.1's 30% cap would force a cut only to **79p (20.2%)** at the same volume. Getting to **69p** depends on the CEO adopting the rule I recommend: **work out every price again at each yearly review, and cut it whenever the rule gives a lower figure.** The customer copy at §12 is written on that rule.

**O. The pay-once price should step down each year as the build is paid off (§11.2).** At the reference volume that means **£28.99 → £25.49 → £22.49 → £18.95**. A buyer in year three would otherwise pay for 24 months of build cost that has already left the cost base. That would also push the product's year-four margin toward the cap, if most customers pay once and then stop using the app (§11.3).

**P. The copy for PRICE-7, PRICE-8 and PRICE-9 is at §12.** It contains no support date, labels the only date as an accounting date in the same sentence, and says the cut depends on subscriber numbers. **One conflict in `requirements.md` needs resolving:** PRICE-1 asks for a per-month figure for every tier. For pay-once that figure only exists if you assume a period, and PRICE-13 forbids implying one. §12.4.

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

### 4.6 A fifth gap, found on 2026-09-22: the scope grew again after this section was drafted *(inserted)*

**What moved.** §4 was written against `requirements.md` at **139 requirements**. The copy on disk on 2026-09-22 carries **163**. I counted numbered rows in the requirement tables and excluded the Block 4 ruling's R-number map (R-1 to R-8) and the standing conditions S-1 to S-3, which are not requirements. That document's own change log still says 139. **The file changed while this sheet was being written**: line numbers moved between two reads in this session. So **163 is a snapshot**, and the PM/BA owns the real count. [E, `products/haunt/requirements.md`, read from disk 2026-09-22.]

| New since §4 | Count | Sized by anyone? | Carried in this sheet? |
|---|---|---|---|
| **VEN-20 … VEN-24** — the Block 4 ruling's criteria | 5 | The ruling sizes **R-5 only**, at *"2–4 days on top"*. I read it as placing the rest inside the CTO's existing rows | **Yes.** R-5 is in §3.2 at 22.5 h; the rest is carried on the CTO's word |
| **PRICE-13, PRICE-14** — the enumerated pricing-string check in CI and the accounting-date qualifier | 2 | No | No. Small [J] |
| **PLAT-6** — name checks before "Haunts" is used in public | 1 | No | No. An App Store search and a UK IPO search. The CGO owns the trademark search. **A domain is already in §3.4 at £10** |
| **CONF-19** — companions, free text, suggestions drawn only from the user's own history | 1 | No | **No** |
| **DATA-15** — import from a competitor's export | 1 | No | **No** |
| **LOOK-1 … LOOK-4** — the inference screen, heatmap, recap, and recap-to-image | 4 | No | **No** |
| **ONB-1 … ONB-3** — onboarding rules, seeding, "find your local" | 3 | ONB-3 at **2–4 days** by the PM/BA [J]. **Not a CTO figure** | **No** |
| **PHOTO-1 … PHOTO-7** — photos held as references to the user's library | 7 | No | **No** |
| **Total** | **24** | | |

**Photos, the question I was asked directly. No cost line in §3 changes.** PHOTO-1 stores *"the platform's stable local library reference, as text"*, and the app *"never copies image bytes into its own container"*. That leaves hosting, database and storage at £0.00. They were £0.00 already, because Candour holds none of the journal; the photos stay in the customer's own library. The backup ends up in one of two places, and the requirements have not yet chosen between them (`requirements.md` §12.1): an encrypted file the user saves, or the user's own cloud account. **Neither is Candour's storage, so there is no Candour line for backup to grow.** **What photos do change is labour, in two places:**

- **Build**: library-reference APIs on two platforms, an export that resolves references and streams a multi-gigabyte archive, and handling of broken references. The PM/BA asked the CTO for *"the marginal build hours"* at §12.2.5. **They have not been given.**
- **Support**: three new kinds of contact that did not exist before — *"my photos didn't come back"* after a restore (PHOTO-4 names this trap), broken references (PHOTO-7), and large exports (PHOTO-6). **I have not moved the variable support rate in §3.5 for them** [J]. The rate is unmeasured anyway (§16.2), and moving a guess by a guess adds noise, not information. This is recorded so that nobody later assumes photos were costed at zero on purpose.

**Two items carry a recurring cost as well as a one-off one, and that is what matters most here.**

1. **DATA-15, competitor import.** It parses a file format Candour does not control. **When a third party changes its export format, Candour's parser breaks and someone has to fix it, whether or not anyone promised.** That is maintenance, not build — the same reasoning as §5. [J] **10–20 h/yr** until the CTO names a figure. It is also a new untrusted-input surface, which the PM/BA has already routed to the CSO.
2. **LOOK-2, the heatmap, depends on a map, and I can find no cost for any map in this repository.** A11Y-3 requires contrast over *"map tiles"*. The compliance note lists MapKit as an *"architectural tripwire"*. **I found no artifact that names where the tiles come from.** If they are fetched over a network, the product's "no outbound traffic" claim changes. If the provider meters them, that is the **first per-user variable cost this product would have outside support labour.** Requirements §20.2 lists *"the map entirely"* as the largest cut available. **Flagged to the CTO (§17.3). I am not asserting any provider's price, because I retrieved none.**

**Priced as sensitivity, on my judgment [J], so the decision is not held up waiting for it:**

| Scenario | Additional capital hours | Additional h/yr | **Annual cost base `A`** | **`N*` at 99p** | Move |
|---|---|---|---|---|---|
| This sheet as published | 0 | 0 | £43,132.09 | 12,692 | — |
| The 16 unsized items, central [J] | +250 | 0 | £45,857.92 | 13,494 | +6.3% |
| … plus DATA-15 and photo upkeep | +250 | +20 | £46,512.12 | 13,686 | +7.8% |
| **Everything still unsized: §4.2's five, §4.4's non-engineering labour, and these** | **+625** | **+20** | **£50,600.87** | **14,889** | **+17.3%** |

> **Answer to "does the scope in `requirements.md` now exceed what you costed?": yes. It is larger by 24 requirements, 16 of them unsized by any seat. On my judgment that means roughly 6–8% more volume before 99p is honest, and about 17% with everything else still unsized. I cannot tighten that. Only the CTO's sizing pass can, and it should cover all 21 unsized items (§4.2's five and these sixteen) in one go, before requirements sign-off.**

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


*(Honest monthly price = `(A/N + £3.614) × 1.694118 ÷ 12`, at the point cost base. Re-derivable with a calculator from §3.6 and §6.)*

**Read the table from right to left.** 99p is the right-hand column. It is honest at 12,692 subscribers, and it is a deliberate below-cost price (Deviation 2) at every count to its left. At 4,000 subscribers the honest monthly price is **£2.03**. At 2,000 it is **£3.55**. **Candour does not choose which column is true. The market does. This sheet chooses only to show every column.**

---

## 7. The ladder on the three-year period

### 7.1 How each tier is priced — one rule, one volume

Every tier is priced by the **same rule** — `(A/N + s) × 1.694118` — at the **same subscriber count**. That is what *"discounted on the same curve as the others"* (Correction C3.0) means arithmetically. The reference count is `N*` = **12,692**, the volume at which 99p a month is exactly honest.

**A property of that reference point, stated because it explains why three of the four prices did not move from v2.** At `N*` the fixed-cost share per subscriber, `A/N*`, is always **£3.3985**, whatever `A` is, because `N*` is defined as the count at which 99p covers `A/N + £3.614` at the pricing rule. **A bigger cost base moves `N*`, not the prices at `N*`.** That is why the build growing from 2,090 to 2,300.5 hours, and the AI tooling, and the security line, changed the volume Haunt needs (12,692, up from v2's 11,922) and **changed no price**.

| Tier | `s` | Cost of service / yr | Honest price / yr | **Honest price per billing period** |
|---|---|---|---|---|
| Monthly | £3.6140 | £7.0125 | £11.880 | **£0.9900 a month** |
| Quarterly | £2.7420 | £6.1405 | £10.403 | **£2.6006 a quarter** |
| Yearly | £2.4150 | £5.8135 | £9.849 | **£9.8485 a year** |
| Pay once | £2.3060 | £5.7045 | £9.664 | **£28.9916 once** — three years of the pay-once tier's own cost of service; §11 |

### 7.2 Rounding — the third deviation, recorded per tier

**The store's price grid, retrieved at primary this session.** Apple, *App Store Pricing Update*, "United Kingdom (GBP)". **Price steps:** £0.10 from £0.29 to £9.99 · £0.50 from £0.49 to £49.99 · £1 from £0.99 to £199.99 · … **Supported conventions:** X.99 (£0.99–£11,999.99) · X.00 (£1–£10,000) · X.90 (£0.90–£99.90) · X.95 (£0.95–£49.95). [E, [apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf](https://www.apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf), downloaded and text-extracted 2026-09-22. **Single source by nature**: Apple is the only publisher of Apple's grid.]

**The rule is unchanged from `cost-sheet-v2.md` §7.2.** Charge the nearest conventional point in either direction. Where two are equally near, take the lower. Never take a point that carries the margin above 30%. Record every rounding.

| Tier | Honest | **Charged** | Displacement | Margin at `N*` | **Deviation from ~20%** | Why |
|---|---|---|---|---|---|---|
| Monthly | £0.9900 | **£0.99** | 0.00% | **16.51%** | **−3.49 pp** | Commission passed through at no markup (Deviation 1) |
| Quarterly | £2.6006 | **£2.59** | −0.41% | **16.11%** | **−3.89 pp** | Pass-through, plus rounding down |
| Yearly | £9.8485 | **£9.89** | +0.42% | **16.91%** | **−3.09 pp** | Pass-through, plus rounding up |
| Pay once | £28.9916 | **£28.99** | −0.01% | **16.50%** | **−3.50 pp** | Pass-through; revenue recognised over 36 months (§7.3) |

**What the grid cannot do, carried forward from v2 and still true.** At a 99p price point one 10p step is worth about **ten margin points**. At this price, **Apple's grid is coarser than Candour's constitution.** The quarterly and yearly tiers are the only ones that can be priced to the penny.

**Not yet confirmed, and owed before any price publishes:** (1) the exact points as App Store Connect shows them. Apple does not publish the complete list outside the tool, and the conventions above suggest points (£18.95, for example) that should be checked there. (2) **Google Play's GBP grid.** I tried again this session. [Google's help page](https://support.google.com/googleplay/android-developer/answer/10532353) says the price ranges are in tables and links out to *"play.google.com/supported-locations"*. The table did not come back through retrieval. **Two stores may not offer the same nearest point.** Owner: CFO, at store configuration.

### 7.3 Annual margin on every tier, including pay-once — as Article 9 requires

**Article 9** names *"A one-off or pay-once tier escaping the cumulative lifetime margin test"*. The number it gives to expose that is *"The **annual** margin on every tier including one-off tiers, at every republication, with one-off revenue recognised over the amortisation period rather than in the year of receipt."*

**So £28.99 is recognised as £9.66 a year for 36 months.** Recognised any other way, the margin in the year of purchase would be about +250% and would describe nothing real. With the revenue spread, the pay-once tier's annual margin at `N*` is **16.50%** in each of the three years, the same as the monthly tier.

**The recognition method, stated because a method chosen after the fact is a gaming vector: straight-line, 1/36 of the price in each month from the month of purchase.** Not matched to cost, not front-loaded, and never re-selected per year. §11.3 shows the one place where straight-line recognition creates a problem, and deals with it through price rather than by changing the method.

### 7.4 The table the plans screen must carry (PRICE-1, PRICE-4), at launch

| Tier | Charged | Per month | Per year | Saving against monthly — rounded **down** |
|---|---|---|---|---|
| Monthly | £0.99 each month | **£0.99** | £11.88 | — |
| Quarterly *(recommended for cutting, §15)* | £2.59 every 3 months | **£0.86** | £10.36 | £1.52 a year — **12.7%** |
| Yearly | £9.89 each year | **£0.82** | £9.89 | £1.99 a year — **16.7%** |
| Pay once | £28.99, once | **see §12.4** | — | **Stated as the crossover, not as a percentage — §12.4** |

*(2.59 ÷ 3 = 0.8633; 9.89 ÷ 12 = 0.8242; 11.88 − 10.36 = 1.52, and 1.52 ÷ 11.88 = 12.79%, rounded down to 12.7%; 11.88 − 9.89 = 1.99, and 1.99 ÷ 11.88 = 16.75%, rounded down to 16.7%.)*

**The pay-once discount is real, and this cost sheet can show it.** £28.99 against 36 monthly payments of 99p (£35.64) is **£6.65, or 18.6%** (18.66%, rounded down). That clears the condition UX's **B11** set: there must be a real saving before any saving is claimed. **But the plans screen should not print "18.6% over three years".** Three years is the amortisation period. A saving quoted "over three years" beside a price is exactly the implied horizon that PRICE-11 and PRICE-13 forbid. §12.4 explains what the screen says instead.

### 7.5 The compliant band

| Tier | Recovers its cost at | Reaches the 30% cap at | Width |
|---|---|---|---|
| Monthly 99p | 8,984 | 17,140 | 1.908× |
| Quarterly £2.59 | 9,384 | 16,564 | 1.765× |
| Yearly £9.89 | 9,396 | 16,043 | 1.707× |
| Pay once £28.99 | 9,503 | 16,091 | 1.693× |
| **Every tier compliant at once** | **9,503** | **16,043** | **1.688×** |

**Cutting the quarterly tier changes that band by nothing.** Its floor (9,384) and ceiling (16,564) both sit inside the band that pay-once and yearly set. That is one of the two reasons §15 recommends cutting it.

---

## 8. The amortisation cliff — the figure the PM/BA is waiting on

### 8.1 The date

**Launch + 36 months.** More precisely, the clock starts on **the earlier of Haunts' first sale and its public release** (Definitions), and the build has been fully amortised at the end of month 36. **The price change takes effect at the first price review after that date.** Nobody can put a calendar date on it today, because launch is not set. The build is 61.3 focused solo weeks, and `requirements.md` PLAT-4 owns the calendar.

> **The date is published on the first cost sheet issued after launch, and on the plans screen, as an accounting date labelled as one in the same sentence (PRICE-14). It is not a support date. Haunts has no support date (D4).**

### 8.2 The size, at the reference volume

When the build leaves the cost base, `A` falls from **£43,132.09** to **£18,042.74** — a fall of 58%. Nothing about the product changes.

| At `N*` = 12,692 | Months 1–36 | **From month 37** |
|---|---|---|
| Cost of serving one monthly subscriber for a year | £7.0125 | **£5.0356** |
| Honest monthly price | £0.990 | **£0.711** |
| **Charged, after rounding** | **£0.99** | **£0.69** |
| Margin if the price is **not** changed | 16.51% | **+51.8%** — above the hard cap |
| **Cut** | | **30.3%** |

**The whole ladder at the same volume:**

| Tier | Months 1–36 | **From month 37** | Cut | Margin after | Margin if not cut |
|---|---|---|---|---|---|
| Monthly | £0.99 | **£0.69** | 30.3% | 13.66% | +51.8% |
| Quarterly | £2.59 | **£1.79** | 30.9% | 17.95% | +58.2% |
| Yearly | £9.89 | **£6.49** | 34.4% | 16.36% | +62.5% |
| Pay once (for new buyers) | £28.99 at launch; see §11.2 | **£18.95** | 34.6% from £28.99; 15.7% from year three's £22.49 | 16.53% | — |

**Re-derivation.** The v2 cost base gave 30.3% and 69p at three years (`cost-sheet-v2.md` §5.1, Correction C5.4). **The v3 base gives the same charged price.** The honest post-cliff price rises from 69.6p to 71.1p, and the nearest price point is still 69p. **So the figure the PM/BA asked for is the same number C5.4 recorded, now re-derived on the current base.** It is not a carried-over number.

### 8.3 The cut depends on how many subscribers Haunts has — and on which rule Candour commits to

**§0-F said the cut is not automatic. This is the arithmetic behind that.** Two different rules could decide it, and they give different answers.

- **What the Constitution requires on its own: the 30% cap.** Article 2.1: *"no product's margin may exceed 30%, regardless of justification."* After the cliff, 99p breaches the cap only above **7,170 subscribers**. Below that count, **the Constitution requires no cut at all.** Above it, the price must come down only far enough to get back under 30%. At `N*` that is **79p**, a 20.2% cut, with a margin of 27.0%.
- **What Candour's own pricing rule gives: the honest price, worked out again.** Article 2.1: *"Prices target a margin of approximately **20% over published costs**… **A deviation in either direction is a deviation**"*, and a deviation needs a written justification. Suppose Candour kept 99p after the cliff while the honest price was 71p. That would be a deviation above target, and **I can find no honest justification to write for it.** "We charged below cost earlier" is not a cost. Running a deliberate below-cost price was the CEO's choice (Deviation 2), and it creates no debt that later customers owe. **So under this rule the price falls to wherever the rounding rule puts the honest price. At `N*` that is 69p.**

| Subscribers at the first review after month 36 | 2,000 | 4,000 | 5,000 | 6,000 | 7,170 | 8,000 | 10,000 | **12,692** | 15,000 |
|---|---|---|---|---|---|---|---|---|---|
| Honest monthly price after the cliff | £1.78 | £1.15 | £1.02 | 95p | 87p | 83p | 76p | **71p** | 68p |
| Margin at an unchanged 99p | −29.9% | +3.0% | +13.7% | +22.1% | **+30.0%** | +34.6% | +43.4% | **+51.8%** | +57.1% |
| **Cap only — the cut the Constitution requires** | none | none | none | none | none (at the cap) | to 90p | to 79p | **to 79p** | to 69p |
| **Honest-price rule — the cut I recommend committing to** | none | none | none | to 95p | to 89p | to 79p | to 79p | **to 69p** | to 69p |

*(Under the cap-only row, the price is the highest grid point that keeps the margin at or below 30%, per clause 3 of the rounding rule. Under the honest-price row, it is the nearest grid point to the honest price, and never higher than 99p. The first cut under the honest-price rule comes at about **5,540 subscribers**, where the honest price falls below 97p. The full 69p is reached from about **11,100 subscribers**.)*

> **My recommendation, and the copy at §12 is written on it: at every yearly price review, every tier's price is worked out again from the published cost sheet and the actual customer count, and cut whenever the rule gives a lower price.** The cap is the floor under that commitment, not the commitment itself. **Adopting it is a pricing decision under Constitution 5.4 and belongs to the CEO.** If he adopts only the cap, the copy at §12 changes in two numbers: "about 12,700" becomes "more than about 7,200", and "69p" becomes "79p". I recommend against that, because it keeps a price the cost sheet shows to be above the honest one, with no justification to publish.

**What the rule does not do: it never raises a price automatically.** Below about 5,300 subscribers the honest price after the cliff is **above** 99p. At 2,000 subscribers it is £1.78. Any rise is a separate decision by the CEO under 5.4, with Article 4's notice (§10). That is also true before the cliff.

### 8.4 The counterfactual price Article 9 asks for

Article 9 requires *"The counterfactual price at every republication: what the price would be if no layer had opened since the last expired."* **At launch it is identical to the actual price**, because only one layer exists and none has expired. **From the first review after month 36, it is the §8.3 honest-price row, computed without any later increment.** If a v1.1 increment has been capitalised by then, the gap between the actual price and this counterfactual is exactly what that increment costs customers, and the sheet prints both prices side by side.

---

## 9. D7's cumulative test, modelled — the limb that costs nothing

**The clause, as v1.3 settled it.** Article 2.1: *"a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit against the cost of serving them… **This test is one-directional: it forbids a long-standing customer's position drifting above a newer customer's.**"* `CHANGELOG.md` v1.3 item 6 gives the reading: *"that subscriber's own cost — their single share of the build, charged once, plus their own years of running cost."*

**A monthly subscriber at `N*`, cumulative margin by years subscribed, on that reading:**

| Years subscribed | 1 | 2 | 3 | 4 | 5 | 6 | 10 | 20 |
|---|---|---|---|---|---|---|---|---|
| **No cut at the cliff** (99p for ever) | −20.5% | +4.4% | +16.5% | +23.7% | +28.5% | **+31.8%** | +39.2% | +45.2% |
| **Cut to 69p at the cliff** | −20.5% | +4.4% | +16.5% | +16.0% | +15.6% | +15.3% | +14.7% | +14.2% |
| *Annual margin in that year, no cut* | | | 16.5% | **51.8%** | 51.8% | 51.8% | | |

*(Build share per subscriber: £75,268.05 ÷ 12,692 = £5.93, charged once. Running cost: £1.42 + £3.61 a year. Net proceeds: £8.415 a year at 99p, or £5.865 at 69p.)*

**Why it costs nothing. Two reasons, both arithmetic.**

1. **The annual test always breaks first.** The cumulative margin approaches the post-cliff annual margin over time and never overtakes it, because the one-off build share only ever adds cost. So any price that passes the annual cap every year also passes the cumulative test. In the table, the annual cap is breached in **year 4** and the cumulative one in **year 6**. **The cumulative limb forbids nothing the annual limb has not already forbidden.**
2. **The lever it takes away is one the App Store already denies.** D7 records that Candour gives up *"Grandfathering and legacy tiers as retention levers."* Apple's page on subscription pricing, retrieved this session: *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. **You don't have the option to preserve the higher price for existing subscribers.**"* [E, [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions), retrieved 2026-09-22. **Single source by nature.**] **Google Play's equivalent was not retrieved.** If Play *does* allow an old, higher price to be kept, then the cumulative limb has real force for Android subscribers. **Owner: CFO, at store configuration.**

> **Finding: on Apple, D7's cumulative limb costs Candour £0. The cost of D7 is entirely in its notice limb.**

---

## 10. The notice period — 180 days recommended, and what each option costs

> **CEO decision, 2026-09-22 (D14(b)): 90 days, not the 180 recommended below.** Declined on the written grounds in the decision record: Haunts is a personal journal with no workflow to migrate, 90 can be lengthened later while 180 can never be lowered, and rises are expected to be rare. This section's analysis is preserved as written; the PRICE-12 copy string in §12.3 has been changed to 90 per this sheet's own instruction to change the number and nothing else.

**The duty.** Article 4: *"Where a price rises for a customer who has already bought, give at least 90 days' notice before the new price applies — and longer where a customer would need longer to move to an alternative, **judged from the export the product actually ships**… Each product publishes the notice period it guarantees, in its first cost sheet and on its pricing page, before its first sale; that period may be lengthened, never shortened."*

**The platform's own period is much shorter.** Apple: *"Subscribers receive notice of a price change 27 days before the renewal date."* Consent is needed only if a rise is *"more than 50% of the current price"* **and** above roughly US$5 a period (US$50 a year for annual plans), or if there was another rise within 12 months. [E, same Apple page, retrieved 2026-09-22.] **Candour's period has to be delivered by Candour's own means** (Correction C5.6; PRICE-12; NOT-6).

### 10.1 What notice costs, modelled

Notice costs money only when Candour **raises** a price. Its cost is the revenue given up while existing customers stay on the old price during the notice period.

**The reference case: one 10p step on the monthly tier (99p → £1.09), across 12,692 subscribers.** Each monthly renewal at the old price gives up 10p ÷ 1.2 × 0.85 = **7.08p**. Across `N*` that is **£899 a renewal cycle**.

| Notice | Renewals at the old price | **Revenue given up** | At 4,000 subscribers |
|---|---|---|---|
| Apple's own 27 days | ~1 | £899 | £283 |
| **90 days** (the Article 4 floor) | ~3 | **£2,697** | £850 |
| **180 days** (recommended) | ~6 | **£5,394** | £1,700 |

*(Assumes every subscriber is monthly. Yearly subscribers give up either nothing or a whole year at the old price, depending on where their renewal date falls against the notice window. That is left out rather than guessed.)*

**Where Haunts' prices are likely to go.** Down: the cliff (§8) and the recompute rule (§8.3) both push prices down, and neither involves notice. **A rise happens only if the CEO decides to shrink the below-cost deviation at low volume.** Suppose he did that at 4,000 subscribers, taking 99p to £1.99, the grid point below its honest £2.03. At 180 days' notice that single rise would cost about **£17,000** (£1.00 ÷ 1.2 × 0.85 × 4,000 × 6), or about £8,500 at 90 days. On Apple's thresholds it would need no customer consent: it is more than 50%, but well under US$5. That is the price of giving customers six months to leave with their data, charged against a price that was already below cost. **Stated because it is the real exposure, not the 10p case.**

### 10.2 Why 180 days

1. **The Constitution's test points above 90 for this product.** The test is whether a customer *"would need longer to move to an alternative, judged from the export the product actually ships."* Haunts' export (DATA-3) is a zip of JSON, CSV and a README. **No alternative I am aware of loads it directly, and nobody in this pipeline has checked whether any does.** The CGO's judgment for exactly this case (Correction C6.6): *"Where a product's export is not directly loadable by any alternative Candour is aware of… 180 days rather than 90."* **That is the CGO's judgment, not constitutional text, and I am adopting it as mine.**
2. **The honest argument for 90, recorded against my own recommendation.** The period *"may be lengthened, never shortened."* So 90 keeps an option open and 180 closes it. **I do not think that option is worth keeping.** Its only use would be to shorten the notice later, and the clause exists to stop that.
3. **It costs little at the volumes Haunts is likely to have.** About £1,700 more per 10p step at 4,000 subscribers.

> **Recommendation: Haunts guarantees 180 days' notice of any price rise for an existing customer, published in this sheet and on the plans screen before the first sale.** This is the CEO's decision (5.4). The CGO should confirm the export test.

---

## 11. The pay-once tier

### 11.1 The price, the discount and the crossover

| | |
|---|---|
| **Price at launch** | **£28.99** — three years of the pay-once tier's own cost of service at `N*`, priced by the same rule as every other tier (£28.9916, rounded to £28.99) |
| **Against paying monthly** | 36 × 99p = £35.64. **Difference £6.65, or 18.6%** (18.66%, rounded down) |
| **Why the discount is real and not decoration** | It is the same cost saving the other tiers get: **billing events avoided.** A monthly subscriber creates 12 billing events a year, and each is priced at a 1% chance of a 20-minute support contact (§3.5). A pay-once buyer creates none after purchase. £59.40 at five years was exactly 60 × 99p and saved nothing, which is why UX blocked **B11**. **£28.99 is below 36 × 99p because it costs less to serve.** |
| **Crossover** | A monthly subscriber passes £28.99 on their **30th payment** (29 × 99p = £28.71; 30 × 99p = £29.70). That payment falls **29 months after the first**, which is the PM/BA's "2 years 5 months", re-derived and confirmed under gate Condition 6. **Both describe the same event.** A yearly subscriber passes it on their **3rd** payment (£29.67), two years after the first. A quarterly subscriber passes it on their **12th** (£31.08) |
| **Name** | **"Pay once"** (PRICE-6) |

**One judgment of mine is withdrawn, because D4 changed what it was about.** `cost-sheet-v2.md` §5.6 said that at a three-year life *"it is borderline and I would still name the period"* — something like *"Three years, paid up front"*. **That was right while the pay-once tier bought a supported period. Under D4 it buys no period at all.** A pay-once buyer keeps the app for as long as it exists and runs, with no end date on Candour's side. So *"Pay once"* now describes the tier exactly, and **"three years, paid up front" would now be false.** It would also present the amortisation period as something the customer is buying, which PRICE-11 forbids. **Withdrawn.**

### 11.2 The pay-once price should step down each year while the build is being paid off

**The problem with a flat £28.99.** A subscriber pays towards the build only in the months the build is in the cost base. A pay-once buyer at launch prepays three years, all of them inside the amortisation period. **A pay-once buyer in month 30 also prepays three years at £28.99, but only 7 of those 36 months have any build cost left in them.** A new buyer at the first review after month 36 would pay £18.95 for the same product. **So a flat price charges late buyers for build cost that has already been recovered from other customers.** v2 treated this as something to disclose (Correction C3.2). **It can be fixed, and the fix is cheap.**

**The fix: the honest pay-once price in year k counts only the build that remains to be amortised.**

`pay-once price, year k = [ 3 × (F/N + s_P) + (years of build remaining) × (build per year ÷ N) ] × 1.694118`

| Bought in | Build years left | Honest | **Charged** | Margin, recognised over 36 months | Monthly crossover |
|---|---|---|---|---|---|
| **Year 1** | 3 | £28.992 | **£28.99** | 16.50% | 30th payment |
| **Year 2** | 2 | £25.643 | **£25.49** | 15.93% | 26th payment |
| **Year 3** | 1 | £22.294 | **£22.49** | 17.35% | 23rd payment |
| **From the first review after month 36** | 0 | £18.945 | **£18.95** | 16.53% | 20th payment |

*(At `N*`. Build per year £25,089.35 ÷ 12,692 = £1.9768 a head; `F/N` = £1.4216; `s_P` = £2.306.)*

**Like every other price, this schedule only applies at the reference volume, and the §8.3 rule governs it.** Each year's pay-once price is worked out again from the actual customer count and cut if the rule gives a lower figure. At low volume, where the honest pay-once price is above £28.99, it does not fall. **I am not recommending a fixed, pre-announced ladder of future prices.** I am recommending that the pay-once price follow the same rule as the rest of the ladder, which, done correctly, counts only the build that is left. §12's copy says the pay-once price may be lower for later buyers. It does not print a schedule that would be conditional on volume.

**What it costs.** Two extra store price changes, each a republication under Article 2.1, at the yearly review that already happens. And at the reference volume, about 17% less revenue per pay-once buyer across the three years, averaged: £22.49 and £25.49 against £28.99 twice. §14 shows what that does to reach.

### 11.3 Two consequences of spreading the revenue that nobody had modelled

**(a) A flat pay-once price can push the product through the cap in year four.** Pay-once revenue is recognised over 36 months (§7.3). So buyers from years two and three are still being recognised in year four, **at a price that included build cost the year-four cost base no longer contains.** Take the year-four product margin at `N*`, with subscribers already cut to 69p, and assume old pay-once buyers stop using the app:

| Share of customers who paid once | 0% | 25% | 50% | 75% | 100% |
|---|---|---|---|---|---|
| **Year-four product margin, flat £28.99** | 13.7% | 20.9% | 29.0% | **38.2%** | **48.5%** |
| **Year-four product margin, stepped (§11.2)** | 13.7% | 17.6% | 22.1% | 27.2% | **33.1%** |
| Stepped, if every old buyer is still using it (the §11.3(b) cost) | 13.7% | 13.8% | 13.9% | 14.1% | 14.2% |

**Article 2.1's cap applies per product, per financial year, *"regardless of justification."*** With a flat price, a product that sells mostly pay-once — **which is what §15 recommends** — breaches the cap in year four if its early buyers drift away. Stepping the price keeps it under the cap up to about 85–90% pay-once. Above that, the remaining lever is a cut in the price new pay-once buyers pay in year four. **I recommend stepping, and testing the product margin at every review with pay-once revenue recognised as §7.3 states.** Changing the recognition method to make the margin come out right would be a gaming vector, so the method stays fixed.

**(b) The tail: a pay-once buyer's cost does not stop at month 36, but their revenue does.** Support for an active pay-once user is modelled at **£2.31 a year** (§3.5), for as long as they use the app. **Haunts has no telemetry, so Candour will never know how many are still using it.** There are two ways to carry that cost after month 36:

- **Load it onto the subscription price.** Then subscribers pay for the support of customers on another tier. If surviving pay-once users numbered a quarter of the subscriber base, the post-cliff honest monthly price at `N*` would be **79p rather than 69p**. At half, 89p.
- **Absorb it, as a published deviation below target on the product margin.** At `N*` with a quarter surviving, that is about **£7,300 a year**.

> **Recommendation [J]: absorb it, publish it, and never load it onto the subscription price.** Article 2.1 forbids *"no customer subsidises another product unknowingly"*. That clause is about products, not tiers, **so this is my judgment and not a requirement of it.** Its reasoning still applies inside one product: a subscriber should not pay for a choice another customer made. This deviation also falls *below* target, which is the direction of Deviation 2, the one the CEO has already accepted. **It is a pricing decision under 5.4 and belongs to the CEO.** Either way it is published: the tail is a named line on every cost sheet after month 36.

**This is the real cost of combining D4 (no support date) with a pay-once tier, and it is recorded here so nobody discovers it in year four.** It is also a reason Haunts cannot honestly promise a support date. Every year of support given to pay-once buyers after month 36 is funded by someone other than them.

---

## 12. The customer-facing copy — PRICE-7, PRICE-8, PRICE-9 (and PRICE-12)

**What follows are drafts for `requirements.md` §10.1, where the canonical strings live. That document belongs to the PM/BA, and it was being edited while this sheet was written, so I have not edited it.** The PM/BA should transcribe these drafts. **UX must confirm the wording, and the CGO must confirm Article 4 is met, before sign-off** (as §10.1 already sets out). Brackets mark things only launch can fill. Each figure is at launch prices, and each is re-derived at every yearly review.

**The rules I drafted against:** PRICE-13(b) — no *"supported until"*, no *"lifetime"*, *"forever"* or *"for life"*, no tier said to *cover*, *include* or *last* a period. PRICE-14 — any amortisation date is labelled an accounting date **in the same sentence**. PRICE-10 — the no-support-date statement sits on every screen that shows a price. **B1** — nothing is pushed.

### 12.1 S1 — the crossover, on the plans screen (PRICE-7)

> *"Paying monthly costs £11.88 a year. Paying once costs £28.99. If you pay monthly, your 30th payment — 29 months after your first — takes you past £28.99, and from then on you'll have paid more than paying once would have cost, for the same app. If you pay yearly, your third payment does the same. Which is cheaper for you depends on how long you keep using Haunts, and we don't publish a date until which Haunts will be supported — see below."*

**Fills:** £[M] = **£11.88**; £[P] = **£28.99**; [T] = **30th payment, 29 months after the first** (§11.1). **I added the yearly clause** because §15 keeps the yearly tier and its crossover comes sooner. If the quarterly tier survives, add: *"If you pay every three months, your 12th payment does."*

### 12.2 S2 — later price cuts, on the pay-once screen (PRICE-8, PRICE-14)

> *"If you pay once, you won't share in later price cuts — there's no ongoing price for us to reduce. We work out Haunts' prices again every year from its published costs, and cut them when the numbers allow. The biggest cut is due after [month year] — an accounting date, when the cost of building Haunts has been fully counted, not a statement about how long Haunts will be supported. If Haunts has about 12,700 subscribers by then, the monthly price will fall from 99p to 69p, about 30% less; with fewer subscribers it will fall by less or not at all, and our published cost sheet will show why. The pay-once price is worked out again too, so it may be lower for people who buy later. If you subscribe, any cut reaches you automatically at your next renewal — the App Store doesn't let us keep anyone on the old price."*

**Fills:** [C]% = **about 30%**, 99p → 69p, at about 12,700 subscribers (§8.2). **[month year]** = the start date plus 36 months, set at launch (§8.1). **The PM/BA's draft said *"falls by about [C]%"* with no condition. It is changed on purpose**, because a cut promised without its condition is a promise Candour might not owe (§0-F, §8.3). *"Cut them when the numbers allow"* is the §8.3 recompute rule. **If the CEO does not adopt that rule, this sentence is false and must change** — see §8.3 for the two numbers that change.

### 12.3 S4 — price reviews and the notice guarantee, on the plans screen (PRICE-9, PRICE-12)

> *"How our prices change: we work them out again every year from Haunts' published cost sheet and cut them when the numbers allow — the biggest cut is due after [month year], an accounting date, not a statement about how long Haunts will be supported. Any cut reaches subscribers automatically. If we ever raise a price you already pay, we'll tell you in the app at least 90 days before the new price applies, and you can cancel, or export everything free, before then."*

**PRICE-9** puts the cadence and the step-down on the plans screen. S2 can only do that on the pay-once screen, so this needs a separate string. **PRICE-12** asks for the guaranteed notice period on the pricing page. This string carries **180 days on my recommendation (§10). If the CEO chooses 90, change the number and nothing else.** *"Tell you in the app"* is the persistent in-app notice of NOT-6 and PRICE-12, not a push notification (**B1**).

### 12.4 One conflict in `requirements.md`, and how I would resolve it

**PRICE-1** requires a *"per-month equivalent **to the penny**"* for **every** tier. **For pay-once, that figure only exists if you assume a period.** The only period available is the three-year amortisation period, and **PRICE-11 and PRICE-13 forbid presenting it as a duration.** "£0.81 a month" beside "Pay once" invites the reader to ask *over how long?*, and the only honest answer is *"we don't know, and we don't promise"*. The same applies to printing *"saves 18.6% over three years"*.

> **Proposed resolution [J]: the pay-once row shows "£28.99, once" in the per-month column, and its saving is expressed by S1's crossover sentence instead of a percentage.** A per-month figure for pay-once would be arithmetic on a period Haunts does not have. The crossover is a fact about the customer's own spending that they can check. **The 18.6% is still published here, in the cost sheet, so B11's condition — that a real saving exists before one is claimed — is met.** PRICE-1 should be amended in the open by the PM/BA with UX, not quietly worked around in the build. **Flagged, not blocked. It is outside my blocking scope.**

### 12.5 S3 — the Article 4 statement (PRICE-10). Not redrafted; one flag

The PM/BA's S3 stands as drafted, and it is UX's and the CGO's to confirm. **One flag, because it promises more than the Constitution does, and someone should decide that on purpose rather than by default.** S3 says *"If we ever stop **supporting** Haunts you'll get at least 90 days' notice…"*. Article 7.2 guarantees notice on **discontinuation**, meaning *"Shutting a product down"*. `CHANGELOG.md` v1.3 records that *"7.2 governs how a product **ends** and does not reach a product merely allowed to rot."* **So S3 promises notice in a case the Constitution does not cover: the app stays on sale but is no longer maintained.** I think that is the right promise, and cheap to keep: Candour stops selling when it stops maintaining. **But it is a promise, and it will read as part of the customer's contract.** Owners: **CGO** (whether it discharges Article 4 and what it commits Candour to) and **CEO** (whether to make it).

---

## 13. The Article 9 shared-fee allocation rule

**The problem, restated with the new number.** Some of Haunt's cost lines are company costs that would be incurred in the same amount if Haunt did not exist:

| Shared cost | £/yr |
|---|---|
| AI tooling — the agent seats (§3.4.1) | £897.50 |
| Apple Developer Program | £74.04 |
| ICO data protection fee | £52.00 |
| Google Play registration, amortised (£18.70 ÷ 3) | £6.23 |
| **Total** | **£1,029.77 — 2.39% of `A`** |

The domain (£10) is Haunt's own and is not shared. **Haunt carries 100% because it is the only product.** The Definitions require this: Cost is *"everything it takes to run a product **or the company**"*, and a company with one product has nowhere else to put its costs. **The loophole is not that Haunt carries them today. It is that nothing brings Haunt's share down tomorrow.** A price set on 100% does not fall by itself when a second product arrives, and Article 2.1 says *"no customer subsidises another product unknowingly."*

**Proposed rule, carried from `cost-sheet-v2.md` §13 and unchanged except in size:**

> **Shared-cost allocation.** A cost is **shared** if it would be incurred in the same amount were any one Candour product not to exist. Shared costs are divided **equally across live products** at each annual republication. A product that is live for only part of a year carries a pro-rated share. Every cost sheet states **how many products the allocation was made across, and the per-product amount**. Reallocation happens at the **next annual republication** after a launch, so allocation is never a reason to bring a launch forward or push it back. Any resulting price cut for an existing product goes to existing customers first (Article 2.3.3.1).
>
> **Applied today: one live product. Haunt carries £1,029.77. On the day a second product ships, Haunt's share falls to £514.89 and its prices are worked out again at the next review.**

**Why an equal split and not something cleverer.** An allocation by usage, revenue or hours needs a measurement Candour does not take (no telemetry; hours not recorded, §3.3), and whoever chooses the key can tune it. **An equal split cannot be tuned.** Its weakness is that it is crude when products differ greatly in size. That is a problem for when a second product exists, and it is settled in public when it arises.

**Status.** v2 called this *"a governance fix, not a money fix"* at 0.42% of the cost base. **At 2.39% it is still small, but it is now worth about 300 subscribers on `N*`**, and its largest component is a cost that grows as Candour does more work with agents. **Recommended Article 9 row, flagged again:** *"Charging one product 100% of a shared company cost — exposed by every cost sheet stating the number of live products the shared-cost allocation was made across."* This is the second time I have raised it. **Under *"Twice-flagged is escalated"* I am not flagging it a third time: I am asking the CEO to adopt or decline it in writing.** Article 11 amendments are his, on the CGO's advice.

---

## 14. How many customers Haunts needs — a negative finding

**Three-year published cost: £129,396.27.**

| Tier | Contribution per customer | **Break-even needs** |
|---|---|---|
| **Monthly 99p** | £0.4001 per subscriber-month | **323,423 subscriber-months** = 8,984 held continuously for 36 months |
| **Pay once £28.99** | £13.617 per buyer | **9,503 distinct buyers** |
| Pay once, stepped (§11.2), sales spread evenly | £11.255 per buyer on average | **about 11,500 distinct buyers** [I] |

**With churn, which is what actually decides it.** The tenure figures are the category benchmarks carried forward from `pricing-ladder-model.md` §4.2. **They are single-origin (RevenueCat)**, and that has now been flagged in five artifacts. §16.4.

| Average subscriber tenure | **Distinct subscribers needed** | **New subscribers every month, for 36 months** |
|---|---|---|
| 4.5 months | 71,872 | 1,996 |
| **5.2 months (central)** | **62,197** | **1,728** |
| 6.3 months | 51,337 | 1,426 |
| 7.6 months | 42,556 | 1,182 |
| 13.2 months | 24,502 | 681 |
| **Pay once, flat** | **9,503** | **264** |
| **Pay once, stepped** | **~11,500** | **~319** |

**The subscription needs 6.5 times as many people as pay-once at a flat price, and 5.4 times as many with the step-down.** For the subscription to need fewer people than pay-once, the average subscriber would have to stay **about 34 months**. The retrieved category medians are 5 to 8.

> **Negative finding, at the strength the evidence supports: Haunts is not unviable at a compliant price. It is unviable at 99p on any reach this company has evidence for.** At the volumes anyone can describe, the honest monthly price is **£2.03 at 4,000 subscribers and £3.55 at 2,000**. Both are ordinary app prices, both would be compliant, and neither is 99p. **What the arithmetic rules out is not the product. It is 99p combined with a subscriber base in the low thousands.** The CEO has already accepted that combination as a deliberate deviation below cost (§6.1, Deviation 2), and this sheet publishes its size.

**What would overturn it** (my charter: *"a negative finding… must state (a) what evidence or change would overturn it, and (b) where you looked"*):

1. **A measured average tenure above about 34 months.** It can be measured free in App Store Connect within 90 days of launch.
2. **An acquisition channel.** **D10(b)'s competitor import is the first one anyone has written down**, and it is the right kind: it goes after people who have lost their location history and have nowhere to put it. **It has no number attached.** Nobody has estimated how many UK users hold a Google Timeline or Arc export, or what share would move. **Until someone does, it is a channel without a reach figure, and it overturns nothing.** Owner: Research Analyst.
3. **Pay-once converting nearly as well as monthly.** §15's recommendation depends on the reach advantage *per buyer* holding up *per viewer*. **Nobody has measured how much worse a £28.99 up-front price converts than 99p a month.** If it converts 5.4 to 6.5 times worse, the advantage is gone. It can be tested in the Play 12-tester closed test.
4. **A CEO decision to keep the deviation below cost**, which is the decision already recorded. It does not change the arithmetic. It changes what the arithmetic is for.

**Where I looked:** every cost input in §3, re-derived from the CTO's tables; `research/haunt-brief.md`, `proposals/haunt/*`, both UX notes, both compliance notes, `requirements.md` in full (including §23 and D10(b)'s reasoning), for a reach multiple or an acquisition estimate. **The competitor-import channel is new since v2. No reach figure exists anywhere.**

---

## 15. Recommendation

My charter asks for a recommendation with a reason, not a menu.

> ### Launch at: **Pay once £28.99 · Yearly £9.89 · Monthly 99p** — with the two-week full-feature trial, **no quarterly tier**, **180 days' guaranteed notice** of any price rise, and every price **worked out again at each yearly review and cut whenever the rule gives a lower figure**, pay-once included (§8.3, §11.2).
>
> ### Lead with pay-once. Keep monthly as the way to try it.

**The reason, in one sentence: reach is the constraint that decides this product, and pay-once is the only tier that does not lose to it.** It needs roughly 11,500 buyers over three years, against about 62,000 subscribers. No lever in this sheet is larger — not the build estimate, not the platforms, not the price.

**The supporting reasons, briefly.**

- **Pay-once is the tier with the fewest ways to go wrong.** Nothing to cancel, no renewal to be surprised by, no DMCCA renewal-notice cases, and no charge made by inaction. With D4 it also describes exactly what the customer gets (§11.1).
- **Yearly stays** because it is the best-resolved price on the grid (§7.2), and its compliant band (9,396–16,043) sits almost exactly on pay-once's (9,503–16,091), so keeping it costs the band nothing (§7.5).
- **Monthly stays** because it is the CEO's price, and because it is how someone tries Haunts without paying £28.99 up front. A trial in front of it keeps it honest.
- **Quarterly goes.** It changes the compliant band by nothing (§7.5). It adds a store product on two platforms, a column in PRICE-1's table, a crossover clause in S1, and its own set of DMCCA renewal-notice cases. **And it is the rung nobody has argued for**: the PM/BA already lists it as a cut at §20.2. **It costs something and buys nothing.** Cutting a tier is a pricing-shape decision (Condition 9, 5.4), so this is the CEO's call.

**What I record against my own recommendation**, as in the last two sheets, because it is still true: **the CEO's decision to build Haunts was not a commercial one** (*"if I can release it and it makes a bit of money then I am happy with that"*). Leading with pay-once is the commercially efficient choice. **What still holds under his actual aim** — that Haunts exists and is sold honestly — **is the honesty case:** pay-once is the tier a customer can check against this sheet with one division, and the one with no renewal to be caught out by. **And §11.3 is the price of leading with it:** stepping the price, and absorbing the tail cost, only matter because most customers would pay once.

---

## 16. What moves these numbers, and what would overturn them

### 16.1 The build estimate

The estimate has grown 450 → 1,330 → 2,090 → 2,300.5 hours in four weeks, always upward. §4.5 and §4.6 price what is still unsized: **+6% to +17% on the volume 99p needs.** **Build hours do not move any launch price** (§7.1), **but they move the volume at which those prices are honest**, and so how large Deviation 2 is.

### 16.2 The variable cost — the platform mix and the billing-event cost

| Case | Monthly `s` | **`N*` at 99p** | Post-cliff honest monthly price at that `N` |
|---|---|---|---|
| 100% iOS | £2.5346 | 9,632 | 62p |
| **60/40, as carried** [J] | **£3.6140** | **12,692** | **71p** |
| 100% Android | £5.2332 | 24,241 | 84p |
| Billing-event cost `e` = £0 | £2.3060 | 9,164 | — |

**The platform mix is a guess, and it moves `N*` 2.5-fold.** It can be tested free in the mandatory Play 12-tester closed test. **The billing-event cost is what anchors the whole discount curve.** At `e` = £0, the honest pay-once price at `N*` is **exactly £35.64 = 36 × 99p**. The discount disappears and UX's **B11** bites again, which is the §3.5 warning in numbers. **Both can be measured within 90 days of launch** from store reporting and the support inbox. Until then, every discount on the ladder rests on one seat's judgment about a support pattern nobody has observed.

### 16.3 The largest unresolved question about the cost base: who does the build?

**§4.4 found labour this sheet leaves out**: the non-engineering work. That error runs in the customer's favour. **This is the mirror-image question, and it runs against the customer.** The CTO's 2,090 hours are *"focused solo hours"*, the effort of one human developer (`subscription-sizing-note.md`, unit statement). **Candour's build pipeline includes Engineer agent seats** (`CLAUDE.md`, `/build`; Constitution Article 10). If agents write a material share of the code and the founder reviews it, the founder's actual hours will be fewer than 2,300.5. In that case, **pricing at 2,300.5 hours × £32.71 while also carrying the agents' subscription (§3.4.1) counts the same work twice.** That is Article 9's first loophole: *"Inflating costs to raise the allowable price."*

**How large, I cannot say, and I will not guess.** Nobody has built anything, and nobody records hours. **The two errors point in opposite directions and may partly cancel. Neither is known.**

> **Same remedy as §3.3, and it now does two jobs: record the hours actually worked on Haunts from the first day of build, by category and by who did them.** At the first yearly review, **capitalised hours are restated from the recorded hours, not from the estimate**, which Article 9 already requires: *"Capitalised hours per product against the gate estimate **and** hours actually recorded, restated annually."* Agent time is carried in the tooling line, not in the labour line. **Until then, the launch price rests on an estimate that could be wrong in either direction, and this sheet says so.** Owner: CEO.

### 16.4 Single-origin benchmarks — escalated, not flagged again

Both the tenure figures (§14) and the conversion benchmarks come from one publisher, RevenueCat. `pipeline/evidence-standard.md`: *"A load-bearing claim flagged as unverified on two separate occasions must be resolved, or formally accepted in writing by the CEO, before it may anchor a third artifact."* **They anchor §14 here, which makes this at least the fifth artifact.** **I am asking the CEO to accept them in writing as single-origin, or to commission a second source.** Either answer is fine; staying silent is not. They move no price. They move the reach finding.

### 16.5 What would not overturn anything

- **The labour benchmark.** Every figure scales linearly with £32.71. A different benchmark moves `N*`, not the launch prices.
- **The FX rate.** Dollar-priced lines are about 2.3% of `A` (£977.77 of £43,132.09).
- **The shared-fee rule** (2.4%), and the ICO tier (0.1%).

### 16.6 Where I looked

**Read from disk, 2026-09-21 and 2026-09-22:** `constitution.md` v1.3 in full; `CHANGELOG.md` v1.3; `roles/cfo.md`; `pipeline/evidence-standard.md` v1.1; `pipeline/templates/cost-sheet.md`; `decisions/2026-09-16-haunt-gate.md` — Conditions 1–10, **D1–D10**, Corrections C3–C6 and §17.3; `products/haunt/requirements.md` §§0–2, 8.1, 9, 10, 12, 12.2, 19–20, 24–26 and every requirement row; `products/haunt/cost-sheet-v2.md` §§0, 5, 7–10, 12–17; `products/haunt/subscription-sizing-note.md`, `feasibility-note.md` and `android-and-stack-note.md`, for the unit of the build estimate and any map or tile source; `products/haunt/compliance-note.md` C1–C11.

**Retrieved externally this session (2026-09-22), at primary:** Apple's UK GBP price grid (PDF, text-extracted); App Store Connect Help on subscription price changes — decreases, the 27-day notice and the consent thresholds. **Carried from §§1–6 (2026-09-21, or 2026-09-18 for ONS)** and not re-retrieved: ONS ASHE, Claude pricing, Apple Developer Program, the ICO fee, Google Play registration, GBP/USD.

**Attempted and failed:** Google Play's GBP price grid (the help page links to a table that did not come back through retrieval); Google Play's policy on keeping existing subscribers on an old price (§9). **Not attempted, and not asserted:** any map-tile provider's pricing (§4.6).

**Looked for and did not find:** a reach estimate for competitor import; any seat's sizing of the 16 new requirements; any source for map tiles; any recorded hours.

---

## 17. Blocks and flags

**My blocking power, quoted:** *"Launch of any pricing not backed by a published cost sheet; any proposal without a credible cost model."* It covers the price level and the cost model, and nothing else.

### 17.1 The block — **LIFTED**

> **LIFTED, 2026-09-22.** The block as narrowed at `cost-sheet-v2.md` §16.1 read: *"No Haunt price may be published under Article 3… until the supported life is published… **The block is about the existence of a published period, not about which one.**"* Constitution **v1.3** has published one: *"**Standard amortisation period:** three years (36 months), straight-line, in equal monthly amounts. It is the same for every Candour product"* (Definitions; CEO decision **D6**; `CHANGELOG.md` v1.3). **The checklist item that was failing now passes. The block lifts in full, and I am not replacing it with another.**
>
> **Checked, so the lift is not a formality.** (1) This sheet re-derives every price on the three-year period and carries the Article 2.1 schedule and statement (§2, §3.3). (2) The cost model is credible in the charter's sense: every sized item is carried, and every unsized item is named, bounded and priced as sensitivity (§4.5, §4.6). **A model that states its gaps is credible. One that hides them is not.** (3) The labour benchmark is at primary (Condition 5, discharged).

**What the lift does not do.** It does not set a price: pricing is the CEO's alone (5.4). It does not clear release. And it does not waive the checks that must happen **before a price appears in a store**. Those are pre-publication tasks, not blocks:

| Before the first price publishes | Owner |
|---|---|
| Confirm each charged point in App Store Connect and in Play Console (§7.2) | CFO |
| The CEO's decisions on §15's recommendation, §8.3's recompute rule, §10's notice period and §11.3's tail | CEO (5.4) |
| The §12 strings transcribed into `requirements.md` §10.1 and confirmed by UX and the CGO | PM/BA, UX, CGO |
| The start date and the date of the first pound of revenue, on the first cost sheet after launch (§3.3) | CFO |

**One stale statement to correct elsewhere.** `requirements.md` §0 still says the CFO's sheet *"is priced on a **five-year** life"*, and lists the CFO block as live. **Both are now out of date.** Owner: PM/BA.

### 17.2 Blocks I do not hold

I hold **no block** over: the shape of the ladder; cutting the quarterly tier; stepping the pay-once price; the notice period; the treatment of the tail; the naming of any tier; any wording at §12; or any Article 9 or 11 proposal. **I have argued strongly for several of them. Arguing is not blocking.**

### 17.3 Flags — each with the seat that holds it

| # | Flag | Holder |
|---|---|---|
| F1 | **Size the 21 unsized requirements in one pass** (§4.2's five and §4.6's sixteen). Say whether VEN-17 sits inside the venue rows. Name a security-and-defect row to replace my provisional 45 h/yr (§5) | **CTO** |
| F2 | **No artifact names a map-tile source.** Network tiles change the offline claim; metered tiles would be the first per-user variable cost (§4.6). LOOK-2 depends on it | **CTO**; **CGO** if MapKit's Schedule 6 is triggered |
| F3 | **DATA-15 carries recurring maintenance** whenever a third party changes its export format (§4.6) | **CTO** to size |
| F4 | **PRICE-1 conflicts with PRICE-11 and PRICE-13 for the pay-once tier** (§12.4) | **PM/BA** with **UX** |
| F5 | **S3 promises notice on ceasing *support*, which is wider than 7.2's *discontinuation*** (§12.5) | **CGO**, then **CEO** |
| F6 | **Record hours from day one of build, by category and by who did them.** This closes §3.3's missing ratio, §4.4's missing labour and §16.3's possible double count together | **CEO** |
| F7 | **Accept the RevenueCat-only benchmarks in writing, or commission a second source** (§16.4) | **CEO** |
| F8 | **Adopt or decline the shared-cost rule and its Article 9 row, in writing** (§13) | **CEO** on the **CGO**'s advice |
| F9 | **The Play-side facts** behind §9's "costs nothing": whether Play lets an old, higher price be kept for existing subscribers | **CFO**, at store configuration |
| F10 | **A reach estimate for competitor import**, the first acquisition channel anyone has written down (§14) | **Research Analyst** |
| F11 | **"Haunts" is a working name until PLAT-6's three checks pass.** This sheet uses it in its §12 copy, and that copy must not be published before those checks | **CGO** (trademark), **PM/BA** |

---

## 18. Corrections — mine and others', visibly and in place

| Where | What was said | What is true | Classification |
|---|---|---|---|
| **Decision record, Condition 9.4, 9.5 and C5.4; `cost-sheet-v2.md` §10** | The cliff cut is presented as automatic: *"Price must fall to ~68p"*; *"at three years the cut is 30.3%, 99p → 69p"* | **The cut depends on subscriber count.** The Constitution requires it only above ~7,170 subscribers, and then only to 79p at `N*`. **69p is the result of Candour's own recompute rule at ~12,700** (§8.3). The figure is right; calling it automatic is not | **CORRECTION** — a statement of what the rules require. **Mine**: v2 §10 and my figures behind C5.4 |
| **`cost-sheet-v2.md` §5.1, §5.6** | Crossover at three years: *"29 months"* | **The 30th payment**, which falls 29 months after the first. v2 used payment count at five years (*"49 months"*) and elapsed time at three, **so one of its two figures was inconsistent with the other.** The PM/BA's "2 years 5 months" is correct as elapsed time | **Arithmetic convention, mine.** §0-G's *"not month 29"* is right on the payment-count convention, and §11.1 now gives both |
| **`cost-sheet-v2.md` §5.6** | At three years, name the tier for its period, not "Pay once" | **Withdrawn.** Under D4 the tier buys no period, and a period in its name would now be false (§11.1) | **Superseded by D4** |
| **`cost-sheet-v2.md` §9, S1 and S2 drafts** | *"covers the whole period we've committed to supporting"*; *"when the build cost finishes being paid off in [month year]"* | **Replaced by §12.** The first named a support date D4 withdrew. The second printed an unlabelled date and an unconditional cut | Superseded by D4; the unconditional cut is the CORRECTION above |
| **This sheet, §0-E** | *"the cut is 30.3%, the monthly price falls from 99p to 69p"* | True **at `N*`, under the recompute rule**, which the CEO has not yet adopted. §0-N and §8.3 give the condition | **Clarification.** Nothing false; a condition was left implicit |
| **`requirements.md` §0 and §21.3** | The CFO's sheet is priced on a five-year life; the CFO block is live | Priced on three years; **the block is lifted** (§17.1) | Stale, owed by the PM/BA |
| **Decision record, §17.3 (Condition 9.3)** | Discounts deeper than ~10% collapse the band | Already filed by this seat as a CORRECTION. **Still owed before the record publishes on 2026-10-16** | CORRECTION, filed |

**A process note, because gate Condition 6 is working and should be seen working.** Three of the seven rows are corrections to my own earlier work. Two of them — the automatic cut and the crossover convention — were found only by re-deriving an earlier figure on a new base, rather than carrying it forward.

---

## 19. Disclosures

### 19.1 Related-party disclosures

**None.** No payment to the founder, his family, or any affiliated entity is contemplated. **All founder labour — £75,249.35 of build and £17,009.20 a year of fixed labour at the ONS benchmark — is unpaid and not drawn.** It appears as cost because Constitution 2.1 requires *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."* The AI tooling (§3.4.1) is paid to a third-party supplier and is not a related party.

### 19.2 What a sceptical customer should take from this document

1. **Haunts costs one person's time, plus the software tools that help him.** There is no server, no data collection and no advertising. **About 97% of the cost is labour, valued at a published national median, and none of it has been paid.**
2. **The price depends on how many people buy it.** 99p a month is the honest price at about 12,700 subscribers. **At the numbers Haunts is likely to reach, 99p is below cost, deliberately, and this sheet says by how much.**
3. **Haunts promises no support date.** The three years in this sheet is how the build cost is spread for accounting. It is not how long Haunts will last.
4. **Prices are worked out again every year and cut when the numbers allow.** The largest cut is due after month 36 and depends on how many subscribers there are. A cut reaches subscribers automatically. **A pay-once buyer does not share in later cuts, and the screen tells you so before you buy.**
5. **Any rise in a price you already pay comes with at least 180 days' notice (if the CEO adopts the recommendation), and you can leave with all your data first.**
6. **Nothing here has been built.** The largest figure is an estimate that has grown five-fold in a month, and may still turn out too high if Candour's own agents do part of the work. **Actual hours will replace it at the first yearly review.**

---

## Change log

| Date | Change |
|---|---|
| 2026-09-21 | **§§0–6.2 drafted** on Constitution v1.3, D1–D8, the Block 4 ruling and `requirements.md` at 139 requirements. Supersedes `cost-sheet-v2.md` in full. **The draft stopped at §6.2 when the seat hit a rate limit.** |
| 2026-09-22 | **Completed, §6.2's close to §19.** Continued from §6.2 without rewriting §§0–6.2. **Three marked insertions:** the header line on the name (D9); an **addendum to §0** (items M–P); and **§4.6**, the scope added since §4 (24 requirements, 16 unsized, photos adding no cost line). Delivers: the ladder and per-tier margins on three years (§7); **the cliff — 30.3%, 99p → 69p at `N*`, launch + 36 months, depending on subscriber count** (§8); D7's cumulative limb at £0 and the notice limb priced, **180 days recommended** (§§9–10); **pay-once at £28.99 with a real 18.6% discount, stepping down yearly** (§11); **the copy for PRICE-7, 8, 9 and 12** (§12); the shared-cost rule at 2.39% (§13); the reach finding (§14); **one recommendation** (§15); **the CFO block lifted** (§17.1); seven corrections (§18). Retrieved at primary this session: Apple's GBP grid and Apple's subscription price-change page. **Not a price: Constitution 5.4 reserves pricing to the CEO.** |

*Prepared by the Chief Financial Officer under `roles/cfo.md`. It prepares and flags; it does not certify (Constitution 6.1). Arithmetic in §§6–16 is owed re-derivation by a seat other than this one under gate Condition 6 before publication.*

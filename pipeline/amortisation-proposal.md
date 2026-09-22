# Amortisation of build labour — a standard company-wide period

**Seat:** Chief Financial Officer · **Date:** 2026-09-20 · **Status:** Proposal to the CEO. Not a decision, not an amendment, and not a price.

**Scope.** This document governs **every Candour product**, which is why it sits in `pipeline/` and not in `products/haunt/`. Haunt is used throughout as the worked example because it is the only product with a cost base, and every Haunt figure here is traceable to `products/haunt/cost-sheet-v2.md`.

**What this document is not.** The **CGO is drafting the constitutional wording** for the Definitions entry in parallel. Nothing below is proposed amendment text. Where I describe a rule, I am describing an accounting convention and its arithmetic consequences, for the CGO to turn into wording and the CEO to decide under Article 11 and Constitution 5.4. **I flag; I do not block on any of it, except where §9 says otherwise, and that block is the one I already hold.**

**Evidence:** tagged per `pipeline/evidence-standard.md` v1.1. Every external source below was **retrieved at primary on 2026-09-20** in the session that produced this document; nothing external is cited from memory. Repository files are marked *read from disk 2026-09-20*. Constitutional claims quote the clause in the same passage.

---

## 0. The answers, before the arithmetic

**A. The recommended standard period is three years (36 months), straight-line, from the date of a product's first sale.** The argument is software economics, not Haunt: the platforms force a rewrite cadence of roughly one year (Apple's annual SDK requirement, Google Play's annual target-API requirement, both retrieved at primary at §2.2), so by month 36 a material share of the original build has already been replaced by maintenance labour that is separately charged as an operating cost. Amortising past that point charges a year-4 customer for code that no longer exists. §2.

**B. Haunt's numbers did influence the choice, and I say so plainly rather than letting the coincidence pass.** I recommended three years for Haunt on 2026-09-20 in `cost-sheet-v2.md` §14, and I am now recommending three years for every product. §2.4 sets out which parts of the argument are independent of Haunt, which are not, and what would have changed my answer.

**C. For Haunt, the standard period changes no number at all.** The three-year column already exists in `cost-sheet-v2.md` §5.1. Monthly **99p**, quarterly **£2.59**, yearly **£9.89**, pay-once **£28.99**; 99p is honest at **11,922** subscribers, recovers its cost at 8,439 and hits the 30% cap at 16,101; the reach requirement is **58,426 distinct subscribers (1,623 a month for three years)** or **8,927 pay-once buyers (248 a month)**. What changes is not the arithmetic but **what Candour says on the pricing screen**. §4.

**D. The cliff moves, it does not go away, and for Haunt it gets worse.** At three years the cut falls in **month 37** and is **30.3%** on the monthly tier (99p → 69p) against 20.2% at five years, because a shorter period makes the build a larger share of each subscriber's annual cost. If the price is not cut, the realised margin is **+54.4%**, against a cap Article 2.1 applies *"regardless of justification"*. Article 2.3.3.1 lands the cut on existing customers and Apple performs it irreversibly. §5.

**E. Four new gaming vectors replace the one that is being removed, and the exposing numbers are cheap.** Inflating capitalised hours; restarting the clock with a "v2"; rolling layers so the price never actually falls; and deferring the start date. Each is exposed by a **published layer schedule** — one line per capitalised increment, with its hours, start date, period and balance — plus the **capitalised share of each year's labour**. §6.

**F. The public write-off on discontinuation must survive, and it becomes more important, not less.** It is now the only published number that penalises over-stuffed or over-long capitalisation, because the support commitment that used to discipline the period has gone. It attaches to Article 7.2's closing cost sheet, which already exists. §7.

**G. The D2 hours gap does not disappear with the promise. Candour still owes the hours.** Withdrawing the customer-facing sentence removes a **contractual** exposure under CRA 2015 s.36(3). It does not remove a **costing** error: security and defect-fix work is real recurring labour whether or not anyone promised it, and a cost sheet that omits real hours understates the honest price. The sensitivity stands at 3–10% on the volume the price needs. §8.

**H. My standing block does not lift on this proposal — it changes its lifting condition.** Constitution v1.2 as it stands says *"Absent a published support commitment, build labour is a first-year operating cost."* **Decoupling without the amendment does not give Candour a three-year amortisation; it gives Candour first-year expensing**, an annual cost base of **£90,205.20 rather than £40,517.17 (2.23×)**, and an honest monthly price at the same volume of about **£1.58 rather than 99p**. The amendment must be in force before any Haunt price publishes. §9.

**I. One disagreement, recorded once.** The v1.2 clause gave customers a published support commitment as a by-product of an accounting rule. Removing it removes that, and Article 7.2 does not replace it: 7.2 governs **exit** (90 days' notice, free export), not **continuation**. I am not blocking and the classification under Article 11.2 belongs to the CGO — but the decision record should say what was lost rather than imply nothing was. §10.

---

## 1. What is being replaced, and why — stated so a stranger can audit the change

**The clause, quoted in full.** Constitution v1.2, Definitions: *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year; maintenance and support are operating costs. Three conditions bind that treatment: the amortisation period must equal a **published** support commitment to customers; any unamortised remainder is written off publicly on discontinuation (7.2); and the period may be shortened, never lengthened. Absent a published support commitment, build labour is a first-year operating cost."* [E, `constitution.md` v1.2, read from disk 2026-09-20]

**Three flaws surfaced in three days, and all three come from the same tie.**

1. **It punishes honest under-promising.** Commit to two years, discover you can support five, and the clause forbids the longer period reaching the price. Priced out at Haunt's five-year reference volume, an early customer faces an honest price **£4.21 a year higher** than if the true life had been declared — £8.42 over two years, with no mechanism to give it back [`cost-sheet-v2.md` §5.5, read from disk 2026-09-20].
2. **The permitted direction is the price-raising one.** Shortening compresses the same build into fewer years, which raises the annual charge and therefore the price; it is permitted with no justification. Lengthening lowers the price and is banned outright. Article 2.1 requires *"deviations… must be justified in writing"* and Article 2.3.3.1 makes *"Price reductions for existing customers"* the first call on the waterfall's remainder. The ratchet runs against both.
3. **The tie freezes the period in both directions once sold against.** CRA 2015 s.36(3): *"Any information that is provided by the trader about the digital content that is information mentioned in paragraph (a), (j) or (k) of Schedule 1… (main characteristics, functionality and compatibility)… is to be treated as included as a term of the contract"*, and s.36(4): *"A change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader."* [E, [CRA 2015 s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36), retrieved at primary 2026-09-20]. A published support period is such information. Once sold against, it cannot be shortened; the ratchet bars lengthening; and breaking the tie destroys the amortisation treatment altogether.

**The replacement, as the CEO framed it.** A **standard company-wide amortisation period**, used purely as an accounting convention, with **no customer-facing support promise attached**. It is ungameable not because a rule forbids the choice but because **there is no choice to make**: the period is the same for every product, so it cannot be selected to flatter one product's price. Customers are protected by Article 7.2 — *"At least **90 days' notice** to every customer"*, *"Full data export (Article 4)… free"*, *"The product's code is **open-sourced where third-party rights allow**"*, and *"A published closing cost sheet for the product's final period"* — which is untouched.

**What the replacement fixes, checked against the three flaws.** Flaw 1 dissolves completely: there is nothing to under-promise, so there is no penalty for honesty. Flaw 2 dissolves: there is no per-product shortening or lengthening to permit or forbid. Flaw 3 dissolves **provided** the period is published as an accounting convention and not as a characteristic of the product — which is a drafting condition, and the most important one in this document. §3.5.

---

## 2. The recommended period: three years

### 2.1 What a company-wide period has to be good at

It applies to every product Candour ever ships, so it cannot be argued from one product's convenience. Four properties, in the order that decided it:

1. **It should approximate the period over which the original build still exists as an asset.** Amortisation is not a pricing lever; it is an attempt to charge each year's customers for the share of the build they are actually using. If the code has been replaced, the customer is paying twice — once through the amortised original and once through the maintenance labour that replaced it.
2. **It should be shorter than the horizon over which Candour can predict anything.** Candour has shipped nothing and measured no product's life. Where a life cannot be reliably estimated, the honest response is a **published convention with a published reason**, not a forecast dressed as one.
3. **It should make the two errors roughly symmetrical.** Too short overcharges early customers and puts a steep cliff in the middle of a product's life. Too long undercharges early customers, enlarges the unamortised remainder written off if the product dies, and hands a later reader a cost sheet full of a build that no longer exists.
4. **It should be a round number a customer can check in one division.** A cost sheet that requires a reader to trust a schedule is worse than one they can reproduce.

### 2.2 The evidence, retrieved at primary

**The platforms force an annual rewrite cadence. This is the load-bearing evidence and it is from the two publishers themselves.**

- **Apple.** *"Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26"* — in force since **28 April 2026**; the prior requirement, Xcode 15 / iOS 17, ran from **29 April 2024** [E, [Apple Developer, *Upcoming requirements*](https://developer.apple.com/news/upcoming-requirements/), retrieved at primary 2026-09-20]. **(single source by nature — Apple is the only publisher of Apple's rules)**
- **Google.** From **31 August 2026**, new apps and updates *"Must target Android 16 (API level 36) or higher"*, and existing apps *"Must target Android 15 (API level 35) or higher to remain available to new users on devices running Android OS higher than the app's target API level"* [E, [Android Developers, *Meet Google Play's target API level requirement*](https://developer.android.com/google/play/requirements/target-sdk), retrieved at primary 2026-09-20]. **(single source by nature)**

> **[I], from those two [E] premises:** a mobile product cannot remain on sale without an annual, externally-dated pass over its own build. Three such passes have happened by month 36. The original build is not a three-year-old asset by then; it is a three-year-old asset that has been opened, altered and re-shipped three times, with each alteration separately charged to customers as maintenance. **Three years is roughly where "the build we capitalised" stops being a description of the code that is running.** I state this as inference rather than measurement: nobody has measured what share of a Candour build survives three years, because Candour has no build.

**The accounting convention points the same way, and gives the mechanism for publishing it.** The Large and Medium-sized Companies and Groups (Accounts and Reports) Regulations 2008, Schedule 1, paragraph 22: **22(1)** *"Intangible assets must be written off over the useful economic life of the intangible asset"*; **22(2)–(3)** where the useful life cannot be reliably estimated, the asset is written off over *"a period chosen by the directors"* which *"must not exceed ten years"*; and **22(4)** the directors must disclose *"the period referred to in sub-paragraph (2) and the reasons for choosing that period"* [E, [SI 2008/410 Sch 1](https://www.legislation.gov.uk/uksi/2008/410/schedule/1), retrieved at primary 2026-09-20].

**Why that matters here, stated precisely rather than over-claimed.** Candour is *"an unincorporated brand operated by its founder, not a registered legal entity"* (`constitution.md`, Preamble), so these Regulations do not bind it today. What they supply is a **precedent for the exact structure the CEO has chosen**: where a life cannot be reliably estimated, the law does not demand a forecast — it accepts a chosen period, caps it, and requires the chooser to publish the period **and the reasons**. That is this proposal in three lines, and it means Candour's convention would already be in the shape its own accounts will need at incorporation. **The ten years is a ceiling for a going concern's intangibles generally, not a target for consumer software, and I am not using it as support for a long period.**

### 2.3 Why not two, five or ten

| Period | The case for it | Why I am not recommending it |
|---|---|---|
| **1 year** | No amortisation machinery at all; identical to expensing | Charges the entire build to the first year's customers, who are the fewest. On Haunt that is an annual cost base of **£90,205.20 (2.23×)** and an honest monthly price of **£1.58** at the §4 reference volume. It makes every launch price a punishment for being early |
| **2 years** | Smallest unamortised remainder at risk; most conservative | Shorter than the interval over which the platforms force the work, so the cliff lands while the first version is still recognisably the shipped product. On Haunt it raises the volume at which 99p is honest by **73%** and puts an irreversible 30.3% cut at month 25 [`cost-sheet-v2.md` §5.1] |
| **3 years** | See §2.1–2.2 | — |
| **5 years** | Lowest prices at any volume; flattest cliff (20.2% on Haunt) | It is a **forecast**, and Candour has no measured year of anything to forecast from. It also maximises the unamortised remainder: a product that dies at month 30 writes off **50%** of its build at five years against **17%** at three. And it charges year-5 customers for a build that has had five forced rewrites pass over it |
| **10 years** | The statutory ceiling where life is unknowable | Not defensible for consumer mobile software on the retrieved platform cadence. It would also make the write-off on early death the largest number on most closing cost sheets |

**One genuine cost of choosing three over five, carried rather than hidden.** Three years produces higher honest prices at any given volume than five. On Haunt at the five-year reference volume the difference is **£1.146 against £0.990 a month — £5.62 per customer over three years** [`cost-sheet-v2.md` §14.1]. **Under the old clause that difference was the price of my caution about a promise. Under decoupling there is no promise, so it is now purely the price of a shorter accounting convention — and it buys a smaller write-off exposure and a cost sheet that describes code that exists.** I think that is a fair trade. It is a judgment [J] and the CEO may reasonably take the other side.

### 2.4 Did Haunt's numbers influence this? Yes. Here is exactly how

**The honest answer is yes, and the coincidence deserves more than a disclaimer.** I recommended three years for Haunt earlier today, on deliverability grounds — that *"Three years is the longest period for which the promise and the funded work plausibly coincide"* [`cost-sheet-v2.md` §14.1]. I am now recommending the same number company-wide. A reader is entitled to suspect the second recommendation was reverse-engineered from the first, which is precisely the failure the CEO caught when the five-year figure turned out to have been reverse-engineered from £59.40.

**So here is the separation, item by item:**

- **The deliverability argument — "will Candour actually do 360 hours a year for five years?" — is now irrelevant and I have dropped it.** It was an argument about keeping a *promise*. There is no promise. It cannot support the company-wide number and I am not using it.
- **What survives independently of Haunt** is §2.2: the platform rewrite cadence (retrieved from Apple and Google, applies to any mobile product Candour ships), the write-off asymmetry (arithmetic, applies to any product), and the "chosen period, published with reasons" precedent (statute, applies to any company).
- **What the Haunt numbers contributed** is a sanity check in one direction only: three years does not make Haunt's prices absurd, and it does not change three of its four prices at all. **Had three years made Haunt unshippable I would have said so, and I would still have recommended three, because a company-wide accounting convention that bends to the first product's convenience is the vector this whole exercise exists to close.**
- **The test I applied to myself:** would I recommend three years for a product with none of Haunt's properties — a small web tool with no app store, no OS cadence and a £5,000 build? **Yes, but for a weaker reason**: dependency and framework turnover rather than store policy, which I have not retrieved evidence for. **That is the soft spot in this recommendation and it is named at §11.**

---

## 3. The convention in full

Written as accounting mechanics, for the CGO to compress into wording. Each clause exists because something would otherwise be ambiguous or gameable; where that is the case, §6 names the vector.

### 3.1 What is capitalised

**Only one-off build labour that produces a shippable increment of the product, plus one-off third-party costs incurred to ship it.** Everything else — maintenance, support, compliance upkeep, hosting, tooling, fees — is an operating cost of the year it falls in, exactly as v1.2 already says: *"maintenance and support are operating costs."*

**The test, stated so the boundary is not argued afresh each year [J, this seat's convention]:** work is capital if it delivers a capability the product did not previously have. Work is operating if it keeps a capability the product already has working. *Making the app run on the next iOS is operating, however many hours it takes.* Haunt's cost sheet already applies this split — 2,278 build hours against 360 h/yr maintenance [`cost-sheet-v2.md` §§2.2–2.3].

**Materiality floor [J]:** an increment below **100 hours (£3,271 at the current benchmark)** is expensed, not capitalised. A schedule of twelve trivial layers is less legible than one honest expense line, and Constitution 1.5 makes legibility a cost question.

**Pre-launch spikes that return "don't build"** are not capital, because there is no product to amortise them over. They are written off publicly. This is unchanged from `cost-sheet-v2.md` §2.2 and holds independently of the period.

### 3.2 The period and the start date

- **Three years (36 months), straight-line, in equal monthly amounts.**
- The clock starts on the **earlier of the product's first sale and its public release**, published on the product's first cost sheet. Not on the date the work was done, and not on a date chosen later. §6 vector 4 is why this sentence is specific.
- A product that never launches has no clock. Its hours are written off publicly.

### 3.3 Layers, not a single balance

**Each capitalised increment is its own layer with its own 36-month clock, starting when that increment ships.** A later increment never extends, restarts or re-bases an earlier one.

This is the structural answer to the "v2" vector (§6, vector 2). It has a consequence the CEO should see now rather than discover in year four: **a product under continuous development carries overlapping layers, so its amortised charge does not fall to zero on one date — it steps down as each layer expires.** That is more honest than a single cliff, and it is also how a company could hide a cliff that ought to happen, which is why the layer schedule is published.

### 3.4 Changing the standard period later

**A change to the standard period is an Article 11 amendment and applies only to layers capitalised after it takes effect.** Existing layers run out on the period they started under.

**Why this clause is not optional.** Without it, re-amortising existing layers over a longer period lowers prices retrospectively (harmless) and over a shorter period raises them (not harmless) — which re-creates flaw 2 at company scale instead of product scale. The exposing number is in the layer schedule: every layer shows the period it was opened under.

### 3.5 The drafting condition that makes the whole thing work

> **The period must be published as an accounting convention and must be accompanied, on the same page, by an explicit statement that it is not a support commitment.**

**Why.** CRA 2015 s.36(3) attaches to *"information… about the digital content"* concerning *"main characteristics, functionality and compatibility"* [E, retrieved at primary 2026-09-20, quoted in full at §1]. A cost sheet line reading *"build amortised over three years"* is information about Candour's accounting. A pricing-screen line reading *"three-year product"* is information about the product. **The first is the plan; the second re-creates exactly the contractual freeze the CEO is removing.** The distance between them is one sentence of drafting, and the drafting is the CGO's.

**I am not giving a legal opinion and cannot.** Constitution 6.1: *"anything involving… third-party licence terms whose interpretation determines a product's architecture or cost, receives review by qualified human professionals."* Whether this separation holds against s.36 is a determination for the CGO and, before launch, for a qualified human. **What I can say from the money side is that the entire cost advantage of decoupling evaporates if the separation fails, because a period that is contractual is a period that is frozen, and we are back at flaw 3 with fewer words.** Recorded as flag **A3** (§12).

### 3.6 What does not change

- **Straight-line.** No front-loading, no accelerated curves. A customer can divide.
- **Any unamortised remainder is written off publicly on discontinuation (7.2).** §7.
- **Pay-once revenue is recognised over the amortisation period, not in the year of receipt** — the rule I set at `cost-sheet-v2.md` §16.3 (F7). It now has a cleaner hook: both sides of that tier run on the same 36 months.
- **Labour is costed at the published ONS benchmark whether or not it is drawn** (Constitution 2.1). Nothing here touches that.

---

## 4. What it does to Haunt

### 4.1 The four lives, side by side

All figures at the point-estimate cost base: capitalised build **£74,532.04**, fixed annual operating cost **£15,673.16**, benchmark **£32.71/hour** [`cost-sheet-v2.md` §§2.2–2.3, read from disk 2026-09-20]. `N*` is the subscriber count at which 99p a month is exactly the honest price under Candour's pricing rule `V = C(N) × 1.694118`.

| | **2 years** | **STANDARD — 3 years** | **5 years** |
|---|---|---|---|
| Amortised build per year | £37,266.02 | **£24,844.01** | £14,906.41 |
| **Annual fixed cost `A`** | **£52,939.18** | **£40,517.17** | **£30,579.57** |
| Total published cost over the period | £105,878.36 | **£121,551.52** | £152,897.83 |
| **Monthly** | £0.99 | **£0.99** | £0.99 |
| **Quarterly** | £2.59 | **£2.59** | £2.59 |
| **Yearly** | £9.89 | **£9.89** | £9.89 |
| **Pay once** | £19.49 | **£28.99** | £48.49 |
| 99p recovers its cost at | 11,027 | **8,439** | 6,369 |
| **99p is exactly honest at `N*`** | **15,577** | **11,922** | **8,998** |
| 99p hits the 30% cap at | 21,038 | **16,101** | 12,152 |
| **Distinct subscribers needed** (5.2-month tenure) | 50,892 | **58,426** | 73,493 |
| **Sustained acquisition rate** | 2,121/month | **1,623/month** | 1,225/month |
| **Distinct pay-once buyers needed** | 11,517 (480/mo) | **8,927 (248/mo)** | 6,701 (112/mo) |
| **Cliff falls at** | month 25 | **month 37** | month 61 |
| **Size of the cut (monthly tier)** | 30.3% | **30.3%** | 20.2% |
| Margin if the price is not cut | +62.2% | **+54.4%** | +44.7% |

*Re-derivable in one line: at `N*`, `A/N* = 11.88 ÷ 1.694118 − 3.6140 = £3.39851`, so `N* = A ÷ 3.39851`. At three years, £40,517.17 ÷ 3.39851 = **11,922**.*

### 4.2 The thing the CEO is actually choosing

> **The period does not set three of the four prices. It sets the number of customers at which they are honest.**

Monthly, quarterly and yearly are 99p, £2.59 and £9.89 at two, three and five years alike, because the honest price is `(A/N + s) × 1.694118` and holding the price at 99p moves `N`, not `V`. Only the pay-once tier's **price** moves, because it is the only tier that buys a span of time rather than a unit of it.

**Against the five-year figures published at D2, the standard three-year period costs Haunt:** 2,924 more subscribers before 99p is defensible (+32.5%), **398 more new subscribers every month** (+32.5%), and **2,226 more pay-once buyers** (+33.2%). **Against two years it saves** 3,655 subscribers and 498 a month. Nothing in the three-year column is arithmetically impossible; all of it sits inside a reach finding this seat has already called unreachable on the evidence available [`cost-sheet-v2.md` §12.4].

### 4.3 What actually changes for Haunt — and it is words, not numbers

Three changes, none of them arithmetic:

1. **D2 is withdrawn or rewritten.** *"For five years from launch the app continues to run on then-current iOS and Android, security and defect fixes are made, and the bundled venue index is refreshed"* [E, `decisions/2026-09-16-haunt-gate.md`, CEO decisions log, read from disk 2026-09-20] was published as a support commitment. **If commitments are decoupled, D2 must be formally superseded in the decisions log rather than quietly not repeated.** The gate record publishes 2026-10-16 and would otherwise carry a commitment the company no longer makes. Owner: **CGO** (record integrity), **CEO** (5.4).
2. **The pay-once tier loses its stated horizon**, and this is the one place decoupling makes the customer story harder rather than easier. §4.4.
3. **The cliff date stays on the pricing screen**, and it is now the *only* forward-looking date Candour publishes about the product. §5.3.

### 4.4 The pay-once tier, honestly restated

**£28.99 is three years of the cost of serving a pay-once buyer** — `(£3.39851 + £2.3060) × 1.694118 = £9.664/year`, times three, rounded to the nearest available Apple price point. Under the old rule that number had a customer-facing justification: you were buying the declared supported life. **Under decoupling, the three years is Candour's accounting horizon and the customer is promised nothing.**

**Is that honest? Only with the disclosure, and the disclosure is not optional [J]:** the pricing screen must state the per-year equivalent (**£9.66**), that access is not time-limited, that **no support period is promised**, and that Article 7.2 governs any ending — 90 days' notice, free export throughout and for 90 days after, code open-sourced where rights allow, closing cost sheet published.

**Two consequences I am not going to soften.**

- **Correction C3.2's asymmetry gets sharper, not softer.** *"The pay-once buyer has pre-paid five years forward and does not participate in any future reduction"* [E, `decisions/2026-09-16-haunt-gate.md` C3.2]. At three years the new-buyer price falls **36.2%** at month 37 (§5.2) and the month-30 buyer gets nothing back. Apple's automatic pass-through reaches subscribers; it does not reach a completed one-off purchase.
- **The tier's name is now harder to defend, not easier.** UX blocks any "lifetime/forever" framing at **B11**, and my own §5.6 judgment was that at short periods the tier should be named for its period — *"Three years, paid up front"*. **Under decoupling that name is unavailable too, because Candour is no longer promising three years of anything.** What is left is a plain label — *"Pay once — £28.99"* — carrying the disclosure above. **This is UX's block and the CEO's naming decision; I hold neither. I raise it because the cost sheet and the pricing screen must describe the same product.** Flag **A4**.

---

## 5. The cliff does not disappear — it moves, and for Haunt it gets steeper

### 5.1 What a cliff is, in one paragraph

At the end of the amortisation period the build leaves the cost base. Nothing about the product changes and nothing about its quality changes; the cost of serving a customer simply falls, and Article 2.1's cap then makes the price follow: *"no product's margin may exceed 30%, regardless of justification."* A standard period does not remove this. **It guarantees it, on a date known at launch, for every product Candour ever ships.**

### 5.2 Haunt at month 37

At `N*` = 11,922, post-cliff `A` = £15,673.16 (fixed operating cost only), so `A/N` falls from £3.3985 to £1.3146:

| Tier | Months 1–36 | **Month 37 onward** | **Cut** | Margin if not cut | Margin after the cut |
|---|---|---|---|---|---|
| Monthly | £0.99 | **£0.69** | **30.3%** | **+54.4%** | 15.70% |
| Quarterly | £2.59 | **£1.69** | 34.8% | — | 14.93% |
| Yearly | £9.89 | **£6.29** | 36.4% | — | 16.07% |
| Pay once | £28.99 | **£18.49** | 36.2% | — | 16.97% |

*Re-derivable: monthly cost of service falls from £7.0125 to £4.9286 a year; £4.9286 × 1.694118 = £8.3497 a year = £0.6958 a month; nearest available Apple price point £0.69. Charged prices are the nearest conventional point per the rounding rule at `cost-sheet-v2.md` §7.2.*

**Against five years the cut is half again as large: 30.3% versus 20.2%.** The reason is arithmetic and worth stating because it is counter-intuitive: a shorter period makes the amortised build a **larger** share of each subscriber's annual cost, so more of that cost falls away on the day it ends.

### 5.3 What that means in practice

1. **It is not optional and it is not a choice.** At an unchanged 99p the realised margin in the first post-cliff year is **+54.4%**, against a cap that admits no justification. The price cut is the Constitution operating as designed.
2. **It lands on existing customers, and Apple makes it irreversible.** *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don't have the option to preserve the higher price for existing subscribers."* [E, [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions), retrieved at primary 2026-09-20]. Article 2.3.3.1 puts *"Price reductions for existing customers"* first in the waterfall's remainder; the store enforces exactly that and offers no mechanism to do otherwise. **This is the rare case where the platform and the constitution want the same thing, and neither can be talked out of it.**
3. **It arrives earlier in a product's acquisition programme.** Haunt's own model needs sustained acquisition throughout — 1,623 new subscribers a month for three years. Month 37 is the day after that programme ends, which is the least bad place for it; at two years it fell in the middle of one.
4. **The date is knowable at launch and must be published then.** It is launch + 36 months, calculable on day one. **It must appear on the pricing screen and on every republished cost sheet.** Under decoupling this is now the only forward-looking date Candour publishes about a product — and it is a commitment to a **price reduction**, which creates no exposure in the harmful direction under CRA s.36 and is worth stating for exactly that reason.
5. **The pay-once buyer does not participate.** §4.4.
6. **Under layering (§3.3), a product in continuous development will not have one cliff but a staircase.** Each expiring layer is a scheduled step down. That is more honest and harder to read, which is why §6 vector 3 exists.

---

## 6. The new gaming vectors, named in Article 9's style

Article 9: *"We name our own loopholes, and publish the numbers that expose each one… If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* A fixed period closes *"declaring a long supported life flatters the cost base"* (Correction C3.3(b)) by removing the choice. **Four vectors replace it. The first two are the ones the CEO named; the third and fourth are mine.**

| # | Loophole | The number that exposes it |
|---|---|---|
| **V1** | **Inflating build hours.** With the period fixed, the only remaining lever on the amortised charge is the numerator. Padding the estimate, or capitalising work that is really maintenance, raises the price for three years and is invisible in a single total | **Capitalised hours per product, published against (a) the gate estimate and (b) hours actually recorded**, restated at every annual republication. Plus **capitalised hours as a percentage of all hours worked on that product that year** — a product in steady state should trend to zero, and one that does not is either genuinely building or mislabelling |
| **V2** | **Restarting the clock with a "v2".** Re-badging a year of maintenance as a new build opens a fresh three-year layer and keeps the amortised charge — and the price — up for ever | **A published layer schedule:** one line per capitalised increment, with hours, ship date, period, amount amortised to date and remaining balance. A real v2 is a discrete layer with a shipped change behind it; a fake one is a layer with no release note. Second number: **the year-on-year change in capitalised share (V1) plotted against the release history** |
| **V3** | **Rolling the layers so the price never actually falls.** Every expiry is offset by a new layer, so the staircase at §5.3(6) never descends. Each step is individually justifiable; the pattern is the problem | **The counterfactual price, published at every republication: what the price would be if no layer had opened since the last one expired.** If the published price never falls below the counterfactual, the product is being continuously re-capitalised and a reader can see it in one column |
| **V4** | **Deferring the start date.** Amortisation that begins late moves the cliff late, and "launch" is a soft enough word to move | **The amortisation start date is the earlier of first sale and public release, published on the first cost sheet and never restated.** Exposing number: **the date of the first pound of revenue, published beside it.** A gap between the two is visible and has to be explained |

**A fifth, carried forward rather than newly created, because a standard period makes it easier not harder:** **splitting one build across two products to capitalise shared work twice.** The exposing number is the one already proposed at `cost-sheet-v2.md` §13 — shared costs allocated equally across live products at each annual republication, with **per-product hours summing to total hours worked**.

**What all five have in common, and why the fix is cheap.** Every one of them is invisible in a total and obvious in a schedule. **The entire defence is one published table per product, of maybe five rows, republished annually alongside the cost sheet Article 3 already requires.** That is the Article 9 instrument working as intended: name the vector, publish the number, and the number costs nothing because it is a by-product of doing the accounting correctly at all.

---

## 7. A product that outlives the period, and one that dies inside it

### 7.1 Outliving it is now the normal case, and that is the main gain

Under v1.2, a product still running after its declared life had a governance problem: the promise had expired, the accounting had expired, and extending either was barred. **Under decoupling there is nothing to expire except the accounting.** The product carries on; its maintenance and support continue to be charged as operating costs of the year they fall in; the price steps down at the cliff and stays down.

**What a long-lived product looks like on a cost sheet from month 37:** a cost base that is entirely operating — for Haunt, £15,673.16 a year plus per-subscriber support — and prices roughly a third lower. **A ten-year Haunt would spend seven of those ten years cheaper than it launched**, and nothing in the Constitution or in Candour's accounting would need to change for that to happen. That is the answer to flaw 1 in its strongest form: honest conservatism now costs a customer nothing beyond the first three years, because there is no promise the conservatism under-sold.

If a genuine new build increment ships in year four, it opens its own layer (§3.3) and the price reflects it — visibly, against the V3 counterfactual.

### 7.2 Dying inside it — the public write-off survives, and matters more

**My recommendation: keep it, unchanged in substance, with a different hook.**

v1.2 ties the write-off to the support commitment's disappearance. With no commitment, the write-off attaches directly to the amortisation schedule: **on discontinuation under Article 7.2, the unamortised balance of every open layer is written off and published in the closing cost sheet that 7.2 already requires** — *"A published closing cost sheet for the product's final period."*

**Why it matters more now, not less.** The support commitment used to discipline the period from the customer's side: declare five years and you owed five years. That discipline has gone. **The write-off is what is left.** A company that capitalises aggressively (V1) or restarts clocks (V2) and then kills the product has to publish the size of what it never recovered, against a period it chose in public. On Haunt:

| Product dies at | Unamortised remainder written off (3-year standard) | (at 5 years, for comparison) |
|---|---|---|
| Month 12 | **£49,688.03 (67%)** | £59,625.63 (80%) |
| Month 18 | **£37,266.02 (50%)** | £52,172.43 (70%) |
| Month 30 | **£12,422.01 (17%)** | £37,266.02 (50%) |
| Month 36 | **£0** | £29,812.82 (40%) |

*Straight-line: £74,532.04 ÷ 36 = £2,070.33 a month.*

**Three things the write-off is not, said plainly so it is not over-read.**

1. **It is not a cost to customers and nothing is recovered from them.** The incidence falls on unrecovered founder labour. Customers of a discontinued product owe nothing and get Article 7.2 — 90 days, free export, open-sourcing where rights allow.
2. **For an unincorporated brand with undrawn labour it has no cash effect.** It is a disclosure, not a payment, and `constitution.md` Article 10 already requires that kind of honesty: *"Where we have not yet done a thing… the relevant rules are commitments about the future."* Calling it a "write-off" without saying this would imply a loss of money that never moved.
3. **It is not a penalty and should not be designed as one.** Killing a product that should be killed is correct under Constitution 5.2. The write-off exists so the *number* is public, not to make the decision expensive.

### 7.3 The one question this proposal does not answer

**A product discontinued at month 30 has customers who paid three-year-amortised prices for 30 months of product.** They were charged on a horizon that did not materialise. Under v1.2 they at least had a published commitment that was broken visibly; under decoupling they have a price that was computed on a convention. **My view [J]: this is correctly handled by Article 7.2 plus the published write-off, and not by a refund** — because the alternative is a proportionate-refund mechanism Candour does not have and cannot build (`cost-sheet-v2.md` §2.6, launch bar **L1**). But it is the sharpest question a sceptical customer can ask about this scheme and it deserves an answer in the decision record rather than silence. Flag **A5**, owner **CGO** with the CEO deciding.

---

## 8. The D2 hours gap — confirmed, and corrected in one respect

**The finding, as I made it this morning.** D2 promises that *"security and defect fixes are made"*. The CTO's nine maintenance rows fund OS-compatibility work, venue-index reconciliation, Expo upgrades, OEM regression chasing, subscription upkeep, regulatory upkeep and accessibility re-verification. **There is no row for security patching, and none for defect fixes that are not OS- or OEM-driven.** [`cost-sheet-v2.md` §4.1, on `products/haunt/subscription-sizing-note.md` §9.2, both read from disk 2026-09-20]

**The question put to me: if the customer-facing promise disappears entirely, does the gap disappear with it?**

> ### Answer: no. Two different things were wrong, and only one of them was about the promise. **Candour still owes the hours.**

**What does disappear: the contractual exposure.** *"Security and defect fixes are made"*, published as pre-contract information about the product's characteristics, is a term of the contract under CRA 2015 s.36(3), and s.36(4) makes it unchangeable without the consumer's express agreement [E, retrieved at primary 2026-09-20, quoted at §1]. **That exposure is created by publishing the sentence, and withdrawing the sentence removes it.** This is a real gain and it is the CEO's to bank — subject to D2 being formally superseded in the decisions log (§4.3(1)) rather than merely not repeated.

**What does not disappear: the costing error.** The gap is in the **cost model**, and a cost model does not care what was promised.

1. **The work happens anyway.** A React Native application with four local native modules and two SDK majors a year has a real dependency-CVE surface [`cost-sheet-v2.md` §4.1; CTO §9.3]. Candour will patch it, because the alternative is shipping known-vulnerable software, which Article 1 does not survive. **Hours that will be worked are costs, and Constitution 2.1's Definitions are explicit that they count whether or not anyone is paid for them:** *"labour valued at a published market benchmark whether or not it is actually paid."*
2. **Omitting them understates the honest price, which is a candour problem pointing the opposite way to the usual one.** Article 9's first row is *"Inflating costs to raise the allowable price"*. This is the mirror: a cost sheet showing a low number because a real line is missing. It is not a route to over-charging — it is a route to a **price rise later**, when the missing line reappears, and to a customer being told the cost went up when in fact it was always there.
3. **Decoupling makes it slightly worse, not better, on one point.** With a five-year promise, the security work had a stated end. With no promise, the honest statement is that security and defect work is funded **for as long as the product is sold**, ending only at discontinuation under 7.2. **That is an open-ended operating cost and it belongs in the fixed annual line at whatever size the CTO sets.**
4. **The legal floor does not move with the promise either**, and I flag rather than opine: CRA 2015's quality and description provisions apply to digital content supplied under a contract regardless of any voluntary support statement. Whether an unpatched vulnerability engages them is a **CGO** determination and, under Constitution 6.1, ultimately a qualified human's. I note only that *"we never promised"* is a weaker answer than it sounds.

**The number, unchanged from this morning** [`cost-sheet-v2.md` §4.1], restated on the three-year base:

| Un-named security / defect-fix line | Annual cost base `A` (3 years) | 99p is honest at |
|---|---|---|
| +0 h/yr (as the CTO's table stands) | £40,517.17 | **11,922** |
| +30 h/yr | £41,498.47 | 12,211 |
| +45 h/yr | £41,989.12 | 12,355 |
| +60 h/yr | £42,479.77 | 12,500 |
| +90 h/yr | £43,461.07 | 12,788 |

> **Confirmed: the gap is a cost gap, it survives the removal of the promise, and it is worth 3–10% on the volume the price needs. What changes is who must fix it: it is no longer a wording question for the CEO. It is a missing row, and only the CTO can size it.** Flag **A2**, owner **CTO**.

---

## 9. My block — restated, with a new lifting condition

> ### BLOCK — maintained, and **this proposal does not lift it.**
>
> **What it is:** no Haunt price may be published under Article 3, and no price set under Constitution 5.4, until build labour has a lawful amortisation basis under the Constitution in force at that time.
>
> **Why decoupling alone does not lift it.** Constitution v1.2, Definitions: *"the amortisation period must equal a **published** support commitment to customers… **Absent a published support commitment, build labour is a first-year operating cost.**"* **Withdrawing the support commitment without amending the Definitions does not produce a three-year amortisation. It produces first-year expensing.** On Haunt that is an annual cost base of **£90,205.20** against £40,517.17 — **2.23× the cost base**, and at `N*` = 11,922 an honest monthly price of **£1.58 rather than 99p** (`C = £90,205.20 ÷ 11,922 + £3.6140 = £11.1803`; `× 1.694118 ÷ 12 = £1.5784`). Every price in §4 is wrong in the direction that over-charges the first year's customers, who are the fewest.
>
> **This is a checklist item failing, not a feeling of unease:** the Definitions name a precondition, the precondition would be unmet, and the consequence is arithmetic.
>
> **What lifts it:** the Article 11 amendment the CGO is drafting being **in force**, with a standard period stated in it. **Any period lifts it** — two, three, five. My recommendation of three years is a recommendation, not part of the block. The block is about the existence of a lawful basis, not about which one.
>
> **What also lifts it, and is worth naming so the block is not a trap:** the CEO deciding **not** to amend, and publishing Haunt's prices on the first-year-expensing basis with the tripled cost base shown on the face of the cost sheet. That is an honest, constitutionally compliant option today. It is a bad commercial one and I recommend against it, but it is available and a block that pretends otherwise is a block being used as leverage.

**Sequencing, stated because it is easy to get wrong:** the amendment must land **before** the price, and the price must land **before** launch. Between now and the amendment there is no valid Haunt price, and any figure quoted in the interim — including every figure in §4 of this document — is conditional on an amendment that has not been made.

---

## 10. Disagreement, recorded once

**My charter: *"Disagreement is a deliverable, not a discourtesy."* This is the one thing in this proposal I would argue about, and having argued it I will proceed either way.**

The CEO's framing is that *"customers remain protected by Article 7.2 — 90 days' notice and free data export on discontinuation — which is the actual protection mechanism."* **I agree that 7.2 is the real protection against the ending. I do not agree that it replaces what is being removed, because the two do different work.**

- **Article 7.2 governs exit.** Notice, export, open-sourcing, a closing cost sheet. It tells a customer what happens **when the product stops**.
- **A published support commitment governed continuation.** It told a customer what happens **while the product runs** — that it would keep working on next year's OS, that defects would be fixed. 7.2 says nothing about that, and a product can decay for years without ever triggering it.

**So the honest accounting of the change is that customers lose a promise about quality-over-time and keep a promise about exit.** Whether that is a *weakening* under Article 11.2 — *"Amendments that weaken a customer-facing or transparency rule must be explicitly labelled 'WEAKENING' in the change log and include the reason"* — is the **CGO's** classification and the **CEO's** decision, and there is a respectable argument that it is not one, because the commitment was an accidental by-product of an accounting clause rather than a rule written to protect anyone. **My position is narrower and is within my scope: whatever label is chosen, the decision record should state in terms that a customer-facing commitment existed in v1.2 and does not exist after this change.** A change log that records only the accounting would be true and incomplete, and Article 9's *"Quietly weakening the rules"* row is written against exactly that gap between true and complete.

**What would make me drop this entirely:** Candour publishing, voluntarily and separately from the accounting, a plain statement of what it maintains while a product is on sale — not dated, not a period, not a term about characteristics, just *"while a product is sold, we keep it running on current OS versions and we fix security defects."* **That costs the hours §8 says are owed anyway, and it gives back the thing being lost without re-creating the freeze.** It is not my drafting to do and I do not block on it. Flag **A1**, owner **CEO** on the **CGO**'s advice.

---

## 11. What would overturn this recommendation, and where I looked

*(Required by `roles/cfo.md`: a negative finding — and a recommendation against alternatives is one — must state what would overturn it and where I looked.)*

**What would move me off three years:**

1. **Evidence on how long software builds actually remain in service.** I have none. The §2.2 inference rests on platform *rewrite cadence*, which is a proxy for code turnover, not a measurement of it. **A credible published study of code-survival rates in maintained mobile applications would change this number in either direction, and I would follow it.**
2. **A Candour product with a materially different shape** — no app store, no annual platform forcing function, a build dominated by durable data work rather than UI. A second product of that kind is a reason to revisit the convention **prospectively** under §3.4, never retrospectively.
3. **A measured Candour maintenance year.** After one real year of Haunt maintenance, the split between "keeping the old build alive" and "replacing it" becomes observable for the first time. **That is the single cheapest evidence that would improve this decision and it does not exist until launch + 12 months.**
4. **A determination that the §3.5 separation fails** — that publishing any period, however labelled, is pre-contract information about the product. Then the whole scheme's legal footing changes and the right answer may be to publish no period at all and expense everything, which is ugly but safe.

**Where I looked:** `constitution.md` v1.2 (Definitions, Articles 2.1, 2.3, 3, 4, 5.4, 7.2, 9, 10, 11); `roles/cfo.md` as amended; `pipeline/evidence-standard.md` v1.1; `decisions/2026-09-16-haunt-gate.md` including Conditions 9.1–9.4, Corrections C1–C4 and the CEO decisions log D1–D3; `products/haunt/cost-sheet-v2.md` in full; `pipeline/templates/` (no template exists for a company-wide accounting proposal — this document follows the cost-sheet template's discipline of itemisation, deviation and change log without claiming to be one). Externally, retrieved at primary this session: CRA 2015 s.36; SI 2008/410 Sch 1 para 22; Apple's upcoming-requirements page; Google Play's target-API requirement; App Store Connect's subscription price-decrease mechanics.

**What I did not do, and it matters:** I did not retrieve any empirical evidence on product lifespans, code survival, or typical amortisation periods actually used by comparable software companies. **The claim that three years approximates useful life is an inference from platform cadence, not a measured fact, and it is the weakest load-bearing claim in this document.** Nothing here should be read as more than that.

---

## 12. Flags

| # | Flag | Owner |
|---|---|---|
| **A1** | Removing the commitment removes a customer-facing protection that Article 7.2 does not replace. The decision record should say so; classification under 11.2 is the CGO's. A voluntary, undated maintenance statement would give it back without re-creating the freeze (§10) | **CEO** on the **CGO**'s advice |
| **A2** | **The security/defect-fix maintenance row is still missing and is still owed.** It survives the removal of D2's promise; worth 3–10% on the volume (§8) | **CTO** to size |
| **A3** | **The §3.5 separation is the load-bearing legal assumption of this whole scheme** — a published accounting convention must not read as a published product characteristic under CRA s.36(3). Constitution 6.1 human review before launch | **CGO**, then qualified human |
| **A4** | The pay-once tier can no longer be named for a period, and its disclosure must carry the per-year equivalent, the absence of any support promise, and Article 7.2 (§4.4) | **UX** (B11); **CEO** on naming |
| **A5** | A product discontinued inside the period leaves customers who paid on a horizon that did not happen. My answer is 7.2 plus the published write-off, not a refund — but the question deserves an answer in the record (§7.3) | **CGO**, CEO decides |
| **A6** | **D2 must be formally superseded in the decisions log, not silently dropped.** The gate record publishes 2026-10-16 and would otherwise carry a commitment Candour no longer makes (§4.3) | **CGO** (record integrity); **CEO** (5.4) |
| **A7** | Correction C3.3(b)'s Article 9 row (*"declaring a long supported life flatters the cost base"*) is **closed by this proposal** and should be replaced in the loophole table by V1–V4 (§6) rather than deleted | **CEO** on the **CGO**'s advice |

**Blocks I do not hold, stated so silence is not read as consent:** I hold no block on the choice of period, on the Article 11 amendment or its wording, on the classification under 11.2, on D2's withdrawal, on the naming of any tier, or on whether Haunt launches at all. **I have argued about several of those above. Arguing is not blocking, and this paragraph is where the difference is labelled.**

---

## Change log

| Date | Change |
|---|---|
| 2026-09-20 | **Created.** Proposes a standard company-wide amortisation period of **three years**, decoupled from any customer-facing support commitment, following the CEO's decision to break the v1.2 Definitions tie. Governs every Candour product; Haunt is the worked example. CRA 2015 s.36, SI 2008/410 Sch 1 para 22, Apple's SDK requirement, Google Play's target-API requirement and App Store Connect's price-decrease mechanics **retrieved at primary this session**. Haunt figures carried from `products/haunt/cost-sheet-v2.md` §§2, 5.1, 7, 10, 12 and re-derived here. **Confirms the D2 security/defect hours gap survives the removal of the promise.** Constitutional wording is the CGO's and is deliberately not drafted here. **Not a decision: the period, the amendment and every price remain Constitution 5.4 matters for the CEO.** |

# Verification — `pipeline/amendment-draft-amortisation.md`

**Seat:** The Skeptic · **Date:** 2026-09-21 · **Status:** Verification report. Not a dissent memo, not a certification, not a decision.

**Why this document exists.** Condition 6 of `decisions/2026-09-16-haunt-gate.md` [E, read from disk 2026-09-21]:

> *"Arithmetic — plus any claim that a named clause of the Constitution or of law requires or forbids something — is re-derived in every future pack by a seat other than its author."*

The amendment draft is not a gate pack, so Constitution 5.3 owes no dissent memo and none is given. What is owed is Condition 6's re-derivation, by a seat other than the CGO, of the draft's claims about **UK statute, secondary legislation, platform policy and the Constitution's own text**. That is what follows.

**There is no template for this.** `pipeline/templates/` holds nine files and none of them is a verification report [E, `pipeline/templates/`, listed from disk 2026-09-21: `cost-sheet.md`, `decision-record.md`, `dissent-memo.md`, `gate-pack.md`, `idea-brief.md`, `proposal.md`, `requirements.md`, `research-brief.md`, `review-pack.md`]. This confirms the draft's own flag F7 and extends it: `pipeline/templates/amendment.md` is owed, and so is a verification stub, because Condition 6 has now been invoked once and will be invoked again.

**What this seat did not do.** The period (three years, D6), the Article 11.2 classification, and the 90-day notice floor (D7) are CEO decisions under Constitution 5.4 and Article 11.1. This report does not reopen them. Where a verification finding bears on one, §7 says so and stops there.

---

## 0. Summary — what verified and what did not

**The legal spine of the amendment is sound.** Every one of the draft's statutory and secondary-legislation quotations was retrieved at primary this session and every one is verbatim accurate. The reading of CRA 2015 s.36 that carries §1.3 — the decisive reason to amend — survives independent retrieval. So does the correction at C6.1 that s.36(4) does not reach price. So does SI 2008/410 Sch 1 para 22. The Constitution citations are accurate to the line, all 23 sampled.

**Three findings are serious, and all three concern the same class of defect: a source quoted accurately but read in part.** None of them touches the statutes. All three touch material destined for **permanent publication** — `CHANGELOG.md` under Article 3's *"Continuously"* row, and `decisions/2026-09-16-haunt-gate.md` on 2026-10-16.

| # | Rank | Finding | Where it lands |
|---|---|---|---|
| **V1** | **Serious** | The claim that Apple requires an annual SDK rebuild is **not supported by the retrieved Apple page**, which states one requirement with one date. The CFO's own second date puts the interval at **24 months**, not 12 | Public change log §16 item 2; and **D6 itself**, which the CEO has already decided |
| **V2** | **Serious** | *"Apple's default notice is sent after the new price has taken effect"* is one clause of a paragraph whose other three sentences say a subscriber gets **27 days' notice before their renewal at the new price**. Read whole, the page does not say what the draft reports | Public change log §16 item 4; C6.2, C6.4, C5.6, §14.3(c) |
| **V3** | **Serious** | The correction of Correction C3.3(b) is, on the Constitution's own usage of *"margin"*, **itself the inversion**. C3.3(b) reads correctly; the draft's counter substitutes *"permitted price"* for *"margin"* | Public change log §16 item 8; §5.3; flag F3 |
| **V4** | Friction | CRA 2015 Sch 2 **paragraph 23 does not carve out paragraph 15**. The draft's *"paragraph 23 permits modification… on reasonable notice"*, and the change log's *"what UK law gives is a right to cancel on reasonable notice"*, both overstate an indicative list | Public change log §16 item 4; §14.3(b); C6.2 |
| **V5** | Friction | *"£9.89 could be quintupled and not approach US$50"* is borderline, not certain, and the page's linked **per-storefront thresholds table was not retrieved** | §14.3(c); C6.2 |
| **V6** | Friction | Edit 6 states the s.36 rule flatly — *"is not changed for customers who have already bought"* — omitting the express-agreement exception the statute contains. As constitutional text this is fine; as an em-dash citation of s.36(3) it misdescribes the section | Constitution text, Edit 6 |
| **V7** | Friction | §14.1 reason 2 characterises Article 2.1's register as uniformly soft, omitting *"no product's margin may exceed 30%, regardless of justification"* | Internal reasoning only |

**A clean pass is a valid finding and here is the honest one:** on the law, this draft is the most carefully sourced document in the repository. Two errors in D7 were caught by the CGO at primary and corrected against the CEO's own text, which is the behaviour Condition 6 exists to produce. The findings below are about **platform evidence and one internal correction**, not about the statute.

---

## 1. Method and sampling

**Exhaustive, not sampled:** every external source cited anywhere in the draft. There are five distinct external URLs and one further URL reached through the CFO's proposal, which the draft relies on for its published rationale. All six were retrieved at primary on 2026-09-21 by this seat, independently of the CGO's retrieval. None is cited here from memory.

**Exhaustive, not sampled:** every line-numbered citation to `constitution.md`. Twenty-six distinct line references appear in the draft; all twenty-six were checked against the file.

**Sampled:** citations to other repository files. The draft carries **128 [E] tags, 2 [K], 38 [I], 22 [J]**. Of the repository-file [E] claims, this seat verified against source: all of `decisions/2026-09-16-haunt-gate.md` claims that carry a legal or constitutional assertion (Conditions 6, 9.2, 9.3, 9.4, 9.7, 9.9; Corrections C1.6, C3.0–C3.6, C4; decisions D2, D4, D5, D6, D7) — that is all load-bearing ones — plus eleven arithmetic figures drawn from `products/haunt/cost-sheet-v2.md`, chosen because the draft's §5.3 correction and §4.2 classification turn on them. `pipeline/governance-review-2026-09.md`, `products/haunt/pricing-ladder-model.md`, `products/haunt/subscription-compliance-note.md` and `roles/cgo.md` were **not** re-verified; the claims drawn from them are not load-bearing for any finding here, and that is stated rather than left as an implication of silence.

**What this seat did not attempt.** No independent legal advice. Constitution 6.1 [E, `constitution.md` line 154]: *"Agent reviews **prepare and flag; they do not certify**… The company never represents an AI compliance opinion as assurance."* Launch bar L1 is unaffected by anything in this report, and F9 in the draft is correct that it now covers three things.

---

## 2. External sources — retrieved at primary, verbatim check

### 2.1 Consumer Rights Act 2015, section 36 — **VERIFIED, exact**

[E, https://www.legislation.gov.uk/ukpga/2015/15/section/36, retrieved by this seat 2026-09-21]

- **Heading:** *"Digital content to be as described."* The draft's use of the heading at §14.3(a) to argue the section is about description rather than price is accurate.
- **s.36(3):** *"Any information that is provided by the trader about the digital content that is information mentioned in paragraph (a), (j) or (k) of Schedule 1 or paragraph (a), (v) or (w) of Schedule 2 (main characteristics, functionality and compatibility) to the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 (SI 2013/3134) is to be treated as included as a term of the contract."* **Verbatim match** to the draft's quotation at §1.3, §14.3(a), C5.3 and C6.1. The parenthetical gloss **is** in the section itself, as the draft asserts.
- **s.36(4):** *"A change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader."* **Verbatim match.**

**Consequence for §1.3, the draft's decisive finding.** The statutory half of the chain verifies. Steps 1 and 2 of the chain remain **inference** from Schedule 2 (a) and (v), correctly tagged [I] by the draft, and the draft's three qualifications (prospective-only reading, who the trader is, agent analysis is not advice) are the right three. **This seat re-derived the chain independently and reaches the same conclusion on the same text.** Per `pipeline/evidence-standard.md` I record the limit of that agreement: re-derivation of an *interpretation* by a second agent seat is not independent, because the second pass inherits the first's reading. What is independently verified is that the words are as quoted; that a dated support statement is *"main characteristics"* information remains a reading, and L1 is where it is confirmed.

### 2.2 SI 2013/3134, Schedules 1 and 2 — **VERIFIED, exact**

[E, https://www.legislation.gov.uk/uksi/2013/3134/schedule/2 and .../schedule/1, both retrieved 2026-09-21]

| Cited as | Retrieved text | Verdict |
|---|---|---|
| Sch 2 heading | *"Information relating to distance and off-premises contracts"* | Match |
| Sch 2 **(a)** | *"the main characteristics of the goods, services or digital content, to the extent appropriate to the medium of communication and to the goods, services or digital content"* | Match. The draft truncates after *"medium of communication"*; the omission is not material |
| Sch 2 **(f)** | *"the total price of the goods, services or digital content inclusive of taxes, or where the nature of the goods, services or digital content is such that the price cannot reasonably be calculated in advance, the manner in which the price is to be calculated"* | **Match, verbatim.** C6.1's central claim — price is (f), and (f) is not among the paragraphs s.36(3) incorporates — **verifies** |
| Sch 2 **(v)** | *"where applicable, the functionality, including applicable technical protection measures, of digital content"* | Match |
| Sch 2 **(w)** | *"where applicable, any relevant compatibility of digital content with hardware and software…"* | Match |
| Sch 1 **(a), (j), (k)** | Identical wording to Sch 2 (a), (v), (w) respectively | The draft says *"materially the same terms"*. **They are in fact identical terms.** The draft understates its own accuracy |

**C6.1 is correct and is the most valuable single correction in the draft.** A CEO decision cited a description provision for a pricing proposition; the CGO retrieved the section, found the error, and corrected it against the CEO's own text rather than working around it. That is Condition 6 operating as designed and it should be said plainly.

### 2.3 Consumer Rights Act 2015, Schedule 2 (the grey list) — **VERIFIED as to text; the draft's gloss on paragraph 23 is over-broad**

[E, https://www.legislation.gov.uk/ukpga/2015/15/schedule/2, retrieved 2026-09-21]

- **Heading:** *"Consumer contract terms which may be regarded as unfair."*
- **Paragraph 11:** *"A term which has the object or effect of enabling the trader to alter the terms of the contract unilaterally without a valid reason which is specified in the contract."* **Verbatim match.**
- **Paragraph 15:** *"A term which has the object or effect of permitting a trader to increase the price of goods, digital content or services without giving the consumer the right to cancel the contract if the final price is too high in relation to the price agreed when the contract was concluded."* **Verbatim match.**
- **Paragraph 23** (Part 2): *"Paragraphs 11 (variation of contract without valid reason), 12 (determination of characteristics of goods etc after consumer bound) and 14 (determination of price after consumer bound) do not include a term under which a trader reserves the right to alter unilaterally the conditions of a contract of indeterminate duration if — (a) the trader is required to inform the consumer with reasonable notice, and (b) the consumer is free to dissolve the contract."*

**FINDING V4 — friction, but it belongs in the change log before publication.**

The draft says at §14.3(b): *"Paragraph 23 permits modification of a contract of indefinite duration where the trader gives reasonable notice and the consumer may terminate."* Two things are imprecise and one of them matters.

1. **Paragraph 23 is a carve-out from paragraphs 11, 12 and 14. Paragraph 15 is not in its list.** So the reasonable-notice-plus-exit safe harbour does **not** extend to a price-increase term. A reader of the change log would take away that notice plus a right to terminate answers paragraph 15. It does not; paragraph 15 asks for a right to **cancel if the final price is too high**, and paragraph 23 says nothing about it. **The draft's own Guard 1 at §14.3(d) already reaches the right practical answer** — the clause must carry the exit, not substitute for it — so the drafted Article 4 bullet is unaffected. It is the *stated reason* that is loose.
2. **The statute says *"indeterminate duration"*, not *"indefinite duration"*.** Trivial in itself; noted because this is a document that quotes statute in a published change log.

**And a third, which is the reason V4 is not merely pedantic.** The change log at §16 item 4 states: *"What UK law gives is a right to **cancel on reasonable notice** (CRA 2015 Sch 2 paras 15 and 23)."* Schedule 2 is an **indicative list of terms which *may* be regarded as unfair** — the heading says so. It does not confer a right. The accurate formulation is that a term permitting a price rise without a right to cancel is on the grey list and may be held unfair, and that a variation term on an indeterminate-duration contract escapes paragraphs 11, 12 and 14 where reasonable notice and a right to dissolve are given. **The draft's conclusion — that the law's protection runs through cancellation rather than consent, and that *"reasonable"* carries no number — survives intact.** What needs changing is one sentence of a document Candour will publish permanently, in which a statement about what UK law *gives* is stronger than the statute retrieved.

**Recommended replacement for the change log sentence, offered so the finding is not merely a complaint:**

> *"UK law's protection here runs through cancellation rather than consent. A term letting a trader raise the price without giving the consumer a right to cancel is on the Consumer Rights Act 2015 Schedule 2 grey list of terms which may be regarded as unfair (paragraph 15); a variation term on a contract of indeterminate duration escapes paragraphs 11, 12 and 14 where the trader gives reasonable notice and the consumer is free to dissolve (paragraph 23). 'Reasonable' carries no number, and paragraph 23 does not reach paragraph 15."*

**One boundary this seat did not test and flags rather than assumes.** CRA 2015 s.64 excludes from the fairness assessment terms specifying the main subject matter or the appropriateness of the price, where transparent and prominent. Whether and how that interacts with a price-*variation* term was **not retrieved** and is not asserted here in either direction. It is an L1 question and is already inside F9's scope.

### 2.4 SI 2008/410, Schedule 1, paragraph 22 — **VERIFIED, exact**

[E, https://www.legislation.gov.uk/uksi/2008/410/schedule/1, retrieved 2026-09-21. The paragraph-level URL used in the draft's chain returns 404; the schedule-level URL resolves.]

> *"(1) Intangible assets must be written off over the useful economic life of the intangible asset. (2) Where in exceptional cases the useful life of intangible assets cannot be reliably estimated, such assets must be written off over a period chosen by the directors of the company. (3) The period referred to in sub-paragraph (2) must not exceed ten years. (4) There must be disclosed in a note to the accounts the period referred to in sub-paragraph (2) and the reasons for choosing that period."*

**Every element the draft and the CFO rely on verifies:** the *"period chosen by the directors"*, the ten-year cap, and the 22(4) duty to disclose the period **and the reasons**. The draft's use of it is also correctly bounded — it is invoked as a **precedent for a structure**, not as a rule binding an unincorporated brand, and the CFO says so explicitly. **The draft's Fix 1 argument is strengthened by retrieval, not weakened:** relying on para 22's shape while omitting its 22(4) disclosure limb would indeed be selective, and the draft is right to insist the reasons go in the public change log.

One phrase the draft does not quote and a reader should have: **22(2) applies *"where in exceptional cases"* the useful life cannot be reliably estimated.** Candour's position — no product shipped, no life measured — is arguably the ordinary case for a pre-revenue company rather than an exceptional one for a going concern. This does not disturb anything, because Candour is not bound by the Regulations today and is borrowing a shape. It is noted because the change log says para 22 *"establishes the shape used here"*, and a reader who retrieves it will see the words *"in exceptional cases"* and wonder whether they were read.

### 2.5 Apple — App Store Connect, pricing for auto-renewable subscriptions

[E, https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions, retrieved 2026-09-21. **Single source by nature** — Apple is the only publisher of Apple's rules, so independence cannot be tested and the draft is right to say so.]

**The consent criteria — VERIFIED, verbatim.** Under the heading *"Consent needed"*:

> *"The subscriber is located in a region that requires consent for any price changes. · The price increase is more than 50% of the current price and the difference in price exceeds approximately US$5 per period for non-annual subscriptions, or US$50 per year for annual subscriptions. · The subscriber experienced a price increase for that subscription within the past 12 months."*

**The no-consent default — VERIFIED, verbatim:** *"If none of the criteria apply, Apple will automatically notify subscribers of the price increase with no additional request for consent."*

**The price-decrease quote relied on at §6.1 T3 and C5.4 — VERIFIED, verbatim:** *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don't have the option to preserve the higher price for existing subscribers."*

---

### **FINDING V2 — serious. The "notice sent after the price takes effect" claim does not survive reading the paragraph whole.**

The draft states this five times, including twice in text destined for publication:

- §14.3(c): *"Apple's default notification in the no-consent case goes out after the new price has taken effect."*
- §16 item 4 (public change log): *"Apple's default is **27 days' notice for a monthly plan**, sent, where no consent is needed, **after the new price has taken effect.**"*
- C5.6 and C6.2 (published 2026-10-16): the same.

**The sentence relied on is really there.** Under *"Consent not needed"*: *"After the new price goes into effect, notifications are sent via email and push notifications — if enabled by the subscriber — 27 or 7 days before the next renewal date."* So this is **not fabrication and not a citation from memory**. The draft quoted a real sentence.

**But three further sentences in the same section, retrieved this session, say the opposite of what the draft reports:**

1. *"If a price increase occurs within the minimum required notice period, subscribers will renew at their existing price for one more billing period and will be notified before the end of their next billing period."*
2. *"Subscribers receive notice of a price change 27 days before the renewal date, and the subscription renews at the new price on the next renewal date."*
3. The page's own timing table: **First email — *"27 days before renewal date."*** · First in-app messaging — *"First app launch after entering notice period."* · Push notification — *"7 days before renewal date, if in-app messaging wasn't viewed."*

**Read whole, the mechanism is:** the price change takes effect **at the storefront** on a date Candour chooses, and each individual subscriber is then notified **27 days before their own renewal**, renewing at the new price only at that renewal. Apple's own phrase *"the minimum required notice period"* confirms there is one and that it is honoured — a subscriber inside it gets another billing period at the old price.

**So the load-bearing proposition is wrong.** *"After the new price goes into effect"* refers to the price change taking effect **in App Store Connect**, not to the subscriber being charged. **No Apple subscriber is charged a higher price before being told.** The draft's framing — that Apple's notice is retrospective and Candour's 90 days is therefore *"genuinely in advance"* where Apple's is not — is the sharpest rhetorical claim in C6.4 (*"The refinement is not redundant. It is doing most of the work."*) and it rests on a partial quotation.

**What survives, and it is most of it.** 90 > 27 remains true. **3.3× remains true** (90 ÷ 27 = 3.33). Apple's consent thresholds remain unreachable at 99p, so D7's second premise remains wrong and C6.2's core correction stands. **What does not survive is the "after the fact" contrast**, and with it the strongest version of C6.4's conclusion. The honest version: Candour's floor is **3.3× the platform's notice period**, not *"advance notice where the platform gives none"*.

**Why this is ranked serious rather than friction.** The tagging is not the issue — the claim is properly tagged [E] with a retrieved link, and the sentence is genuinely on the page. The issue is Article 3. This text publishes permanently, it is a statement about a named third party's policy, that third party publishes the contradicting sentences on the same page, and Candour's whole claim to authority is that its published documents are checkable. **A reader who follows the link will find the three sentences the draft did not quote.** Under Constitution 4's *"claims we cannot substantiate are claims we do not make"* [E, `constitution.md` line 97], this one should be restated before it publishes.

**Falsifiable — what would dissolve this finding.** A retrieved Apple page, or a section of this page not surfaced by this session's retrieval, stating that in the no-consent case a subscriber may be charged the increased price at a renewal occurring less than 27 days after they were notified. **I looked at the whole of the linked page's price-increase section and found the opposite stated three times.** I did not retrieve the linked per-storefront thresholds page or Apple's developer-agreement text.

---

### **FINDING V5 — friction. The annual-tier consent arithmetic is borderline, and a linked source was not retrieved.**

§14.3(c) and C6.2 state: *"£9.89 could be quintupled and not approach $50"* and *"£9.89 a year could be quintupled without approaching US$50."*

Re-derived: quintupling £9.89 gives £49.45; the **difference** — which is what Apple's threshold tests — is **£39.56**. Apple's gate is *"approximately US$50 per year for annual subscriptions."* £39.56 converts to roughly **US$47–50** across a plausible range of rates. **That is at the line, not ten times short of it.** The claim as written is an overstatement of the kind the monthly-tier claim is not: on the monthly tier a 50% rise on 99p is about 50p against a US$5 gate, which genuinely *"cannot"* engage, and the draft's *"roughly ten times out of reach"* is correct there.

**And the page names a source the draft did not retrieve.** Immediately after the threshold, Apple writes: *"(International equivalents for prices not in USD are based on current exchange rates with specific thresholds that are subject to change…)"* and links a per-storefront thresholds table. **The GB threshold is a published number, not an FX conversion, and nobody has opened it.** Under `pipeline/evidence-standard.md` a load-bearing threshold reached by arithmetic on a foreign-currency approximation, where the publisher provides the actual figure one click away, is a citation that stopped one step short.

**Practical effect: small.** The annual-tier limb also requires the rise to exceed 50%, and a quintupling is +400%, so on any realistic Candour price rise the limb does not engage. **The fix is to say what is true — that no price rise Candour would plausibly make reaches these thresholds — rather than to assert an impossibility that the arithmetic does not deliver.** Or retrieve the GB threshold and state it.

---

## 3. **FINDING V1 — serious. The platform-cadence premise, on which a public rationale and a CEO decision both rest**

### 3.1 What is claimed

The change log at §16 item 2, destined for permanent publication under Article 3's *"Continuously"* row [E, `constitution.md` line 79]:

> *"Apple requires every app to be rebuilt against a current SDK annually and Google Play requires an annual target-API bump, so a mobile build is opened, altered and re-shipped three times by month 36…"*

And in the same entry: *"The platform cadence is **annual**."* And at §6.4: *"The retrieved platform evidence establishes a forced-rework cadence of **one year**."*

**The claim also underwrites a decision the CEO has already taken.** D6 [E, `decisions/2026-09-16-haunt-gate.md`, read from disk 2026-09-21]: *"Adopted on the CFO's platform-cadence reasoning, retrieved at primary: Apple requires builds on a current SDK annually and Google Play a current target API annually, so by month 36 the original build has been forced through three replacement passes…"*

### 3.2 What the sources actually say

**Apple** [E, https://developer.apple.com/news/upcoming-requirements/, retrieved by this seat 2026-09-21]:

> *"Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26."* — in force since **28 April 2026**.

**Google** [E, https://developer.android.com/google/play/requirements/target-sdk, retrieved by this seat 2026-09-21]:

> *"New apps and app updates must target Android 16 (API level 36) or higher to be submitted to Google Play…"* — from **31 August 2026**. And: *"Existing apps must target Android 15 (API level 35) or higher to remain available to **new users** on devices running Android OS higher than your app's target API level. Apps that target Android 14 (API level 34) or lower… will only be available on devices running Android OS that are the same or lower than your app's target API level."*

### 3.3 Three things the retrieved evidence does not support

**(a) *"Every app rebuilt annually"* is not what either page says, and the difference is the whole mechanism.**

Apple's requirement binds *"apps **uploaded** to App Store Connect."* An app that ships and is never updated is not forced to rebuild; it is simply not accepted for upload until it is. Google's existing-app rule is not removal either — it is loss of availability **to new users on newer devices**. Neither publisher compels a rewrite of code already on a store.

**Why this matters to the argument rather than to the wording.** The rationale's claim is that *"a mobile build is opened, altered and re-shipped three times by month 36, with each alteration separately charged to customers as maintenance"* — and therefore that *"amortising past that point charges a year-4 customer for code that no longer exists."* That inference requires the rework to be **compelled**, because a product that Candour chooses not to update still has its original build intact and running. **As retrieved, the platforms compel rework only on the condition that you want to ship an update or stay discoverable to new users.** That is a strong commercial compulsion — it is not the mechanical, externally-dated pass the rationale describes. The distinction is exactly the one the draft itself insists on elsewhere: *"a seat's heuristic is not an article"* [E, `pipeline/evidence-standard.md`].

**(b) The word *"annually"* is not established by the Apple page at all, and the CFO's own second date contradicts it.**

The retrieved Apple page shows **one requirement with one date**: in force since 28 April 2026. It does not state a cadence. The cadence claim comes from the CFO's second date — *"the prior requirement, Xcode 15 / iOS 17, ran from 29 April 2024"* [E, `pipeline/amortisation-proposal.md` §2.2, read from disk 2026-09-21] — **which this seat could not verify at that URL, because the page carries current requirements, not a history.**

And taken at face value, **that pair of dates describes a 24-month interval, not a 12-month one.** 29 April 2024 → 28 April 2026 is two years. So on the CFO's own two retrieved data points, Apple's SDK floor moved **once in two years**, not twice.

**Google's is annual** — target-API bumps are dated yearly, and the 31 August 2026 requirement is on that pattern. So one of the two publishers supports an annual cadence and the other, on the evidence retrieved, does not.

**(c) The consequence runs through the draft's own central argument, and it runs in an unexpected direction.**

The draft's §6.4 uses *"the cadence is annual"* to do two pieces of work:

1. To conclude that *"three annual passes is not a reason to prefer three years over two or four"* — i.e. the evidence **brackets** but does not **select**.
2. To dismiss the first clause of the CFO's two-year rejection: *"'shorter than the interval over which the platforms force the work' **does not survive its own evidence**: the platforms force the work **annually**, so a two-year period already contains two forced passes. **There is no principled line in the retrieved evidence between two passes and three.**"*

**If Apple's interval is two years rather than one, point 2 is wrong and the CFO's rejected reason is partly rehabilitated** — a two-year amortisation would contain roughly *one* Apple SDK pass, which is arguably *"shorter than the interval over which the platforms force the work."* Point 1 survives regardless: the evidence still brackets rather than selects, and if anything a two-year Apple cadence brackets **wider**, not narrower.

**This is a re-derivation finding of exactly the class Condition 6 names**, and it runs against this seat's usual direction: the draft's criticism of the CFO is the part that does not hold, while the draft's concession to the CFO is the part that does.

### 3.4 What this does and does not touch

- **It does not touch the period.** Three years is D6, it is the CEO's under 5.4, and nothing here says it is wrong. §7 says what it does bear on.
- **It does not touch the amendment.** No clause of the drafted constitutional text depends on the cadence.
- **It does touch two published documents.** `CHANGELOG.md` item 2 asserts a fact about Apple's requirements that the retrieved Apple page does not support. D6 in the Haunt record, publishing 2026-10-16, asserts the same. Under Article 4's *"claims we cannot substantiate are claims we do not make"*, and under Article 9's method of publishing the number that exposes a vector, the honest form is available and costs nothing.

**Recommended replacement for the change log's factual sentence, offered because a finding without a remedy is half a job:**

> *"Apple does not accept an app uploaded to App Store Connect unless it is built against a current SDK — the present floor, Xcode 26 and the iOS 26 SDK, has applied since 28 April 2026 — and from 31 August 2026 Google Play requires new apps and updates to target Android 16, with apps on older targets losing availability to new users on newer devices. Neither publisher states a cadence on the page retrieved; what they establish is that a mobile product cannot be updated, or stay discoverable, without periodic externally-dated passes over its own build. Those passes are charged to customers separately as maintenance, so a capitalised build stops describing the running code well before a long amortisation period ends. **How much before, nobody has measured, including us.** That is why the period is reviewed at the first product's launch plus 12 months."*

**Falsifiable — what would overturn V1.** A retrieved Apple page stating an annual SDK cadence, or a retrieved Apple requirements history showing a 12-month interval between successive SDK floors, or a retrieved Apple policy compelling rebuild of apps already on the store. **Where I looked:** the `upcoming-requirements` page in full, which is the source the CFO cites and the only one either document cites for the Apple limb. I did not search for an Apple requirements archive, and I say so rather than implying none exists.

---

## 4. **FINDING V3 — serious. The correction of C3.3(b) appears itself to be the inversion**

### 4.1 What is claimed

§5.3 of the draft, and §16 item 8 of the **public** change log:

> *"Both rows owed from the Haunt gate record's Correction C3.3 are discharged here — (a) carried; (b) **corrected, its stated mechanism having run in the wrong direction on its own author's arithmetic**: the harm comes from a **short** period recovered fast, not a long one."*

And in the working at §5.3: *"**A longer life lowers the annual charge, lowers the cost base, and therefore lowers the price a product is permitted to charge**… **Long is the stricter direction, not the flattering one.** … **That sentence corrects C3.3(b) and does not say so.**"*

### 4.2 What C3.3(b) actually says

[E, `decisions/2026-09-16-haunt-gate.md`, C3.3, read from disk 2026-09-21]:

> *"(b) **Declaring a long supported life flatters the cost base**, raising the compliant margin at any subscriber count, and is then discontinued early. The CFO's three-year-versus-five-year band table is the proof of concept."*

### 4.3 Re-derivation

Two clauses, tested separately against `products/haunt/cost-sheet-v2.md` §5.1 [E, read from disk 2026-09-21], the same table the draft reproduces:

| | L = 2 | L = 3 | L = 5 |
|---|---|---|---|
| Annual fixed cost `A` | £52,939.18 | £40,517.17 | £30,579.57 |
| Honest monthly price at N = 8,998 | £1.341 | £1.146 | £0.990 |
| 99p hits the 30% hard cap at | 21,038 | 16,101 | 12,152 |

**Clause 1 — *"declaring a long supported life flatters the cost base."*** A longer life spreads the same build over more years, so the annual cost base **falls**: £52,939 → £40,517 → £30,580. *"Flatters"* means makes look smaller or better. **C3.3(b) is correct.** The draft agrees with this half — *"a longer life lowers the annual charge, lowers the cost base"* — and then treats the whole sentence as inverted.

**Clause 2 — *"raising the compliant margin at any subscriber count."*** This is where the two readings part.

- **C3.3(b)'s reading, which is the Constitution's own usage:** *margin* is a realised ratio of price over cost. Article 2.1 [E, `constitution.md` lines 46–47]: *"Prices target a **margin** of approximately 20% **over published costs**"*; *"no product's **margin** may exceed 30%"*; *"**Margin** is measured per product, per financial year."* **At a fixed price, a smaller cost base yields a larger margin.** At 99p and any given subscriber count, the realised margin at L = 5 exceeds that at L = 3, which exceeds that at L = 2. **The draft's own table proves it:** 99p reaches the 30% cap at **12,152** subscribers on a five-year life and only at **21,038** on a two-year life. The cap bites sooner at L = 5 *because the margin at 99p is higher there at every count*. **C3.3(b) is correct on the Constitution's usage of the word it used.**
- **The draft's reading:** *"the price a product is **permitted** to charge."* On that substitution a longer life gives a lower permitted price, so long is the stricter direction and C3.3(b) is inverted. **But the draft has replaced *margin* with *permitted price*, and the Constitution uses *margin* for the ratio, not for the price ceiling.**

**Verdict: on the text of C3.3(b) and the Constitution's own definition of margin, C3.3(b) reads correctly and the proposed correction is the inversion.** The draft's arithmetic is right; the word it re-derived is not the word C3.3(b) used.

### 4.4 What is genuinely true, and it is a better finding than either version

**The vector C3.3(b) describes exists and is real:** declare a long life → smaller annual cost base → hold the price → bank a larger realised margin → discontinue early, before the customers have had the years they paid the long-amortised price for.

**Where the draft has found something valuable is that the vector does not succeed**, and the reason is precisely the arithmetic it re-derived: Article 2.1's 30% hard cap, which *"admits no justification"*, bites at **fewer** subscribers on a longer life. So the mechanism C3.3(b) names is real and the Constitution already closes it, sooner rather than later. **That is a materially different and more interesting statement than *"its stated mechanism runs in the wrong direction."***

**And the draft's own row 3 is a second, different vector, not a correction of the first.** *"Recovering the build quickly and then discontinuing once it is recovered"* — a **short** period, fully recovered, so an early discontinuation writes off nothing and the closing cost sheet's exposing number reads zero. **Both vectors belong in Article 9. Neither replaces the other.** The draft's row 3 is a genuine addition; what it is not is a correction of C3.3(b).

### 4.5 Why this is ranked serious

Three reasons, in order.

1. **It publishes.** §16 item 8 is public change-log text asserting that a prior record was wrong. Article 11.2's whole architecture rests on the change log being findable and true. **A false correction in a change log is worse than an uncorrected record**, because it teaches a reader that Candour's self-criticism is unreliable in both directions.
2. **It is the exact failure class the evidence standard was rewritten to catch.** `pipeline/evidence-standard.md` [E, read from disk 2026-09-21]: *"one seat redefined a term the Constitution explicitly defines."* The Constitution defines how it uses *margin* across four sentences of Article 2.1. **The draft's re-derivation substitutes a different quantity for it and then reports a contradiction.**
3. **The draft's own flag F3 already says the right thing and the document does not follow it.** F3: *"the CFO should be told rather than corrected around."* But §16 item 8 corrects around anyway, in text ready to publish. **Either the CFO re-derives it first — the draft itself invites exactly that at §5.3, *"the CFO should nonetheless confirm it"* — or it does not go in the change log yet.** This seat's recommendation is the former, and this report is the second re-derivation Condition 6 contemplates.

**Falsifiable — what would dissolve V3.** A showing that *"compliant margin"* in C3.3(b) was used, in context, to mean the price ceiling rather than the realised ratio; or a Constitution or repository definition of *margin* that means the permitted price. **Where I looked:** C3.3 in full and its surrounding C3.0–C3.6; Article 2.1's four uses of *margin*; the Definitions entries for Cost and Profit; `cost-sheet-v2.md` §5.1's table and §5.5's *"Shortening raises prices. Lengthening lowers them."* **That CFO sentence is about prices and is correct. It does not mention margin, and it therefore does not, as the draft asserts, silently correct a sentence about margin.**

---

## 5. Constitution citations — exhaustive check

Every line-numbered citation in the draft — 26 distinct references, single lines and ranges — was checked against `constitution.md` as it stands on disk [E, read 2026-09-21]. **All 26 are accurate: the line number resolves and the quoted words match.** Two further citations used in this report's own reasoning were checked at the same time and also resolve: line 97 (*"claims we cannot substantiate are claims we do not make"*) and line 125 (*"The Skeptic holds no block by design"*).

| Line | Cited for | Verdict |
|---|---|---|
| 19 | Definitions preamble, *"may only change by public amendment"* | Accurate |
| 21 | The **Cost** entry, quoted in full at §1.0 | **Accurate word for word**, including the three bound conditions and the fallback sentence |
| 34 | Article 1.3, *"We say what a product cannot do"* | Accurate |
| 45 | Article 2.1 cost-sheet bullet | Accurate |
| 46 | *"approximately 20%"*, *"a deviation in either direction is a deviation"*, the 30% backstop | Accurate |
| 47 | The cumulative lifetime test, quoted in full at §8.1 | Accurate |
| 48 | *"each product's customers get that product's honest number"* | Accurate |
| 49 | *"annually and at every price change"* | Accurate |
| 63–66 | Article 2.3's waterfall; *"Price reductions for existing customers"* is line 64 | Accurate |
| 74–81 | The Article 3 transparency table | Accurate |
| 79 | *"This constitution and its full change history — Continuously"* | Accurate |
| 80 | Decision records *"Within 30 days of the decision"* | Accurate |
| 89 | Article 4 chapeau, *"Every product must, without exception:"* | Accurate |
| 89–97 | Article 4's seven bullets | Accurate |
| 95 | The export clause | Accurate |
| 117 | Constitution 5.4, *"release to real users"* | Accurate |
| 154 | Constitution 6.1, *"prepare and flag; they do not certify"* | Accurate |
| 173–180 | Article 7.2 | Accurate |
| 192–200 | Article 8 | Accurate |
| 204–218 | Article 9 | Accurate |
| 206 | *"We name our own loopholes, and publish the numbers that expose each one"* | Accurate |
| 224 | Article 10, *"binds through publicity, not law"* | Accurate |
| 225 | *"commitments about the future"* | Accurate |
| 227 | The deliberately-named gap | Accurate |
| 234 | Article 11.1, *"date, diff, and rationale"* | Accurate |
| 235 | Article 11.2, the WEAKENING label | Accurate |

**On the classification, within the limits set for this invocation.** This seat was asked not to reopen the Article 11.2 determination and does not. What it *does* verify, because Condition 6 requires it, is the clause-level claim the determination rests on. Article 11.2 as retrieved reads: *"Amendments that **weaken** a customer-facing or transparency rule must be explicitly labelled 'WEAKENING' in the change log and include the reason."* **The draft's §4.1 analysis of that text — that the trigger is the character of the rule, that there is no reliance element, and that the consequence is a label rather than a prohibition — is accurate on the words.** The application of that test to this amendment is interpretation, and `pipeline/evidence-standard.md` is explicit that a second agent pass does not make interpretation independent. **This seat therefore records that the clause is quoted correctly and that the determination is the CEO's, and declines to add a fourth agent pass over an interpretive question — which is what that standard tells it to do.**

### 5.1 Two smaller notes on the draft's use of the Constitution

**V7 — friction, internal only.** §14.1 reason 2 argues Article 4 is the right home partly because *"Article 2.1's register is deliberately softer — 'target a margin of approximately 20%', 'deviations are permitted' — and a hard floor placed among soft neighbours will be read soft."* **Article 2.1 also contains *"As a hard backstop, no product's margin may exceed 30%, regardless of justification"*, which is the hardest sentence in the article.** The placement conclusion survives on reasons 1, 3 and 4, which are stronger anyway. The characterisation is selective and should not be repeated.

**V6 — friction, but it enters constitutional text.** Edit 6 reads: *"A published support date is a term of the customer's contract — Consumer Rights Act 2015, s.36(3) — and is not changed for customers who have already bought."* The statute retrieved says a change *"is not effective **unless expressly agreed** between the consumer and the trader."* As a **Candour rule** the flat form is fine and stricter than the law; as a sentence whose em-dash presents it as the content of s.36(3), it drops an exception the section contains. **One word fixes it:** *"…and is not **unilaterally** changed for customers who have already bought."* Small, and worth taking because this sentence goes into a document whose only force is that it is accurate in public.

---

## 6. Repository citations — sampling stated

**Verified against source (all load-bearing):** Condition 6; Conditions 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9; Corrections C1.5, C1.6, C3.0–C3.6, C4; decisions D1, D2, D4, D5, D6, D7. All quoted accurately, including the long Condition 9.2 block at §7.1 and the D7 sentence at §14.3.

**Arithmetic re-derived from `products/haunt/cost-sheet-v2.md`** [E, read from disk 2026-09-21] — eleven figures, all reproducing:

| Claim | Source | Re-derivation |
|---|---|---|
| £1.341 / £1.146 / £0.990 at L = 2/3/5 | §5.1 | Matches |
| 21,038 / 16,101 / 12,152 cap counts | §5.1 | Matches |
| £52,939.18 / £40,517.17 / £30,579.57 annual `A` | §5.1 | Matches |
| £4.21 a year, £8.42 over two years | §5.5 | £1.341 − £0.990 = £0.351/mo × 24 = **£8.424**. Matches |
| £44,719 unrecovered on a mid-life shortening; £1.458; 47% | §5.5 | Matches; 1.458 ÷ 0.990 = 1.473 |
| £90,205.20 vs £40,517.17 = **2.23×** | §16.1 | 90,205.20 ÷ 40,517.17 = **2.2263**. Matches |
| +243.4% cumulative margin on a pay-once buyer at year 1 | §8.5 | Matches |
| 20.2% at five years, 30.3% at two/three | §5.4 | 1 − 79/99 = 0.2020; 1 − 69/99 = 0.3030. Matches |
| 99p → 69p at three years | D6 / §5.4 | Consistent with 30.3% |
| 90 ÷ 27 = **3.3×** | §14.3(c) | 3.333. Matches |
| The §8.3 algebra: `R_t ≤ 1.3 C_t` ∀t ⟹ `ΣR ≤ 1.3 ΣC` | §8.3 | **Correct.** The reductio on Reading 2 holds |
| The §8.4 weighted-mean result: cumulative margin ≤ largest annual margin on the same path | §8.4 | **Correct.** `ΣR/ΣC = Σ(C_t · R_t/C_t)/ΣC_t` is a `C`-weighted mean of the yearly ratios, and a weighted mean cannot exceed its largest member |

**The §8 determination on *"the cost of serving them"* re-derives cleanly and this seat endorses the arithmetic.** The reductio at §8.3 is the strongest piece of reasoning in the draft: Reading 2 makes the clause's own closing sentence arithmetically impossible, so Reading 2 is unavailable. That is a textual argument settled by one line of algebra, which is precisely the category the evidence standard says a second seat *can* independently re-derive. **It re-derives.** The §8.4 finding that the clause *is* a live prohibition on tenure-based price divergence — reached against the CFO's own "no-op" suspicion and in the customer's favour — follows from the weighted-mean result and also re-derives.

**Not re-verified, stated rather than implied:** `pipeline/governance-review-2026-09.md` §D and §D3; `products/haunt/pricing-ladder-model.md`; `products/haunt/subscription-compliance-note.md`; `roles/cgo.md`'s blocking-scope quotation; `CHANGELOG.md` v1.2 item 5. None is load-bearing for any finding in this report. Anyone relying on them should retrieve them.

---

## 7. What this bears on, for the policy decisions this seat was told not to reopen

The invocation reserved the period, the classification and the notice floor to the CEO, and asked that verification findings bearing on them be stated rather than swallowed. Three do.

**On the period (D6).** Nothing here says three years is wrong, and this seat has no view on the number. What V1 establishes is that **the reason recorded for it, in both the decision record and the change log, states a fact about Apple that the retrieved Apple page does not support** — and that on the CFO's own pair of dates the Apple interval is two years, not one. Under Article 11.1 the rationale is part of the amendment, and under SI 2008/410 para 22(4) — the precedent Candour has chosen to borrow — the **reasons** are what must be published. **A sound decision resting on a misstated reason is still a decision that publishes a misstatement.** The remedy is a rewritten sentence, not a reopened decision, and one is drafted at §3.4.

There is a second-order point the CEO may want: V1(c) shows the draft's criticism of the CFO's two-year rejection does not hold. **That does not argue for two years** — the write-off asymmetry and the other grounds are untouched — but it removes one of the reasons given for setting two aside, and the draft's own conclusion that the evidence *brackets rather than selects* becomes stronger, not weaker. The committed re-check at launch + 12 months is the right instrument and it is unaffected.

**On the notice floor (D7).** The floor is not disturbed. **The case for it is weaker than the draft states, and still strong.** V2 removes the *"Apple notifies after the fact"* contrast; what remains is 90 days against a platform default of 27, in a legal regime that specifies no number. That is enough to carry C6.4's conclusion in its ordinary form and not enough to carry *"it is doing most of the work"* in the form drafted. V4 and V5 further trim the legal and arithmetic framing without touching the clause. **The drafted Article 4 bullet at Edit 7 is unaffected by all three findings** — its guards were built from paragraph 15 read correctly.

**On the classification (Article 11.2).** Untouched, and deliberately not re-derived beyond the clause check at §5. One observation offered without a recommendation: the draft's determination rests in part on §4.8's account of what v1.2's 2.23× penalty made near-certain, and that multiple re-derives exactly. The classification therefore does not depend on anything V1–V7 disturbs.

---

## 8. What could not be verified, flagged rather than assumed good

Per `pipeline/evidence-standard.md`: *"Unverifiable citations… are flagged as such, never assumed good."*

1. **Apple's prior SDK requirement date, *"29 April 2024."*** Not present on the retrieved `upcoming-requirements` page, which carries current requirements only. **This is the datum on which the entire cadence claim turns.** It is single-origin, from the CFO, and unretrievable at the cited URL.
2. **Apple's per-storefront price-increase thresholds for GB.** Published by Apple at a page linked from the retrieved source; **not opened by any seat**. Relevant to V5.
3. **Whether Apple's *"minimum required notice period"* is stated as a number anywhere.** The page uses the phrase without defining it; the 27-day figure appears in the timing table. Relevant to V2, and the gap runs in the direction of Apple giving *more* protection than the draft credits, not less.
4. **CRA 2015 s.64** and its interaction with a price-variation term. Not retrieved, not asserted, inside F9's L1 scope.
5. **The UK accounting framework that will apply at incorporation.** The draft's T6 correctly declines to assert it from memory and this seat does the same. **[K], low confidence**, that a constitutional convention and a statutory treatment could diverge. Not a finding.
6. **Whether a dated support statement is *"main characteristics"* information under Sch 2 (a)/(v).** Interpretation, not retrieval. Two agent seats now read it the same way; `pipeline/evidence-standard.md` says that agreement is not independent evidence. L1.

---

## 9. Steering in the invocation — reported, as the charter requires

`roles/skeptic.md` [E, read from disk 2026-09-21]: *"If your invocation contains framing ('just confirm…', 'we believe…', 'should be fine'), note the steering attempt in your memo: making nudges visible is part of the job."*

**The invocation was clean of that kind of framing and this should be said first.** No confidence language, no summary of the draft's conclusions, no request to confirm anything, and an express instruction to *"flag anything unverifiable rather than assuming it good."* It supplied file paths and a scope. That is what the charter asks for.

**Two things are nonetheless worth recording, neither in bad faith.**

**(a) The scope was narrowed in advance, and the narrowing sits in tension with the basis given for the invocation.** The invocation rests on Condition 6, which covers *"any claim that a named clause of the Constitution or of law requires or forbids something"*, and then removes *"the classification"* from what may be reopened. **The Article 11.2 classification is itself exactly such a claim** — that a named clause does not require a label here. So the instruction simultaneously invokes a rule and carves out one of its clearest applications.

**In substance this changes nothing, for two independent reasons**, and I record both rather than leaving the objection to look larger than it is. First, the invocation preserved the escape explicitly — *"If verification turns up something that bears on them, say so"* — and I have used it at §7. Second, and more important, `pipeline/evidence-standard.md` reaches the same place on its own: **re-derivation by a second seat does not extend to interpretation**, because *"a second pass inherits the first pass's reading"* and *"a process that answers an interpretive failure by adding agent passes is prescribing more of what already failed."* **So the narrowing asks me to do what the evidence standard already requires.** I verified the clause and declined the interpretation, which is what I would have done unprompted. **Recorded because a scope boundary that happens to be right is still a boundary somebody else drew, and the next invocation may draw one that is not.**

**(b) One characterisation travelled with the file paths:** *"The amendment draft rests on claims of that kind — about UK statute, secondary legislation, platform policy, and the Constitution's own text."* That is a description of where to look, and it is accurate — but it is also the invoking agent telling this seat which classes of claim matter. **It did not narrow my search**; I checked the Constitution citations exhaustively and the arithmetic independently, neither of which that sentence pointed at, and two of my three serious findings are in a class it named last. Noted for completeness, not as a complaint.

**Nothing in the invocation asked this seat to reach a conclusion, and it did not.**

---

## 10. What would overturn this report, and where I looked

*(Universal charter clause: a negative finding carries a block's duty — it must state what would overturn it and where the seat looked.)*

**Overturned in whole or part by any of:**

1. **For V1:** a retrieved Apple source establishing an annual SDK cadence, a requirements history showing a 12-month interval, or a policy compelling rebuild of apps already published. Or a showing that *"forced"* in the rationale was always meant as commercial rather than mechanical compulsion — in which case the wording still needs changing, because the change log does not say so.
2. **For V2:** a retrieved Apple statement that a subscriber in the no-consent case may be charged the new price at a renewal less than 27 days after notification.
3. **For V3:** evidence that *"compliant margin"* in C3.3(b) meant the permitted price rather than the realised ratio; or a Candour definition of *margin* as a price ceiling. The CFO, as C3.3's arithmetic source, is the seat that can settle this and should be asked rather than corrected around — which the draft's own F3 says.
4. **For V4 and V5:** the retrieved GB threshold figure, or a reading of paragraph 23 that does reach paragraph 15.
5. **For the report as a whole:** qualified human legal review under Constitution 6.1, which is launch bar L1 and is where all of this is confirmed or corrected by someone who may actually opine.

**Where I looked.** `constitution.md` in full; `roles/skeptic.md`; `pipeline/evidence-standard.md`; `pipeline/amendment-draft-amortisation.md` in full (all 1,264 lines, §0 through §18); `pipeline/amortisation-proposal.md` §0–§3 and its citation apparatus; `decisions/2026-09-16-haunt-gate.md` in full including Conditions 1–10, Corrections C1–C4 and the CEO decisions log D1–D7; `products/haunt/cost-sheet-v2.md` §5, §8, §14, §16; `pipeline/templates/` listed. **Retrieved at primary this session, independently:** CRA 2015 s.36; CRA 2015 Schedule 2; SI 2013/3134 Schedules 1 and 2; SI 2008/410 Schedule 1; Apple's `upcoming-requirements`; Apple's App Store Connect subscription-pricing help page; Google Play's target-SDK requirements page.

---

## 11. Asks

**This seat prepares and flags; it does not certify, and it holds no block by design** [E, `constitution.md` line 125: *"The Skeptic holds no block by design"*]. Every item below is the CEO's.

1. **Before `CHANGELOG.md` publishes:** rewrite the platform-cadence sentence in §16 item 2 (V1). Replacement drafted at §3.4.
2. **Before `CHANGELOG.md` publishes:** remove or restate *"sent… after the new price has taken effect"* in §16 item 4, and the same phrase at §14.3(c), C5.6 and C6.2 (V2). Keep 3.3×; drop the retrospective-notice contrast.
3. **Before `CHANGELOG.md` publishes:** hold §16 item 8's assertion that C3.3(b) was directionally wrong, **and direct the CFO to re-derive it** (V3). The draft's own F3 asks for this; the change log should not go out ahead of it. If the CFO confirms this seat's reading, the honest entry is that C3.3(b)'s vector is real and Article 2.1's 30% cap already closes it — which is a better Article 9 row than either version.
4. **Before `CHANGELOG.md` publishes:** replace the *"what UK law gives is a right to cancel on reasonable notice"* sentence (V4). Replacement drafted at §2.3.
5. **Retrieve Apple's GB price-increase threshold**, or soften the annual-tier claim to what the arithmetic supports (V5). Cheap either way.
6. **One word in Edit 6:** *"is not **unilaterally** changed"* (V6).
7. **Note that D6's recorded reason** in `decisions/2026-09-16-haunt-gate.md`, publishing 2026-10-16, carries the same Apple claim as the change log and needs the same fix. **This is not a reopening of D6.**
8. **A verification template is owed** alongside `pipeline/templates/amendment.md` (extends F7). Condition 6 has been invoked once and will be again.

**Nothing in this report is a reason to delay the amendment.** The constitutional text at §15 Edits 1–10 is untouched by every finding except one word in Edit 6. What needs work before publication is the **rationale** and two **corrections** — which is to say, the parts a stranger will read to decide whether Candour's published documents can be trusted.

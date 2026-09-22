# Subscription compliance note — Haunt

**Seat:** Chief Governance Officer · **Date:** 2026-09-18
**Commissioned by:** the CEO, following `products/haunt/pricing-ladder-model.md` (CFO, 2026-09-18) §9.2 and §10.4.4.

**Status: this is a compliance determination, not a certification.** Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**. Before launch, anything involving personal data at scale, payments, health information, regulated domains, or **third-party licence terms whose interpretation determines a product's architecture or cost**, receives review by qualified human professionals."* §3 of this note turns on the interpretation of Apple's Schedule 2 against a UK statute, and its answer determines whether Haunt must build a notification surface. **That is the 6.1 case exactly, and §6.3 records it as a launch condition.**

**Template note:** `pipeline/templates/` contains no template for a compliance note (checked this session; the existing `products/haunt/compliance-note.md` set the house shape and this document follows it). The deviation is stated rather than made silently.

**Evidence:** tagged per `pipeline/evidence-standard.md` v1.1. Everything external below was **retrieved this session, 2026-09-18**, at primary where a primary exists. Nothing is cited from memory. Every constitutional or statutory claim quotes the clause it relies on, in the same passage, per that standard's *"Claims about our own rules"* — and where I state my own professional judgment rather than a requirement, I say so, per *"A seat's heuristic is not an article."*

---

## 0. The answers, before the detail

1. **The DMCCA subscription-contracts regime is not in force today, and the twice-flagged claim is resolved — with its date corrected.** Every duty-imposing section of Part 4 Chapter 2 is marked *prospective* on legislation.gov.uk today; the only sections commenced are commenced "for specified purposes", which is the power to make the regulations, not the duty. **No commencement SI has been made for the Chapter.** The date is **not** spring 2027, which is what `compliance-note.md` §4.5 records: the Government stated **January 2027** on 9 August 2026. §1.

2. **The CEO's observation is evidence and it is correct, for the reason he thinks.** He receives no renewal reminders because no reminder duty exists yet. It is not evidence of widespread non-compliance; it is evidence the regime has not commenced. §1.4.

3. **The duty, when it commences, is more likely Candour's than Apple's — and the merchant-of-record fact does not settle it.** Apple Distribution International is Candour's **commissionaire** for the UK, not its reseller: *"'commissionaire' means an agent who purports to act on their own behalf and concludes agreements in their own name but acts on behalf of other persons"*, and Schedule 2 §1.3 makes Candour *"the principal"* [E]. DMCCA s.280 defines a trader as a person acting *"whether acting personally or through another person acting in P's name **or on P's behalf**"* [E]. **The Government expressly declines to resolve the intermediary case**, saying it *"will depend on the facts and specific contractual arrangements in place in each case"* [E, primary]. **Candour must plan on the duty being its own.** §3.

4. **It is not fatal, and it does not require collecting an email address.** This is the finding that dissolves the CFO's largest unpriced item. The Government's own explanation of "durable medium" disqualifies only *"an in-app message/notification **which appears briefly but cannot be retained and revisited**"* [E, primary, Annex B p.48–49]. **A persistent, retainable, revisitable in-app record is not excluded by that sentence** — and StoreKit already gives an offline app the renewal date on-device. **The collision the CFO feared between the reminder duty and Article 1.3/Article 4 does not arise on the primary text.** It arises only on the law-firm gloss, which compresses the Government's sentence into "in-app doesn't count". §4.

5. **The law-firm briefing the CFO relied on adds a word the primary source does not carry, and I checked.** Osborne Clarke's summary is a fair précis but the operative qualifier — *"which appears briefly but cannot be retained and revisited"* — is what makes the whole difference here, and it survives only in the primary. **This is the third artifact to rest on that claim and the first to retrieve it.** §2.3.

6. **The paid-once tier is outside the regime entirely**; the yearly tier attracts a renewal cooling-off right with a proportionate refund that **Candour has no mechanism to pay**; and the two-week trial is the single highest-risk element, because it triggers both a reminder notice and a renewal cooling-off period at the moment of conversion. §5.

7. **Condition 9's replacement is drafted at §7, and the correction entry C3 at §7.3.** Its classification is **neither** of the two the template offers, and I say so rather than forcing it: nothing in Condition 9 was false when written. It is an **amendment recording a later CEO decision under 5.4**, before first publication. The template's classification test has two categories and this is a third; C3.4 records why, and C3.5 drafts the fix to the template itself. **I do not edit the decision record; the CVO applies this.**

8. **On "lifetime": the CVO's test is right and its conclusion does not follow from it.** *"Honest provided the page states plainly what it covers"* is the correct test. The word fails that test, because a disclosure whose job is to reverse the ordinary meaning of the headline word is not plain language — and, unlike the subscription regime, **DMCCA ss.226–227 are in force now** [E]. **Confirmed in principle, corrected in application.** §8.

9. **Yes, the lifetime vector belongs in Article 9's table at the next amendment, and I have found a second one that also belongs.** Declaring a long supported life lowers the annual amortised cost and therefore raises the compliant margin at any given subscriber count — so the support commitment is itself a lever on the price ceiling. Article 9: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* §9.

10. **One escalation is still open and is not settled here**, because it is not this document's question and settling it in passing is how heuristics become law: the reading of *"the cost of serving them"* in Article 2.1's cumulative test, now flagged in three artifacts. §10.2 gives it an owner and a date rather than a fourth flag.

---

## 1. Commencement, retrieved at source

### 1.1 What the Act contains

The subscription-contracts regime is **Part 4, Chapter 2** of the Digital Markets, Competition and Consumers Act 2024, **sections 253–281** [E, [DMCCA 2024, Contents](https://www.legislation.gov.uk/ukpga/2024/13/contents), retrieved 2026-09-18]. There is no dedicated Schedule for the Chapter other than Schedule 23, whose Part 3 carries the prescribed content of reminder notices (referenced at s.259(1)(a)).

### 1.2 What is in force today

The chapter page carries the banner *"This version of this chapter contains provisions that are prospective."* [E, [DMCCA 2024 Part 4 Chapter 2](https://www.legislation.gov.uk/ukpga/2024/13/part/4/chapter/2), retrieved 2026-09-18]. Section by section, as displayed today:

| Section | Subject | Status shown |
|---|---|---|
| 253 Overview · 254 Meaning of "subscription contract" | scope | **Prospective** |
| 255 Excluded contracts · 256 Pre-contract information · 258 Reminder notices · 267 Cancellation: further provision · 277 Power to make further provision | — | **In force for specified purposes** |
| 257, 259, 260, 261, 262, 263, 264, 265, 266, 268–276, 278–281 | every operative duty, right, offence and remedy | **Prospective** |

[E, same page.]

**Read that table correctly, because it is the trap.** "In force for specified purposes" on ss.256, 258 and 277 does **not** mean the pre-contract-information duty or the reminder-notice duty bites. Section 277 is *"Power to make further provision in connection with this Chapter"*; commencing these sections for specified purposes is what lets the Secretary of State **make the regulations** that the whole regime depends on. **Section 254 — the section that defines what a subscription contract even is — is prospective**, and s.275(3) provides: *"This Chapter does not apply in relation to contracts entered into before section 254 comes into force"* [E, [s.275](https://www.legislation.gov.uk/ukpga/2024/13/section/275), retrieved 2026-09-18]. **With s.254 uncommenced, the Chapter applies to no contract at all.** [I]

### 1.3 The commencement instruments

The most recent commencement instrument is **The Digital Markets, Competition and Consumers Act 2024 (Commencement No. 3 and Transitional Provisions) Regulations 2026 (SI 2026/284)**, commencing on **6 April 2026** — and what it commences is **Chapter 4 of Part 4 (alternative dispute resolution)** together with Schedules 25, 26 and 27. **It commences nothing in sections 253–281** [E, [SI 2026/284](https://www.legislation.gov.uk/uksi/2026/284/made), retrieved 2026-09-18].

**So: no commencement regulations for the subscription-contracts Chapter exist. There is no appointed day.** [I, from the above]

### 1.4 The actual date, and the correction it forces

Two Government statements, both retrieved at primary:

- **2 April 2026 — DBT Government Response:** *"We will legislate when parliamentary time allows and we anticipate that the regime will commence in **spring 2027**. We will also publish guidance to support business implementation."* [E, [Government response to consultation on the implementation of the new subscription contracts regime](https://www.gov.uk/government/consultations/consultation-on-the-implementation-of-the-new-subscription-contracts-regime/outcome/government-response-to-consultation-on-the-implementation-of-the-new-subscription-contracts-regime-web-accessible-version) and the [PDF version](https://assets.publishing.service.gov.uk/media/69cce372a2e82c1bd822d7de/government-response-to-consultation-on-the-implementation-of-the-new-subscription-contracts-regime.pdf), published 02/04/2026, p.18; both retrieved 2026-09-18]

- **9 August 2026 — GOV.UK press release:** *"New rules will now come into force in **January 2027**, in time for when customers often start new subscriptions for the year ahead."* The same release states that *"businesses will need to provide clearer up-front information, regular reminders and a much easier exit to contracts"* and that *"A new 14-day cooling-off period will also let consumers cancel after a trial or long-term contract renews."* [E, [PM starts roll out of 'everyday fixes' on the cost of living](https://www.gov.uk/government/news/pm-starts-roll-out-of-everyday-fixes-on-the-cost-of-living-ending-rip-off-discounts-and-subscription-traps), GOV.UK, 9 August 2026, retrieved 2026-09-18]

> **The position as of 2026-09-18, stated as the gate needs it:**
>
> - **In force today:** nothing that imposes a subscription duty on anyone. Five sections are commenced for specified purposes only — essentially the power to make regulations.
> - **Not in force:** every duty, every right, every remedy, every offence in ss.253–281, including s.254 itself, without which the Chapter applies to no contract.
> - **The date:** **January 2027** is the Government's stated intention, announced 9 August 2026, superseding the "spring 2027" in the April Government Response. **It is not a legal date.** No commencement SI has been made, and the secondary legislation the regime depends on — the regulations under s.277 that carry the durable-medium requirement — **has not been published**. [I]

**`products/haunt/compliance-note.md` §4.5 is corrected in two respects.** Its conclusion — that the regime does not bite — was and is right. Its date was right when written and is now stale by four months in the *unfavourable* direction, and one of its two stated grounds is now gone: **Haunt is no longer a one-off purchase.** The correction banner owed is at §10.4.

### 1.5 The CEO's observation, treated as evidence

The CEO reports that he receives no renewal reminders for subscriptions he currently holds [E — the CEO's own report to this seat, 2026-09-18; primary observation, single observer, unquantified]. He is right that this is diagnostic, and it discriminates exactly as he supposed:

- **Consistent with:** the regime not being in force. ✔ Confirmed at source above.
- **Inconsistent with:** the regime being in force and complied with. ✔
- **Also consistent with:** the regime being in force and widely breached — which §1.2–1.3 now rule out independently. [I]

**What Apple actually sends today is a *receipt*, after the charge, and the subscriber can switch it off.** The setting is *"Receive Renewal Receipts"* in Apple Account → Subscriptions [E, **secondary, two sources, plausibly one origin** — [9to5Mac](https://9to5mac.com/2020/02/11/you-can-now-opt-out-of-receiving-subscription-renewal-emails-from-apple/), [Macworld](https://www.macworld.com/article/233837/how-to-stop-receiving-subscription-renewal-emails-from-apple.html), both retrieved 2026-09-18; **flagged: I could not retrieve an Apple-published page describing an advance renewal reminder for ordinary renewals or for trial endings, and I looked** — see §10.3]. A receipt sent *after* the money has gone, which the consumer may disable, is not a reminder notice in the s.258 sense, which is given *"in advance of the last cancellation date"* (s.259(4)) [E]. **The CEO's experience and Apple's documented behaviour agree.** [I]

**This is the whole of the answer to the escalation.** The claim that anchored `compliance-note.md` §4.5 and then `pricing-ladder-model.md` §9.2 is now resolved at source, its date corrected, and it may anchor this third artifact.

---

## 2. The escalation, formally closed

### 2.1 What the rule required

`pipeline/evidence-standard.md` v1.1, *Claims about our own rules*: *"**Twice-flagged is escalated.** A load-bearing claim flagged as unverified on two separate occasions must be resolved, or formally accepted in writing by the CEO, before it may anchor a third artifact. Flagging is otherwise free and infinite, which is how a known gap becomes furniture."*

The two prior flags, quoted rather than characterised:

1. **`products/haunt/compliance-note.md` §4.5** (CGO, 2026-09-16): *"the DMCCA subscription-contracts regime does not bite, both because Haunt is a one-off purchase and because commencement has been pushed to **spring 2027**"* — tagged *"[E, secondary … **single underlying origin (DBT consultation response, 2 April 2026), not retrieved at source**]"*.
2. **`products/haunt/pricing-ladder-model.md` §9.2** (CFO, 2026-09-18): the durable-medium requirement, tagged *"**secondary, law-firm briefing, single underlying origin (the DBT consultation response), not retrieved at source — flagged**"*.

**Same underlying origin, flagged twice, by two seats.** The escalation was owed and it is discharged here: **resolved, not accepted.**

### 2.2 What the retrieval changed

| Claim as it stood | Status after retrieval at source |
|---|---|
| Regime does not bite because Haunt is a one-off | **Ground gone.** The CEO's ladder is a subscription contract on s.254(2) and (3) both. §5.1 |
| Regime does not bite because commencement is spring 2027 | **Conclusion stands; date wrong.** Nothing is in force; the stated date is **January 2027**. §1.4 |
| Reminder notices must be on a durable medium | **Confirmed — and it is not yet law.** It is a stated legislative intention for regulations under s.277 that have not been made. §4.1 |
| Email/SMS/WhatsApp qualify; in-app notifications do not | **Materially incomplete.** The Government's qualifier is *"which appears briefly but cannot be retained and revisited"*. §2.3 |
| Discharging the duty would require collecting an email address | **Not established, and on the primary text, not required.** §4.2 |

### 2.3 The gloss that did the damage, named precisely

The CFO's source characterised the Government's position as: *"email, SMS, and WhatsApp qualify as durable media, but fleeting in-app notifications that cannot be retained do not"* [E, [Osborne Clarke](https://www.osborneclarke.com/insights/uk-digital-markets-competition-and-consumers-act-subscription-contracts-regime-take-shape), as quoted at `pricing-ladder-model.md` §9.2, read from disk 2026-09-18]. **That is an accurate précis.** The problem is what happened to it downstream: by §9.2(a) it had become *"Haunt has no server, no account, and no email address… Discharging a reminder-notice duty would require Candour to **collect an email address**."* [E, same file]

The Government's actual sentence, retrieved at primary:

> *"Section 280 of the DMCCA defines 'durable medium' as 'paper, email or any other medium that — (a) allows information to be addressed personally to the consumer, (b) enables the consumer to store information in a way accessible for future reference for a period that is long enough for the purposes of the information, and (c) allows the unchanged reproduction of information stored'. As such, we expect a written letter, email, SMS or WhatsApp message would qualify, as long as the consumer could retain and retrieve it. **However, an in-app message/notification which appears briefly but cannot be retained and revisited would not meet this criteria.**"*
>
> [E, [Annex B: summary of question responses](https://assets.publishing.service.gov.uk/media/69cd2ce7b5210036050bc67c/annex-b-summary-of-question-responses.pdf), DBT, published 02/04/2026, Question 23, pp.48–49; retrieved and text-extracted 2026-09-18]

**The list is expectational and open (*"we expect… would qualify"*), and the exclusion is conditional, not categorical.** What is excluded is the ephemeral notification. What is not excluded — and what the whole of Haunt's answer turns on — is a notice that **can** be retained and revisited. [I]

**Two things I want on the record about how this nearly went wrong**, because the September 2026 failures this company has already documented were all of this shape:

- **Neither prior artifact retrieved the primary, and the primary was free.** The Government Response PDF and Annex B are both open documents on GOV.UK under the Open Government Licence. The evidence standard's sentence — *"The source in every case was a file in this repository, free to retrieve"* — generalises: here it was a file on a public website.
- **The compression happened across two documents, not inside one.** §4.5 flagged its source honestly. §9.2 quoted §4.5 honestly. The loss of *"which appears briefly"* happened in the step from a quoted précis to an inferred consequence, and no single seat did anything careless. **A chain of honest citations can still lose the load-bearing word**, and the only defence is the rule that was applied here: retrieve at source before the third artifact.

---

## 3. Whose duties are they? The merchant-of-record answer is the wrong answer to this question

### 3.1 Where the statute puts the duty

**Section 254(1):** *"For the purposes of this Chapter, a subscription contract is a contract **between a trader and a consumer** — (a) for the supply of goods, services or digital content by the trader to the consumer in exchange for payment by the consumer…"* [E, [s.254](https://www.legislation.gov.uk/ukpga/2024/13/section/254), retrieved 2026-09-18]

**Section 258, the reminder duty, opens:** *"Where **a trader enters into a subscription contract with a consumer** that does not include a concessionary period, **the trader must give to the consumer a notice**…"* [E, [s.258](https://www.legislation.gov.uk/ukpga/2024/13/section/258), retrieved 2026-09-18]

**Section 280, the definition that decides it:** *"**'trader'** means a person ('P') acting for purposes relating to P's business, **whether acting personally or through another person acting in P's name or on P's behalf**."* [E, [s.280](https://www.legislation.gov.uk/ukpga/2024/13/section/280), retrieved 2026-09-18]

The final limb is not decorative. It is the standard UK consumer-law formulation and it exists precisely to stop a principal escaping trader status by routing the sale through an intermediary. **Its disjunction — "in P's name **or** on P's behalf" — is drafted to catch the case where the intermediary acts in its own name.** [I, from the quoted text]

### 3.2 What Apple actually is, in the UK, for Haunt

`compliance-note.md` §4.1 established that Apple Distribution International Ltd. is **merchant of record** for UK users and concluded *"the consumer's contract of sale is with Apple, not with Candour"* [E, `products/haunt/compliance-note.md` §4.1, read from disk 2026-09-18, citing [Apple Media Services Terms (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html)]. **That finding is correct and it is about tax and payment. It does not answer the trader question, and this note establishes why.**

Three retrievals, all at primary this session:

**(a) Apple's consumer-facing terms say Apple is the developer's agent.** *"App licenses are provided to you by Apple or a third party developer ('App Provider'). Apple acts as an agent for App Providers in operating the App Store."* [E, [Apple Media Services Terms and Conditions (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html), retrieved 2026-09-18]

**(b) Apple's developer agreement puts the UK in the commissionaire column, and defines the word.** Exhibit A, section 2, *"Apple as Commissionaire"*: *"You appoint Apple Distribution International Ltd. as **Your commissionaire** for the marketing and End User download of the Licensed and Custom Applications by End Users located in the following regions… For the purposes of this Agreement, **'commissionaire' means an agent who purports to act on their own behalf and concludes agreements in their own name but acts on behalf of other persons**, as generally recognised in many Civil Law legal systems."* **"United Kingdom" appears in that list.** [E, [Exhibits to Schedule 2 and 3 (English, UK), 21 August 2025](https://developer.apple.com/support/downloads/terms/exhibits/Exhibits-to-Schedule-2-and-3-20250821-English-UK.pdf), Exhibit A §§1–2; retrieved and text-extracted 2026-09-18]

**(c) Schedule 2 names Candour the principal and makes Candour solely responsible.** *"The parties acknowledge and agree that their relationship under this Schedule 2 is, and shall be, that of **principal and agent, or principal and commissionaire**, as the case may be… and that **You, as principal, are, and shall be, solely responsible for any and all claims and liabilities involving or relating to, the Licensed Applications**."* (§1.3) And, directly on point: *"To the extent You promote and offer for sale **auto-renewing subscriptions**, within or outside of Your Licensed Application, **You must do so in compliance with all legal and regulatory requirements**."* (§3.10) [E, [Schedule 2 and 3 to the Apple Developer Program License Agreement (English)](https://developer.apple.com/support/downloads/terms/schedules/Schedule-2-and-3-English.pdf); retrieved and text-extracted 2026-09-18]

> **Finding.** Apple is not Haunt's reseller. Apple is Haunt's **commissionaire**: it concludes the agreement in its own name, **on Candour's behalf**, with Candour as principal — and its own developer agreement expressly assigns regulatory compliance for auto-renewing subscriptions to the developer. [I, from (a), (b) and (c)]

**That is the opposite of the direction §4.1's finding was travelling in when applied to subscriptions**, and the error would have been an easy one: "merchant of record" sounds like it settles who the seller is, and in tax terms it does. In agency terms it does not. **I record that this seat wrote §4.1 and that this note narrows its reach.**

### 3.3 The Government has looked at this question and declined to answer it

> *"**Third party responsibilities:** Broadly speaking, the duties imposed on traders under Chapter 2, Part 4 are on **the trader with whom the consumer enters a subscription contract** for the supply of particular goods, services or digital content. However, we appreciate that it is common for businesses to enter into agreements with other businesses in relation to consumer-facing matters e.g. a third-party may provide payment or communication services. **Whether that position is affected by arrangements between the trader and another business will depend on the facts and specific contractual arrangements in place in each case.**"*
>
> [E, [Annex B: summary of question responses](https://assets.publishing.service.gov.uk/media/69cd2ce7b5210036050bc67c/annex-b-summary-of-question-responses.pdf), DBT, Question 23, p.48; retrieved 2026-09-18. The Government adds that guidance *"will cover commonly raised points"* including this one — **that guidance is unpublished.**]

**This is as close to "we are not going to tell you" as a government response gets, and it is the honest answer to give**, because the answer genuinely does turn on the contract. [J]

### 3.4 The determination, with both readings stated

**Reading A — the duty is Candour's.** Candour is a "trader" on s.280 because Apple acts on Candour's behalf. Candour is the principal under Schedule 2 §1.3, the supplier of the digital content under s.254(1)(a), and the party Apple's own consumer terms identify as the App Provider from whom the licence comes. Schedule 2 §3.10 assigns regulatory compliance for auto-renewing subscriptions to Candour in terms. On this reading Candour must give the reminder notices.

**Reading B — the duty is Apple's.** Section 258 attaches to *"a trader [who] **enters into** a subscription contract with a consumer"*, and a commissionaire, by the definition Apple itself supplies, *"concludes agreements in their own name"*. The consumer's counterparty on the face of the transaction is Apple Distribution International; the consumer never contracts with Candour by name; and Apple, not Candour, controls billing, renewal, cancellation and refund.

**Which one I hold, and how firmly.** [J, moderate confidence] **Reading A.** Three reasons, in order of weight: (1) s.280's definition of trader is drafted with the disjunction that covers exactly this arrangement, and a construction on which a developer escapes every duty by appointing a commissionaire would gut the Chapter for the entire app economy; (2) Schedule 2 §3.10 is Apple contracting *out* of that responsibility and *into* Candour, and while a contract between businesses cannot reassign a statutory duty, the Government's sentence at §3.3 makes the contractual arrangements relevant to where the duty sits; (3) Reading B leaves a consumer with a statutory right and nobody to exercise it against, which is not how the Chapter is built.

**What I will not do is present that as the answer.** It is a view on an unsettled question of statutory construction, about an Act that is not in force, whose implementing regulations are unmade and whose guidance is unpublished. **Under `roles/cgo.md` I prepare and flag. Under Constitution 6.1 this is the named case: *"third-party licence terms whose interpretation determines a product's architecture or cost"*, which "receives review by qualified human professionals" before launch.** §6.3 carries it as a condition.

> **Operationally, the two readings converge and that is the useful part.** On Reading A Candour owes the notices. On Reading B Candour owes nothing — but Apple demonstrably does not send advance renewal reminders today (§1.5), so a Candour that assumed Reading B would ship a product on which **nobody** discharges the duty. **Both readings therefore point to the same build: Candour implements the notices.** The determination decides whether that is a legal obligation or a voluntary one; it does not change what gets built. [I]

---

## 4. If the duty is Candour's: the minimum compliant implementation, and whether the collision is real

This section runs on the assumption that Reading A is right, because that is the assumption a build must be planned on. **Where it lands: survivable with a stated design, and the design collects nothing.**

### 4.1 What is actually required, and what is merely intended

**On the face of the Act** (all prospective, none in force):

- **s.258** — a reminder notice *"in respect of each renewal payment that relates to the end of a relevant six-month period"*, and, where the contract includes a **concessionary period**, in respect of the **first renewal payment** as well [E, s.258].
- **s.259** — the notice carries *"the information set out in Part 3 of Schedule 23"*, given *"in such a way that the information… is more prominent than any other information given to the consumer at the same time"*, within a period the trader itself specifies in its key pre-contract information, which must be *"a period in advance of the last cancellation date which is reasonable for"* informing the consumer and enabling cancellation [E, [s.259](https://www.legislation.gov.uk/ukpga/2024/13/section/259), retrieved 2026-09-18].
- **s.257(9)** — where full pre-contract information was not given before the contract, *"the trader must give the consumer that information **in writing on a durable medium** as soon as reasonably practicable after the contract has been entered into"* [E, [s.257](https://www.legislation.gov.uk/ukpga/2024/13/section/257), retrieved 2026-09-18].

> **Note what is and is not on the face of the Act.** **s.259 does not itself require a reminder notice to be on a durable medium.** The durable-medium requirement for reminder notices is a **stated intention for regulations under s.277(1)(a)** — *"We will legislate to require that: reminder notices must be given to consumers in writing on a durable medium"* [E, Annex B Q23, p.47]. **Those regulations do not exist.** Section 257(9) is the only durable-medium duty currently written into the statute itself, and it is prospective too. [I]

**Why that matters for sequencing, and it is not an invitation to gamble:** the requirement Candour must design for is knowable in substance and unknowable in detail until the s.277 regulations and the accompanying guidance are published. Both are promised before commencement. [I]

### 4.2 Does a persistent in-app notice satisfy "durable medium"?

**The definition, quoted in full** (s.280): *"'durable medium' means paper, email or any other medium that — (a) allows information to be addressed personally to the consumer, (b) enables the consumer to store information in a way accessible for future reference for a period that is long enough for the purposes of the information, and (c) allows the unchanged reproduction of information stored"* [E, s.280].

**The Government's gloss** excludes *"an in-app message/notification **which appears briefly but cannot be retained and revisited**"* [E, Annex B Q23, pp.48–49, quoted in full at §2.3].

Tested limb by limb against a **persistent in-app notice record** — a durable entry written to the device's own store, listed in a permanent in-app "Notices" screen, not dismissible into nothing, exportable with everything else:

| Limb | Persistent in-app record | Confidence |
|---|---|---|
| (a) *"addressed personally to the consumer"* | The app instance is bound to one person's device and one Apple subscription; the notice names their plan, their renewal date and their price. **Arguable both ways** — the phrase is ordinarily read as requiring the trader to direct the message *to* an identified individual, and here the trader directs it to a device rather than a person. [J] | **Weakest limb.** Moderate |
| (b) *"store information… accessible for future reference for a period long enough"* | Satisfied plainly: the record persists on device, indefinitely, with no expiry. | High |
| (c) *"allows the unchanged reproduction of information stored"* | Satisfied plainly, and Haunt's export requirement (Condition 8.3) already delivers it in machine-readable form. | High |

> **Determination:** on the primary text and the Government's own qualifier, **a retainable, revisitable in-app notice is not excluded, and limb (a) is the only one seriously in doubt.** The CFO's conclusion that the duty *"would require Candour to collect an email address"* is **not supported by the source it rests on**, and I record that this seat's own §4.5 was one of the two artifacts that carried the unverified claim there. [I]

**Two hedges I am not going to bury.** [J] First, limb (a) is genuinely open and the guidance may close it against this design — the Government's list of things it *expects* to qualify is a list of **addressed** channels. Second, **belt-and-braces is available and cheap**: iOS local notifications are addressed to the device's owner and can be paired with the persistent record, so the user receives a notification *and* has something retainable to revisit. **Neither requires an email address, an account, a server, or a single byte leaving the device.**

### 4.3 The minimum compliant implementation

In the order a build should take it, cheapest and most certain first. All of it is local; none of it collects anything.

| # | Requirement | Implementation | Collects? | Sizing |
|---|---|---|---|---|
| 1 | **Pre-contract information (ss.256–257)** | App Store description + the StoreKit purchase sheet + a first-run disclosure screen, which **Condition 8.1 already requires** for an unrelated reason | Nothing | Near-zero; largely already owed |
| 2 | **Easy and online exit (s.260)** | Apple's own Manage Subscriptions, deep-linked from a plainly-labelled in-app control | Nothing | Hours |
| 3 | **Persistent notices surface** | An in-app "Notices" screen: append-only, never auto-clearing, included in export | Nothing | The real increment; CTO to size |
| 4 | **Reminder notices (ss.258–259)** | Written to (3) ahead of each qualifying renewal, plus a local notification, from renewal dates read on-device | Nothing | Scheduling logic |
| 5 | **Cooling-off notice at trial end (s.266)** | Same surface, triggered by the first renewal payment | Nothing | Shares (3) and (4) |
| 6 | **Belt-and-braces, optional** | Offer — never require — an email address purely for notices, off by default | **Would collect.** See §4.4 | Do not build unless guidance forces it |

**The dependency this rests on, and I flag it as unverified rather than asserting it.** Items 3–5 require the app to know its own renewal dates **without a server**. My understanding is that StoreKit 2 exposes current entitlement and renewal information locally on device [**[K], high confidence, not retrieved this session**]. **This is load-bearing for the whole of §4 and it is the CTO's to confirm, not mine to assume** — it is listed at §10.3 and carried as a condition at §6.3. If it is wrong, item 6 becomes the only route and §4.4's analysis governs.

### 4.4 The collision, stated precisely — and why it does not arise

The CFO's framing is right about what would be at stake if the duty could only be discharged by email:

> *"Discharging a reminder-notice duty would require Candour to collect an email address — a new personal-data collection on a product whose entire proposition is that it collects nothing, which would make Candour a controller, would make the ICO fee certainly rather than probably owed, and would need a new build, a new privacy surface and a new Article 4 assessment."* [E, `pricing-ladder-model.md` §9.2(a)]

**Every limb of that is correct, and the premise is wrong.** [I] For the record, had the premise held, here is what it would have cost constitutionally, because the CEO is entitled to see the counterfactual priced rather than waved away:

- **Article 1.3** — *"Honest by default. Pricing, capability, and limitations are stated plainly. We say what a product cannot do."* Candour's substantiated marketing claim is the one corrected three times at gate (decision record, O4). Collecting an email address would not falsify it if disclosed, but it would move Haunt from "collects nothing" to "collects one thing, for this reason", and **every published claim would need re-cutting.**
- **Article 4** — *"Collect the minimum data necessary, state why, and delete it when no longer needed."* An email collected **solely to discharge a statutory notice duty** would satisfy "minimum" and "state why" comfortably; "delete when no longer needed" means deletion on cancellation. **Article 4 would not forbid it.** [I] Recording that plainly matters, because the September 2026 failures this company documents were all cases of a seat reading a prohibition into a clause that does not contain one, and I am not going to add a fifth.
- **UK GDPR** — Candour would become a controller of an email address and a subscription status. `compliance-note.md` §3.3 already prices the ICO fee as probable; it would become certain.
- **The real cost is not any of those. It is that the product's single strongest differentiator would be gone**, and the CFO's own arithmetic says Haunt has no acquisition channel to spare. [J]

> **Finding on the CEO's question: not fatal to the subscription ladder; survivable with a stated design; and on the primary text most likely not a duty that requires any collection at all.** The stated design is §4.3 items 1–5. **Item 6 is the fallback and it should not be built now.**

**What would overturn this finding** (charter clause: *"Negative findings carry the same duty as blocks"* — this is a positive finding, but it clears a path and the same duty applies): [I]

1. **The s.277 regulations or the DBT guidance defining "durable medium" so as to require an addressed off-device channel.** This is the live one. Both are promised before commencement (January 2027) and neither is published. **This must be re-checked when they are, and that is a dated task, not a standing intention** — §6.3.
2. **The CTO finding that renewal dates are not available on-device without a server.** §4.3.
3. **A determination under Reading B that the duty is Apple's** — which would remove the obligation but not the design, per §3.4.

Where I looked for a contrary answer: the Act ss.254–281 at source; the Government Response in full (both the web version and the PDF, text-extracted); **Annex B in full, text-extracted and searched for "durable medium", "in-app", "SMS", "WhatsApp" and "email"**; Apple's UK consumer terms; Apple's Schedule 2 and its UK Exhibits. **The phrase "in-app" occurs in Annex B in exactly one operative place and it is the sentence quoted at §2.3.**

---

## 5. What else the ladder revives that the one-off did not

The CEO asked for this explicitly, and it is the part of §9.2 the CFO could not do from a pricing seat. Tier by tier, against the CFO's recommended ladder (99p monthly · £2.79 quarterly · £10.90 yearly · £59.40 paid once · two-week full-feature trial).

### 5.1 Which tiers are in scope at all

**Section 254(2)** catches a contract providing for *"an automatically recurring, or continuing, supply"* with the consumer automatically incurring *"recurring liabilities"* and a right to end it. **Section 254(3)** independently catches *"a supply… free of charge, or at a rate specified in the contract… for a period specified in the contract"* followed by automatic liability for payment [E, s.254].

| Tier | In the regime? | Why |
|---|---|---|
| Monthly 99p | **Yes** — s.254(2) | Recurring liability, terminable |
| Quarterly £2.79 | **Yes** — s.254(2) | Same |
| Yearly £10.90 | **Yes** — s.254(2) | Same |
| **Two-week free trial → any paid tier** | **Yes — s.254(3) as well as (2)** | This is the paradigm case the subsection is written for |
| **Paid-once £59.40** | **No** | No recurring or continuing liability and nothing to renew. It is a one-off digital-content purchase, governed by CRA 2015 and the CCRs as today. |

> **The paid-once tier is outside the subscription regime entirely.** That is a real and unremarked property of the CFO's ladder: the tier he recommends renaming is also the only tier that carries none of this. [I] **It is not a reason to push customers onto it** — see the Article 9 vector at §9.1, which is the same manoeuvre wearing a different hat.

### 5.2 Cooling-off — the trial is the exposure, not the price

**Section 265(3)** defines a *"relevant renewal"*, which starts a 14-day renewal cooling-off period, as arising *"when the consumer becomes liable under the contract for a first renewal payment following the end of a **concessionary period**"*, and separately where renewal payments resume after a 12-month gap or the contract continues beyond 12 months [E, [s.265](https://www.legislation.gov.uk/ukpga/2024/13/section/265), retrieved 2026-09-18].

Applied:

- **Two-week trial → monthly.** The trial is a concessionary period. **A renewal cooling-off period opens the day the first 99p is taken**, and a **cooling-off notice** is owed (s.266), which the Government intends to require *"in writing on a durable medium"* [E, Annex B Q23].
- **Yearly £10.90.** A 12-month contract renewing engages s.265(3)(b): **a renewal cooling-off period at every annual renewal.**
- **Monthly and quarterly without a trial.** No renewal cooling-off period.
- **Initial cooling-off.** The digital-content waiver survives: *"The initial waiver applies to digital content contracts in a way that is consistent with the approach under the CCRs"* [E, Government Response, p.9]. `compliance-note.md` §4.2 already established that Apple's purchase flow performs that waiver [E, §4.2, citing [CCRs 2013 reg.37](https://www.legislation.gov.uk/uksi/2013/3134/regulation/37)]. **Unchanged by the ladder.**

**The refund mechanic is where this bites, and it bites on a fact already on file.** For digital content the Government will legislate that *"If a consumer cancels a digital content contract during a renewal cooling-off period, the consumer will receive a **proportionate refund** — ensuring that the consumer pays an amount which is in proportion to the part of the contract performed, calculated on the basis of the total subscription contract price agreed for that supply"* [E, Government Response, p.10].

> **Candour cannot pay a proportionate refund.** `compliance-note.md` §4.1: *"**Candour cannot process a refund.** There is no mechanism. Refund requests go to Apple, are decided by Apple against Apple's criteria."* [E, read from disk 2026-09-18] Apple's Schedule 2 §6.3 confirms the only route: Apple refunds the End-User and *"You shall reimburse, or grant Apple a credit for, an amount equal to the price"* [E, Schedule 2 §6.3]. **So on Reading A, Candour would owe a statutory refund it has no mechanism to make, discharged in practice only by Apple's discretion.** [I]
>
> **This is a concrete, checkable question for the qualified human review under 6.1**, and it is a better question than the reminder one because it has no design answer: a build cannot fix it. On 99p the money is pennies; the *obligation* is not pennies.

### 5.3 Price rises — largely Apple's, and Apple does it better than the Act requires

`pricing-ladder-model.md` §2.4 establishes that Candour will be cutting prices roughly annually and stepping down ~32% at the amortisation cliff. **Increases are the direction the law constrains**, and Apple already performs the notification:

> *"If none of the criteria apply, Apple will automatically notify subscribers of the price increase with no additional request for consent… notifications are sent via email and push notifications — if enabled by the subscriber — 27 or 7 days before the next renewal date."* — with a **60 days before renewal** first email for annual, 2-, 3- and 6-month subscriptions, and consent required where the subscriber's region requires it or the increase exceeds the stated thresholds. [E, [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions), retrieved 2026-09-18]

Apple's consumer terms match: *"You will be notified by email at least 30 days in advance if the price of a Subscription is increasing"* and *"If you do not agree to a price change, you may cancel your Subscription (without charge) prior to the price change entering into effect"* [E, Apple Media Services Terms (UK), retrieved 2026-09-18].

**Finding:** price-rise notification is substantially discharged by Apple today, on an **addressed** channel, without Candour holding anything. [I] **Candour's own duty is the cost-sheet republication Article 2.1 already requires** — *"Cost sheets are reviewed and republished at least annually and at every price change"* — which is a transparency duty, not a notice duty.

**One re-derivation owed to the CFO under Condition 6, because it is a claim that a named source requires something.** `pricing-ladder-model.md` §0.4 and §2.4 state that Apple *"does not permit preserving the old price"* on a decrease, and cite the App Store Connect Help page. **I retrieved that page and the quotation is exact:** *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don't have the option to preserve the higher price for existing subscribers."* [E, same page]. **But Schedule 2 §3.9 reads, more broadly:** *"When You make price changes to an existing subscription item, You may elect to retain current pricing for Your existing customers by indicating Your intent in the App Store Connect tool."* [E, Schedule 2 §3.9] The two are reconcilable — §3.9's next sentence is about increases, and the Help page is the specific operational statement — but **they are not identical, and the CFO's finding that the reduction is irreversible rests on the Help page alone.** Recorded as a **flag to the CFO**, not a correction: the conclusion is probably right and the supporting citation is narrower than the claim built on it. §10.4.

### 5.4 Cancellation — Article 4's clause comes alive, and it is nearly free

`compliance-note.md` §4.3 recorded, of Article 4's *"Make cancellation as easy as signup"*: *"a clause aimed at subscription traps does not bite on a product that is not a subscription — and… the clause **will** bite hard if the CFO's Model 3 (subscription) is ever revived"* [E, read from disk 2026-09-18]. **It is revived. The clause bites.** And the statutory version is s.260: arrangements *"in a way which is straightforward"* and *"without having to take any steps which are not reasonably necessary"*, with online exit where the contract was formed online and instructions *"displayed online in a place or places that a consumer seeking to end the contract is likely to find them"* [E, s.260].

**Apple's Manage Subscriptions is that mechanism** — in-account, online, two taps, and the same route for every subscription the user holds. The Government's own guidance intention is directly on point: online exit may be delivered through *"A clearly labelled button on a website or in an app"* [E, Annex B Q22, p.47]. **Candour's whole obligation is a clearly-labelled in-app control that deep-links there, plus not obstructing it.**

Article 4 adds one thing the statute does not, and it is the thing this seat would actually police: *"no dark patterns: no false urgency, no confirm-shaming… no deliberately buried settings"*. **Condition 8.4 already forbids the machinery** — *"No countdown UI, no expiry notifications, no streaks, no badges"*. **A cancellation-flow retention offer is confirm-shaming's natural home and it is forbidden here before anyone proposes it.** [I] It belongs in requirements as an acceptance criterion, and §6.3 carries it.

### 5.5 Pre-contract information — already owed, for a different reason

Section 256 requires *"key pre-contract information"* (Schedule 23 Part 1) given together and separately from other material, and *"full pre-contract information"* (Part 2) given or made available; online, the key information must be given *"in writing… [so that] the consumer is not required to take any steps to read the information, other than the steps the consumer must take to enter into the contract"* [E, s.256]. Section 257(2) additionally requires that for an online subscription *"the final step which the consumer is required to take to enter into the contract involves the consumer expressly acknowledging"* the payment obligation [E, s.257].

**Condition 8.1 already requires almost exactly this**, on Article 4 and Article 1.3 grounds: *"The limit, the window, and what happens at its end are stated in plain language in the App Store description and on first run, before the user writes anything."* [E, `decisions/2026-09-16-haunt-gate.md` Condition 8.1] **The statutory list is longer and it is prescribed** (Schedule 23), so the work is to map Schedule 23 Parts 1 and 2 onto Haunt's App Store metadata and first-run screen. **Cheap, and cheapest done at requirements** — which is the same argument the CGO made for Condition 7 and was right about.

### 5.6 The whole list, in one table

| Duty | Statute | Falls on (Reading A) | Discharged by Apple today? | Candour's increment |
|---|---|---|---|---|
| Pre-contract information | ss.256–257, Sch.23 | Candour | Partly (purchase sheet) | Map Sch.23 onto store copy + first run |
| Express acknowledgment of payment | s.257(2) | Candour | **Yes** (StoreKit purchase sheet) | None |
| Reminder notices | ss.258–259 | Candour | **No** — Apple sends *receipts*, after the fact, switch-off-able | §4.3 items 3–4 |
| Easy / online exit | s.260 | Candour | **Yes, substantially** | A labelled deep link |
| Initial cooling-off | ss.264–265, waiver retained | Candour | **Yes** (waiver performed in flow) | None |
| **Renewal cooling-off + notice + proportionate refund** | ss.264–266 | Candour | **No, and unfixable by build** | **§5.2 — 6.1 review item** |
| Price-increase notice | (Apple's own) | Apple | **Yes, and better** | None |
| Cancellation as easy as signup | **Constitution Art. 4** | Candour | n/a | No retention friction; acceptance criterion |

---

## 6. The determination, and what it conditions

### 6.1 The four answers the CEO asked for, in his order

1. **In force today?** No. Every duty in ss.253–281 is prospective; s.254 itself is uncommenced and s.275(3) makes the Chapter inapplicable to any contract entered before s.254 commences. No commencement SI exists for the Chapter. **The Government's stated date is January 2027**, announced 9 August 2026, superseding "spring 2027". Secondary legislation and guidance: unpublished.
2. **Whose duties?** Unsettled, and the Government says so. **Candour must plan on them being its own** — Apple is Candour's commissionaire, not its reseller, and Schedule 2 §3.10 assigns regulatory compliance for auto-renewing subscriptions to the developer. **Apple already discharges price-rise notice and easy exit; it does not discharge reminder notices; and the renewal-cooling-off refund is the one Candour could not discharge even if it tried.**
3. **Fatal, survivable, or not ours?** **Survivable with a stated design.** The design is §4.3 items 1–5 and it collects nothing. **The Article 1.3 / Article 4 collision the CFO identified does not arise on the primary text** — the Government excludes only the *ephemeral* in-app notice. The one limb genuinely in doubt is s.280(a), *"addressed personally"*, and a local notification paired with the persistent record answers it without collecting anything.
4. **What else the ladder revives?** §5. In short: renewal cooling-off (trial and yearly tier), cooling-off notices, pre-contract information under Schedule 23, and Article 4's cancellation clause — which the prior note expressly reserved against exactly this event.

### 6.2 Blocks and flags, labelled per the amended charter

**I hold no block today.** `roles/cgo.md`: my blocking power is *"Gate passage — for constitutional breach, unanswered dissent, or missing compliance evidence"*, and *"Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it — a block is a checklist item failing, never a feeling of unease."* Nothing in §§1–5 is a checklist item failing today: the regime is not in force, and the compliance evidence for it now exists and is in this document.

**One conditional block, pre-declared so it cannot look invented later.** **It engages on publication of `decisions/2026-09-16-haunt-gate.md` under Article 3 with Condition 9 unamended.** Article 3 requires *"Decision records for every gate decision — kill, proceed, or park… Within 30 days of the decision"*, and the record publishes **2026-10-16**. A record published on that date stating that *"The one-off purchase shape is decided"*, when the CEO has decided a subscription ladder, publishes a false account of the company's own decision. That is a breach of the purpose of Article 3 and of Article 1.3's *"Honest by default"*, and it is the quiet-weakening failure Article 9's table names. **What lifts it:** C3 at §7.3 applied to the record as a commit on the open branch, before merge and before publication. **What does not lift it:** amending the record after publication, or superseding it in a later document.

**Flags, with the seat that owns each:**

| # | Flag | Owner |
|---|---|---|
| F1 | The s.277 regulations and DBT guidance are unpublished and will define "durable medium". **Re-check required before launch and again at commencement.** | **CGO** (me), dated at §6.3 |
| F2 | On-device availability of renewal dates without a server — load-bearing for all of §4.3 and tagged [K], not retrieved | **CTO** |
| F3 | The renewal-cooling-off proportionate refund is a duty Candour has no mechanism to discharge | **CEO**, via the 6.1 human review |
| F4 | Subscription-mechanics build increment now also includes a notices surface not in the CFO's §9.1 sensitivity | **CTO**, then **CFO** |
| F5 | `pricing-ladder-model.md`'s "Apple does not permit preserving the old price" rests on a narrower citation than the claim (§5.3) | **CFO** |
| F6 | Article 2.1's *"the cost of serving them"* — third flag, still unresolved (§10.2) | **CGO / CEO** |

### 6.3 What should attach to requirements sign-off, and to launch

Written as acceptance criteria, because the decision record's own lesson (Condition 4, Condition 7) is that these are cheap at requirements and expensive afterwards.

**At requirements:**

- **R1.** Schedule 23 Parts 1 and 2 mapped onto App Store metadata and the first-run disclosure screen, merged with Condition 8.1's existing disclosure duty rather than built twice.
- **R2.** A **persistent, append-only in-app notices surface**, included in the Condition 8.3 export, never auto-clearing, never dismissible into nothing.
- **R3.** Reminder and cooling-off notices written to R2 and paired with a local notification, on renewal dates read on-device. **No email address, no account, no server.**
- **R4.** A plainly-labelled in-app cancellation control deep-linking to Apple's Manage Subscriptions, and **no retention offer, no confirm-shaming, no friction in that flow** (Article 4; Condition 8.4).
- **R5.** The CTO answers F2 before R2 and R3 are estimated.

**Before launch (Constitution 6.1):**

- **L1.** **Qualified human legal review** of: whether the s.258 duty falls on Candour or on Apple Distribution International given the commissionaire arrangement; and the renewal-cooling-off refund mechanic at F3. This is the 6.1 trigger in terms — *"third-party licence terms whose interpretation determines a product's architecture or cost"*.
- **L2.** **A dated re-retrieval by this seat of the s.277 regulations and the DBT guidance**, when published and in any event **by 2026-12-01**, and again within 14 days of any commencement SI. **Anti-drift (5.2) applies to the company's own obligations as much as to its ideas**, and an undated "we'll check later" is the mechanism by which a known gap becomes furniture.

---

# JOB 2 — the Condition 9 amendment

**I do not edit `decisions/2026-09-16-haunt-gate.md`.** The record is the CVO's to amend and the decision is the CEO's under 5.4. What follows is drafted for transplant: §7.1 replaces Condition 9, §7.3 is the correction entry. **Both must land as a commit on the open branch `haunt/discovery-and-governance-v1.2`, before merge**, because the record publishes under Article 3 by **2026-10-16** and an amendment applied after the merge would be an amendment to a published record, which classifies differently (C1.6: *"Had this correction come after publication, the classification would be different"*).

## 7. Drafted replacement

### 7.1 Condition 9, as it should now read

> **9. Pricing — the shape is amended; the number is still not set.**
>
> *(Original text preserved at Correction C3 below, together with the reason it was superseded.)*
>
> **The CEO has decided a different shape from the one this record adopted on 2026-09-16.** Haunt is to be sold as a **subscription ladder with a two-week full-feature trial and no permanent free tier**, alongside a **paid-once tier**. Under Constitution 5.4 *"pricing changes"* are the CEO's alone and this is his to decide. What this condition does is record the decision accurately and attach what travels with it.
>
> **9.1 The number is still not set, and the bars on setting it have changed.** Price remains a Constitution 5.4 decision. Condition 1 (re-derivation of the cost model) is discharged by `products/haunt/window-conversion-model.md`; Condition 5 (the ONS ASHE benchmark) is discharged at primary by `products/haunt/pricing-ladder-model.md` §1. **Two bars remain, and both are new:**
>
> **9.2 A published five-year support commitment is a precondition, not a nicety.** Constitution v1.2, Definitions: *"**One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year… the amortisation period must equal a **published** support commitment to customers; any unamortised remainder is written off publicly on discontinuation (7.2); and the period may be shortened, never lengthened. **Absent a published support commitment, build labour is a first-year operating cost.**"* **Candour has published no support commitment for any product.** On the clause as written, every amortised figure in every Haunt model is therefore currently unavailable, and the correct treatment charges the whole £45,957.55 build to year one — which the CFO records as making *"every figure… wrong by a factor of about three"* [`pricing-ladder-model.md` §12.5]. **The CEO's own two numbers name the period:** 99p × 12 × 5 = £59.40, and against a five-year published life the monthly and paid-once tiers return **identical margins at every subscriber count**, while against a three-year life **they have no overlapping compliant band at all** [`pricing-ladder-model.md` §8.2]. **The commitment is dated, product-level, published, and contractual** — CRA 2015 s.36(3) makes pre-contract information about characteristics and functionality a term of the contract. *"Supported until [date]"* is not marketing.
>
> **9.3 The compliant band is narrow and every point of discount narrows it further.** At 99p/month on a five-year life the band runs **3,122 subscribers (cost recovery) to 4,988 (the Article 2.1 hard cap)** — a factor of 1.60. Across the recommended ladder it is **3,523–4,988, a factor of 1.42**; at two months free on annual, 1.23×; **at 25% off annual, 1.05×, which is not a band at all** [`pricing-ladder-model.md` §2.3]. Article 2.1: *"As a hard backstop, **no product's margin may exceed 30%**, regardless of justification."* **A discount curve deeper than roughly 10% therefore has no subscriber count at which every tier is simultaneously compliant**, and the CEO's original sketch (quarterly at 33% off) has none.
>
> **9.4 A price cut of roughly one third falls due on a date Candour can calculate at launch.** At the end of the published supported life the amortised build leaves the cost base. At N = 4,278 and L = 5, the year-six cost of serving a subscriber falls from £6.765 to £4.616 and the realised margin at an unchanged 99p jumps to **+62.3%** — twice the cap. The price must fall to about **68p** to return to target and to no more than **74p** to clear the cap [`pricing-ladder-model.md` §2.4(b)]. **This is not drift; it is a ~32% step, on a single calculable date.** Article 2.3's waterfall makes *"Price reductions for existing customers"* the first call on the remainder, so the cut lands on the **installed base**, not only on new buyers. **Apple performs it automatically and, on its own operational documentation, does not offer the option to preserve the higher price on a decrease** — *"If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don't have the option to preserve the higher price for existing subscribers"* [App Store Connect Help, *Manage pricing for auto-renewable subscriptions*, retrieved by the CFO and re-retrieved by the CGO 2026-09-18; note the narrower cross-reference recorded at `subscription-compliance-note.md` §5.3]. **The ratchet, once started, runs one way.**
>
> **9.5 The cadence the CEO is accepting.** At least one published cost sheet and one price review every year for the life of the product (Article 2.1: *"Cost sheets are reviewed and republished at least **annually** and at every price change"*), a step change of roughly a third at the amortisation cliff, and every reduction landing automatically and irreversibly on existing subscribers. **This is the obligation Candour wrote down in 2.3.3.1 before there was money at stake; a subscription is the shape that makes it bite.**
>
> **9.6 The subscription regime, now determined.** `products/haunt/subscription-compliance-note.md` (CGO, 2026-09-18) resolves the twice-flagged DMCCA claim at source. **Nothing in the DMCCA subscription-contracts regime is in force today; the Government's stated commencement is January 2027; the duties, when they commence, must be planned on as Candour's; and they are dischargeable on this architecture without collecting anything.** Requirements items **R1–R5** and launch items **L1–L2** of that note attach to this condition. **L1 — qualified human legal review under Constitution 6.1 — is a launch bar, not a recommendation.**
>
> **9.7 What this condition does not disturb.** **Condition 8 survives in full and unamended**, including the CEO's lapse clarification at 8.2 and the dependency Correction C2.5 records: *"the CEO's lapse clarification within 8.2 is clean under Article 1.2 **only because 8.1 discloses the lapse behaviour before the first entry**."* A subscription lapse is now a live mechanic rather than a prospective one, so **8.1 becomes load-bearing on the day the ladder is built.** Conditions 2, 3, 4, 6, 7 and 10 are untouched.
>
> **9.8 Two dependencies that are not the CEO's to close and are not closed.** (a) The **UX seat must re-test** its finding that *"Free + subscription: cannot be built honestly"* [`ux-note.md` §6.3] — the two grounds it rested on fell at C1.1 and C2.2, and the lapse behaviour it said did not exist now does [`pricing-ladder-model.md` §11.2]. **The ladder is not buildable until that seat has looked again.** (b) The **CTO must size** the subscription-mechanics increment, which is not in the 1,330 hours, and must answer whether 220 h/yr maintenance holds to year five across five iOS and five Android major releases.
>
> **9.9 The CFO's standing block, restated so it is not mistaken for discharged.** *"No price may be published under Article 3 without a cost sheet behind it, and the cost sheet for this ladder is not complete until the support commitment is published"* [`pricing-ladder-model.md` §12.5]. **What lifts it:** the published commitment, or a re-derivation on the first-year-expense treatment.

### 7.2 Why each element is in there rather than left to the models

[J, mine] A decision record is read by someone who will not open the cost model. Four things in the CFO's document are **decisions dressed as arithmetic**, and a record that omits them publishes a shape without its consequences: the support commitment (without which no figure in any Haunt model is available at all), the band width (which forecloses the discount curve the CEO sketched), the year-six step-down (which is a dated future obligation, not a forecast), and the irreversibility of the cut. **None of those is a number. All four are commitments.** The number genuinely can wait; these cannot, because they constrain what number is available.

### 7.3 Correction C3, drafted for the CVO to apply

> ---
>
> # Correction C3 — 2026-09-18, before first publication
>
> **Classification: AMENDMENT recording a later CEO decision — neither a CORRECTION nor a WEAKENING.** The template's test (`pipeline/templates/decision-record.md`) offers two categories and this is a third; the reasoning is at C3.4, and the gap in the test is reported to the CVO at C3.5 rather than papered over by forcing the nearer label.
>
> **Condition 9 as adopted on 2026-09-16 read, in full:**
>
> > *"**9. Pricing is not set by this record.** Price remains a Constitution 5.4 decision, unavailable until Condition 1 completes. The one-off purchase *shape* is decided; the number is not."*
>
> **C3.1 — Nothing in that text was wrong when it was written, and nothing in it is being corrected.** It accurately recorded the decision the CEO made on 2026-09-16. It is superseded because **the CEO has since made a different decision**, which is his alone under Constitution 5.4 — *"The following are never automated: kill/proceed decisions, spending real money, **pricing changes**, anything affecting user data policy, and release to real users. Agents prepare; the founder decides."* **The distinction matters:** C1 and C2 each corrected a false statement about what the rules require. C3 does not. **A record that filed this under "correction" would be claiming the CEO had been wrong, when in fact he changed his mind, which he is entitled to do and which the record should show him doing.**
>
> **C3.2 — What changed.** From a **one-off purchase** to a **subscription ladder with a two-week full-feature trial and no permanent free tier**, retaining a **paid-once tier**. Sequence, so a reader can audit it: the CFO's `window-conversion-model.md` (2026-09-17) recommended against subscription outright; the CEO directed a ladder be modelled at full effort; `pricing-ladder-model.md` (2026-09-18) returned a recommendation that **separates** the ladder from the free tier and supports the ladder *"if and only if"* a five-year support commitment is published. **The CFO has changed position on the ladder and records having done so** — *"I record the change because a seat that never moves is not being useful"* (§10.1.2). **The free tier is the element every model kills, and the CEO's shape does not include one.**
>
> **C3.3 — Why this is not a WEAKENING.** Article 11.2 labels amendments that *"weaken a customer-facing or transparency rule"*. Applying the C1.6 discipline — *"Two acts happened here, and an earlier draft of this correction described one"* — the acts here are counted:
>
> 1. **A shape decision was replaced.** No customer protection sat inside Condition 9; it was a record of shape and a reservation of the number. **Nothing is removed.**
> 2. **Protections are added, not withdrawn.** C3 attaches a published support commitment, a band constraint, a dated price-reduction obligation, and DMCCA requirements R1–R5 and launch bars L1–L2.
> 3. **Condition 8 is untouched**, and 9.7 records that 8.1 becomes load-bearing rather than optional once a lapse mechanic exists. **That is a tightening in practice.**
> 4. **Nothing has been published and nobody has relied on anything.** Publication is due 2026-10-16.
>
> **One thing runs the other way and is recorded rather than netted off**, because netting is how a withdrawal travels under an amendment's cover: **a subscription creates a lapse state that a one-off purchase did not have.** The decision record already contemplated it (the CEO's clarification within 8.2) but it was prospective; it is now a live mechanic. **The UX seat's B2 release block, which Correction C2.6 records as *"zero-now, not zero-forever"*, is the check on that, and 9.8(a) makes the re-test a precondition rather than a hope.**
>
> **C3.4 — Why the template's two categories do not fit.** The test settled on 2026-09-16 distinguishes a **CORRECTION** (*"fixes a false statement about what the rules require, before first publication"*) from a **WEAKENING** (*"removes or narrows a protection that has been published and may have been relied upon"*). **This is a third thing: an accurate record of decision A, superseded by decision B, before publication.** Forcing it into "correction" would misdescribe the CEO; forcing it into "weakening" would misdescribe the change. **The answer the template itself gives is the right one regardless of label:** *"the answer to Article 9's quiet-weakening vector is **visibility**, not any particular word: original preserved, error named, seat attributed, date recorded."* Original preserved above; no error to name; decision attributed to the CEO; dated.
>
> **C3.5 — Recommended amendment to the template, for the CVO.** Add a third bullet to the classification test: *"An **AMENDMENT** records a later decision that supersedes an earlier one, where the earlier record was accurate when made. It preserves the original, names the decision-maker and the date, and states what travels with the new decision. It is not a correction (nothing was false) and not a weakening unless a protection is actually removed — in which case say both."* **This is a company-level change, not a Haunt one, and it is drafted here because this record is the first to need it.**
>
> **C3.6 — Consequential corrections owed elsewhere**, visibly and in place, **in the same publication as this record**:
>
> | File | What is owed |
> |---|---|
> | `products/haunt/compliance-note.md` §4.3 | Article 4's cancellation clause now bites: Model 3 is revived. The section reserved this outcome expressly. |
> | `products/haunt/compliance-note.md` §4.5 | The "not applicable" finding is superseded on both its grounds. Commencement is **January 2027**, not spring 2027, and Haunt is no longer a one-off. See `subscription-compliance-note.md` §§1–2. |
> | `products/haunt/cost-sheet.md` §2.4, §2.1, §13 | ONS benchmark closed at primary; Apple merchant-of-record upgraded from [K] to [E]. |
> | `products/haunt/window-conversion-model.md` §3.1, §6.4 | Flag 1 and the standing block discharged. |
> | `products/haunt/ux-note.md` §6.3 | Flagged for re-test by the UX seat under 9.8(a). Not corrected by any other seat. |
>
> ---

---

## 8. "Lifetime" — the CVO's test confirmed, its conclusion corrected

**The CEO's reading, as given to me:** "lifetime" means access for the life of the *product*, priced at five years of monthly. **The CVO's position:** honest provided the page states plainly what it covers — the product's life, not the buyer's — with Article 7.2's discontinuation terms attached.

### 8.1 What is right, and it is most of it

**The substance is honest, and against a five-year published support commitment it is unusually clean.** [I] Three things are true at once and all three are checkable by a customer:

- Five years of 99p is £59.40 exactly, so the paid-once tier is not a premium dressed as a convenience.
- At L = 5 the two tiers return **identical margins at every subscriber count** [`pricing-ladder-model.md` §8.2], so neither path subsidises the other.
- The crossover — the tenure at which a monthly subscriber has paid what the paid-once buyer paid — falls **exactly at the end of the supported life** [`pricing-ladder-model.md` §6.5]. **Nobody is worse off on either path, on Candour's own published promise.**

**And the CVO's test is the correct test.** Article 1.3: *"**Honest by default.** Pricing, capability, and limitations are stated plainly. **We say what a product cannot do.**"* The test is plain statement of what the thing covers. **Attaching Article 7.2's discontinuation terms is also right and I would go further than "attached":** 7.2 requires *"At least **90 days' notice** to every customer"*, export throughout the notice period and for 90 days after, open-sourcing where third-party rights allow, and *"A published closing cost sheet for the product's final period"* — and the Definitions add that *"any unamortised remainder is written off publicly on discontinuation (7.2)"*. **A paid-once buyer in year two of a five-year commitment is precisely the person those clauses exist for, and the pricing page should link them, not merely allude to them.**

### 8.2 Where the conclusion does not follow: the word fails the test it is being measured against

**A disclosure whose job is to reverse the ordinary meaning of the headline word is not plain language. It is a correction of an impression the headline just created.** [J, mine, stated as this seat's judgment] "Lifetime" in ordinary consumer use means *the buyer's* — that is why the word is chosen. A page reading "Lifetime — £59.40 (this means the life of the product, not your life)" does not state a limitation plainly; it states an overstatement and then retracts it, and the retraction is doing work the headline should never have created.

**Unlike the subscription regime, this one is in force now, and that changes the register of the objection.** [I] **Section 226** of the DMCCA — *"Misleading actions"* — has been **in force since 6 April 2025 by S.I. 2025/272** [E, [DMCCA 2024 Part 4 Chapter 1](https://www.legislation.gov.uk/ukpga/2024/13/part/4/chapter/1), commencement notes for ss.225–227, retrieved 2026-09-18]. A practice is a misleading action where it involves:

> *"(b) an overall presentation which is likely to deceive the average consumer about a matter relating to a product, a trader or any other matter relevant to a transactional decision"* — and, decisively, **"an overall presentation may be deceiving even if the information it contains is true."** [E, [s.226](https://www.legislation.gov.uk/ukpga/2024/13/section/226), retrieved 2026-09-18]

**That sentence is the answer to "but we disclosed it".** A true disclaimer under a misleading headline is exactly the case s.226(b) is drafted for. `compliance-note.md` §4.5 also records that s.227 (misleading omissions) catches information given *"in a way that is unclear or untimely"*, and that the CMA now holds direct enforcement powers.

**So the ground shifts.** The CVO is arguing that disclosure cures the word. Under Article 1.3 that is a judgment call on which reasonable seats differ. **Under s.226(b) it is a judgment call the statute has already expressed a view on**, and the view is that true information in a deceiving presentation is still a misleading action. [I]

**One more reason, specific to Haunt and not to language generally.** Candour is about to publish a **five-year support commitment** as a term of the contract (§7.1 9.2). **A company cannot publish "supported until 2032" and "lifetime" on the same product and claim both are plain.** The CFO put this exactly right and I adopt it: *"a tier called 'lifetime' sold against a published five-year support commitment is two public numbers disagreeing"* [E, `pricing-ladder-model.md` §8.4].

### 8.3 The determination, and the wording I would sign

> **Confirmed:** the CVO's test (plain statement of what it covers, Article 7.2 attached) is the right test, and the CEO's economics are honest.
> **Corrected:** the word "lifetime" does not survive that test, and the objection is not only a values objection — **DMCCA s.226(b) is in force and addresses precisely the "true disclaimer under a misleading headline" case.**
> **This seat's recommendation:** do not use the word. **This is a flag, not a block** — marketing copy is a release matter, and the seats holding release blocks on Article 4 and honesty grounds are **UX** and, at pre-release verification, **QA**. My block is gate passage, and it does not reach a word on a pricing page.

The CFO's drafted wording is nearly right and I would make one change [J]:

> *"**Pay once — £59.40.** Supported until [date], the same as every other tier. The same as paying 99p a month for the whole of that period, with nothing to cancel. **If we discontinue Haunt before [date], you get at least 90 days' notice, your full export throughout and for 90 days after, and we publish the closing cost sheet and what we had not yet recovered.**"*

The added sentence is the Article 7.2 attachment the CVO asked for, **written out rather than linked**, because Article 1.3's *"We say what a product cannot do"* is not discharged by a hyperlink — and because a paid-once buyer is the customer for whom that paragraph is the entire risk. **Note also that the label "Pay once" carries no claim needing retraction**, which is the test §8.2 applies.

---

## 9. Article 9 — the loophole table, at the next amendment

### 9.1 The CFO's vector: yes, it belongs

**The finding, quoted rather than characterised:** *"A lifetime tier converts a recurring price into a one-off payment, and thereby moves it outside the cumulative margin test's scope entirely. The clause constrains what a subscriber pays 'merely by staying'. A lifetime buyer pays nothing by staying… a Candour under revenue pressure in year four, facing an automatic and unpreservable price cut on its whole subscriber base, has exactly one lawful escape: **push new customers onto lifetime.**"* [E, `pricing-ladder-model.md` §6.4]

**I confirm it belongs in the table, on three grounds:**

1. **It meets Article 9's own criterion.** The article's closing sentence is not hedged: *"If a reader finds a gaming vector not listed here, **we commit to adding it rather than using it**."* The CFO has found one, named it, and expressly declined to use it. **The commitment is already made; the amendment performs it.**
2. **It is the same species as an entry already in the table.** *"Redefining 'cost,' 'surplus,' 'reserve,' or 'net proceeds'"* is about escaping a test by changing what falls inside it. So is this: the price does not change, the customer's classification does. [I]
3. **It is newly live.** The cumulative test is itself new in v1.2 (*"For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**"*), and Haunt is the first product to have a recurring shape. **A test gets its first loophole the first time it constrains anything.**

**The CFO's proposed row, which I would adopt with a tightened exposure column:**

| Loophole | The number that exposes it |
| --- | --- |
| Escaping the cumulative margin test (2.1) by converting recurring customers to one-off purchases | **The annual margin published for every tier, including one-off tiers, at every republication — together with the share of new customers taking each tier, year by year.** A shift in mix is the thing that shows the manoeuvre; a single tier's margin does not. |

### 9.2 A second vector, found in the course of this work and named rather than used

**The support commitment is a lever on the price ceiling, and nothing currently exposes it.** [I, from the CFO's own arithmetic]

The Definitions make the amortisation period equal to the published support commitment. Lengthening that period lowers the annual amortised charge, which lowers annual cost, which **raises the margin earned at any given subscriber count**. The CFO's own table shows the mechanism at full size: moving from a three-year to a five-year commitment moves the compliant band at 99p/month from **4,126–6,590 down to 3,122–4,988** [`pricing-ladder-model.md` §8.3] — *"a five-year commitment makes the CEO's price lawful at a lower subscriber count than a three-year one would."*

> **So: declare a long supported life, price against the flattered cost base, then discontinue early.**

**What already guards it, partially.** The Definitions bind the period three ways — it *"must equal a published support commitment to customers"*, *"any unamortised remainder is written off publicly on discontinuation (7.2)"*, and *"the period may be shortened, never lengthened"*. **But a public write-off is a disclosure, not a remedy**: a customer who paid a price justified by a five-year commitment and got three years is told the number and keeps the loss. Article 7.2's 90 days' notice and closing cost sheet are the customer-facing answer, and neither returns money. [I]

**My proposed row:**

| Loophole | The number that exposes it |
| --- | --- |
| Declaring a long supported life to spread build cost, flatter the cost base and raise the compliant margin — then discontinuing early | The declared supported life published alongside **actual** supported life on discontinuation, and the unamortised remainder written off under the Definitions and Article 7.2, **stated as a proportion of the declared period** |

### 9.3 How this proceeds, and what it is not

**Both rows are Article 11 amendments and therefore the CEO's**, on this seat's advice: *"Any change to this document is recorded in a public change log with date, diff, and rationale"* (11.1). **Neither is a weakening** — adding a loophole to the loophole table strengthens a transparency rule — so 11.2's WEAKENING label does not apply.

**This is a flag, not a block.** My blocking power is gate passage, and an unamended Article 9 is not a gate breach. **What I do record is the timing:** Article 9's commitment is *"add rather than use"*, and Haunt's paid-once tier is the exact instrument the first vector describes. **Shipping the tier while the row is unwritten is the order in which this looks worst**, and the cheapest fix is to carry both rows in the same amendment cycle as the support commitment, which is owed anyway.

---

## 10. Gaps, escalations, corrections owed, and where I looked

### 10.1 Disagreement, stated once and in writing

Per the universal charter clause — *"Disagreement is a deliverable, not a discourtesy"* — three, recorded once each and not relitigated:

1. **With the CFO, on the largest item in his model.** §9.2(a) of `pricing-ladder-model.md` records the durable-medium reminder duty as *"possibly the largest unpriced item in this document"* and infers that discharging it *"would require Candour to collect an email address"*. **The inference is not supported by the primary source**, which excludes only the ephemeral in-app notice. The CFO flagged his source honestly and the compression happened across two documents rather than inside his; **the seat that supplied the unverified claim was this one.** §2.3.
2. **With the CVO, on "lifetime".** Its test is right; its conclusion is not, and the statutory ground (s.226(b)) is one the CVO did not have in front of it. §8.
3. **With my own prior artifact, twice.** `compliance-note.md` §4.5's commencement date is stale and one of its two grounds has fallen (§1.4); §4.1's merchant-of-record finding is correct about tax and was being carried toward a conclusion about *duties* that the commissionaire arrangement reverses (§3.2). **Both are this seat's, both are named here rather than quietly superseded.**

### 10.2 The escalation this note does **not** settle, given an owner and a date

Article 2.1's cumulative test measures against *"the cost of serving **them**"*. The CFO has now flagged twice that the clause is *"non-redundant only because its two tests use different cost measures"* and that on a pro-rata reading *"the clause is a no-op"*; he models the incremental reading *"because it is the only one on which the clause means anything"*, and expressly assigns the determination to this seat [E, `window-conversion-model.md` §4.1; `pricing-ladder-model.md` §6, §10.4.4].

**With `pricing-ladder-model.md` it has been flagged twice and this note would be the third artifact to touch it.** Under the evidence standard it must now be resolved or formally accepted by the CEO. **I am not resolving it here, and the reason is not workload.** It is an interpretive question about a clause of the Constitution, arising inside a document about a different subject, and the evidence standard's own finding is that *"a process that answers an interpretive failure by adding agent passes is prescribing more of what already failed"*. **Settling a constitutional definition in passing, in a note about consumer law, is how a heuristic becomes law** — which is the September 2026 failure this company has already documented four times.

> **Owner: CGO, as a standalone determination, with the CEO deciding. Due before any Haunt price is published under Article 3, and in any event by 2026-10-16**, so it travels in the same publication as the decision record. **If it is not resolved by then, it goes to the CEO for formal written acceptance under the evidence standard, which is the other half of the rule and is not a lesser outcome.**

### 10.3 What this seat could not establish

| Gap | Why it matters | Owner |
|---|---|---|
| **The s.277 regulations and the DBT guidance** | They will define "durable medium" operationally and could close limb (a) against an in-app notice. **Unpublished; promised before commencement** | **CGO** — dated re-retrieval, L2, by 2026-12-01 |
| **Whether renewal dates are available on-device without a server** | Load-bearing for all of §4.3. Tagged **[K], high confidence, not retrieved** | **CTO** (F2) |
| **Whether Apple sends any advance reminder before an ordinary renewal or a trial ending** | Decides whether anything discharges s.258 under Reading B. **I could not retrieve an Apple-published page describing one.** What I could establish — *"Receive Renewal Receipts"*, after the charge, switch-off-able — is **secondary and plausibly single-origin** | **CGO / CTO**, verifiable directly in a sandbox subscription |
| **Whether the duty falls on Candour or on Apple** | The determination itself. **The Government declines to answer it generally** (§3.3) | **Qualified human legal review, Constitution 6.1** (L1) |
| **The proportionate-refund mechanic on a renewal cancellation** | A statutory duty with no mechanism available to Candour; **no build fixes it** | **Same review** (F3) |
| **Schedule 23 Parts 1–3 in detail** | I retrieved the operative sections but not the Schedule's item-by-item lists, which set the prescribed content of pre-contract information and reminder notices | **CGO**, at requirements (R1) |
| Whether Google Play's arrangement mirrors Apple's commissionaire structure | Android is not in the MVP; becomes live if it ever is | **CTO / CGO**, deferred |

### 10.4 Corrections owed elsewhere, visibly and in place

| File | What is owed |
|---|---|
| `products/haunt/compliance-note.md` §4.5 | **Both grounds superseded.** Commencement is **January 2027**, not spring 2027; Haunt is no longer a one-off. The "not applicable" finding is withdrawn and replaced by §§1–6 of this note. The flagged single-origin claim is **resolved at source**. |
| `products/haunt/compliance-note.md` §4.1 | The merchant-of-record finding stands for **tax and refund mechanics** and does **not** settle who the trader is for DMCCA Part 4 Chapter 2. Apple is Candour's **commissionaire**; Candour is the principal. §3.2. |
| `products/haunt/compliance-note.md` §4.3 | Article 4's cancellation clause now bites, exactly as that section reserved. §5.4. |
| `products/haunt/pricing-ladder-model.md` §9.2 | The email-collection inference is **not supported by the primary source**; the reminder duty is dischargeable without collecting anything. **The item should be re-sized, not deleted** — a notices surface is a real build increment (F4). |
| `products/haunt/pricing-ladder-model.md` §0.4, §2.4 | **Flag, not correction:** the Help-page quotation is exact, and Schedule 2 §3.9 is broader. §5.3. |
| `decisions/2026-09-16-haunt-gate.md` Condition 9 | **Replace per §7.1; add Correction C3 per §7.3. As a commit on `haunt/discovery-and-governance-v1.2`, before merge and before 2026-10-16.** |
| `pipeline/templates/decision-record.md` | Add the third classification category. §7.3 C3.5. |

### 10.5 Where I looked

**Retrieved from disk this session, in full:** `constitution.md` v1.2 (Definitions; Articles 1, 2.1, 2.3, 3, 4, 5.2, 5.4, 5.6, 6.1, 7.2, 9, 10, 11); `roles/cgo.md` as amended; `pipeline/evidence-standard.md` v1.1 including *"Claims about our own rules"*; `decisions/2026-09-16-haunt-gate.md` in full including Conditions 1–10 and Corrections C1 and C2; `products/haunt/pricing-ladder-model.md` in full; `products/haunt/compliance-note.md` §4 in full and its section index; `pipeline/templates/decision-record.md`; `pipeline/templates/` directory listing.

**Retrieved externally this session (2026-09-18), at primary:** DMCCA 2024 Contents; Part 4 Chapter 2 with its prospective/in-force status section by section; **ss.254, 256, 257, 258, 259, 260, 265, 275, 280**; Part 4 Chapter 1 commencement notes and **s.226**; **SI 2026/284** (Commencement No. 3); the **DBT Government Response** of 02/04/2026 (web version and PDF, text-extracted and searched); **Annex B: summary of question responses** (PDF, text-extracted and searched for "durable medium", "in-app", "SMS", "WhatsApp", "email", "third party"); the **GOV.UK press release of 9 August 2026**; Apple Media Services Terms and Conditions (UK); **Apple Schedule 2 and 3** (text-extracted: §§1.3, 3.8, 3.9, 3.10, 6.3); **Exhibits to Schedule 2 and 3 (English, UK)**, Exhibit A §§1–2, confirming the United Kingdom in the commissionaire list; App Store Connect Help, *Manage pricing for auto-renewable subscriptions*.

**Attempted and failed:** the Hansard written ministerial statement of 13 April 2026 (HTTP 403 from parliament.uk); Annex B at its web-accessible URL (404 — obtained as PDF instead); an Apple-published page documenting advance renewal or trial-end reminders (searched; **not found**, which is itself the §10.3 finding).

**Looked for and did not find:**
- **Any statement in the Government Response or Annex B that in-app notices as such do not qualify.** The only operative sentence is the conditional one at §2.3.
- **Any resolution of the intermediary/trader question.** The Government's answer is that it *"will depend on the facts and specific contractual arrangements in place in each case"*, with guidance promised.
- **Any commencement provision for ss.253–281** in any instrument.
- **Any published Candour support commitment for any product.** Absent — which is why §7.1 9.2 is a precondition rather than a recommendation.

### 10.6 Related-party disclosures

**None.** Nothing in this note contemplates a payment to the founder, family or any affiliated entity.

---

## Change log

| Date | Change |
|---|---|
| 2026-09-18 | Created at the CEO's direction. **Closes the twice-flagged DMCCA commencement and durable-medium claims at source** under `pipeline/evidence-standard.md` *"Twice-flagged is escalated"*, correcting the commencement date from spring 2027 to **January 2027** and correcting the CFO's email-collection inference. Determines the trader question as far as it can be determined and refers the remainder to qualified human review under Constitution 6.1. Drafts the replacement **Condition 9** and **Correction C3** for the CVO to apply to `decisions/2026-09-16-haunt-gate.md`. Confirms the CVO's test on "lifetime" and corrects its conclusion. Recommends **two** rows for Article 9's loophole table. **One conditional block pre-declared** (§6.2), engaging on publication of the decision record with Condition 9 unamended. External sources retrieved 2026-09-18. **Not a certification.** |

# Article 11 amendment draft — amortisation of one-off build labour

**Seat:** Chief Governance Officer · **Date:** 2026-09-20 · **Status:** **DRAFT FOR THE CEO.** Article 11 amendments are the CEO's decision (Constitution 5.4 — *"pricing changes"*; Article 11.1). This seat prepares and flags; it does not certify and it does not amend.

**Target:** Constitution **v1.2** → **v1.3**. Amends the **Definitions** entry for **Cost**, adds one Definitions entry, and makes consequential edits to **Articles 2.1, 7.2, 9** and (optionally) **10**. Articles **2.3** and **3** were checked and need nothing; §3.2 and §3.3 say why.

**Revision 2 — 2026-09-20, after CEO decisions D4 and D5 and the CFO's proposal.** The CEO has adopted **Option B** (D4): amortisation decoupled from any support promise, **and** Article 4 gains a duty to publish a support date or state plainly that none is given. Haunt takes the second limb. This revision incorporates that, incorporates the CFO's layering and start-date mechanics from `pipeline/amortisation-proposal.md`, and settles the Article 11 classification on the Option B basis. **Sections edited in place rather than appended-to; the change log at §12 records every change and why.** *(The preserve-verbatim-and-append convention used in `decisions/2026-09-16-haunt-gate.md` governs published records. This is an unpublished working draft the CEO is about to act on, and a draft whose operative text is superseded 400 lines below its own statement of it is worse to act on, not more honest.)*

**Division of labour, stated so the seams are visible.** The **CFO** owns the accounting substance and the number, at `pipeline/amortisation-proposal.md` [E, read from disk 2026-09-20], which recommends **three years (36 months)** with layered clocks and a published layer schedule. **This seat owns the constitutional wording, the Article 11 classification, the Article 9 rows, the consequential edits, and the conformance check.** §6 states the tests the period must pass, §6.4 gives this seat's verdict on whether the CFO has answered the sharpest of them, and §6.3 states the one problem visible regardless of the number. This seat does not set the period.

**There is no template for an Article 11 amendment.** `pipeline/templates/` holds nine templates and none of them is this [E, `pipeline/templates/`, listed from disk 2026-09-20]. This draft follows the structure of the v1.2 entry in `CHANGELOG.md` for its change-log section (§9) and invents the rest. **Flag: `pipeline/templates/amendment.md` is owed**, and this document's §9 is a serviceable first draft of it. Filed with `pipeline/governance-review-2026-09.md` §D, which found the same gap for gate packs.

**Evidence conventions.** Per `pipeline/evidence-standard.md` v1.1 as amended [E, read from disk 2026-09-20]: every claim tagged [E]/[K]/[I]/[J]; **every assertion about what the Constitution or a law requires, permits or forbids quotes the clause, by number, in the same passage.** Repository files are tagged [E] with the path and the fact of reading this session. External law is tagged [E] with a retrieved link and the retrieval date. Nothing here is cited from memory.

---

## 0. The findings, before the drafting

1. **v1.2's Cost definition contains a clause that permits an unlawful act.** *"The period may be shortened, never lengthened"*, combined with *"the amortisation period must equal a **published** support commitment to customers"*, permits Candour to shorten a published support commitment. CRA 2015 s.36(3) makes that commitment a term of the consumer's contract and s.36(4) makes a change to it ineffective without that consumer's express agreement [E, retrieved 2026-09-20 — §1.3]. **A constitution that permits an unlawful act is defective whether or not anyone acts on it**, and this one is published continuously under Article 3. This, not the two fairness flaws, is the decisive reason to amend.

2. **The amendment is sound in design and I recommend it.** Separating *how long a cost is spread* from *what is promised to a customer* is the right cut. v1.2 welded them together and the weld is what produced all three flaws. [J]

3. **Article 11 classification, settled on the Option B basis: no WEAKENING label is owed.** §4 sets out the reasoning, including the argument against my own conclusion. **Without Option B the label would have been owed and I would still be recommending it** — that is stated at §12.1 rather than quietly dropped, because a recommendation that disappears the moment it is accommodated was never worth making. What Option B changes is not the label; it is the substance the label would have described. **The residual difference — a customer now receives information where v1.2 made a promise near-certain — is named in the change log without the label** (§9).

4. **Article 9 gains seven rows, consolidated from this seat's four and the CFO's V1–V4.** §12.4. The two owed from Correction C3.3 are discharged: (a) carried, (b) **does not survive** — its stated mechanism runs in the wrong direction on `cost-sheet-v2.md` §5.1, and the CFO's §5.5 second count silently corrects it. §5.3.

5. **The determination owed on Article 2.1's *"the cost of serving them"* is settled here, on the text, as the incremental reading**, and the reasoning is shown rather than asserted. It changes no Haunt price. **The one-sentence question for the CEO is at §12.5.** §8.

6. **Haunt: Condition 9.2 is obsolete and the decision record publishes on 2026-10-16.** **Correction C5** is drafted at §7 and revised at §12.6 for D4/D5, with a fallback if the amendment is still pending. **D2 is superseded, not corrected** — nothing in it was false, and D4 already records that. **Two CFO errors are carried into C5:** Condition 9.3 is wrong on its own author's later finding, and Condition 9.4 cites Article 2.3.3.1 for an obligation that comes from Article 2.1.

7. **The T1 objection is PARTLY ANSWERED and does not block.** The CFO's §2.4 is an honest and substantially successful separation. **But the retrieved platform evidence establishes a cadence of one year and brackets the answer at "a small number of years" — it does not select three over two.** Within that bracket the selection still rests on Haunt. **Two cheap fixes close it; I recommend the CEO assent to three years with both attached.** §6.4.

8. **D5's recording is adequate on the hard part and inadequate in four respects.** The Research Analyst's warning is preserved and the test forbids the growth argument, which is the part that matters. Missing: an owner and a revisit point; **an evidence bar for "unprompted demand" on an architecture that by design collects nothing**; the online-safety determination; and anything preventing the option being mentioned in marketing before it is gated. §12.7.

---

## 1. What is wrong with v1.2, clause by clause

### 1.0 The clause as it stands, quoted in full

Constitution v1.2, **Definitions**, entry for **Cost** [E, `constitution.md` line 21, read from disk 2026-09-20]:

> **Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and labour valued at a published market benchmark whether or not it is actually paid. **One-off build labour is capital, amortised straight-line over the product's declared supported life**, rather than charged wholly to its first year; maintenance and support are operating costs. Three conditions bind that treatment: the amortisation period must equal a **published** support commitment to customers; any unamortised remainder is written off publicly on discontinuation (7.2); and the period may be shortened, never lengthened. Absent a published support commitment, build labour is a first-year operating cost.

Adopted at v1.2 on 2026-09-16, drafted by the CVO, on the CFO's treatment [E, `CHANGELOG.md` v1.2 item 5, read from disk 2026-09-20]. Its stated rationale: *"the tie to a **published** commitment is what stops the period being chosen to flatter a price."*

### 1.1 First flaw — it punishes honest under-promising

Commit to two years honestly, discover in year three that you can support five, and the ratchet blocks the extension from reaching the price. Nothing in the Constitution stops Candour from *doing* more support; what is blocked is re-amortising the build over the longer life [I, from the quoted clause].

The CFO has put a number on who loses. At a subscriber count of 8,998, a customer buying in year one of an honestly-under-promised two-year commitment faces an honest monthly price of **£1.341** against the **£0.990** a five-year declaration would have produced — **£8.42 over two years**, for a product that turned out to have the longer life anyway, with no mechanism to give it back [E, `products/haunt/cost-sheet-v2.md` §5.5, read from disk 2026-09-20].

**Agreed. The rule makes the customer-adverse error the permitted one and the customer-favourable correction the forbidden one.** [I]

### 1.2 Second flaw — the permitted direction is the price-raising one

Shortening compresses the same build cost into fewer years, which raises the annual charge and therefore the price. Lengthening lowers it. Declared at the outset at the same subscriber count: two years gives an honest **£1.341**/month, three years **£1.146**, five years **£0.990** [E, `cost-sheet-v2.md` §5.5]. Shortened mid-life it is worse: publish five years, shorten to three at the end of year two, and **£44,719** unrecovered must be recovered in one remaining year, taking the honest price to **£1.458** — a 47% increase [E, ibid.].

Against that, two clauses of our own:

- Article 2.1 [E, `constitution.md` line 46]: *"Prices target a margin of approximately **20% over published costs**… deviations are permitted but must be justified in writing on the cost sheet… **A deviation in either direction is a deviation**."*
- Article 2.3.3.1 [E, `constitution.md` lines 63–66]: the remainder of profit goes, first in order of preference, to *"Price reductions for existing customers"*.

**v1.2 permits the price-raising direction with no justification required at all, and forbids the price-lowering direction outright.** [I, from the three clauses quoted] That is the inversion. The CVO and the CFO have both reached it; I reach it independently on the text.

### 1.3 Third and decisive flaw — the clause permits an act the law forbids

**This finding is this seat's, retrieved at source this session, and it is the one that makes amendment obligatory rather than desirable.**

**Consumer Rights Act 2015, section 36** [E, https://www.legislation.gov.uk/ukpga/2015/15/section/36, retrieved 2026-09-20]:

> **(3)** *"Any information that is provided by the trader about the digital content that is information mentioned in paragraph (a), (j) or (k) of Schedule 1 or paragraph (a), (v) or (w) of Schedule 2 (main characteristics, functionality and compatibility) to the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 (SI 2013/3134) is to be treated as included as a term of the contract."*
>
> **(4)** *"A change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader."*

The referenced paragraphs, retrieved rather than assumed, because s.36(3) is a pointer and a pointer cited from memory is a citation without a retrieval:

- **Schedule 2** (*"Information relating to distance and off-premises contracts"* — the schedule that applies to an app-store purchase), **paragraph (a)**: *"the main characteristics of the goods, services or digital content, to the extent appropriate to the medium of communication"*; **paragraph (v)**: *"where applicable, the functionality, including applicable technical protection measures, of digital content"* [E, https://www.legislation.gov.uk/uksi/2013/3134/schedule/2, retrieved 2026-09-20].
- **Schedule 1** (on-premises) paragraphs (a), (j), (k) are in materially the same terms [E, https://www.legislation.gov.uk/uksi/2013/3134/schedule/1, retrieved 2026-09-20].

**The chain, stated so each link can be attacked separately:**

1. A dated, product-level, published statement that a product *"is supported until [date]"* — continuing to run on then-current OS versions, receiving security and defect fixes, with the bundled index refreshed [E, `decisions/2026-09-16-haunt-gate.md`, D2, read from disk 2026-09-20] — is information about the **main characteristics and functionality** of digital content. [I, from Schedule 2 (a) and (v) as quoted]
2. Under s.36(3) it is therefore **a term of the contract**. [I]
3. Under s.36(4) a change to it *"made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader."* [E, quoted above]
4. v1.2 requires the amortisation period to **equal** the published commitment. Shortening the amortisation therefore requires shortening the commitment. [I, from the clause quoted at §1.0]
5. **So v1.2's *"the period may be shortened, never lengthened"* purports to permit, as against every consumer who has already bought, precisely the unilateral change s.36(4) renders ineffective.** [I]

**Three honest qualifications, because an overstated legal finding is worth less than a narrow one.**

- **Prospective-only reading.** The clause could be read as permitting shortening only for *future* customers. It does not say so. And on that reading the period would differ between cohorts while the clause speaks of a single product-level period that *"must equal"* a single published commitment — so the tie breaks and, on v1.2's own terms, the amortisation treatment falls away entirely and the whole remaining build goes to expense [I; the same structural point is reached independently by the CFO at `cost-sheet-v2.md` §5.5, third count]. **A constitution should not rely on a saving construction it does not state.** The defect stands on either reading.
- **Who the trader is, is undetermined.** Apple and Google are merchants of record for an app-store sale, and whether Candour is *"the trader"* for CRA purposes is an open Constitution 6.1 question already recorded as a **launch bar** [E, `decisions/2026-09-16-haunt-gate.md`, C3.6]. **The finding does not depend on resolving it.** If Candour is the trader, s.36 binds Candour directly. If it is not, the description is still Candour's and s.36 binds whoever supplies — in which case v1.2 licenses Candour to procure a change that is ineffective in the supply contract, which is not better. Either way the clause permits something that does not work.
- **This is agent analysis, not advice.** Constitution 6.1 [E, `constitution.md` line 154]: *"Agent reviews **prepare and flag; they do not certify**… The company never represents an AI compliance opinion as assurance."* The existing L1 launch bar — qualified human legal review — is the place this gets confirmed, and it is unchanged by this draft.

**Why this is decisive and the two fairness flaws are not.** Flaws 1 and 2 are arguments that the rule is *unwise*. A company may keep an unwise rule. Flaw 3 is that the rule, on its face, in a document Article 3 publishes *"Continuously"* [E, `constitution.md` line 79], grants a permission the law withholds. That is a defect in the document regardless of conduct, and Article 10's first bullet is the reason it matters here more than elsewhere: *"This constitution currently binds through publicity, not law. We say so plainly rather than implying legal force we don't have."* [E, `constitution.md` line 224] **A document whose entire force is publicity cannot afford a published clause that is wrong about the law.** [J]

### 1.4 What v1.2 got right, and what any replacement must keep

Its purpose is named at Correction C3.3(b) [E, `decisions/2026-09-16-haunt-gate.md`, C3.3]: stop the period being chosen to flatter a price. **That purpose is real and the replacement must keep it closed.** §5 shows it is closed better by fixity than by the ratchet, and §5.3 records that C3.3(b)'s stated *mechanism* was wrong even so.

---

## 2. The amendment — Definitions

### 2.1 Diff against v1.2

`[N]` is the **CFO's to propose and the CEO's to decide** (5.4). This seat does not fill it in. Everything else is drafted.

```diff
 ## Definitions

 These terms mean the same thing everywhere in this constitution and in every
 Candour document. Per Article 9, they may only change by public amendment.

-- **Cost:** everything it takes to run a product or the company, itemised —
-  hosting, tooling, support, third-party services, and labour valued at a
-  published market benchmark whether or not it is actually paid. **One-off
-  build labour is capital, amortised straight-line over the product's declared
-  supported life**, rather than charged wholly to its first year; maintenance
-  and support are operating costs. Three conditions bind that treatment: the
-  amortisation period must equal a **published** support commitment to
-  customers; any unamortised remainder is written off publicly on
-  discontinuation (7.2); and the period may be shortened, never lengthened.
-  Absent a published support commitment, build labour is a first-year
-  operating cost.
+- **Cost:** everything it takes to run a product or the company, itemised —
+  hosting, tooling, support, third-party services, and labour valued at a
+  published market benchmark whether or not it is actually paid. **One-off
+  build labour is capital, amortised straight-line over the standard
+  amortisation period**, rather than charged wholly to its first year;
+  maintenance and support are operating costs. Labour spent on work that does
+  not ship is not capital: it is an operating cost in the year it is incurred,
+  and where a product is abandoned before release the whole of its build
+  labour is written off publicly in that year.
+- **Standard amortisation period:** **[N] years**, straight-line, in equal
+  monthly amounts. It is **the same for every Candour product**, and no
+  product sets its own. It is **an accounting convention and nothing more**:
+  it is not a promise that a product will be supported, maintained or
+  available for that period, **no customer-facing commitment of any kind
+  attaches to it or is implied by it**, and it is never published as, or in
+  place of, the support statement Article 4 requires. What Candour owes a
+  customer when a product ends is fixed by Article 7.2 and does not depend on
+  how much of the build remains unrecovered. Four conditions bind the
+  treatment: the clock starts on the **earlier of a product's first sale and
+  its public release**, published on its first cost sheet and never restated;
+  **each capitalised increment runs its own clock from the date it ships**, so
+  a later increment never extends, restarts or re-bases an earlier one; any
+  unamortised remainder is **written off publicly on discontinuation** (7.2);
+  and every cost sheet publishes the schedule required by 2.1. The period
+  changes only by public amendment to this document (Article 11), never for
+  one product, and **a change applies only to increments capitalised after it
+  takes effect** — increments already running finish on the period they began
+  under.
 - **Profit:** income minus cost over a period.
```

### 2.2 The replacement, as running text for pasting

> - **Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and labour valued at a published market benchmark whether or not it is actually paid. **One-off build labour is capital, amortised straight-line over the standard amortisation period**, rather than charged wholly to its first year; maintenance and support are operating costs. Labour spent on work that does not ship is not capital: it is an operating cost in the year it is incurred, and where a product is abandoned before release the whole of its build labour is written off publicly in that year.
> - **Standard amortisation period:** **[N] years**, straight-line, in equal monthly amounts. It is **the same for every Candour product**, and no product sets its own. It is **an accounting convention and nothing more**: it is not a promise that a product will be supported, maintained or available for that period, **no customer-facing commitment of any kind attaches to it or is implied by it**, and it is never published as, or in place of, the support statement Article 4 requires. What Candour owes a customer when a product ends is fixed by Article 7.2 and does not depend on how much of the build remains unrecovered. Four conditions bind the treatment: the clock starts on the **earlier of a product's first sale and its public release**, published on its first cost sheet and never restated; **each capitalised increment runs its own clock from the date it ships**, so a later increment never extends, restarts or re-bases an earlier one; any unamortised remainder is **written off publicly on discontinuation** (7.2); and every cost sheet publishes the schedule required by 2.1. The period changes only by public amendment to this document (Article 11), never for one product, and **a change applies only to increments capitalised after it takes effect** — increments already running finish on the period they began under.

**The CFO's proposal recommends `[N]` = three years (36 months)** [E, `pipeline/amortisation-proposal.md` §0-A and §2, read from disk 2026-09-20]. This seat's verdict on that recommendation is at §6.4: **assent, with two disclosure fixes attached.**

### 2.3 Five drafting decisions, each with its reason

**(a) The period gets its own Definitions entry rather than living inside Cost.** Definitions is where company-wide constants belong, and Article 9's anti-redefinition row already protects that section by name. Burying a company constant inside the definition of another term is how it gets amended by accident. [J]

**(b) *"An accounting convention and nothing more"*, and the express denial of any implied commitment.** This is the load-bearing sentence and it is deliberately over-written. The whole point of the amendment is that the period stops being a promise; a reader who finds *"amortised over five years"* on a cost sheet must not be able to read it as *"supported for five years"*. **If the CEO trims one thing from this draft, it must not be this sentence.** [J]

**(c) The clock starts on the *earlier* of first sale and public release.** *(Revised at Revision 2 to adopt the CFO's `pipeline/amortisation-proposal.md` §3.2.)* Release to real users is already a named event in Constitution 5.4 [E, `constitution.md` line 117: *"release to real users"*], and it exists for free and non-profit products (Article 8) which have no first sale. **"Earlier of" rather than either alone, because "launch" is a soft enough word to move** — the CFO's V4 vector, now row 7 at §12.4. The date is published on the first cost sheet and never restated. [I]

**(d) The abandoned-work sentence is new and closes a hole v1.2 left open.** v1.2's fallback (*"absent a published support commitment, build labour is a first-year operating cost"*) disappears with the commitment, and without a replacement there is no stated treatment for hours spent on a product that never ships. The CFO has already met the case: a spike that returns *"don't build"* has no supported life to amortise over [E, `cost-sheet-v2.md` §2.2]. The sentence states what the CFO already does. [I]

**(e) A future change to `[N]` applies only to increments capitalised after it takes effect.** *(Revised at Revision 2. The first draft said "applies to every live product at its next republication" and **that was wrong** — the CFO caught it at `pipeline/amortisation-proposal.md` §3.4 before anyone acted on it, and the correction is recorded here rather than absorbed into a rewrite.)* Re-amortising existing increments over a **longer** period lowers prices retrospectively, which is harmless; over a **shorter** period it raises them, which is **flaw 2 re-created at company scale instead of product scale.** Prospective-only removes the direction that harms. Without any commencement rule at all, a future amendment could be timed to suit whichever product benefits — the residual vector fixity creates, given a row and a number at §12.4. [I]

**(f) Layers, adopted from the CFO.** Each capitalised increment runs its own clock from the date it ships [E, `pipeline/amortisation-proposal.md` §3.3]. This is the structural answer to re-badging a year of maintenance as a "v2" to open a fresh clock, and it has a consequence worth seeing now: **a product under continuous development does not have one cliff, it has a staircase.** That is more honest and harder to read, which is why the published layer schedule at §12.3 is not optional. **The CFO's 100-hour materiality floor is deliberately *not* in the Constitution** — it is a sensible convention that belongs in `pipeline/templates/cost-sheet.md`, and a number that granular in the Definitions would need an Article 11 amendment to tune. [J]

### 2.4 What the amendment does **not** do, stated so silence is not read as consent

- **It does not forbid Candour from publishing a support commitment.** It removes the accounting reason to publish one. A product may still make a dated support promise as a product decision; it is then contractual under CRA 2015 s.36(3) [E, §1.3] and it binds, with no constitutional consequence either way.
- **It does not touch Article 7.2.** 90 days' notice, free export throughout the notice period and for 90 days after, open-sourcing where third-party rights allow, and a published closing cost sheet all stand unaltered [E, `constitution.md` lines 173–180].
- **It does not change any Haunt price by itself.** Three of Haunt's four modelled prices are identical at two, three and five years; what the period moves is the subscriber count at which they are honest, and the pay-once price [E, `cost-sheet-v2.md` §5.2].
- **It does not settle whether Haunt should publish a five-year support commitment.** That becomes a pure product and contract question, which is the amendment's chief virtue. §7.

---

## 3. Consequential edits — every article checked, including the ones that need nothing

Checked in the order requested: **2.1, 2.3, 3, 7.2, 9, 10.** Article 9 is set out separately at §5 because it is substantial.

### 3.1 Article 2.1 — **one required edit, one recommended**

**Required.** The Definitions entry now points at 2.1 for the disclosure (*"every cost sheet states the build labour capitalised, the amount recovered to date, and the months remaining (2.1)"*), and 2.1 must actually carry it, or the cross-reference is to nothing. Current first bullet [E, `constitution.md` line 45]:

> *"Every product publishes a **cost sheet**: hosting, tooling, support, third-party services, and a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

```diff
-- Every product publishes a **cost sheet**: hosting, tooling, support,
-  third-party services, and a fair-market cost for labour (including the
-  founder's, whether or not it is actually drawn).
+- Every product publishes a **cost sheet**: hosting, tooling, support,
+  third-party services, and a fair-market cost for labour (including the
+  founder's, whether or not it is actually drawn). Where build labour is
+  capitalised, the cost sheet states the amount capitalised, the amount
+  recovered to date, the months remaining in the standard amortisation
+  period, and that the period is a company-wide accounting convention rather
+  than a statement about how long the product will be supported.
```

**The trailing clause is not decoration.** It is what stops the disclosure itself re-creating the implication the amendment removes. A cost sheet that says *"build amortised over [N] years, 14 months remaining"* and nothing else reads, to a customer, exactly like a support horizon. [J]

**Recommended, and separable — the cumulative-lifetime disclosure.** This follows from the determination at §8 and the CEO may take it, defer it, or reject it without affecting anything else in this draft. Current text [E, `constitution.md` line 47]:

> *"Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit against the cost of serving them."*

Proposed addition, at the end of that bullet:

> *"The cumulative position is published, not merely tested: every cost sheet for a recurring product states the cumulative margin on a subscriber at the end of the standard amortisation period and at twice that period."*

**Why.** The CFO has flagged twice that the cumulative test may be a no-op, and on every cost shape modelled to date the annual test breaches first by up to five years [E, `cost-sheet-v2.md` §8.3]. §8 settles the interpretation and finds the clause **rarely binds independently**. A clause that rarely binds is worth little as a test and a great deal as a **published number**: two figures on a cost sheet let a reader see a long-tenure subscriber's whole position without doing the arithmetic. This converts a rhetorical protection into an auditable one at a cost of two table rows. [J]

### 3.2 Article 2.3 — **no edit; one flag about a citation elsewhere**

The waterfall [E, `constitution.md` lines 57–66] allocates *profit*. Amortisation changes when a cost lands, not how profit is allocated once measured. Nothing in 2.3 reads wrong after the amendment. **No edit.**

**Flag, outside this amendment and cheap to fix while the file is open.** Haunt Condition 9.4 says *"Article 2.3.3.1 lands the cut on the **installed base**"* [E, `decisions/2026-09-16-haunt-gate.md`, Condition 9.4]. The obligation to cut the price when the build leaves the cost base comes from **Article 2.1** — the ~20% target and the 30% hard cap measured per financial year — not from 2.3.3.1, which sets the *order of preference for the remainder of profit* and is a supporting citation rather than the operative one. The point Condition 9.4 makes is right; the clause it hangs on is the wrong one. Correctable in the same C5 pass at §7. **Flag, not a block** — it changes no number and no decision.

### 3.3 Article 3 — **no edit**

The transparency schedule [E, `constitution.md` lines 74–81] carries *"Product cost sheets and margins — At launch, at every price change, and at least annually"* and *"This constitution and its full change history — Continuously"*. The new disclosures ride on the existing cost-sheet row; the amendment itself rides on the change-history row. v1.2 never listed a support commitment in Article 3, so nothing is orphaned by removing it. **No edit, and this was checked rather than assumed.**

### 3.4 Article 7.2 — **one recommended edit**

Article 7.2 [E, `constitution.md` lines 173–180] requires *"A published closing cost sheet for the product's final period."* The Definitions entry sends the write-off of the unamortised remainder to 7.2, but 7.2 does not name it, so the obligation exists only by cross-reference from Definitions.

```diff
 - A published closing cost sheet for the product's final period.
+ - A published closing cost sheet for the product's final period, stating the
+   build labour capitalised, the amount recovered from customers to date, and
+   the unamortised remainder written off.
```

**Why it is worth the line.** This is the single number that exposes the early-discontinuation vector, and Article 9's commitment is to *"publish the numbers that expose each one"* [E, `constitution.md` line 206]. A write-off obligation that lives only inside a definition of an accounting term is where a reader will not look. **Strengthening**, and it costs nothing because the CFO would compute the figure anyway.

### 3.5 Article 10 — **no required edit; one optional addition offered in Article 10's own register**

Nothing in Article 10 reads wrong after the amendment. In particular, the deliberate gap named in its fourth bullet — that the Constitution says nothing about *"a product limiting a customer's access to content that customer authored and holds on their own device"* [E, `constitution.md` line 227] — is untouched, and this amendment must not be read as filling or narrowing it. **No required edit.**

**Optional, and offered because Article 10 is the article for exactly this.** A single company-wide period is, for any individual product, an approximation. Article 2.1 requires that *"each product's customers get that product's honest number"* [E, `constitution.md` line 48]. The tension is real (§6.3) and the answer is disclosure rather than denial:

> *"The standard amortisation period is one number applied to every product, chosen because a period chosen per product is a period chosen to suit a price. It is therefore, for any particular product, an approximation of nothing in particular — it does not claim to track how long that product will live or be supported. We say so here because a cost sheet showing a build cost spread over a fixed term invites exactly the opposite reading, and because the alternative — a period tuned per product — is the loophole this convention exists to close. What a customer is owed when a product ends is in Article 7.2, and does not move with this number."*

**This seat recommends taking it.** [J] It costs one paragraph, it is honest, and it pre-empts the single most likely misreading of the new clause. But it is optional: the amendment is coherent without it, and Article 10 should not become a commentary on every clause.

### 3.6 Also checked, and clean

- **Definitions preamble** — *"Per Article 9, they may only change by public amendment"* [E, `constitution.md` line 19]. The new entry inherits this automatically; §5 extends Article 9's naming row so the protection is explicit rather than merely inherited.
- **Articles 1, 4, 5, 6, 8, 11** — no dependency on the amortisation clause. Article 8's non-profit annex constrains distribution and sale, not cost treatment; a non-profit initiative amortises like any other product and its price is limited by its own annex, which is stricter.
- **`pipeline/templates/cost-sheet.md`** — will need the new disclosure rows. Template change, not a constitutional one; cheap, and owed at the same time [E, `pipeline/templates/`, listed from disk].

---

## 4. The Article 11 classification

**This is the part of the draft the CEO should read most sceptically, because it is the part where this seat's recommendation runs against the CEO's framing.** It is stated once, in full, and then it is the CEO's decision under 5.4 and 11.1.

### 4.1 The question Article 11.2 actually asks

Article 11.2, quoted in full [E, `constitution.md` line 235]:

> *"Amendments that **weaken** a customer-facing or transparency rule must be explicitly labelled 'WEAKENING' in the change log and include the reason."*

Three things follow from the text, and they matter because each is a place the argument could go wrong.

1. The trigger is **the character of the rule**, not the size of the change and not the motive behind it. There is no materiality threshold and no good-faith exception.
2. The trigger contains **no reliance element**. It does not ask whether a customer relied, or could have relied, or existed.
3. The consequence is **a label and a reason** — not a prohibition. Article 11.2 does not stop a weakening. It makes one findable.

Point 3 is the one that should govern the CEO's decision, and it is why this seat holds no block here. **The question is not whether to permit this amendment. It is whether a reader of the change log will be able to find what was taken away.** [I]

### 4.2 What is removed, stated precisely enough to be argued with

Not *"the five-year support commitment"* — that is D2, a product decision, and §7 deals with it separately. What the amendment removes from the **Constitution** is this:

> **The structural condition that a product could be priced on amortised build labour only if Candour had published a dated support commitment to its customers.**

And the practical consequence of that condition, which is what makes it customer-facing rather than merely internal: absent a published commitment, *"the £45,957.55 build is a first-year expense and every price roughly triples"* [E, `decisions/2026-09-16-haunt-gate.md`, D2 consequences, read from disk 2026-09-20 — the build figure has since moved to £74,532.04 at `cost-sheet-v2.md` §2.2, which makes the multiple larger, not smaller]. **So under v1.2, any Candour product sold at a defensible consumer price necessarily carried a published, dated, contractual support promise.** After v1.3, no product is required to publish any support commitment at any price. [I, from the clause at §1.0 and the CFO's arithmetic]

### 4.3 The three respects in which this amendment strengthens

**(a) It removes a permission to do an unlawful thing.** *"The period may be shortened, never lengthened"* permits shortening a published commitment which, once sold against, is a contract term that s.36(4) makes unchangeable without the consumer's express agreement [E, §1.3]. A constitution that removes its own permission to act unlawfully has strengthened. [I]

**(b) It removes the per-product choice of period — and with it both a gaming vector and a penalty on honest under-promising.** The vector is named at C3.3(b) and the penalty is priced at §1.1. Both exist only because the period was chosen per product; fixity closes both at once. [I]

**(c) It adds three published numbers where there were none** — build labour capitalised, recovered to date, months remaining (§3.1) — plus the unamortised remainder at the closing cost sheet (§3.4). On the **transparency limb** of 11.2 this amendment is unambiguously a strengthening. [I]

### 4.4 The strongest argument against my conclusion, put at full strength

**It is this, and it is better than either "the commitment was never the protection" or "it was legally unsound".** Both of those are weak — see §4.5. The strong one is:

> **v1.2 never guaranteed any customer a support commitment. It offered Candour a choice.** Its final sentence — *"Absent a published support commitment, build labour is a first-year operating cost"* — expressly contemplates products with no commitment at all. Candour could always have declined the capitalised treatment, published nothing, and charged more. A rule Candour could lawfully opt out of at any time, unilaterally and without telling anyone, is an **incentive**, not a protection. Removing an incentive is not weakening a rule.

**That argument is substantially right, and it is the reason this is a narrow weakening rather than a large one.** [I]

**Why it does not carry the day.** An incentive that cannot realistically be declined functions as a rule. The price multiple — *"roughly triples"* on the company's own published arithmetic — is not a choice a consumer software company makes twice. [I] And Article 11.2's test is not *"was the rule absolute"*; it is whether a customer-facing rule is weakened. A rule that bound in every case where the price was defensible is a rule. **The honest way to hold the argument is: v1.2 made the commitment near-certain, and v1.3 makes it entirely optional. That is a reduction, and it is nameable in one sentence, which is the test that matters.** [J]

### 4.5 Two arguments this seat has been offered and does not accept

**"The commitment was never the protection — Article 7.2 is."** Article 7.2 is untouched and it is a real protection [E, `constitution.md` lines 173–180]: 90 days' notice, free export throughout and for 90 days after, open-sourcing where rights allow, closing cost sheet. **But 7.2 and a support commitment protect different things, and the difference is exactly the case a customer would complain about.** 7.2 governs *how a product ends*. A support commitment governs *whether it keeps working*. A product can comply with 7.2 perfectly while running on a two-year-old OS, unpatched, with a stale index, for as long as its owner likes — because it has not been discontinued, so no notice is owed and no clause engages. **7.2 covers the shutdown case and does not cover the rot case.** Saying 7.2 is "the real protection" is true of endings and false of continuity. [I, from the text of 7.2 and of D2's definition of what a support commitment buys]

**"The clause was legally unsound, so it was never a protection."** This conflates two halves of one clause that point in opposite directions. The **unlawful** half is *"may be shortened"* — the permission to take the commitment away, which is the anti-customer half. The **lawful** half is *"the amortisation period must equal a published support commitment"* — the requirement to make the commitment, which is the pro-customer half and is unimpeachable. s.36 does not touch it. **The illegality argument, correctly applied, shows that v1.2 understated the customer's protection, because the escape hatch it advertised did not work.** It is an argument that the clause was *better* for customers than it read, not that it was empty. Deleting the whole clause deletes both halves. [I, from §1.3]

### 4.6 Why the Correction C1.6 precedent does not transfer

The CEO and CVO settled a classification against this seat's recommendation on 2026-09-16, on three grounds [E, `decisions/2026-09-16-haunt-gate.md`, C1.6]. **All three were sound there. None of them reaches this case, and the reasons are structural rather than rhetorical.**

| C1.6's ground | Why it does not transfer |
|---|---|
| **1.** *"Condition 8 was a **claim about what the Constitution requires**, and that claim was false. Correcting a misstatement of the rules is not amending them."* | v1.2's Cost definition is not a claim about the rules. **It is the rule**, validly adopted at v1.2 by the route Article 11 prescribes. There is nothing false to correct. |
| **2.** *"**This record has never been published.** Publication is due 2026-10-16. No customer has seen the rule, nobody has relied on it."* | The **Constitution is published continuously** — Article 3, row 4: *"This constitution and its full change history — Continuously"* [E, `constitution.md` line 79]. v1.2 has been public since 2026-09-16. This is the load-bearing difference between the two cases. |
| **3.** *"WEAKENING asserts that Candour reduced a protection it properly owed. It did not — it mistakenly claimed to owe one."* | Candour **properly owed** this one. It was in the Constitution, by amendment, with a published rationale. Ground 3 is an argument against *false* self-criticism; here the self-criticism is true. |

C1.6 also recorded the limit of its own holding, and it is worth quoting because it anticipated exactly this: *"**Had this correction come after publication, the classification would be different**, and that is stated here so the distinction cannot be borrowed later for a case it does not fit."* [E, ibid.] **This is a case it does not fit.** [I]

### 4.7 Is there a third label, as at Correction C3?

Correction C3 invented **SUPERSESSION** for a decision record, for a decision the CEO changed his mind about where nothing was false [E, `decisions/2026-09-16-haunt-gate.md`, C3]. It is a good category and it is the right one for D2 (§7.3).

**It is not available here.** Article 11's text provides two things and only two: every amendment is recorded with *"date, diff, and rationale"* (11.1), and weakening amendments carry a label and a reason (11.2) [E, `constitution.md` lines 234–235]. **Inventing a third constitutional category inside an amendment that does not amend Article 11 would be doing quietly the thing Article 11 exists to stop.** If the CEO wants a third category, the honest route is to amend Article 11 expressly, in this same amendment, labelled and reasoned. This seat does not recommend it: two labels are enough, and a third would most likely be used to avoid the second. [J]

### 4.8 Determination — as it stood before D4, and as it stands now

**Before D4** (the amendment alone, no Article 4 duty): *"a WEAKENING of one customer-facing rule under Article 11.2, and simultaneously a strengthening of three others. The label is owed."* **That was this seat's recommendation and it is preserved here rather than deleted**, because §12.1 turns on it.

> ### **After D4, with Option B adopted: no WEAKENING label is owed.**

**The reasoning, and it is not that the CEO accommodated the seat.** Option B does not compensate for the loss with something unrelated. **It changes what is lost.** Set the two side by side:

| | v1.2 | v1.3 + Option B |
|---|---|---|
| What a customer gets | A dated support commitment, **near-certain** because declining it multiplied the cost base by 2.23× | A **mandatory, unconditional statement** of the support position — a date, or plainly that no date is committed — on **every product, at every price** |
| When | Only where the product was priced on amortised build labour | Always. There is no configuration in which a Candour product is silent |
| Could Candour avoid it? | Yes, by expensing the build and charging roughly three times more | **No.** Article 4 admits no exception: *"Every product must, without exception"* |

**The decisive fact, and it is new evidence since §4 was first written.** D4 records the CEO's reason in his own words: *"what if something happens if I am unable to support a product until the date… if I don't have the time or money?"* [E, `decisions/2026-09-16-haunt-gate.md`, D4, read from disk 2026-09-20]. **v1.2 therefore attached a 2.23× cost penalty to declining to publish a date the company has now said in writing it cannot guarantee.** A rule whose only compliant path runs through a promise you cannot keep is not a customer protection — it is a mechanism for manufacturing a future public breach. **Removing it and replacing it with a duty to state the truth either way is Article 1.3 operating as designed:** *"Honest by default. Pricing, capability, and limitations are stated plainly. **We say what a product cannot do.**"* [E, `constitution.md` line 34] [I]

**The residual, stated plainly rather than argued away, because it is real.** A customer who would have received a *promise* under v1.2 may now receive a *disclosure* that no promise is made. **That is a difference and it is not nothing.** It is named in the change log (§9) without the 11.2 label, on this ground: **11.2 asks whether a customer-facing rule is weakened, and the rule here is not weakened but replaced by one that binds in strictly more cases and can never be opted out of.** A rule that always applies and always tells the truth is not a weaker rule than one that usually applied and could require a lie. [I]

**Applying the test I set myself at §4.2, in its own terms:** *is there anything the v1.2 reader could rely on that the v1.3 reader cannot?* The v1.2 reader could expect **that there would be a commitment**. The v1.3+B reader can expect **to be told, before buying, whether there is one**. The first expectation was stronger in one dimension and, on the CEO's own evidence, could not have been honoured. **The v1.3 reader's expectation is weaker in that dimension and is one Candour can actually meet on every product it will ever ship.** [I]

### 4.9 Option B, as adopted at D4

**Adopted by the CEO on 2026-09-20 (D4).** Haunt takes the second limb: *"no guaranteed support date"* [E, ibid.]. The finalised Article 4 text is at **§12.2**. What follows is the original framing, preserved because §12.1 and the change log refer to it.

**Offered because a seat that identifies a loss and proposes no remedy has done half a job.** If the CEO's objection to the label is that he does not want to reduce customer protection — as opposed to not wanting the word — there is a clean way to have both, and it is cheap:

> **Add to Article 4** (product ethics, which is the correct home for a customer-facing publication duty): *"State, before first sale, the date until which the product will be supported — or state plainly that no such commitment is made. Either is honest; silence is not."*

**What this achieves.** The accounting decoupling survives intact: the amortisation period remains a company-wide convention attached to no promise. But the customer-facing protection is not merely preserved, it is **improved**, because under v1.2 the commitment was near-certain-but-optional and under Option B it is a duty to *either* commit *or* say plainly that you are not committing — which is the Article 1.3 answer (*"Pricing, capability, and limitations are stated plainly. We say what a product cannot do."* [E, `constitution.md` line 34]).

**Classification under Option B: no WEAKENING label is owed. The amendment becomes a net strengthening on every limb.** [I]

**The cost of Option B, stated so it is not adopted as free.** A published support date is contractual under CRA 2015 s.36(3) [E, §1.3] and frozen by s.36(4). **A duty to publish one, or to publish a disclaimer, forces every product to make that choice in public before its first sale** — which is the point, and which the CEO may reasonably not want on a first product built by one part-time person. The disclaimer branch is a real branch and is not a loophole: *"Haunt makes no dated support commitment"* is an honest, publishable sentence, and a customer can price it.

**This seat's recommendation, in order of preference:** Option B; failing that, the amendment as drafted **with** the WEAKENING label at §4.8. **Against:** the amendment as drafted without the label.

### 4.10 What would overturn this determination, and where I looked

*(Required by `roles/cgo.md` as amended [E, read from disk 2026-09-20]: a negative finding carries a block's duty.)*

**Overturned by any of:**

1. **An independent obligation, outside the Constitution, that already requires Candour to publish a support period for every product.** If one exists, v1.2's condition was adding nothing and its removal takes nothing. **I looked and did not find one.** Apple's guideline 3.1.2(a) ongoing-value requirement concerns what an auto-renewing subscription must deliver, not a published support horizon [E, as characterised at `decisions/2026-09-16-haunt-gate.md` Condition 9.7; the guideline itself was **not re-retrieved this session** and is carried as **[K], medium confidence** — flagged, and it is not load-bearing here because the finding is that no such duty was found]. The DMCCA duties determined at source in `subscription-compliance-note.md` concern pre-contract information, reminders, cooling-off and refunds, not support horizons [E, as recorded at `decisions/2026-09-16-haunt-gate.md` Condition 9.6 and C3.4–C3.6]. CRA 2015 s.36 makes a commitment binding **if given**; it does not require one to be given [E, s.36 text at §1.3].
2. **A demonstration that v1.2's commitment condition was already a dead letter** — e.g. that Candour would in fact have published no commitment and charged the tripled price. The CEO is the only person who can give that evidence and D2 is evidence to the contrary.
3. **Adoption of Option B**, which removes the weakening rather than rebutting it.

**Where I looked:** `constitution.md` in full (v1.2, all eleven articles, Definitions and Preamble); `CHANGELOG.md` v1.0–v1.2; `decisions/2026-09-16-haunt-gate.md` in full including C1–C4 and the CEO decisions log; `pipeline/templates/decision-record.md` classification test; `pipeline/evidence-standard.md`; `pipeline/governance-review-2026-09.md`; `products/haunt/cost-sheet-v2.md` §0, §2, §5, §8, §13, §14; CRA 2015 s.36 and SI 2013/3134 Schedules 1 and 2 at source.

**What would *not* overturn it:** that no customer has yet bought anything (Article 11.2 has no reliance element, §4.1); that the amendment is on balance good (it is — §0.2; 11.2 is not a net test); that the CEO's motive is honest (11.2 has no motive element).

---

## 5. Article 9 — the loophole table

Article 9's commitment [E, `constitution.md` lines 204–218]: *"We name our own loopholes, and publish the numbers that expose each one… If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."*

### 5.1 One edit to an existing row

```diff
-| Redefining "cost," "surplus," "reserve," or "net proceeds" | Definitions may only change by public amendment (Article 11) |
+| Redefining "cost," "surplus," "reserve," "net proceeds," or the standard amortisation period | Definitions may only change by public amendment (Article 11), and a change to the period publishes its effect on every live product |
```

**Why.** The new entry inherits the Definitions preamble's protection automatically, but Article 9's job is to name things, not to rely on inheritance. The period is now the single number with the largest leverage on every published price in the company. [J]

### 5.2 Four new rows

| Loophole | The number that exposes it |
| --- | --- |
| **Setting or amending the standard amortisation period to suit whichever product is being priced at the time** (Definitions) | The period is fixed company-wide and changes only by public amendment. Every change publishes, **for every live product**, the build labour still unrecovered at the moment of change and the resulting price effect on each — so a change made for one product is visible in the other products' numbers |
| **A one-off or pay-once tier escaping the cumulative lifetime margin test (2.1)**, which constrains only what a subscriber pays *by staying* | The **annual** margin on every tier, **including one-off tiers**, published at every republication — with one-off revenue recognised over the standard amortisation period rather than in the year of receipt. Recognised on receipt, a pay-once tier shows +243.4% in the year of purchase, which is what makes the escape visible |
| **Recovering the build quickly and then discontinuing the product once it is recovered** | The closing cost sheet's **unamortised remainder written off** (7.2), against the amortisation start date. An early discontinuation showing a write-off of zero is a product whose customers paid for the whole build and did not get the product |
| **Running a product past the end of its amortisation period without reducing the price**, once the build has left the cost base | Every cost sheet states build labour capitalised, recovered to date, and **months remaining**; the first republication after the period ends shows the cost base falling, and Article 2.1's annual margin test shows the price that must follow |

### 5.3 The two rows owed from Correction C3.3 — carried, and one of them corrected

Correction C3.3 [E, `decisions/2026-09-16-haunt-gate.md`, C3.3, read from disk 2026-09-20] recorded two vectors for the next amendment. **This is that amendment. Both are disposed of here.**

**C3.3(a) — the pay-once tier outside the cumulative test. Carried, unchanged in substance, at row 2 above.** The amendment does not touch it: the cumulative lifetime test constrains *"what a subscriber pays by staying"* [E, Article 2.1, `constitution.md` line 47] and a one-off purchase involves no staying, at any amortisation period. The exposing number is the CFO's, from `cost-sheet-v2.md` §8.5 [E, read from disk 2026-09-20]: cumulative margin on a pay-once buyer at the reference count runs **+243.4% at one year, +16.8% at five, −26.3% at ten** — it *falls* with tenure, so the cumulative test never catches it and the annual test catches it in the year of purchase, hard. The accounting answer the CFO states and this seat adopts: **one-off revenue is recognised over the amortisation period, not on receipt.** Row 2 makes that an Article 9 exposing number rather than a convention someone has to remember.

**C3.3(b) — *"declaring a long supported life flatters the cost base"*. Does not survive, for two independent reasons, and the second is the awkward one.**

**Reason 1 — the amendment removes the act.** C3.3(b) describes *declaring* a supported life. After v1.3 no product declares anything: the period is one number, company-wide, changeable only by public amendment. **The vector as described is not available to anyone.** [I]

**Reason 2 — its stated mechanism runs in the wrong direction on the CFO's own arithmetic, and this would have been true with or without the amendment.** C3.3(b) says a long life *"flatters the cost base, raising the compliant margin at any subscriber count"*. On `cost-sheet-v2.md` §5.1 [E, read from disk 2026-09-20]:

| | L = 2 | L = 3 | L = 5 |
|---|---|---|---|
| Amortised build per year | £37,266.02 | £24,844.01 | £14,906.41 |
| Honest monthly price at N = 8,998 | £1.341 | £1.146 | **£0.990** |
| 99p hits the 30% hard cap at | 21,038 | 16,101 | **12,152** |

**A longer life lowers the annual charge, lowers the cost base, and therefore lowers the price a product is permitted to charge** — and at a price fixed at 99p it makes the 30% cap bite at *fewer* subscribers, not more. **Long is the stricter direction, not the flattering one.** The price-raising direction is **short**, and the CFO states it plainly at `cost-sheet-v2.md` §5.5: *"Shortening raises prices. Lengthening lowers them."* [E] **That sentence corrects C3.3(b) and does not say so.** I record it here because an uncorrected error in a decision record that publishes on 2026-10-16 is exactly what Article 9's quiet-weakening row is about, and because C3.3(b) is currently the stated justification for the ratchet this amendment removes — a bad reason for removing a clause is still worth replacing with the right one.

**What survives of C3.3(b), corrected:** the *shape* it identified — declare a period, price against it, then discontinue early — is real. The direction is inverted: the harm comes from a **short** period recovered fast, after which discontinuation costs the company nothing and costs the customer the whole build. **That corrected vector is row 3 above**, and the exposing instrument C3.3(b) proposed is still the right one, with one substitution: *"the published commitment date against the actual discontinuation date"* becomes **the amortisation start date against the actual discontinuation date**, because there is no commitment date any more.

**Confidence and independence.** The arithmetic above is the CFO's, re-derived from its own stated formula `C(N) = A/N + s` and its own table, by this seat, as Haunt Condition 6 requires [E, `decisions/2026-09-16-haunt-gate.md`, Condition 6: *"Arithmetic — plus any claim that a named clause of the Constitution or of law requires or forbids something — is re-derived in every future pack by a seat other than its author"*]. **The direction finding is arithmetic, not interpretation, so re-derivation by a second seat is genuinely independent here** — the distinction the evidence standard draws [E, `pipeline/evidence-standard.md`]. The CFO should nonetheless confirm it, because it corrects the CFO's own record and a seat should not have its error corrected without being told.

### 5.4 One further row, the CFO's, offered but not adopted by this seat

`cost-sheet-v2.md` §13 proposes a shared-cost allocation rule and a matching Article 9 row: *"Charging one product 100% of a shared company cost — exposed by every cost sheet stating the number of live products the shared-cost allocation was made across"* [E, read from disk 2026-09-20]. It is sound, it is 0.42% of Haunt's cost base, and **it is not part of this amendment.** Adopting it here would bundle two unrelated changes into one Article 11 entry, which makes the change log harder to read and the diff harder to audit. **Recommendation: take it as its own amendment at the same sitting, or defer it — the CFO's own point is that it should be settled while no price depends on it, and that remains true next month.** [J]

---

## 6. The conformance check on the period — tests, not a verdict

**This seat does not set the period and does not know the CFO's number.** `pipeline/amortisation-proposal.md` was not on disk when this was written. What follows is what the chosen period must survive, written so it can be applied to any number, plus the one problem visible without the number.

### 6.1 Six tests the CFO's proposal should answer

**T1 — the reason for the number must not mention a price.** *(The sharpest test, and the one most likely to fail.)* The whole point of fixity is that the period cannot be chosen to flatter a price. **But it is being chosen now, at the one moment in Candour's history when exactly one product exists and its prices have already been modelled at two, three and five years.** If the stated reason for `[N]` is *"because it is the period at which Haunt's ladder works"*, then row 1's vector has been run once — legitimately in form, at the moment of the convention's creation — and every future reader will be able to see it in the dates. **The CFO must be able to state the reason in terms that do not reference Haunt's prices at all**, and the change log must carry that reason (§9). This is a flag on the *rationale*, not on any particular number: three years may well be right for reasons that have nothing to do with Haunt.

**T2 — both tails.** Name a plausibly short-lived Candour product and a plausibly long-lived one, and state what `[N]` does to each. A fixed period is defensible only if it is tolerable at both ends, because there is no per-product escape by design.

**T3 — the cliff becomes a company-wide cadence.** At month `12[N]+1` every product's build leaves its cost base and Article 2.1's annual test forces a price reduction; on Haunt's five-year modelling that is **20.2%**, and at two years **30.3%** [E, `cost-sheet-v2.md` §5.4]. Apple performs the cut on the installed base automatically and *"you don't have the option to preserve the higher price for existing subscribers"* [E, as quoted at `decisions/2026-09-16-haunt-gate.md` Condition 9.4]. **Is the resulting cadence one Candour can execute across several products at once?** It is now the same month-count after release for all of them, which is either an administrative convenience or a pile-up, depending on launch spacing.

**T4 — which routine do we want: routine write-offs, or routine price cuts?** If `[N]` is longer than a typical product life, the 7.2 write-off happens on most discontinuations and **stops being a signal** — Article 9's row 3 instrument degrades. If `[N]` is shorter than typical life, the post-period price cut happens on most products and becomes ordinary. **One of these will be routine. The CFO should say which, deliberately, rather than discovering it.**

**T5 — Article 2.1's honest-number requirement.** §6.3.

**T6 — a forward flag, tagged as the guess it is.** At incorporation, Candour's statutory accounts will be prepared under whatever UK accounting framework applies, which has its own rules on capitalising and amortising development costs. **I have not retrieved those rules and I am not going to assert them from memory** — any statement about them here would be a citation without a retrieval, which `pipeline/evidence-standard.md` treats as fabrication. [K, low confidence] is that a constitutional convention and a statutory treatment could diverge, and that divergence would need reconciling rather than hiding. **This is a question for the CFO and ultimately for Constitution 6.1 human review at incorporation, not a finding.** Article 10's second bullet already covers the present position: the company is not incorporated and these are *"commitments about the future"* [E, `constitution.md` line 225].

### 6.2 What this seat can confirm about the period, whatever it is

- **A fixed period does not create cross-subsidy.** Article 2.1: *"Margins are per product, never averaged across the portfolio"* [E, `constitution.md` line 48]. Each product still amortises **its own** build over the common period. No product's build lands on another product's customers. Checked, because it is the first thing a sceptical reader will ask about a company-wide number.
- **The Article 8 annex is unaffected.** A non-profit initiative amortises like any other product and remains bound by its stricter annex [E, `constitution.md` lines 192–200].
- **Three of Haunt's four prices do not move with the period** — monthly 99p, quarterly £2.59, yearly £9.89 are the same at two, three and five years; what moves is the subscriber count at which they are honest, and the pay-once price [E, `cost-sheet-v2.md` §5.2]. **So the period decision is lower-stakes on price than it looks, and higher-stakes on volume.**

### 6.3 The one problem I can see regardless of the number

**A single company-wide period is, for any individual product, an approximation of nothing in particular.** Set against Article 2.1 [E, `constitution.md` line 48]:

> *"Margins are per product, never averaged across the portfolio: **each product's customers get that product's honest number**, and no customer subsidises another product unknowingly."*

Under v1.2 the amortisation line on a cost sheet at least *claimed* to correspond to something about that product — its declared supported life. Under v1.3 it corresponds to a company convention. **The line on the cost sheet is no longer a measurement of anything product-specific, and Article 2.1 asks for that product's honest number.** [I]

**Why this is a disclosure problem and not a defect in the amendment.** The alternative — a period that genuinely tracks each product's life — is precisely the per-product choice that produced C3.3(b), the under-promising penalty and the s.36 problem. **An honest approximation, labelled as an approximation, is better than a bespoke figure chosen by the party who benefits from it.** [J] That is the trade the amendment makes and it is the right one.

**What it requires, and both are already drafted:** the cost-sheet sentence at §3.1 (*"…and that the period is a company-wide accounting convention rather than a statement about how long the product will be supported"*), and the optional Article 10 paragraph at §3.5. **§3.1 is required. If the CEO also takes §3.5, this problem is closed rather than merely disclosed.** [J]

### 6.4 T1 applied to the CFO's proposal — **PARTLY ANSWERED, and it does not block**

*(What follows in italics was written **before** the CFO's proposal existed, and is preserved unchanged so the prediction can be marked against the answer. The verdict follows it.)*

*(Stated in advance, per the instruction that disagreement is a deliverable, so that it is on the record before the CFO's number arrives rather than after.)*

**If `pipeline/amortisation-proposal.md` argues for `[N]` primarily from Haunt's ladder arithmetic, this seat will flag it — not block it — as failing T1**, and will ask that the change log record both the arithmetic reason and the fact that only one product existed when the convention was set. **That is a disclosure remedy, not an objection to the number.** The CFO's `cost-sheet-v2.md` §14.1 recommendation of three years rests substantially on *deliverability* — whether 360 hours a year of maintenance will actually happen — which is a reason about Candour rather than about Haunt's prices, and would pass T1 as stated [E, read from disk 2026-09-20]. **Under this amendment that reason weakens, because the period no longer promises anyone any maintenance at all.** The CFO will need a different reason, and should be told so before writing rather than after.

#### The verdict, after reading `pipeline/amortisation-proposal.md`

**The prediction held and the CFO acted on it before being told.** §2.4 of the proposal states: *"The deliverability argument — 'will Candour actually do 360 hours a year for five years?' — is now irrelevant and I have dropped it. It was an argument about keeping a **promise**. There is no promise."* [E, read from disk 2026-09-20] **That is the right call, made unprompted, and it is the single most persuasive thing in the proposal** — a seat that drops its own prior reason when the reason stops working is a seat whose remaining reasons are worth more. [J]

**What the CFO then put in its place is genuinely independent of Haunt, and two of the three are retrieved at primary.**

- **Apple:** apps *"must be built with Xcode 26 or later using an SDK for iOS 26…"*, in force 28 April 2026; the prior requirement ran from 29 April 2024 [E, cited by the CFO at proposal §2.2 with a retrieved link to developer.apple.com — **single source by nature**, Apple being the only publisher of Apple's rules].
- **Google:** from 31 August 2026 apps *"must target Android 16 (API level 36) or higher"* [E, ibid. — **single source by nature**].
- **SI 2008/410 Sch 1 para 22:** where useful life cannot be reliably estimated, an intangible is written off over *"a period chosen by the directors"* not exceeding ten years, and the directors must disclose *"the period… and the reasons for choosing that period"* [E, ibid.]. **This is the strongest part of the argument and it is structural rather than numerical:** it establishes that "a chosen period, published with its reasons" is a recognised and respectable answer where a life cannot be forecast — which is exactly Candour's position, and exactly what this amendment does.

> ### **Verdict: PARTLY ANSWERED. The objection is substantially reduced, it no longer warrants holding up the CEO's assent, and I recommend assent to three years. It does not dissolve, and the residue is precisely locatable.**

**Where the residue is.** The retrieved platform evidence establishes a forced-rework cadence of **one year**. The step from *"the platforms force an annual pass over the build"* to *"three years is where the capitalised build stops describing the running code"* is an inference the CFO correctly tags **[I]** and correctly names as *"the weakest load-bearing claim in this document"* (§11). **That inference brackets the answer; it does not select within the bracket.** Three annual passes is not a reason to prefer three years over two or four — nothing in Apple's or Google's requirement distinguishes them. What the independent evidence genuinely rules out is **one** (no amortisation at all) and **ten** (indefensible for consumer mobile software on that cadence), and it argues against **five** via the write-off asymmetry, which is arithmetic and independent. **So the bracket is roughly two to four, and within it the deciding work is done by Haunt.**

**Two places where that is visible in the proposal's own text:**

1. **The 2-year rejection at §2.3 has two clauses and the second is Haunt** — *"On Haunt it raises the volume at which 99p is honest by 73% and puts an irreversible 30.3% cut at month 25."* The first clause, *"shorter than the interval over which the platforms force the work"*, does not survive its own evidence: the platforms force the work **annually**, so a two-year period already contains two forced passes. **There is no principled line in the retrieved evidence between two passes and three.**
2. **The self-test at §2.4 reaches the honest answer and marks its own weakness** — asked whether three years would suit a £5,000 web tool with no app store, the CFO answers *"Yes, but for a weaker reason: dependency and framework turnover rather than store policy, which I have not retrieved evidence for."* **For any Candour product that is not a mobile app, the entire independent limb of this argument is absent.** Since the convention binds every product Candour ever ships, that is not a footnote.

**What I am explicitly not saying.** I am not saying the number is wrong, that it was reverse-engineered, or that the CFO concealed anything. §0-B, §2.4 and §11 volunteer every one of these points before I reached them, which is the behaviour the evidence standard exists to produce. **And the commitment at §2.4 is the right one and I accept it: *"Had three years made Haunt unshippable I would have said so, and I would still have recommended three."*** My objection was that the period might be *selected* to suit a price. The proposal shows it was selected on external grounds **within a bracket those grounds define**, with Haunt deciding a residual the evidence leaves open. **That is a materially different and much smaller thing than the vector I named.**

**I also record that my T1 test as I wrote it was too strict**, and this seat should say so rather than let a badly-drawn test convict a good answer. I wrote that *"the reason for the number must not mention a price."* **On an unincorporated company with one product and no measured year of anything, no such reason exists for any number** — a test nothing can pass is a wrong test, which is the same reductio this company already ran on Article 4's export clause at Correction C1.1. **The right test is the one the CFO actually met: state which parts of the reason are independent of any product, state which are not, and publish both.**

#### The two fixes, and they are cheap

> **Fix 1 — the separation goes in the public change log, not only in an internal proposal.** Article 11.1 requires *"date, diff, and **rationale**"* [E, `constitution.md` line 234]. The rationale currently lives at `pipeline/amortisation-proposal.md` §2.4, which is not the change log. **Move its substance into the `CHANGELOG.md` entry in the CFO's own terms**, including the three sentences a sceptical reader most needs: that the deliverability argument was dropped; that the independent evidence brackets rather than selects; and that **only one product existed when the convention was fixed, and its numbers acted as a sanity check within the bracket.** Drafted at §9, item 2. **This is Article 9's own method applied to ourselves — name the vector, publish the number** — and it is also, exactly, what SI 2008/410 para 22(4) requires of the directors whose precedent the CFO is relying on. Relying on that precedent while omitting its disclosure limb would be selective.

> **Fix 2 — one scheduled, prospective-only revisit.** The CFO names the cheapest evidence that would improve this decision and dates it: *"A measured Candour maintenance year… becomes observable for the first time [at] launch + 12 months"* (`pipeline/amortisation-proposal.md` §11, item 3). **Commit now, in the change log, to reviewing the standard period once at the first product's launch + 12 months, on that measured evidence, published either way — including a published "no change" with its reason.** This costs nothing and it is safe, because the amendment already makes any change **prospective only**: existing increments finish on the period they began under (§2.2), so a revisit can never re-price a customer who has already bought, in either direction. **It converts a one-shot choice made in an evidence vacuum into a provisional choice with a dated correction** — which answers the actual complaint in my objection, that the convention is being fixed at the worst possible moment to fix it.

**The guard on Fix 2, so it does not reopen what fixity closed.** A scheduled revisit is a chance to move the period to suit whatever is being priced at the time. Three things close that and all three already exist: the change is **prospective-only** (§2.2); it is an **Article 11 amendment** with a public diff and rationale (11.1); and Article 9 row 1 (§12.4) requires the change to publish its effect **on every live product**, so a change made for one is visible in the others' numbers. [I]

**Not a block.** `roles/cgo.md` gives this seat a block on *"gate passage — for constitutional breach, unanswered dissent, or missing compliance evidence"* [E, read from disk 2026-09-20]. This is none of those. **Flag F2, downgraded from "open" to "answered with two disclosure fixes attached", owner CEO.**

---

## 7. The Haunt consequence — drafted Correction C5

### 7.1 Why a correction is owed, and by when

Haunt Condition **9.2** makes a published five-year support commitment a **precondition on the price** [E, `decisions/2026-09-16-haunt-gate.md`, Condition 9.2, read from disk 2026-09-20]:

> *"**A published five-year support commitment is a precondition, not a nicety.** v1.2's Definitions make build labour capital only where the amortisation period equals a **published** commitment; absent one it is a first-year expense and 'every figure is wrong by a factor of about three.' … The commitment is dated, product-level, published and contractual — CRA 2015 s.36(3). 'Supported until [date]' is not marketing."*

**Every sentence of that was true when written.** It is made untrue by the amendment, not by any error. And the record carries a hard date: *"**Published within 30 days (Constitution, Article 3) — due by 2026-10-16.**"* [E, ibid., header]

**So there is a sequencing problem and it is the practical point of this section.** If the amendment lands before 2026-10-16, the record must not publish with 9.2 stating a constitutional requirement that no longer exists — that would put a false statement about the current Constitution into the first public document Candour ever issues. If the amendment has not landed by 2026-10-16, the record publishes on time (Article 3 is not optional) with a **pending note** rather than a correction. §7.4 drafts both.

### 7.2 Drafted Correction C5 — for insertion in `decisions/2026-09-16-haunt-gate.md`

*(Drafted by the CGO; adoption is the CEO's. Follows the correction convention the record already uses: original preserved verbatim, error or cause named, seat attributed, dated.)*

> ---
>
> # Correction C5 — [date], before first publication
>
> **Classification: SUPERSESSION — by constitutional amendment.** Not a correction: nothing in Condition 9.2 was false when it was written, and no seat was wrong. Not a weakening: no protection recorded in this document is removed by it. **The rule 9.2 was written under has been amended** (Constitution v1.3, Definitions — `pipeline/amendment-draft-amortisation.md`; `CHANGELOG.md` v1.3).
>
> **This is a second flavour of the SUPERSESSION label the CGO proposed and the CVO adopted at C3.** C3 superseded a condition because *"the CEO changed his mind, which is his alone under Constitution 5.4."* C5 supersedes one because the governing rule changed under it. **`pipeline/templates/decision-record.md` should carry both flavours when it next gains the label**, which C3 already asked for and which has not yet happened.
>
> **Condition 9.2 as adopted is preserved in place above and is not edited.** What follows states its status.
>
> **C5.1 — the precondition no longer exists.** Constitution v1.2's Definitions permitted build labour to be capitalised only where the amortisation period equalled a **published support commitment to customers**. Constitution v1.3 replaces that with a **standard amortisation period fixed company-wide**, expressly *"an accounting convention and nothing more"* to which *"no customer-facing commitment of any kind attaches or is implied"*. **There is therefore no longer any accounting consequence to publishing or withholding a support commitment for Haunt.** 9.2's arithmetic (99p × 12 × 5 = £59.40; identical margins across tiers at five years) was correct and is now simply not load-bearing: it derived a *period* from a *price*, and the period is no longer Haunt's to derive.
>
> **C5.2 — what the amendment unlocked, stated because it is the point rather than a side-effect.** Under v1.2, declining a five-year commitment tripled every price. **Under v1.3 the CEO may make, shorten, lengthen or decline a support commitment for Haunt purely on its merits as a promise**, with no effect on the cost sheet. The CFO's reasons for preferring three years to five — that 360 hours a year on two platforms, from one part-time person, for five years, is *"a judgment with no measured year behind it"* [`products/haunt/cost-sheet-v2.md` §14.1] — were an argument about deliverability that had to fight an accounting penalty. They no longer do.
>
> **C5.3 — what a support commitment still is, if one is made.** Contractual. CRA 2015 s.36(3) treats information about a product's main characteristics and functionality as a term of the contract, and s.36(4) provides that *"a change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader"* [E — https://www.legislation.gov.uk/ukpga/2015/15/section/36, retrieved by the CGO 2026-09-20]. **9.2's last sentence survives the amendment intact: *"Supported until [date]" is not marketing.*** What changes is that it is now a free choice rather than a forced one, and a promise chosen freely is the only kind worth publishing.
>
> **C5.4 — consequences within Condition 9, itemised.**
>
> | Sub-clause | Status after v1.3 |
> |---|---|
> | **9.2** | **Superseded in full.** The precondition is gone; the arithmetic stands but decides nothing. |
> | **9.3** | Untouched by this amendment. **Separately in error and separately owed a correction** — see C5.6. |
> | **9.4** | **Survives; its number becomes contingent.** The amortisation cliff still exists, now at the end of the standard period rather than a product-declared life. The *"~32%"* figure was computed on five years; the cut at the standard period is whatever the cost sheet shows (20.2% at five years, 30.3% at two, on `cost-sheet-v2.md` §5.4). **Also: the operative clause for the cut is Article 2.1's annual margin cap, not Article 2.3.3.1, which governs the order of preference for the remainder of profit.** 2.3.3.1 is why the reduction reaches existing customers first; 2.1 is why there must be a reduction at all. |
> | **9.5** | **Survives unchanged.** Annual republication and price review remain Article 2.1 duties. |
> | **9.6** | Untouched. The DMCCA items R1–R5, L1–L2 are independent of amortisation. **L1 — qualified human legal review — remains a launch bar.** |
> | **9.7** | Untouched. |
> | **9.8(b)** | Untouched. The CTO must still size the subscription increment and answer whether 220 h/yr maintenance holds to year five — **now purely a cost question, no longer also a promise question.** |
> | **9.9** | **The CFO's standing block survives, and its lifting condition changes.** It was *"incomplete until the support commitment is published"*; the CFO has since narrowed it to lift *"the moment the period is published"* [`cost-sheet-v2.md` §16.1]. Under v1.3 the period is published **in the Constitution**. **Only the CFO lifts a CFO block** (Constitution 5.6) — this is recorded as a flag to that seat, not as a lifting. |
>
> **C5.5 — CEO decision D2 is superseded, not corrected.** D2 (five-year support commitment, both platforms, 2026-09-20) recorded a promise and a consequences paragraph. **Nothing in it was false.** Its consequences paragraph describes Constitution v1.2 accurately — *"v1.2 permits build labour to be amortised only against a published commitment… The period may be shortened, never lengthened"* — and that description is now historical. **The promise itself is untouched and remains the CEO's to keep, change or withdraw**, on product and contract grounds, with no constitutional consequence either way. D2's clock still starts at launch. **Nobody needs to defend D2; it needs only to be re-decided on its own merits, and it can now be re-decided freely, which under v1.2 it could not.**
>
> **C5.6 — a separate correction is owed to Condition 9.3 and is not this one.** 9.3 states *"At 25% off, 1.05×, which is not a band"* and that discounts deeper than ~10% collapse the compliant band. The CFO has since found that finding wrong and its own: *"Discounts deeper than ~10% do not collapse the band. My own earlier finding was wrong, and Condition 9.3 carries the error… the blended band at an 18.4% pay-once discount is 1.69×… The band closes at roughly 41%, not 25%"* [`products/haunt/cost-sheet-v2.md` §0-G and §6.3]. **That is a CORRECTION, it belongs to the CFO, it is owed before the same 2026-10-16 publication date, and it is not folded into C5** — a supersession and a correction should not travel under one heading, which is the lesson C1.6 recorded when a withdrawal nearly travelled under a correction's cover.
>
> ---

### 7.3 Where C5 sits in the record

**After Correction C4 and after the CEO decisions log**, as the next dated entry. The CEO decisions log sits between C2 and C3 in the current file and is chronological; C5 is later than all of it. **Condition 9.2 itself is not edited** — the record's established convention is preservation plus an appended correction [E, C1, C3 and C4 all follow it].

### 7.4 If the amendment has not landed by 2026-10-16

Article 3 requires publication *"Within 30 days of the decision"* [E, `constitution.md` line 80] and the deadline is not extendable by a pending amendment. **Publish on time, with this note in place of C5:**

> **Pending note — [date], before first publication.** Condition 9.2 rests on Constitution **v1.2**'s Definitions, under which build labour could be capitalised only against a published support commitment. **An Article 11 amendment replacing that treatment with a fixed company-wide amortisation period is drafted and before the CEO** (`pipeline/amendment-draft-amortisation.md`). If it is adopted, 9.2's precondition falls away and a Correction C5 will be appended here. **This note is published rather than held back, because a reader of this record is entitled to know that its governing clause is under active amendment on the day they read it.**

**This seat recommends the pending note be published even if the amendment lands first**, as part of C5's preamble — the fact that the clause was under amendment while the record was being prepared is itself part of the record. [J]

---

## 8. The determination owed on Article 2.1 — *"the cost of serving them"*

**Status:** owed by this seat, due **2026-10-16**, flagged as possibly a no-op by the CFO on two separate occasions [E, `products/haunt/cost-sheet-v2.md` §8: *"I have flagged twice that 'the cost of serving them' may make this clause a no-op"*, read from disk 2026-09-20]. Under `pipeline/evidence-standard.md`, **twice-flagged is escalated**: *"A load-bearing claim flagged as unverified on two separate occasions must be resolved, or formally accepted in writing by the CEO, before it may anchor a third artifact."* [E, read from disk 2026-09-20] **It is settled here, on the text, with the reasoning shown — and put to the CEO for assent rather than treated as self-executing.**

### 8.1 The clause

Article 2.1, third bullet, quoted in full [E, `constitution.md` line 47]:

> *"Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit against the cost of serving them. A recurring price whose every individual year is compliant can still breach this document over a decade, and the cumulative test is what catches it."*

### 8.2 The candidate readings

| | What *"the cost of serving them"* means | Cost attributed to a subscriber after `t` years |
|---|---|---|
| **Reading 1 — incremental** | The subscriber's share of the one-off build, charged **once**, plus their own years of fixed and variable cost | `B/N + t × (F/N + s)` |
| **Reading 2 — pro-rata** | The subscriber's pro-rata share of **that year's total product cost**, every year they stay | `Σ` of each year's `C(N)` |
| **Reading 3 — marginal** | Only the cost that would not be incurred but for this subscriber | `t × s` |

The readings are the CFO's framing at `cost-sheet-v2.md` §8.1 [E], adopted here because it is exhaustive.

**Reading 3 is not available, and was disposed of before this determination was owed.** Correction C1.2 [E, `decisions/2026-09-16-haunt-gate.md`]: the Definitions define Cost as *"everything it takes to run a product or the company, itemised… and labour valued at a published market benchmark whether or not it is actually paid"*, and **Article 9 names redefining "cost" as a gaming vector**. Substituting marginal for total cost is that redefinition. On Reading 3 the cumulative margin at five years is **+94.2%** [E, `cost-sheet-v2.md` §8.1], which is the reductio.

### 8.3 Determination: Reading 1, the incremental reading

**The ground is textual and it is decisive: Reading 2 falsifies the clause's own last sentence.**

The clause states that it catches something the annual test does not: *"A recurring price whose every individual year is compliant can still breach this document over a decade, and the cumulative test is what catches it."*

**Under Reading 2 that is arithmetically impossible.** If in every year `t` the annual margin complies — `R_t ≤ 1.3 × C_t` — then summing over all years gives `ΣR ≤ 1.3 × ΣC`, so the cumulative margin complies too. **Reading 2 makes the cumulative test a restatement of the annual test, which cannot catch a case in which every individual year is compliant, which is precisely the case the clause says it catches.** A reading on which a clause's own explanation of itself is false is not an available reading. [I, from the clause text and one line of algebra]

**Reading 1 does not have that defect**, because a one-off cost is incurred once per customer and not annually. A subscriber's cost path under Reading 1 is not a scaled copy of the product's annual cost path, so the two tests can diverge — which is what the clause claims for itself.

**And the clause's named mischief selects the same reading.** *"Merely by staying"* names accumulation through tenure: pay long enough and you have paid for something you were only ever going to be charged for once. That is Reading 1's shape and it is not Reading 2's. [I]

**Determination:** *"the cost of serving them"* means **the cost attributable to that subscriber: their share of the product's one-off costs, charged once, plus their own years of fixed and variable cost.** Under v1.3 it is computable directly from the cost sheet's new disclosure — build capitalised, recovered to date, months remaining (§3.1).

### 8.4 Where the clause actually bites — and the CFO's "nearly a no-op" is too pessimistic, in the customer's favour

**A general result first, because it disposes of a whole family of cases and it is arithmetic, so it can be re-derived.** Cumulative margin over `t` years is `ΣR/ΣC − 1`, and `ΣR/ΣC` is a cost-weighted mean of the yearly ratios `R_t/C_t`. A weighted mean cannot exceed its largest member. **So a subscriber's cumulative margin can never exceed the largest annual margin on their own cost-and-revenue path** — under *any* allocation, Reading 1 or Reading 2. [I]

**It follows that the cumulative test cannot bite on a subscriber whose price path is the product's price path.** Where every subscriber pays the current published price, each year's individual ratio is the product's annual ratio, the annual test catches the largest of them first, and the cumulative test arrives late with nothing new to say. **That is exactly what the CFO found on Haunt** — the annual 30% cap breaches in year 6 and the cumulative in year 11 [E, `cost-sheet-v2.md` §8.3] — and this determination explains *why* it found it, rather than treating it as a property of Haunt.

**But that condition is a real condition, and it fails in a named and foreseeable case.** The annual test is measured *per product, across all customers*; the cumulative test is measured *per customer, over their lifetime*. **They diverge the moment a subscriber's own price stops tracking the product's price** — grandfathered pricing, a legacy tier, a reduction applied to new customers but not to existing ones, or any arrangement in which tenure itself determines what you pay. In that case the product's annual margin can sit comfortably under 30% on a growing base at a lower price while a long-tenure subscriber's own cumulative position runs above it. **The clause catches that and nothing else catches it.**

> **So the clause is not a no-op. It is, read properly, a prohibition on tenure-based price divergence — which is what *"merely by staying"* says on its face.** The CFO's finding that it *"never binds independently"* is right on Haunt's cost shape and right for any product where everyone pays the same current price, and it is wrong as a general statement about the clause. **This seat records the disagreement in the customer's favour and invites the CFO to re-derive the weighted-mean argument, which is arithmetic and therefore genuinely re-derivable by a second seat** (Haunt Condition 6; `pipeline/evidence-standard.md`).

### 8.5 What follows from the determination

1. **No Haunt price changes.** Confirmed both ways by the CFO at `cost-sheet-v2.md` §8.2–8.3 [E]; the determination is consistent with that arithmetic and does not disturb it.
2. **It has a live application already on the table.** Correction C3.2 records an open question: the pay-once buyer pre-pays forward and *"does not participate in any future reduction"*, and whether such a buyer is an existing customer for Article 2.3.3.1 purposes is *"undetermined. Owner: CFO and CGO, before the price publishes"* [E, `decisions/2026-09-16-haunt-gate.md`, C3.2]. **That is a tenure-based price-divergence case, which is the case this clause is now determined to govern.** It remains open; this determination narrows it rather than closing it, and it is listed at §10.3.
3. **The recommended disclosure at §3.1 follows from it.** Publishing the cumulative position at the standard period and at twice it turns a test that rarely binds into two numbers a reader can check. **That is the cheapest available answer to "is this clause doing anything?"** — and it is a better answer than deleting a clause that binds in a case Candour has not yet reached.
4. **No amendment to 2.1's cumulative sentence is proposed.** The clause means what it says once the reading is fixed. Amending it would be legislating around an interpretive question that has now been answered, which is the move Article 10 warns against.

### 8.6 Why this is a determination and not an escalation — and where the CEO's signature is still wanted

**The reasons for settling it here.** The question is textual, the answer turns on one line of algebra rather than on a policy this seat would like the clause to have, and both candidate readings were supplied and modelled by another seat rather than constructed by this one. The September failure was a seat reading a clause to mean what it needed it to mean [E, `decisions/2026-09-16-haunt-gate.md`, C1.1]; **this determination reaches a reading that gives Candour a live obligation it did not previously acknowledge, which is the opposite direction.**

**The reasons the CEO should still sign it.** `pipeline/evidence-standard.md` is explicit that adding agent passes does not fix an interpretive failure, and that *"four agent passes over Article 4 in September 2026 produced the same wrong answer; the human produced the right one"* [E]. **This seat is not asking for a second agent pass. It is asking the CEO to read §8.3's one-line argument and say yes or no**, and recording that the twice-flagged escalation rule offers exactly two exits — resolution, or formal CEO acceptance — and this seat is offering the first while inviting the second.

> **Requested of the CEO:** assent to the determination at §8.3, or reject it and say which reading is right. **Either closes the item due 2026-10-16.** Silence does not: on the evidence standard's own terms an unresolved twice-flagged claim may not anchor a third artifact, and `cost-sheet-v2.md` is already the third.

---

## 9. Drafted change-log entry for `CHANGELOG.md`

Article 11.1 [E, `constitution.md` line 234]: *"Any change to this document is recorded in a public change log with **date, diff, and rationale**."* The diff is at §2.1, §3.1, §3.4, §3.5 and §5. What follows is the entry, drafted in the house style set by v1.2 and **revised at Revision 2 for Option B as adopted at D4** — item 2a is the Article 4 duty, and the WEAKENING block is replaced by a statement of why no label is owed. The diff also now covers §12.2, §12.3 and §12.4.

> ## v1.3 — [date]
>
> **Constitution text amended.** One Definitions entry replaced, one added, four consequential edits. Source: the CEO's decision to replace the support-commitment-linked amortisation rule with a company-wide accounting convention; `products/haunt/cost-sheet-v2.md` §5.5 (CFO); `pipeline/amortisation-proposal.md` (CFO); `pipeline/amendment-draft-amortisation.md` (CGO).
>
> **The occasion.** v1.2 tied the amortisation of one-off build labour to a **published customer-facing support commitment**, with the period shortenable but never lengthenable. Three flaws surfaced within four days of its adoption, the third of them decisive.
>
> 1. **It punished honest under-promising.** Commit to two years, find you can support five, and the extension could not reach the price. On the CFO's modelling the cost fell on early customers at **£8.42 a head over two years** for a product that turned out to have the longer life anyway.
> 2. **The permitted direction was the price-raising one.** Shortening compresses the same build into fewer years and raises the price; lengthening lowers it. v1.2 permitted the first without justification and forbade the second outright — against Article 2.1's requirement that *"a deviation in either direction is a deviation"* justified in writing, and against Article 2.3.3.1's placing of price reductions for existing customers first in the waterfall.
> 3. **Decisively: the clause permitted an act the law forbids.** A published, dated support commitment is information about a product's main characteristics and functionality, which **CRA 2015 s.36(3)** treats as *"included as a term of the contract"*; **s.36(4)** provides that *"a change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader"* (retrieved at source by the CGO, 2026-09-20). A commitment sold against is therefore frozen in **both** directions, and v1.2's *"may be shortened, never lengthened"* purported to permit unilaterally what the law makes ineffective. **A constitution that permits an unlawful act is defective whether or not anyone acts on it** — and this one is published continuously under Article 3.
>
> ### Constitution
>
> 1. **Definitions, Cost — build labour is amortised over a standard company-wide period, not over a declared supported life.** The tie to a published support commitment is removed, as is the shorten-never-lengthen ratchet and the absent-a-commitment fallback. New: labour on work that does not ship is an operating cost in the year incurred, and a product abandoned before release writes off its whole build publicly in that year. _Rationale: the three flaws above. Separating how long a cost is spread from what is promised to a customer is the cut v1.2 failed to make, and every flaw followed from the weld._
> 2. **Definitions — new entry, Standard amortisation period: [N] years**, running from release, **the same for every product**, expressly *"an accounting convention and nothing more"* to which **no customer-facing commitment attaches or is implied**. Changes only by public amendment, never for one product, and a change applies to every live product at its next republication. **Ungameable by construction:** a period fixed across all products cannot be chosen to suit the product being priced, which is what the v1.2 ratchet was trying and failing to achieve. _**[N] = three years (36 months), and the reason is published in full here rather than left in an internal proposal — Fix 1 at §6.4.** Apple requires every app to be rebuilt against a current SDK annually, and Google Play requires an annual target-API bump, so a mobile build is opened, altered and re-shipped three times by month 36 and each alteration is separately charged to customers as maintenance; amortising past that point charges a year-4 customer for code that no longer exists. Where a useful life cannot be reliably estimated, SI 2008/410 Sch 1 para 22 establishes the shape used here — a period chosen by the directors, capped, **published together with the reasons for choosing it.** **What that evidence does not do is select three over two**, and the change log says so rather than implying more precision than exists: an annual platform cadence brackets the answer at a small number of years and no retrieved source distinguishes two forced passes from three. **Within that bracket the deciding work was done by the only product Candour has.** The CFO dropped its earlier, Haunt-specific deliverability argument when the support promise was decoupled, and has recorded that it would have recommended three years even had three years made Haunt unshippable. **This convention was therefore fixed at the one moment in this company's history when a single product existed and its prices were already modelled. That is stated because it is true and because Article 9's method is to name the vector rather than wait to be caught by it.** **It is reviewed once, on measured evidence, at the first product's launch + 12 months** — the first date at which anyone will know how much of a Candour build survives a year — **and any change is prospective only, so no customer's price can move retrospectively in either direction.**_
> 3. **Article 2.1 — cost sheets state the build labour capitalised, the amount recovered to date, the months remaining, and that the period is a company-wide convention rather than a support horizon.** **Strengthening.** _Rationale: three published numbers where there were none, and a sentence that stops the disclosure re-creating the implication the amendment removes._
> 4. **Article 7.2 — the closing cost sheet states the build capitalised, the amount recovered from customers to date, and the unamortised remainder written off.** **Strengthening.** _Rationale: it is the number that exposes early discontinuation after full recovery, and Article 9's commitment is to publish the numbers that expose each vector._
> 5. **Article 9 — four new loophole rows and one extended row.** New: setting or amending the standard period to suit whichever product is being priced; a one-off or pay-once tier escaping the cumulative lifetime margin test; recovering the build fast and discontinuing once it is recovered; running past the period's end without cutting the price. Extended: the anti-redefinition row now names the standard amortisation period alongside cost, surplus, reserve and net proceeds. _Rationale: fixity closes two vectors and opens one, and Article 9's commitment is to name our own rather than use them. Both rows owed from Haunt Correction C3.3 are discharged here — C3.3(a) carried, C3.3(b) corrected: its stated mechanism ran in the wrong direction on the CFO's own arithmetic, and the harm it named comes from a short period recovered fast, not a long one._
> 6. **Article 10 — the approximation is admitted.** [If §3.5 taken.] One company-wide period is, for any particular product, an approximation of nothing in particular; Article 2.1 asks for that product's honest number; we say so rather than letting a fixed term read as a support horizon. _Rationale: the alternative — a period tuned per product — is the loophole this convention exists to close._
>
> ### 2a. **Article 4 — every product states its support position, without exception.** New bullet: state, before first sale and on the product's own pricing page, **either the date until which the product will be supported, or plainly that no support date is committed. Silence is not an option.** A published date is a term of the customer's contract (CRA 2015 s.36(3)) and is not changed for customers who have already bought. A product's amortisation period is an accounting convention, is never published as or in place of a support date, and the cost sheet carrying it says so on its face. **Strengthening.** _Rationale: v1.2 delivered a support commitment as a **by-product** of an accounting choice — near-certain, because declining it multiplied the cost base by 2.23×, but available to Candour to decline in silence at a higher price. It also attached that penalty to declining a promise this company has since said in writing it cannot guarantee. **A rule whose only compliant path runs through a date you cannot keep manufactures a future public breach; it does not prevent one.** This bullet replaces it with a duty that binds every product at every price, admits no exception, and can always be satisfied honestly — including by saying no date is committed, which is what Haunt does._
>
> ### **Not labelled WEAKENING, and the reason is set out rather than assumed**
>
> **The CGO's original recommendation was that the amendment alone would be a WEAKENING under Article 11.2 and must be labelled.** It is not deleted from the record: `pipeline/amendment-draft-amortisation.md` §4.8 preserves it at full strength, because what changed is not the label but the substance it would have described.
>
> **What changed.** Item 2a was adopted alongside the amendment rather than instead of the label. Under v1.2 a customer might receive a support commitment, where a product happened to be priced on amortised build labour. **Under v1.3 every customer of every Candour product, at every price, is told the support position before buying, and Candour cannot opt out of telling them.** Article 11.2 asks whether a customer-facing rule is weakened; this rule is not weakened but replaced by one that binds in strictly more cases and admits no exception.
>
> **The residual, stated plainly because it is real and a reader should not have to find it.** A customer who would have received a **promise** under v1.2 may now receive a **disclosure that no promise is made**. That is a difference and it is not nothing. It is recorded here without the 11.2 label, on the ground above, and because the promise v1.2 made near-certain was one the company could not honestly guarantee.
>
> **Two arguments were offered for dropping the label and both were rejected on the record** at `pipeline/amendment-draft-amortisation.md` §4.5, so that neither is available later for a case it does not fit: that Article 7.2 was *"the real protection"* (7.2 governs how a product **ends** and does not reach a product merely allowed to rot), and that the clause was *"legally unsound"* (the unlawful half was the permission to **take the commitment away**; the requirement to **make** one was lawful and unimpeachable). **The label was dropped because of item 2a, and for no other reason.**
>
> **What is unchanged, because a customer reading this should not have to hunt for it.** Article 7.2 is untouched: **at least 90 days' notice of discontinuation, full data export free throughout the notice period and for 90 days after, open-sourcing where third-party rights allow, and a published closing cost sheet.** Article 4's export and dark-pattern rules are untouched. Article 2.1's ~20% target and 30% hard cap are untouched.
>
> _Not labelled WEAKENING: items 2a, 3, 4, 5 and 6 add duties, published numbers and named loopholes and remove none. Item 1's removal of the shorten-never-lengthen ratchet removes a permission, not a protection._

---

## 10. Blocks, flags, and what is still open

### 10.1 Blocks

**None. This seat holds no block on this amendment.** [E, `roles/cgo.md`, read from disk 2026-09-20: the CGO's block is *"Gate passage — for constitutional breach, unanswered dissent, or missing compliance evidence"*.] An Article 11 amendment is not a gate, and the amendment does not breach the Constitution — it is the Constitution's own prescribed route for change. **Recorded precisely so that silence is not read as consent and a non-block is not read as a block:** this seat supports the amendment and recommends it.

### 10.2 Flags — concerns outside this seat's blocking scope, each with the seat that holds the power

| # | Flag | Held by |
|---|---|---|
| F1 | ~~**The Article 11.2 classification.**~~ **CLOSED at Revision 2.** The CEO adopted Option B at D4; on that basis no label is owed and this seat's recommendation and the outcome agree. Reasoning at §4.8; why the earlier recommendation is preserved rather than deleted, at §12.1. | *closed* |
| F2 | **T1 — the reason for `[N]` must not be an argument from Haunt's prices** (§6.1, §6.4). If it is, the change log should say so. | CFO, then CEO |
| F3 | **C3.3(b) is directionally wrong on the CFO's own arithmetic** (§5.3). It corrects a CFO record and the CFO should be told rather than have it corrected around them. | CFO |
| F4 | **Condition 9.3 is owed its own correction before 2026-10-16** (§7.2, C5.6), in the CFO's words, not folded into C5. | CFO |
| F5 | **The CFO's standing block's lifting condition changes** — the period is published in the Constitution, not on a product page (§7.2, C5.4). **Only the CFO lifts a CFO block** (Constitution 5.6). | CFO |
| F6 | **Condition 9.4 cites Article 2.3.3.1 for an obligation that comes from Article 2.1** (§3.2). Changes no number; correctable in the same pass. | CFO / CEO |
| F7 | **`pipeline/templates/amendment.md` does not exist**, and `pipeline/templates/decision-record.md` still lacks the SUPERSESSION label that Correction C3 asked for on 2026-09-19 — now needed in two flavours (§7.2). Charter and template changes need only the CEO's assent, not Article 11 [E, `pipeline/governance-review-2026-09.md` header]. | CEO |
| F8 | **The CFO's shared-cost allocation rule and its Article 9 row** (§5.4) are sound and deliberately **not** bundled into this amendment. | CEO |
| F9 | **Constitution 6.1 human review.** The s.36 analysis at §1.3 is agent analysis. The existing **L1 launch bar** (qualified human legal review) is the place it is confirmed, and is unchanged. | CGO / CEO |

### 10.3 Still open, and not closed by this draft

- **The CFO's period.** `pipeline/amortisation-proposal.md` was not on disk when this was written. §6 is written to be applied to whatever number arrives; §6.4 states this seat's disagreement **in advance** so it is on the record before the number rather than after.
- **C3.2 — whether a pay-once buyer is an "existing customer" for Article 2.3.3.1.** Owner CFO and CGO, before the price publishes [E, `decisions/2026-09-16-haunt-gate.md`, C3.2]. §8.4 narrows it — it is a tenure-based price-divergence case, which is the case the cumulative test is now determined to govern — but does not close it.
- **Whether Haunt publishes a support commitment at all**, and for how long. Now a free product and contract decision (C5.2). **The CEO's, under 5.4.**
- **The ICO fee determination** for Haunt, recorded as this seat's at `cost-sheet-v2.md` §2.3 [E]. Unrelated to this amendment; listed so it is not lost.

### 10.4 What would overturn this draft, and where I looked

*(Document-level. The classification's own falsifiers are at §4.10 and are not repeated.)*

**Overturned by any of:**

1. **A finding that a fixed company-wide period is not achievable** — e.g. that a future product's economics make `[N]` indefensible at either tail (§6.1 T2). That is the CFO's to find and it would send the design back, not just the number.
2. **Qualified human legal review disagreeing with §1.3** — that a published support period is *not* Schedule 2 (a)/(v) information, or that s.36(4) does not freeze it in the shortening direction. **That would dissolve flaw 3 and leave flaws 1 and 2, which are arguments that the clause is unwise rather than defective.** The amendment would still be worth making; the urgency would fall.
3. **A demonstration that `[N]` was chosen from one product's prices** (§6.1 T1), which would not overturn the wording but would change what the change log must say.
4. **Adoption of Option B** (§4.9), which changes the classification and nothing else.

**Where I looked:** `constitution.md` v1.2 in full; `roles/cgo.md`; `pipeline/evidence-standard.md` v1.1; `pipeline/governance-review-2026-09.md`; `pipeline/templates/` (nine templates listed; `decision-record.md` classification test read); `CHANGELOG.md` v1.0–v1.2; `decisions/2026-09-16-haunt-gate.md` in full (decision, dissent response, ten conditions, overrules, C1, C2, CEO decisions log D1–D3, C3, C4); `products/haunt/cost-sheet-v2.md` §0, §2.1–2.5, §5.1–5.6, §6, §8.1–8.5, §13, §14.1–14.3; **CRA 2015 s.36 and SI 2013/3134 Schedules 1 and 2 retrieved at source, 2026-09-20.**

**Not retrieved, and flagged rather than assumed:** `pipeline/amortisation-proposal.md` (does not yet exist); Apple App Store guideline 3.1.2(a) (carried as **[K]**, not load-bearing — §4.10); UK accounting standards on capitalised development costs (**not retrieved, not asserted** — §6.1 T6); `products/haunt/cost-sheet.md` v1 and `pricing-ladder-model.md` (superseded by `cost-sheet-v2.md`, which states its own supersessions).

---

## 11. What this seat is asking the CEO to decide *(superseded by §12.8 — preserved because it is the list the CEO was given before D4)*

1. **Adopt the amendment** at §2, with `[N]` from the CFO. *(Recommended.)*
2. **Take or decline the consequential edits:** §3.1 required-plus-recommended, §3.4 recommended, §3.5 optional. *(Recommended: take all four.)*
3. **Take or decline Option B** (§4.9) — an Article 4 duty to state a support date or state plainly that none is given. *(Recommended, first preference.)*
4. **Decide the Article 11.2 classification** (§4.8). *(Recommended: WEAKENING in one respect, with the named sentence, unless Option B is taken — in which case no label is owed.)*
5. **Adopt Correction C5** for the Haunt record (§7.2), or the pending note (§7.4) if the amendment has not landed by **2026-10-16**.
6. **Assent to or reject the determination at §8.3**, closing the item due 2026-10-16.
7. **Note the nine flags at §10.2**, four of which are the CFO's to action before the same publication date.

**This seat prepares and flags; it does not certify.** Every item above is a Constitution 5.4 or Article 11.1 decision and belongs to the CEO.

---

# Revision 2 — after CEO decisions D4 and D5

## 12. Revision 2 additions

### 12.1 Why the pre-D4 recommendation is preserved rather than deleted

§4.8 still carries this seat's original determination — that without Option B the **WEAKENING** label was owed. **It is kept, at full strength, for three reasons.**

1. **Option B is not a way of avoiding the label; it is a way of not doing the thing the label describes.** If the CEO had taken the amendment alone, the label would still be owed and this seat would still be recommending it. Deleting the earlier recommendation would make the record read as though the objection evaporated on contact with a decision, which is the opposite of what happened.
2. **A reader of `CHANGELOG.md` v1.3 will see no WEAKENING label and is entitled to know why there is none.** The answer is not "the CGO changed its mind"; it is "the Constitution now carries an Article 4 duty that did not exist when the objection was raised." That is a fact about the document, checkable in one place.
3. **It is the third time this seat has recommended a classification and the second time the outcome differed from the recommendation.** Twice previously (C1.6, C3) the CEO and CVO decided against it and were entitled to. **This time the substance moved instead of the label, which is the better outcome and the one worth having on the record.**

### 12.2 Article 4 — the finalised Option B duty, as adopted at D4

Article 4 opens *"Every product must, without exception:"* and is a list of bullets [E, `constitution.md` lines 87–97]. The new bullet, drafted for insertion after the plain-language-pricing bullet:

```diff
 - Use plain-language pricing with no hidden fees, forced bundles, or drip pricing.
+- State, before first sale and on the product's own pricing page, **either the
+  date until which the product will be supported, or plainly that no support
+  date is committed**. Silence is not an option. A published support date is a
+  term of the customer's contract — Consumer Rights Act 2015, s.36(3) — and is
+  not changed for customers who have already bought. **A product's standard
+  amortisation period (Definitions) is an accounting convention, is never
+  published as or in place of a support date, and the cost sheet carrying it
+  says so on its face.**
 - Make cancellation as easy as signup.
```

**Four drafting notes.**

**(a) *"Silence is not an option"* is the whole point of the bullet.** It is the operative difference from v1.2, under which a product could say nothing about support at a higher price. It is Article 1.3 in its own words — *"We say what a product cannot do"* [E, `constitution.md` line 34].

**(b) The s.36(3) citation is in the text deliberately**, and there is precedent: Article 7.1.5 already names the Contracts (Rights of Third Parties) Act 1999 in the Constitution's own text [E, `constitution.md` line 170]. It is there so that a future seat cannot publish a date without meeting the fact that it is contractual.

**(c) *"Is not changed for customers who have already bought"* rather than *"is never changed"*.** s.36(4) makes a unilateral change ineffective as against a consumer who has contracted [E, §1.3]. Offering a **longer** date to new customers is not that, and a drafting that barred it would re-create flaw 1 in a new place. **The clause binds the direction that harms and leaves the direction that helps open.** [I]

**(d) The final sentence discharges the CFO's flag A3**, which it calls *"the load-bearing legal assumption of this whole scheme"* [E, `pipeline/amortisation-proposal.md` §3.5, §12]. **This seat's determination on it:** a statement about how **Candour spreads a cost in its own accounts** is not information *"about the digital content"* concerning *"main characteristics, functionality and compatibility"* within CRA 2015 s.36(3) and Schedule 2 paragraphs (a), (v) and (w) [E, retrieved 2026-09-20 — §1.3]. Schedule 2 (a) is *"the main characteristics of the goods, services or digital content"*; an amortisation schedule is a characteristic of the seller's bookkeeping, not of the software. **The risk is not in the cost sheet; it is in the pricing screen**, where *"three-year product"* would be exactly the Schedule 2 (a) information the scheme exists to avoid creating. **The distance between the two is one sentence of drafting, and the bullet above is that sentence.** Per Constitution 6.1 this is agent analysis, and the existing **L1 launch bar** — qualified human legal review — is where it is confirmed.

### 12.3 Article 2.1 — the consequential edit, revised for layers

Replaces the version at §3.1, which assumed a single balance per product. The CFO's layering (§2.3(f)) makes a schedule necessary rather than optional.

```diff
-- Every product publishes a **cost sheet**: hosting, tooling, support,
-  third-party services, and a fair-market cost for labour (including the
-  founder's, whether or not it is actually drawn).
+- Every product publishes a **cost sheet**: hosting, tooling, support,
+  third-party services, and a fair-market cost for labour (including the
+  founder's, whether or not it is actually drawn). Where build labour is
+  capitalised, the cost sheet publishes an **amortisation schedule** — one
+  line per capitalised increment, with its hours, ship date, period, amount
+  amortised to date and remaining balance — together with capitalised hours as
+  a share of all hours worked on the product that year, and a statement that
+  the period is a company-wide accounting convention and not a statement about
+  how long the product will be supported.
```

**The trailing clause is not decoration.** Without it the schedule itself re-creates the implication the amendment removes: *"build amortised over three years, 14 months remaining"* reads, to a customer, exactly like a support horizon. [J]

**The recommended cumulative-lifetime disclosure at §3.1 is unchanged and still separable** — it follows from §8 and the CEO may take it, defer it or reject it without affecting anything else.

### 12.4 Article 9 — the consolidated table

**Two seats proposed loophole rows independently and they are complementary, not duplicative.** This is one amendment and the CEO should adopt one table, not two. Mine were about the period, the tiers and the endings; the CFO's V1–V4 are about the hours, the clocks and the schedule. **Merged, de-duplicated and reduced to seven rows** (my "running past the period without cutting the price" and the CFO's V3 "rolling the layers" are the same harm reached two ways, so they share a row with both exposing numbers).

| # | Loophole | The number that exposes it | Origin |
| --- | --- | --- | --- |
| 1 | **Setting or amending the standard amortisation period to suit whichever product is being priced at the time** | Fixed company-wide; changes only by public amendment and **only prospectively**. Every change publishes, **for every live product**, the build labour still unrecovered and the price effect on each — so a change made for one is visible in the others' numbers | CGO |
| 2 | **Inflating capitalised build hours**, or capitalising work that is really maintenance — with the period fixed, the numerator is the only lever left | **Capitalised hours per product against (a) the gate estimate and (b) hours actually recorded**, restated annually; plus **capitalised hours as a share of all hours worked on the product that year**, which should trend to zero in steady state | CFO (V1) |
| 3 | **Restarting the clock with a "v2"** — re-badging a year of maintenance as a new build to open a fresh layer | **The published layer schedule**: hours, ship date, period, amortised to date, balance. A real increment has a shipped change behind it; a fake one is a layer with no release note | CFO (V2) |
| 4 | **The price never falls when the build leaves the cost base** — by inaction, or by opening a new layer to offset every expiry | **The counterfactual price at every republication:** what the price would be if no layer had opened since the last expired. Plus the **annual margin** at the first republication after an expiry, against Article 2.1's cap, which admits no justification | CFO (V3) + CGO |
| 5 | **Deferring the start date**, because "launch" is a soft enough word to move | The start date is the **earlier of first sale and public release**, published on the first cost sheet and never restated — with **the date of the first pound of revenue published beside it**. A gap between the two has to be explained | CFO (V4) |
| 6 | **A one-off or pay-once tier escaping the cumulative lifetime margin test (2.1)**, which constrains only what a subscriber pays *by staying* | The **annual** margin on every tier **including one-off tiers**, at every republication, with one-off revenue recognised **over the amortisation period** rather than in the year of receipt. Recognised on receipt a pay-once tier shows **+243.4%** in the year of purchase, which is what makes the escape visible | Haunt C3.3(a) |
| 7 | **Recovering the build quickly and then discontinuing once it is recovered** | The closing cost sheet's **unamortised remainder written off** (7.2), against the published amortisation start date. **An early discontinuation showing a write-off of zero is a product whose customers paid for the whole build and did not get the product** | Haunt C3.3(b), corrected |

**Plus the one-line edit to the existing anti-redefinition row at §5.1**, which now names the standard amortisation period alongside cost, surplus, reserve and net proceeds.

**Deliberately not in this amendment** (F8): the CFO's fifth vector — splitting one build across two products to capitalise shared work twice — and the shared-fee allocation rule at `cost-sheet-v2.md` §13. **Both are sound and both are about *shared costs across products*, which is a different subject.** Bundling them makes one change log entry carry two unrelated changes and makes the diff harder to audit. **Recommendation: a second, separate amendment at the same sitting.** Neither becomes harder to fix by waiting a month, and the CFO's own reason for urgency — settle it while no price depends on it — is still true next month, because Candour still has one product.

**Correction C3.3(a) and C3.3(b) are both discharged by this table**, which is what C3.3 asked for: *"Both belong in Article 9's loophole table at the next amendment."* This is the next amendment.

### 12.5 The determination at §8, in one sentence for the CEO

> **"The cost of serving them" in Article 2.1 means that subscriber's own cost — their share of the one-off build charged once, plus their own years of running cost — and on that reading the cumulative lifetime test is not the no-op the CFO suspected: it is a live prohibition on a long-standing customer's total position drifting above what a newer one pays. Do you assent, or reject it and name the other reading?**

*(The reasoning is at §8.3; the one line that decides it is that the other reading makes the clause's own final sentence arithmetically impossible. Either answer closes the item due 2026-10-16; silence does not, because the evidence standard's twice-flagged rule offers only resolution or formal acceptance.)*

### 12.6 Correction C5 — revised for D4 and D5

The draft at §7.2 stands, with these changes. **D4 has already done part of C5's work**, recording that *"D2 is superseded, not corrected — nothing in it was false; the framework it relied on changed underneath it"* and that *"Condition 9.2's 'published five-year support commitment is a precondition' falls with it"* [E, `decisions/2026-09-16-haunt-gate.md`, D4]. C5 therefore **executes** rather than announces.

- **C5.2 is rewritten.** It said the amendment lets the CEO *"make, shorten, lengthen or decline a support commitment on its merits"*. **He has decided: Haunt publishes no guaranteed support date** (D4, second limb). C5.2 should state that and state what now binds instead — **the new Article 4 bullet (§12.2): Haunt must say so plainly, on its own pricing page, before first sale.** Not saying it is now a breach of Article 4, which is a stronger position than v1.2 produced.
- **C5.4's row for 9.9 is unchanged and now confirmed by the CFO in its own words:** the block *"does not lift on this proposal — it changes its lifting condition"*, and *"withdrawing the support commitment without amending the Definitions does not produce a three-year amortisation. It produces first-year expensing"* — £90,205.20 against £40,517.17, **2.23×**, and an honest monthly price of **£1.58 rather than 99p** [E, `pipeline/amortisation-proposal.md` §9]. **Sequencing, stated because it is the thing most likely to go wrong: the amendment must be in force before any Haunt price publishes under Article 3.**
- **Two CFO errors are carried into C5, as instructed, and neither is mine to write in the CFO's voice.**
  - **Condition 9.3** states *"At 25% off, 1.05×, which is not a band"* and that discounts deeper than ~10% collapse the compliant band. Its author has since found that wrong: *"Discounts deeper than ~10% do not collapse the band. My own earlier finding was wrong, and Condition 9.3 carries the error… the blended band at an 18.4% pay-once discount is 1.69×… The band closes at roughly 41%, not 25%"* [E, `products/haunt/cost-sheet-v2.md` §0-G and §6.3]. **Classification: CORRECTION** — a false statement, caught before first publication. **Owner: CFO, in its own words, before 2026-10-16. Filed as a separate correction, not folded into C5**, because a supersession and a correction must not travel under one heading — the lesson C1.6 recorded when a withdrawal nearly travelled under a correction's cover.
  - **Condition 9.4** cites *"Article 2.3.3.1 lands the cut on the installed base"*. The obligation to cut the price when the build leaves the cost base comes from **Article 2.1** — the ~20% target and the 30% cap measured per financial year, which *"admits no justification"*. **Article 2.3.3.1 is why the reduction reaches existing customers first; Article 2.1 is why there must be a reduction at all.** The point 9.4 makes is right and the clause it hangs on is the wrong one. **Classification: CORRECTION.** Changes no number and no decision. Correctable in the same pass.
  - **A third, noticed while checking the second and recorded because it is the same class:** 9.4's *"~32% price cut"* and *"price must fall to ~68p"* were computed on a five-year life. **On the three-year standard the cut is 30.3%, 99p → 69p** [E, `pipeline/amortisation-proposal.md` §5.2, re-derived from its own stated formula]. The figure is not wrong as written — it was right for the period then in force — so this is **not** a correction but a **consequence of the supersession**, and belongs inside C5 rather than in the CFO's separate correction.
- **A new C5.7 is owed, covering D5**, because C5 is the last correction before publication and D5 is currently recorded only in the decisions log. §12.7.

### 12.7 D5 — is the recording adequate?

**Asked to check it, and the honest answer is: adequate on the hard part, inadequate in four respects. None of the four is a reason to change the decision; all four are reasons to add lines before 2026-10-16.**

**What it gets right, and it is the part that usually goes wrong.** The Research Analyst's warning is preserved **verbatim and against the decision** — that a sharing layer is *"the only growth mechanism this product could ever have"*, so the option *"will be exercised for company reasons and then justified with user reasons"* [E, `decisions/2026-09-16-haunt-gate.md`, D5, read from disk 2026-09-20]. The test then **forbids the argument the warning predicts**: sharing is proposed *"only on evidence of unprompted demand from existing users… and never on a growth or revenue argument"*, re-entering as a fresh proposal through a full gate, with the controller consequence on the table from the first line. **A record that preserves the warning it is overriding, and writes the test in the warning's own terms, is doing the thing this company exists to do.** [J]

**Four gaps.**

**(a) No owner and no revisit point.** `pipeline/governance-review-2026-09.md` §D3 found exactly this and asked for it to be structural: *"Conditions in decision records need an owner and a deadline. Make both fields structural."* [E, read from disk 2026-09-20] D5 has neither. Constitution 5.2's four-week anti-drift clock does not reach it — a gated option is not an idea in the pipeline — so nothing else will catch it. **A gate with no owner is a gate nobody is minding. Recommend: owner CVO** (it re-enters as a proposal, which is CVO work), **with a stated review point rather than a deadline** — not before the first annual cost-sheet republication, so that the evidence at (b) has had a year to exist or fail to.

**(b) The evidence bar is missing, and this is the serious one.** *"Evidence of unprompted demand from existing users"* is the load-bearing phrase and the record attaches no standard to it. **Candour has, by design, no instrument that could produce that evidence.** The cost sheet records crash and analytics tooling at **£0.00** — *"Deliberately absent (Article 4 data minimisation)"* [E, `products/haunt/cost-sheet-v2.md` §2.3] — and on this architecture Candour holds no journal data at all. **The only channels that exist are the support inbox and store reviews, both self-selected.** So the test as written is either unsatisfiable honestly, or satisfiable by the weakest evidence that will ever arrive — which is precisely the route the Research Analyst's warning describes. **Recommend the record name the bar now, while nothing turns on it:** demand counted from unsolicited contacts only; **never from a prompt, survey or in-app ask, because asking is prompting** and Article 1.1's test is *"whether they would recommend it **unprompted**"* [E, `constitution.md` line 32]; the count and the channel published with the proposal; and the self-selection stated on the face of it, per `pipeline/evidence-standard.md`'s honesty-about-our-evidence-situation section.

**(c) The regulatory list is incomplete in one place I can identify and not determine.** D5 names DPIA, privacy notice, ICO registration and moderation duties. **A sharing layer would also raise whether Haunt becomes a user-to-user service under the UK online safety regime, which is a different statute with different duties from data protection.** *[K, low confidence — **not retrieved this session, and deliberately not asserted**.]* This seat will not state what that regime requires from memory; `pipeline/evidence-standard.md` treats a citation without a retrieval as fabrication. **What the record should say is that the question exists and must be determined at source in the first line of any such proposal**, alongside the controller analysis. **Naming an undetermined question is cheap; discovering it at a gate is not.**

**(d) Nothing stops the option being mentioned before it is gated.** *"Sharing coming soon"* on a store listing or pricing page would be pre-contract information about the product's functionality — Schedule 2 paragraph (v), *"the functionality… of digital content"* [E, retrieved 2026-09-20 — §1.3] — and therefore a contract term under CRA 2015 s.36(3) for a feature that has not passed a gate and may never exist. It would also breach Article 4's *"Remain honest in marketing: claims we cannot substantiate are claims we do not make"* [E, `constitution.md` line 97]. **One line closes it: the option is not referenced in any customer-facing material until it has passed a gate.**

> **Summary for the CEO: the decision is sound and the reasoning is well recorded. Four lines are owed before 2026-10-16 — an owner and a review point, an evidence bar for "unprompted", the online-safety question named as undetermined, and a bar on marketing it before it is gated. (b) is the one that matters, because without it the test the CEO wrote to stop the warning coming true is a test that anything can pass.**

### 12.8 Revised asks — supersedes §11

1. **Adopt the amendment** at §2 as revised (Definitions entry with layers, start date and prospective-only change), with `[N]` = **three years**. *(Recommended.)*
2. **Adopt the Article 4 duty** at §12.2. *(D4 already decides this; §12.2 is the text.)*
3. **Adopt the consequential edits:** Article 2.1 as revised at §12.3 (required), Article 7.2 at §3.4 (recommended), Article 10 at §3.5 (optional, recommended), Article 9 at §12.4 (required).
4. **Attach the two fixes at §6.4** — the separation published in the change log, and one scheduled prospective-only revisit at launch + 12 months. *(Recommended. They are the difference between my T1 objection being disclosed and being unaddressed.)*
5. **Classification: no WEAKENING label**, with the residual named in the change log without it (§4.8, §9). *(This seat's recommendation, and it agrees with the outcome for the first time in three attempts.)*
6. **Answer §12.5 in one line**, closing the determination due 2026-10-16.
7. **Adopt Correction C5** as revised at §12.6, and **direct the CFO to file its own correction to Condition 9.3** separately, before 2026-10-16.
8. **Add the four D5 lines** at §12.7, of which **(b) is the one that matters**.
9. **Note the flags at §10.2**, as updated: **F1 closed** (classification settled by D4 + Option B); **F2 answered with fixes** (§6.4); **F3, F4, F5, F6 stand**; **F7 stands and has grown** — `pipeline/templates/decision-record.md` now needs the SUPERSESSION label in **three** flavours (changed mind, amended rule, and D4's hybrid), and `pipeline/templates/amendment.md` and `cost-sheet.md` both need work; **F8 stands** (§12.4); **F9 stands** and now also carries the CFO's A3, discharged in drafting at §12.2 and confirmed at L1.

**This seat prepares and flags; it does not certify.** Every item above is a Constitution 5.4 or Article 11.1 decision and belongs to the CEO.

---

## 13. Change log for this document

| Date | Change |
|---|---|
| 2026-09-20 | **Created.** Amendment drafted against v1.2 with `[N]` unset; Article 11 classification determined as **WEAKENING in one respect**; Option B offered as the route that would remove the need for the label; Article 9 rows drafted; Correction C5 drafted; the *"cost of serving them"* determination settled as the incremental reading. CRA 2015 s.36 and SI 2013/3134 Schedules 1 and 2 retrieved at primary. |
| 2026-09-20 | **Revision 2, after CEO decisions D4 and D5 and `pipeline/amortisation-proposal.md`.** *Edited in place, not appended-to; every change is listed here.* **(1)** Header and §0 rewritten. **(2)** Definitions entry revised to adopt the CFO's layering, the earlier-of-first-sale-or-release start date, and **prospective-only** amendment of the period — the last of these **correcting this seat's own first draft**, which said a change applies to every live product at its next republication and would have re-created flaw 2 at company scale; caught by the CFO at proposal §3.4 and recorded at §2.3(e) rather than absorbed into a rewrite. **(3)** §2.3 gains drafting note (f) on layers. **(4)** §4.8 determination revised: **no WEAKENING label under Option B**, with the pre-D4 recommendation preserved at full strength and the reasoning for the change of outcome set out; §4.9 marked as adopted. **(5)** §6.4 replaced with the T1 verdict — **partly answered, does not block**, with the residue located and two fixes proposed; this seat's own T1 test recorded as **too strict as written**. **(6)** New §12: the preserved-recommendation rationale, the finalised Article 4 duty, the revised Article 2.1 edit, the consolidated seven-row Article 9 table, the one-sentence question for the CEO, C5's revisions including the two CFO errors, the D5 adequacy check, and revised asks superseding §11. **(7)** Apple, Google and SI 2008/410 evidence carried from the CFO's proposal **with its links and its single-source flags intact**, not re-retrieved by this seat and marked as such at §6.4. |

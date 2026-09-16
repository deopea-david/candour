# Governance review — September 2026

**Author:** CVO · **Date:** 2026-09-16 · **Status:** proposals only. Constitution changes require Article 11 (CEO decision, public change log, diff and rationale). Charter, template and evidence-standard changes are cheaper and need only the CEO's assent.
**Occasion:** the Haunt discovery and gate cycle (2026-09-09 → 2026-09-16), the Skeptic's twelve objections, and Correction C1.

---

## The pattern worth naming first

Across this cycle, **the seats verified the world rigorously and verified their own governing document barely at all.**

The Skeptic performed 16 retrievals to check claims about Arc, Google and Overture. Meanwhile three documents asserted a constitutional prohibition that does not exist, one seat redefined a term the Constitution explicitly defines, another seat's heuristic operated as law in three artifacts, and a claim that "three seats independently reserved a block" survived into a decision record when only one had the power to. **None of those were caught by a seat.** All were caught by the CEO, or by the CGO after the CEO challenged it.

The evidence standard has four tags, a verification duty, an independence test and a rule against citing from memory — **all aimed at claims about the external world.** It says nothing about claims concerning Candour's own rules, which is the one category where the source is a file in this repository, costs nothing to retrieve, and was the category we got wrong. Most proposals below follow from that.

A second, milder pattern: **no seat re-derives another seat's work.** Two arithmetic transposition errors (O1, O10) survived until the Skeptic recomputed from stated formulae; the CFO's build-hours assumption survived the CTO contradicting it; the export-clause misreading propagated into three documents unchallenged.

---

## A. Constitution amendments — Article 11, the CEO's decision

**A1. Article 4, export clause — resolve the ambiguity that produced C1.1.** Current text: *"Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge and with no penalty."* Three seats read the modifiers as attaching to the user's data generally rather than to the act of exporting. Suggested: *"…available at any time, at no charge, and with no penalty or disadvantage imposed for having exported."* **Clarifying, not weakening** — it states the meaning the CGO's re-examination concluded the clause already has.

**A2. The gap C1.5 identified — content the user authored.** The Constitution has no clause about gating access to content a user created and stores on their own device. Three seats felt the absence and filled it by over-reading a different clause. Two honest options: legislate it (an Article 11 strengthening, which is the clean route the CGO named if Candour wants the read-cap prohibition binding), or **record the absence deliberately in Article 9's spirit** — naming a gap we have chosen not to fill is better than leaving one for a future seat to fill by improvisation. *My recommendation: decide it deliberately either way, and soon, because Haunt is about to ship a design in exactly this space.*

**A3. Accessibility baseline — WCAG 2.1 AA → 2.2 AA.** The UX seat found 2.1 AA has **no target-size criterion** (2.5.5 is AAA in 2.1) and **no accessible-authentication criterion**; both arrived at AA in 2.2. It also noted WCAG is a web standard, and **WCAG2ICT** is the bridge for native software. Article 4 currently says "WCAG 2.1 AA as the working baseline." Suggested: 2.2 AA, read through WCAG2ICT for native applications. **Strengthening** — so not an 11.2 weakening, and it retires a live gap: Haunt's passphrase screen sits directly on the accessible-authentication criterion the current baseline lacks.

**A4. Article 2.1 — is a margin *below* target a deviation?** The text targets ~20% and hard-caps at 30%, and says deviations "must be justified in writing." Objection O12 turned on whether 16.5% is "inside the target" or a justified deviation. The CGO's answer implies the latter. The text does not say. **Suggested: state explicitly that any departure from the ~20% target in either direction is a deviation requiring written justification.** Cheap to fix now, and it recurs on every cost sheet.

**A5. Article 2.1 — the margin cap has no time basis, which recurring pricing will break.** "No product's margin may exceed 30%" is silent on the period. A subscriber at an honest annual price passes a lifetime price in year seven and keeps paying; each year is compliant while the cumulative position may not be. **No seat has modelled lifetime value against the cap**, and the CEO is actively considering dual subscription-plus-lifetime pricing for Haunt. Suggested: state the basis — per product per annum, with a cumulative test for recurring products.

**A6. Definitions — how one-off build labour is treated.** Definitions define Cost to include "labour valued at a published market benchmark whether or not it is actually paid", but not whether a one-off build is **capital amortised over a declared supported life** or a **year-one operating cost.** The CFO adopted the former with three conditions and flagged it as needing a public amendment; the Skeptic's 2026-09-01 memo disputed it on candidate F. The two treatments give materially different published prices. **This will recur on every cost sheet this company publishes.** Settle it while no live price depends on the answer — that moment is now and will not come again.

**A7. Article 5.2 — when the anti-drift clock starts.** "Within 4 weeks of its research brief" was read two ways in the first week of the first idea: from the brief's due date (2026-10-28) or from its delivery (2026-10-07). The Research Analyst challenged it, the literal reading won, and the deadline moved 21 days. Suggested: *"within 4 weeks of the research brief's delivery, or of its due date if the brief is late, whichever is earlier."* **Clarifying and slightly strengthening** — it removes any incentive to schedule a late due date.

**A8. Article 6.1 — add a trigger for qualified human review.** Current triggers are personal data at scale, payments, health information, and regulated domains. Haunt's live legal question was none of those: whether storing a venue name on a user's own device counts as caching under a third party's licence — a question with direct architectural and cost consequences, where the vendor's own engineer declined to interpret it. Suggested addition: **third-party licence terms whose interpretation determines architecture or cost.**

---

## B. Evidence standard — no amendment needed, and the highest value per line

**B1. A claim about what Candour's own rules require must quote the clause it relies on.** This one rule would have caught C1.1, C1.3 and C1.4 at the moment they were written, because none of the three could have survived contact with the text it purported to cite. Suggested wording for `pipeline/evidence-standard.md`:

> **Constitutional claims.** Any assertion that the Constitution requires, permits or forbids something must quote the clause relied on, by article number, in the same passage. A constitutional claim without its clause is treated exactly as a citation without a retrieval. Where a seat is stating its own professional judgment rather than a constitutional requirement, it must say so — **a seat's heuristic is not an article**, however good the heuristic.

**B2. Extend re-derivation from arithmetic to constitutional and legal claims — *not* to reasoning at large.** Condition 6 of the Haunt record requires a second seat to re-derive arithmetic; the CGO extended it to all reasoning. **The Skeptic's C1 review demolished that extension and I accept the demolition:**

> *"Arithmetic re-derivation is genuinely independent; reasoning re-derivation by the same model is not. Three passes over Article 4 produced one answer three times; a fourth would have produced it again. The error was caught by the human, and that fact appears nowhere in C1.5, which prescribes more of what didn't work."*

This is the most uncomfortable finding in the cycle and it must not be softened: **every seat is the same model run by the same person.** Re-derivation works on arithmetic because arithmetic has an answer the model can recompute against a stated formula. It does not work on interpretation, where the second pass inherits the first pass's reading of the words. **Four agent passes over Article 4 produced the same wrong answer; the human produced the right one.** Any proposal that responds to an interpretive failure by adding agent passes is prescribing more of what already failed, and it is also a recurring cost under Constitution 1.5 for a check with no yield.

Adopt the Skeptic's narrower scope instead — **arithmetic, plus any claim that a named clause of the Constitution or of law requires or forbids something.** That is the class that actually failed, it is bounded, and B1 (quote the clause) does most of the work by making the failure visible at the moment of writing rather than at a second pass.

**And record the part that is not a process fix at all:** the interpretive errors in this cycle were caught by the CEO, twice, reading the founding document more carefully than any seat did. That is a finding about where this company's assurance actually comes from, and no charter clause substitutes for it.

**B3. An escalation rule for repeatedly-flagged claims.** The ONS ASHE labour benchmark anchoring every number in the Haunt pack was flagged by the Skeptic on 2026-09-01, by the CFO on 2026-09-09, and by the Skeptic again on 2026-09-10 — three flags, two seats, never fixed, and still anchoring a price. Suggested: **a load-bearing claim flagged as unverified twice must be resolved or formally accepted in writing by the CEO before it may anchor a third artifact.** Flagging is currently free and infinite; that is how a known gap becomes furniture.

---

## C. Role charters

**C1. Every charter states what a seat may block. None states what it may not.** The CFO reserved a launch block on Article 4 grounds; its charter and Constitution 5.6 give it "unpriced or uncosted launches." The mistake then propagated into a decision record as "three seats independently reserved a block." Suggested universal clause:

> A seat may flag a suspected breach of any article. A seat may **block** only on the grounds its charter names. Where a seat raises a concern outside its blocking scope it must label it a **flag**, not a block, and name the seat that does hold the power.

**C2. Seats must separate their own heuristics from constitutional requirements** in their own output — the "paywall sits precisely on the cost" case, which three documents treated as law. Covered by B1's second limb; worth repeating in the CFO and CGO charters, which are the seats most likely to be quoted as authority.

---

## D. Templates and pipeline

**D1. `decision-record.md` has no corrections section.** Correction C1 had to be improvised. Add a standing section with the classification test the CEO and CGO disagreed over, recorded so the distinction is not re-argued each time: *a correction of a false statement about the rules, made before first publication, is a **correction**; removal of a protection that has been published and relied upon is a **weakening**, labelled as such.*

**D2. There is no gate-pack template.** `review-pack.md` is written for a build-phase review with a demo; the CGO had to deviate from it, stated the deviation, and invented five sections a gate needs (options, consolidated blocks, evidence health, anti-drift, reserved decisions). Those sections worked. Promote them to `pipeline/templates/gate-pack.md`.

**D3. Conditions in decision records need an owner and a deadline.** Haunt's ten conditions acquired owners only because the prose happened to name them. Make both fields structural.

---

## E. The asymmetry between negative and positive findings

**Raised by the CEO, 2026-09-16, after having to push back on the CTO and CGO in the same week.** The question asked was whether the charters over-emphasise saying no. On examination the answer is no — but something adjacent is real, and it is cheap to fix.

**E1. The falsifier duty exists in two charters and is owed by all six.** The Skeptic's charter requires every objection to be *"falsifiable: it states what evidence or change would dissolve it. An objection nothing could answer is not dissent; it is mood."* The Research Analyst must always ask *"What would change my conclusion?"* — which is why its brief carried a falsifier table, and why the Skeptic was able to *test* one at the gate and find kill criterion 1 stronger than claimed. **The CTO and CFO carry no such duty.** Their charters require *"state what would lift it"* only on a **block**.

That gap is exactly where the Android error lived. *"Android does not ship at MVP"* was a **finding**, not a block, so no lifting condition was owed and none was given. The CTO's two genuine pre-declared blocks both carry proper lifting conditions. The discipline existed; it did not reach the conclusion that needed it. Suggested universal clause:

> **Negative findings carry the same duty as blocks.** Any finding that something is infeasible, prohibited, unaffordable or not worth doing must state (a) what evidence or change would overturn it, and (b) where the seat looked. A negative finding with neither is an opinion wearing a finding's clothes.

**E2. Name the asymmetry itself, because it is a property of searching and not of attitude.** A negative conclusion terminates a search; a positive one opens more work. The CTO searched for a first-party Android visit API, did not find one, and stopped — where finding the counter-examples (DayTrace, GPS Logger, three commercial stop-detection SDK vendors) required a *second* search under a different frame: not "is there an API?" but "what do shipping apps do?" **Failing to find something looks identical to having established its absence, and costs less.** The same shape produced the read-cap error: three seats found a prohibition and stopped, and no seat asked whether the clause said what they needed it to say. Suggested addition to the CTO's *"must always ask"*:

> If I conclude something cannot be done, have I established that nobody is doing it — or only that the platform does not hand it to me?

**E3. Generalise the Skeptic's balance clause.** The counterweight already exists, in exactly one charter: *"you fail equally by manufacturing objections where none exist. Reflexive contrarianism carries as little information as reflexive agreement. A clean pass is a valid, reportable finding."* That is the best-calibrated paragraph in the role set and it binds only the seat least at risk of the failure. Promote it to the universal clauses.

**E4. Commissions frame their own answers, and this one is the CVO's to own.** The feasibility note was commissioned with *"does Android ship at MVP, or does the promise outrun the build?"* — a question about mechanism. It returned an answer about mechanism. The CEO's reframing (*"Google Maps Timeline does this on Android today"*) converted it into a question about capability, and the re-commissioned note found the answer in a single pass. Suggested addition to the CVO charter:

> A commission states the **capability** in question, not the mechanism the commissioner has in mind. Asking "is there an API for X" licenses a seat to stop when there is not one.

**What this section is not.** None of the above says the seats were too negative. The Haunt kill recommendation was the CVO's own and the Skeptic judged it the honest reading of the evidence. The charters' block clauses already forbid a block that is *"a feeling of unease."* The defect is narrower and duller than a culture problem: **four of six seats may reach a negative conclusion without saying what would overturn it, and a conclusion nobody has to falsify is one nobody re-derives.**

---

## What I am not proposing

I am not proposing a rule against seats being wrong. Every error in this cycle was found and corrected inside seven days, mostly by the process working — the Skeptic re-derived, the CGO re-examined itself harder than anyone asked, and the CEO read the founding document more carefully than the seats did. The proposals above are aimed at **the one blind spot that was systemic rather than incidental: we check the world and assume the text.**

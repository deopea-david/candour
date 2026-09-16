# Candour change log

Maintained per Article 11: every amendment recorded with date, change, and rationale. Amendments that weaken a customer-facing or transparency rule are labelled **WEAKENING** (11.2).

## v1.2 — 2026-09-16

**Constitution text amended** (first change to the text since v1.0), plus evidence-standard, charter and template amendments. Source: the Haunt discovery and gate cycle (2026-09-09 → 2026-09-16), the Skeptic's twelve gate objections and its review of Correction C1, and `pipeline/governance-review-2026-09.md`.

**The occasion, stated plainly because it is the point.** During that cycle three documents asserted a constitutional prohibition that does not exist, one seat redefined a term the Constitution explicitly defines, another seat's heuristic operated as law in three artifacts, and a claim that three seats had independently blocked survived into a decision record when only one held the power. **No agent seat caught any of it. The CEO did, twice, by reading the founding document more carefully than the seats had.** The amendments below follow from that, and from the Skeptic's finding that adding agent passes cannot fix an interpretive failure, because every seat is the same model.

### Constitution

1. **Article 4, export clause — scope clarified.** *"available at any time, at no charge and with no penalty"* now reads *"…at no charge, and with no penalty or disadvantage imposed for having exported,"* with an express statement that the clause governs exit and is **not** a requirement that an export reproduce the product's own experience, nor a rule about what a product may gate internally. **Clarifying, not weakening** — it states the meaning the clause already bore. _Rationale: three seats read the modifiers as attaching to the user's data generally, and built an absolute prohibition on it. The reductio that settled it: export is worse than the app in every product that ships one, so a reading on which that gap is itself a penalty is satisfiable by nothing._
2. **Article 4, accessibility baseline — WCAG 2.1 AA → WCAG 2.2 AA**, read through **WCAG2ICT** for native software. **Strengthening.** _Rationale: 2.1 AA has no target-size criterion (2.5.5 is AAA there) and no accessible-authentication criterion; both are AA in 2.2. The UX seat found a live product feature — a passphrase screen — sitting directly on the criterion the old baseline lacked. WCAG is written for the web; WCAG2ICT is the bridge for native applications._
3. **Article 2.1 — a deviation in either direction is a deviation.** A margin below the ~20% target is recorded and justified like any other, never labelled as no deviation. **Strengthening.** _Rationale: a cost sheet carried a 16.5% margin while recording "deviation from target: none proposed". Article 9 lists mislabelling as a gaming vector, and a justification requirement means nothing if a deviation can be labelled away._
4. **Article 2.1 — the margin cap gains a time basis.** Per product per financial year, and for recurring products tested **cumulatively over the customer's lifetime**. **Strengthening.** _Rationale: the 30% ceiling was silent on period. A subscriber at an honest annual price passes a lifetime price around year seven and keeps paying — every individual year compliant, the cumulative position possibly not. Found while the CEO was considering dual subscription-and-lifetime pricing, i.e. before it could bite._
5. **Definitions, Cost — one-off build labour is capital**, amortised straight-line over the product's **declared supported life**, with three binding conditions: the period must equal a published support commitment; any unamortised remainder is written off publicly on discontinuation (7.2); the period may be shortened, never lengthened. Absent a published support commitment, build labour is a first-year operating cost. _Rationale: the CFO and the Skeptic had adopted opposing treatments, which give materially different published prices, and the question recurs on every cost sheet the company will ever publish. Settled while no live price depended on the answer — a moment that does not come twice. The CFO's treatment was adopted; the tie to a **published** commitment is what stops the period being chosen to flatter a price._
6. **Article 5.2 — when the anti-drift clock starts.** Four weeks from the research brief's **delivery**, or its due date if the brief is late, **whichever is earlier**. **Strengthening.** _Rationale: read two ways in the company's first week. A brief delivered three weeks early would, on the looser reading, have bought three weeks of slack. Delivering early now shortens the window; it never extends it._
7. **Article 6.1 — new trigger for qualified human review:** third-party licence terms whose interpretation determines a product's architecture or cost. _Rationale: the first live legal question the company met fitted none of the existing triggers — whether storing a venue name on a user's own device is "caching" under a vendor's licence — and the vendor's own engineer declined to interpret it._
8. **Article 10 — a gap named rather than left to be discovered.** The Constitution says nothing about a product limiting access to content the customer authored and holds on their own device. The gap is recorded, with the incident that exposed it, and **deliberately left open**: legislating it in haste around one product's pricing question is how a constitution acquires rules it cannot defend. What binds meanwhile is stated. _Rationale: silence is what the seats filled by improvising. A named gap is a commitment to argue about it in the open when it next matters._

### Evidence standard

9. **New section: claims about our own rules.** Any assertion that the Constitution, a law, a licence or a standard requires, permits or forbids something must **quote the clause, by number, in the same passage** — a constitutional claim without its clause is treated exactly as a citation without a retrieval. **A seat's heuristic is not an article.** Re-derivation by a second seat covers arithmetic **plus claims that a named clause requires or forbids something**, and expressly **not** reasoning at large — because every seat is the same model, a second interpretive pass inherits the first's reading, and four passes over Article 4 produced the same wrong answer where the human produced the right one. **Twice-flagged is escalated:** a load-bearing claim flagged unverified twice must be resolved or formally accepted by the CEO before anchoring a third artifact.

### Charters (all twelve)

10. **Negative findings carry the same duty as blocks** — state what would overturn the finding, and where you looked. _Rationale: "state what would lift it" bound only blocks. A CTO conclusion that Android was infeasible was a **finding**, owed no falsifier, and was wrong: the platform lacks the primitive, but third-party apps ship the capability. A negative terminates a search where a positive opens one, so absence of evidence is the cheaper conclusion and looks identical to evidence of absence._
11. **Both failure modes, for every seat** — the Skeptic's clause promoted to the universal clauses: manufacturing objections fails as surely as missing problems, and a clean pass is a valid, reportable finding. _Rationale: the best-calibrated paragraph in the role set bound only the seat least at risk of the failure._
12. **Block only on your own grounds.** A seat may flag any suspected breach but may block only on the grounds its charter names; a concern outside that scope is a **flag**, and names the seat that does hold the power. Seats repeating one another do not multiply into independent blocks — the evidence standard's independence test applies to seats as to sources. _Rationale: a CFO block was reserved on Article 4 grounds outside its charter, a second seat concurred, a third was counted before it had opined, and "three seats independently reserved a block" reached a decision record._
13. **CTO** gains a standing question: if I conclude something cannot be done, have I established that **nobody is doing it** — or only that the platform does not hand it to me?
14. **CVO** gains a commissioning discipline: a commission states the **capability** in question, not the mechanism the commissioner has in mind. Where a commission's framing produced a wrong answer, the error is the CVO's, not the answering seat's.

### Templates

15. **`decision-record.md`** gains a **Corrections** section carrying the correction-versus-weakening classification test, so the distinction is not re-argued each time; conditions gain **owner** and **due/gates-what** columns; the overrules section now requires "none" to be stated precisely.
16. **`pipeline/templates/gate-pack.md` added.** `review-pack.md` is build-shaped with a demo; the CGO had to deviate from it at the first gate and invented the five sections a gate needs (options, consolidated blocks, evidence health, anti-drift, reserved decisions). Those sections are now the template, including the instruction that page one summarises **the disagreement, not the recommendation**, and that the recommended-next-step section stays empty because the decision is the CEO's.

_Not labelled WEAKENING: no amendment in this version removes or narrows a customer-facing or transparency protection. Items 2, 3, 4 and 6 strengthen; 1 clarifies a clause whose meaning was misread in Candour's own favour-of-caution direction; 5, 7 and 8 close definitional and coverage gaps._

## v1.1 — 2026-08-30

Charters and pipeline amendments (constitution text unchanged), in two themes: guarding against reflexive no-bias, and the evidence standard guarding against hallucinated claims and citations.

1. **Skeptic charter:** both failure modes now explicit — missing real problems _and_ manufacturing fake ones; a clean pass is a valid, reportable finding. Every objection must be tiered (fatal/serious/friction) and falsifiable (states what would dissolve it).
2. **Blocking seats (CGO, CTO, CSO, CFO, QA, UX):** every block must cite the specific article, standard, or criterion breached and what would lift it. No vibes-blocks.
3. **/audit:** now includes a calibration review scoring past dissents and blocks against outcomes — the long-term, evidence-based answer to "is this seat too negative or too soft?"
4. **Dissent memo template:** verdict line (including clean pass) and objection tiers added.
5. **`pipeline/evidence-standard.md` added** (canonical): claim taxonomy [E] retrieved evidence (links mandatory) / [K] model knowledge (confidence stated) / [I] inference / [J] judgment; citing from memory prohibited and treated as fabrication; independence rules (a press release rewritten thrice is one source); single-origin claims flagged; secondary-evidence honesty for a company with no industry contacts.
6. **Skeptic becomes the verifying seat:** retrieves all load-bearing sources itself and checks claim against source, samples the rest with the sampling stated, flags unverifiables, challenges load-bearing [K] claims. Dissent memos gain a verification report.
7. **Clean invocation rule:** the Skeptic is spun up fresh with file paths only — no summaries, opinions, or steers from the invoker — and reports any detected steering in its memo. /gate rewritten to invoke it neutrally, first.
8. All charters, agents, research templates, `CLAUDE.md`, and the boardroom instructions reference the standard; the boardroom instructions now also state the surface's honest limit (one shared context — formal gates belong in Claude Code).

## v1.0 — 2026-08-30

All placeholders resolved by the CEO; the constitution leaves draft status. Amendments continue under Article 11.

1. **Numbers fixed:** distribution cap **35%** of annual surplus (strictly annual — no CIC-style carry-forward, deliberately stricter than the CIC regime); decision window **4 weeks**; research briefs due **3 weeks** from commissioning; post-sale locks (pricing and the buyer's constitution adoption) **3 years**; sale-proceeds slice **20%** of net proceeds; discontinuation notice **90 days** with free data export for **90 days** after shutdown.
2. **Article 2.1 strengthened:** a hard per-product margin ceiling of **30%** added — no justification permits exceeding it — plus an explicit no-portfolio-averaging rule: margins are per product, so no customer unknowingly subsidises another product. _Rationale: a portfolio average would license cross-subsidy and be gameable with a token low-margin product; the CEO chose the stricter per-product regime._
3. Article 10's "placeholders still open" admission removed (resolved); Article 11.4 reworded from a condition into a record.

## v0.3 — 2026-08-30

Source: the boardroom's own Article 7 dissent (raised by the Project's Skeptic seat, reviewed and approved by the CEO), plus the CEO's decision to generalise the NHS annex.

1. **Article 7 retitled "Endings"** and extended beyond sale: **7.2 Discontinuation** (≥[90] days' notice, free data export through and beyond shutdown, open-sourcing where third-party rights allow, closing cost sheet) and **7.3 Departure** (walking away triggers 7.2 for every live product). _Rationale: the cheapest abandonment of customers was a shutdown, which old Article 7 never touched._
2. **Sale conditions hardened:** buyer's constitution adoption now carries a [3]-year lock (condition 1 previously had no duration); the sale agreement must name the condition-4 recipient as entitled to enforce conditions 2–3 under the Contracts (Rights of Third Parties) Act 1999; "each transaction, however small" stated explicitly; the sale assessment must itemise all consideration and the date of first contact.
3. **"Net proceeds" defined** (Definitions) — all consideration in any form including side arrangements routed to the founder — and added to Article 9's loophole table. _Rationale: at the 10% floor with a generous reading of "net", condition 4 could be hollowed without amending a word._
4. **Article 11.3 trigger made objective:** the amendment freeze starts at any written expression of interest, sent or received, with the date published. **Article 10** now admits the residual gap: the rule makes dodging it require an affirmative false statement, not a definitional shrug — it cannot make lying impossible.
5. **Article 8 generalised from "The NHS project annex" to "Non-profit initiatives":** the CEO may designate any product non-profit (permanent, published); designated initiatives take zero distribution, publish minimal costs, can never be sold (only transferred to an asset-locked body), intend to spin out when real, and are encouraged — not required — to be open-source and self-hostable, decided per initiative. They are the first-preference recipients of waterfall donations (2.3) and sale proceeds (7.1). _Not labelled WEAKENING under 11.2 (the old annex was neither customer-facing nor a transparency rule), but noted candidly: a named commitment to the NHS project became a generic mechanism, because a constitution should not depend on a project that may never go live. The NHS idea now earns designation through the pipeline like anything else._

## v0.2 — 2026-08-30

Source: full-document review (all findings reviewed and approved by the CEO before application).

1. **Definitions block added** (new section after the Preamble): cost, profit, reserve, surplus, distribution. _Rationale: Article 9 locked these definitions against quiet change, but they were never defined — the loophole clause was itself gameable._
2. **Articles 2.2/2.3 reconciled into a profit waterfall** — reserve top-up → optional distributions ≤[35]% of surplus → price cuts / new products / donations. **WEAKENING** label applied per 11.2, transparently: as literally drafted, old 2.3 allocated all above-reserve surplus to customers/products/donations with no distribution step, so inserting one weakens that literal text. The old text contradicted 2.2, which always permitted capped distributions; this amendment resolves the contradiction in favour of the intended meaning — the founder may be paid, transparently, within the published cap.
3. **Article 3:** decision records for _every_ gate outcome — kill, proceed, or **park** — are published. _Rationale: parks are the decisions most tempting to leave quiet._
4. **Article 4:** data portability added — customers can export their data in a usable, machine-readable format, free, anytime. _Rationale: principle 1.2 forbade lock-in profits but no product rule delivered it._
5. **Article 5.1:** pipeline stage order corrected (discovery precedes proposal and gate). _Rationale: drafting error; the templates and commands already worked this way._
6. **Article 5.2:** research briefs due [3] weeks from commissioning (one written extension); an overdue brief starts the decision clock at its due date. _Rationale: the anti-drift clock could previously be stalled forever upstream in "awaiting research"._
7. **Article 5.6 added:** blocking powers and the CEO-only, publicly-recorded overrule codified in the constitution rather than living only in charters.
8. **Article 10:** AI workforce disclosure — Candour is operated by its founder and AI agents under charters, stated publicly.
9. **Footer:** founding year set (2026).
10. **Repo:** `LICENSE.md` added (governance docs CC BY-SA 4.0; product code decided per product, presumption of open source), `.gitignore` added, `roles/dormant-seats.md` cleaned of subagent boilerplate that applied only to active seats.

## v0.1 — 2026-08-30

Founding draft: constitution, twelve role charters, pipeline templates, Claude Code agents and commands, boardroom Project instructions.

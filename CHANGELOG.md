# Candour change log

Maintained per Article 11: every amendment recorded with date, change, and rationale. Amendments that weaken a customer-facing or transparency rule are labelled **WEAKENING** (11.2).

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

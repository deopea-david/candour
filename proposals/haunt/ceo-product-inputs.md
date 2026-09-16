# CEO product inputs — Haunt

**Status:** captured by CVO, 2026-09-16, during and after the discovery gate · **Owner on receipt:** PM/BA at `/build`
**Purpose:** the CEO raised these after the gate pack was compiled. They are not in the proposal, the feasibility note or the UX note. They are recorded here so requirements are written *around* them rather than retrofitted to them — the CTO's standing warning is that schema and settings-tree decisions are cheap now and expensive later.

---

## 1. The venue page — probably the product, not a feature

**CEO, 2026-09-16:** *"a feature could be to see the venues list that the user has been to, including a review summary and notes for the venue."*

**Why this is more significant than it was raised as** [J, CVO]: this is Letterboxd's *film page* applied to a pub — every visit, your rating, your notes, an aggregate verdict on a place. Discovery found Arc Timeline 4 already has a places tab with visit history and notes on timeline items; the two gaps it could not close were **venue ratings and Android**. The venue page is where a rating stops being a number on an event and becomes a standing judgment on a place. **On the evidence in `research/haunt-brief.md` §3.1, this is the differentiator — the timeline is the capture mechanism that feeds it.**

**Consequence for requirements:** the venue is a first-class entity with its own identity, aggregate state and history — not a label on a visit. Deciding that after the schema exists is the expensive version.

**Consequence for the venue-index spike (decision record Condition 2):** this *raises* the stakes on it. The UX note found that Overture's documented duplicates would silently split accumulated visit counts and rating history. The venue page is precisely where that corruption becomes visible, and there is no server and no backfill. The spike's re-specified metrics (duplicate rate and junk rate in the top five candidates) are load-bearing on this feature, not merely procedural.

---

## 2. Session segmentation — detect when a night ends, not when the day does

**CEO, 2026-09-16:** *"some algorithm used to detect when a session ends and a new one begins. So it is not just per day for example."*

**The instinct is right and the failure case is specific** [I, CVO]: calendar-day bucketing splits a night out at 00:00 — which is the exact moment a night out is most likely to be in progress. A product whose founding example is "a night out" cannot use a boundary that reliably bisects one.

**Three things that must be decided at schema time, not at build time:**

1. **Sessions must be *derived*, not stored as immutable facts.** Visits are the atomic record; a session is a grouping computed over them. If sessions are persisted as first-class immutable rows, every future improvement to the segmentation algorithm either corrupts existing history or cannot be applied to it. Derived-and-recomputable means the algorithm can be improved for the life of the product. **This is the single most consequential line in this document** and it costs nothing to get right now.
2. **The user's override is authoritative and must be persisted separately from the algorithm's output.** Any heuristic will merge two nights or split one, and this is a *journal* — the user's account of their own evening outranks ours. Merge and split must exist, and a user's manual correction must survive recomputation rather than being overwritten the next time the algorithm runs.
3. **"Home" is an inference, and a sensitive one.** The most reliable session boundary is returning to a sleep location, which means the app derives where the user lives. That inference stays on-device like everything else, but it should be **visible and editable** rather than silent — Article 4's "state why" applied to a derived fact rather than a collected one. The CGO's compliance note (§3) rests the household-exemption GDPR position on the data never leaving the device; that position is unaffected, but an *undisclosed* home inference is a transparency problem even where it is not a legal one.

**The connection nobody has drawn yet** [I, CVO, from `products/haunt/ux-note.md` §1]: UX identified the confirmation loop as the product's core interaction *and* its biggest usability risk, and designed it as a pull queue with bulk day-level confirm/discard. **Session segmentation improves that directly** — confirming one night out with four venues is a materially better interaction than confirming four separate visits, and it reduces the queue pressure that UX was designing defences against. These two features should be specified together rather than separately.

**Not yet assessed by any seat.** No effort estimate exists; it is not in the CTO's 16–19 week figure, and the CFO's re-derivation under Condition 1 should be told about it before it runs, not after.

---

## 3. Dual pricing — open question, sequenced behind the CGO

**CEO, 2026-09-16:** *"Are we ruling out subscription at a lower cost and lifetime at a higher cost?"*

**Not ruled out.** What UX ruled out was *free + subscription*, on the grounds that a lapse either locks the journal (a read-cap with a clock) or changes nothing (so nobody renews). Paid subscription alongside paid lifetime has not been assessed by any seat.

**Why it is sequenced, not answered:** the lapse behaviour is the read-cap question in different clothing, and the CGO is re-examining the read-cap basis now, following two arguments from the CEO that the CVO conceded (the export clause is an exit-penalty clause rather than a UX-parity clause; and "it costs us nothing" substitutes marginal cost for the Constitution's own definition of Cost, which includes benchmarked build labour).

**Three constraints for whoever models this:**

- **Article 2.1 binds the spread.** With no server, the honest subscription price on the current sheet is **£3.21–£4.88/year**; lifetime lands near **£29.59**. Arc's £44.99/year is not available to Candour — the 30% margin cap forbids it. The shape is right; the spread is far narrower than the market's.
- **A third lapse behaviour exists and is clean under every reading:** a lapse stops *automatic capture* while everything already written stays readable, editable and exportable forever. This matches the only free-tier design the UX note found survivable ("capture paid, manual free") and sells the engine rather than access to the user's own memories. Note the App Store constraint UX attached: a non-capture tier must not request `Always` location.
- **An unmodelled hazard in offering both.** At £4.88/year a subscriber passes the £29.59 lifetime price in year seven and continues paying. Margins are per product under 2.1 and capped at 30%; **cumulative** margin on a long-tenure subscriber may breach the cap while every individual year looks compliant. No seat has modelled lifetime value against the margin cap.

**Governance note:** `decisions/2026-09-16-haunt-gate.md` records the one-off purchase *shape* as decided, with only the number open (Condition 9). Moving to dual pricing changes the shape. That is the CEO's under 5.4, but it amends a record that publishes under Article 3 by **2026-10-16**, so it is corrected in the open rather than silently superseded.

---

## Commissions these imply, for the CVO to place

- **PM/BA** — items 1 and 2 enter requirements as first-class scope, with the three schema decisions in item 2 settled before any data model is signed off.
- **CTO** — effort for session segmentation; and the derived-vs-stored decision confirmed as an architectural constraint rather than an implementation detail.
- **CFO** — Condition 1's re-derivation must include session segmentation and the venue page, and must not run before this document reaches it.
- **UX** — specify the confirmation queue and session segmentation together; and model the three lapse behaviours once the CGO reports.

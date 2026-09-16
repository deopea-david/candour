# Dissent memo — Haunt, Correction C1

**Date:** 2026-09-16 · **Author:** The Skeptic · **Published unedited in the decision record.**
**Subject:** `decisions/2026-09-16-haunt-gate.md` — Correction C1 and the replacement Condition 8 (8.1–8.5).
**Standing:** The gate has passed; Constitution 5.3 does not compel this memo. It exists because Condition 6 institutionalises re-derivation by a second seat, and the reasoning in C1 had not been re-derived by one. I am not re-opening the PROCEED. I hold no block (Constitution 5.6) and am not asking for one.

**Artifacts read cold, from disk, this session:** `constitution.md`; `roles/skeptic.md`, `roles/cgo.md`, `roles/cfo.md`, `roles/ux-lead.md`; `pipeline/evidence-standard.md`; `pipeline/templates/dissent-memo.md`; `decisions/2026-09-16-haunt-gate.md` (in full); `proposals/haunt/ceo-product-inputs.md` (in full); `proposals/haunt/dissent-memo.md` (verdict and O1–O3 in full, remainder sampled); `products/haunt/compliance-note.md` §4.3–§5.3 and full heading structure; `products/haunt/cost-sheet.md` §8 and full heading structure; `products/haunt/ux-note.md` §6–§7 and full heading structure. **Retrieved externally:** CRA 2015 s.36 and DMCCA 2024 s.227 (see Verification). **Retrieved empirically:** the repository's git state, to test C1.6's second ground.

---

## Verdict

**Serious concerns. None fatal. The correction's two central textual conclusions are correct, and I say so without hedging.**

C1.1 and C1.2 are right. I checked both against the Constitution's words rather than against the argument built on them, and the Constitution says what the correction now says it says. A seat that re-examined its own reasoning, conceded the two grounds it was challenged on, and then went on to find three more errors — two against itself — has done the thing this company says it wants. **That is the honest headline and it should not be buried under what follows.**

What follows is nonetheless substantial, and it divides into three kinds:

1. **The correction is incomplete.** It disposes of three grounds for the withdrawn condition and never mentions the fourth, which appears in all three of the documents it corrects: **Article 1.2 (lock-in)**. It then uses Article 1.2 to ground the replacement. A correction that relies on a clause it did not dispose of has not finished.
2. **The replacement rule (8.1–8.5) is written about *entries*, and the product's differentiator is *aggregates over entries*.** The CEO's own product inputs, captured the same day, make the venue page "probably the product, not a feature." Nothing in 8.1–8.5 stops a visibility window from making the venue page quietly state a falsehood about the user's own life, and improve on payment.
3. **The process finding underneath all of it is not the one C1.5 makes.** The error did not harden because no seat re-derived another seat's reasoning. It hardened because three seats agreeing was counted as corroboration, when by Candour's own evidence standard three seats are one source. Extending Condition 6 from arithmetic to reasoning does not touch that, because the second seat is the same model as the first.

**On the contested classification at C1.6, which I am the last seat to reach: I do not dissent from the CORRECTION label.** I dissent from two of its three grounds, and from the implicit claim that the label disposes of the whole act. Detail at §4.

---

## 1. The textual arguments, checked against the Constitution's words

I did this first, before reading any seat's argument about it, for the reason the invocation gives: both are claims about what Candour's own governing document says, and they should be checkable by reading it.

### 1.1 C1.1 — the export clause. **Verified. The correction is right.**

Article 4's bullet reads in full [E — `constitution.md` Article 4]:

> *"Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge and with no penalty."*

The clause opens with leaving. Its object is *export*. The three modifiers — "available at any time", "at no charge", "with no penalty" — are a list attached to the noun they follow. There is no reading on which "with no penalty" governs the user's access to their data generally while "at no charge" and "available at any time" govern only export; the three travel together or none do, and "at no charge" plainly cannot mean the product is free. **The modifiers attach to export.**

Article 7.2 confirms it independently [E — `constitution.md` Article 7.2]: *"Full data export (Article 4) available throughout the notice period and for 90 days after shutdown, free."* The Constitution's own second use of the clause is about export at an ending. That is its domain.

`compliance-note.md` §4.4 said [E — verbatim]: *"A read-cap is a penalty, applied at any time, to the user's own data."* That sentence detaches the modifiers from export and reattaches them to the data. **It is a misreading, and the concession is correct.**

**One caveat, which matters more than it looks.** The record presents the CEO's reductio as load-bearing: *"export is worse than the app in every product that has ever shipped one, so a reading on which that gap is itself a penalty is satisfiable by nothing."* That reductio attacks a weaker version of the original than the original's strongest form. The misreading did not assert that the *export/app fidelity gap* is a penalty; it asserted that *withholding in-app access as the price of not paying* is one — an adverse consequence imposed by the trader, which the fidelity gap is not. A defender of the original could accept the reductio and keep the claim.

**It would not help them, because the grammar already settles it.** But the record should rest C1.1 on the grammar and Article 7.2, not on the reductio, because the strength of "that claim was false" is the first of C1.6's three grounds for the classification, and a ground should rest on its strongest support. **Recorded as friction, not as a defect in the conclusion.** (Objection C1-O9.)

### 1.2 C1.2 — the definition of Cost. **Verified as to the text. Over-stated as to the consequence.**

Definitions [E — `constitution.md`, Definitions]:

> *"**Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and labour valued at a published market benchmark whether or not it is actually paid."*

Article 2.1 [E]: *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

So Candour's defined Cost is a total that includes benchmarked build labour. `compliance-note.md` §4.4 argued [E — verbatim] that a cap *"would gate something that costs Candour nothing, which makes it arbitrary scarcity rather than a pricing mechanism"*, and that *"on the MVP as proposed there is no cost-aligned free tier available, because there is no marginal cost to align one to."* That is marginal cost. The Constitution's is total. **The substitution is real and the concession is correct.**

**Where I part company is the Article 9 characterisation.** C1.2 states: *"Article 9 names redefining 'cost' as a gaming vector… the CGO records that the direction is not a defence, because Article 9 names the redefinition and not its direction."*

Article 9's row reads [E — `constitution.md` Article 9]: *"Redefining 'cost,' 'surplus,' 'reserve,' or 'net proceeds' | Definitions may only change by public amendment (Article 11)."* Its exposure mechanism is **public amendment of the definitions**. The row above it — *"Inflating costs to raise the allowable price (2.1)"* — is the one about cost arithmetic, and its exposure is itemised cost sheets. Neither describes what happened here. What happened here is that a seat used "costs us nothing" colloquially inside an argument about **where a paywall sits**, which is not a price computation, does not enter a published number, and did not change any definition in any document. No cost sheet was affected. No price moved.

**So C1.2's finding is right and its severity is wrong.** And the severity error matters, because C1.6 ground 3 states the principle it breaches [E — verbatim, same document]: *"inaccuracy in the self-critical direction is still inaccuracy."* C1.2 puts an Article 9 gaming-vector finding on the record against a seat whose actual error was loose language in an argument that C1.4 disposes of on other grounds entirely. **A record that names over-severity as a failure mode two sections after committing it has not applied its own test to itself.** (Objection C1-O10.)

**And C1.2 and C1.4 are the same error stated twice, in framings that exclude each other.** C1.4 establishes that *"nothing in the Constitution constrains where a paywall sits."* If that is right — and it is; I checked, and Article 2.1 constrains the price *level* (~20% target, 30% hard cap, per product, no cross-subsidy) and says nothing about paywall placement — then **no** cost concept constrains paywall placement, and which definition of Cost the CFO and CGO used is moot. C1.2 only has work to do if you first accept the premise C1.4 demolishes. The record presents them as two independent findings. They are one finding with two incompatible dispositions. (Objection C1-O8.)

### 1.3 The ground C1 never disposes of: **Article 1.2**

This is the most consequential thing in this memo's first half.

The withdrawn condition was never grounded on the export clause alone. It was grounded on the export clause **and Article 1.2**, in all three documents [E — verbatim]:

- `cost-sheet.md` §8.2, the originating table: *"Withholds the user's own local data behind a paywall. **Article 4** (data at any time, no penalty), **Article 1.2 (lock-in)**. This is the most tempting design and the clearest breach."*
- `cost-sheet.md` §8.2, again: *"Cap tightened for existing free users after launch | Retroactive; **Article 1.2**."*
- `ux-note.md` §6.2: *"History window ('last 30 days free') — **Breach. Article 4 and Article 1.2.**"*
- `ux-note.md` §7, block **B2**: *"**Article 4** (data 'at any time, at no charge and with no penalty'; dark patterns) **and Article 1.2 (lock-in)**."*

Article 1.2 reads [E — `constitution.md` Article 1]: *"**No exploitation.** We do not profit from confusion, lock-in, addiction, or information asymmetry."*

**Correction C1 does not mention Article 1.2 as a ground for the condition it withdraws.** It disposes of the export clause (C1.1), the Cost definition (C1.2), and the alignment heuristic (C1.4); it records that no clause covers gating authored content (C1.5). Article 1.2 appears exactly once in the whole correction — as *support for the replacement*, at 8.2: *"(Article 1.2; CRA 2015 s.36.)"*

So the correction **uses Article 1.2 to make the ratchet binding while leaving it undischarged as a ground for the rule it removed.** If 1.2 is strong enough to bind non-retroactivity, the record owes a paragraph on why it is not strong enough to reach the cap itself.

**My own reading, offered so this is not a bare procedural complaint:** I think a read-cap with complete, free, immediate, unpenalised export of *everything* is probably **not** lock-in in Article 1.2's sense. Lock-in is the inability to leave with what is yours; unconditional complete export is its antidote, and 8.3 makes that unconditional. On that reading Article 1.2 falls too, and the correction's conclusion survives intact.

**But that argument is mine, made now, and the record is what is being reviewed.** Three documents named a clause; the correction withdrew the rule without answering it. That is the same failure class C1.5 names — a ground carried across documents without being re-derived — occurring inside the document that names it. (Objection C1-O1.)

---

## 2. C1.3 — the blocks, checked against the charters and Constitution 5.6

### The CFO's block: **C1.3 is right.**

Constitution 5.6 [E — verbatim]: *"…and **CFO (unpriced or uncosted launches)**."*
`roles/cfo.md` [E — verbatim]: *"**Can block:** Launch of any pricing not backed by a published cost sheet; any proposal without a credible cost model."*

`cost-sheet.md` §8.2 reserved this [E — verbatim]: *"I am stating in advance, in writing, that a free tier which restricts access to entries the user has already created **breaches Constitution Article 4** and I will treat it as a launch-blocking defect."*

A design that breaches Article 4 is not an unpriced launch and not an uncosted one. The cost model was not absent; it was present and, on this point, disagreed with. **The block was asserted on grounds the charter does not reach. C1.3 is correct and the concession is properly made.**

### "One block was properly held, not three" — **understates the correction's own effect.**

C1.3 conflates two different questions, and they come apart here:

- **Was the block within the seat's charter?** CFO: no. UX: yes — `roles/ux-lead.md`: *"Can block: Release of flows breaching Article 4."* B2 is squarely Article 4. CGO: yes as to competence — its block is gate passage, and gate passage on constitutional-breach grounds is its charter's core.
- **Is the clause it cited still standing after C1.1?** CFO: n/a. CGO: no — its §4.4 reservation rests entirely on the misread export clause. UX: **only if Article 1.2 survives** (§1.3 above), because B2's Article 4 limb falls with C1.1 and its dark-pattern limb is answered by replacement 8.4.

`roles/ux-lead.md` requires that *"Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it — a block is a checklist item failing, **never a feeling of unease**."* The UX note's own correction banner concedes that what remains is *"its judgment that a read-cap is the wrong product… as judgment, not as law"* [E — verbatim, `products/haunt/ux-note.md`, banner]. **Judgment unattached to a failing checklist item is precisely what that charter sentence forbids a block from being.**

So the honest statement is narrower than the record's: **one block was competently held; whether any block is currently *grounded* turns entirely on Article 1.2, which the correction never addresses.** If 1.2 falls, the count of currently-exercisable Article 4 blocks on these facts is **zero**, not one. The record should resolve 1.2 and then state the count — the two findings are the same finding. (Objection C1-O2.)

### The third "seat" was never a seat. **This is the mechanism, and C1.3 corrects the count without correcting it.**

The full chain, verbatim and dated:

| Date | Seat | What it actually says |
|---|---|---|
| 2026-09-09 | **CFO**, `cost-sheet.md` §8.2 | **Originates.** *"That is not a paywall. That is a hostage, and the hostage is being held on the victim's premises."* Reserves a block. |
| 2026-09-10 | **CGO**, `compliance-note.md` §4.4 | *"**I concur with the CFO**, and I go further… I concur, without qualification, and I record my own block on the same facts. My charter's block is gate passage; the CFO's is unpriced or uncosted launches; **the UX seat holds one on Article 4 grounds. Three independent seats can stop this design** and I would expect all three to."* |
| 2026-09-10 | **UX**, `ux-note.md` §6.2 | *"Already blocked by the CFO, endorsed by the CVO; **I am the third seat. The CFO's formulation is the right one and I adopt it**: 'That is not a paywall. That is a hostage…'"* |

Read the CGO's sentence again. At the moment it was written, the UX seat had **not opined on the read-cap**. What the CGO counted was that *the UX seat holds a block power on Article 4 grounds* — a fact about the charter, true of every design ever proposed. **The third of the "three independent seats" was a charter clause.** When the UX seat did opine, it adopted the CFO's words verbatim and called itself the third.

So: one argument, authored once, concurred in once, adopted verbatim once, and then counted as three.

`pipeline/evidence-standard.md` already contains the rule that disposes of this [E — verbatim]: *"corroborating sources count only if they have separate origins. **Three articles rewriting one press release are one source.**"* And `roles/skeptic.md` contains the reason it applies with extra force inside this company [E — verbatim]: *"you are the same model, run by the same person, as every other seat. True independence is impossible."*

**Candour wrote the independence rule for external sources and never applied it to its own seats.** That is the finding. C1.3 corrects the arithmetic of the count. It does not correct the inference that produced it. (Objection C1-O3 — and see §5, because this is what Condition 6 fails to reach.)

---

## 3. The replacement rule 8.1–8.5

New text, no seat has reviewed it, so this is a first review rather than a re-derivation. I assess it against the design it is written for: a visibility window with optional favourites, on a one-off-purchase iOS product with no server.

### What is good, said plainly

**8.3 is the best clause in the correction and the CGO's claim for it is correct.** *"An export implemented against the visible set rather than the full set is the breach this article actually names."* That is exactly right, and it is the one place where Article 4's export clause — properly read per C1.1 — **does** bite on a visibility window. It is also an implementation-level trap rather than a policy one: a developer writing `SELECT … WHERE visible = 1` against the export path commits the breach without ever forming an intention. Writing it down as an acceptance criterion at requirements is the cheapest possible intervention and it closes a real exposure nobody had recorded. **No objection. Clean.**

**8.2 has a stronger legal backbone than the record claims, and I verified it.** CRA 2015 s.36(3) treats pre-contract information about *main characteristics, functionality and compatibility* as a term of the contract; s.36(4) then provides that *"A change to any of that information, made before entering into the contract or later, is not effective unless expressly agreed between the consumer and the trader"* [E — [CRA 2015 s.36, legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/15/section/36), retrieved 2026-09-16]. A shortened window is a change to disclosed functionality and is **not effective** without express agreement. So 8.2's ratchet is not merely a Candour promise; on a disclosed window it is close to a statutory floor. Worth recording both because it strengthens 8.2 and because it means Candour should claim less credit for it.

**8.1's citation checks out.** DMCCA 2024 s.227 defines material information as *"information that the average consumer needs to take an informed transactional decision"* and expressly catches information given *"in a way that is unclear or untimely, or in such a way that the consumer is unlikely to see it"* [E — [DMCCA 2024 s.227, legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2024/13/section/227), retrieved 2026-09-16]. The compliance note's reading of it survives the correction unchanged.

### C1-O4 [SERIOUS] — 8.1–8.5 are written about entries. The product is aggregates over entries.

`proposals/haunt/ceo-product-inputs.md` was captured **the same day as this correction** and opens [E — verbatim, CEO's own words]: *"a feature could be to see the venues list that the user has been to, including a review summary and notes for the venue"* — which the CVO then assesses as *"the differentiator — the timeline is the capture mechanism that feeds it"*, and *"probably the product, not a feature."*

Now apply a visibility window to it.

A user has visited The Bell eleven times over two years and rated it eight times. Six visits are inside the window or favourited; five are not. **What does the venue page say?** Nothing in 8.1–8.5 answers this, because every clause is written about *entries*:

- **8.5** requires aged-out entries to remain *"enumerable"* and *"restored in full on payment."* Enumerable is not counted. A list of hidden items is not a corrected average.
- **8.4** forbids *"'N memories expiring' prompts"* — so the app may not draw attention to the gap.
- **8.3** guarantees the export is complete — which is no help, because the false number is on screen, not in the export.

The available outcomes are: the venue page shows **"3 visits, average 3.8"** when the truth is eleven and 4.2 — *the app stating a falsehood about the user's own life* — or it shows a gap it is forbidden from explaining, or it computes over everything and the window has no effect on the one screen that matters.

**And the first outcome is a conversion mechanism built out of understating the user's history.** It is not a countdown, not a notification, not a badge; 8.4 does not name it. It is quieter than anything 8.4 forbids and it works better than all of them, because the pitch becomes "pay to find out what you actually did." Article 1.3 (*"Honest by default"*) and Article 4 (*"Remain honest in marketing: claims we cannot substantiate are claims we do not make"*) both bear on it, and neither is cited anywhere in Condition 8.

The same problem hits session segmentation, the CEO's second input: a night out with four venues, two aged out, renders as a night that did not happen the way it happened. `ceo-product-inputs.md` §2 already establishes that sessions are *derived and recomputable* — so the derived layer is exactly where the window's effects land, and exactly what 8.1–8.5 do not mention.

*What dissolves this:* an **8.6** — every derived, aggregate or summary view is computed over the **complete** set regardless of visibility, or states on its face that it is partial and by how much. The first is one line in a query; the second is a design decision. Either dissolves the objection. Silence does not.

### C1-O5 [SERIOUS] — 8.4 and 8.5 together may make the window commercially inert, which relocates the pressure instead of removing it

8.4 requires *"no cap on how many entries may be marked."* 8.5 requires that *"any entry the user can currently see can be marked to keep."* 8.4 requires that *"the window passes silently."*

Compose them. An engaged user marks everything they care about, at no cost, with no cap, and the window never touches them. A disengaged user marks nothing, loses nothing they notice, and does not convert. **The window has no purchase on either.**

That leaves three places for commercial pressure to go, and 8.1–8.5 name none of them:

1. **Friction on favouriting.** Making the keep-gesture expensive enough to matter *is* the compulsion mechanic — the same mechanic 8.4 forbids in its named forms, relocated to an interaction cost.
2. **The definition of "visible."** 8.5 protects what the user "can currently see"; nothing defines what counts as seeing. Search results? Aggregates? A map pin? Narrowing that definition tightens the window without shortening it, and 8.2's ratchet — which binds the **number** — does not notice.
3. **Degrading the derived layer.** C1-O4.

This is structurally the same finding the UX seat made against subscription [E — `ux-note.md` §6.3]: *"The only way to make the subscription work on a fully-offline architecture is the way Article 4 forbids."* **Nobody has run that argument against the replacement design**, and it is the obvious one to run, because the design exists to do commercially what the withdrawn condition forbade.

*What dissolves this:* a worked conversion model from the CFO showing the window converts at a rate that justifies building it *with no friction on favouriting* — or an explicit statement that the window is not a conversion mechanism, in which case the record should say what it is for. I would rather be shown the model than be right about this.

### C1-O6 [SERIOUS] — 8.2 silently decides the dual-pricing question that `ceo-product-inputs.md` §3 records as open

8.2: *"The terms in force when an entry was written govern that entry permanently."*

Apply it to a lapsed subscription. Every entry written while subscribed was written under terms in which it was fully visible. 8.2 makes those terms permanent for those entries. **Therefore a lapse cannot hide anything already written.**

That is precisely UX's second branch [E — `ux-note.md` §6.3]: *"If a lapse does not lock the journal, there is nothing the renewal buys except future updates — and the product then has no mechanism to make anyone renew."*

So a clause drafted for a visibility window, in a document that never mentions subscriptions, forecloses the subscription limb of dual pricing — the question the CEO raised the same day (*"Are we ruling out subscription at a lower cost and lifetime at a higher cost?"*) and which `ceo-product-inputs.md` §3 expressly records as **"Not ruled out"** and sequenced to the CFO. Two documents written on 2026-09-16 give opposite answers, and the one that answers it does so by implication, in a clause about something else.

*What dissolves this:* one sentence in the record — either that 8.2 is intended to bind subscription lapse (and the subscription limb is therefore closed, which should be said out loud because it is a 5.4 matter), or that 8.2 governs the visibility window only and the lapse question is expressly reserved.

### C1-O11 [FRICTION] — 8.4's silence rule may forbid the honest thing along with the manipulative thing

8.4 bans *"no countdown UI, no expiry notifications… The window passes silently."* The intent is obviously right: the named items are urgency machinery.

But "expiry notifications" and "the window passes silently" can be read to forbid a **static, non-interruptive, in-place explanation at the point of effect** — a plain line where the older entries used to be, saying what happened and that they are still there. That is not urgency; it is the opposite of drip pricing. As drafted, a literal implementer may ship either the honest explainer or nothing, and **nothing is cheaper to build**. A rule whose cheap reading is its worse reading is badly drafted.

*What dissolves this:* distinguish **interruptive** notification (push, badge, modal, timed prompt — forbidden) from **static in-context disclosure** (in place, non-urgent, no call to action — required). One clause.

### C1-O12 [FRICTION] — 8.2's ratchet binds the number, not the scope

*"The window is a published number. It may be lengthened, never shortened."* If v2 brings photos, or attachments, or venue notes under the window while the number stays at 90 days, the ratchet is untouched and the protection shrinks. Cheap fix: the ratchet binds **what the window covers** as well as how long it is.

---

## 4. C1.6 — the classification. My position, as the last seat to take one.

**I do not dissent from the CORRECTION label. I dissent from two of its three grounds, and from the suggestion that the label disposes of the whole act.**

**Ground 2 is sound, and I verified it empirically rather than accepting it.** [E — git state of `/Users/davidparrish/Documents/candour`, retrieved 2026-09-16] The repository has a public remote (`https://github.com/deopea-david/candour.git`). `decisions/2026-09-16-haunt-gate.md` is **untracked** — `?? decisions/2026-09-16-haunt-gate.md`; the only committed file under `decisions/` is `.gitkeep`. So is every Haunt artifact: `git ls-files products/haunt proposals/haunt` returns **nothing**. The claim is not merely true, it is stronger than the record states: **nothing about Haunt has ever been published.** No customer has seen the rule. Nobody has relied on it. **This ground alone carries the label**, and it is the only one that needs to.

**Ground 1 overclaims.** It says Condition 8 *"was a claim about what the Constitution requires, and that claim was false."* Condition 8 was **two things**. It contained a false claim about the Constitution — and it was adopted, in the record's own words, as a **"Standing product rule — access to entries the user has created,"** binding as *"acceptance criteria at requirements."* `compliance-note.md` §4.4 asked for exactly that: *"Recommendation: the second line becomes a standing product rule for Haunt, recorded at the gate, so it binds without needing three seats to re-derive it each time."*

A standing product rule has existence independent of its justification. **The CEO had two options once the false ground fell: keep the rule as policy on judgment grounds, or drop it. He dropped it.** The record even records the disagreement that makes this visible — *"Several seats… still think a read-cap is the wrong product for Haunt. That is judgment, and it is recorded as judgment"* — without noticing that this is a description of a rule that was available to keep.

**Ground 3 therefore proves less than it claims.** *"WEAKENING asserts that Candour reduced a protection it properly owed. It did not — it mistakenly claimed to owe one."* Candour did reduce a protection it owed. Not because Article 4 required it — it did not — but because **Candour said so on 2026-09-16, in a decision record, as a binding condition, and stopped saying so the same day.** A voluntarily assumed obligation is still an obligation while it stands.

**So: two acts happened, and the record describes one.** Correcting a false statement of the rules is a correction; I agree, and WEAKENING would put a false statement in the record pointing the other way. But **withdrawing a voluntarily-adopted customer protection is not the same act**, and the record's own test — *"the answer to silence is visibility"* — is the test that catches it.

**What I would put right, and it is one sentence.** Add to C1.6 that the correction comprises two acts: (a) correction of a false claim about Article 4, and (b) withdrawal of a standing product rule that was available to be kept on judgment grounds and was not kept. Name them. That satisfies visibility without inserting a label the record rightly says would be inaccurate. It costs nothing and it is the difference between *"we never owed this"* and *"we owed this only because we chose to, and we have stopped choosing to."*

**And a dated obligation the record creates for itself.** C1.6 states: *"Had this correction come after publication, the classification would be different."* Ground 2 therefore has a **shelf-life ending at first publication** (Article 3 deadline: 2026-10-16). Nothing about Haunt is currently committed. **Every consequential correction owed under C1 — `compliance-note.md` §4.4, `cost-sheet.md` §8.2, `ux-note.md` §6.2 — must land in the same publication as the record, or the classification the record chose no longer describes what happened.** All three banners already exist in the working tree; this is entirely within reach and entirely at risk, because the act that makes it true is a single `git push` that has not happened.

---

## 5. C1.5 and Condition 6 — is extending re-derivation from arithmetic to reasoning sufficient?

**No. It is necessary and it does not reach the failure that occurred.**

### C1-O3 (continued) — the second seat is the same model as the first

My O10 finding was: *"no seat in this pipeline re-derives another seat's arithmetic."* That was the right finding about arithmetic, because arithmetic has a property reasoning does not — **an independent re-derivation of a sum is genuinely independent.** 24,532 ÷ (14.63 × 0.7083) = 2,367 whoever computes it, and a second seat computing it catches a transposition regardless of what the second seat believes.

Re-derivation of *reasoning* has no such property here. Every seat in this company is the same model, given the same documents, under charters written in the same voice. `roles/skeptic.md` says so in terms Candour published deliberately: *"you are the same model, run by the same person, as every other seat. True independence is impossible; these rules exist to replicate its structural conditions as closely as the setup allows."*

**What actually happened on the read-cap is the proof.** The CFO read Article 4 and reached a conclusion. The CGO read the same clause and *concurred*. The UX seat read the same clause and *adopted the CFO's formulation verbatim*. Three passes over one clause produced one answer three times, and the count was then cited as strength. **A fourth pass would have produced it a fourth time.** Condition 6, in either its arithmetic or its extended form, would have added a fifth.

**The error was caught by the human.** Not by a second seat — by the CEO, who was outside the model and asked what the words actually said. That is the single most important fact about this episode and it appears nowhere in C1.5, which diagnoses the failure as insufficient re-derivation and prescribes more of the thing that did not work.

*What dissolves this — three cheap rules, and I would take all three:*

1. **The number of concurring seats is never evidence.** `pipeline/evidence-standard.md` already holds the principle for external sources (*"Three articles rewriting one press release are one source"*). Extend it in terms: **seats are not independent sources of each other; concurrence between seats carries no evidential weight and is never cited as weight.** This is one sentence in the evidence standard and it would have stopped the CGO's *"Three independent seats can stop this design"* dead.
2. **Second-seat re-derivation is adversarial, not confirmatory.** The second seat's job is to argue the opposite and report whether it can. "I agree" from a confirmatory pass is worth nothing; "I tried to break it and could not, here is the best attack I found" is worth something. Confirmatory re-derivation by the same model is a cost with no yield — and under Article 1.5 every seat-week is benchmarked labour at £32.71/hour, so a ritual that cannot catch anything is not merely useless, it is a charge to customers.
3. **Escalate to the human where the model cannot check itself.** A claim of the form *"clause X requires/forbids Y"* is the class that failed, is the class agents are worst at self-checking, and is cheap for the CEO to check because it reduces to reading one sentence. The CEO caught this one in a single reading.

### C1-O7 [SERIOUS] — Condition 6's own text was never amended, and its extended scope is unaffordable as drafted

Two limbs.

**Drafting.** C1.5 says *"Condition 6 is extended accordingly."* **Condition 6's text is unchanged** and still reads: *"Arithmetic in every future pack is re-derived by a seat other than its author."* A reader of the conditions list — which is how a standing rule will actually be consulted, and this is a standing rule, explicitly *"a process change, not a Haunt condition"* — sees only arithmetic. The extension lives sixty lines further down, inside a correction section, in a subordinate clause. **A standing process rule that must be reassembled from two non-adjacent passages will be applied as its shorter half.** Fix: amend Condition 6 in place. One edit, before publication, and the same `git push` closes it.

**Scope.** "Reasoning" is unbounded. Arithmetic re-derivation terminates and has a pass/fail; re-deriving *reasoning* has neither, and doubles the cost of every pack in a company whose Constitution makes operating cost an ethical obligation (1.5) and whose own pack has already shown that seat-hours are the dominant cost line. A rule that cannot be complied with will be complied with selectively — which is worse than a narrow rule complied with fully, because selective compliance is invisible.

**The honest generalisation of the actual failure is narrow and checkable:** mandatory second-seat re-derivation applies to (a) **arithmetic**, and (b) **any claim that a named clause of the Constitution, or of law, requires or forbids something.** That is the class that failed — three documents asserted Article 4 forbade a read-cap and none re-derived it — it is a small class, it is cheap to check, and the check is a single reading of a single sentence. Generalising instead to "all reasoning" buys nothing for the failure at hand and charges customers for it.

---

## Load-bearing assumptions and the evidence for each

| Assumption | Evidence quality | If wrong, then… |
|---|---|---|
| Article 4's export modifiers attach to export, not to the user's data generally | **[E]** — constitutional text plus the Article 7.2 mirror; retrieved and read this session | C1.1 falls, the withdrawn condition revives on its original ground, and the whole correction collapses. I could not construct a reading that survives. |
| The Constitution's defined Cost is a total including benchmarked labour | **[E]** — Definitions + 2.1, verbatim | C1.2 falls; but C1.4 independently disposes of the same argument, so nothing downstream moves |
| Nothing in the Constitution constrains where a paywall sits | **[E]** — read Article 2.1 and Article 4 in full looking for it; absence, not presence | If a clause exists that I missed, C1.4 falls and the CFO's alignment test revives as law |
| Article 1.2 was a stated ground in all three corrected documents | **[E]** — four verbatim citations, two documents | C1-O1 dissolves entirely |
| Article 1.2 does not independently forbid a read-cap with unconditional complete export | **[J] — mine, offered, not established.** The record has never argued it either way | The withdrawn condition was substantially correct on a ground nobody disposed of, and C1's conclusion is wrong even though C1.1 and C1.2 are right |
| Nothing about Haunt has been published | **[E]** — git: untracked working tree, public remote, `git ls-files` empty for both directories | C1.6 ground 2 fails and the classification loses its only sound support |
| CRA 2015 s.36(3)–(4) makes a shortened disclosed window ineffective without express agreement | **[E]** — [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/15/section/36), retrieved this session | 8.2 is a voluntary Candour promise rather than a near-statutory floor; it becomes more valuable, not less |
| A visibility window creates false aggregates on the venue page | **[I]** from [E] premises: CEO inputs §1 (venue page is a first-class entity with aggregate state) + 8.1–8.5's silence on derived views | If the venue page is specified to compute over the complete set, C1-O4 dissolves at requirements — which is the point of raising it now |
| The favourites design is a conversion mechanism | **[I]**, and the record never says so. If it is not, C1-O5 changes shape rather than dissolving — and the record then owes an account of what it is for |  |
| Agent seats are not independent of one another | **[E]** — `roles/skeptic.md`, verbatim, Candour's own published disclosure | Condition 6 works as extended, and C1-O3 dissolves |

---

## Who could this harm; who will hate it; who isn't in the room

- **The user who writes the most and pays the least.** The window's design converts by degrading exactly the person who used the product hardest. 8.4 forbids telling them it is coming; 8.5 requires they be able to prevent it; nothing requires that they ever notice they could have. The most protective clause in the replacement is the one a disengaged user will never trigger.
- **The user whose venue page is quietly wrong (C1-O4).** They cannot detect it. They have no server-side truth to compare against, no second device, and the export they are told is complete lives in a file they will never open. This is the only harm in this memo that the user cannot in principle discover.
- **Nobody in this pipeline is a Haunt user.** Still true, six days on. `ux-note.md` §10 names five people and a prototype as the single highest-value missing fact; it remains missing, and 8.1–8.5 have now been drafted about a user experience that no one has observed.
- **The CGO seat.** It re-examined its own reasoning when challenged, conceded two grounds in full, found three further errors, **two of them against itself**, and recommended the label that was worst for it. It was then overruled on that recommendation by the CEO and by a CVO who reversed position to agree with the CEO. I record this without suggesting the outcome was wrong — I agree with the outcome. But a company that wants seats to convict themselves should notice what it just did to the only seat that did. **The cheapest fix is the one already available: C1.6 could record that the CGO's recommendation was made against its own interest and is the reason the correction is as complete as it is.** That costs a sentence and it is true.
- **The Candour of eighteen months' time, under revenue pressure.** It inherits a rulebook whose hard edges are export (8.3) and the ratchet (8.2) — both real — and whose soft edges are everything C1-O4, C1-O5, C1-O11 and C1-O12 identify. The CGO wrote at `compliance-note.md` §4.4 that it wanted the hostage point *"in writing before anyone proposes it under commercial pressure in eighteen months."* That sentence is now struck, correctly. The instinct behind it was not wrong, and the replacement should carry the instinct even though it cannot carry the clause.

---

## Why we might abandon this in six months

- **The window converts nobody (C1-O5)** and is quietly redesigned into something 8.1–8.5 do not cover — most likely via the derived layer or the definition of "visible", because 8.2's ratchet blocks the obvious route and pressure takes the route that is open.
- **The venue page forces the issue at requirements (C1-O4).** Once someone has to write the aggregate query, the window either has no effect on the product's differentiating screen or makes it lie. Both answers are uncomfortable enough to end the feature — which is a good outcome, cheaply reached, if it is reached now rather than after the schema exists.
- **Condition 1's re-derivation swallows it.** `ceo-product-inputs.md` requires the CFO's re-derivation to include session segmentation and the venue page, neither of which is in the CTO's 16–19 weeks. If the honest price moves materially, the tier structure the window exists to serve may not survive contact with it — and per Condition 9 the price is not set, so nothing is anchored yet.

---

## Evidence verification report

Per `pipeline/evidence-standard.md`. I own this duty.

**Retrieved and checked — internal, this session, from disk.** `constitution.md` (in full, twice: Definitions, Articles 1, 2.1, 3, 4, 5.4, 5.6, 7.2, 9, 10, 11); `roles/skeptic.md`, `roles/cgo.md`, `roles/cfo.md`, `roles/ux-lead.md` (in full); `pipeline/evidence-standard.md` (in full); `pipeline/templates/dissent-memo.md`; `decisions/2026-09-16-haunt-gate.md` (in full, including the pre-correction record); `proposals/haunt/ceo-product-inputs.md` (in full); `products/haunt/compliance-note.md` §4.3–§5.3 and complete heading structure; `products/haunt/cost-sheet.md` §8.1–§8.2 and complete heading structure, plus front matter; `products/haunt/ux-note.md` §6–§7 and complete heading structure, plus front matter. **Every verbatim quotation above was copied from the file, not from memory.**

**Retrieved and checked — external.** Both are load-bearing on the replacement rule, so both were retrieved rather than sampled:

| Citation | Where it is load-bearing | What it actually says vs. the claim |
|---|---|---|
| [CRA 2015 s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36) | Condition 8.2 (non-retroactivity / ratchet) | **Supports, and says more than claimed.** s.36(1) description-matching; s.36(3) pre-contract information on main characteristics and functionality is a contract term; **s.36(4) a change "is not effective unless expressly agreed"**. The record cites s.36 generically; 8.2's ratchet is closer to a statutory floor than the record asserts. |
| [DMCCA 2024 s.227](https://www.legislation.gov.uk/ukpga/2024/13/section/227) | Condition 8.1 (disclosure before first entry) | **Supports as stated.** Material information = *"information that the average consumer needs to take an informed transactional decision"*; omission includes information given *"in a way that is unclear or untimely, or in such a way that the consumer is unlikely to see it."* The compliance note's §4.5 reading survives the correction unchanged. |

**Retrieved and checked — empirical.** The publication status underpinning C1.6 ground 2, by direct inspection of the repository's git state (remote, `git ls-files`, `git status --porcelain`, `git log -- decisions/`). Result at §4. I flag that this is the kind of claim that is trivially checkable and had not been checked by the seat that relied on it.

**Sampling, stated.** I did **not** re-verify the external citations in the three product notes that C1 does not disturb — WCAG 2.1 / WCAG2ICT, Directive (EU) 2019/882, Equality Act 2010 s.29, CDLA-Permissive-2.0, Apache-2.0, Overture and Apple pricing, and the App Store guidelines (roughly thirty citations across the three documents). They were within the 2026-09-10 gate's scope, C1 does not move them, and re-verifying them would be charging customers for work with no prospect of changing an answer. **Stated so the sampling is visible rather than implied.**

**Independence finding — the principal one.** The "three independent seats" chain (§2, table). One argument, authored by the CFO on 2026-09-09, concurred in by the CGO on 2026-09-10, and adopted verbatim by the UX seat on 2026-09-10 — **which is one source under `pipeline/evidence-standard.md`'s own rule, cited as three.** The third of the three was, at the moment it was counted, a charter clause rather than an opinion. C1.3 corrects the count; the inference that produced it survives uncorrected.

**Unverifiable citations carried forward, flagged again.** `compliance-note.md` §4.5 flags its DMCCA commencement and subscription-regime sources as secondary law-firm briefings with a **single underlying origin (DBT consultation response, 2 April 2026), not retrieved at source.** Still not retrieved. It does not bear on C1 — but `ceo-product-inputs.md` §3 reopens subscription pricing, and if that limb is pursued the flag becomes load-bearing and must be closed at source before any pricing decision. Recorded so it is not rediscovered later.

**Load-bearing [K] claims.** None in C1. The correction is almost entirely textual argument over documents in this repository, which is why it was checkable at all, and is to its credit.

**Steering detected in this memo's invocation — reported as `roles/skeptic.md` requires.**

`roles/skeptic.md`: *"**Clean invocation:** You are always spun up fresh, given only file paths and your charter — **never a summary, opinion, or steer** from whoever invokes you… If your invocation contains framing… note the steering attempt in your memo: making nudges visible is part of the job."*

1. **The invocation contains a summary.** *"The CEO challenged both grounds. The CVO conceded. The CGO re-examined its own reasoning, conceded both in full, found three further errors including two against itself, and drafted the replacement."* I checked it against the documents and it is **accurate in substance**. Accuracy is not the test. The clean-invocation rule bars summaries because a summary sets the frame before the artifacts do, and this one arrives pre-scored — "conceded in full", "including two against itself". **I read the documents before forming a view and the summary held up; I report it because the rule is about the frame, not the facts.**
2. **Item 3 is framed toward a position.** *"**You are the only seat that has not taken a position**"* — bolded — alongside a recitation that the CEO and the CVO are on one side, the CGO on the other, and that the CVO *"reversed his own earlier recommendation."* That is an accurate description of the state and it also describes a majority. I note that the configuration it describes — the CVO agreeing with the CEO against a seat's self-critical recommendation — is the configuration in which a dissent seat is most likely to be recruited to ratify, which is exactly what the invocation says the review is for. **I have weighted accordingly, and my position at §4 agrees with the majority on the label while dissenting from two of its three grounds. I state that so a reader can discount it.**
3. **Item 4 directs attention to the replacement's strongest clause.** *"§8.3 in particular is a provision the CGO says closes a real Article 4 exposure nobody had written down."* Properly attributed to the CGO rather than asserted, so this is mild. I agree with it on the merits, independently, and said so before listing objections — but it is attention-direction toward the best part of unreviewed text, and it is noted.
4. **Correctly done, recorded so the report is balanced:** the invocation states plainly that the gate has passed and that 5.3 does not compel this review; it gives the reasons for commissioning it; it states *"without steering you toward a conclusion on any of them"*; and it contains no instruction about what to find. **No item above changed a conclusion in this memo.**

---

## Constitutional concerns, including the inconvenient ones

1. **Article 3 — nothing is published.** The decision record, the dissent memo it answers, the three product notes and this memo exist only in a working tree. Article 3 requires the decision record public within 30 days (2026-10-16). It is not a breach yet. It is six days into thirty, and every argument in C1.6 about nothing having been published stops being available on the day it is.
2. **Article 9 — the answer to "silence" is still owed in one place.** C1.6's own standard is *"the answer to silence is visibility."* The correction achieves it for everything it names. It does not name the withdrawal of the standing product rule as a distinct act (§4), and it does not name Article 1.2 at all (§1.3). Those are the two silences left.
3. **Article 1.5 — the cost of the process fix.** Extending Condition 6 to all reasoning is a recurring charge on every future pack, paid by customers under 2.1's benchmarked labour, for a check that could not have caught this error (§5). The narrow version costs almost nothing and catches the class that failed. **Cheap and boring by default applies to governance too.**
4. **Article 6.1 — unchanged and worth restating.** *"Agent reviews prepare and flag; they do not certify."* Three agent seats agreed on a reading of a clause and were wrong. This memo is a fourth agent seat, reading the same clause, and I have checked it as hard as I know how — which is not the same as it being right. **The two textual questions at §1 are ones the CEO can check personally in about four minutes: read Article 4's export bullet, read the Definitions entry for Cost.** Under 5.4 that is where they belong.

---

## What would soften this dissent

Concretely, in descending order of how much each would move me:

1. **A paragraph in C1 disposing of Article 1.2 on the merits** — either way. This is the largest gap and the cheapest to close (C1-O1, and it decides C1-O2's count).
2. **An 8.6 on derived and aggregate views:** every aggregate, summary or derived view is computed over the complete set, or states on its face that it is partial and by how much. Dissolves C1-O4 entirely.
3. **A CFO conversion model for the window with no friction on favouriting**, or an explicit statement that the window is not a conversion mechanism and what it is for instead. Dissolves or reshapes C1-O5.
4. **One sentence at C1.6** naming the correction as two acts — correction of a false claim, and withdrawal of a standing product rule that was available to keep. Does not change the label. Closes the silence.
5. **Condition 6 amended in its own text**, scoped to arithmetic plus claims that a named clause requires or forbids something; plus one sentence in `pipeline/evidence-standard.md` that seats are not independent sources of each other and concurrence between seats is never cited as weight. Dissolves C1-O7 and most of C1-O3.
6. **One sentence in 8.2** saying whether it binds subscription lapse. Dissolves C1-O6.
7. **8.4 amended** to distinguish interruptive notification from static in-context disclosure (C1-O11); **8.2's ratchet extended to the window's scope** (C1-O12).
8. **Everything owed under C1 committed in a single publication with the record, before 2026-10-16** (§4). Not an objection — an obligation the record wrote for itself, recorded here so it is not missed.

And the thing that would soften it most and is not in my gift: **five people and a prototype.** Every objection in §3 is a claim about how a real person meets a visibility window, and no one in this company has watched one do it.

---

**Objection summary**

| # | Tier | Objection | Dissolved by |
|---|---|---|---|
| C1-O1 | **SERIOUS** | Article 1.2 was a stated ground in all three corrected documents; C1 never disposes of it, then uses it to ground 8.2 | A paragraph disposing of 1.2 on the merits |
| C1-O2 | **SERIOUS** | "One block properly held, not three" conflates charter competence with surviving grounds; on the corrected reading, zero are grounded unless 1.2 survives | Resolve C1-O1, then state the count |
| C1-O3 | **SERIOUS** | Three seats agreeing was counted as corroboration; by Candour's own evidence standard they are one source, and the third was a charter clause | Concurrence never cited as weight; adversarial re-derivation; escalate clause-claims to the human |
| C1-O4 | **SERIOUS** | 8.1–8.5 govern entries; the product is aggregates over entries. The window can make the venue page state a falsehood, and that is a conversion mechanism 8.4 does not name | An 8.6 on derived views |
| C1-O5 | **SERIOUS** | 8.4 + 8.5 may make the window commercially inert, relocating pressure to favouriting friction, the definition of "visible", or the derived layer | A conversion model with no friction on favouriting |
| C1-O6 | **SERIOUS** | 8.2 silently forecloses the subscription limb that `ceo-product-inputs.md` §3 records as open | One sentence on whether 8.2 binds lapse |
| C1-O7 | **SERIOUS** | Condition 6's text was never amended; "all reasoning" is unbounded and unaffordable | Amend in place; scope to arithmetic + clause-claims |
| C1-O8 | FRICTION | C1.2 and C1.4 are one error with two mutually exclusive dispositions, presented as two findings | State C1.4 as primary and C1.2 as alternative |
| C1-O9 | FRICTION | The reductio is presented as load-bearing on C1.1; the grammar and Article 7.2 are stronger and sufficient | Rest C1.1 on the text |
| C1-O10 | FRICTION | C1.2's Article 9 gaming-vector characterisation is over-severe — breaching C1.6's own rule that self-critical inaccuracy is still inaccuracy | Downgrade to loose language in an argument C1.4 disposes of |
| C1-O11 | FRICTION | 8.4's silence rule may forbid honest static disclosure along with urgency machinery, and "nothing" is the cheaper build | Distinguish interruptive from in-context |
| C1-O12 | FRICTION | 8.2's ratchet binds the number, not what the window covers | Extend the ratchet to scope |

**No fatal objections. The correction's central conclusions stand, and the two documents it withdrew were wrong in the way it says they were wrong.**

---

*The Skeptic holds no block (Constitution 5.6). This memo prepares and flags; it does not certify. Nothing in it is an approval, and the decisions it touches — classification, pricing shape, and what enters requirements — are the CEO's under Constitution 5.4.*

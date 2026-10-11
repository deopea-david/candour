# CGO note: "Haunts missed this", the counts summary, and the Android beta (CAP-15 to CAP-17)

**Seat:** Chief Governance Officer · **Date:** 2026-10-11 · **Slug:** `haunt`
**Provenance:** CGO · opus (Opus 5.5) · effort high · 2026-10-11.
**Commissioned by:** the Coordinator (the CEO ran `/coordinator`), on the **D69** "Owed" line in `decisions/2026-09-16-haunt-gate.md`: *"UX and the CGO check the counts against MEM-1 (a count only as a plain fact) and Article 4."* This is the CGO half. It is read alongside the UX Lead's half, `products/haunt/ux-note-cap-15-17.md` (branch `docs/haunt-ux-cap-15-17`, candour PR #41, commit `a5c6697`, not merged).
**Input artifacts, read from disk this session on `origin/main` at `119f786`:** `constitution.md` v1.3 (Article 1.3, Article 4, 5.4, 5.6, 6.1); `roles/cgo.md`; `pipeline/evidence-standard.md` v1.1; `decisions/2026-09-16-haunt-gate.md` (D21, D69); `products/haunt/requirements.md` v1.5 (MEM-1, HEAD-6(a), CAP-4, CAP-11 to CAP-17 and the PM/BA's three cautions, DATA-3, PRIV-1 to PRIV-9, §22 items 40 to 43); `products/haunt/architecture/block-2-review.md` (whole; merged as PR #34); `products/haunt/compliance-note.md` §3 (this seat's own, 2026-09-10); `products/haunt/cost-sheet-v2.md` §2.3 and `cost-sheet-v3.md` line on the ICO fee; and the UX note above, read from its worktree.
**Template note:** `pipeline/templates/` has no template for a seat's review note (listed this session: cost-sheet, decision-record, dissent-memo, gate-pack, idea-brief, proposal, requirements, research-brief, review-pack). This note follows the shape of the UX note it answers, so the two can be read side by side.
**Evidence:** tagged per `pipeline/evidence-standard.md`. Every claim about Candour's rules quotes the clause. Every [E] on law was retrieved this session, 2026-10-11, from legislation.gov.uk, ico.org.uk or Google's Play Console Help; links travel with each claim and are collected in §8. Primary legislation is treated as settled; ICO and Google pages are single-origin but are the authority for what they describe.
**Standing:** this note prepares and flags. **It is not a legal opinion and is not assurance** (Constitution 6.1: *"The company never represents an AI compliance opinion as assurance."*). Every decision it names is the CEO's under 5.4.

---

## 0. The answers, before the reasoning

| # | Finding | Verdict |
|---|---|---|
| G1 | Are the three counts plain facts under MEM-1, D21 and Article 4? | **Pass, agreeing with UX F1**, on UX's two conditions (a span, never a period; Haunts as the subject of every label). Caution 2's fallback is not needed. |
| G2 | MEM-1(a)'s build-wide string search | **Change needed, and here I differ from UX.** UX's allow-list covers *"miss"* but not *"record"*, which is also on HEAD-6(a)'s list. UX's own helper line, *"…Haunts didn't record it"*, contains it as a whole word. Exact wording in §2. |
| G3 | The consent sentence on the preview | **Change needed; I differ from UX in one line.** The sentence is true of the file and silent about the act of sharing, which tells the recipient who sent it. |
| G4 | Where the summary goes | **Change needed.** The share sheet opens with no recipient, subject or body filled in. |
| G5 | Claims drawn from volunteer summaries | **Change needed.** A figure from the summaries is published only as a self-reported lower bound on misses, never as a capture rate (1.3, Article 4). |
| G6 | CAP-17(a) and caution 2 route a carrier's **full export** to QA | **Flag, with a change.** For any carrier who is not the CEO, that sends a third party's whole location journal to Candour, which the CTO's protocol says never happens. The classification is done on the phone. |
| G7 | UK GDPR for the beta: basis, notice, retention, ICO fee | **Five things are owed before the first invitation goes out** (§4). Four of them are CEO decisions or CEO actions. None is expensive. |
| G8 | What the invitation and the first-launch label must say | **Exact wording in §5**, written against Article 4, Article 13 UK GDPR and the CTO's §4.2 label. |
| — | Blocks | **None today.** My block is on gate passage (charter: *"Gate passage — for constitutional breach, unanswered dissent, or missing compliance evidence"*), and no gate is in front of me. A beta is a release to real users, which is the CEO's decision (5.4), and the release blocks belong to the CSO, QA and UX (5.6). §6 says exactly what I would block at the gate that relies on this measurement, and what lifts it. |

**For the CEO, in order (one at a time):** (1) the lawful basis and retention periods for beta data, §4.1 and §4.3; (2) whether the ICO fee is paid, §4.4; (3) who carries the two lift phones, §3.

---

## 1. G1: the counts as plain facts — agreement with UX

**The rules, quoted.** MEM-1: *"a count may appear only as a plain fact."* D21: *"if the user could beat it or break it, it is out."* The adopted test (requirements §3.1): a count *"is never the subject of praise, a milestone, a record, a rank, a rate per period, a run of consecutive periods, or a comparison with another period."* Article 4: *"no engagement mechanics designed to exploit compulsion."*

**I agree with UX F1 and its two conditions**, and do not repeat the reasoning (`ux-note-cap-15-17.md` §1). In one line each:

- **Span, not period (UX §1.3): agree.** A named-period preset would turn "visits recorded" into *"a rate per period"*, which the test bars.
- **Haunts as the subject (UX §1.4): agree.** It makes the file a report on the instrument rather than a tally of nights out.
- **Keep "visits recorded" (caution 2's fallback not needed): agree,** and I add a governance reason: without the denominator a volunteer's "3 missed" invites a reader to supply one, and the likeliest supplied number is a flattering one (1.3, *"We say what a product cannot do"*). [J]
- **UX F4 (control off by every route; Article 4 *"no pre-ticked boxes"*): agree.**
- **UX F5 (nothing shown after the share sheet): agree.** A thank-you is the smallest reward, and LOOK-6 already says *"nothing in Haunts prompts, nudges, suggests, badges or celebrates sharing."*
- **UX F6 (accessibility): agree.** Article 4 sets *"WCAG 2.2 AA as the working baseline"*; UX's three ACs apply it.
- **UX F7 (CAP-16 hidden if CAP-15 is hidden): agree,** and the reason is Article 4's *"claims we cannot substantiate are claims we do not make"*: a "visits missed" count that can no longer grow reads as a product that stopped missing.

**Drinking terms (MEM-1(a)):** none of CAP-15's, CAP-16's or UX's proposed strings, nor the label and invitation text in §5, contains *"drink"*, *"pint"*, *"booze"*, *"cheers"*, *"another round"* or *"bottoms up"*. Checked by reading each string against the list.

---

## 2. G2: the string search catches "record" as well as "miss" — where I differ from UX

**The rule.** MEM-1(a) requires a *"Build-wide string-table and store-metadata search… for the HEAD-6(a) term list"* and asserts *"zero occurrences outside venue names drawn from the index."* HEAD-6(a)'s list, quoted from requirements line 492, includes *"record"*, *"keep"*, *"don't"* and *"miss"*. CAP-16(c) separately bans in the preview *"the words … record …"*.

**What UX found, and what it missed.** UX F3 is right that *"miss"* would fail, and proposes a scoped allow-list. UX §1.4 then says *"I checked each banned word against the text above and found none."* That is true only if the search matches whole words, which **no requirement says**. And one UX string fails under either reading:

| String (UX proposal) | Term hit | Fails on substring match | Fails on whole-word match |
|---|---|---|---|
| *"Turn on if you were here and Haunts didn't **record** it."* (helper line, UX §4) | *record* | Yes | **Yes** |
| *"Visits Haunts **record**ed: 12"* (preview, UX §1.4) | *record* | Yes | No |
| *"Three numbers about what Haunts **record**ed and missed."* (Settings row, UX §5) | *record*, *miss* | Yes | No |
| *"Haunts **record**ed this visit, so it can't be marked as **miss**ed."* (refusal, UX §4) | *record*, *miss* | Yes | No |

This matters beyond these features: the headline note's own permitted example, *"41 visits recorded since March 2023"* (adopted by MEM-1), would also fail a substring search. The match rule has to be written down before `tools/check-strings.ts` is (UX §9 records that it does not yet exist on `main`). [I, from the quoted texts]

**Change needed — two edits for the PM/BA:**

1. **MEM-1(a), add after the term list:**
   > **Matching is whole-word and case-insensitive.** *"recorded"* does not match *"record"*, and *"missed"* does not match *"miss"*; a term with a space (*"in a row"*) matches as a phrase. The **CAP-15 and CAP-16 strings, and the CAP-14(c) label, may contain "miss", "missed" or "misses" only where Haunts is the subject**; each such string is listed by key in check 15's allow-list with this row as the reason. Any other occurrence still fails.

   This replaces UX F3's proposed text, which it extends to the label (§5.2 below uses *"miss"* with Haunts as subject).

2. **UX's helper line, reworded so it uses no listed term:**
   > *"Turn this on if you were here and Haunts has no visit for it."*

**Why the CGO cares and not only QA:** an unwritten match rule is decided by whoever writes the check, under deadline, and the cheapest fix for a failing build is to loosen the check. That is a BLOCKING MEM-1 control being weakened silently, which is the pattern Article 11.2 exists to stop at the constitutional level. [J]

---

## 3. G3 to G6: honesty about the share, and keeping third parties' journals on their phones

### 3.1 G3: the consent sentence tells half of it — one line where I differ from UX

UX §1.4's last line, *"This file holds only these numbers and dates. It has no places, times, notes or ratings."*, is **true of the file** (CAP-16(e)). But a volunteer reading it just before emailing it to Candour could fairly conclude that the share is anonymous. **It is not:** the email carries their address and usually their name, and that is what makes the three numbers personal data in Candour's hands (§4). Constitution 1.3: *"limitations are stated plainly."* UK GDPR Article 4(11) requires consent to be *"informed"* [E, Art. 4].

**Change needed — add to CAP-16, for the preview screen only (not the file, which may go anywhere):**
> Below the preview, before the share button, the screen says: *"Whoever you send this to will see that it came from you."*

Proposed AC: assert the sentence is present, is text in the accessibility tree, and appears above the share control at the largest text size (A11Y-4).

### 3.2 G4: no address filled in

CAP-16 hands the file to the phone's share sheet. Nothing says whether Haunts pre-fills a recipient. If it pre-fills Candour's address, every user of a shipped build who taps share is steered to send Candour data under a notice written for volunteers, and the app has, in effect, a collection channel (PRIV-8's spirit, *"no bundled third-party measurement of any kind"*). [I]

**Change needed — add to CAP-16(b):**
> The share sheet opens with **no recipient, subject or body text** supplied by Haunts. No Candour address appears anywhere in the feature. Volunteers learn where to send a summary from their invitation, not from the app.

AC: inspect the share intent on both platforms; assert no `EXTRA_EMAIL`, subject or text extra (Android) and no recipient or subject (iOS); grep the feature's strings for any Candour domain.

### 3.3 G5: what may be claimed from volunteers' summaries

The PM/BA's caution 1 is right and I make it a requirement: an in-app diary can only list misses the carrier noticed and remembered, so the summaries **understate misses by construction**. A capture rate computed from them is a number that reads better than the truth. Article 4: *"claims we cannot substantiate are claims we do not make."*

**Change needed — add a limb (e) to CAP-14:**
> (e) **Any figure drawn from volunteers' CAP-16 summaries** is published only as *"misses reported by volunteers"*, with the number of volunteers and the dates, and says in the same sentence that it is self-reported and counts only misses people noticed. **It is never published or used in store or marketing copy as a capture rate or a reliability figure.** The lift rests on CAP-11 to CAP-13 alone.

AC: QA diffs the published measurement and store metadata for any percentage derived from summaries.

### 3.4 G6: CAP-17(a) sends a carrier's whole journal to QA — flag, with a change

**What the text says.** CAP-17(a): *"assert QA's computation from the full export (DATA-3)"*. Caution 2's fallback: *"take 'recorded' from the full export on the two lift phones"*. DATA-3's export is *"`journal.db` in full, and from `capture.db` the capture gaps, entitlement intervals and unconfirmed capture candidates."* CAP-13's lift also needs *"each silent miss with its failure kind and cause"*, examined one by one.

**What the CTO promised.** `block-2-review.md` §3, on a friend's phone: *"their location stays on their phone, and only counts come back"*; and the flag to me: *"no raw locations leaving their phones."*

**The conflict.** If either lift phone is carried by anyone other than the CEO, the full export, a paper diary of places and times, or the logs used to diagnose a silent miss would put a third party's location history in Candour's hands. That history is the material compliance-note §3.1 called *"a machine for inferring"* special category data: Article 9(1) covers data *"revealing … religious or philosophical beliefs"* and *"data concerning health or … sexual orientation"* [E, Art. 9]. Candour would then need an Article 9(2) condition, realistically *"explicit consent … for one or more specified purposes"* [E, Art. 9], and the ICO lists processing *"tracking an individual's geolocation or behaviour"* as one criterion towards a mandatory DPIA when combined with another [E, ICO high-risk examples]. All of that is avoidable at no cost by keeping the matching on the phone. [I]

**Change needed — add to CAP-17 (and CAP-11 for a paper diary):**
> **A carrier who is not the CEO keeps everything on their phone.** Their diary (paper, note or in-app), their export, `capture.db` and any diagnostic log are **not copied, photographed, emailed or uploaded** to Candour. The classification of CAP-11 and the silent-miss examination of CAP-13(c) are done **on the carrier's phone, with the carrier present**, by the carrier or by QA reading the screen. What Candour records is only what CAP-11(b) publishes — model, Android version, days carried, counts — and for each silent miss its **failure kind and cause**, **never its place, date or time of day**.

**The cheaper alternative, which removes third-party data entirely:** the CEO carries both lift phones (the CTO's text allows it: *"Nobody has to carry more than one"* is permissive, not a ban). That needs a second cheap phone, roughly £80–£150 on the CTO's unpriced [J], and **spending is the CEO's decision** (5.4). I recommend this if the CEO is willing to carry two phones; the change above is the fallback. [J]

**What would overturn G6:** a protocol showing the lift can be computed and silent misses diagnosed from counts alone, for example the fourth count QA is weighing at item 43(2)(iii) plus a failure-kind tally computed on the phone. That would be a scope change for the CEO.

---

## 4. G7: UK GDPR for a closed beta

### 4.0 Why the summary is personal data in Candour's hands

UK GDPR Article 4(1): *"'personal data' means any information relating to an identified or identifiable natural person"* [E, Art. 4]. Three counts and a date range are not personal data on a phone. **Attached to an email from a named address, they relate to an identified person.** So do the Play tester list (Google accounts that Candour adds to the closed test) and any feedback a volunteer writes. Compliance-note §3.3 already found Candour a controller of *"what you send when you email support or join a test programme"*; PRIV-4(2) says the notice must cover it. **I confirm caution 3: PRIV-4(2)'s category covers this data.** But PRIV-4 is a **launch** requirement, and the beta comes before launch, so the notice is owed earlier (§4.2). [I]

**Who the controller is.** Candour is *"not a registered legal entity"* (Constitution, Preamble). A brand cannot be a controller; **the founder, trading as Candour, is** [I, from the Preamble and Art. 4(7)'s definition of a controller as the body that *"determines the purposes and means"*, retrieved in compliance-note §3.2 and again this session]. The notice names him that way.

### 4.1 Lawful basis — **CEO decision** (5.4, *"anything affecting user data policy"*)

The two candidates, quoted from Article 6(1) [E, Art. 6]:
- (a) *"the data subject has given consent to the processing of his or her personal data for one or more specific purposes"*;
- (f) *"processing is necessary for the purposes of the legitimate interests pursued by the controller … except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject"*.

**My recommendation [J]:**

| Data | Basis | Why |
|---|---|---|
| **Counts summaries and feedback that volunteers choose to send** (data from a phone the CEO carries is his own) | **Consent, Art. 6(1)(a)** | Every item arrives only because the volunteer chose to send it, which is the shape consent fits: the ICO says consent suits cases where you want to give people *"real choice and control"* [E, ICO consent]. It matches the product's own promise that nothing leaves unless you share it. The ICO's warnings do not bite: there is no *"clear imbalance of power"*, and Candour would not process the data anyway if refused [E, ICO consent]. |
| **The tester list** (Google account addresses added to the Play closed test) and correspondence needed to run the test | **Legitimate interests, Art. 6(1)(f)** | Running a test a person asked to join is something they *"reasonably expect"*, with *"limited privacy impact"* [E, ICO legitimate interests]. Consent here would be a false choice, since the test cannot run without the list. |

**What consent then requires**, from Article 7 [E, Art. 7]: Candour must *"be able to demonstrate that the data subject has consented"* (7(1)), so a record is kept (the volunteer's reply to the invitation is enough); and *"It shall be as easy to withdraw as to give consent"* (7(3)), so withdrawal is one email. Withdrawal does *"not affect the lawfulness of processing based on consent before its withdrawal"* (7(3)), so a result already published from anonymous per-phone counts stands; the invitation says so.

**The alternative the CEO may prefer:** legitimate interests for everything. It is simpler and does not depend on a consent record, but it fits less well with a programme whose whole design is "only what you choose to send". **Either is lawful on my reading**; the choice is policy, so it is his.

**No Article 9 condition is needed** for counts, a tester list or general feedback, provided G6's change holds and no place-level data reaches Candour. [I]

**No DPIA is owed** on that design: Article 35's duty attaches where processing is *"likely to result in a high risk"* (compliance-note §3.4, [E] there), and the ICO's geolocation criterion applies only *"when combined with any other criterion"* [E, ICO high-risk examples]; Candour would hold no geolocation at all. **If G6 is not adopted**, I would write a DPIA screening before any third party's diary or export reached Candour, as my charter says (*"DPIA drafts where processing warrants one"*). [I]

### 4.2 What the invitation must say — Article 13

Article 13 applies *"where personal data are collected from the data subject"* and is satisfied at the time of collection [E, Art. 13]. **The invitation is that moment.** It must give, among other things: the controller's *"identity and the contact details"* (13(1)(a)); *"the purposes of the processing … as well as the legal basis"* (13(1)(c)); where 6(1)(f) is used, *"the legitimate interests pursued"* (13(1)(d)); *"the recipients or categories of recipients"* (13(1)(e)); *"the period for which the personal data will be stored"* (13(2)(a)); the rights of access, rectification, erasure, restriction, objection and portability (13(2)(b)); where consent is used, *"the right to withdraw consent at any time"* (13(2)(c)); **the right to complain to the controller under section 164A of the 2018 Act (13(2)(ca)), a requirement added since `compliance-note.md` was written**; and the right to complain to the Commission (13(2)(d)) [E, Art. 13, latest revised text].

**Change needed — PRIV-4, add:**
> **Before the first person outside Candour is invited to any test**, a test-programme notice covering PRIV-4(2) and (3) for test data is published, and the invitation links to it or contains it. It meets UK GDPR Article 13(1) and (2), including 13(2)(ca). The launch notice later absorbs it.

The exact invitation text, written to carry all of this in plain words, is at §5.1.

### 4.3 Retention — **CEO decision** on the numbers

Article 5(1)(e): personal data are *"kept in a form which permits identification of data subjects for no longer than is necessary"* [E, Art. 5]. Constitution Article 4: *"Collect the minimum data necessary, state why, and delete it when no longer needed."*

**Recommended [J]:**
- **Summaries and feedback emails:** deleted **30 days after the measurement result is published or the test closes, whichever is later.** What survives is the published per-phone counts with no names, which are not personal data once the sender is gone. [I]
- **The tester list:** removed from the Play test and deleted **within 30 days of the test closing**, unless a tester has asked in writing to join the next one.
- **Consent records:** kept as long as the data they cover, then deleted with it. Keeping them longer would be holding personal data to prove a consent to processing that no longer exists. [J]
- **On withdrawal:** deleted within 7 days of the request, and the volunteer is told when it is done.

These numbers go into the invitation. Changing them later for data already held would need the volunteers to be told.

### 4.4 Does the ICO registration cover it? — **CEO action**

**The duty.** *"A data controller must comply with the requirements of this regulation unless all of the processing of personal data they undertake is exempt processing"*; *"Within the first 21 days of each charge period a data controller must pay a charge"*; and for a new controller the charge period is *"the period of 12 months beginning on the date on which the person becomes a data controller"* [E, Charges Regs reg. 2(1), 2(2), 2(6)(c)]. The ICO: *"organisations (including sole traders) that use personal information need to pay a data protection fee"* [E, ICO fee page].

**Is the beta exempt?** I read the Schedule's list in full [E, Charges Regs Schedule para 2(2)]. The candidates that sound close do not fit:
- 2(2)(b), *"personal, family or household affairs"*: no; this is a business testing a product. [I]
- 2(2)(d), *"administration in relation to the members of staff and volunteers of"* the controller: a beta tester's capture counts are not staff or volunteer administration. **Moderate confidence** [I]: "volunteers" in that paragraph reads as people who work for the organisation unpaid, not people testing its product. This is the one point I would put to the Constitution 6.1 human review (L1) if it is commissioned.
- 2(2)(a), not processed *"by automated means"*: no; email is automated.

**So, on my reading, a fee is owed no later than 21 days after the first tester's data reaches Candour** — earlier if Candour is already a controller of anything else (a support inbox, a mailing list). [I]

**Does a registration exist?** **I found no record on `main` that the fee has been paid.** Every reference is a budget line: `cost-sheet-v2.md` and `cost-sheet-v3.md` carry *"ICO data protection fee, Tier 1 … £52.00"* [E, retrieved by the CFO 2026-09-20 and 2026-09-22; **not re-verified by me**: the ICO pages I retrieved today do not state tier amounts], and both list the fee *"determination"* as open with the CGO (`cost-sheet-v2.md` F8). **This note closes that determination: owed, once the beta starts at the latest.** [I]

**Does a paid fee "cover" the beta?** Since 2018 the fee is a charge on the controller, not a registration of named purposes, so a paid fee covers all of a controller's processing [K, moderate confidence; the regulation's text I retrieved is consistent with this, since it attaches the charge to *"a data controller"* and not to a purpose]. **Where I looked:** reg. 2 and the Schedule of the 2018 Regulations, and two ICO fee pages. **What would overturn it:** an ICO statement that the register entry must list processing purposes and be updated for new ones.

**Action for the CEO:** confirm whether the fee has been paid; if not, pay it before the first invitation goes out. It is £52 a year on the CFO's figure and already on the cost sheet, so this is not new spending, only spending that is now due.

### 4.5 Two scoping limits the invitation must state

- **UK only.** Requirements line 947: *"The whole consumer-law analysis is UK."* A Play closed test can be offered in other countries; the test is restricted to the UK in Play Console, and the invitation says it is for people in the UK. EU testers would bring the EU GDPR, which nobody has analysed. [I]
- **18 and over** [J]. The app records nights out and MEM-1 exists because it *"edges towards encouraging drinking"*. Article 6(1)(f) also weighs interests *"in particular where the data subject is a child"* [E, Art. 6]. A volunteer test has no reason to include under-18s.

### 4.6 One thing for the PM/BA and CTO, flagged not owned

**A 14-day test against a two-week trial.** The product has *"a two-week full-feature trial"* (requirements §2) and CAP-7 stops capture when entitlement ends. If a test build enforces entitlement, capture stops around day 14 and the second week of a 14-day carry becomes gaps marked *"capture not entitled"* (DEF-5). The measurement would be harmed and the invitation could not truthfully say the test is free throughout. **Test builds need capture entitled for the whole test**, however the CTO chooses to do it. Owner: PM/BA to write, CTO to design, QA's item 43(2)(ii) touches it.

---

## 5. G8: the release — the invitation and the first-launch label

**The governing texts.** Block 2 §4.2: any Android build outside Candour before the lift says, *"at first launch and in the invitation, that Android capture has not yet been measured on their kind of phone and may miss visits, and that missed time is shown where Haunts knows about it. It makes no claim that capture is automatic or reliable on Android."* CAP-14(c): *"no store copy or in-app text says capture is automatic or reliable on Android."* CAP-17(d): no copy *"says or implies that adding a missed visit makes Haunts reliable, or that it will fix the miss."* Constitution 1.3: *"We say what a product cannot do."* Article 4: *"claims we cannot substantiate are claims we do not make."* 5.4: *"release to real users"* is the CEO's.

**Also relevant, and new to this line of work:** Google requires new personal developer accounts to run a closed test with *"a minimum of 12 testers who have been opted in continuously for at least 14 days"* before production [E, Play Console Help 14151465]. `android-and-stack-note.md` already records this. **So some closed test is not optional for Android; it is on the critical path, and every one of its builds falls under §4.2's label.** Testers opt in through Google's page, where Candour may *"Provide a feedback URL or email address"* that *"appears on your tester opt-in page"* [E, Play Console Help 9845334]. That page is a second place the label's substance must appear. [I]

### 5.1 The invitation — proposed exact text

Placeholders in square brackets are for the CEO. The invitation is not an app string, so check 15 does not scan it, but MEM-1 binds it as *"store and marketing copy"*. I read it against the beat-or-break test: nothing in it states, praises or invites a number about the reader's visits, and words on HEAD-6(a)'s list that appear (*"keep"*, *"don't"*, *"miss"*) are used in their plain sense, never about going out more.

> **Help test Haunts on Android (a test version)**
>
> Haunts is a private journal of the places you go. It runs on your phone and keeps your journal there.
>
> **What we're testing, honestly.** We haven't yet measured how well Haunts notices your visits on Android phones like yours. Some phones stop apps running in the background to save battery, and when that happens Haunts can miss visits. When Haunts knows it wasn't running, your timeline shows that time. When it doesn't know, a visit can be missing with nothing to show for it. Finding out how often that happens is the point of this test.
>
> **What we'd ask.** Use Haunts as you normally would for at least 14 days. If you notice a visit Haunts missed, you can add it yourself and mark it "Haunts missed this". Adding it fills in your own journal; it doesn't fix Haunts. If you'd like to, you can send us a capture summary from Settings: three numbers, the dates they cover, and the app version. All of this is optional.
>
> **What we receive, and what we don't.** The app sends us nothing. Your journal, your places, times, notes and ratings stay on your phone. If you email us a summary, we receive those three numbers and dates, and your email address and name as they appear on your email. To run the test we also hold the Google account email you join with. If your phone shares crash reports with Google, Google may pass crash details on to us; never your journal.
>
> **Why, and on what basis.** We use the summaries you choose to send to measure how Haunts behaves on real phones, before we sell it for Android, **with your consent**, which you can withdraw at any time by emailing [address] with the word "delete". We keep the tester list because you asked to join the test, which is our legitimate interest in running it. We use your data for nothing else.
>
> **What we publish.** The results, by phone model, with no names. If you withdraw after they are published, we delete everything we hold about you; the published numbers stay, because they don't identify you.
>
> **How long we keep it.** Summaries and emails: deleted 30 days after the results are published or the test closes, whichever is later. The tester list: deleted within 30 days of the test closing. If you ask us to delete your data, we do it within 7 days and tell you when it's done.
>
> **Who else sees it.** Google, which runs the test list through Google Play, and our email provider, [name]. Nobody else.
>
> **Your rights.** You can ask to see, correct or delete what we hold, object to how we use it, or have a copy. If you're unhappy, tell us first at [address]; you can also complain to the Information Commissioner's Office at ico.org.uk.
>
> **Who we are.** Candour is [founder's full name], trading as Candour, [contact address]. Full test privacy notice: [link].
>
> **The small print, in plain words.** The test is free, and testing never signs you up to pay for anything. It's open to people in the UK aged 18 or over. Test versions can have bugs: you can export your whole journal at any time from Settings, free, and it's yours whatever happens to the test. Haunts makes no promise to support this test version for any period.

Notes on the text, for the reviewer:
- **"Adding it fills in your own journal; it doesn't fix Haunts."** This is CAP-17(d) said aloud rather than merely avoided. [J]
- **"with nothing to show for it"** states the silent-miss case. §4.2 requires *"missed time is shown where Haunts knows about it"*; saying what happens where it doesn't know is 1.3. [J]
- **"Haunts makes no promise to support this test version for any period"** follows Article 4's support clause in spirit: Article 4's duty attaches *"before first sale"*, and a free test is not a sale, so this line is [J], not a requirement.
- **Crash reports via Google** is [K, moderate]: Play's Android vitals reach the developer from users who share diagnostics with Google. QA confirms what Play Console actually shows for a closed test before this sentence ships.
- **"before we sell it for Android"** is true only if the CEO has decided to sell Android at all; he has (requirements §2: *"Platforms: iOS and Android at launch (D1, CEO 2026-09-20)"*).

### 5.2 The first-launch label — proposed exact text (CAP-14(c), Block 2 §4.2)

> **Test version for Android**
>
> We haven't yet measured how well Haunts notices your visits on phones like yours. Some phones stop apps running in the background, and Haunts can miss visits when that happens. When Haunts knows it wasn't running, your timeline shows that time. When it doesn't, a visit can be missing with nothing to show for it.
>
> [Continue]

Requirements for the label, proposed as CAP-14(c)'s AC additions:
- **One screen, one button, "Continue".** No checkbox to tick, no *"I understand"* that must be affirmed, no countdown, no second button styled as the right answer (Article 4: *"no false urgency, no confirm-shaming, no pre-ticked boxes"*). It is information, not consent; consent for data sits in the invitation. [J]
- **It does not mention "Haunts missed this" or the summary.** CAP-15(f) bars *"no new onboarding step (ONB-1)"* and *"no prompt … to keep a diary"*; the invitation carries those, the app does not. [I]
- **The same paragraph is reachable afterwards** from Settings → About for as long as the build is a pre-lift test build, as static text (the PRIV-9 pattern). A label seen once at first launch and then gone is easily forgotten by day 10. [J]
- **The same substance appears on the Play opt-in page** through the feedback-URL field or the test description, so a tester meets it before installing. [I]
- **Its strings join MEM-1(a)'s allow-list** for *"miss"* with Haunts as subject (§2), and no other listed term appears in it. Checked: it contains no *"record"*, *"keep"*, *"don't"* or *"this week"*.
- **It is removed only by the lift**, never by a build flag that a release candidate could ship with set. QA checks the string in any external pre-lift build (CAP-14(c) AC already says *"CI or QA checks the string"*).

---

## 6. What I would block, stated now

My charter: *"Can block: Gate passage — for constitutional breach, unanswered dissent, or missing compliance evidence. Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it."*

**I am not blocking anything today**, because no gate is in front of me. The beta itself is a CEO decision under 5.4, and I cannot block a release; the CSO, QA and UX hold release blocks (5.6). UX has stated its own release conditions (`ux-note-cap-15-17.md` §8) and I do not repeat them.

**At the gate or phase review that relies on this measurement** — the review pack putting the Block 2 lift and the Android release build to the CEO, which I compile under 5.5 — **I would block gate passage for missing compliance evidence** if any of the following is absent:

| Missing evidence | Ground | Lifted by |
|---|---|---|
| A test privacy notice published before the first invitation, meeting Art. 13 including 13(2)(ca) | UK GDPR Art. 13 [E]; PRIV-4 as changed in §4.2 | The notice, dated before the first opt-in |
| A consent record for every volunteer whose summary is used, if the CEO chooses consent | UK GDPR Art. 7(1) [E] | The records, or the CEO's written choice of legitimate interests with the balancing written down |
| Evidence the ICO fee is paid | Charges Regs reg. 2 [E] | The ICO's receipt or register entry |
| Any non-CEO carrier's diary, export, `capture.db` or logs held by Candour | UK GDPR Art. 9 [E]; Constitution Article 4, *"Collect the minimum data necessary"* | Deletion confirmed, and a DPIA screening written; or the measurement re-run under G6 |

Each is a checklist item, cheap to satisfy, and I would rather it were satisfied than blocked.

---

## 7. What would overturn these findings, and where I looked

- **G2** is overturned if `tools/check-strings.ts` is written with whole-word matching and the helper line is reworded; then only the allow-list remains. I did not read the check, which does not exist on `main`.
- **G6** is overturned by a protocol that computes the lift and diagnoses silent misses from counts alone (§3.4), or by the CEO carrying both phones.
- **§4.1**: the basis choice is policy; either is lawful on my reading. A Constitution 6.1 human review could disagree, most plausibly on 2(2)(d) of the fee Schedule.
- **§4.4**: overturned by evidence the fee is already paid, which would make the action moot, or by an ICO statement that the register must list purposes.
- **§5**: the label and invitation are [J] drafting against quoted clauses. A volunteer who reads the label and still believes capture is reliable would show the wording failed; the test's own emails are the place to look.
- **Where I looked:** the files under "Input artifacts", and the sources in §8. I ran nothing, contacted nobody, and installed nothing.

---

## 8. Sources retrieved this session (2026-10-11)

| Tag | Source | Used for |
|---|---|---|
| [E, Art. 4] | [UK GDPR Art. 4, legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/article/4) | Personal data (4(1)); consent (4(11)) |
| [E, Art. 5] | [UK GDPR Art. 5](https://www.legislation.gov.uk/eur/2016/679/article/5) | Storage limitation (5(1)(e)) |
| [E, Art. 6] | [UK GDPR Art. 6](https://www.legislation.gov.uk/eur/2016/679/article/6) | Lawful bases 6(1)(a), (f); revised to 5 Feb 2026 |
| [E, Art. 7] | [UK GDPR Art. 7](https://www.legislation.gov.uk/eur/2016/679/article/7) | Demonstrating and withdrawing consent |
| [E, Art. 9] | [UK GDPR Art. 9](https://www.legislation.gov.uk/eur/2016/679/article/9) | Special categories; explicit consent |
| [E, Art. 13] | [UK GDPR Art. 13](https://www.legislation.gov.uk/eur/2016/679/article/13) | Information at collection, incl. 13(2)(ca) |
| [E, Charges Regs] | [SI 2018/480 reg. 2](https://www.legislation.gov.uk/uksi/2018/480/regulation/2) and [Schedule](https://www.legislation.gov.uk/uksi/2018/480/schedule) | Fee duty, charge period, exemptions |
| [E, ICO fee page] | [ICO, data protection fee](https://ico.org.uk/for-organisations/data-protection-fee/) | Sole traders pay (single source; authoritative) |
| [E, ICO consent] | [ICO, when is consent appropriate](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/when-is-consent-appropriate/) | Choosing consent (single source; authoritative) |
| [E, ICO legitimate interests] | [ICO, when can we rely on legitimate interests](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/when-can-we-rely-on-legitimate-interests/) | Tester list basis (single source; authoritative) |
| [E, ICO high-risk examples] | [ICO, examples of processing likely to result in high risk](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/examples-of-processing-likely-to-result-in-high-risk/) | DPIA trigger for geolocation (single source; authoritative) |
| [E, Play Console Help 9845334] | [Google, set up an open, closed or internal test](https://support.google.com/googleplay/android-developer/answer/9845334) | Opt-in page; feedback channel (single source; authoritative for Play) |
| [E, Play Console Help 14151465] | [Google, testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465) | 12 testers for 14 days (single source; authoritative for Play) |

**Not retrieved, and labelled where used:** the ICO fee tier amounts (carried from the CFO's retrieval); DPA 2018 s.164A itself (cited only as Art. 13(2)(ca) refers to it); what Play Console shows of testers' crash data [K].

---

## 9. Changes for the PM/BA, in one place

1. **MEM-1(a):** the whole-word match rule and the scoped *"miss"* allow-list, extended to the CAP-14(c) label (§2). Replaces UX F3's text.
2. **CAP-15 helper line:** *"Turn this on if you were here and Haunts has no visit for it."* (§2). Replaces UX's.
3. **CAP-16:** the preview sentence *"Whoever you send this to will see that it came from you."* with its AC (§3.1).
4. **CAP-16(b):** no recipient, subject or body supplied; no Candour address in the feature (§3.2).
5. **CAP-14(e):** volunteer figures published only as self-reported misses, never as a rate (§3.3).
6. **CAP-17 and CAP-11:** a non-CEO carrier's diary, export, store and logs stay on their phone; classification on the phone (§3.4).
7. **PRIV-4:** a test notice before the first invitation, meeting Art. 13 including 13(2)(ca) (§4.2).
8. **CAP-14(c):** the label text and its ACs (§5.2).
9. **§22:** item 43(1)'s CGO half and caution 3 are answered by this note; item 40 can cite §1's agreement with UX F7. **New §22 items:** the lawful basis and retention (CEO); the ICO fee (CEO); who carries the lift phones (CEO, with spending); entitlement in test builds (PM/BA, CTO; §4.6).

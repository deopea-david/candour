# UX note: the "Haunts missed this" entry and the counts summary (CAP-15 to CAP-17)

**Seat:** UX / Design Lead · **Date:** 2026-10-10 · **Slug:** `haunt`
**Provenance:** UX Lead · opus (Opus 5.5) · effort medium · 2026-10-10.
**Commissioned by:** the Coordinator (the CEO ran `/coordinator`), on the **D69** "Owed" line in `decisions/2026-09-16-haunt-gate.md`: *"UX and the CGO check the counts against MEM-1 (a count only as a plain fact) and Article 4."* This is the UX half. The CGO's half is separate, and nothing here stands in for it.
**Input artifacts, all read from disk this session on `origin/main` at `119f786`:** `constitution.md` (Article 4 in full; Article 5 block list), `roles/ux-lead.md`, `pipeline/evidence-standard.md`, `decisions/2026-09-16-haunt-gate.md` (D21, D69), `products/haunt/requirements.md` v1.5 (§3.1 MEM-1; DEF-5; CAP-4, CAP-11 to CAP-17 and the PM/BA's three cautions; ENT-4; HEAD-6; §15 A11Y-1 to A11Y-10; §22 items 40 to 43), `products/haunt/ux-home-headlines.md` §4.1, §4.2, §5.3, `products/haunt/architecture/block-2-review.md` §3, §4.
**Output scope:** this file only. `requirements.md` is not edited; the PM/BA applies any change below. Each proposed change is written so it can be pasted.
**Template note:** `pipeline/templates/` has no UX-note template (listed this session: cost-sheet, decision-record, dissent-memo, gate-pack, idea-brief, proposal, requirements, research-brief, review-pack). This note follows the charter's named outputs: a usability review note, an Article 4 conformance check and an accessibility note.
**Evidence:** every claim here is about Candour's own rules, and each one quotes the clause it relies on. No external source was retrieved or is cited. My own judgments are tagged [J]. WCAG success-criterion numbers are those already cited in `requirements.md` §15; where I name one it does not cite, I tag it [K].
**Honesty statement:** I have run no usability test and watched no user. Whether a volunteer reads three numbers as a score is an empirical question, and I am answering it with judgment. §6 says what would overturn each answer.
**Status:** this note prepares and flags. It does not certify (Constitution 5.4 and 6.1). Nothing in it is a decision.

---

## 0. The answers, before the reasoning

**A numbering note first.** The commission asks for *"§22 item 42"*. On `main`, item 42 is the CFO's cost note. The question about the counts is **item 43(1)**, which points to the PM/BA's caution 2. I have answered item 43(1).

| # | Finding | Verdict |
|---|---|---|
| F1 | Whether the three counts are plain facts under MEM-1, D21 and the beat-or-break test | **Pass, if two changes are made:** Haunts is the subject of every label, and the date range offers no week or month presets. The fallback in caution 2, which drops "visits recorded", is not needed. |
| F2 | "Misses covered by a gap" as a label | **Change needed.** "Gap" is internal vocabulary. Use the timeline's own words from CAP-4. |
| F3 | The build-wide string search in MEM-1(a) would fail on CAP-15 and CAP-16's own strings | **Change needed.** HEAD-6(a)'s list contains *"miss"* and *"this week"*, and MEM-1(a) applies that list to every string in the build. A narrow allow-list entry is needed. |
| F4 | The wording and placement of the "Haunts missed this" control | **Pass on placement. Change needed:** the control must start off in every entry route (Article 4: *"no pre-ticked boxes"*). Exact wording is proposed below. |
| F5 | Whether the share-sheet export is started by the user, with no nudging | **Pass, with one addition:** Haunts says nothing after the share sheet closes. No thank-you message and no toast. |
| F6 | Accessibility (§15) | **Change needed.** The marker must be part of the row's single accessible label (A11Y-6). The preview must be real text with each number on the same line as its label, and must survive the largest text size (A11Y-4). |
| F7 | Whether CAP-15(h)'s keep-or-hide choice changes the answer | **It does not change F1.** It does expose a coupling nobody has decided: whether CAP-16 follows CAP-15 when the control is hidden. That is a flag to the CEO through item 40. |
| — | Blocks | **None.** No release is in front of me, and my block applies to release (Article 5). I state below the conditions under which I *would* block at release, so nobody has to discover them later. |

---

## 1. F1: are "visits recorded", "visits missed" and "misses covered" plain facts?

### 1.1 The rules, quoted

- **MEM-1** (`requirements.md` §3.1): *"Haunts never encourages drinking, and never rewards the frequency or volume of visits — anywhere in the product… **a count may appear only as a plain fact.**"*
- **D21** (decision record): *"Haunts never encourages drinking and never rewards visit frequency or volume… The test, from UX: **if the user could beat it or break it, it is out.**"*
- **The test as adopted** (§3.1, from `ux-home-headlines.md` §4.1): a count *"is never the subject of praise, a milestone, a record, a rank, **a rate per period**, a run of consecutive periods, or **a comparison with another period**."*
- **Article 4:** *"no engagement mechanics designed to exploit compulsion."*
- **HEAD-6** applies MEM-1 to the headline slot and is not a separate rule (§8.2: *"HEAD-6 is the headline slot's application of MEM-1"*). The commission's "HEAD-6 beat-or-break test" is therefore the MEM-1 test, and that is the one I apply here.

### 1.2 The test, applied to each count

**"Visits missed"** counts visits the user added with the marker. Its subject is Haunts' failures. A user cannot beat it by going out more. They could only lower it by not adding misses, which would damage their own journal and gain them nothing. It has no run, so nothing can break. **Not a score of the user.** [J]

**"Misses covered"** is a subset of the visits missed: the misses Haunts at least admitted to. Its subject is the app's honesty. Nothing about it is the user's to beat or break. **Not a score of the user.** [J]

**"Visits recorded"** is where the risk sits, and caution 2 is right to raise it. It counts the user's visits, so it is a measure of volume. Two things about it matter:

1. **A count of visits over a span is already permitted.** §4.2 of the headline note, adopted by MEM-1, lists *"Your most-visited place: The Eagle, 41 visits recorded since March 2023"* and *"Your journal goes back to March 2024: 64 places"* as plain facts. The word *recorded* is the one §5.3 asks for (*"Counts are phrased as recorded… not as life-facts"*).
2. **What turns it into a pace is the window, not the number.** The headline note's own example of the line not to cross is *"You've been out 3 times this week!"*: a count over a recent window that *"sets a pace the user can match or miss"*. CAP-16 says only that the counts sit *"over a stated date range"*. If that range is a picker with presets such as "This week", "Last 7 days" or "This month", the summary becomes **a rate per period**, which MEM-1 rules out. Exporting two weeks in a row then makes a comparison between periods, even though the app never shows one. CAP-16(b) already stores nothing about earlier exports, which is right, and it means the app cannot show a comparison. The risk is that the user is invited to make one.

**Who the labels make the subject matters too.** The three numbers in a row (recorded, missed, covered) look like a scorecard. The question is whose scorecard. With **Haunts as the grammatical subject of every label**, the file reads as a report on the instrument: what Haunts caught, what it missed, and what it admitted to missing. With the user as the subject (*"Your visits: 12"*), the first line reads as a tally of nights out. [J]

**Answer to item 43(1):** all three counts are plain facts under MEM-1 and D21 **if** the two changes below are made. A user cannot beat or break any of them. "Visits recorded" may stay, so caution 2's fallback is not needed. Keeping it also has an honesty benefit: without the denominator, a volunteer's "3 missed" cannot be read in proportion. [J]

### 1.3 Change needed: the date range

Proposed text for CAP-16, added after *"over a stated date range"*:

> **The range is a span, never a period.** It runs from a start date the user chooses (default: the date of the earliest visit in the journal, or the install date if that is later) to today. **No preset names a period** ("this week", "last 7 days", "this month", "last month" or similar), and the range is never prefilled from an earlier export. The range is shown as two dates: *"From 1 October 2026 to 24 October 2026"*.

Proposed AC, added to CAP-16(c):

> Assert the range control offers no named preset, that the default start date is as stated, and that opening the summary twice shows the same default both times. Nothing is remembered from an earlier export (CAP-16(b)).

[J] The rule protects the measurement as well. A volunteer's range should be their carrying period (CAP-11), not a calendar week.

### 1.4 Change needed: the labels, and the exact preview text

Proposed exact text for the preview and the file. It replaces CAP-16's working labels and uses CAP-4's wording for a gap (see F2):

```
Haunts capture summary
From 1 October 2026 to 24 October 2026
Haunts 1.0.0 on Android

Visits Haunts recorded: 12
Visits you added that Haunts missed: 3
Of those, during a time Haunts showed it wasn't running: 2

This file holds only these numbers and dates. It has no places, times, notes or ratings.
```

- Haunts is the subject of every count line. The second line names the user only as the person who *added* the visit, which is an act of editing, not a measure of going out.
- The last line is the consent sentence. It tells the user what they are about to share, in words a first-time user can check against the three numbers above it. It is not a reassurance flourish, and it is true by CAP-16(e).
- *"capture summary"* is not on CAP-16(c)'s banned list (*rate, score, accuracy, caught, streak, best, record, improve*). I checked each banned word against the text above and found none.
- The machine-readable keys in the file can stay as the PM/BA wrote them. This wording is for what a person reads.

---

## 2. F2: "misses covered by a gap"

"Gap" is DEF-5's term for engineers. The user meets gaps on the timeline as CAP-4(a) words them: *"Haunts wasn't running between 14:10 and 19:40. Anything you did then isn't here."* A volunteer cannot match "covered by a gap" to anything they have seen. **Change needed:** use the third line of §1.4, *"Of those, during a time Haunts showed it wasn't running"*. That links the count to the screen the user already knows. [J]

A partly covered miss still counts as missed and not covered, as CAP-16 says. The proposed words *"during a time"* match that rule, because a stay that only partly overlaps a gap was not during it. [I]

---

## 3. F3: MEM-1(a)'s string search would fail on these features' own strings

MEM-1(a) requires a *"Build-wide string-table and store-metadata search… for the HEAD-6(a) term list (… and the rest)"* and *"assert[s] zero occurrences outside venue names drawn from the index."* HEAD-6(a)'s list includes *"miss"* and *"this week"*. So **"Haunts missed this"**, **"You added this. Haunts missed it."** and the summary's second line would all fail check 15 (`tools/check-strings.ts`) as written. CAP-16(c) also adds this feature's strings to that same search.

*"miss"* is on the headline list for the absence framing, as in *"12 days since you last visited"* or *"miss your local"*. Here the subject is the app, not the user's absence from a place. **Change needed.** Proposed addition to MEM-1(a):

> **One scoped exception:** the strings of CAP-15 and CAP-16 may contain *"miss"* only where **Haunts** is the subject (*"Haunts missed…"*, *"…that Haunts missed"*). Each such string is listed by key in check 15's allow-list, with this row as the reason. Any other occurrence still fails.

Without this change, either the build fails or someone loosens the check under deadline pressure. The second outcome is worse. [J]

---

## 4. F4: the "Haunts missed this" control

**Placement: pass.** CAP-15 puts the control in the manual composer (ENT-4), as a labelled text control, with no prompt to use it anywhere else (CAP-15(f): *"no prompt to add another or to keep a diary"*). That is the right place. A user who knows a visit is missing is already in the composer, and nobody else is invited in. I would **not** add an "Add a missed visit" call to action to the gap surface on the timeline. CAP-15(f) already rules that out, and I agree with it. [J]

**Default state: change needed.** CAP-15 does not say what state the control starts in. Article 4 is explicit: *"no pre-ticked boxes."* A route that opens the composer from a gap or a time range could reasonably be built to pre-set the marker, so the requirement should close that off. Proposed addition to CAP-15:

> The control is **off when the composer opens, by every route**. The user turns it on.

Proposed AC: *"Open the composer from each route that reaches it; assert the control is off each time."*

**Wording: change needed, small.** Proposed:

- **Control** (a switch, with the label as text): **"Haunts missed this visit"**. Helper line under it: *"Turn on if you were here and Haunts didn't record it."*
- **On the visit's row and page** (CAP-15's own example, kept): *"You added this. Haunts missed it."*
- **CAP-15(d)'s refusal sentence:** *"Haunts recorded this visit, so it can't be marked as missed."*
- **CAP-15(e)'s overlap sentence:** *"This overlaps a visit Haunts recorded at The Eagle, 19:10 to 21:40. Open it?"* The user can still save.

None of these thanks the user, counts anything, or asks for more entries. The helper line gives a first-time user what the switch means without any explanation from us. [J]

---

## 5. F5: is the share-sheet export user-initiated, with no nudging?

**Pass.** CAP-16 and its ACs already require that:

- the summary is generated *"only when the user taps the control, never on a schedule, on a count, at the end of the measurement, at launch or on any event"*;
- *"no notification, badge, banner, interstitial or reminder offers it"*;
- it is *"reachable only by navigating to it"* (a labelled row in Settings);
- the user reads the exact text before sharing;
- *"no state is written that records that the user did or did not export."*

Showing the exact text before the share sheet is good consent design. It goes beyond Article 4's minimum and costs one screen. [J]

**One addition (change needed, small).** After the share sheet closes, whether the user shared or cancelled, **Haunts shows nothing**: no "Thanks for helping", no toast and no confetti. A thank-you after a share is the smallest form of reward, and on a volunteer beta it is exactly what a well-meaning builder would add. Proposed addition to CAP-16(b): *"Assert that on return from the share sheet, shared or cancelled, the app shows no message, toast or animation."*

**Settings row wording, proposed:** **"Share a capture summary"**, with the secondary line *"Three numbers about what Haunts recorded and missed. No places."* It sits with the other data rows (export, backup), not at the top of Settings, and is the same weight as its neighbours. [J]

---

## 6. F6: accessibility (§15)

The baseline is Article 4: *"WCAG 2.2 AA as the working baseline, read through WCAG2ICT where the product is native software."* Three changes are needed. None is a block today; each is a release condition (§8).

1. **The marker is part of the row's single label.** A11Y-6 requires *"one accessible label covering everything in it."* Proposed addition to A11Y-6's example: a missed visit's label ends *"… You added this. Haunts missed it."* Proposed AC: assert the marker text is in the row's accessible label on the timeline, the venue page list and search.
2. **The preview is text, and each number sits with its label.** The preview must be real text in the accessibility tree, not an image or a rendered file. Each count is on one line with its label (*"Visits Haunts recorded: 12"*), not a label column next to a number column that a screen reader reads out of order. A11Y-6 cites SC 1.3.1 for this kind of relationship. Proposed AC: with VoiceOver and TalkBack, assert the preview reads in the order of §1.4 and each number is spoken with its label.
3. **The preview survives the largest text size** (A11Y-4: *"no loss of content or function"*). The share button must not cover the consent sentence, and the text scrolls. Add the composer switch and the preview screen to A11Y-4's screenshot set and to the A11Y-10 per-release checklist.

The switch is covered by A11Y-5's target-size floor and needs nothing new. It must expose its state as on or off, which is SC 4.1.2 [K]. The marker is text, not a colour or icon, so A11Y-2 is met as written.

---

## 7. F7: does CAP-15(h)'s keep-or-hide choice change the answer?

**It does not change F1.** The beat-or-break reading depends on the labels and the range, not on who sees the control. With the range defined as a span (§1.3), a long-term user's summary covers years. That is the permitted *"since March 2023"* shape, not a pace. [J]

**It does expose a gap in what has been decided (flag, not a block).** CAP-15(h) says what happens to existing entries if the control is hidden. Nothing says whether the **CAP-16 summary** is hidden at the same time. If the marker can no longer be set, "visits missed" stops growing, and an everyday user would see a summary that looks like Haunts has stopped missing anything. That is a slow drift into an unsupported claim (Article 4: *"claims we cannot substantiate are claims we do not make"*). **Proposed addition to CAP-16:** *"If the CAP-15 control is hidden, this summary is hidden with it."* Item 40's decision should name both. The decision is the CEO's.

**UX's read on item 40, since it asks for one** [J]: I lean towards **keeping** the control. It is a repair tool for the user's own journal, and it is the honest companion to the gap surface: the gap says when Haunts wasn't running, and the marker says what it missed. I see no compulsion mechanic in it. The cost is permanent string-policing, which F3's allow-list makes cheap. The evidence that would change my mind is in item 40: whether volunteers used it unprompted, and whether anyone treated the summary as something to improve.

---

## 8. What I would block at release, stated now

Under Article 5, UX may block *"release, on Article 4 or accessibility grounds."* I am not blocking now. At the release gate I would block:

| Condition at release | Ground | What lifts it |
|---|---|---|
| The date range offers a preset that names a period, or is prefilled from an earlier export | MEM-1 (*"a rate per period"*; *"a comparison with another period"*) and Article 4 (*"no engagement mechanics designed to exploit compulsion"*) | Presets removed; the §1.3 AC passes |
| Anything is shown after the share sheet that thanks, rewards or counts | Article 4, as above; MEM-1 | The §5 AC passes |
| The marker control is on when the composer opens, by any route | Article 4 (*"no pre-ticked boxes"*) | The §4 AC passes |
| The preview is not readable in order by VoiceOver and TalkBack, or loses content at the largest text size | Article 4 (WCAG 2.2 AA); A11Y-4, A11Y-6 | The §6 ACs pass on both platforms |

## 9. What would overturn these answers, and where I looked

- **F1** would be overturned if volunteers in the beta treated the summary as something to beat: for example, by trying to push "visits recorded" up between exports, or by mentioning the number as an achievement in what they send. The beta's own messages are the place to look. If that happens, the caution-2 fallback (share only missed and covered) becomes the right answer, and I would say so.
- **F3** would be overturned if check 15 turned out to scope the HEAD-6(a) list to headline strings only. I read MEM-1(a)'s text, which says *"build-wide"*. I did not read `tools/check-strings.ts`, which does not exist on `main` yet.
- **Where I looked:** the files listed under "Input artifacts", all read on `119f786`. I ran no prototype and no test.

---

## 10. Changes for the PM/BA, in one place

1. **CAP-16:** add the span-not-period rule and its AC (§1.3).
2. **CAP-16:** replace the working labels with the §1.4 preview text, and use CAP-4's wording for a gap (§2).
3. **MEM-1(a):** add the scoped *"miss"* allow-list entry (§3).
4. **CAP-15:** the control is off by every route, with its AC; adopt the control, refusal and overlap wording (§4).
5. **CAP-16(b):** nothing is shown after the share sheet; the Settings row wording and placement (§5).
6. **A11Y-6, A11Y-4, A11Y-10:** the marker in the row label; preview reading order; largest-text screenshots (§6).
7. **CAP-16:** hidden with CAP-15 if CAP-15 is hidden; name both in item 40 (§7).
8. **§22:** item 43(1) can be marked answered by this note for UX. The CGO's half is still open.

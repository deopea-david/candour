# Omission check: the template markers still owed

**CGO subagent · opus (Opus 5.5) · effort high · 2026-10-04.** Written by a CGO subagent run, not by the main session. **Provenance of the script:** the CGO wrote `scripts/omission-check.py` as well as this spec; `pipeline/amendment-draft-coordinator.md` §11 item 18 had named the Engineer for the script, a departure that is the CEO's to accept. Exception (iii) to the role rule (D4a) is now replaced by D16 (`decisions/2026-10-02-coordinator-seat.md`, 2026-10-04); the CGO remains the script's owner. Specification only. **It changes no template.** The templates change by a separate PR, which the CEO merges or not.

**Why this exists.** Annex E of `roles/coordinator.md` makes M2(i) a mechanical check: *"Every block, every fatal or serious objection, every failed QA limb and every 5.2 date under 7 days in the source artifacts appears verbatim in the report."* It also says *"template markers make the labels greppable."* `pipeline/amendment-draft-coordinator.md` §11 item 18 names the files that need them. `scripts/omission-check.py` builds what the current markers allow. This page specifies the rest.

Everything here is about our own files. The observations are [E], read from disk on 2026-10-04 at `origin/main` `12a2a62`.

## 1. What the script can see today, and what it cannot

| M2(i) item | Marker that exists today | Built? |
|---|---|---|
| Fatal or serious objection | The tier tag the dissent template requires: *"Every objection below carries a tier — **[FATAL] / [SERIOUS] / [FRICTION]**"* (`pipeline/templates/dissent-memo.md`, line 11). | **Built.** It reads the tag in a heading, in a bold lead, at the start of a list item, and in a summary-table tier column. |
| 5.2 date under 7 days | `**Decision due:** [date] (5.2)` (`gate-pack.md`, line 5); `**Anti-drift clock:** … due [date + 4 weeks]` (`research-brief.md`, line 4); `- [ ] Research brief … due: [date …]` (`idea-brief.md`, line 15). | **Built**, for those three lines, when the date is an ISO date. If the date is not ISO, the script prints a GAP line. |
| Block | **None.** No template has a block marker. Real blocks are written in prose and in many forms: `> **BLOCK (conditional).**` (`proposals/haunt/gate-pack.md`, line 224), *"Block 4 STANDS, on limb (b) alone"* (`products/haunt/block-4-ruling.md`, line 17), and rows of the gate-pack §4 table. | **Not built for prose.** The script checks the marker proposed below wherever it already appears. Every run prints a GAP line until the templates carry the marker. |
| Failed QA limb | **None.** There is no QA report template; `roles/qa.md` names *"release-readiness reports"* and specifies no format. | **Not built for prose**, as for blocks. |

**Seen in the real memos, and the reason the objection marker needs tightening.** In `proposals/haunt/dissent-memo-c1.md`, three of the seven serious objections (C1-O1, C1-O2, C1-O3) carry their tier **only** in the summary table at lines 355–357. In the body they are named in prose: *"(Objection C1-O1.)"* (line 84). The script reads the table, so it finds all seven. But a memo with no summary table, and with tiers only in prose, would be invisible to it. That failure is silent, which is the worst kind for an omission check.

## 2. The markers

Each marker is **one line, fixed text, in capitals where it is a keyword**. It must work inside a blockquote or a list item, with or without bold. The script already strips `>`, list bullets, `*` and backticks before it matches.

### 2.1 Dissent memo (`pipeline/templates/dissent-memo.md`): tighten the existing tag

Add this to "The strongest case against", after the tier sentence:

> Each fatal, serious or friction objection opens with its own heading, in this form: `### [TIER] ID. Headline`. For example: `### [SERIOUS] O2. The cost model was never re-derived`. The headline is the sentence the CEO is shown verbatim. A summary table may restate it, but never instead of the heading.

The script already reads this form (heading, tag, ID, headline). The change makes it the only form, so a memo cannot fall outside the scan.

### 2.2 Blocks: every template where a seat declares or restates one

The **seat that declares the block** writes it in its own artifact, in this form:

```
BLOCK (CTO): <the ground, citing the article, standard or acceptance criterion>
LIFTS WHEN: <the lifting condition>
```

- `LIFTS WHEN:` follows within three lines. A block without it fails the check, because every blocking charter requires *"state what would lift it"* (for example `roles/qa.md`, `roles/cgo.md`).
- **When a block is lifted or overruled**, its author changes `BLOCK` to `LIFTED BLOCK` or `OVERRULED BLOCK`, and adds the date and the decision-record line. The marker no longer matches, so the block stops being required in reports. The history stays on the page.
- **Where:** `review-pack.md` "Seat reports"; `gate-pack.md` §4 (one marker per live row, under the table, so the table keeps its shape); `decision-record.md` "Overrules exercised" uses `OVERRULED BLOCK`. A seat's own note or ruling (no template exists) uses the same two lines.
- **Would-be blocks** that engage at a later stage are not blocks yet. They use `PRE-DECLARED BLOCK (seat):` and are not required in reports until their author converts them. This keeps M2 from demanding every pre-declared release block in every report. Whether a pre-declared block should be copied anyway is a judgment for the CEO; I have not assumed one. [J]

### 2.3 Failed QA limbs: a QA report section (no template exists yet)

```
QA FAIL (AC-7): <the limb that failed, in QA's own words>
```

One line per failed acceptance criterion or limb, in the QA seat's release-readiness report. The ID is the acceptance-criterion ID from the requirements. **A QA report template is owed.** Writing it is QA's and the PM/BA's work, not this seat's. Until it exists, the marker goes in a section the QA seat titles "Failed limbs".

### 2.4 5.2 dates: one marker everywhere, in ISO form

```
5.2 DUE: 2026-10-07
```

- The existing lines stay as they are. Add this line beside them in `gate-pack.md` (header), `research-brief.md` (header) and `idea-brief.md` (under "Commissioned discovery"), and in a `STATUS.md` for any open idea.
- **ISO dates only.** A date in words (*"7 October"*) cannot be computed against today, and it produces a GAP line.
- When the decision is taken, the decision record's 5.2 line records it. The `5.2 DUE:` line in the gate pack is then changed to `5.2 DECIDED: <date>`, so a decided matter stops counting as at risk.

### 2.5 Decision record (`decision-record.md`)

No new marker beyond `OVERRULED BLOCK` (2.2). Its header `**Anti-drift (5.2):** deadline [date]` is deliberately **not** scanned, because a decision record exists only once the decision is taken.

## 3. What changes in the script when the templates adopt these

- The CGO sets `MARKERS_IN_TEMPLATES = True`, and the GAP line for blocks and failed QA limbs goes.
- The script learns `5.2 DECIDED:` and `PRE-DECLARED BLOCK`, so that it skips them. *Today it already ignores both, because neither matches.*
- **Legacy artifacts written before the markers stay invisible.** That is stated, not hidden. Any report covering a pre-marker artifact still needs the Coordinator to read it for blocks by hand. The phase-review audit samples this.

## 4. Known limits of the script as built, for the phase-review audit

1. **Blocks and failed QA limbs in prose are not seen** (§1). This is the largest gap, because blocks are the first thing honest-broker rule 1 lists.
2. **Case (b) authority:** the script checks that the cited line sits under a recommendation or next-steps heading in a seat artifact. It cannot check Annex D's rule that a request *"that quotes or relays text from a retrieved source does not count"*.
3. **Case (a) authority:** the script checks that the file is on the allowlist, that it is on `main`, and that the cited line exists and is not blank. It cannot check that the line actually says this step comes next. `decisions/*.md` is allowlisted as a whole, including any audit filed there.
4. **The CEO's recorded words** resolve only against what the Coordinator passes with `--ceo-words`. From a session transcript, only entries Claude Code marks `origin.kind: "human"` are read; from a decision record (`decisions/*.md`, as merged to `main`), only blockquoted italic quotes. Quotes are matched verbatim, ignoring case, quote style and whitespace; every fragment of an elided quote must sit in one turn, in order; a found quote with a fragment under 4 words is a GAP. **Decision records do not mark who is quoted**, so a blockquoted italic quote of another seat would count. A marker such as `> CEO: *"…"*` in `decision-record.md` would close this; it belongs with §2.5.
5. **Objections are de-duplicated by ID within each source only.** A table restatement of a heading objection in the same memo is dropped; nothing in one memo hides anything in another.
6. **M8(b) is a screen.** Its phrase list is in the script (`VIEW_PHRASES`) and is the CGO's. Quotes, blockquotes, code and a `My view` block in item 3 is excluded, so a view written inside quotation marks escapes it. Confirmed counts only, as Annex E requires.
7. **Untagged or lower-case tiers without brackets are not seen.** A bracketed tag in any case is found, and an upper-case tier word leading a heading, list item or bold lead is found. A bracketed tag mid-sentence gives a GAP line (not a FAIL, because the Coordinator cannot edit a Skeptic memo to clear it). Each source's INFO line gives the fatal and serious counts extracted, to set against the memo's own verdict.

## 4a. Response to the CTO's review of PR #23 (head `a7eacbf`)

Second and final attempt under the review loop (Annex D). Each reproduction the CTO gave is now a regression test in `scripts/omission-check-test.py`, class `CTOReview` (R1 is kept as a passing test).

| Finding | Response |
|---|---|
| **F1** headlines in an HTML comment or under Links | **Fixed.** HTML comments are removed first; objection headlines, blocks, failed QA limbs and 5.2 dates count only inside item 2. |
| **F2** a cited memo left off the sources | **Fixed.** Each source is printed on an INFO line. A cited gate pack, dissent memo, review pack, decision record, research brief or idea brief that is not a source FAILs, as does any dissent memo in a cited `proposals/<slug>/`. *Chosen over adding them automatically:* the run's source list stays what the Coordinator states, and the FAIL names the file to add. |
| **F3** six template shapes dropped silently | **Fixed, with one limit accepted.** All six shapes in R3 are extracted. A leading tag with no headline FAILs ("tag found, headline not extracted"). *Accepted:* a bracketed tag mid-sentence is a GAP, not a FAIL, and a lower-case tier without brackets is not seen (§4 item 7). |
| **F4** subagent results read as the CEO's words | **Fixed** by the transcript's own marker: only `origin.kind: "human"` entries are read, an allowlist. Over the 20 most recent transcripts of this project, the user-role entries carry `human` (455), `task-notification` (163), `peer` (120) or no origin (interruptions and injected context). Shell output and slash-command expansions inside a human turn are removed. A transcript with no human-marked turn FAILs. |
| **F5** a whole text file as the CEO's words | **Fixed, with a residual stated.** Only `decisions/*.md` as merged to `main`, and only its blockquoted italic quotes; the report itself is refused (§4 item 4). |
| **F6** loose quote matching | **Fixed.** One turn, in order; a fragment under 4 words gives a GAP when found and a FAIL when not. |
| **F7** `asked` passes with no record | **Fixed.** FAIL, as M2(ii) does. |
| **F8** any file with "recommend" in a heading | **Fixed.** Case (b) needs a path inside the repository that git tracks, not the report, not memory, under a heading that *is* a recommendation or next-steps heading. |
| **F9** `--main-ref` chooses its own main | **Fixed.** A ref that is not the default main FAILs the integrity line. *Residual, recorded:* a local `origin/main` can be moved with `git update-ref`. |
| **F10** a view in item 1 | **Fixed.** A `My view` line outside item 3 FAILs M2(iii), is itself an M8(b) hit, and does not exempt what follows it. |
| **F11** a case (a) PASS hides what was cited | **Fixed** as the CTO suggested: the PASS line prints the cited line. *Accepted:* whether that line authorises the step is a reading, which Annex D sends to the CEO ("what a clause means"). |
| **F12** `RESULT: PASS` beside a GAP | **Fixed, both ways.** The result reads `PASS-WITH-GAPS` and the exit status is 3. *Why both:* the RESULT line is what the CEO reads, and the exit status is what any automation reads; either alone leaves one reader seeing a pass. Until §2 is adopted, every report run is `PASS-WITH-GAPS` at best, which is the honest result. |

## 5. What would overturn this, and where I looked

- **Overturn:** a template I did not read that already carries a block or QA marker, or a reading of Annex E under which M2(i) does not require blocks to be machine-found. Either would shrink §2.
- **Where I looked:** all nine files in `pipeline/templates/`; `roles/qa.md`, `roles/cgo.md`, `roles/coordinator.md` (Annex A, D, E); `pipeline/amendment-draft-coordinator.md` §11 item 18; the three dissent memos on disk (`pipeline/dissent-chief-of-staff.md`, `proposals/haunt/dissent-memo.md`, `proposals/haunt/dissent-memo-c1.md`); `proposals/haunt/gate-pack.md`; `products/haunt/block-4-ruling.md`; both decision records.

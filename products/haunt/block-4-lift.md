# Block 4 — lift confirmation

**Seat:** Chief Technology Officer · **Date:** 2026-09-28 · **Ticket:** SPK-01 (`deopea-david/haunts` #279) · **Status:** The written confirmation that `block-4-ruling.md` §6 promised: *"When the items below are in a signed-off requirements document, the block lifts. I will confirm in writing against this list rather than re-argue it."* **Prepares and flags; does not certify** (Constitution 6.1). Kill/proceed and release stay with the CEO (Constitution 5.4).

**Checked:** `products/haunt/requirements.md` **v1.3** (PM/BA, *"draft for sign-off"*) as on `origin/main` at `a530dd3`, against `products/haunt/block-4-ruling.md` (CTO, 2026-09-21) §2.3, §6 and §11, and against the Engineer's source text at `products/haunt/venue-index-remediation.md` §11.

**Template note:** `pipeline/templates/` holds nine templates and none is a block lift or ruling [E, listed from disk 2026-09-28]. This follows the ruling's own structure: the verdict first, then the check, then what would overturn it.

**Evidence.** Every source is a Candour artifact read from disk on 2026-09-28 and cited by file and section. No external source is used. Tags follow `pipeline/evidence-standard.md`.

---

## 0. The verdict

**Block 4 is LIFTED. Limb (b) is met.** `requirements.md` v1.3 contains R-1, R-2, R-3, R-4, R-5 and R-7 as QA-verifiable, BLOCKING acceptance criteria. Each one is verbatim from its source or tighter. I found no item that was dropped or written more loosely in a way QA could not still fail a build on. §2 has the check, line by line.

**What the lift does and does not do:**

1. **It removes Block 4 from requirements sign-off and from venue-index work.** It does **not** sign the document off. Who signs off, and when, is not mine. The CFO's price block (`requirements.md` §0) is unaffected.
2. **It does not touch Blocks 2 and 3**, which the ruling recorded as *"engaged"* on 2026-09-21 (§2.4). I have not re-examined either one here. `STATUS.md` lists Block 2 as *"live — now the larger build risk"* and does not mention Block 3. Block 1 stays *"avoided, not lifted"*. **This is not a general build clearance.** D59 still requires the CEO's architecture decision before any product code.
3. **Limb (a) stays discharged and can be revived by evidence.** The standing conditions S-1, S-2 and S-3 (`block-4-ruling.md` §8; `requirements.md` §7.7.5) still apply. §3.2 below gives S-1 the number the PM/BA asked for, so it now fires by rule instead of by judgement.
4. **The limb's other half, "and in the schema", is now a build check, not a lift condition.** No schema exists, and none may exist until D59 is decided. VEN-7…VEN-12 are BLOCKING criteria, so QA fails a build that does not implement them. I will check VEN-8's trigger myself when I review the first migration (§3.4).

**Authority, stated precisely.** Constitution 5.6 says the CTO holds a block on *"build commencement"* and that *"Only the CEO may overrule a block"*. It says nothing about who **lifts** one. This seat's power to lift comes from its charter: every block must *"state what would lift it"*. The lift conditions are in `block-4-ruling.md` §2.3 and §6. This is a confirmation against conditions this seat set in writing beforehand. It is not a new judgement.

---

## 1. One defect in my own ruling, corrected here

In the ruling, the lift condition and the block's scope together form a loop:

- §2.3 says the block lifts on *"A requirements document for Haunt, **signed off**, containing …"*.
- The same section defines what the block covers: *"'Build commencement' in Block 4 means **requirements sign-off** and any code written against the venue index."*

Read literally, the block forbids sign-off and only a signed-off document can lift it. `requirements.md` §0 and §7.7.7 run into this. They say that *"sign-off of this document is the event that puts it to"* the CTO, while sign-off is itself something the block covers. **This is my drafting defect, the same kind as the circularity §2.3 was written to remove.** The ruling already says what it meant: *"a block that forbids the only thing that could lift it would be a block I had no business declaring."*

**Correction:** the lift depends on **what the document contains**, not on it being signed off. This confirmation is the lift. Sign-off can go ahead as far as Block 4 is concerned. **The one thing sign-off still has to do is keep the checked items** (§4, overturn item 1). **This makes the ruling no looser.** Every item it asked for has to be in the document, and it is.

---

## 2. The check — every R-number the lift requires

**Standard applied** (`block-4-ruling.md` §2.3): *"Verbatim or better — a PM/BA is free to write them more tightly, not more loosely."* I compared each criterion with its source and read each test, because QA fails a build on the test.

### R-1 · AC-1…AC-6 and the four schema preconditions — **MET**

| Ruling item | Requirements v1.3 | Verbatim or better? |
| --- | --- | --- |
| AC-1 copy on first reference; page renders with the index deleted | **VEN-7** | Verbatim in substance. The test is word for word: *"delete the shipped index file; assert the venue page renders identically"* |
| AC-2 refresh writes only unreferenced rows, **enforced in the schema** | **VEN-8** | Verbatim. Keeps *"a trigger or equivalent"* and *"rejected rather than silently skipped"* |
| AC-3 offered, never applied; inert; declining is the default and is remembered | **VEN-9** | The test is verbatim. The prose leaves out one sentence from the source: *"A refresh that would have changed a referenced row writes a `refresh_proposal` instead."* The test still requires it (*"assert … exactly one open proposal"*), so QA can fail a build without it. **Not looser in effect.** Errata below |
| AC-4 a user rename outranks the dataset permanently; no name proposal afterwards | **VEN-10** | Verbatim, and adds `ux-note.md` §2.3 as a source |
| AC-5 merges survive a re-split | **VEN-11** | The test is verbatim (*"assert one surviving venue, all visits attached, history intact"*). The prose leaves out *"a refresh that splits an upstream record must not fork a merged Candour venue"* and the name of the table (`venue_merge`). The test's "one surviving venue" covers the first, and §7.2's preconditions name the table. **Not looser in effect.** Errata below |
| AC-6 no join on GERS ID alone | **VEN-12** | Verbatim |
| Preconditions: `venue` (`venue_id` never derived from a dataset id; `name_source`; nullable `gers_id`; `first_referenced_at` set once, never cleared), `venue_ref`, `venue_merge`, `refresh_proposal` with `declined_at` | **§7.2 preconditions** | Verbatim, except that `venue_ref` loses *"A visit's reference to a venue is a row here"*. What "referenced" means is still there, word for word |
| On the promise line, so it cannot be cut quietly | **§20.1 item 2** | **Tighter.** The ruling did not ask for this |

**Tightening beyond R-1:** VEN-13 (the refresh review surface is not a queue that builds pressure) is the PM/BA's own addition.

**Errata, not a condition of the lift:** at the next revision, the PM/BA should restore the three sentences left out of VEN-9, VEN-11 and the `venue_ref` precondition. Each one states a behaviour the tests already enforce, so the prose should say it too. This takes minutes, and "verbatim" is simpler to check than "equivalent in effect".

### R-2 · The three D8 constraints — **MET, and tighter**

| Ruling item | Requirements v1.3 | Verbatim or better? |
| --- | --- | --- |
| Twenty **reachable** rows; QA tests the reachable length, not the visible one | **CONF-4** | Verbatim in substance. Adds (b): the list lengths are build constants that show up in a diff |
| Prefix, incremental, never whole-string or exact | **CONF-5** | Verbatim. (b) adds that the full name must never do *worse* than the prefix |
| Never auto-select, **binding the notification path** | **CONF-3** + **VEN-22** | **Tighter.** VEN-22 lists every notification, quick action, widget, shortcut and deep link, and requires the surface reached from a notification to be byte-identical to the one reached from the queue. It also closes the gap between CAP-9 and D3 that the ruling only flagged (§4.5) |

### R-3 · The confirmation prior with its guard — **MET**

**CONF-11**: the prior is *"a ranking input and never a selection"*, with P3 as test (a), and the 150 m gate as a named constant. **VEN-20** makes P3 release-gating. The ruling's two requirements, that the prior raises a venue and never pre-selects one, are both there.

### R-4 · Near-miss and generic-token hazards — **MET**

**CONF-8** (generic-token suppression as a named, testable function; distance and category shown prominently) and **CONF-9** (near-miss pairs shown side by side before either can be chosen; false-pick rate reported). The ruling asked only that each hazard be *"named and answered rather than discovered at pre-release"*. Both are answered, and CONF-9 is BLOCKING.

### R-5 · P5, repairable by the user on the device — **MET, and tighter**

| Ruling limb | Requirements v1.3 |
| --- | --- |
| The venue page lists the visits it is built from | **VPAGE-2**, pointed to from VEN-21 |
| A visit can be reattached | **VEN-21**, using the same confirm surface, not *"a second, lesser picker"* |
| Merge is reachable from the venue page and reversible | **VEN-14** (unmerge restores exactly), **VPAGE-5** |
| Rename is reachable and permanent | **VEN-15**, **VEN-10** |
| MVP, not backlog | All BLOCKING. VEN-21 is **§20.1 item 7**, and §20.2 bars any cut that sets off S-3 |
| The test without a user: wrong venue → move → merge → undo → nothing lost, all on the device | **VEN-21**, word for word, and **tighter**: it adds session overrides and capture-gap links to what must survive, a limit of two actions to reach it, and (b) the repair must work **when the subscription has lapsed** |

VEN-21(b) is the PM/BA's addition, and I agree with it. A repair that only works while the user is paying does not answer a concern about corruption that is permanent and invisible.

### R-7 · The nine-cell neighbourhood query — **MET, and tighter**

**VEN-23**: fixtures with the true venue in each of the eight neighbouring cells, the union as a named function, and the fixture added to VEN-17's regression set *"so a later optimisation that drops it fails CI"*. That is stronger than the ruling's *"must survive into requirements"*.

### Not part of the lift, checked because the ruling listed them

- **R-6** (false-pick criterion; measured `CLVisit` accuracy) → **CONF-9**, **VEN-24**. VEN-24(c) fails a release whose field-run report has no accuracy figures in it. That is more than R-6 asked for.
- **R-8** (Condition 7's licence screen, export texts, "Delete my backup") → **LIC-1…LIC-5**, **DATA-12**. Not part of Block 4, and `requirements.md` §7.7.7 says so.

**Result: 6 of 6 required items met. Each is verbatim in its tests, and tighter in R-2, R-5 and R-7. There are 3 prose errata, and none of them loosens what QA can fail on.**

---

## 3. What the requirements document puts back to this seat

The PM/BA flagged two things to me in §7.7. I answer both here. One is a decision only this seat can make.

### 3.1 P4 does not pass under VEN-20(c), and I agree with VEN-20(c)

VEN-20(c) compares the **lowest** of the three P1 figures against the threshold. The PM/BA applies the same rule to P4, and P4 then fails: **89.8% against 90%** at σ = 50 m under the harshest single-query policy [E, measured by the Engineer, `venue-index-nameseach.md` §7.2, as quoted in `block-4-ruling.md` §2.1; not re-run by me].

- **The PM/BA's reading is stricter than mine, and it is correct.** My ruling scored P4 as *"MARGINAL PASS"* using the headline figure (93.9%). A criterion that does not say which figure is compared will end up compared against the kindest one. The PM/BA was right to close that gap, and a bar should be read the strict way.
- **This does not revive limb (a).** My discharge never depended on P4 passing under the harshest policy. The ruling said: *"89.8% at σ = 50 m under `t1` is a fail by 0.2 pp. §8 carries it as a standing condition rather than smoothing it into the pass"* (§2.1 item 3). The fact is the same. What is new is the consequence, and it falls in the right place: **as written, a release fails at P4 until the σ = 50 m case improves.** That is a design requirement for the build, not a reason to stop it starting.
- **The threshold must not move to fit the result.** The PM/BA refuses to do that (§7.7.6 item 2), and I agree. If the PM/BA, UX and QA ever reopen P4 for other reasons, my ruling commits me to re-rule against the new value (§3.1).

### 3.2 S-1 gets a number — my decision, because the block is mine

The PM/BA wrote: *"if you want S-1 to fire automatically rather than on judgment, it needs a number, and that number is yours because the block is."* That is right, and *"materially worse"* was loose drafting on my part.

**A second drafting defect, corrected first.** S-1 compares *"measured median horizontal accuracy"* with *"25 m"*. But 25 m is the harness's **σ**: the per-axis standard deviation of an isotropic Gaussian offset (`venue-index-spike.md` §5, as described in `block-4-ruling.md` §5.2). It is not a median distance. For that error model, the distance from the true point follows a Rayleigh distribution with median σ·√(2 ln 2) ≈ **1.177σ**. So **σ = 25 m corresponds to a median error of about 29.4 m**, and a measured median of 30 m corresponds to σ ≈ 25.5 m. *(Arithmetic; under gate Condition 6 a second seat should recompute it.)* Comparing a measured median directly with 25 m would set S-1 off about 18% early.

**S-1, restated — it replaces the ruling's §8 S-1 wording:**

> **S-1.** VEN-24's field run reports the median distance between recorded `CLVisit`/visit centroids and the surveyed venue positions, per platform, in a dense UK city centre. **If either platform's median exceeds 30 m**, the VEN-17 fixture is re-run with σ set to that platform's measured median ÷ 1.177. **If P1 is then below 95%, limb (a) re-engages and Block 4 is declared again**, with no further judgement needed. If P1 holds, the result and the re-run are published in the release pack and the block stays lifted.

Why this shape [J]:

- **The trigger is where the evidence runs out.** P1 was only ever measured at σ = 25 m. Any real error above that is outside what the discharge rests on, so the test is whether P1 holds at the real figure, not whether the real figure is "a lot" worse. The 30 m cut-off is σ = 25 m plus rounding (about 0.6 m), so ordinary measurement noise alone does not set it off.
- **The re-test is cheap.** The fixture runs in about fifteen minutes (VEN-17). Firing automatically costs next to nothing. That is the difference between a standing condition and a permission slip.
- **The Gaussian model may understate the tail** [I]. A real error distribution with heavy tails would make the model's median look better than the typical case really is. VEN-24(a) already asks for the spread, so the release pack will show it. I am not adding a percentile trigger now, because there is no measured distribution yet to set one on.

**What the PM/BA needs to do:** replace the S-1 row in §7.7.5 and VEN-24(b)'s *"materially worse"* with the text above. This is a change to the trigger, not to the lift. The lift does not wait for it.

### 3.3 No other open items in §7.7 belong to this seat

The thresholds stay with the PM/BA, UX and QA (`block-4-ruling.md` §3.1). §7.7.6 item 5 records that UX and QA have not yet confirmed them. That is the PM/BA's item (§22 item 14), not a condition of this lift.

### 3.4 How "in the schema" gets checked

Limb (b) said *"in the requirements document **and in the schema**"*. The ruling's lift (§2.3) asks only for the document, because a block that needs a schema before a build could not be lifted before a build. The schema half is kept by:

1. **VEN-7…VEN-12 are BLOCKING** acceptance criteria. QA fails a build that does not implement them.
2. **This seat's review of the first migration** that creates `venue`, `venue_ref`, `venue_merge` and `refresh_proposal`. I will confirm that VEN-8's rule is a schema trigger, *"not in application code"*, before it merges. **Owner: CTO. Trigger: the first PR touching the venue schema.**
3. For information only, not relied on here: the code-architecture proposal waiting for D59 (branch `haunt/architecture`, not on `main`) already puts VEN-8's trigger in the first migration file.

---

## 4. What would overturn this lift, and where I looked

**The lift is overturned by any of:**

1. **A signed-off version of `requirements.md` that removes or weakens any row in §2.** The lift is a check of v1.3's content. A later version that loosens R-1, R-2, R-3, R-4, R-5 or R-7 undoes it. **S-3 already covers the repair layer. This item covers the rest.** The PM/BA's scope-change log (§24) is where such a change would appear.
2. **S-1** (as restated in §3.2), **S-2** or **S-3** firing, as in `block-4-ruling.md` §8.
3. **Someone showing that one of the prose errata in §2 R-1 is a real loosening**: a behaviour the source criterion requires that the v1.3 **test** no longer catches. I read all six tests against the source and found none. A reader who finds one overturns the R-1 finding.
4. **An architecture decided under D59 that cannot enforce VEN-8 in the schema.** That would bring back the reason limb (b) was declared (`block-4-ruling.md` §2.2: *"enforceable in the schema by a trigger and unenforceable afterwards"*).

**Where I looked:**

- `products/haunt/block-4-ruling.md`, read in full (§0–§12).
- `products/haunt/requirements.md` v1.3: §0 (status and gates on sign-off); §7 in full (§7.1–§7.7.7); the CONF table (CONF-1…CONF-19); VPAGE-1…VPAGE-7; §20.1 and §20.2 (promise and cut lines); §21.1; and the sign-off references throughout.
- `products/haunt/venue-index-remediation.md` §11 in full, compared line by line with VEN-7…VEN-12 and §7.2.
- `constitution.md` v1.3 §5.4, §5.6 and §6.1, and `roles/cto.md`.
- `decisions/2026-09-16-haunt-gate.md` (sequencing clause; D59).
- `deopea-david/haunts` issue #279 (SPK-01), for what "done" means.
- **Where I did not look:** I did not re-run the harness (the ruling did not either; §1 there names the reliance). I did not review Blocks 1–3. I did not read the requirements outside the sections listed. Nothing in the lift depends on them, but a change there that touched venue identity would fall under overturn item 1.

---

## 5. Disposition

| Item | Result | Whose now |
| --- | --- | --- |
| **Block 4, limb (b)** | **LIFTED**, 2026-09-28, on `requirements.md` v1.3's content. 6 of 6 required items met | — |
| **Block 4, limb (a)** | Stays discharged. It comes back under S-1 (now numeric), S-2 or S-3 | CTO to re-rule if one fires |
| **Blocks 1, 2, 3** | Not examined here. As the ruling recorded them: 1 avoided, 2 and 3 engaged. `STATUS.md` does not mention Block 3, and it should | CTO |
| **Loop in the ruling's lift condition** | Corrected (§1): the lift depends on content, not on sign-off | — |
| **P4 under VEN-20(c)** | Stricter reading accepted. A release fails at P4 until σ = 50 m improves. Not a block | Engineer (design), PM/BA (§7.7.1) |
| **S-1's number** | Median > 30 m per platform → re-run at the measured σ → re-declare if P1 < 95% | PM/BA to write into §7.7.5 and VEN-24(b) |
| **Prose errata** in VEN-9, VEN-11 and the `venue_ref` precondition | Restore the source sentences at the next revision | PM/BA |
| **Schema half of limb (b)** | Checked at the first venue-schema PR | CTO |
| **Rayleigh median factor 1.177** | To be recomputed by a second seat (gate Condition 6) | Any seat other than CTO |

---

## 6. Change log

| Date | Change |
| --- | --- |
| 2026-09-28 | Created. **Lifts Block 4** against `requirements.md` v1.3 §7.7.7: R-1, R-2, R-3, R-4, R-5 and R-7 met, checked line by line against the ruling and `venue-index-remediation.md` §11. Corrects the loop in the ruling's lift condition (content, not sign-off). Accepts the PM/BA's stricter P4 reading. Gives S-1 a number and corrects its σ-versus-median units. Records three prose errata for the PM/BA. Blocks 1–3 untouched. **Not a certification.** |

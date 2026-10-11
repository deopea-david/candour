# Cost sheet — Haunts — v3, addendum E: the D69 scope (CAP-15, CAP-16, CAP-17) and the labour at risk from the Block 2 re-scope

**Seat:** Chief Financial Officer · **Date:** 2026-10-11 · **Slug:** `haunt`
**Authority:** D69's "Owed" line, *"the CFO notes the hours and the labour-at-risk (`block-2-review.md` §5)"* (`decisions/2026-09-16-haunt-gate.md`), and `requirements.md` v1.5 §22 item 42. Commissioned by the Coordinator on the CEO's `/coordinator`, 2026-10-11.
**Amends:** `products/haunt/cost-sheet-v3.md` and `products/haunt/cost-sheet-v3-addendum-design.md` (addendum D). **Neither is rewritten.** Every figure this addendum changes is listed in §7, old beside new. When this file is merged, v3 needs a banner pointing here; I have not added it, to avoid a merge conflict. **Owner: the main session, at merge.**
**Status: intended for publication under Constitution 2.1 and Article 3, with v3. It is not a price.** Constitution 5.4: *"The following are never automated: kill/proceed decisions, spending real money, **pricing changes**… Agents prepare; the founder decides."* **D60 holds all three launch prices.** Nothing here changes one. §4 says exactly what the arithmetic touches.
**Evidence:** `pipeline/evidence-standard.md`. **Every hour figure is [J]**: the CTO's judgment, re-added here, not measured. Repository files were read from disk on 2026-10-11 and are cited by path. **No external source was needed, and none was retrieved.** The rate (£32.71), the £3.3985, £3.614 and £1.694118 constants and the Google Play fee are v3's, carried and not re-retrieved.
**Input not yet merged:** the CTO's sizing, `products/haunt/architecture/cap-15-17-sizing.md`, was read from branch `docs/haunt-cap-15-17-sizing` at commit `c7904f1` (PR #42). **If that PR changes the hours, §1 to §4 must be redone.** The formulas below are written so that is a ten-minute job.
**Template note:** as addendum D. It carries only what changes.
**Provenance:** CFO · sonnet (Sonnet 5.5) · effort high · 2026-10-11

---

## 0. The answers

**A. The D69 features add 80.25 h at the point (range 55 to 111), £2,624.98 one-off, to the capitalised build. Ongoing, about 9 h a year (range 4.5 to 15), £294.39.** They are carried as scope added after the estimate, outside the 2,090 h and outside the 75 h spike line, as the CTO asks. The CTO's point and high totals re-add exactly; **his Low total does not (55.0 h, not 55.5 or 56), and an earlier draft of this note wrongly ticked it. Corrected 2026-10-11 after QA's re-derivation (§1).**

**B. The capitalised build goes from 2,777 h (£90,854.37) to 2,857.25 h (£93,479.35). The annual cost base `A` goes from £51,017.93 to £52,187.31: +£1,169.38 a year, +2.3%.** Of that, amortisation is +£874.99 a year (£2,624.98 ÷ 3) and ongoing labour +£294.39. Three-year published cost: £153,053.79 to £156,561.93 (+£3,508.14). §3.

**C. The labour at risk from the Block 2 re-scope is up to 276.25 h (£9,036.14) at the point, range 223 to 334.5 h (£7,294.33 to £10,941.50), if the measurement returns "don't" and Android does not ship.** It is the Android capture layer (5 to 7 weeks), now built before the measurement, plus CAP-16 and CAP-17. **It is a ceiling, not an expected loss, and I have no evidence for a probability.** The 75 h spike (£2,453.25) was already marked at risk in v3 and is not counted again. If the CEO later removes the "Haunts missed this" control (item 40), CAP-15's 29 h (£948.59) joins. §5.

**D. No launch price moves: pay-once £28.99, yearly £9.89 and monthly 99p all stand, by v3's own method.** The cost goes into the volume at which the price is honest, `N*`: 15,012 to **15,356** (+2.3%). At 4,000 subscribers the margin at 99p goes from −44.5% to **−45.4%**. **One unpublished, unfrozen number sits within 2p of a switch: the post-cliff pay-once point would move from £18.90 to £18.49 on my arithmetic.** That is a future step price, not set, not frozen (D60), and the CEO's to fix at v4. I set nothing. §4.

**E. Two things the CTO and I disagree with the record about.** (1) `block-2-review.md` §5's *"the hours are about the same"* is wrong on the arithmetic: 80.25 h against 75 h, and the run is not even sized. I agree with the CTO. (2) CAP-17's classification script (9 h) and result template (2 h) are measurement tooling that never ships in the app. I capitalise them, for consistency with how v3 treated the spike, and flag the choice (§2.2).

**F. CEO decisions: none required.** Two are his to take when convenient: whether to accept the labour risk in §5 (it was flagged to him in `block-2-review.md` §5 and he said yes to D69, but the sum had not been put to him), and the post-cliff point at v4.

---

## 1. Re-deriving the CTO's hours (gate Condition 6)

Source: `cap-15-17-sizing.md` §1.1 to §1.3, `c7904f1`. Each line is Low / Point / High.

| Requirement | Line sums (re-added by me) | Low | Point | High | CTO's total |
|---|---|---:|---:|---:|---|
| **CAP-15** | L: 1.5+3+4+2+3+6 · P: 2+4.5+6+3+4.5+9 · H: 3+6+8+4+6+12 | 19.5 | 29 | 39 | 19.5 / 29 / 39 ✔ |
| **CAP-16** | L: 3+2+5+3+4+8 · P: 4.5+3+7.5+5+6+10 · H: 6+4+10+8+8+15 | 25 | 36 | 51 | 25 / 36 / 51 ✔ |
| **CAP-17** | L: 0.5+1+1.5+6+1.5 · P: 0.75+1.5+2+9+2 · H: 1+2+3+12+3 | 10.5 | 15.25 | 21 | 10.5 / 15.25 / 21 ✔ |
| **Total** | 19.5+25+10.5 · 29+36+15.25 · 39+51+21 | **55.0** | **80.25** | **111** | 56 / 80 / 111 (rounded). **Low ✘: 19.5+25+10.5 = 55.0; the CTO's §0 shows 56 and his Sums line 55.5.** Point and high ✔ |

- **Against the 2,090 h:** 55 ÷ 2,090 = 2.63%; 80.25 ÷ 2,090 = 3.84%; 111 ÷ 2,090 = 5.31%. The CTO's *"+2.7% to +5.3% (+3.8% at the point)"* re-derives at the point and high; **the low is +2.6%, not +2.7%.** The CTO should correct `cap-15-17-sizing.md` §0 and its Sums line. I carry **55.0**.
- **Against today's 2,777 h:** 2.0% / 2.9% / 4.0%.
- **Rounding:** the CTO rounds the point to 80. I carry **80.25**, the sum of his lines, so the sheet re-adds. The 0.25 h is £8.18.
- **Ongoing.** The CTO gives *"about 0.75 to 1.5 h per release"* and *"roughly 5 to 15 h a year at 6 to 10 releases"*. Re-derived: low 0.75 × 6 = **4.5**; high 1.5 × 10 = **15**. **He gives no point; mine is the midpoint, 1.125 × 8 releases = 9 h [J, mine].** The release range is the CTO's assumption from addendum D §1.5, where I found no real cadence; that is unchanged.
- **Plain sums, not a statistical range.** As the CTO says, summing every low and every high overstates the spread. I carry the plain sums so a reader can re-add them, and I price the point.

## 2. What is carried

### 2.1 The table

| | Low | **Point** | High | How |
|---|---:|---:|---:|---|
| One-off hours | 55 | **80.25** | 111 | §1 |
| **One-off at £32.71** | £1,799.05 | **£2,624.98** | £3,630.81 | hours × 32.71 |
| Ongoing hours a year | 4.5 | **9** | 15 | §1 |
| **Ongoing at £32.71 a year** | £147.20 | **£294.39** | £490.65 | hours × 32.71 |
| Ongoing against the 360 h/yr fixed maintenance | +1.3% | **+2.5%** | +4.2% | h ÷ 360 |
| Amortised, a year | £599.68 | **£874.99** | £1,210.27 | one-off ÷ 3 |
| Amortised, a month | £49.97 | **£72.92** | £100.86 | one-off ÷ 36 |

**Cash costs: none.** The CTO flags that CAP-16 may need a share-sheet library (`expo-sharing`) which the CSO must approve; the CTO reads its page as Included in Expo Go with no permissions mentioned [E, as retrieved by the CTO, `cap-15-17-sizing.md` §4; **not re-retrieved by this seat**]. I have found no price for it and no reason to expect one. If a paid dependency appeared it would be a new operating line. **Owner: CSO and CTO.**

### 2.2 Where it sits on the amortisation schedule, and one classification I am flagging

**All of it is launch scope, so it joins v1's line. It does not open one** (Definitions: *"each capitalised increment runs its own clock from the date it ships"*). CAP-15 and CAP-16 build in M2 and CAP-17's app fields with them (CTO §2). If any of it ships after v1, it becomes its own increment with its own clock, and the schedule will show it.

**The classification script and result template are not app code.** CAP-17's line 1.3-4 (the script: 6 / 9 / 12 h) and line 1.3-5 (the result template: 1.5 / 2 / 3 h) are, in the CTO's words, *"measurement tooling for SPK-02, not app code"*. That is 7.5 / 11 / 15 h, £245.33 / £359.81 / £490.65. The Definitions say: *"Labour spent on work that does not ship is not capital: it is an operating cost in the year it is incurred."* **I have capitalised them anyway**, because v3 §3.2 already capitalises the 75 h and 113 h spikes on the stated reasoning that a spike which returns "do" has shipped what it enabled, and treating this tooling differently without a reason would be inconsistent. **That reasoning is arguable and I do not certify it.** The effect of the other reading at the point is £359.81 expensed in one year instead of £119.94 a year for three; `A` in the reference year moves by under £240. **Holder: CGO (constitutional reading), with the CEO. If they say expense it, §3's figures change by the arithmetic in the formula list, and the one-year cost rises.**

## 3. The cost base, restated

### 3.1 Formulas, so another seat can re-derive

```
Hours cost         = hours × £32.71                                     (v3 §3.1)
Capitalised total  = (2,777 + D69 one-off hours) × 32.71 + 18.70        (2,777 and £18.70: addendum D §3.1)
B (amortised/yr)   = Capitalised total ÷ 3                              (D6; Definitions)
F (fixed/yr)       = £20,733.14 + (D69 ongoing hours × 32.71)           (£20,733.14: addendum D §3.2)
A (annual cost)    = B + F
Three-year cost    = 3 × A
```

### 3.2 The result

| | Addendum D (today) | **Low** | **Point** | **High** |
|---|---:|---:|---:|---:|
| Capitalised hours | 2,777 | 2,832 | **2,857.25** | 2,888 |
| Capitalised total | £90,854.37 | £92,653.42 | **£93,479.35** | £94,485.18 |
| `B` | £30,284.79 | £30,884.47 | **£31,159.78** | £31,495.06 |
| `F` | £20,733.14 | £20,880.34 | **£21,027.53** | £21,223.79 |
| **`A`** | **£51,017.93** | £51,764.81 | **£52,187.31** | £52,718.85 |
| Change in `A` | — | +£746.88 (+1.5%) | **+£1,169.38 (+2.3%)** | +£1,700.92 (+3.3%) |
| Three-year published cost | £153,053.79 | £155,294.43 | **£156,561.93** | £158,156.55 |
| Fixed labour a year | 602.25 h | 606.75 h | **611.25 h** | 617.25 h |

*Worked, point: capitalised = 2,857.25 × 32.71 + 18.70 = 93,460.65 + 18.70 = £93,479.35 (2,857.25 × 32.71 = £93,460.6475, rounded). `B` = 93,479.35 ÷ 3 = £31,159.78. `F` = 20,733.14 + 9 × 32.71 (£294.39) = £21,027.53. `A` = 31,159.78 + 21,027.53 = £52,187.31. Check: 51,017.93 + 874.99 + 294.39 = £52,187.31 ✔. Low and high pair each column's low or high one-off hours with its low or high ongoing hours. Figures may differ by 1p from a spreadsheet, from rounding at each step.*

**The amortisation schedule line (Article 2.1), replacing addendum D §3.1's:**

| Increment | Hours | Ship date | Period | Amortised to date | Remaining balance |
|---|---|---|---|---|---|
| **Haunts v1: the whole launch build** | **2,857.25 h** (point; was 2,777) = £93,460.65, plus £18.70 Google Play registration = **£93,479.35** | Not yet set | 36 months | £0.00 | **£93,479.35** |
| *of which added after the CTO's 2,090 h estimate* | *767.25 h: addendum D's 687 + D69's 80.25* | | | | |

*(2,090 + 767.25 = 2,857.25 ✔. 687 is addendum D §3.1: Block 4 R-5 22.5; spikes 75 + 113; design 364; heatmap 75; headlines 37.5.)* **Capitalised hours as a share of all hours worked: still cannot be published**, for the reason v3 §3.3 gives (hours are not recorded; D35 begins that). **Recorded hours so far: 0.**

**The statement Article 2.1 requires, repeated because it must be on the face of the sheet:** the three-year period is a company-wide accounting convention and **not a statement about how long Haunts will be supported.** No support date is committed (D4).

## 4. Does any price move?

### 4.1 Launch prices: no, and they cannot, under the method

**Pay-once £28.99, yearly £9.89, monthly 99p. D60 holds them, and only the CEO changes a price (5.4).** The arithmetic agrees: v3 §7.1 shows that at `N*` the fixed-cost share per subscriber, `A/N*`, is always £3.3985, so a bigger `A` moves `N*` and leaves the prices at `N*` where they were. The margin of each tier at `N*` is unchanged (16.51%, 16.91%, 16.50%).

> **Said plainly, as addendum D §4.1 said it, because a method that never raises a price when costs rise should be looked at hard.** Added scope raises the volume at which the price is honest. It does not raise the price. Below `N*` the gap widens. That is honest only because both numbers are published here.

### 4.2 The volumes (formulas from addendum D §4.2; each scales with `A`)

| | Today (addendum D) | Low | **Point** | High |
|---|---:|---:|---:|---:|
| `N*` = A ÷ 3.3985 | 15,012 | 15,232 | **15,356** | 15,512 |
| 99p covers its cost: A ÷ 4.801 | 10,627 | 10,782 | **10,870** | 10,981 |
| Pay-once at £28.99 covers its cost: 3A ÷ 13.617 | 11,240 | 11,404 | **11,498** | 11,615 |
| Monthly 99p reaches the 30% cap (scaled by A ÷ 51,017.93) | 20,274 | 20,571 | **20,739** | 20,950 |
| Pay-once buyers a month over 36 months | 312 | 317 | **319** | 323 |

### 4.3 Margin at 99p, Deviation 2, restated

Formulas (v3 §6): `C = A/N + 3.614`; honest monthly price = `C × 1.694118 ÷ 12`; margin = `(8.415 − C) ÷ (C + 1.485)` (annual, at 99p a month: 0.85 × 9.90 = 8.415; 0.15 × 9.90 = 1.485).

| Subscribers | Today | **Point** | Low | High |
|---|---:|---:|---:|---:|
| Realised margin at 99p, 4,000 | −44.5% | **−45.4%** | −45.1% | −45.8% |
| Honest monthly price, 4,000 | £2.31 | **£2.35** | £2.34 | £2.37 |

*Worked, point, 4,000: `C` = 52,187.31 ÷ 4,000 + 3.614 = 13.0468 + 3.614 = 16.6608; margin = (8.415 − 16.6608) ÷ (16.6608 + 1.485) = −8.2458 ÷ 18.1458 = −45.44%. Honest monthly = 16.6608 × 1.694118 ÷ 12 = £2.352.*

**Against Article 2.1: no price is forced to move.** The 30% cap moves further away (20,739). The ~20% target was already missed below `N*` on the CEO's written justification (v3 §6.1, Deviation 2), and **that deviation is 0.9 points deeper at 4,000 subscribers** (the gap to target: 65.4 points, was 64.5). Nothing in Article 2.1 ties a justification to the size of a deviation, so D60's acknowledgement stands. I do not ask for a second one: the increase is under one point. D60's reasoning (features chosen knowingly) applies, though D60 itself was about the design scope. Stated so a reader sees it was noticed.

### 4.4 The one place the arithmetic touches a price: D15's step points (not set, not frozen)

D60: *"The D15 step-down figures are not frozen until the launch cost sheet (v4)."* Formula (v3 §11.2, as addendum D §5.3 used it): honest price in year k = `[3 × (F/N* + 2.306) + (build years left) × (B/N*)] × 1.694118`, `N*` = A ÷ 3.3985. Re-run on today's `A` it reproduces addendum D's 25.575, 22.157 and 18.739 ✔.

| Step | Addendum D honest → point | **This addendum: honest** (point; low–high) | Nearest point, same rule |
|---|---|---|---|
| Launch | 28.992 → £28.99 | 28.992 | **£28.99** unchanged |
| M1 (a third recovered) | 25.575 → £25.49 | **25.555** (25.553–25.557) | **£25.49**, unchanged |
| M2 (two thirds recovered) | 22.157 → £22.00 | **22.117** (22.113–22.122) | **£22.00** (11.7p) against £21.99 (12.7p), unchanged |
| Post-cliff pay-once | 18.739 → £18.90 | **18.679** (18.674–18.687) | **£18.49** (18.9p) against £18.90 (22.1p). **Moves, by 2p** |
| Post-cliff monthly | 70.5p → 69p | 70.4p | **69p** (30.3% cut), unchanged |
| Post-cliff yearly | 6.431 → £6.39 | 6.411 | **£6.39**, unchanged |
| D15 recovery thresholds (B and 2B) | £30,284.79 / £60,569.58 | **£31,159.78 / £62,319.56** | rise with the build |

*Worked, post-cliff pay-once, point: `N*` = 52,187.31 ÷ 3.3985 = 15,356.0; `F/N*` = 21,027.53 ÷ 15,356.0 = 1.3693; honest = 3 × (1.3693 + 2.306) × 1.694118 = 3 × 3.6753 × 1.694118 = £18.679. Midpoint between £18.49 and £18.90 is £18.695; all three cases sit 0.8p to 2.1p below it (point 1.6p).*

**Sensitivity to the ongoing-hours assumption (added after QA's re-derivation; QA found the fragility and I had not stated it).** The 9 h a year is my own midpoint; the CTO gave no point (§1). Holding one-off hours at the point (80.25 h) and varying ongoing hours, with `F` = 20,733.14 + hours × 32.71:

| Ongoing h/yr | 4.5 (CTO low) | **9 (mine)** | 11 | 12 | 15 (CTO high) |
|---|---:|---:|---:|---:|---:|
| Honest post-cliff pay-once | £18.650 | **£18.679** | £18.692 | £18.699 | £18.718 |
| Nearest point | £18.49 | **£18.49** | £18.49 | £18.90 | £18.90 |

**The switch to £18.49 holds only while ongoing hours stay below about 11.4 a year** (solved: honest = £18.695 at 11.42 h; QA rounds it to 11.5). That sits between my midpoint and the CTO's high of 15. **The crossover also depends on the one-off hours:** at the Low one-off (55 h) it is about 5.7 h a year, so Low one-off with my 9 h of ongoing gives £18.90 and not £18.49; at the High one-off (111 h) it is about 18.4. The low–high range in the table above pairs low with low and high with high, which is why it does not show this. **Read the £18.49 as one outcome of a coin the inputs have not yet tossed, not as a finding.**

> **How much weight this carries: little, and I say so.** The switch rests on a 1p to 2p margin, on £18.49 existing in App Store Connect and Play Console (v3 §7.2's grid check is still owed, addendum D flag D-F8), and on a cost base that SPK-08 is about to move again (addendum D §6: still unsized, up to about 36% above v3). **I would not publish or freeze any step point on today's numbers.** That is addendum D §5.3's recommendation and D60 already adopts it. **It is the CEO's price, at v4.** I raise it because the commission said to stop and say so if the figures would move a price. **They do not move a launch price. They would move one future step, if frozen today.**

## 5. The labour at risk from the Block 2 re-scope

### 5.1 What changed and what is exposed

`block-2-review.md` §4 moved Block 2 from *"before Android code"* to *"before the Android release build"*. The block's old placement meant **no Android capture labour was exposed to the measurement result.** The new placement lets the Kotlin capture layer be built first, as the instrument the measurement needs. The CTO states the cost in his §3 ("Lift at a later point"): *"if the result is bad, part of the Android capture layer (sized at 5-7 weeks) may need redesign. Labour on work that does not ship is written off as a cost in the year (Constitution, Definitions, 'Cost'). Accepting that risk is the CEO's call."* **This section puts numbers on it. It sets no price and decides nothing.**

**Treatment if the measurement returns "don't" and Android does not ship** (Definitions, *"Cost"*; v3 §3.2): the exposed hours leave the capitalised table and are expensed in the year they are incurred. Nothing here is a cash cost: it is labour valued at the benchmark.

### 5.2 The hours

| Item | Low | **Point** | High | £ at point | Basis | Survives a "don't"? |
|---|---:|---:|---:|---:|---|---|
| **Android capture layer** (Kotlin: Activity Recognition, location, foreground service, boot resilience, per-OEM) | 187.5 | **225** | 262.5 | £7,359.75 | 5 to 7 weeks × 37.5 h/week; `android-and-stack-note.md` §1.7 and §3.2 row 3. **Point is my midpoint (6 weeks) [J, mine]** | **Not if Android is dropped. If it is only reworked, "part" of it** (the CTO's word; no share given) |
| **CAP-16**, counts-only summary | 25 | **36** | 51 | £1,177.56 | CTO §1.2 | **Mostly not** (CTO §3) |
| **CAP-17**, in-app diary | 10.5 | **15.25** | 21 | £498.83 | CTO §1.3 | **Mostly not** (CTO §3) |
| **Exposed by the re-scope and D69** | **223** | **276.25** | **334.5** | **£9,036.14** | sum of the three rows | |
| *In addition, if item 40 removes the control:* **CAP-15** | 19.5 | 29 | 39 | £948.59 | CTO §1.1; §22 item 40 | Yes, if the control stays (item 40) |
| *Already marked at risk in v3 §3.2, not counted again:* **the 75 h Android spike** | 75 | 75 | 75 | £2,453.25 | v3 §3.2 | Treated as in v3 |

*(Low, point, high: 187.5+25+10.5 = 223; 225+36+15.25 = 276.25; 262.5+51+21 = 334.5. £: 276.25 × 32.71 = £9,036.14; 223 × 32.71 = £7,294.33; 334.5 × 32.71 = £10,941.50. With the spike: 351.25 h, £11,489.39.)*

**What this is in proportion.** 276.25 ÷ 2,857.25 = **9.7% of the capitalised build.** Expensed in one year, £9,036.14, with `B` falling by £3,012.05 a year as the hours leave the capital line (9,036.14 ÷ 3). **That fall is not a saving.** The hours were worked, and if Android did not ship, the revenue side changes too. I have not modelled Android being abandoned and I do not present `A` after a write-off as a number to price on.

### 5.3 What I do not know, and what would change it

- **How likely "don't" is.** The CTO says the measurement *"can still return 'don't', but it is not research into an unknown mechanism"* (`block-2-review.md` §0). **I have no pass rate and I do not invent one.** The figures above are what is exposed, not what is expected to be lost.
- **How much of the Android layer a bad result would force a rewrite of.** The CTO says "part" and gives no share. **Owner: CTO.** A share would turn a ceiling into a range.
- **Whether the 5 to 7 weeks is still right.** It comes from the 1,330 h decomposition. I searched `subscription-sizing-note.md`, `design-feasibility-and-sizing.md` and `block-2-review.md` and found no re-size. **Where I looked** is that list. A different figure would overturn the first row.
- **Whether CAP-16 and CAP-17 survive after the measurement.** D69 says the features serve the measurement *"and beyond"*, and item 40 covers only CAP-15. If either is removed after release, the Definitions do not say how labour is treated on a feature that shipped and was then removed. Item 42 treats removal as a write-off. **Flagged to the CGO** as a reading to settle before it happens.
- **Possible overlap with the 75 h spike.** `block-2-review.md` §5 says the 75 h line *"becomes a measurement run plus a little in-app tooling"*. The CTO has not re-sized the run, and `android-and-stack-note.md` does not break the 75 h down. **I add the D69 hours on top and do not reduce the 75 h.** That may overstate by whatever part of the 75 h was throwaway tooling now replaced. I will not guess a reduction in the product's favour (addendum D §1.4 took the same line).

### 5.4 A negative finding, with what would overturn it

| Finding | What would overturn it | Where I looked |
|---|---|---|
| **The CTO's "the hours are about the same" does not hold** | A breakdown of the 75 h showing the in-app tooling inside it | `cap-15-17-sizing.md` §3; `android-and-stack-note.md` §0.3 and §3.2 (no breakdown found); `block-2-review.md` §5 |
| **No launch price is affected** | A change to the pricing rule, to `A/N*`, or a CEO decision (5.4). A cost increase alone cannot do it | v3 §6 and §7.1; addendum D §4.1 and §5; D60 |
| **The risk is exposure, not expectation** | A pass rate, a measured redesign share, or the result itself | `block-2-review.md` §0, §3, §5 |

## 6. What is not in this addendum

- **The measurement run itself** (carrying the phones, protocol, QA's analysis, publication). The CTO has not sized it (§3). It is probably inside the 75 h, and I do not know. **Owner: CTO.**
- **Non-engineering labour**, including the CFO's, UX's, CGO's and QA's review hours on D69 (CTO: *"not included"*), and the volunteer beta's recruitment. v3 §4.4 and addendum D §6 already name non-engineering labour as uncarried. **CEO's recorded hours (D35) are the remedy.**
- **Everything SPK-08 still holds.** Addendum D §6's list stands, and its +625 h sensitivity is unchanged by this note.
- **Android's other exposure.** Play policy work (1 to 2 weeks) and the device-matrix field testing in `android-and-stack-note.md` §3.2 rows 13 and 14 mix both platforms and have no stated Android share. **Not quantified; named.**

## 7. Figures this addendum supersedes

| Where | Before | Now (point) |
|---|---|---|
| Addendum D §3.1, capitalised hours and value | 2,777 h, £90,854.37 | **2,857.25 h, £93,479.35** |
| Addendum D §3.2, `B`, `F`, `A` | £30,284.79; £20,733.14; £51,017.93 | **£31,159.78; £21,027.53; £52,187.31** |
| Addendum D §3.2, three-year cost | £153,053.79 | **£156,561.93** |
| Addendum D §3.2, fixed labour | 602.25 h/yr | **611.25 h/yr** |
| Addendum D §4.2, `N*` | 15,012 | **15,356** |
| Addendum D §4.2, 99p covers cost; pay-once covers cost | 10,627; 11,240 | **10,870; 11,498** |
| Addendum D §4.3, margin at 99p, 4,000 | −44.5% | **−45.4%** |
| Addendum D §5.3, D15 thresholds | £30,284.79 / £60,569.58 | **£31,159.78 / £62,319.56**, not frozen until v4 |
| Addendum D §5.3, post-cliff pay-once (nearest point) | £18.90 | **£18.49**, a 2p switch, not frozen |
| Addendum D §3.1, added after the estimate | 687 h | **767.25 h** |

**Unchanged:** every launch price; M1 £25.49, M2 £22.00; post-cliff monthly 69p and yearly £6.39; the benchmark (£32.71); variable costs; the 90-day notice (D14(b)); and the method throughout.

## 8. Disclosures, flags and change log

**Related-party disclosures: none new.** The added labour is founder and agent labour valued at the benchmark and not drawn; Article 2.1 requires it regardless (*"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)"*).

**Blocks: none.** My power is *"Launch of any pricing not backed by a published cost sheet; any proposal without a credible cost model."* Every sized item is carried, every unsized one is named (§6), and the risk is stated with its basis and its gaps. **The cost model is credible in the charter's sense. D69 stands.**

**Flags, each with the seat that holds it:**

| # | Flag | Holder |
|---|---|---|
| E-F1 | **The risk in §5 should be put to the CEO as a number, once.** `block-2-review.md` §5 flagged it, and D69 answered the feature, not the exposure. This section is the number | Coordinator, for the CEO (5.4) |
| E-F2 | **A one-line erratum to `block-2-review.md` §5** (*"the hours are about the same"*), if wanted. The CTO has said he will not edit a merged memo | Coordinator |
| E-F3 | **The share of the Android capture layer that a bad result would force a rewrite of**, which turns §5's ceiling into a range | CTO |
| E-F4 | **Classification of measurement tooling (CAP-17 script and template, 11 h) as capital** (§2.2) | CGO, with the CEO |
| E-F5 | **Treatment of a feature that ships and is later removed** (CAP-16 and CAP-17, or CAP-15 under item 40): the Definitions are silent | CGO |
| E-F6 | **Do not publish or freeze D15 step points before v4.** The post-cliff pay-once point is within 2p of a switch (§4.4). Grid check for £18.49 still owed (v3 §7.2) | CEO, with the CFO at v4 |
| E-F7 | **PR #42 is unmerged.** If the CTO's hours change, redo §1 to §4 | CFO |
| E-F8 | **Re-derivation by a seat other than the CFO** is owed under gate Condition 6. The formulas in §3.1 and §4.3 are enough to do it by hand | Coordinator to assign |

**Where I looked:** `constitution.md` (Definitions, Articles 2.1, 4, 5.4); `roles/cfo.md`; `pipeline/evidence-standard.md`; `products/haunt/cost-sheet-v3.md` §3.2, §3.3, §6, §7, §11; `products/haunt/cost-sheet-v3-addendum-design.md` in full; `decisions/2026-09-16-haunt-gate.md` D6, D60, D69; `products/haunt/architecture/block-2-review.md` §0, §3, §4, §5; `products/haunt/android-and-stack-note.md` §1.7, §3.2; `products/haunt/requirements.md` §22 items 40 to 43; and the CTO's `cap-15-17-sizing.md` at `c7904f1` (all). **Not read:** `pipeline/model-selection.md` (the commission states the model rule); `m1-wave-plan.md`; the CSO's dependency rulings. **Looked for and not found:** a breakdown of the 75 h; a re-size of the Android capture layer; a real release cadence; a pass probability for the measurement.

### Change log

| Date | Change |
|---|---|
| 2026-10-11 | **Corrected after QA's Condition 6 re-derivation (PR #45):** the Low one-off total is 55.0 h, not 55.5 (the CTO's own Sums line carried the same slip). Low column restated: one-off £1,799.05; `A` £51,764.81; `N*` 15,232. Point and high unchanged. Added the ongoing-hours sensitivity of the D15 post-cliff point (§4.4): the switch holds only below about 11.4 h a year. |
| 2026-10-11 | **Created (D69 "Owed").** Re-adds the CTO's sizing (Low corrected in the row above): **80.25 h at the point (55 to 111), £2,624.98 one-off, plus about 9 h a year (4.5 to 15), £294.39**, carried as post-estimate scope outside the 2,090 h and the 75 h spike line. Capitalised build 2,777 → **2,857.25 h**; `A` £51,017.93 → **£52,187.31 (+2.3%)**; `N*` 15,012 → **15,356**; margin at 99p and 4,000 subscribers −44.5% → **−45.4%**. **Labour at risk from the Block 2 re-scope: up to 276.25 h, £9,036.14 (223 to 334.5 h)**, a ceiling and not an expectation, plus the 75 h spike already carried. **No launch price changes (D60).** One unfrozen future step point, the post-cliff pay-once price, sits within 2p of a switch from £18.90 to £18.49; not set, for the CEO at v4. **Not a price: Constitution 5.4 reserves pricing to the CEO.** |

*Prepared by the Chief Financial Officer under `roles/cfo.md`. It prepares and flags; it does not certify (Constitution 6.1).*

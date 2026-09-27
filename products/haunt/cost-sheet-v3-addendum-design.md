# Cost sheet — Haunts — v3, addendum D: the design scope (SPK-17) and other scope carried since v3

**Seat:** Chief Financial Officer · **Date:** 2026-09-27 · **Backlog key:** SPK-17 (and, in part, SPK-09)
**Amends:** `products/haunt/cost-sheet-v3.md` (2026-09-21/22, with its §20 addendum). **v3 is not rewritten.** Every v3 figure this addendum changes is listed in §7, with the old and the new value side by side. When this file is merged, v3 needs a one-line banner under its title pointing here. I have not added it in this branch, because v3 may also be edited on the coordinator's branch and a banner is not worth a merge conflict. **Owner: the main session, at merge.**
**Status: intended for publication under Constitution 2.1 and Article 3, with v3. It is not a price.** Constitution 5.4: *"The following are never automated: kill/proceed decisions, spending real money, **pricing changes**… Agents prepare; the founder decides."* Nothing below changes a price. §5 recommends that none change.
**Evidence:** tagged under `pipeline/evidence-standard.md` v1.1. Hours are **[J]** throughout: they are other seats' judgments, carried and re-derived, not measured. Every external figure was **retrieved by this seat on 2026-09-27**, with the link given where the claim is made. Where I rely on another seat's retrieval, I say so and do not present it as mine. Constitutional claims quote the clause in the same passage.
**Template note:** as v3 (§0, template note). This is an addendum, so it carries only the elements that change: itemised cost, the amortisation line, price and margin, deviations, and a change log. There are no new related-party items (§8).

---

## 0. The answers

**A. Addendum or v4? An addendum, and v4 is due when the CTO's SPK-08 sizing lands.** Three reasons. (1) **No launch price changes** (§5). (2) **The method is unchanged**: same benchmark, same rule, same amortisation, same reference-volume logic. (3) **The cost base is still moving.** SPK-08 is due to size headlines, photos, the recap, imports and more, and a v4 issued today would be superseded within weeks. **The launch cost sheet should be v4, built once SPK-08 has landed.** That is also when D15's step prices and thresholds get frozen, which guardrail 2 requires before first sale (§5.3).

**B. The CTO's design scope, net of Native Tabs and D54/D55: 364 h one-off (range 248–519), £11,906.44 at £32.71. Plus about 72 h a year ongoing (range 38–124), £2,363.30 a year.** The CTO's one-off sums re-derive exactly (§1). **Two things did not reconcile, and neither changes a decision.** First, the CTO's ongoing point of "≈ 76 h/yr" cannot be reproduced from his own ranges: midpoints give 79. Second, **the commission's framing, "saves about 12 h… Retro's own bar adds about 15 h", double-counts if you add both.** The 12 h saving is already net of Retro's bar. The net is **364 h, not 379 h** (§1.3).

**C. With the other scope now sized or estimated since v3 added in, the total is 476.5 h one-off (£15,586.32) and 82.25 h a year (£2,690.40).** The two additions are the heatmap's offline basemap, at 55–95 h plus 8–12 h a year (the CTO, `map-options-comparison.md`, carried at D22's instruction), and the headline system HEAD-1…18, at UX's 4–6 days (30–45 h). The CTO says UX's figure *"stands until"* SPK-08. **Capitalised build hours go from 2,300.5 to 2,777 (+20.7%).** §2.

**D. The annual cost base rises from £43,132.09 to £51,017.93 (+18.3%). The design scope alone accounts for £6,332.11 of that (+14.7%).** Three-year published cost goes from £129,396.27 to £153,053.79. §3.

**E. No launch price moves: pay-once £28.99, yearly £9.89 and monthly 99p all stand.** That follows from the pricing method, and I state its consequence plainly so it is not mistaken for good news. **The added cost does not raise the price. It raises the volume at which the price is honest**, from 12,692 subscribers to **15,012** (+18.3%). At every volume below that, the below-cost gap is wider. **At 4,000 subscribers the realised margin at 99p goes from −37.7% to −44.5%, and the honest monthly price from £2.03 to £2.31.** §4.

**F. Against Article 2.1: no price is forced to move in either direction.** The 30% cap moves further away: 99p now reaches it at 20,274 subscribers, not 17,140. The ~20% target was already missed below the reference volume, on the CEO's written justification (Deviation 2). That justification is not limited by size, and **the deviation is now larger.** §4.3, §5.

**G. Three downstream figures do move, and none is yet published.** At the reference volume, **D15's second step goes from £22.49 to £22.00**, and the post-cliff pay-once price goes from £18.95 to £18.90. **Both depend on the Apple grid check v3 §7.2 still owes.** The post-cliff yearly price goes from £6.49 to £6.39. The **D15 recovery thresholds rise from £25,089 and £50,179 to £30,285 and £60,570**. **The post-cliff monthly 69p and its 30.3% cut do not move.** §5.2, §5.3.

**H. Reach, the binding constraint, gets 18% harder.** Pay-once at a flat £28.99 needs **11,240 buyers** (312 a month for three years), up from 9,503. The subscription needs **73,568 distinct subscribers** at the central tenure, up from 62,197. §4.4.

**I. What is still not costed is larger than what this addendum adds.** It covers the rest of SPK-08 (photos, the recap and its image, competitor import, onboarding, thumbnail backup, the area field behind the *Neighbourhood* template, the §4.2 five), plus all non-engineering labour. **On v3's own sensitivity, +625 h, that would take the reference volume to about 17,200.** §6.

**J. CEO decisions: none is required. One is recommended, and there is one clarification.** (1) **Recommended:** acknowledge in writing that Deviation 2 is now larger because of scope he chose, and hold the prices (§5.4). (2) **Clarification:** does D54's *"each iOS release"* include Apple's x.y.z bug-fix releases? I assume it does not (§1.4). Either way the answer is worth about £100–£250 a year.

---

## 1. Re-deriving the CTO's hours (gate Condition 6)

Source: `products/haunt/design-feasibility-and-sizing.md` (CTO, 2026-09-27), §0, §5, §6 and §10, read from disk in the coordinator's worktree `agent-ad75fb7ff8b8f2f2e`. Decisions D38 and D42–D58 were read from `decisions/2026-09-16-haunt-gate.md` in that worktree. **All hours are the CTO's [J].** What follows re-derives his arithmetic and does not second-guess his judgment.

### 1.1 The one-off table (§5): re-derives exactly

| # | Item | Low | Point | High |
|---|---|---:|---:|---:|
| 1 | Theme machinery | 32 | 44 | 60 |
| 2 | Appearance screen | 14 | 20 | 28 |
| 3 | Theme test harness | 12 | 18 | 26 |
| 4 | Fonts | 10 | 15 | 22 |
| 5 | Mono beyond the base | 10 | 16 | 24 |
| 6 | Warm | 20 | 30 | 42 |
| 7 | Retro | 40 | 56 | 76 |
| 8 | Floating bar, custom *(custom route)* | 16 | 24 | 34 |
| 9 | Real glass on iOS *(custom route)* | 14 | 22 | 32 |
| 10 | Rotate (Warm) | 8 | 12 | 18 |
| 11 | Typed headline (Mono) | 12 | 18 | 26 |
| 12 | Template additions (D50) | 30 | 45 | 65 |
| 13 | Contour texture | 4 | 6 | 10 |
| 14 | App-icon setting | 28 | 40 | 56 |
| 15 | Alternate icon artwork | 6 | 10 | 16 |
| | **Sum, re-derived** | **256** | **376** | **535** |

*Low: 32+14+12+10+10+20+40+16+14+8+12+30+4+28+6 = 256. Point: 44+20+18+15+16+30+56+24+22+12+18+45+6+40+10 = 376. High: 60+28+26+22+24+42+76+34+32+18+26+65+10+56+16 = 535.* ✔ All three agree with the CTO.

The ratios check too. 256 ÷ 2,090 = 12.2%, 376 ÷ 2,090 = 18.0% and 535 ÷ 2,090 = 25.6%, matching *"+12% … +18% … +26%"*. UX's own rows, converted at 7.5 h a day, sum to 199–317.5 h. The CTO's *"≈ 200–320 h"* and *"about 1.3–1.7×"* (256 ÷ 199 = 1.29; 535 ÷ 317.5 = 1.69) both re-derive. ✔

**The CTO's note on the spread is fair and I adopt it.** A plain sum of every low and every high overstates the range, because the items will not all land at an extreme together. I carry the plain sums anyway, so a reader can re-derive them, and I use the point estimate for everything priced.

### 1.2 The Native Tabs adjustment (§10.3): re-derives exactly

- **The custom route**, #8 + #9: 16 + 14 = **30**, 24 + 22 = **46**, 34 + 32 = **66**. ✔
- **Option A**, Native Tabs for Warm and Mono plus Retro's own bar on both platforms: set-up (6 / 10 / 14) + Retro bar (12 / 18 / 26) + device work (4 / 6 / 10) = **22 / 34 / 50**. ✔
- **Option B**, the system bar in Retro's colours as well: set-up (6 / 10 / 14) + device work (4 / 6 / 10) + Retro colour measurement (2 / 3 / 5) = **12 / 19 / 29**. ✔
- **Saving under A**: 30 − 22 = **8**, 46 − 34 = **12**, 66 − 50 = **16**. **Under B**: 18 / 27 / 37. ✔
- **A costs more than B by** 34 − 19 = **15 h** at the point. That is the *"about 15 h"* D54 records. ✔
- **Revised total under A**: 256 − 8 = **248**, 376 − 12 = **364**, 535 − 16 = **519**. ✔ Matches §10.3.

### 1.3 Which option the decisions select, and the double count to avoid

- **D53** adopts Native Tabs. **D54(2)**: *"Retro has its own small bevelled tab bar over the hidden system bar… (the CTO's estimate: about 15 h more than the system bar in Retro's colours)… Warm and Mono use the system bar."* **That is option A.**
- **D55**: *"The floating pill (12–20 h more, as our own component) is not built… Retro's own bar (D54) applies on both platforms."* **So nothing is added back for Android.** Option A's Retro bar row is already *"(both platforms)"* (§10.3).

> **The one-off design scope is therefore 248 / 364 / 519 h.** It can be reached two ways that agree: 376 − 12 (option A's saving) = **364**, or 376 − 27 (option B's saving) + 15 (D54's Retro bar) = **364**.
>
> **What would be wrong: 376 − 12 + 15 = 379.** The 12 h saving is option A's, and option A already contains Retro's bar. Adding D54's 15 h on top counts the Retro bar twice. The commission's wording, *"saves about 12 h … Retro's own bar adds about 15 h per D54"*, invites that sum. **I record it so no later sheet makes it.** It is 15 h, or £490.65. The point is a correct sheet, not the money.

### 1.4 Ongoing hours (§6, then §10.3, then D53 and D54)

**The CTO's §6, re-derived.** Per release: visual pass 3–6, glass device check 1–2, motion renderers 0.5–1.5, icon switch 0.5–1. **Total 5–10.5 h.** ✔ Per year: 10–24 h. At 6–10 releases a year: **low 6 × 5 + 10 = 40; high 10 × 10.5 + 24 = 129**, which he rounds to 130. ✔ Against 360 h/yr: 40 ÷ 360 = 11.1%, 130 ÷ 360 = 36.1%. ✔

**The one figure that does not re-derive: *"point ≈ 76 h/yr"*.** The CTO's §6 table has no point column. Midpoints give 7.75 h × 8 releases + 17 h = **79 h/yr**. I could not find a combination of his stated midpoints that gives 76. **The difference is 3 h, or £98 a year, and it changes nothing.** It is recorded under Condition 6 because the reason for re-deriving is to report what does not reproduce, however small. **I carry 79 as the pre-adjustment point**, because it is the one I can show.

**What Native Tabs and D53/D54 change.** §10.3 says the glass check becomes *"a contrast spot-check of our tints on Apple's glass (0.5–1 h)"* per release. **D53 then moved the check off the Haunts release cycle entirely**: *"once per bar-colour choice or change, not every release."* **D54(1) put it back on a different cycle**: *"also runs on each **iOS** release"*, meaning Apple's releases, not Haunts'. So:

- **The per-Haunts-release glass check (1–2 h) goes, entirely.** The one-off device work covers the check on each colour choice (§10.3, "Device work", in the 364).
- **A per-iOS-release contrast check (0.5–1 h) comes in**, paced by Apple.

**How many iOS releases a year.** Apple's *About iOS 18 Updates* lists, in the iOS 18 cycle up to 18.6.2, **seven major or minor versions** (18, 18.1 … 18.6) and **eight bug-fix versions** (18.0.1, 18.1.1, 18.2.1, 18.3.1, 18.3.2, 18.4.1, 18.6.1, 18.6.2) [E, [Apple Support 121161](https://support.apple.com/en-us/121161), retrieved 2026-09-27. **Single source by nature.** The page gives no per-version dates. That these 15 fell in one twelve-month cycle, before iOS 26 shipped with 18.7, is [K, high confidence]. Versions 18.7.x are security updates for devices that stayed on iOS 18, and are irrelevant to an iOS-26-minimum app (D23)]. **I assume "each iOS release" means the seven x.y releases**, because that is where Apple changes appearance. Bug-fix releases rarely do [J]. **At 15 a year, the high column below applies.** That is the clarification at §0-J.

**The revised ongoing design hours:**

| Component | Low | Point | High | Basis |
|---|---:|---:|---:|---|
| Per Haunts release: visual pass 3–6 + motion renderers 0.5–1.5 + icon switch 0.5–1 | 4 | 6.25 | 8.5 | CTO §6, glass check removed per D53 |
| × Haunts releases a year | 6 | 8 | 10 | CTO's assumption. §1.5 |
| **= per-release subtotal** | **24** | **50** | **85** | |
| Per-iOS-release contrast check, 0.5–1 h × iOS releases | 3.5 (7 × 0.5) | 5.25 (7 × 0.75) | 15 (15 × 1) | D54(1); count [E] above |
| Annual OS and Expo SDK allowance | 10 | 17 | 24 | CTO §6. **Not reduced**: §10.3 says it *"falls a little"* but gives no figure, and I will not invent one in the product's favour |
| **Ongoing design total, h/yr** | **37.5** | **72.25** | **124** | |

**Against the CTO's pre-adjustment 40 / 79 / 129 (re-derived), the net saving is 2.5 / 6.75 / 5 h a year.** That is consistent with the commission's *"about 1 h per release"*: 1.5 h saved × 8 releases = 12 h, less the 5.25 h of iOS-release checks = 6.75 h. ✔

**The CTO's §6 "per new screen after launch, +25–40% UI cost" is not annualised**, because no roadmap exists to annualise it against. It is real, though: **every future feature carries a three-theme, two-mode surcharge.** It will appear in the hours of each future increment, and each increment's own amortisation line (v3 §3.3) is where a reader will see it.

### 1.5 "Replace the CTO's assumed release cadence with the real one" (SPK-17). **I cannot, because there is no real one.**

**Where I looked:** `requirements.md` (VEN-19, PRICE-9, §22), `backlog-plan.md` §10, `android-and-stack-note.md`, the decision record D1–D58, and v3. **The only documented cadence is VEN-19**: *"The bundled index is refreshed quarterly… inside app updates"* [E, `requirements.md` §7.6, read from disk 2026-09-27]. **That is a floor of four releases a year, not a cadence.** No seat has set a release plan, and none can before the product exists.

**So the 6–10 range stays, and the floor case is shown.** At 4 releases a year, the ongoing design point would be 4 × 6.25 + 5.25 + 17 = **47.25 h/yr** instead of 72.25. **What would overturn this:** a release process document, as VEN-19 requires (*"The release process documents the cadence"*), or a year of actual releases. **Owner: CTO, with the release process.** It is re-costed from actuals at the first annual review, as v3 §16.3 requires for all hours.

---

## 2. Everything carried by this addendum

### 2.1 The design scope (SPK-17)

| | Low | **Point** | High |
|---|---:|---:|---:|
| One-off hours (§1.3) | 248 | **364** | 519 |
| **One-off at £32.71** | £8,112.08 | **£11,906.44** | £16,976.49 |
| Ongoing hours a year (§1.4) | 37.5 | **72.25** | 124 |
| **Ongoing at £32.71 a year** | £1,226.63 | **£2,363.30** | £4,056.04 |
| Against the 2,090 h build | +11.9% | **+17.4%** | +24.8% |
| Against the 360 h/yr maintenance | +10.4% | **+20.1%** | +34.4% |

**Cash costs from the design scope: none that is committed.** Fonts are OFL-licensed and bundled, at **£0** [E, as retrieved by the CTO: OFL FAQ 1.4, `design-feasibility-and-sizing.md` §4.2 and E31. **Not re-retrieved by this seat**]. The subsetting question is SPK-18's (CGO). `expo-glass-effect` and Native Tabs are part of Expo: **£0**, and no new metered service. The fonts add about 3.3 MB to the app. **Haunts has no server, so app size costs Candour nothing.** It costs the customer storage, which UX and the CTO own. **One possible cash cost is named, not priced:** D38(5) says *"Paying for final artwork is a separate CEO decision"*. If he decides to pay, it is a real cost, and because the artwork ships it is capital. **No figure exists, so none is carried** (§6).

### 2.2 Other scope sized or estimated since v3, carried now

| Item | Decision | Low | **Point** | High | h/yr | Who sized it | Why carried now |
|---|---|---:|---:|---:|---:|---|---|
| **Heatmap basemap: OS Open Zoomstack, store-delivered pack, MapLibre** (LOOK-2) | D22 | 55 | **75** | 95 | **8–12 (10)** | CTO, `map-options-comparison.md`, *"For the CFO… **Carry 55–95 hours**"* [J] | D22: *"the heatmap's **55–95 hours**, for the CFO to carry."* An explicit instruction to this seat |
| **Headline system** HEAD-1…18: the Line, the Card, the crawl, the pause control, the fallbacks | D20, D24–D26 | 30 | **37.5** | 45 | — | **UX**, 4–6 days [J], `requirements.md` headline section: *"not sized by the CTO"* | The CTO's note says *"UX's 4–6 d stands until"* SPK-08. **The design motion work (#10, #11, the templates) is sized as additions to this system. Costing the additions while carrying the base at zero would be incoherent.** Labelled as UX's figure, and replaced by the CTO's at SPK-08 |

**Running cost of the basemap: £0, now retrieved at primary rather than carried.**
- **Apple:** *"You get 200GB of Apple hosting capacity included in your Apple Developer Program membership"* [E, [WWDC25 session 325](https://developer.apple.com/videos/play/wwdc2025/325/), retrieved 2026-09-27]. The limit is *"200 GB"* per app record [E, [App Store Connect Help, asset pack size limits](https://developer.apple.com/help/app-store-connect/reference/app-uploads/apple-hosted-asset-pack-size-limits), retrieved 2026-09-27; that page states no fee]. A ~0.8 GB pack uses about 0.4% of it. The Apple Developer Program fee is already in v3 §3.4. **Single source by nature.**
- **Google:** Play Asset Delivery *"is free to use"*, and *"all asset packs are hosted and served on Google Play"* [E, [Android Developers, Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery), retrieved 2026-09-27. **Single source by nature.**]

**Scope added since v3 with no cost effect**, recorded so a reader can see it was checked:
- **D16, D17, D18:** v3's own recommendations, adopted. They change no line.
- **D23:** iOS 26 minimum.
- **D27–D34, D36, D37, D39–D41:** repository and process. D32: *"Nothing in it costs money."* The **labour** for them (SPK-15, SPK-16, the backlog scripts) is process and non-engineering labour, which v3 §4.4 already names as uncarried.
- **D35:** the CEO records his hours. That is a partial remedy for v3 §3.3 and §16.3 (§6).
- **D56:** one mark for the recap credit. That removes a possible Retro wordmark, and no hours were ever attached to it.
- **D57, D58:** wording and a three-fact cap on motion that is already sized.

**One small recurring item is named rather than added.** D43 gives Dependabot a weekly grouped npm PR. Reviewing it is dependency upkeep, which falls inside v3's provisional **45 h/yr security-and-defect line** (v3 §5), still owed a CTO figure (v3 flag F1). **I do not add it separately, to avoid counting the same work twice** [J].

### 2.3 The total carried

| | Low | **Point** | High |
|---|---:|---:|---:|
| One-off hours: design 248 / 364 / 519 + heatmap 55 / 75 / 95 + headlines 30 / 37.5 / 45 | 333 | **476.5** | 659 |
| **One-off at £32.71** | £10,892.43 | **£15,586.32** | £21,555.89 |
| Ongoing hours a year: design 37.5 / 72.25 / 124 + heatmap 8 / 10 / 12 | 45.5 | **82.25** | 136 |
| **Ongoing at £32.71 a year** | £1,488.31 | **£2,690.40** | £4,448.56 |

---

## 3. The cost base, restated

### 3.1 The capitalised build, and the amortisation schedule line

**The Definitions:** *"One-off build labour is capital, amortised straight-line over the standard amortisation period"*, and *"**each capitalised increment runs its own clock from the date it ships**."* **All of this scope is launch scope.** D51 is *"at launch"*, and D44's three themes are *"at launch"*. **So it ships with v1 and joins v1's line. It does not open a line of its own.** If any of it slips past launch, it becomes its own increment with its own clock, and the schedule will show it.

| Increment | Hours | Ship date | Period | Amortised to date | Remaining balance |
|---|---|---|---|---|---|
| **Haunts v1: the whole launch build** | **2,777 h** (point; was 2,300.5) = £90,835.67, plus £18.70 Google Play registration = **£90,854.37** | Not yet set (v3 §3.3) | 36 months | £0.00 | **£90,854.37** |
| *of which added after the CTO's 2,090 h estimate* | *687 h: Block 4 R-5 22.5; spikes 75 + 113; design 364; heatmap 75; headlines 37.5* | | | | |

*(2,300.5 + 476.5 = 2,777. 2,777 × £32.71 = £90,835.67; plus £18.70 = £90,854.37. Check: £75,268.05 + £15,586.32 = £90,854.37. ✔)*

**For Article 9's row on inflated capitalised hours,** *"Capitalised hours per product against the gate estimate **and** hours actually recorded"*, the figures are now: **estimate 2,090 h (CTO); capitalised 2,777 h; recorded 0 h so far.** Recorded hours begin with D35 (the CEO's) and are, as v3 §3.3 states, the only figure that replaces the estimate.

### 3.2 The whole cost base

| | v3 | **Design scope only** | **This addendum (design + heatmap + headlines)** | Low | High |
|---|---:|---:|---:|---:|---:|
| Capitalised total | £75,268.05 | £87,174.49 | **£90,854.37** | £86,160.48 | £96,823.94 |
| Amortised over three years, a year (`B`) | £25,089.35 | £29,058.16 | **£30,284.79** | £28,720.16 | £32,274.65 |
| Fixed annual operating (`F`) | £18,042.74 | £20,406.04 | **£20,733.14** | £19,531.05 | £22,491.30 |
| **Annual fixed cost `A`** | **£43,132.09** | **£49,464.20** | **£51,017.93** | £48,251.21 | £54,765.95 |
| Change on v3 | — | +£6,332.11 (+14.7%) | **+£7,885.84 (+18.3%)** | +11.9% | +27.0% |
| **Total published cost over three years** | £129,396.27 | £148,392.60 | **£153,053.79** | £144,753.63 | £164,297.85 |
| Fixed labour a year | 520 h | 592.25 h | **602.25 h** | | |

*(Point, design only: B = £87,174.49 ÷ 3 = £29,058.16; F = £18,042.74 + £2,363.30 = £20,406.04; A = £49,464.20. Point, all: B = £90,854.37 ÷ 3 = £30,284.79; F = £18,042.74 + £2,690.40 = £20,733.14; A = £51,017.93. Low and high are computed the same way from §2.3. Figures can differ by 1p from a spreadsheet, from rounding at each step.)*

**The variable cost per subscriber (v3 §3.5) is unchanged.** Themes and icons add no per-customer cost that I can identify. **One possible exception is named rather than priced:** a user-chosen icon brings new support contacts on Android (launcher lag, lost shortcuts; CTO §2.4, P3 and P4). v3 §4.6 explains why I do not move an unmeasured rate by a guess.

**Shared company costs (D16) are unchanged at £1,029.77.** They are now **2.0%** of `A`, down from 2.4%. That is because the denominator grew, not the cost.

---

## 4. What it does to margin and reach

The formulas are v3 §6's, unchanged: honest shelf price `V = (A/N + s) × 1.694118`, and margin = `(0.85P − C) ÷ (C + 0.15P)`. The model reproduces every v3 figure exactly on v3's `A`, which I checked before using it on the new one.

### 4.1 Why no launch price moves

v3 §7.1: *"At `N*` the fixed-cost share per subscriber, `A/N*`, is always **£3.3985**, whatever `A` is… **A bigger cost base moves `N*`, not the prices at `N*`.**"* The same property holds here. **Pay-once £28.99, yearly £9.89 and monthly 99p are each still the honest price at the reference volume**, and each still carries the margins v3 §7.2 records at that volume: 16.51%, 16.91% and 16.50%.

> **Stated plainly, because a method that never moves a price when costs rise should be looked at hard.** Under this method, added scope never raises a launch price. It raises the volume at which the price is honest, and it widens Deviation 2 below that volume. **That is honest only because both numbers are published.** It is also why §5.4 asks the CEO to acknowledge the larger deviation rather than letting it pass as "no price change".

### 4.2 The volumes

| | v3 | Design only | **This addendum** | Low | High |
|---|---:|---:|---:|---:|---:|
| **`N*`, where 99p is exactly honest** | 12,692 | 14,555 | **15,012** | 14,198 | 16,115 |
| 99p covers its cost (0% margin) | 8,984 | 10,303 | **10,627** | 10,050 | 11,407 |
| Pay-once at £28.99 covers its cost | 9,503 | 10,898 | **11,240** | 10,631 | 12,066 |
| Every tier compliant from | 9,503 | 10,898 | **11,240** | | |
| Every tier compliant up to (yearly reaches the 30% cap) | 16,043 | 18,398 | **18,976** | | |
| Monthly 99p reaches the 30% cap | 17,140 | 19,657 | **20,274** | 19,175 | 21,764 |

*(`N*` = A ÷ £3.3985. Monthly break-even = A ÷ (£8.415 − £3.614) = A ÷ £4.801. Pay-once = 3A ÷ £13.617. Every threshold scales in proportion to `A`, so the compliant band's width, 1.688×, is unchanged.)*

### 4.3 Margin at the volumes this company has evidence for: Deviation 2, restated

| Subscribers | 2,000 | 4,000 | 6,000 | 8,000 | 10,000 | 12,692 | **15,012** |
|---|---|---|---|---|---|---|---|
| **v3: realised margin at 99p** | −62.9% | −37.7% | −19.4% | −5.6% | +5.2% | +16.5% | — |
| **This addendum: realised margin at 99p** | **−67.7%** | **−44.5%** | **−27.2%** | **−13.7%** | **−2.9%** | **+8.6%** | **+16.5%** |
| Honest monthly price, v3 | £3.55 | £2.03 | £1.52 | £1.27 | £1.12 | £0.99 | — |
| **Honest monthly price, this addendum** | **£4.11** | **£2.31** | **£1.71** | **£1.41** | **£1.23** | **£1.08** | **£0.99** |

**Against Article 2.1, quoted:** *"Prices target a margin of approximately **20% over published costs**… **A deviation in either direction is a deviation**… As a hard backstop, **no product's margin may exceed 30%**, regardless of justification."*

- **The cap: no breach, and it is further away.** Added cost lowers margin at every volume, so it cannot push any tier over 30%. Monthly 99p now reaches the cap at 20,274 subscribers, not 17,140. **The cap forces no price change.**
- **The target: Deviation 2 is larger and is recorded here as larger.** Below 15,012 subscribers every tier runs below the ~20% target. At 4,000 subscribers the gap is **64.5 points** (−44.5% against +20%), up from 57.7. **The written justification is the CEO's, recorded in v3 §6.1**: *"accepting that it may not cover its own benchmarked labour."* **Nothing in Article 2.1 ties a justification to the size of the deviation it covers, so the justification still stands.** Whether to re-confirm it anyway is §5.4, and that is my judgment, not a requirement of the clause.
- **Deviation 1**, the store commission passed through at no markup, is unchanged at −3.50 points at `N*`.

### 4.4 Reach (v3 §14), restated

| | v3 | **This addendum** |
|---|---:|---:|
| Pay-once at a flat £28.99: distinct buyers over three years | 9,503 (264 a month) | **11,240 (312 a month)** |
| Pay-once, stepped under D15 (v3 §14's approximation, scaled) [I] | ~11,500 | **~13,600** |
| Subscription, 5.2-month average tenure (central) | 62,197 (1,728 a month) | **73,568 (2,044 a month)** |
| Subscription, 13.2-month tenure | 24,502 | **28,982** |

*(Every count scales by A ÷ A_v3 = 1.1828. The tenure figures remain single-origin (RevenueCat), as v3 §16.4 records.)*

> **v3's negative finding stands and is now 18% stronger:** Haunts is not unviable at a compliant price. It is unviable at 99p on any reach this company has evidence for. **What overturns it is unchanged** (v3 §14): a measured tenure above about 34 months, a reach figure for competitor import, or pay-once converting nearly as well as monthly. **Where I looked** is v3 §14's list, plus the design and map notes named in §1 and §2 above. **Neither adds a reach estimate.**

---

## 5. The price ladder: what moves, what must, and what I recommend

### 5.1 The launch ladder (D14): no change

| Tier | Charged | Honest at `N*` (15,012) | Margin at `N*` | Must it move? |
|---|---|---|---|---|
| Pay once | **£28.99** | £28.99 | 16.50% | **No** |
| Yearly | **£9.89** | £9.85 | 16.91% | **No** |
| Monthly | **99p** | 99p | 16.51% | **No** |

### 5.2 After the cliff, at the reference volume (v3 §8, D18)

| | v3 (`N*` 12,692) | **This addendum (`N*` 15,012)** | Change |
|---|---|---|---|
| Honest post-cliff monthly | 71.1p | **70.5p** | — |
| **Charged post-cliff monthly** | **69p (30.3% cut)** | **69p (30.3% cut)** | **None** |
| Honest post-cliff yearly | £6.500 | **£6.431** | |
| Charged post-cliff yearly | £6.49 | **£6.39** | −10p. £6.39 is 4.1p from the honest price; £6.49 would be 5.9p away |
| Margin at an unchanged 99p after the cliff | +51.8% | **+52.8%** | |
| 99p breaches the cap after the cliff above | 7,170 | **8,239** | |
| First cut under D18's recompute rule, from | ~5,540 | **~6,370** | |
| Full 69p reached from | ~11,100 | **~12,740** | |

**The cliff is slightly larger, because the build is now a bigger share of `A`** (59.4% against 58.2%). The charged monthly figure does not move because the grid is 10p wide. **The customer copy (v3 §20.5, S2)** says *"If Haunts has about 12,700 subscribers by then, the monthly price falls from 99p to 69p."* **At the point estimate that is still true**, since 69p is reached from about 12,740. **But it is only true by coincidence, and it fails at the high estimate** (about 13,820). **The subscriber figure is a fill, to be computed from the launch cost sheet.** I recommend it then reads as that sheet's `N*`: about 15,000 on today's figures. **Owner: PM/BA, at transcription.** It is flagged, not changed, because the copy is not yet final.

### 5.3 D15's pay-once steps and thresholds

**The step prices shift, because the build/fixed split shifts.** v3 §11.2's formula: price in year k = `[3 × (F/N + s_P) + (build years left) × (B/N)] × 1.694118`, at `N*`.

| Step | v3 honest → charged | **This addendum: honest → nearest grid point** | Note |
|---|---|---|---|
| Launch | £28.992 → **£28.99** | £28.992 → **£28.99** | Unchanged by construction |
| **M1 (a third recovered)** | £25.643 → **£25.49** | £25.575 → **£25.49** | Unchanged |
| **M2 (two thirds recovered)** | £22.294 → **£22.49** | £22.157 → **£22.00** | **−49p.** £22.00 is 15.7p away; £21.99 is 16.7p; £22.49 is 33.3p. **It depends on App Store Connect offering £22.00 at all**, which is v3 §7.2's open grid check. If it does not, £21.99 |
| **Post-cliff** | £18.945 → **£18.95** | £18.739 → **£18.90** | **−5p.** An X.90 point. Same grid caveat; if not offered, £18.95 |
| **Recovery thresholds** (thirds of the launch capitalised figure) | £25,089.35 / £50,178.70 | **£30,284.79 / £60,569.58** | Rise with the build |

**When each step can land** (capped definition, v3 §20.1; all-monthly equivalent at 99p; contribution £4.801 per subscriber-year) [I]:
- **M1 at the month-12 review, and M2 at the month-24 review**, need at least break-even volume: **10,627** (was 8,984).
- **M1 by the month-36 review** needs `N ≥ (F + B/3) ÷ £4.801` = **6,421** (was 5,500 by the same formula). **Below that, no step fires before the cliff.**
- **M2 by the month-36 review** needs `N ≥ (F + 2B/3) ÷ £4.801` = **8,524** (was 7,242).

> **Recommendation, a sequencing one and not a pricing decision: do not freeze D15's step prices or thresholds until the launch cost sheet (v4).** D15's guardrail 2 requires them *"published before first sale"*, not now. v3 §20.2 already sets the thresholds from *"the **launch** cost sheet"*. **Freezing them today would lock in a build figure that SPK-08 is about to move**, and under guardrail 2 a frozen threshold can never be moved afterwards. That is the right rule, and it is the reason not to freeze early.

### 5.4 Must any price move? **No.** Do I recommend moving one? **No.** One acknowledgement is recommended

**No price must move.** The cap is further away (§4.3). The target was already missed below the reference volume, on a written justification that has no size limit. **No constitutional clause is engaged by this cost increase in a way that forces a price.**

**I recommend holding every price, for three reasons [J]:**

1. **Re-price once, not twice.** SPK-08 will move `A` again, probably by more than this addendum does (§6). A pre-launch price change now, and another at v4, would be two price decisions for one launch.
2. **The monthly grid cannot express the change.** The honest monthly price at the point estimate's `N*` is still 99p, and 10p is the grid step. Moving the monthly price would mean choosing a different reference volume, not responding to this cost.
3. **The added cost is scope the CEO chose for product quality and his stated selling point** (D44: customisation *"could be a nice little selling point"*; D51, against the CVO's advice). The CEO's own non-commercial basis, *"if I can release it and it makes a bit of money then I am happy with that"*, covers choosing quality over margin. **What it does not cover is the choice being invisible, and this addendum makes it visible.**

> **One CEO acknowledgement recommended, when convenient (5.4 is his, and this is his pricing position):** *"The design scope I chose (D44–D55) raises Haunts' published cost by about 15%. It does not change any launch price. It widens the below-cost deviation at low volume, to about −44% at 4,000 subscribers, and I accept that."* **Not required by Article 2.1, which is satisfied by the existing justification.** My reason is that a deviation accepted at one size and then grown by later decisions should be accepted again, once, in the record, where a reader can see it was noticed [J]. If he would rather raise prices, the number to start from is §4.3's honest price at a volume he believes. **That is a different decision, and I am not recommending it before v4.**

---

## 6. What is still not costed

**The unsized list has not shrunk.** It has had two items taken off (the heatmap, and the headline system on UX's figure) and several put on. Requirements went from 163 at v3 §4.6 to **219** (`backlog-plan.md` v0.3: *"219 requirement + 19 planning"*). The design scope accounts for 22 of the new ones. This addendum costs 21 of them. HEAD-23 is pending SPK-19, below. **The rest is SPK-08's.** Among them:

| Still unsized | Why it matters | Owner |
|---|---|---|
| PHOTO-1 … 11, and **D14(d) thumbnail backup** | Two platforms' library APIs, streamed export, restore. Also new support contacts (v3 §4.6) | CTO (SPK-08, SPK-11, SPK-12) |
| LOOK-1, LOOK-3 … 9: the inference screen, the recap and its image, the self-portrait (D19(d)) | Unsized build | CTO (SPK-08) |
| **DATA-15, competitor import** | Build, **plus recurring** parser upkeep when a third party changes its format: v3 §4.6 carried 10–20 h/yr only as sensitivity | CTO (SPK-08, SPK-13) |
| ONB-1 … 3 | ONB-3 at 2–4 days is the PM/BA's figure, not the CTO's | CTO |
| **HEAD-23 and the *Neighbourhood* template**: an area name per venue | May need venue-index work, **plus a quarterly refresh cost** (SPK-19). CTO §7 flag 3: *"Don't write it into requirements until the index's fields are confirmed"* | CTO (SPK-19) |
| **D52 theme variants**, including Mono's margin column of times | Contained components, but none is sized except Retro's bar | UX lists them; CTO sizes |
| The §4.2 five (VEN-13, VEN-16, VPAGE-6, VPAGE-7, NOT-6), VPAGE-10 and 11, PRICE-13 and 14, D19(a) weighted ranking, D19(c) note search | Mostly small; **VEN-16 is not** (v3 §4.2) | CTO |
| **Non-engineering labour** (v3 §4.4), now also the repository and process work of D27–D43 | **Every price Candour has modelled still leaves it out** | CEO: recorded hours (D35) are the only remedy |
| **D38(5) paid final artwork** | Cash, and capital if paid | CEO (5.4) |
| **D53: starting on the SDK 58 beta** against the CTO's advice | Rework risk if the beta has bugs. Unpriced, and bounded by D53's own condition to fall back to stable | CTO |

**Priced as sensitivity, on v3 §4.6's own figure** (+625 capital hours and +20 h a year for everything unsized). This is my judgment [J]. It includes the heatmap's former share, and it includes items that arrived after it was set. **I judge the two roughly offset, and I cannot do better than that without SPK-08:**

| Scenario | Capital hours | `A` | `N*` at 99p | Margin at 99p, 4,000 subscribers | Pay-once buyers needed |
|---|---:|---:|---:|---:|---:|
| v3 | 2,300.5 | £43,132.09 | 12,692 | −37.7% | 9,503 |
| **This addendum** | **2,777** | **£51,017.93** | **15,012** | **−44.5%** | **11,240** |
| This addendum + everything still unsized [J] | 3,402 | £58,486.71 | 17,210 | −49.8% | 12,886 |

> **The honest summary: this addendum carries everything a seat has put hours on, and the reference volume has risen 18%. What is still unsized could take it to about 36% above v3. SPK-08 is now the single largest open input to Haunts' price and reach, larger than anything in this addendum.** Recorded hours from day one (D35) are what will eventually replace every [J] in this section.

---

## 7. v3 figures this addendum supersedes

| v3 location | v3 | Now |
|---|---|---|
| §0-B, §3.6 `A` | £43,132.09 | **£51,017.93** |
| §3.6 three-year cost | £129,396.27 | **£153,053.79** |
| §3.2, §3.3 capitalised hours and value | 2,300.5 h, £75,268.05 | **2,777 h, £90,854.37** |
| §3.4 fixed labour | 520 h/yr | **602.25 h/yr** |
| §7.1 `N*` | 12,692 | **15,012** |
| §7.5 compliant band | 9,503–16,043 | **11,240–18,976** |
| §6.1 Deviation 2 table | −37.7% at 4,000 | **−44.5% at 4,000** (§4.3) |
| §8.2 post-cliff yearly | £6.49 | **£6.39** |
| §8.3 cap-only threshold; honest-rule first cut; 69p from | 7,170; ~5,540; ~11,100 | **8,239; ~6,370; ~12,740** |
| §20.2 D15 thresholds | £25,089.35 / £50,178.70 | **£30,284.79 / £60,569.58**, not to be frozen until v4 (§5.3) |
| §20.2 M2 step; post-cliff pay-once | £22.49; £18.95 | **£22.00; £18.90**, subject to the grid check (§5.3) |
| §14 reach | 9,503 pay-once; 62,197 subscribers | **11,240; 73,568** |
| §13 shared costs as a share of `A` | 2.39% | **2.02%** |

**Unchanged:** every launch price; post-cliff monthly 69p and its 30.3% cut; the benchmark (£32.71); variable costs; D17's tail (£2.31 per pay-once user a year); the 90-day notice (D14(b)); and the method throughout.

---

## 8. Disclosures, flags and change log

**Related-party disclosures: none new.** All added labour, £15,586.32 of build and £2,690.40 a year, is founder and agent labour valued at the benchmark and not drawn. Constitution 2.1 requires it anyway: *"a fair-market cost for labour (including the founder's, whether or not it is actually drawn)."*

**Blocks: none.** My blocking power is *"Launch of any pricing not backed by a published cost sheet; any proposal without a credible cost model."* With this addendum, every sized item is carried and every unsized one is named and bounded (§6). **The cost model is credible in the charter's sense, and the v3 lift stands.**

**Flags, each with the seat that holds it:**

| # | Flag | Holder |
|---|---|---|
| D-F1 | **Don't add D54's 15 h to the 12 h saving.** The net design scope is 364 h, not 379 h (§1.3) | Main session; PM/BA wherever the figure is transcribed |
| D-F2 | The ongoing point of *"≈ 76 h/yr"* does not re-derive (midpoints give 79). Add a point column to §6, or state the basis | CTO |
| D-F3 | **A release process document**, as VEN-19 requires. It replaces the assumed 6–10 releases a year (§1.5) | CTO |
| D-F4 | **Does "each iOS release" (D54) include x.y.z bug-fix releases?** Costed at 7 a year; 15 if so (§1.4) | CEO (clarification) |
| D-F5 | **SPK-08 is now the largest open input to price and reach** (§6). It should also replace UX's headline figure (§2.2) | CTO |
| D-F6 | **Don't freeze D15's step prices or thresholds before v4** (§5.3) | CEO, with the CFO at v4 |
| D-F7 | S2's *"about 12,700 subscribers"* is a fill from the launch sheet, true today only by coincidence (§5.2) | PM/BA, at transcription |
| D-F8 | Confirm **£22.00, £18.90 and £6.39** exist in App Store Connect and Play Console (v3 §7.2's open grid check) | CFO, at store configuration |
| D-F9 | Dependabot's weekly PR review (D43) falls inside the provisional 45 h/yr security line. **The CTO's figure is still owed** (v3 F1) | CTO |

**Where I looked:** `constitution.md` v1.3 (Definitions, Articles 2.1, 4, 5.4, 9); `roles/cfo.md`; `pipeline/evidence-standard.md` v1.1; `pipeline/templates/cost-sheet.md`; `products/haunt/cost-sheet-v3.md` in full. **In the coordinator's worktree `agent-ad75fb7ff8b8f2f2e`:** `design-feasibility-and-sizing.md` in full; `decisions/2026-09-16-haunt-gate.md` D10–D58; `backlog-plan.md` (SPK rows, count drift, v0.3 change log); `requirements.md` (VEN-19, the headline estimate, the theme-cost paragraph); `map-options-comparison.md` (the heatmap's hours and running cost). **Retrieved externally this session (2026-09-27):** Apple's *About iOS 18 Updates*; Apple's WWDC25 session 325 and the App Store Connect asset-pack limits; Android's Play Asset Delivery page. **Not re-retrieved and attributed:** the OFL FAQ and font sizes (CTO); every v3 retrieval, including ONS ASHE, FX and the Apple grid. **Looked for and not found:** a release cadence; any CTO sizing of the headline system; a price for final artwork.

*Arithmetic in §§1–5 is owed re-derivation by a seat other than this one under gate Condition 6 before publication. The calculation is small enough to redo by hand from §3.2's `A` and v3 §6's formulas.*

### Change log

| Date | Change |
|---|---|
| 2026-09-27 | **Created (SPK-17).** Re-derives the CTO's design sizing: one-off sums exact; net **364 h** after Native Tabs, D54 and D55; **the 15 h Retro bar is not additional to the 12 h saving**; ongoing **72.25 h/yr** after D53/D54, with the CTO's 76 h/yr point not reproducible (79 by midpoints). Carries the design scope (**£11,906.44 one-off, £2,363.30 a year**) and, at D22's instruction and on the CTO's endorsement of UX's figure, the heatmap basemap and the headline system. **Total +476.5 h one-off (£15,586.32) and +82.25 h a year (£2,690.40). `A` £43,132.09 → £51,017.93 (+18.3%); `N*` 12,692 → 15,012.** No launch price changes; Deviation 2 wider (−44.5% at 4,000 subscribers); cap further away (20,274). D15 steps and thresholds shift; recommends freezing them only at v4. Asset-pack hosting confirmed £0 at primary on both stores. **Not a price: Constitution 5.4 reserves pricing to the CEO.** |

*Prepared by the Chief Financial Officer under `roles/cfo.md`. It prepares and flags; it does not certify (Constitution 6.1).*

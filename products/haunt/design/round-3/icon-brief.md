# Haunts icon and mark: the PLAT-7 brief, version 3 (final marks)

**Seat:** UX / Design Lead · **Date:** 2026-09-27 · **Slug:** `haunt`
**Supersedes** round 1's [`../icon-brief.md`](../icon-brief.md) **for the marks themselves**. Round 1's platform research (§2), its exclusion list (§3) and its process (§5–§6) still stand, and are summarised here rather than repeated. **Round 1 is not edited.**
**Decisions it implements:** **D44** (CEO, 2026-09-27): *"Hybrid A icon: the Masthead h on plum with the double underline, with the full-stop h liked as an alternative. Hybrid B icon: the h with the orange bar."* Also **D11(d)** (the brief is UX's; artwork is a CEO spending decision; no ghost, eye or tracking imagery) and **PLAT-7** (BLOCKING: icons at every size both stores and OSes require, plus the recap mark).
**Status:** prepares and flags; certifies nothing (Constitution 6.1). **Commissions no artwork and spends nothing** (Constitution 5.4; D38(5)).
**Concept masters:** [`concepts/a-icon-masthead.svg`](concepts/a-icon-masthead.svg), [`concepts/a-icon-fullstop.svg`](concepts/a-icon-fullstop.svg), [`concepts/b-icon-bar.svg`](concepts/b-icon-bar.svg); all appearances in [`concepts/icons-final.svg`](concepts/icons-final.svg); wordmarks in [`concepts/wordmarks-final.svg`](concepts/wordmarks-final.svg).

---

## 0. In one screen

- **Up to three icons, depending on one open decision** (`finalise.md` §4). **Option 1:** one store icon only, which is the mark of the default theme (still to be decided, `finalise.md` §5). **Option 2:** that store icon plus user-chosen alternates, so all three marks are made.
- **Two wordmarks:** lowercase "haunts" in Newsreader, with **A's apricot double rule** or **B's orange margin rule**.
- **One recap credit** (LOOK-5): the wordmark of the user's current theme at credit size, small and hideable. **Open for the CEO:** whether the credit follows the theme or is always the store mark; my recommendation is **follows the theme** [J], because the recap image is rendered in the user's theme.
- **Before anything is commissioned:** the CGO answers `requirements.md` §22 item 18 (rights in a tool-made mark). **These concepts were drawn by an AI agent**, so adopting them as final artwork is itself the case that question is about (§6).

---

## 1. The marks, specified

### 1.1 A (Warm): Masthead h with double rule — `a-icon-masthead`

| Element | Specification |
|---|---|
| Field | Plum `#5B2A86`, full bleed |
| Glyph | Lowercase slab-serif h in cream `#FFF8F1`: stem, slab serifs at the top-left and both feet, a rounded shoulder. Occupies about 52% of the canvas width |
| Rules | Apricot `#F2A65A`: **thick (≈ 3.5% of canvas) over thin (≈ 1.6%)**, with a gap equal to the thin rule. Same width as the h's feet (serif to serif) |
| Dark appearance | Field `#1A1422`; glyph and rules unchanged |
| Tinted / themed (one colour) | Glyph and both rules as a single silhouette on transparent |
| Android adaptive | Foreground = glyph and rules **scaled to 90%**, wholly inside the 66/108 safe zone; background = plum |

### 1.2 A alternative: full-stop h — `a-icon-fullstop`

Cream `#FFF8F1` field, plum `#5B2A86` h, **apricot full stop** at the baseline to the right. Dark: field `#1A1422`, cream h, apricot dot. Tinted: h and dot as one silhouette. Adaptive: foreground at 90%.

### 1.3 B (Mono): h with orange bar — `b-icon-bar`

Black `#111111` field, white h, **orange `#C2410C` bar** at the right foot, level with the baseline serifs. Dark: field `#0F0F10`. Tinted: h and bar as one silhouette. Adaptive: foreground at 90%. **The bar is never animated**, anywhere (`finalise.md` §1.3).

### 1.4 Wordmarks

| | A (Warm) | B (Mono) |
|---|---|---|
| Word | "haunts", lowercase, **Newsreader semibold**, tight tracking | Same |
| Device | Apricot double rule beneath, thick over thin, the width of the word | Orange margin rule before the word, the height of the ascenders |
| Colours | Text `#241B2F` (light) / `#F6EFE8` (dark); rule `#F2A65A` / `#F5B77A` | Text `#111111` / `#F2F2F0`; rule `#C2410C` / `#FB923C` |
| Credit size (under ~32 px tall) | **The double rule becomes one hairline** | Unchanged |
| Delivery | **Outlined** (converted to paths), so no font licence travels with the logo; Newsreader is OFL 1.1 in any case (round 1, E2) | Same |

**Name caveat, unchanged:** "Haunts" is a working name until PLAT-6's three checks pass. **Nothing containing the name is finalised before then**, and that includes both wordmarks and any store graphic. The h icons are also tied to the name, which is a cost of a letter mark (round 2 §3).

---

## 2. Platform and store requirements (summary; full text and sources in round 1 §2)

- **Apple:** a 1024 × 1024 canvas; layered icons with Liquid Glass effects assembled in Icon Composer; **six appearances: default, dark, clear light, clear dark, tinted light, tinted dark**; clearly defined edges, no thin hairlines, minimal shapes; a first-letter mnemonic is acceptable [E, round 1 E1].
- **Alternate icons (only if option 2):** chosen by the user in the app's settings; must stay *"closely related to your content and experience"*; *"Avoid creating one someone might mistake for another app"*; **each alternate *"require[s] their own dark, clear, and tinted variants"***, and all are subject to app review [E, HIG App icons, retrieved 2026-09-27]. Changed through `setAlternateIconName`, declared in the build [E, UIKit docs, 2026-09-27].
- **Android launcher:** adaptive icon, foreground, background and **monochrome** layers at 108 × 108 dp, with the mark inside the **66 × 66 dp safe zone** and at least 48 dp [E, round 1 E2].
- **Google Play listing:** **512 × 512, 32-bit PNG, sRGB, ≤ 1024 KB**, full square (Play applies a 30% radius), no drop shadow, no text or graphics that indicate ranking or promote installs [E, round 1 E3].
- **Android notification small icon and splash:** as round 1 §2.4 [K; for the CTO].
- **How Android offers alternate icons, and what iOS shows the user when the icon changes, are not retrieved** [K]; the CTO confirms both (`finalise.md` §4).

---

## 3. Exclusions (round 1 §3, unchanged, with one addition)

No ghost, eye, crosshair, pin, radar or concentric rings, footprints or routes (D9, D11(d)); no glass, bottle, "cheers", confetti, trophy or star-as-reward (MEM-1); nothing that narrows the product to pubs (D9); no headstone shapes; no moon or neon; no padlock as the main idea.

**Added in round 3:** **no alternate icon that disguises the app** (a calculator, a notes app), however privacy-minded the motive. Apple forbids it in terms: *"Avoid creating one someone might mistake for another app"* [E].

---

## 4. Deliverables

| # | Deliverable | Option 1 | Option 2 |
|---|---|---|---|
| D1 | Master vector of each mark (layered: field, glyph, rules or bar or dot; plus a one-colour silhouette) | 1 mark | 3 marks |
| D2 | **iOS icon source** for Icon Composer, 1024 px, annotated for default, dark and mono (clear and tinted derive from it) | 1 | 3 (the primary plus 2 alternates, each with its own dark, clear and tinted variants [E]) |
| D3 | **Android adaptive icon**: foreground (at 90%), background and monochrome layers, vector | 1 | 3 |
| D4 | **Google Play icon**, 512 px PNG, per §2 | 1 (the store icon only) | 1 |
| D5 | **Wordmarks**, outlined, light and dark, with the credit-size variant | Both A and B (the recap credit follows the theme) | Both |
| D6 | Android notification silhouette, if notifications ship | 1 | 1 |
| D7 | **Usage sheet**: clear space (the height of the h's x-height), minimum sizes (icon 29 px; wordmark 16 px tall; credit per LOOK-5), colours, and the §3 exclusions | 1 | 1 |

**LOOK-5 credit size**, unchanged from round 1 [J]: 4% of the recap image's short side, never below 24 px, in the footer margin, outside the content area.

**Acceptance checks** (round 1 §4, unchanged): a **test submission to both stores before the release-candidate build** (PLAT-7(d)); the **misreading test** (five people who have not seen the icon are asked what the app does and what the picture shows; any answer of grave, ghost, being watched or tracked, map or drinking fails it); and the 29 px, greyscale and one-colour checks. **One addition for the letter marks:** ask whether the h reads as a letter at 29 px, and whether A's thin rule survives there or merges into one (acceptable either way).

---

## 5. What to hand a designer or a tool

As round 1 §5: this brief, the concept masters above, the palette tokens (`../tools/palettes.py`, `HYBRIDS`), the exclusions page, the deliverables table and the working-name warning. **The concepts are close to final in idea and not in craft.** A type designer should **redraw the h from Newsreader** (or draw a custom h in its spirit), so that icon and wordmark share one letterform; today the icon's h is geometry drawn by this seat, and the wordmark's h is Newsreader's (`finalise.md` §1.4).

---

## 6. Ownership, spending and sequence

- **`requirements.md` §22 item 18 (CGO, open):** *"who owns artwork a person is commissioned to make, and whether a mark produced with a tool can be owned and registered."* **It now applies directly:** the D44 marks are concepts drawn by an AI agent. If they are used as final artwork unchanged, they are a tool-made mark. If a human designer redraws them, it is commissioned work, and the contract must assign copyright and hand over source files. **The CGO's answer should come before the CEO chooses the route**, and any reliance on it needs a qualified human (Constitution 6.1).
- **Spending:** none proposed. Commissioning a designer, paid recruitment for the misreading test and any trademark filing are each CEO decisions (Constitution 5.4).
- **Sequence:** (1) the default theme, which decides the store icon (`finalise.md` §5); (2) option 1 or 2 for alternate icons (`finalise.md` §4; CTO on feasibility); (3) the CGO on item 18; (4) the CEO on the route and any spend; (5) artwork and the misreading test; (6) PLAT-6's name checks pass; (7) test submission to both stores before the release candidate.

---

## 7. Evidence register (round 3; round 1's register still applies)

| # | Claim | Source | Retrieved |
|---|---|---|---|
| E1 | Alternate icons: chosen in settings; closely related to the app; not mistakable for another app; each needs its own dark, clear and tinted variants; all subject to review | [Apple HIG, App icons (JSON)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json) | This seat, 2026-09-27 |
| E2 | `setAlternateIconName` changes the displayed icon; alternates declared in the build (`CFBundleAlternateIcons`); `supportsAlternateIcons` | [UIKit documentation (JSON)](https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setalternateiconname(_:completionhandler:).json) | This seat, 2026-09-27 |
| — | Store icon specs, adaptive icons, six appearances, OFL | Round 1 `icon-brief.md` §7 and `brand-directions.md` §9 | This seat, 2026-09-26 |

**[K], not retrieved:** whether iOS shows a notice when the icon changes; how Android offers alternate icons; Android notification and splash specifics.

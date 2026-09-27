# Haunts design, round 2: two hybrids, a lowercase logo, glass, and a modern ticker

**Seat:** UX / Design Lead · **Date:** 2026-09-27 · **Slug:** `haunt` · **Commission:** **D42** (CEO, 2026-09-27), read at `decisions/2026-09-16-haunt-gate.md` in the coordinator's worktree. **Nothing is adopted.** D42: *"Nothing is adopted."*
**Builds on round 1, which is unchanged:** [`../brand-directions.md`](../brand-directions.md), [`../themes.md`](../themes.md), [`../icon-brief.md`](../icon-brief.md). Everything round 1 says about the theme rules, the retro guardrails and the icon brief still stands unless this note says otherwise.
**Files:** concepts in [`concepts/`](concepts/); tools in [`../tools/`](../tools/): `palettes.py` (round-2 tokens under `HYBRIDS`), `contrast.py --round2`, **`glass.py`** (new), `generate_round2.py` (new).
**Status:** prepares and flags; certifies nothing (Constitution 6.1). Lean by request: what changed, why, and a recommendation. **Evidence** is tagged under `pipeline/evidence-standard.md`; every [E] was retrieved on 2026-09-26 or 2026-09-27 and is listed in §9. Contrast figures are arithmetic from the scripts.

---

## 0. The answer

| What the CEO asked | What round 2 gives |
|---|---|
| **Hybrid A: Almanac × Doorway** | **"Warm editorial."** Newsreader and Inter on Doorway's cream, plum and apricot, with Doorway's rounded cards. **Calmer than Almanac:** no double rules, no small capitals, no ruled timeline, one accent used once (the apricot headline card). §1 |
| **Hybrid B: Ledger × Almanac** | **"Mono editorial."** Ledger's black-and-white and its code-like details (`//` section labels, `>` kicker, monospace times) with Newsreader venue names, Inter text and Almanac's line icons. One orange signal, used for the mark and the focus ring only. §2 |
| **Lowercase logo** | **"haunts"** in lowercase Newsreader for both hybrids, and a **lowercase-h icon family**: the Masthead h plus two companions in each hybrid. Doorway's constructed lettering is gone. Of Ledger's icons only Entries returns, redrawn around the h. §3 |
| **Liquid Glass tab bar** | A floating glass bar in both hybrids, **measured against the worst content beneath it**. **Finding: legible glass is mostly frosted, not clear.** The bar must be at least **80% opaque in light mode and 90% in dark**, and every label uses full-strength text colour. Reduce Transparency, Increase Contrast and the Android fallback are designed. §4 |
| **A ticker in the modern themes** | A modern ticker for each hybrid, meeting HEAD-9 to HEAD-11 and remaining the user's choice (HEAD-2). **Plus one proposal that is more user-friendly than any crawl: "Rotate", whole sentences one at a time**, which needs a requirements change. §5 |
| **"Procedurally generated"** | More variety **inside** the fixed template catalogue: new templates, several phrasings each, chosen deterministically by date. **Nothing generated freely, nothing random per open.** §6 |
| **Contour** | **One touch: contour lines as texture in the empty band at the top of the self-portrait and heatmap screens**, never behind text, never closed rings. §7 |
| **Homepage (retro)** | Kept. It gets **the same floating bar in the same place, opaque and bevelled, not glass**. §8 |

**My recommendation: Hybrid A as the brand and the modern default, with Hybrid B kept as the first additional theme** (§10). A has Doorway's warmth, which the CEO asked for, and it is the easier of the two for a first-time, non-technical user. B is the more distinctive, and because it shares A's type and icons it would be a comparatively cheap theme.

**The one decision the CEO should make next: Hybrid A or Hybrid B as the brand and default.** The icon, the theme set and the icon brief's final wording all follow from it.

---

## 1. Hybrid A: warm editorial (Almanac's type, Doorway's colour and cards)

**Mockup:** `concepts/hybrid_a-home.svg` (light and dark, Line headline, glass tab bar).

**The idea.** A calm, warm journal. Newsreader carries everything that is *yours* (venue names, the headline, the wordmark); Inter carries everything functional. Doorway supplies the warmth: cream page, white rounded cards, plum for action, and **apricot used once, for the headline card**, so the one thing that changes day to day is the one thing that stands out.

**How it answers "quite busy" and "a bit bland"** [J, this seat's reading of D42]:

| Almanac had | Hybrid A has | Why it is calmer |
|---|---|---|
| Double rules, small capitals, a vermilion kicker, a ruled timeline | **No rules at all.** Sentence-case section labels in Inter. Cards separate things, so lines don't have to | Fewer marks on the page; one way of grouping, not three |
| Paper, ink blue, vermilion and ochre | **Cream, plum and apricot**, with ochre only for the "Unconfirmed" label | Doorway's colours, which the CEO preferred, with one accent colour instead of two |
| Serif and sans at many sizes and weights | **Three text sizes on the home screen** (21, 16–19, 13), two weights | Less typographic noise |
| Headline as a masthead | Headline as an **apricot card** with generous corners (30 pt top, 20 pt bottom: a soft nod to Doorway's arch, never a full arch, so no headstone reading) | Warmth without ornament |

**Palette, measured** (19 pairs per mode; full table in appendix A):

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` / `surface` | `#FFF8F1` / `#FFFFFF` | `#1A1422` / `#251D30` | body text on page **15.67 / 15.79** |
| `text` / `text2` | `#241B2F` / `#5C5266` | `#F6EFE8` / `#B9AFC4` | secondary on card **7.36 / 7.70** |
| `primary` (plum) | `#5B2A86` | `#C9A7F0` | label on button **9.90 / 8.40** |
| Headline card (apricot) with `text` on it | `#F2A65A` | `#F5B77A` | **8.15 / 9.38** |
| `star` / `unconfirmed` | `#B45309` / `#9A4D00` | `#F5B77A` | **5.02 / 9.20**; **6.11 / 9.20** |
| `outline` | `#8C7F99` | `#7E7190` | lowest UI pair **3.56 / 3.59** (needs 3.0) |

**Type:** Newsreader and Inter, both OFL 1.1 with no Reserved Font Name (round 1, `brand-directions.md` §9, E2). **Cards and shape:** 20 pt card corners, 18 pt pill buttons and chips, no borders on cards, hairline outlines only on controls. **Icons:** Almanac's line icons (1.8 pt stroke, rounded joins); the Places tab stays an awning, never a pin.

**Motion** [J]: cross-fades of 150–200 ms and a short damped settle on sheets; nothing on launch, nothing on confirming (MEM-1). Under Reduce Motion, instant changes.

**Risks** [J]: warm and rounded is a common 2026 consumer look, so distinctiveness rests on Newsreader and the apricot card. **Plum and apricot may date** (round 1's warning stands).

---

## 2. Hybrid B: mono editorial (Ledger's monochrome, Almanac's type and icons)

**Mockup:** `concepts/hybrid_b-home.svg`.

**The idea.** A precise, black-and-white record that reads like well-set code *and* like a good page. The code-like touches the CEO liked are kept as **presentation only**: `//` section labels, a `>` before the headline kicker, times and durations in a monospace, a margin column of times on the timeline. The serif is what stops it being a terminal: **venue names and the headline are in Newsreader**, so the places are the warmest thing on the screen.

**What the code-like styling may and may not do.** A `//`, a `>` or lower case is **case and decoration**, allowed by round 1's theme rule (`themes.md` §2); the words are unchanged, and the glyphs are hidden from screen readers. **No blinking cursor, no fake command syntax, no hex codes or IDs shown to users** [J]: a blinking cursor is blink (SC 2.2.2, HEAD-8), and exposed IDs are noise for everyday users.

**Palette, measured:**

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` / `surface` | `#FAFAF8` / `#FFFFFF` | `#0F0F10` / `#1A1A1C` | body text **18.07 / 17.09** |
| `text` = `primary` = `star` | `#111111` | `#F2F2F0` | label on button **18.88 / 16.85** |
| `text2` = `meta` (monospace) = `kicker` | `#555555` | `#A3A3A0` | **7.46 / 6.87** |
| `accent` (orange signal: the mark and focus ring only) | `#C2410C` | `#FB923C` | focus **≥ 4.96** (round 1) |
| `unconfirmed` (orange text) | `#B93D0B` | `#FB923C` | **5.62 / 7.68** |
| `outline` | `#767676` | `#76767A` | lowest UI pair **4.35 / 3.84** |

**Type: three families.** Newsreader and Inter as in A, plus **IBM Plex Mono** for metadata only. Plex reserves the name "Plex" (round 1, E3), so subsetting may require renaming it; that stays a flag for the CGO and CTO. **Alternative that avoids a third family:** Inter's tabular numerals for times, which loses some of the code look [J].

**Risks** [J]: it is **more distinctive and less friendly**. For a first-time, non-technical user, `// to confirm` is a small puzzle the plain words don't pose (the charter's first question). It is also the harder of the two to make feel warm at a memory ("Three years of The Brass Kettle").

---

## 3. The lowercase logo and icon families

**Sheets:** `concepts/hybrid_a-logo.svg`, `concepts/hybrid_b-logo.svg`; six 1024 px icons `hybrid_*-icon-*.svg`.

**Wordmark: "haunts", lowercase, Newsreader semibold, tight letter-spacing**, in both hybrids. Hybrid B puts Ledger's orange margin rule before it. Doorway's constructed lettering is gone, per D42. **The wordmark in the SVGs is a stand-in font** (New York or Georgia); final artwork would draw it from Newsreader and outline it.

**A consistent family built on the lowercase Masthead h**, the icon the CEO liked:

| Hybrid A (cream, plum, apricot) | Hybrid B (black, white, one orange) |
|---|---|
| **A. Masthead h**: cream h on plum with a single apricot underline (round 1's double rule, simplified). *My pick for A* | **A. h with a cursor bar**: white h on black, a short orange bar at its foot. Static: a bar, never a blinking cursor. *My pick for B* |
| **B. h on a card**: plum h on a cream card on apricot, echoing the app's own cards | **B. Entries**: Ledger's Entries, the one Ledger icon the CEO liked, unchanged. It has no h, so it is the odd one out of the family |
| **C. h, full stop**: plum h with an apricot full stop, as a newspaper would set a name. Strong at 29 px | **C. Prompt h**: an orange `>` before a white h. *Risk:* the chevron reads as "play" or "next" [J] |

**Every icon passed the round-1 checks on the sheet** [J]: legible at 60 and 29 px, in one colour, in greyscale, with no ghost, eye, pin, radar, route, headstone, glass or bottle. **A letter-based icon has one cost, stated in round 1 and unchanged:** if PLAT-6's name checks force a rename away from "h", the icon goes with the name. Apple permits a first-letter mnemonic (round 1, `icon-brief.md` §2.1, E1).

---

## 4. Liquid Glass (written first, because it changes both hybrids)

### 4.1 What Apple says, retrieved

- **Glass is for controls and navigation, not content:** *"Liquid Glass forms a distinct functional layer for controls and navigation elements — like tab bars and sidebars — that floats above the content layer"*, and *"Don't use Liquid Glass in the content layer."* [E, HIG Materials]. **So only the tab bar is glass**, and so are the floating add button and sheets if the CTO adopts system components. Cards, the headline and rows are never glass.
- **Two variants:** *"The regular variant blurs and adjusts the luminosity of background content to maintain legibility"*; the clear variant is *"highly translucent"* and is for *"components that float above media backgrounds"* [E]. **Haunts uses the regular variant only.**
- **Tab bars float:** *"A tab bar floats above content at the bottom of the screen. Its items rest on a Liquid Glass background that allows content beneath to peek through."* [E, HIG Tab bars].
- **Accessibility settings change the material:** its appearance *"can differ in response to certain system settings, like … accessibility settings that reduce transparency or increase contrast"* [E, HIG Materials].

### 4.2 The measurement, and what it forced

`tools/glass.py` models the bar as its tint laid over content at some opacity, and sweeps **every colour on a 16-step grid of the sRGB cube** (4,096 colours, including black and white) as the content beneath. It blends two ways, in gamma-encoded sRGB and in linear light, and keeps the stricter answer. **Blur only averages what is beneath, so a solid block of the worst colour is the worst case** [I]. The real material also adjusts luminosity, which should help; **the design does not rely on it** [J].

**First pass: the round-1 approach failed in dark mode.** With idle tabs in secondary text colour and a bar 80% opaque, idle labels fell to **1.61–1.91:1** over white content: a white photo thumbnail, the apricot headline card or Hybrid B's white "Review" button scrolling under the bar. **Redesigned:**

1. **Every tab label and icon uses full-strength text colour.** The selected tab is shown by a **solid pill** with its label on it, which is shape as well as colour (A11Y-2), and which contrast.py measures as an ordinary opaque pair.
2. **Bar opacity: 80% in light mode, 90% in dark.** These are the smallest values at which everything passes:

| Hybrid, mode | Idle label and icon on bar, worst case | Selected pill against bar, worst case | Opacity needed (all labels) |
|---|---|---|---|
| A, light | **10.27:1** (needs 4.5) | **6.17:1** (needs 3.0) | 0.56 |
| A, dark | **5.61:1** | **3.13:1** | **0.90** |
| B, light | **11.76:1** | **11.76:1** | 0.49 |
| B, dark | **5.87:1** | **5.87:1** | 0.86 |

*(Full output: §9, appendix B. Light-mode worst content is black; dark-mode worst content is white.)*

**What this means in plain terms: glass that passes the accessibility baseline over anything is mostly frosted, not clear.** At 80–90% opacity content shows through as a soft tint and movement, not as readable detail. **That is still the benefit the CEO asked for**: content runs the full height of the screen and scrolls behind the bar, so the screen feels taller. It is not see-through glass [J].

### 4.3 The floating bar and the vertical space, honestly

- **What is gained:** round 1's bar was a full-width, opaque 84 pt band. The floating bar is **64 pt tall, inset 16 pt at each side, and content scrolls beneath it**, so the list visibly continues to the bottom edge. **Roughly 40–80 pt of extra visible content** on a 390 × 844 screen, depending on scroll position [J, from the mockups].
- **What must be protected: SC 2.4.11 Focus Not Obscured (AA)**, *"When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content"*, and W3C names *"sticky footers"* as the typical offender [E]. **So the list carries bottom padding equal to the bar's height plus its margin**, so the last row can always scroll clear of the bar, and focus movement scrolls the focused row into the clear area. **Proposed acceptance criterion:** with Full Keyboard Access or Switch Control, step through every row; assert no focused row is entirely beneath the bar.
- **Minimise on scroll** (the bar shrinking as the user scrolls down) exists in iOS [E, HIG Tab bars, described for bars with an accessory]. **I do not propose it:** it is motion on every scroll, and four labelled tabs are clearer than a shrunken bar [J].

### 4.4 Reduce Transparency, Increase Contrast, and Android

| State | What the bar does | Measured |
|---|---|---|
| **Default (iOS)** | Regular glass, tint at 80% (light) / 90% (dark), a 1 px hairline edge | §4.2 |
| **Reduce Transparency on** | **Fully opaque** `surface` colour, same shape, same place. No blur | Labels are ordinary opaque pairs, all pass (appendix A) |
| **Increase Contrast on** | Opaque, plus a **1.5 pt edge** in secondary text colour | Edge against page and cards **≥ 3:1** in both hybrids and modes (appendix A, "Tab bar edge, Increase Contrast") |
| **Both on** | As Increase Contrast | As above |
| **Android (all versions)** | **The same floating pill, opaque `surface` with a soft elevation shadow and a 1 px outline. No blur** | Same as Reduce Transparency |

**Why Android gets no blur, as judgment:** Android has no system equivalent of Liquid Glass [K, high confidence], and a blur behind a view is platform- and version-dependent to build [K, medium confidence: I believe Android's `RenderEffect` blur arrived in API 31 and blurs the view it is applied to rather than what lies behind it, but its reference page did not render for me]. **An opaque pill in the same place looks deliberate, costs little, and passes contrast by construction** [J]. Same geometry on both platforms keeps THEME-1's rule that layout never differs.

### 4.5 What the CTO must confirm, not assumed here

1. **Whether React Native with Expo can render the system's own Liquid Glass tab bar**, or only an imitation. I believe Expo has published modules for glass effects and blur, and that native tab navigators can use the system tab bar [K, low confidence; not retrieved]. **The distinction matters:** the system bar adapts to Reduce Transparency and Increase Contrast by itself; an imitation must detect both settings and be tested for both.
2. **Whether React Native exposes Reduce Transparency and Increase Contrast** on iOS, and what the Android equivalents are. HEAD-10 has already shown that React Native's reduce-motion check misses Android's accessibility switch, so **no platform setting should be assumed readable until tested on a device**.
3. **Performance** of a blurred bar over a long list on the oldest iPhone that runs iOS 26 (PLAT-8(c)'s device matrix).
4. **If the answer to 1 is "imitation only", my recommendation changes:** ship the opaque floating pill on both platforms (the Android fallback everywhere) and add real glass later. The vertical-space benefit survives; only the translucency is lost.

---

## 5. The ticker in the modern themes

**Sheet:** `concepts/ticker-modern.svg`: Hybrid A (light) and Hybrid B (dark) with the Ticker chosen, and the proposed Rotate variant in all four hybrid-and-mode combinations.

**Unchanged rules.** The ticker appears **only if the user chooses it** (HEAD-2); no theme switches it on (round 1, THEME-3). One pass per open, a visible pause control that remembers being paused (HEAD-9), and the still Line under Reduce Motion, a screen reader or accessibility text sizes (HEAD-10, HEAD-11). WCAG 2.2 SC 2.2.2 requires *"a mechanism for the user to pause, stop, or hide it"* for moving content that starts automatically and lasts over five seconds [E, round 1].

**What makes the modern crawl "more user friendly"** [J]:

1. **It lives inside the headline card**, not in a separate strip, so the kicker stays still and only the sentence moves.
2. **Faded edges**, so words slide in and out instead of being cut in half.
3. **Slow and constant**, with no easing to catch the eye. The speed is a named constant UX signs off on a device (HEAD-9).
4. **Pause and options side by side at 44 pt**, both labelled for assistive technology.
5. **It rests on a whole sentence** at the end of its pass, never mid-word.
6. **Touching or scrolling the list pauses it** for that open [J, a proposal, not yet a requirement].

**Proposal: "Rotate", which I think is the genuinely friendlier ticker** [J]. It shows **one whole fact at a time** for about 6 seconds, cross-fades to the next, goes round once per open, then rests on the first. Whole sentences are easier to read than crawling text, and W3C's own concern with moving content is *"anyone who has trouble reading stationary text quickly"* (`ux-home-headlines.md` §2.3, [E]). **It still moves, so it keeps every duty:** a pause control, the fallbacks, one cycle per open, no novelty treatment. **It is a requirements change:** HEAD-2 defines the Ticker as *"scrolls all eligible facts"*, so Rotate needs a §24 row (PM/BA) whichever way it goes. The options are to offer Rotate *instead of* the crawl, or as a fifth appearance. **My recommendation is instead**: two moving appearances would be one more choice than anyone needs [J].

---

## 6. "Possibly procedurally generated": more variety, inside the rules

Headlines are already generated on the phone from a **fixed template catalogue** (HEAD-4: *"Headlines come only from the enumerated template catalogue (T1–T9)"*), and D42 sets the bound: *"more variety within MEM-1 and HEAD-6, never novelty or counts."*

**How to get more variety** [J]:

1. **More templates.** Each new one goes through a §24 row, UX review against MEM-1 and HEAD-6, and QA's string search, as HEAD-4 requires today.
2. **Several phrasings per template** (for example three for T3), chosen **deterministically from the date**, so the daily fixed cycle (HEAD-3) and QA's ability to list every possible sentence are both kept.
3. **Seasonal and date framing** from data the journal already holds (dates and categories), never from anything it does not (HEAD-4(d)).

**Candidate new templates, with example lines** (fictional venues; thresholds for UX to set under HEAD-14):

| Candidate | Example | Why it is inside the line |
|---|---|---|
| **On this day** (extends T5 beyond first visits) | *"On this day in 2024: Northgate Theatre."* | A memory, dated. Nothing to beat |
| **Seasonal memory** | *"Last autumn: your first visit to Regent Cinema."* | A span and a first time, stated once |
| **A pairing, as a ritual** | *"Mill Lane Bakery, then Regent Cinema: a Saturday habit since 2024."* | Describes a ritual (T4's register). *Watch:* never "twice this month" |
| **Neighbourhood** | *"Most of the cafés in your journal are around Mill Road."* | A fact about places. Location-revealing, but D20's refinement withdrew that concern, except for the app-switcher (HEAD-12) |
| **A kind of place** | *"The theatre you've rated highest: Northgate Theatre, 5/5."* | T6's register for another category |
| **Alternative phrasings of T3** | *"Since March 2023: The Brass Kettle."* / *"The Brass Kettle has been one of yours since 2023."* | Same fact, different words |

**What is out, however "procedural"** (MEM-1, HEAD-6, HEAD-4, HEAD-8):

- **Anything written freely by a model at run time.** It cannot be reviewed, it breaks HEAD-4's fixed catalogue, and on-device generation would be a large new component. *"Procedural" here means templates and phrasings, not an AI writing sentences.*
- **Randomness per open.** A new surprise on each open is a variable reward (HEAD-3's reasoning).
- **Counts over a window, streaks, records, rates, comparisons of periods**: *"3 cafés this week"*, *"your busiest month"*, *"4 Fridays in a row"*, *"more than last year"*.
- **Novelty and absence**: *"New place!"*, *"First time in ages"*, *"You haven't been to The Anchor in a while"*, *"days since"*.
- **Nights and drinking**: *"Out till 2am"*, *"a big Saturday night"*, *"your local"* as praise, anything about drinks. The journal does not know what anyone drank, and must not guess (HEAD-4(d), MEM-1).
- **Emoji, exclamation marks and "!"-energy** (HEAD-6(a)).

---

## 7. Contour: one touch, kept

**Sheet:** `concepts/contour-touch.svg`.

**The one touch I propose: contour lines as texture in the empty band at the top of the self-portrait screen (LOOK-8) and the heatmap screen (LOOK-2), in both hybrids.** They are drawn in the accent colour at low strength, **open lines that never close into rings** (closed rings read as a target or radar, round 1 §5), **never behind text or controls**, and **never on the home screen**. It ties the lines the CEO liked to the two screens that are about places over time, where a cartographic hint is most apt and least like tracking [J]. **Cost** [J]: a day, as one decorative asset per mode.

**Not proposed now, and still available:** round 1's idea of a later, optional Contour theme with its colours and the Horizon icon (`themes.md` §4.3). It stays a later candidate because each extra theme adds a column to every verification pass. **Kept out in any form:** pins, dotted routes, footprints, concentric rings and the folded-map icon (D9, D42(3)).

---

## 8. Homepage (retro): kept, with the bar answered

**Sheet:** `concepts/homepage-floating-bar.svg`.

**Does the retro theme get glass? No** [J]. Three reasons:

1. **The period was opaque.** Bevelled grey buttons and gradient title bars are the look; translucency is the one thing the early-2000s web did not have.
2. **Text over translucency on the retro theme's pale boxes and gradients** is text on texture, which round 1 banned because it cannot be measured.
3. **Cost:** a glass retro bar would double the retro theme's contrast testing (glass states × modes) for no gain in character.

**But it gets the same bar geometry.** Round 1's rule is that themes never change layout (`themes.md` §2, THEME-1), so **Homepage's bar floats in the same place, at the same size, with the same four tabs**, drawn as an opaque bevelled panel with bevelled tabs. **The vertical-space gain is the same in every theme**; only the material differs. Everything else about Homepage is unchanged from round 1, and its guardrails (`themes.md` §8.3) stand.

---

## 9. Evidence register and appendices

**Retrieved by this seat for round 2 (2026-09-27):**

| # | Claim | Source |
|---|---|---|
| E1 | Liquid Glass is for the controls and navigation layer, not content; regular and clear variants; appearance changes with Reduce Transparency and Increase Contrast; *"use vibrant colors on top of materials"* | [Apple HIG, Materials (JSON of the page)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/materials.json) |
| E2 | *"A tab bar floats above content at the bottom of the screen"*; minimising on scroll; *"Use single words"* for tab labels | [Apple HIG, Tab bars (JSON of the page)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/tab-bars.json) |
| E3 | SC 2.4.11 Focus Not Obscured (Minimum), AA; sticky footers as the typical offender | [W3C Understanding 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) |
| — | Round 1's register (OFL licences, SC 1.4.3, 1.4.11, 2.2.2, 2.3.1, relative luminance, store icon specs) | `../brand-directions.md` §9, `../themes.md` §11, `../icon-brief.md` §7 |

**Tried and failed:** Android's `RenderEffect` reference page did not render for the retrieval tool, so every Android blur statement is [K].
**[K], not retrieved:** Expo and React Native support for native Liquid Glass and for reading Reduce Transparency and Increase Contrast (the CTO's to confirm, §4.5); Android's lack of a system glass material.

**Negative findings, with what would overturn each** (the charter's duty):

| Finding | Overturned by | Where I looked |
|---|---|---|
| Legible glass must be ≥ 80% opaque (light) and ≥ 90% (dark) | An on-device measurement showing the system's adaptive material keeps labels at 4.5:1 over white content at lower opacity. Apple's adaptive luminosity may do exactly that, but I cannot measure it from here | `tools/glass.py`, a model that ignores adaptation |
| Retro gets no glass | The CEO preferring the look, accepting the extra testing | Judgment; round 1's texture rule |
| Free-text generation of headlines is out | A design in which generated text is constrained to reviewable templates, which is what §6 already proposes | HEAD-4, HEAD-6, MEM-1 |

**Appendix A:** the full opaque-pair tables for both hybrids and Homepage are produced by `python3 tools/contrast.py --round2`: **76 hybrid pairs, all pass** (Homepage's 50 unchanged from round 1); the output is pasted unedited at the end of this document. **Appendix B:** glass results, `python3 tools/glass.py`, reproduced here:

| Hybrid | Mode | Label | Colour | Minimum opacity to pass | At opacity used | Worst content (model) |
|---|---|---|---|---|---|---|
| A | light | idle tab label and icon | `#241B2F` | 0.53 | **10.27:1** at 0.80 | black |
| A | light | selected pill vs bar | `#5B2A86` | 0.56 | **6.17:1** at 0.80 | black |
| A | dark | idle tab label and icon | `#F6EFE8` | 0.86 | **5.61:1** at 0.90 | white |
| A | dark | selected pill vs bar | `#C9A7F0` | 0.90 | **3.13:1** at 0.90 | white |
| B | light | idle tab label and icon | `#111111` | 0.49 | **11.76:1** at 0.80 | black |
| B | light | selected pill vs bar | `#111111` | 0.38 | **11.76:1** at 0.80 | black |
| B | dark | idle tab label and icon | `#F2F2F0` | 0.86 | **5.87:1** at 0.90 | white |
| B | dark | selected pill vs bar | `#F2F2F0` | 0.75 | **5.87:1** at 0.90 | white |

---

## 10. Recommendation, cost and the next decision

**Hybrid A as the brand and the modern default** [J], for three reasons:

1. **It is what the CEO's feedback converges on:** Almanac's type, which he kept; Doorway's colours, which he preferred; and less busy than Almanac, which he asked for.
2. **It is the kinder of the two for everyday users**, the charter's first test. Hybrid B's `//` and `>` are charming to some and a small puzzle to others.
3. **It holds MEM-1 easily:** warmth sits on one card holding a memory, not on counts or celebration.

**Hybrid B: keep it as the first additional theme, not discard it** [J]. Because it shares A's type, icons, layout and bar, it is a set of token values plus a monospace for metadata, so it is **the cheapest possible third theme**. The proposed set becomes **A (default), Homepage (retro), and B ("Mono") as the first addition**, with Contour later if ever. Round 1's caution stands: each theme adds 15–25% to UI verification [J].

**Cost, as [J] for the CTO to size** (none of it in the 2,090-hour estimate):

| Item | Estimate [J] |
|---|---|
| Floating tab bar, opaque version (all platforms) | 1–2 days |
| Real glass on iOS, if the CTO confirms feasibility, plus Reduce Transparency and Increase Contrast states | 2–4 days, and a device-test burden every release |
| Modern ticker styling (crawl) in each theme | 1 day per theme; the behaviour is HEAD-9–11 work already counted |
| Rotate, if adopted | 1–2 days, plus the §24 change |
| Extra templates and phrasings (§6) | ~0.5 day per template including review, plus QA string search |
| Contour texture (§7) | ~1 day |
| Hybrid B as a theme | 2–3 days, plus the per-theme verification share |

**The one decision the CEO should make next: Hybrid A or Hybrid B as the brand and default.** The icon (A's Masthead h or B's cursor-bar h), the theme set and the icon brief's final wording all follow from it. The glass, ticker and template proposals can wait until after.

---

## Appendix A: measured contrast, opaque pairs (output of `tools/contrast.py --round2`, unedited)

#### Hybrid A: warm editorial (Almanac type, Doorway colour) (`hybrid_a`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#241B2F` | `#FFF8F1` | **15.67:1** | 4.5:1 | pass |
| light | Body text on row/card | `#241B2F` | `#FFFFFF` | **16.50:1** | 4.5:1 | pass |
| light | Secondary text on page | `#5C5266` | `#FFF8F1` | **6.99:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#5C5266` | `#FFFFFF` | **7.36:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#5B2A86` | `#FFF8F1` | **9.41:1** | 4.5:1 | pass |
| light | Link on row/card | `#5B2A86` | `#FFFFFF` | **9.90:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#5B2A86` | **9.90:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#5B2A86` | `#FFFFFF` | **9.90:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#5B2A86` | `#FFF8F1` | **9.41:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#9A4D00` | `#FFFFFF` | **6.11:1** | 4.5:1 | pass |
| light | Control border on row/card | `#8C7F99` | `#FFFFFF` | **3.74:1** | 3.0:1 | pass |
| light | Control border on page | `#8C7F99` | `#FFF8F1` | **3.56:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#5B2A86` | `#FFFFFF` | **9.90:1** | 3.0:1 | pass |
| light | Focus ring on page | `#5B2A86` | `#FFF8F1` | **9.41:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#B45309` | `#FFFFFF` | **5.02:1** | 3.0:1 | pass |
| light | Headline card text on apricot | `#241B2F` | `#F2A65A` | **8.15:1** | 4.5:1 | pass |
| light | Idle tab label on opaque bar | `#241B2F` | `#FFFFFF` | **16.50:1** | 4.5:1 | pass |
| light | Tab bar edge, Increase Contrast, on page | `#5C5266` | `#FFF8F1` | **6.99:1** | 3.0:1 | pass |
| light | Tab bar edge, Increase Contrast, on cards | `#5C5266` | `#FFFFFF` | **7.36:1** | 3.0:1 | pass |
| dark | Body text on page | `#F6EFE8` | `#1A1422` | **15.79:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#F6EFE8` | `#251D30` | **14.21:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#B9AFC4` | `#1A1422` | **8.56:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#B9AFC4` | `#251D30` | **7.70:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#C9A7F0` | `#1A1422` | **8.80:1** | 4.5:1 | pass |
| dark | Link on row/card | `#C9A7F0` | `#251D30` | **7.92:1** | 4.5:1 | pass |
| dark | Label on primary button | `#24123A` | `#C9A7F0` | **8.40:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#F5B77A` | `#251D30` | **9.20:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#F5B77A` | `#1A1422` | **10.23:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#F5B77A` | `#251D30` | **9.20:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#7E7190` | `#251D30` | **3.59:1** | 3.0:1 | pass |
| dark | Control border on page | `#7E7190` | `#1A1422` | **3.99:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#C9A7F0` | `#251D30` | **7.92:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#C9A7F0` | `#1A1422` | **8.80:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#F5B77A` | `#251D30` | **9.20:1** | 3.0:1 | pass |
| dark | Headline card text on apricot | `#241B2F` | `#F5B77A` | **9.38:1** | 4.5:1 | pass |
| dark | Idle tab label on opaque bar | `#F6EFE8` | `#251D30` | **14.21:1** | 4.5:1 | pass |
| dark | Tab bar edge, Increase Contrast, on page | `#B9AFC4` | `#1A1422` | **8.56:1** | 3.0:1 | pass |
| dark | Tab bar edge, Increase Contrast, on cards | `#B9AFC4` | `#251D30` | **7.70:1** | 3.0:1 | pass |

#### Hybrid B: mono editorial (Ledger monochrome, Almanac type) (`hybrid_b`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#111111` | `#FAFAF8` | **18.07:1** | 4.5:1 | pass |
| light | Body text on row/card | `#111111` | `#FFFFFF` | **18.88:1** | 4.5:1 | pass |
| light | Secondary text on page | `#555555` | `#FAFAF8` | **7.13:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#555555` | `#FFFFFF` | **7.46:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#111111` | `#FAFAF8` | **18.07:1** | 4.5:1 | pass |
| light | Link on row/card | `#111111` | `#FFFFFF` | **18.88:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#111111` | **18.88:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#555555` | `#FFFFFF` | **7.46:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#555555` | `#FAFAF8` | **7.13:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#B93D0B` | `#FFFFFF` | **5.62:1** | 4.5:1 | pass |
| light | Control border on row/card | `#767676` | `#FFFFFF` | **4.54:1** | 3.0:1 | pass |
| light | Control border on page | `#767676` | `#FAFAF8` | **4.35:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#C2410C` | `#FFFFFF` | **5.18:1** | 3.0:1 | pass |
| light | Focus ring on page | `#C2410C` | `#FAFAF8` | **4.96:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#111111` | `#FFFFFF` | **18.88:1** | 3.0:1 | pass |
| light | Idle tab label on opaque bar | `#111111` | `#FFFFFF` | **18.88:1** | 4.5:1 | pass |
| light | Monospace metadata on row | `#555555` | `#FFFFFF` | **7.46:1** | 4.5:1 | pass |
| light | Tab bar edge, Increase Contrast, on page | `#555555` | `#FAFAF8` | **7.13:1** | 3.0:1 | pass |
| light | Tab bar edge, Increase Contrast, on cards | `#555555` | `#FFFFFF` | **7.46:1** | 3.0:1 | pass |
| dark | Body text on page | `#F2F2F0` | `#0F0F10` | **17.09:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#A3A3A0` | `#0F0F10` | **7.58:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#A3A3A0` | `#1A1A1C` | **6.87:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#F2F2F0` | `#0F0F10` | **17.09:1** | 4.5:1 | pass |
| dark | Link on row/card | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 4.5:1 | pass |
| dark | Label on primary button | `#111111` | `#F2F2F0` | **16.85:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#A3A3A0` | `#1A1A1C` | **6.87:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#A3A3A0` | `#0F0F10` | **7.58:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#FB923C` | `#1A1A1C` | **7.68:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#76767A` | `#1A1A1C` | **3.84:1** | 3.0:1 | pass |
| dark | Control border on page | `#76767A` | `#0F0F10` | **4.24:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#FB923C` | `#1A1A1C` | **7.68:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#FB923C` | `#0F0F10` | **8.46:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 3.0:1 | pass |
| dark | Idle tab label on opaque bar | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 4.5:1 | pass |
| dark | Monospace metadata on row | `#A3A3A0` | `#1A1A1C` | **6.87:1** | 4.5:1 | pass |
| dark | Tab bar edge, Increase Contrast, on page | `#A3A3A0` | `#0F0F10` | **7.58:1** | 3.0:1 | pass |
| dark | Tab bar edge, Increase Contrast, on cards | `#A3A3A0` | `#1A1A1C` | **6.87:1** | 3.0:1 | pass |

#### Homepage (retro, c. 2001-2004) (`homepage`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#1A1A1A` | `#DCE4F0` | **13.59:1** | 4.5:1 | pass |
| light | Body text on row/card | `#1A1A1A` | `#FFFFFF` | **17.40:1** | 4.5:1 | pass |
| light | Secondary text on page | `#4A4A4A` | `#DCE4F0` | **6.92:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#4A4A4A` | `#FFFFFF` | **8.86:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#0033CC` | `#DCE4F0` | **6.99:1** | 4.5:1 | pass |
| light | Link on row/card | `#0033CC` | `#FFFFFF` | **8.95:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#0033CC` | **8.95:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#1A1A1A` | `#FFFFFF` | **17.40:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#1A1A1A` | `#DCE4F0` | **13.59:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#A33A00` | `#FFFFFF` | **6.64:1** | 4.5:1 | pass |
| light | Control border on row/card | `#5E7FA3` | `#FFFFFF` | **4.17:1** | 3.0:1 | pass |
| light | Control border on page | `#5E7FA3` | `#DCE4F0` | **3.25:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#0033CC` | `#FFFFFF` | **8.95:1** | 3.0:1 | pass |
| light | Focus ring on page | `#0033CC` | `#DCE4F0` | **6.99:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#B36B00` | `#FFFFFF` | **4.18:1** | 3.0:1 | pass |
| light | Title-bar text on lighter end of gradient | `#FFFFFF` | `#2D5AA0` | **6.81:1** | 4.5:1 | pass |
| light | Title-bar text on darker end of gradient | `#FFFFFF` | `#16336B` | **12.21:1** | 4.5:1 | pass |
| light | Box heading on box title strip (lower end of gradient) | `#16336B` | `#D3DFF0` | **9.06:1** | 4.5:1 | pass |
| light | Box heading on box title strip (upper end of gradient) | `#16336B` | `#FFFFFF` | **12.21:1** | 4.5:1 | pass |
| light | Selected tab label | `#1A1A1A` | `#F4B860` | **9.84:1** | 4.5:1 | pass |
| light | Idle tab label (link colour) | `#0033CC` | `#E6ECF5` | **7.54:1** | 4.5:1 | pass |
| light | Ticker text on ticker strip | `#1A1A1A` | `#FFFFCC` | **16.93:1** | 4.5:1 | pass |
| light | Bevel button label | `#1A1A1A` | `#ECE9D8` | **14.27:1** | 4.5:1 | pass |
| light | Bevel button edge on content | `#716F64` | `#FFFFFF` | **5.05:1** | 3.0:1 | pass |
| light | Bevel button edge on its own face | `#716F64` | `#ECE9D8` | **4.14:1** | 3.0:1 | pass |
| dark | Body text on page | `#E8E8E8` | `#000022` | **16.75:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#E8E8E8` | `#0B0B33` | **15.44:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#B4B4C8` | `#000022` | **10.07:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#B4B4C8` | `#0B0B33` | **9.28:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#66CCFF` | `#000022` | **11.38:1** | 4.5:1 | pass |
| dark | Link on row/card | `#66CCFF` | `#0B0B33` | **10.49:1** | 4.5:1 | pass |
| dark | Label on primary button | `#000022` | `#66CCFF` | **11.38:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#FFCC66` | `#0B0B33` | **12.69:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#FFCC66` | `#000022` | **13.76:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#FFB870` | `#0B0B33` | **11.12:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#6D7FB0` | `#0B0B33` | **4.79:1** | 3.0:1 | pass |
| dark | Control border on page | `#6D7FB0` | `#000022` | **5.19:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#66CCFF` | `#0B0B33` | **10.49:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#66CCFF` | `#000022` | **11.38:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#FFCC66` | `#0B0B33` | **12.69:1** | 3.0:1 | pass |
| dark | Title-bar text on lighter end of gradient | `#FFFFFF` | `#33337A` | **11.08:1** | 4.5:1 | pass |
| dark | Title-bar text on darker end of gradient | `#FFFFFF` | `#1B1B55` | **15.74:1** | 4.5:1 | pass |
| dark | Box heading on box title strip (lower end of gradient) | `#FFCC66` | `#1B1B55` | **10.55:1** | 4.5:1 | pass |
| dark | Box heading on box title strip (upper end of gradient) | `#FFCC66` | `#2E2E78` | **7.92:1** | 4.5:1 | pass |
| dark | Selected tab label | `#000022` | `#FFCC66` | **13.76:1** | 4.5:1 | pass |
| dark | Idle tab label (link colour) | `#66CCFF` | `#16164A` | **9.33:1** | 4.5:1 | pass |
| dark | Ticker text on ticker strip | `#FFFF99` | `#1A1A00` | **16.80:1** | 4.5:1 | pass |
| dark | Bevel button label | `#E8E8E8` | `#2B2B5E` | **10.65:1** | 4.5:1 | pass |
| dark | Bevel button edge on content | `#8A8AC0` | `#0B0B33` | **5.84:1** | 3.0:1 | pass |
| dark | Bevel button edge on its own face | `#8A8AC0` | `#2B2B5E` | **4.02:1** | 3.0:1 | pass |

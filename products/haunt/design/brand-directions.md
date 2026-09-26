# Haunts brand directions: four options for the CEO

**Seat:** UX / Design Lead · **Date:** 2026-09-26 · **Slug:** `haunt` · **Commission:** **D38** (CEO, 2026-09-26), read at `decisions/2026-09-16-haunt-gate.md` in the coordinator's worktree, because this worktree's copy of the record predates D38.
**Companion files:** [`themes.md`](themes.md) (the theme system and the retro theme), [`icon-brief.md`](icon-brief.md) (PLAT-7), [`concepts/`](concepts/) (26 SVGs), [`tools/`](tools/) (the palette source, the contrast measurement script and the SVG generator).
**Status:** this note prepares and flags. It does not certify (Constitution 6.1). **Nothing in it is adopted.** D38: *"They come back to the CEO for sign-off before any is adopted; nothing is adopted by this decision."*
**Template note:** `pipeline/templates/` holds no design or UX template (listed this session: `cost-sheet.md`, `decision-record.md`, `dissent-memo.md`, `gate-pack.md`, `idea-brief.md`, `proposal.md`, `requirements.md`, `research-brief.md`, `review-pack.md`). This note follows the commission's list of contents instead, and says so rather than departing silently.
**Evidence:** tagged under `pipeline/evidence-standard.md`. Every [E] was retrieved on **2026-09-26** and is listed with its link in §9. **Contrast ratios are arithmetic, not evidence**: they are computed by `tools/contrast.py` from the hex values in `tools/palettes.py` with the W3C formula, and anyone can re-run them. Taste is tagged [J], and most of this document is taste.

**The honesty statement, as in my earlier notes.** I have shown these concepts to **nobody**. No user has seen them, no preference test has been run, and a design direction is exactly the kind of thing people judge differently from the person who drew it. The fonts in the SVGs are **stand-ins** (§1.3). What would overturn my recommendation is in §8.

---

## 0. The answer, before the reasoning

| # | Direction | In one line | Risk in one line |
|---|---|---|---|
| **1** | **Almanac** | A well-kept notebook with a newspaper's manners: warm paper, an editorial serif, ink blue, one vermilion rule. | Can read as a news app or a generic journal; the page icon can read as a file icon. |
| **2** | **Doorway** | Bold and warm: plum and apricot, a constructed lowercase wordmark, arches as the motif. The most distinctive. | An arch can read as a **headstone** in a product called Haunts. My first draft did; I redrew it. |
| **3** | **Ledger** | Quiet and precise: near-monochrome, a monospace for times and facts, one orange signal. The privacy tool. | The least distinctive. Can feel cold, and reads as a notes or developer tool. |
| **4** | **Contour** | Cartographic: Ordnance Survey greens, contour lines, italic place names. | **Pulls the brand towards maps, which is towards tracking**, the association D9 exists to refuse. I recommend against it. |

**My recommendation: Almanac as the brand and the modern default, with Doorway's warmth held as an option if the CEO finds Almanac too quiet** (§7). Almanac is the only direction whose metaphor is the product itself: a private record of places, kept like a notebook, with headlines set like a newspaper's. That matches the register the headline note already chose (`ux-home-headlines.md` §4.4: *"a **newspaper masthead, not a rolling-news ticker**"*). It also pairs naturally with the retro theme, which is also about news.

**The first decision the CEO should make: which direction, if any, becomes the brand.** Everything else (the theme set, the icon, the brief's final wording) follows from that choice, and none of it should be decided first.

**What every direction shares, so the comparison is fair.** The same home screen: the same headline, the same confirm queue, the same timeline, the same four tabs, in the same order. Only colour, type, shape, iconography and texture differ. That is the theme rule in `themes.md` §2 applied to the brand directions too, so the CEO is comparing looks and not layouts.

---

## 1. What binds every direction

### 1.1 The constraints, quoted

- **MEM-1** (`requirements.md` §3.1, BLOCKING): *"Haunts never encourages drinking, and never rewards the frequency or volume of visits, anywhere in the product."* The test: *"If the user could 'beat' it or 'break' it, it is out."* **Applied to visual design** [J, this seat's reading]: no pint glasses, wine glasses, cocktails, bottles, "cheers", neon bar signage, confetti, trophies, flames, stars-as-reward, progress rings, level bars or badges. **Stars appear only as the user's own rating**, always with the number as text (A11Y-2). And because the index holds **346,184** venues rather than **42,407** pubs (D9), the imagery must not narrow the product to a night out: no moon-and-cocktail "evening" palettes.
- **D9 and D11(d):** the mark *"excludes ghost, eye and tracking imagery"*. D9's reason: *"being invisibly followed is precisely the association the product exists to refuse."* **I extend it in two places, as judgment:** (a) **no map pins anywhere in the interface**, including the Places tab, which uses an awning in every mockup; and (b) **no concentric rings, radar sweeps, footprints or dotted routes**, which read as tracking just as surely as an eye does.
- **Accessibility**, Constitution Article 4: *"Meet accessibility standards (**WCAG 2.2 AA** as the working baseline, read through **WCAG2ICT** where the product is native software…)"*. For colour that means SC 1.4.3, *"a contrast ratio of at least 4.5:1"* for text and 3:1 for large text, and SC 1.4.11, *"a contrast ratio of at least 3:1 against adjacent color(s)"* for user-interface components and graphical objects [E, W3C Understanding 1.4.3 and 1.4.11]. **Every direction is measured in light and dark in §6 and passes every pair listed.**
- **Protective defaults (DFLT-1)** and **no novelty treatment on headlines (HEAD-8)**: *"No "NEW", "BREAKING", dot, badge, count, red or warning colour, flashing, entry animation or coach-mark."* This is why no direction uses red as a headline colour. Almanac's vermilion kicker is a brick red-brown at 5.78:1; I judge it reads as print ink, not as a warning, but the CEO should look at it with that clause in mind [J].

### 1.2 The tokens every direction defines

One set of names, so a theme is a swap of values and never a change of code paths (`themes.md` §3). Defined in `tools/palettes.py`:

| Token | Used for | Requirement |
|---|---|---|
| `bg`, `surface` | Page; rows and cards | None of its own |
| `text`, `text2` | Primary and secondary text | 4.5:1 on `bg` and `surface` |
| `primary`, `on_primary` | Links, primary buttons, the selected tab | 4.5:1 as text; label on button 4.5:1 |
| `kicker` | The headline's label, e.g. "From your journal" | 4.5:1 |
| `unconfirmed` | The "Unconfirmed" state label (always a word and a dashed outline, never colour alone) | 4.5:1 |
| `outline`, `focus`, `star` | Control borders, focus ring, rating glyphs | 3:1 (SC 1.4.11) |
| `accent`, `divider` | The mark, decorative rules, hairlines | Decorative only; never the sole carrier of meaning |

### 1.3 Type: what may be bundled, and what the SVGs actually show

**Only fonts licensed for bundling in a paid app are proposed.** Every proposed family is under the **SIL Open Font License 1.1** or, for one retro fallback, the Bitstream Vera licence. The OFL FAQ answers the question directly: bundling in commercial software is permitted, *"Examples of bundling made possible by the OFL would include: … mobile device applications"* [E, OFL FAQ 1.4]. Three conditions travel with it [E, OFL FAQ 1.20, 1.5–1.6, 3.1]:

1. **Ship the copyright statement, licence notice and licence text** with the app. *"A mention of this information in your About box … is good practice."* **This belongs in the LIC section of `requirements.md`**, as an attribution row beside the Overture one (PM/BA, §24 row).
2. **Never sell the font by itself.** Irrelevant to an app, and satisfied.
3. **Reserved Font Names.** Where a font declares one, a modified version must be renamed. **IBM Plex reserves "Plex" and Source Sans 3 reserves "Source"** [E, their OFL files]. Whether **subsetting** a font to shrink the app counts as modification is a question I did not retrieve an answer to [K, low confidence: I believe the OFL FAQ treats subsetting as a modification]. **It matters only for Ledger and Contour**, and is a **flag for the CGO**, who owns licence questions (Constitution 6.1: *"third-party licence terms whose interpretation determines a product's architecture or cost"*), not a finding.

**Excluded, and why:** Verdana, Georgia, Tahoma, Trebuchet MS, Helvetica, Avenir and Gill Sans. They are proprietary system or commercial fonts and are **not** licensed for bundling in an app [K, high confidence, not retrieved; excluded on the cautious side]. The retro theme needs the Verdana-and-Georgia look above all, which is why it uses **Gelasio**, an OFL face that is *"metrics compatible with Georgia"* [E, Gelasio README], and **DejaVu Sans**, which is not a Verdana clone but shares its wide, open proportions [J].

**The SVGs use stand-ins, and say so.** Each SVG names the proposed OFL family first in its font stack, then a system face. On a machine without the OFL font installed, the system face renders: New York or Georgia for Newsreader, Helvetica Neue for Inter, Avenir Next for Bricolage Grotesque, Menlo for IBM Plex Mono, Gill Sans for Source Sans 3, and Verdana for DejaVu Sans. **The stand-ins are close in feel and wrong in detail.** The Doorway wordmark is the exception: it is drawn geometry, not type, so it renders exactly. **No icon uses any font.** Converting text to outlines would have meant downloading the font files, which I did not do (no downloads without the CEO's permission, and none was needed for concept work).

---

## 2. Direction 1: Almanac

**Files:** `concepts/almanac-home.svg`, `concepts/almanac-wordmark.svg`, `concepts/almanac-icons-sheet.svg`, and the three 1024 px icons `almanac-icon-dogear.svg`, `almanac-icon-masthead.svg`, `almanac-icon-leaf.svg`.

**The idea.** Haunts is a private record of places, kept the way people used to keep a good notebook: dated, a little annotated, returned to. Almanac dresses it as that notebook with a newspaper's manners. It uses warm paper rather than white, an editorial serif for the things that are yours (venue names, the headline), a clean sans for everything functional, ink blue for action, and a single vermilion rule as its signature. **The headline slot is set like a masthead**: a double rule, a small-capitals kicker, one well-set sentence. That is the register `ux-home-headlines.md` §4.4 already chose, and it holds MEM-1 without effort, because a calm register has no volume to turn up [J].

**What it feels like to use** [J]. Quiet, literate, slow in a good way. Lists are ruled rather than carded, so the timeline reads like a page and not like a feed. Nothing bounces. It should feel like the opposite of a social app: the user is reading their own record, and nobody is performing for anyone.

**Palette** (measured; full table at §6):

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` (paper / ink) | `#F6F2EA` | `#16181B` | text on it **14.51 / 14.57** |
| `surface` | `#FFFDF8` | `#202328` | secondary text on it **6.76 / 6.29** |
| `text` | `#1C2127` | `#EDE8DE` | |
| `text2` | `#545B64` | `#A9A398` | |
| `primary` (ink blue) | `#1F4E79` | `#8DB8E8` | label on button **8.66 / 8.50** |
| `kicker`, `star` (vermilion ink) | `#A63A24` | `#E8957C` | **6.35 / 6.77** |
| `accent` (the rule, the mark) | `#B3412A` | `#E58A6F` | decorative and logotype only |
| `unconfirmed` (ochre) | `#8A5300` | `#E0B25A` | **6.23 / 8.02** |
| `outline` | `#8A8375` | `#7B766D` | lowest UI pair **3.37 / 3.49** (needs 3.0) |

**Type.** **Newsreader** for venue names, headlines and the wordmark. It was designed for reading news on screens [K, medium confidence], which is the headline slot's job. **Inter** for interface text, numbers and times. Both are **OFL 1.1**, with no Reserved Font Name declared [E, their OFL files: [Newsreader](https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/OFL.txt), [Inter](https://raw.githubusercontent.com/google/fonts/main/ofl/inter/OFL.txt)]. Newsreader has an optical-size axis, so a large headline and a small venue name each get the right cut [K, medium confidence].

**Iconography and shape.** Line icons at a 1.8 px stroke with rounded joins. Corners are small (6 px), rules are hairline, and there are no cards on the timeline. **The Places tab is an awning over a doorway, not a pin**, in every direction.

**Motion** [J]. Cross-fades of 150–200 ms and nothing that travels. A confirmed visit settles into the timeline with a fade, not a fly-in. Under Reduce Motion there are no position changes at all, only instant state changes (A11Y-9). **Nothing celebrates a confirmation**: there is no tick burst, because confirming is housekeeping, not an achievement (MEM-1).

**Wordmark.** "Haunts" in Newsreader semibold, underlined by the double vermilion rule: a thick rule over a thin one, as in newspaper typography. At credit size in the recap footer (LOOK-5), the word stands almost alone and the rule becomes a hairline.

**App-icon concepts** (`almanac-icons-sheet.svg`):

- **A. Dog-ear.** A slightly tilted page with its top corner folded down in vermilion. People dog-ear the pages they come back to, which is what a haunt is. *Risk:* it can read as a **document or file icon**. The tilt and the coloured fold push it away from that, and only partly succeed [J].
- **B. Masthead h.** A slab-serif lowercase h over the double rule. It is the strongest at 29 px of all twelve concepts [J, from the sheet]. *Risk:* it is a letter, so it is weaker if the name changes under PLAT-6, and Apple tolerates a mnemonic letter but prefers simplicity over text (`icon-brief.md` §2).
- **C. Pressed leaf.** A leaf pressed in the gutter of an open book: a memory kept. The warmest of the three. *Risk:* it reads as a **nature, gardening or eco app**, and leaves are a crowded icon category [J].
- **Considered and dropped: a bookmark ribbon.** The obvious notebook mark, but I believe **Day One**, the leading journalling app, uses a bookmark-like mark [K, medium confidence, not retrieved]. Too close.

**Headlines in Almanac.** Line: the masthead, as described. Card: up to three facts under one masthead, separated by hairlines. Ticker (if the user chooses it): one ruled strip with the kicker at the left, slow, with the pause control at the right. See `themes.md` §5.

**What it risks.**
- **"Too close to a news app or a generic notebook"** [J]. Serif-on-paper is a well-used look. Its distinctiveness rests on execution: the vermilion rule, the masthead, the ruled timeline. Executed badly, it is beige.
- **"Too quiet."** The CEO asked for *"distinctive"*. Almanac is distinctive in register more than in colour. If the CEO looks at it and thinks "tasteful but forgettable", that is a legitimate reading, and Doorway is the answer to it.
- **The vermilion kicker near HEAD-8's "no red".** At `#A63A24` it is closer to brick than to alert red and is never used for a warning, but the CEO should judge it by eye [J].

---

## 3. Direction 2: Doorway

**Files:** `concepts/doorway-home.svg`, `concepts/doorway-wordmark.svg`, `concepts/doorway-icons-sheet.svg`, and `doorway-icon-fanlight.svg`, `doorway-icon-arcade.svg`, `doorway-icon-ajar.svg`.

**The idea.** A haunt is a place you walk into, again and again. Doorway makes the door its motif: the arch, the threshold, the fanlight over a terraced front door. It is bold and warm, with deep plum, apricot and a teal accent. Its wordmark is **constructed, not typeset**: a lowercase "haunts" drawn from arches and stems, so the h, n and u *are* doorways. It is the most distinctive of the four and the most "brand" [J].

**What it feels like to use** [J]. Friendly, confident and modern, the closest to what people expect from a well-made consumer app in 2026. Rounded cards (22 px corners), pill-shaped choices, and a headline in an **arch-topped card**, the one place the motif enters the interface itself.

**Palette:**

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` | `#FFF8F1` | `#1A1422` | text on it **15.67 / 15.79** |
| `surface` | `#FFFFFF` | `#251D30` | secondary text on it **7.36 / 7.70** |
| `text` | `#241B2F` | `#F6EFE8` | |
| `text2` | `#5C5266` | `#B9AFC4` | |
| `primary` (plum) | `#5B2A86` | `#C9A7F0` | label on button **9.90 / 8.40** |
| headline card (apricot), with `text` on it | `#F2A65A` | `#F5B77A` | **8.15 / 9.38** |
| `teal` (secondary link) | `#0F6E6A` | `#5CC8C0` | **6.07 / 8.08** |
| `star` | `#B45309` | `#F5B77A` | **5.02 / 9.20** |
| `unconfirmed` | `#9A4D00` | `#F5B77A` | **6.11 / 9.20** |
| `outline` | `#8C7F99` | `#7E7190` | lowest UI pair **3.56 / 3.59** |

**Type.** **Bricolage Grotesque** for display: a characterful grotesque with optical sizes, which gives the headline card personality without a novelty face [K, medium confidence]. **Instrument Sans** for the interface. Both are **OFL 1.1** with no Reserved Font Name [E, [Bricolage Grotesque OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/bricolagegrotesque/OFL.txt), [Instrument Sans OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/OFL.txt)]. The wordmark uses no font.

**Iconography and shape.** Rounded line icons at a 2 px stroke; arches as the only ornament; large radii; generous spacing.

**Motion** [J]. A short, damped settle on sheets and cards, never a bounce. Under Reduce Motion, settles become cross-fades. **No door "opening" animation on launch**: a door swinging open every time the app starts is a small ceremony that rewards opening the app, the very thing HEAD-3's once-a-day rule exists to avoid.

**Wordmark.** The constructed lowercase "haunts" (`doorway-wordmark.svg`), with round terminals; the n and h are the arch. It is the only one of the four wordmarks with no font licence underneath it, because it is drawing [I, from how it is built]. The ownership question for a tool-drawn mark still applies (`icon-brief.md` §6).

**App-icon concepts** (`doorway-icons-sheet.svg`):

- **A. Fanlight door.** A Georgian front door under a fanlight, set in an apricot frame on plum. It is recognisably British, recognisably a *place*, and unlike any app icon I can picture [J].
- **B. Arcade.** Three equal arched openings cut into one wall: a covered row of shopfronts. *Risk:* a colonnade is close to the generic **bank or museum** icon [J].
- **C. Door ajar.** An arched door swung partly open, with light behind it. *Risk:* a door with a gap is the standard **"exit" or "log out"** symbol in many interfaces [K, high confidence].
- **A correction to my own draft, recorded because it is the most important finding in this section.** My first drawings of A and B were plain arches: one on a plinth, three of different heights. **Rendered, they read as headstones, and B also as a bar chart.** For a product the CEO renamed because *"Haunt seems a bit dark"* (D9), a headstone is the one association that cannot be risked. Redrawn, A has a fanlight and a squared door leaf, and B has equal openings in a continuous wall. **Any final Doorway artwork must be tested for this reading on people who have not been told what it is meant to be** (the misreading test, `icon-brief.md` §4).

**Headlines in Doorway.** Line: the apricot arch-topped card. Card: the same, with up to three facts divided by hairlines. Ticker: a plain apricot strip with the pause control at the right; the arch top is dropped, because a moving strip with a curved top has nowhere tidy for text to go.

**What it risks.**
- **Headstones**, above. The direction leans on a shape with a funerary reading, in a product whose name already has a ghostly one. I think it can be handled, but the risk never quite goes away [J].
- **Arches can read as religious buildings** [J]. Mild for a round-topped door, stronger for a pointed arch, so pointed arches are out.
- **The colour pair can date.** Purple and apricot feel current in 2026 [J], and current is the opposite of lasting. A journal people keep for years should not look like one year.
- **Arches are common.** I did not search trademarks (that is the CGO's PLAT-6 check). A single arch is **never** to be drawn in yellow, doubled, or on red [J], because of one very famous pair of arches.

---

## 4. Direction 3: Ledger

**Files:** `concepts/ledger-home.svg`, `concepts/ledger-wordmark.svg`, `concepts/ledger-icons-sheet.svg`, and `ledger-icon-card.svg`, `ledger-icon-entries.svg`, `ledger-icon-bracket.svg`.

**The idea.** The honest tool. Haunts' one differentiator that survived discovery is architectural: no outbound calls, a journal that never leaves the phone (`proposals/haunt/proposal.md`, *"literally no outbound calls at all"*). Ledger makes the product look like it means that: near-monochrome, precise, with a monospace for times and facts, and one orange signal colour for the mark, the headline rule and the timeline's margin line. It is a record, kept exactly.

**What it feels like to use** [J]. Calm, fast and serious, like a well-made command-line tool that happens to be pleasant. Times sit in a left margin, as in a logbook. Nothing is decorated. It will appeal strongly to the privacy-minded early adopter this product first reaches, and less to everyone else.

**Palette:**

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` | `#FAFAF8` | `#0F0F10` | text on it **18.07 / 17.09** |
| `surface` | `#FFFFFF` | `#1A1A1C` | secondary text on it **7.46 / 6.87** |
| `text`, `primary`, `star` | `#111111` | `#F2F2F0` | label on button **18.88 / 16.85** |
| `text2` | `#555555` | `#A3A3A0` | |
| `kicker`, `unconfirmed` (orange text) | `#B93D0B` | `#FB923C` | **5.62 / 7.68** |
| `accent`, `focus` (signal orange) | `#C2410C` | `#FB923C` | focus on page **4.96 / 8.46** |
| `outline` | `#767676` | `#76767A` | lowest UI pair **4.35 / 3.84** |

**Type.** **IBM Plex Sans** for the interface and **IBM Plex Mono** for times, durations and the wordmark. Both are **OFL 1.1**, and **both reserve the name "Plex"** [E, [Plex Sans OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexsans/OFL.txt), [Plex Mono OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/OFL.txt)]. The consequence, from the OFL FAQ: *"when authors have reserved names via the RFN mechanism, you need to change the internal names of the font … even if it is just a small change"* [E, OFL FAQ 3.1]. If the build subsets Plex to save space, it may have to rename it. That is a small engineering chore, not a blocker, and a **flag for the CGO and CTO** (§1.3).

**Iconography and shape.** Square line icons, 1.5 px stroke, 2 px corners; state shown by filled or hollow squares plus words; a vertical margin rule on the timeline.

**Motion** [J]. Almost none. Instant state changes with a 100 ms fade at most. Reduce Motion changes nearly nothing because there is nearly nothing to reduce, which is itself an accessibility virtue.

**Wordmark.** Lowercase "haunts" in Plex Mono, preceded by a thick orange margin rule, as if it were the first entry in a log.

**App-icon concepts** (`ledger-icons-sheet.svg`):

- **A. Index card.** A white card with a tab. *Risk:* it reads as a **folder**, the Files app's territory [J, from the sheet]. Weak.
- **B. Entries.** Three bars beside an orange margin rule. *Risk:* it reads as a **list or menu icon** (the "hamburger" family), a to-do app or a notes app [J]. Weak.
- **C. Bracketed h.** A monoline h in square brackets, white on orange. The strongest of the three and legible at 29 px. *Risk:* brackets read as **code**, so it looks like a developer tool; and it is a letter (as Almanac B).

**Headlines in Ledger.** Line: a thin orange rule down the left, a monospace kicker (`> from your journal`) and one sentence in Plex Sans. Card: the same, stacked. Ticker: one line, monospace, with the pause control; it is the least natural fit for a ticker of the four [J].

**What it risks.**
- **The least distinctive direction** [J]. Monochrome-plus-one-colour is the default look of a great many productivity apps. The CEO's word was *"distinctive"*, and Ledger answers it only through restraint.
- **Cold.** A journal of memories set like a server log may feel like the wrong register for "three years of The Brass Kettle" [J].
- **Reads as a developer tool**, which narrows the audience in the same way D9 worried a name could narrow the product.

---

## 5. Direction 4: Contour

**Files:** `concepts/contour-home.svg`, `concepts/contour-wordmark.svg`, `concepts/contour-icons-sheet.svg`, and `contour-icon-lines.svg`, `contour-icon-map.svg`, `contour-icon-horizon.svg`.

**The idea.** A personal atlas. It borrows from Ordnance Survey cartography, which Haunts already ships as its offline basemap (D22, *"OS Open Zoomstack"*): muted greens, contour lines, place names in italic serif (a long-standing mapmakers' convention for names [K, medium confidence]), a letterspaced capital wordmark set on a curve like a map label. It is the most atmospheric of the four, and the most British.

**What it feels like to use** [J]. Outdoorsy and unhurried, like a walking map spread on a table. Beautiful in the heatmap (LOOK-2); less at home on a list of café visits.

**Palette:**

| Token | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| `bg` | `#F3F5F0` | `#121815` | text on it **13.58 / 15.12** |
| `surface` | `#FFFFFF` | `#1B2420` | secondary text on it **6.84 / 7.00** |
| `text` | `#1D2A24` | `#E6EDE8` | |
| `text2` | `#4F5E57` | `#9FB0A7` | |
| `primary` (OS green) | `#2E6B4A` | `#7CC39A` | label on button **6.33 / 8.26** |
| `water` (links, focus) | `#2C6E8F` | `#7FC0DE` | **5.62 / 7.95** as text |
| `kicker`, `star`, `unconfirmed` (contour brown) | `#86592F` | `#D4A373` | **6.03 / 7.04** |
| `outline` | `#7D8A83` | `#6F7F77` | lowest UI pair **3.28 / 3.77** |

**Type.** **Source Serif 4** (italic, for place names and headlines) and **Source Sans 3** for the interface, both **OFL 1.1**. **Source Sans 3 reserves the name "Source"**, as an Adobe trademark; Source Serif 4's file as retrieved declares none [E, [Source Sans 3 OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/sourcesans3/OFL.txt), [Source Serif 4 OFL](https://raw.githubusercontent.com/google/fonts/main/ofl/sourceserif4/OFL.txt)]. The same subsetting flag as Ledger applies.

**Iconography and shape.** Line icons with slightly organic curves; 14 px corners; **contour texture confined to empty areas and never behind text** (a rule the mockup follows: the texture sits in the header's empty band and down the headline panel's left edge).

**Motion** [J]. Gentle cross-fades. **No camera flights on the heatmap under Reduce Motion** (A11Y-9 already requires this); a map-flavoured brand makes it tempting to animate maps everywhere, and the direction's motion rule would be "maps move only when the user moves them".

**Wordmark.** "HAUNTS", letterspaced capitals set along a gentle curve, with two contour lines beneath: a map label.

**App-icon concepts** (`contour-icons-sheet.svg`):

- **A. Landform lines.** Irregular contour lines crossing a green tile, deliberately open rather than closed. *Risk:* it reads as **water, waves or a weather app** [J, from the sheet]; closed, concentric contours would have read as a **target or radar**, which D9's reasoning excludes.
- **B. Folded map.** A three-panel folded map with a river, and **no pin**. *Risk:* it is the visual language of **navigation apps** [K, high confidence], so it tells people "maps", and a location app that looks like maps invites exactly the "it tracks me" assumption the product must earn its way past.
- **C. Horizon.** Layered hills with a low sun. *Risk:* it reads as a **travel, weather or photos** app, and a low sun can read as evening, which drifts towards nightlife [J].

**Headlines in Contour.** Line: a white panel with a contour-line edge, an italic serif sentence and a letterspaced kicker. Card: the panel with up to three facts. Ticker: a slim panel, same styling, with the pause control.

**What it risks, and why I recommend against it as the brand.**
- **It pulls the brand towards maps, and maps towards tracking** [J]. D9's whole argument was that an association can undo a product's claim: *"for a location-history product, being invisibly followed is precisely the association the product exists to refuse."* A brand that says "map" first says "location app" first. Haunts is a journal about places, and the map is decoration over a list (A11Y-1: *"The map is decoration over a complete list product"*).
- **Too close to outdoor-activity and hiking apps**, a category whose products *do* record your routes [J].
- **None of its three icons is strong** at 60 px [J, from the sheet].
- **It would make a good optional theme later** (`themes.md` §4.3), which is where its real strength, the heatmap, lives.

---

## 6. Contrast: how it was measured, and the result

**Result: 176 pairs measured across the four directions and the retro theme, in light and dark. Every pair passes its threshold.** The full tables are in the appendix at the end of this document, generated by `python3 tools/contrast.py` and pasted unedited.

**Method.** WCAG's relative luminance, *"L = 0.2126 * R + 0.7152 * G + 0.0722 * B"*, each channel linearised with the **0.04045** threshold (W3C's errata to the 0.03928 in the spec text, noting that *"for 8 bit color values the difference is not significant"*), and the ratio (L1 + 0.05) / (L2 + 0.05) [E, W3C, *Relative luminance*]. Thresholds: 4.5:1 for text, 3:1 for UI components and graphical objects [E, W3C Understanding 1.4.3, 1.4.11]. **Every text pair is held to 4.5:1 even where it would count as large text**, because Dynamic Type makes "large" a property of the user's settings, not of the design [J].

**What the measurement does not cover, stated so no one reads "all pass" as more than it is:**

1. **Only listed pairs.** A new token combination introduced in build is unmeasured until it is added to `palettes.py`. **Proposed rule:** CI runs `contrast.py --check`, which exits non-zero on any failure, and no colour is used in the app that is not a token (`themes.md` §9, THEME-2).
2. **Solid colours only.** Text over a gradient is measured at both ends of the gradient (the retro theme does this); **text over texture or imagery is not measurable, so it is not allowed** (A11Y-3's principle for maps, extended to texture).
3. **Rendered colour.** iOS Liquid Glass materials are translucent, and a translucent tab bar over content changes the colours behind text [I, from Apple's description of *"translucency"*, [E, Apple HIG App icons]; that page is about icons, and I have not retrieved Apple's guidance for interface materials]. **Any translucent surface needs an on-device measurement.**
4. **Increase Contrast.** A11Y-10 tests with Increase Contrast on. Each theme should define a higher-contrast variant of `text2`, `outline` and `divider` for it; I have not specified those values yet (`themes.md` §6.2).
5. **The logotype is exempt and I have not relied on the exemption.** SC 1.4.3: *"Text that is part of a logo or brand name has no contrast requirement"* [E]. All four wordmarks nevertheless meet 4.5:1 in the colours drawn.

---

## 7. Recommendation, with reasons

**Almanac as the brand and the modern default** [J]. Five reasons, in order of weight:

1. **It is the product's own metaphor.** A private record of places, kept like a notebook and headlined like a paper. Doorway's metaphor (a door) is about arriving; Almanac's is about remembering, which is what the product does after the arrival.
2. **It makes MEM-1 and HEAD-8 easy to hold.** A masthead register has no volume to turn up. A bold, playful brand is under constant pressure to celebrate things, and every celebration is a MEM-1 review.
3. **It pairs with the retro theme.** Both are about news: Almanac is the broadsheet and Homepage is the web portal. The headlines are the thread between them, which is what the CEO asked the retro theme to do (*"to go with the headlines"*, D38).
4. **It does not say "map" or "tracking"**, and it does not narrow the product to a night out.
5. **It is cheap.** Two font families, no custom-drawn type, no illustration system.

**Which Almanac icon:** **B, Masthead h**, for legibility at small sizes, **if** the name survives PLAT-6; **C, Pressed leaf**, if the CEO wants no letter in the mark. A is the weakest [J].

**The strongest alternative is Doorway**, and I would not argue hard against it. It is more distinctive and more modern, and the fanlight icon is the best single icon in this document [J]. I rank it second because its central shape carries a funerary reading in a product named Haunts, which is a risk that has to be managed for ever rather than solved once.

**A hybrid is possible and I would not recommend it yet.** Almanac's type and palette with Doorway's fanlight icon would work visually [J], but a brand whose icon and interface say different things is a brand that was decided by committee. Choose one first; borrow later if needed.

**Cost, as [J] for the CTO and CFO to replace.** Adopting any one direction as the default look costs roughly the same, because it replaces a look the build would need anyway: **about 3–5 days** of design-system set-up (tokens, two bundled fonts, icon set, the headline presentations). Doorway adds **1–2 days** for its arch-topped card and constructed wordmark. **None of this is in the CTO's 2,090-hour estimate.** Final artwork is separate and is the CEO's spending decision (`icon-brief.md` §6).

---

## 8. Negative findings, and what would overturn each

The charter requires every negative finding to say what would overturn it and where I looked.

| Finding | What would overturn it | Where I looked |
|---|---|---|
| **Contour is not recommended as the brand** | A preference test in which people shown the Contour icon and home screen do **not** describe it as a map, navigation or tracking app. Five to eight people would be enough to see whether the reading is common | My own rendered sheets and D9's reasoning. No people |
| **Ledger is the least distinctive** | The same kind of test, with people able to pick Ledger's icon out of a grid of productivity-app icons | My own judgment of the rendered sheet. No people, no icon survey |
| **Doorway carries a headstone risk** | People who have not been told the concept describing the redrawn icons as doors, not graves | My first-draft render, which I saw as headstones myself |
| **Almanac icon A reads as a file icon** | People describing it as a page or a book rather than a document | The rendered sheet |
| **Proprietary fonts (Verdana, Georgia, Helvetica and others) are excluded** | A licence retrieved from the foundry that permits bundling in a paid app | I did not retrieve these licences; the exclusion is the cautious default, tagged [K] |
| **The Day One bookmark concern** | Day One's current icon, retrieved, not resembling a bookmark | Not retrieved; [K, medium confidence] |

**The general caveat, once:** every judgment in this document about how an image *reads* is one person's reading. It is the kind of claim a small, cheap test settles and argument does not. `requirements.md` §22 item 1 already names the absence of any usability testing as *"the highest-value missing fact in the pipeline"*. **A 20-minute icon-and-screen preference test with five to eight people would settle more than this document can.** Recruiting and any incentives would be spending, so it is the CEO's to authorise.

---

## 9. Evidence register (all retrieved 2026-09-26 by this seat)

| # | Claim | Source |
|---|---|---|
| E1 | OFL permits bundling in commercial software including *"mobile device applications"*; notice and licence text must ship; the font may not be sold alone; RFN renaming on modification | [OFL FAQ](https://openfontlicense.org/ofl-faq/), entries 1.4, 1.5–1.6, 1.20, 3.1 |
| E2 | Newsreader, Inter, Bricolage Grotesque, Instrument Sans, Gelasio, Silkscreen, Source Serif 4: OFL 1.1, no RFN declared | Their `OFL.txt` files in `google/fonts`: [Newsreader](https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/OFL.txt), [Inter](https://raw.githubusercontent.com/google/fonts/main/ofl/inter/OFL.txt), [Bricolage](https://raw.githubusercontent.com/google/fonts/main/ofl/bricolagegrotesque/OFL.txt), [Instrument Sans](https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/OFL.txt), [Gelasio](https://raw.githubusercontent.com/google/fonts/main/ofl/gelasio/OFL.txt), [Silkscreen](https://raw.githubusercontent.com/google/fonts/main/ofl/silkscreen/OFL.txt), [Source Serif 4](https://raw.githubusercontent.com/google/fonts/main/ofl/sourceserif4/OFL.txt). **As summarised by the retrieval tool; I did not read each licence line by line** |
| E3 | IBM Plex Sans and Mono: OFL 1.1 with RFN "Plex"; Source Sans 3: OFL 1.1 with RFN "Source" | [Plex Sans](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexsans/OFL.txt), [Plex Mono](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/OFL.txt), [Source Sans 3](https://raw.githubusercontent.com/google/fonts/main/ofl/sourcesans3/OFL.txt) |
| E4 | Gelasio is *"metrics compatible with Georgia"* | [SorkinType/Gelasio README](https://github.com/SorkinType/Gelasio) (single source, the designer's own) |
| E5 | Silkscreen: *"Classic web design pixel font from Jason Kottke, 2001"* | [googlefonts/silkscreen](https://github.com/googlefonts/silkscreen) (single source) |
| E6 | DejaVu / Bitstream Vera licence: may be *"sold as part of a larger software package"*; not by itself; renaming rules | [DejaVu LICENSE](https://raw.githubusercontent.com/dejavu-fonts/dejavu-fonts/master/LICENSE) |
| E7 | SC 1.4.3 text (4.5:1, 3:1 large, logotype exemption) | [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |
| E8 | SC 1.4.11 text (3:1 for UI components and graphical objects; inactive components exempt) | [W3C Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) |
| E9 | Relative-luminance formula and the 0.04045 errata | [W3C WAI wiki, Relative luminance](https://www.w3.org/WAI/GL/wiki/Relative_luminance) |
| E10 | Apple app-icon guidance (layers, Liquid Glass, appearances, text, simplicity) | [Apple HIG, App icons (JSON of the page)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json); the [HTML page](https://developer.apple.com/design/human-interface-guidelines/app-icons) does not render for the retrieval tool. Used in `icon-brief.md` |

**Not retrieved, and tagged [K] where used:** the licences of Apple's and Microsoft's system fonts; Day One's icon; the design intent of Newsreader and Bricolage Grotesque; the cartographic italic convention; common "exit" and "bank" icon conventions.

---

## Appendix: measured contrast, every pair (output of `tools/contrast.py`, unedited)


#### Almanac (`almanac`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#1C2127` | `#F6F2EA` | **14.51:1** | 4.5:1 | pass |
| light | Body text on row/card | `#1C2127` | `#FFFDF8` | **15.94:1** | 4.5:1 | pass |
| light | Secondary text on page | `#545B64` | `#F6F2EA` | **6.15:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#545B64` | `#FFFDF8` | **6.76:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#1F4E79` | `#F6F2EA` | **7.76:1** | 4.5:1 | pass |
| light | Link on row/card | `#1F4E79` | `#FFFDF8` | **8.52:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#1F4E79` | **8.66:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#A63A24` | `#FFFDF8` | **6.35:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#A63A24` | `#F6F2EA` | **5.78:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#8A5300` | `#FFFDF8` | **6.23:1** | 4.5:1 | pass |
| light | Control border on row/card | `#8A8375` | `#FFFDF8` | **3.70:1** | 3.0:1 | pass |
| light | Control border on page | `#8A8375` | `#F6F2EA` | **3.37:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#1F4E79` | `#FFFDF8` | **8.52:1** | 3.0:1 | pass |
| light | Focus ring on page | `#1F4E79` | `#F6F2EA` | **7.76:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#A63A24` | `#FFFDF8` | **6.35:1** | 3.0:1 | pass |
| dark | Body text on page | `#EDE8DE` | `#16181B` | **14.57:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#EDE8DE` | `#202328` | **12.91:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#A9A398` | `#16181B` | **7.10:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#A9A398` | `#202328` | **6.29:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#8DB8E8` | `#16181B` | **8.60:1** | 4.5:1 | pass |
| dark | Link on row/card | `#8DB8E8` | `#202328` | **7.62:1** | 4.5:1 | pass |
| dark | Label on primary button | `#0E1A26` | `#8DB8E8` | **8.50:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#E8957C` | `#202328` | **6.77:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#E8957C` | `#16181B` | **7.64:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#E0B25A` | `#202328` | **8.02:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#7B766D` | `#202328` | **3.49:1** | 3.0:1 | pass |
| dark | Control border on page | `#7B766D` | `#16181B` | **3.94:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#8DB8E8` | `#202328` | **7.62:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#8DB8E8` | `#16181B` | **8.60:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#E8957C` | `#202328` | **6.77:1** | 3.0:1 | pass |

#### Doorway (`doorway`)

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
| light | Text on apricot chip / headline card | `#241B2F` | `#F2A65A` | **8.15:1** | 4.5:1 | pass |
| light | Teal secondary link on card | `#0F6E6A` | `#FFFFFF` | **6.07:1** | 4.5:1 | pass |
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
| dark | Text on apricot chip / headline card | `#241B2F` | `#F5B77A` | **9.38:1** | 4.5:1 | pass |
| dark | Teal secondary link on card | `#5CC8C0` | `#251D30` | **8.08:1** | 4.5:1 | pass |

#### Ledger (`ledger`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#111111` | `#FAFAF8` | **18.07:1** | 4.5:1 | pass |
| light | Body text on row/card | `#111111` | `#FFFFFF` | **18.88:1** | 4.5:1 | pass |
| light | Secondary text on page | `#555555` | `#FAFAF8` | **7.13:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#555555` | `#FFFFFF` | **7.46:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#111111` | `#FAFAF8` | **18.07:1** | 4.5:1 | pass |
| light | Link on row/card | `#111111` | `#FFFFFF` | **18.88:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#111111` | **18.88:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#B93D0B` | `#FFFFFF` | **5.62:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#B93D0B` | `#FAFAF8` | **5.38:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#B93D0B` | `#FFFFFF` | **5.62:1** | 4.5:1 | pass |
| light | Control border on row/card | `#767676` | `#FFFFFF` | **4.54:1** | 3.0:1 | pass |
| light | Control border on page | `#767676` | `#FAFAF8` | **4.35:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#C2410C` | `#FFFFFF` | **5.18:1** | 3.0:1 | pass |
| light | Focus ring on page | `#C2410C` | `#FAFAF8` | **4.96:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#111111` | `#FFFFFF` | **18.88:1** | 3.0:1 | pass |
| dark | Body text on page | `#F2F2F0` | `#0F0F10` | **17.09:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#A3A3A0` | `#0F0F10` | **7.58:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#A3A3A0` | `#1A1A1C` | **6.87:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#F2F2F0` | `#0F0F10` | **17.09:1** | 4.5:1 | pass |
| dark | Link on row/card | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 4.5:1 | pass |
| dark | Label on primary button | `#111111` | `#F2F2F0` | **16.85:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#FB923C` | `#1A1A1C` | **7.68:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#FB923C` | `#0F0F10` | **8.46:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#FB923C` | `#1A1A1C` | **7.68:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#76767A` | `#1A1A1C` | **3.84:1** | 3.0:1 | pass |
| dark | Control border on page | `#76767A` | `#0F0F10` | **4.24:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#FB923C` | `#1A1A1C` | **7.68:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#FB923C` | `#0F0F10` | **8.46:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#F2F2F0` | `#1A1A1C` | **15.50:1** | 3.0:1 | pass |

#### Contour (`contour`)

| Mode | Pair | Foreground | Background | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| light | Body text on page | `#1D2A24` | `#F3F5F0` | **13.58:1** | 4.5:1 | pass |
| light | Body text on row/card | `#1D2A24` | `#FFFFFF` | **14.91:1** | 4.5:1 | pass |
| light | Secondary text on page | `#4F5E57` | `#F3F5F0` | **6.23:1** | 4.5:1 | pass |
| light | Secondary text on row/card | `#4F5E57` | `#FFFFFF` | **6.84:1** | 4.5:1 | pass |
| light | Link / tab label on page | `#2E6B4A` | `#F3F5F0` | **5.77:1** | 4.5:1 | pass |
| light | Link on row/card | `#2E6B4A` | `#FFFFFF` | **6.33:1** | 4.5:1 | pass |
| light | Label on primary button | `#FFFFFF` | `#2E6B4A` | **6.33:1** | 4.5:1 | pass |
| light | Headline kicker on headline surface | `#86592F` | `#FFFFFF` | **6.03:1** | 4.5:1 | pass |
| light | Headline kicker on page | `#86592F` | `#F3F5F0` | **5.49:1** | 4.5:1 | pass |
| light | 'Unconfirmed' state label | `#86592F` | `#FFFFFF` | **6.03:1** | 4.5:1 | pass |
| light | Control border on row/card | `#7D8A83` | `#FFFFFF` | **3.60:1** | 3.0:1 | pass |
| light | Control border on page | `#7D8A83` | `#F3F5F0` | **3.28:1** | 3.0:1 | pass |
| light | Focus ring on row/card | `#2C6E8F` | `#FFFFFF` | **5.62:1** | 3.0:1 | pass |
| light | Focus ring on page | `#2C6E8F` | `#F3F5F0` | **5.12:1** | 3.0:1 | pass |
| light | Rating stars (also shown as text 4/5) | `#86592F` | `#FFFFFF` | **6.03:1** | 3.0:1 | pass |
| light | Water-blue link on card | `#2C6E8F` | `#FFFFFF` | **5.62:1** | 4.5:1 | pass |
| dark | Body text on page | `#E6EDE8` | `#121815` | **15.12:1** | 4.5:1 | pass |
| dark | Body text on row/card | `#E6EDE8` | `#1B2420` | **13.37:1** | 4.5:1 | pass |
| dark | Secondary text on page | `#9FB0A7` | `#121815` | **7.92:1** | 4.5:1 | pass |
| dark | Secondary text on row/card | `#9FB0A7` | `#1B2420` | **7.00:1** | 4.5:1 | pass |
| dark | Link / tab label on page | `#7CC39A` | `#121815` | **8.68:1** | 4.5:1 | pass |
| dark | Link on row/card | `#7CC39A` | `#1B2420` | **7.68:1** | 4.5:1 | pass |
| dark | Label on primary button | `#0E1F16` | `#7CC39A` | **8.26:1** | 4.5:1 | pass |
| dark | Headline kicker on headline surface | `#D4A373` | `#1B2420` | **7.04:1** | 4.5:1 | pass |
| dark | Headline kicker on page | `#D4A373` | `#121815` | **7.96:1** | 4.5:1 | pass |
| dark | 'Unconfirmed' state label | `#D4A373` | `#1B2420` | **7.04:1** | 4.5:1 | pass |
| dark | Control border on row/card | `#6F7F77` | `#1B2420` | **3.77:1** | 3.0:1 | pass |
| dark | Control border on page | `#6F7F77` | `#121815` | **4.26:1** | 3.0:1 | pass |
| dark | Focus ring on row/card | `#7FC0DE` | `#1B2420` | **7.95:1** | 3.0:1 | pass |
| dark | Focus ring on page | `#7FC0DE` | `#121815` | **8.99:1** | 3.0:1 | pass |
| dark | Rating stars (also shown as text 4/5) | `#D4A373` | `#1B2420` | **7.04:1** | 3.0:1 | pass |
| dark | Water-blue link on card | `#7FC0DE` | `#1B2420` | **7.95:1** | 4.5:1 | pass |

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

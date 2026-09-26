# Haunts themes: the system, the proposed set, and the retro theme

**Seat:** UX / Design Lead · **Date:** 2026-09-26 · **Slug:** `haunt` · **Commission:** **D38** (CEO, 2026-09-26): *"the app offers selectable styles, with a **modern default** and at least one alternative. The CEO's example is a **retro theme** in the spirit of an early-2000s website, to go with the headlines (D20)."*
**Companion files:** [`brand-directions.md`](brand-directions.md), [`icon-brief.md`](icon-brief.md), mockups [`concepts/themes-default-vs-retro-light.svg`](concepts/themes-default-vs-retro-light.svg) and [`concepts/themes-default-vs-retro-dark.svg`](concepts/themes-default-vs-retro-dark.svg), token source [`tools/palettes.py`](tools/palettes.py), measurement [`tools/contrast.py`](tools/contrast.py).
**Status:** prepares and flags; certifies nothing (Constitution 6.1). **Nothing here is adopted.** D38(4): *"Themes are new scope. Once a direction is signed off, they enter `requirements.md` through a §24 scope-change row (PM/BA), are sized by the CTO and are costed by the CFO."* The requirement rows in §9 are drafts for the PM/BA to lift, as `ux-home-headlines.md` §9 was.
**Template note:** no design template exists in `pipeline/templates/`; this note follows the commission's list of contents and says so.
**Evidence:** tagged under `pipeline/evidence-standard.md`; every [E] was retrieved on 2026-09-26 and is listed in §11. Contrast ratios are arithmetic from `tools/contrast.py`.

---

## 0. The answers, before the reasoning

1. **A theme is a skin, never a different app.** It may change colour, type, shape, iconography, texture, motion *style* and the *styling* of each headline appearance. It may never change layout, information architecture, copy, behaviour, accessibility or any privacy surface. §2.
2. **The set at launch: two themes.** The **modern default** (whichever brand direction the CEO chooses; shown as Almanac, my recommendation) and **Homepage**, the retro early-2000s theme. §4.
3. **Candidates for later, not launch:** Contour, as a cartographic theme that suits the heatmap, and a Plain theme in the platform's own look. **Each extra theme multiplies the testing of every screen**, so I recommend earning the second theme before adding a third. §4.3.
4. **Dark mode is not a theme.** It is a separate setting that applies to every theme: *Match phone* (default), *Light*, *Dark*. Every theme ships both. §6.
5. **The theme never chooses the headline appearance.** Line, Card, Ticker or Off stays the user's own setting (HEAD-2). A theme only decides how each one looks. **Choosing Homepage does not switch the ticker on.** §5, and a disagreement with the commission's wording, recorded once at §10.
6. **The retro theme keeps the period's look and none of its tricks.** Hit counters, visitor numbers, badges, "NEW!", blink, guestbooks and anything a user could beat or break are out. Bevelled buttons, title-bar gradients, underlined blue links, tabbed navigation, Verdana-and-Georgia proportions, a pixel face for labels and the portal-style news ticker are in. §8.
7. **Themes are never rewards, and I recommend they are never sold separately.** No theme is unlocked by use, and every theme stays available in every entitlement state. The second half is pricing, so it is the CEO's decision (§3.4).
8. **Cost** [J]: about **5–8 days** for the theme machinery, **4–6 days** for Homepage, and roughly **15–25% extra UI verification per theme, for ever**. None of this is in the 2,090-hour estimate. §7.

---

## 1. Why themes, and the one risk they carry

The CEO asked for themes because he wants Haunts to be *"a pleasure to use, not horrible to look at"*, and because taste varies (D24's general direction: *"I like this idea in general, allowing customisation by the user"*). A theme is the cheapest kind of customisation that genuinely changes how a product feels [J].

**The risk is that a theme becomes a second product.** Each theme is another surface to test at every text size, in light and dark, on both platforms, with VoiceOver and TalkBack, for every screen that ever ships. A theme that is allowed to move things, reword things or behave differently multiplies that cost and, worse, lets an accessibility or Article 4 failure hide in the theme nobody tests. **So the system below is built on one rule: themes change how things look, never what they are or where they are.**

---

## 2. What a theme may change, and what it may never change

| A theme **may** change | A theme **may never** change | Why the line is here |
|---|---|---|
| **Colour**: every token in `palettes.py` (`bg`, `surface`, `text`, `primary`, `kicker`, `outline`…) | **Layout and information architecture**: what is on each screen, its order, the tabs, where each control sits, the focus order | HEAD-16 fixes the focus order (*"ENT-9 status, headline, options, timeline"*). A user who switches theme, or asks a friend for help, must find everything in the same place |
| **Type**: families, weights, letter-spacing, case (for example small capitals or pixel capitals for the same string) | **Copy**: no theme adds, removes or rewords a string. Case is presentation; words are not. A theme may show or hide the *visible* label of a control that already has one (the retro "+ Add" is the add control's own label), but the accessible name never changes | QA's MEM-1 and HEAD-6 string searches run over one string table (`requirements.md` MEM-1(a)). A theme with its own copy is a string table QA has not searched |
| **Shape**: corner radii, rule weights, bevels, borders, card or ruled lists | **Behaviour**: what any control does, what is on by default, what is asked, when anything changes | DFLT-1 and every Article 4 criterion are behavioural. A skin cannot be allowed to carry behaviour |
| **Iconography**: the drawing of each interface icon, never its meaning; one icon per concept | **Accessibility**: contrast, target sizes (A11Y-5), Dynamic Type (A11Y-4), reduce-motion (A11Y-9, HEAD-10), screen-reader labels (A11Y-6, HEAD-16), no colour-only meaning (A11Y-2) | Constitution Article 4, WCAG 2.2 AA. D38(1): *"A retro theme is a look, not an exemption."* |
| **Texture**: rules, gradients, patterns, **only where no text sits on them** | **Privacy surfaces**: the app-switcher cover (HEAD-12, LOOK-2(e)), the Privacy screen (PRIV-2), the transmission sentence (PRIV-1), backup and export flows, the passphrase moment | These are claims the product makes. They must read identically however the app is dressed |
| **Motion style**: easing and duration of the *same* transitions, within the motion budget in §6.3 | **What moves**: no theme adds an animation the default lacks. Under Reduce Motion every theme is equally still | A11Y-9, HEAD-10 |
| **Headline presentation**: how Line, Card and Ticker each look | **Which** headline appearance is shown, and **what** it says (HEAD-2 to HEAD-18) | §5 |
| **The splash colour** (launch screen background) | **The app icon.** No theme changes it at launch (§3.3) | Alternate icons are extra store assets and platform work for little gain [J] |

**One test settles most cases** [J]: *if a screenshot of the app in theme A and in theme B were described aloud to a blind user, would the two descriptions be identical?* If not, the theme has changed something it may not.

---

## 3. How themes are built and offered

### 3.1 Tokens, not code paths

Every colour, font, radius, rule weight, texture and motion curve the interface uses is a **named token**. A theme is a set of values for those tokens, for light and dark. **No component contains a theme check** (no "if retro then…"). That single rule is what keeps the cost of a theme close to the cost of its values rather than the cost of its screens [J]. The token names are fixed in `brand-directions.md` §1.2 and `tools/palettes.py`.

**Two exceptions, declared rather than smuggled in.** The retro theme needs (a) bevelled edges and (b) title-bar gradients, which are not colours. They are expressed as **shape and texture tokens** (`edge_style: flat | bevel`, `title_fill: solid | gradient`) that every component reads. The default sets them to flat and solid.

### 3.2 Where the choice lives

- **Settings → Appearance**, with two controls: **Theme** (a list of theme names, each with a small still preview of the home screen) and **Light or dark** (*Match phone*, *Light*, *Dark*).
- **No prompt, banner, tip or "try the retro theme!" anywhere, ever.** Themes are found in Settings like any other preference. Promoting a theme is a small engagement mechanic with nothing in it for the user [J], and HEAD-7 already bars the headline slot from announcing features.
- **No "NEW" label on a theme** in the list, for the HEAD-8 reason.
- **The choice persists** across launches and updates, and is included in the export's settings block so it survives a restore (DATA-3's round-trip principle).

### 3.3 The app icon does not change with the theme

iOS and Android can both offer alternate app icons [K, high confidence, not retrieved]. **I recommend against it at launch:** each alternate icon is a full extra icon set (`icon-brief.md` §4), with its own light, dark, tinted and themed-monochrome variants, and it sits outside the app on the one surface other people see most [J]. A retro icon would be charming. It is a later, separately sized feature, not part of a theme.

### 3.4 Themes are never rewards, and never gated by entitlement

- **Never unlocked by use.** A theme "earned" after 50 visits, or after a year, is a reward for visit frequency: a streak with a paint job. MEM-1 forbids it: *"never rewards the frequency or volume of visits — anywhere in the product."*
- **Available in every entitlement state.** What the subscription sells is *"the capture engine and the maintained venue index"* (`requirements.md` §2). A theme is neither. Locking the retro theme behind payment, or removing it on lapse, would make the unpaid state look punished, which is the kind of thing ENT-9 and B8 exist to prevent (*"styles a working journal as disabled"*).
- **Whether themes could ever be sold separately is a pricing question, and pricing is the CEO's alone** (Constitution 5.4). **My recommendation is no**: a paid cosmetic in a product whose pitch is honest, all-in pricing reads as a nickel-and-dime [J]. Recorded as a recommendation, not a rule.

---

## 4. The proposed set

### 4.1 Theme 1: the modern default

**Whichever brand direction the CEO chooses becomes the default theme.** I recommend Almanac (`brand-directions.md` §7), and the mockups show it. If the CEO chooses Doorway or Ledger instead, nothing in this document changes except the name.

**Default for a new install:** the modern default, in *Match phone* mode. DFLT-1 does not apply, because neither value is more protective than the other, and the settings register should record that (§9, THEME-5).

### 4.2 Theme 2: Homepage, the retro early-2000s theme

Described in full in §8, with its guardrails. Named **Homepage** because an early-2000s website was somebody's homepage [J]. Alternative names if the CEO prefers: *Portal*, *Broadband*, *Web 1.0*. **I would avoid "Geocities"** (a proper name and a former Yahoo! product [K, high confidence]) and **"Dial-up"** (a joke about slowness, in an app that is fast).

**Why it earns its place** [J]: the CEO asked for it; it is the most joyful way to meet the *"a pleasure to use"* half of D38; and it is the natural costume for the headlines, which were first imagined *"like headlines/marquee at the top of the homescreen, bit like news channels"* (D20). The portal ticker is the one headline appearance that looks most at home in it.

### 4.3 Candidates for later, and why not at launch

| Candidate | What it is | Why it might earn a place | Why not at launch |
|---|---|---|---|
| **Contour** | The cartographic direction (`brand-directions.md` §5) as a theme, not the brand | Beautiful on the heatmap, which already uses the OS basemap (D22); its tracking risk matters far less as an opt-in skin than as the brand [J] | A third theme adds a third column to every verification pass |
| **Plain** | The platform's own look: system fonts (San Francisco, Roboto), system colours, no brand texture | Cheapest possible theme; suits people who want the app to look like their phone; bundles no fonts, because it uses the fonts the OS already provides [K, high confidence] | It is also the least distinctive, and the default must be good enough that nobody needs an escape from it |
| **Ledger** | The monochrome direction as a theme | For the privacy-minded user who wants a tool, not a journal | As above |

**Explicitly not a theme: "high contrast" or "accessible".** Every theme meets the baseline, and iOS Increase Contrast adjusts every theme's tokens (§6.2). A separate accessibility theme would imply the others are less accessible, which must never be true.

---

## 5. Headlines in each theme

**The rule.** The user's headline appearance (Line, Card, Ticker, Off) is chosen in the headline options and Settings (HEAD-2, HEAD-5), persists across relaunch and update, and **is untouched by a theme change**. A theme supplies the *look* of each appearance. **Switching to Homepage does not switch the ticker on**, and switching away from it does not switch the ticker off. Everything in HEAD-1 to HEAD-18 applies identically in every theme: one fact a day in a fixed order (HEAD-3), the template catalogue (HEAD-4), memories never volume (HEAD-6), no novelty treatment (HEAD-8), the pause control and one pass per open (HEAD-9), the automatic fallbacks (HEAD-10, HEAD-11), never in the app-switcher (HEAD-12), never announced (HEAD-16).

| Appearance | Modern default (Almanac) | Homepage (retro) |
|---|---|---|
| **Line** (default appearance) | A masthead: thick and thin rules, the kicker *"From your journal"* in vermilion small capitals, one sentence in Newsreader, the options control at the right | A pale-yellow portal module with a thin blue border: the same kicker in Silkscreen capitals, the sentence in DejaVu Sans, a bevelled options button |
| **Card** | Up to three facts under one masthead, separated by hairlines; one fact at accessibility text sizes | Up to three facts in one portal module, separated by dotted rules, with a gradient title strip carrying the kicker |
| **Ticker** | A single ruled strip: kicker at the left, the sentence scrolling slowly, pause and options controls at the right | **The portal news ticker:** a navy label block (the kicker in pixel capitals) and a pale-yellow strip, with bevelled options and pause buttons at the right. This is the look the CEO asked for |
| **Off** | Zero height | Zero height |
| **Ticker, with Reduce Motion, a screen reader or accessibility text sizes** | Renders as the Line, still | Renders as the retro Line, still (third phone in the mockup) |

**What the retro ticker borrows from the period, and what it refuses** [K for the period, high confidence; J for the choices]. It borrows the look of the headline module on early-2000s portal and news sites: a labelled box, a contrasting strip, text moving right to left. It **refuses the period's behaviour**: `<marquee>` ran for ever, could not be paused and often came with a blinking "NEW!". Ours makes one pass per open and stops (HEAD-9), always has a visible pause control that remembers being paused, and never blinks. The commission's own test settles it: nothing in the ticker can be beaten or broken.

**The mockups.** `concepts/themes-default-vs-retro-light.svg` and `…-dark.svg` show three phones on the same screen: (1) the modern default with the Line; (2) Homepage with the Ticker, which **the user** chose; (3) Homepage with Reduce Motion on, where the same Ticker setting renders as a still Line. The layout, copy and order are identical across all three. **The explanation for the fallback** (*"Your phone is set to reduce motion, so headlines stay still"*, `ux-home-headlines.md` §7.2) appears on the options screen as HEAD-10(c) requires, **not** on the home screen, so the mockup does not show it there.

---

## 6. Light, dark, higher contrast, and motion

### 6.1 Light and dark are a setting, not themes

- **Settings → Appearance → Light or dark: *Match phone* (default), *Light*, *Dark*.** It applies to whatever theme is chosen.
- **Every theme ships a light and a dark set of tokens**, and each is measured (`brand-directions.md` §6 and appendix: all pairs pass in both modes for the four directions and for Homepage).
- **Why separate** [J]: people choose dark for reasons of eyesight, battery or bedtime, and those reasons do not change with taste. Tying dark to a theme would force a user to choose between the look they like and the mode they need.
- **Homepage's dark set** is the period's own dark look: navy-black background, sky-blue links, gold headings, a dark-olive ticker with pale-yellow text. It exists because the rule is that every theme ships both modes, not because the period demanded it.

### 6.2 Increase Contrast, Bold Text, larger text

- **iOS Increase Contrast** (and Android's high-contrast text) is tested by A11Y-10 on every release. **Each theme defines a higher-contrast variant** of `text2`, `outline`, `divider` and any texture opacity, used when the setting is on. The values are not yet specified; **target: text2 at 7:1 and outlines at 4.5:1 in that mode** [J]. The CTO should confirm what React Native exposes on each platform.
- **Bold Text** (iOS) swaps weights in every theme, including the retro pixel face, which has no bold and so is replaced (§8.4).
- **Dynamic Type** at every size, in every theme, with no truncation of venue names (A11Y-4). Retro boxes and tabs grow with their text; nothing in the retro theme has a fixed height, whatever the period did.

### 6.3 The motion budget, the same for every theme

A theme may choose easing and duration **within** this budget, and may add nothing outside it [J]:

- Transitions of **100–250 ms**, cross-fades or short settles. No bounce, no overshoot beyond a few pixels, no parallax.
- **No motion on arrival**: no launch animation, no entry animation on the headline (HEAD-8), no confetti or celebration on confirming a visit (MEM-1).
- **The ticker is the only continuous motion in the app**, and it is governed by HEAD-9 to HEAD-11.
- **Under Reduce Motion** (iOS) or **Remove animations** (Android accessibility setting, HEAD-10(b)): every theme becomes equally still, with instant changes or plain cross-fades.

---

## 7. Cost, as this seat's [J], for the CTO to size and the CFO to cost

Themes are new scope (D38(4)); none of this is in the CTO's 2,090-hour estimate.

| Item | Estimate [J] | Notes |
|---|---|---|
| **Theme machinery**: tokenised styling read at runtime, the Appearance settings screen with previews, persistence and export round-trip, snapshot tests per theme | **5–8 engineer days** | A tokenised design system is good practice anyway; the marginal cost is runtime switching, the settings UI and the test matrix |
| **Homepage theme**: token values for light and dark, three bundled OFL families (Gelasio, DejaVu Sans, Silkscreen), bevel and gradient shape tokens, the retro styling of the four headline appearances, design coverage of every screen | **4–6 days** of design and build, plus **1–2 days** of first verification | Screens beyond the home screen are not designed yet; this assumes a small app |
| **Verification, recurring** | **About 15–25% more UI verification per extra theme**, on every release, for ever | A11Y-10's per-release checklist becomes theme × mode × platform. This is the cost that matters, and why I recommend two themes, not four |
| **Per new screen** | Each new screen is designed and checked in every theme and mode | The tokens keep this small if components never contain theme checks (§3.1) |
| **App size** | Roughly **0.5–1.5 MB** for three font families, subset [K, low confidence] | Small beside the 21.3 MB venue index; subsetting has the Reserved Font Name wrinkle for some families (`brand-directions.md` §1.3). For Homepage: Gelasio and Silkscreen declare no Reserved Font Name, and DejaVu's licence restricts only the words *"Bitstream"* and *"Vera"* in a modified font's name, which "DejaVu Sans" does not contain [E, their licence files; my reading, for the CGO to confirm] |
| **Font notices** | Minutes | OFL requires the copyright statement, licence notice and licence text to ship with the app [E, OFL FAQ 1.20]; a LIC row for the PM/BA |

**Could the retro theme be cut?** Yes, cleanly: it is a set of values, and the default works without it. If the CTO's sizing makes it expensive, a smaller version, the retro *headline* styling alone (the portal ticker and module inside the modern default), would deliver the part D38 tied it to at perhaps a third of the cost [J]. I do not recommend starting there, because a portal ticker inside a broadsheet looks like a mistake, but it is the honest fallback.

---

## 8. The retro theme: Homepage

### 8.1 The idea

The web of roughly 2001–2004, before the smartphone, as people remember it fondly: pale blue-grey pages, a navy gradient title bar, Verdana at small sizes, Georgia headings, underlined blue links, tabbed navigation, grey bevelled buttons, content in boxed modules with gradient title strips, dotted dividers, "»" bullets, a pixel font for tiny labels, and a news ticker in a pale-yellow strip [K, high confidence for the period's conventions; not retrieved, and no single site is copied]. It should feel like finding your old homepage, cleaned up and made legible, and holding your own news.

**What it is not:** a parody, and not a museum piece. Every period trick that manipulated attention or measured the visitor is gone (§8.3). What is left is the look, and the warmth people attach to it [J].

### 8.2 The look, specified

| Element | Light | Dark | Measured (light / dark) |
|---|---|---|---|
| Page `bg` | `#DCE4F0` | `#000022` | body text on it **13.59 / 16.75** |
| Content boxes `surface` | `#FFFFFF` | `#0B0B33` | secondary text **8.86 / 9.28** |
| Title-bar gradient | `#16336B` → `#2D5AA0` | `#1B1B55` → `#33337A` | white text at **both ends**; lowest pair passes 4.5:1 (appendix of `brand-directions.md`) |
| Box title strip gradient | `#FFFFFF` → `#D3DFF0` | `#2E2E78` → `#1B1B55` | heading text measured at both ends; all pass |
| Links (`primary`), always **underlined** | `#0033CC` | `#66CCFF` | label on button **8.95 / 11.38** |
| Selected tab / idle tab | `#F4B860` / `#E6ECF5` | `#FFCC66` / `#16164A` | all tab labels pass 4.5:1 |
| Ticker strip and its text | `#FFFFCC`, text `#1A1A1A` | `#1A1A00`, text `#FFFF99` | pass |
| Bevel button face and edge | `#ECE9D8`, edge `#716F64` | `#2B2B5E`, edge `#8A8AC0` | edge on content **5.05**; edge on own face **4.14 / 4.02** |
| `unconfirmed` label | `#A33A00` | `#FFB870` | **6.64 / 11.12** |
| `star` (rating glyphs) | `#B36B00` | `#FFCC66` | **4.18 / 12.69** |
| Lowest UI pair (control border on page) | `#5E7FA3` on `#DCE4F0` | | **3.25** (needs 3.0) |

**Type**, all bundle-safe:
- **Gelasio** for headings and the wordmark: OFL 1.1, and *"metrics compatible with Georgia"* [E, Gelasio OFL file and README].
- **DejaVu Sans** for body text: the Bitstream Vera licence, which allows the fonts to be *"sold as part of a larger software package"* but not *"by itself"* [E, DejaVu LICENSE]. Its wide, open proportions carry the Verdana feel [J]; **Verdana itself is not bundle-licensed** [K, high confidence, excluded on the cautious side].
- **Silkscreen** for short capital labels only: OFL 1.1, and the retrieved README calls it a *"Classic web design pixel font from Jason Kottke, 2001"* [E, single source]. It is period-authentic, not a pastiche.

**Shape:** square corners everywhere; 1.5 px bevel edges with a light top-left highlight; boxes with 1 px borders and a gradient title strip; tabs as bevelled rectangles; dotted rules between days. **The tabs stay at the bottom of the screen**, where the default puts them, because a theme may not move navigation (§2). Period sites put tabs at the top; that is the one period convention the layout rule overrides, and the mockup shows it.

**Iconography:** the same icon meanings as the default, drawn as small chunky glyphs with 1 px outlines. **Decorative glyphs** ("»", "::") are drawn, not typed into the string table, and are hidden from screen readers.

### 8.3 Guardrails: which period tropes are out, which are in

The test, from `ux-home-headlines.md` §4.1 and D38(2): **"If the user could 'beat' it or 'break' it, it is out."** Most of what follows fails that test. The rest fails on Article 4, on accessibility, or on the product's privacy claim, and each row names its ground.

**Out, however period-accurate:**

| Trope | Ground |
|---|---|
| **Hit counters, "You are visitor #n"**, in any form, including a count of app opens | **MEM-1**: a number that goes up every time you open the app is a volume count you can beat. Also **Article 4**, *"Collect the minimum data necessary"*: the app does not count opens and must not start |
| **Any counter in period dress**: "142 places!" in LED digits, odometers, "visits this year" | MEM-1 and HEAD-6. A plain count may appear only where a template already states it (T2's *"41 visits recorded"*), set as ordinary text |
| **Badges and award GIFs**: "Cool site of the day", "Best of the web", ribbons, rosettes, trophies | MEM-1: reward imagery. Also Article 1.3, honest by default: they are awards nobody gave |
| **"NEW!" blinkers, "HOT!" flames, sparkles, "BREAKING"** | **HEAD-8** in terms: *"No "NEW", "BREAKING", dot, badge, count, red or warning colour, flashing"*. Also Article 4, *"no false urgency"* |
| **`<blink>` and anything that blinks**, including a blinking text cursor in the ticker | HEAD-8 (*"flashing"*), and SC 2.2.2 (§8.4). The retro theme has **nothing that blinks at all**, so it never relies on the under-five-seconds allowance |
| **A marquee that runs for ever** | HEAD-9: one pass per open, visible pause, paused persists. The ticker is in; the endless marquee is out |
| **Guestbooks, "Sign my guestbook"** | A social layer. **D5 gates sharing** behind its own proposal and gate, and D11(c): *"nothing anywhere in the product prompts, suggests, nudges, badges or celebrates sharing"* |
| **"Email this page to a friend", "Bookmark us!", "Tell a friend"** | D11(c), as above |
| **Webrings, link exchanges, "Next site »", banner ads, affiliate buttons** | Links out of the app to other people's sites are not a feature of the product, and anything fetched would be a network call the product says it does not make (**PRIV-1**, **PRIV-8**) |
| **"Top 10", "Most popular", charts and rankings** | MEM-1 and HEAD-6: *"a rank"*. T2's plain "most-visited place" stays, in the default's words |
| **"Last updated 12 days ago", "days since"** | HEAD-6 names *"days since"*: an absence count reads as an obligation to return |
| **"Tip of the day", "Did you know?", daily polls, "Rate this site"** | HEAD-7 (no tips); **PRIV-6** (no review prompt); a daily-changing element is a variable reward for opening the app (HEAD-3's reasoning) |
| **Visited-link purple** | It records and displays what you have already looked at, which HEAD-8(c) forbids for headlines (*"Assert nothing records whether a headline has been seen"*), and it carries meaning by colour alone (A11Y-2). Links are one colour |
| **Splash pages, "Skip intro", pop-up windows** | A gate between the user and their journal; ONB-1's first-run rules; an interruption |
| **Auto-playing MIDI or any sound** | Nothing in Haunts plays sound unasked [J]; SC 1.4.2 Audio Control is Level A [K, high confidence, not retrieved] |
| **Cursor trails, animated GIFs, spinning globes, "under construction" diggers** | The motion budget (§6.3). The digger also misstates the product as unfinished, against Article 1.3 [J] |
| **"Best viewed in 800×600" or "…in Internet Explorer"** | It tells a user with large text that they are using the app wrong, which contradicts A11Y-4 [J] |
| **Clip-art beer mugs, cocktail GIFs, party imagery** | **MEM-1**: *"Haunts never encourages drinking"*. The period loved them; the product cannot |
| **Fake progress bars and "loading…" theatre** | False (Article 1.3), and progress framing is barred on the queue (CONF-1) and on headline eligibility (HEAD-15) |

**In:**

| Trope | Condition |
|---|---|
| Navy gradient title bar | Text measured at both ends of the gradient |
| Georgia-like headings (Gelasio), Verdana-like body (DejaVu Sans) | Sizes follow Dynamic Type, never fixed at the period's 11 px |
| Underlined blue links; venue names as links | Underline always present, so links are not distinguished by colour alone |
| Bevelled grey buttons | 44 × 44 pt minimum target (A11Y-5); edge contrast measured |
| Tabbed navigation, orange selected tab | Bottom of the screen, as in every theme; selected state shown by fill **and** weight, not colour alone |
| Boxed modules with gradient title strips, "» To confirm" | The "»" is decoration, hidden from assistive technology |
| Dotted dividers, "::" and "»" ornaments | Decorative only |
| Silkscreen pixel capitals for short labels (the kicker, tab labels at small sizes) | Only for strings a few words long; replaced at larger sizes (§8.4) |
| The portal news ticker | Only if the user has chosen Ticker; HEAD-9 to HEAD-11 in full |
| A pale-yellow "note" module for the headline Line and Card | Contrast measured |
| A dark variant in the period's navy-and-gold | Every pair measured |

### 8.4 How the retro theme passes WCAG 2.2 AA

Read through WCAG2ICT, as Article 4 requires, where *"a single 'web page' was equated to a 'software program'"* (`requirements.md` §15, citing UX's earlier retrieval).

- **SC 1.4.3 Contrast (Minimum) and SC 1.4.11 Non-text Contrast.** Every text pair at 4.5:1 or better and every UI pair at 3:1 or better, in light and dark, including both ends of every gradient (appendix of `brand-directions.md`). SC 1.4.3 requires *"a contrast ratio of at least 4.5:1"* and SC 1.4.11 *"at least 3:1 against adjacent color(s)"* [E].
- **SC 2.2.2 Pause, Stop, Hide (Level A).** The criterion: *"For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it…"* [E]. **The ticker** meets it with a visible pause control whenever it moves, remembered across launches, plus the options control that turns it off in two taps (HEAD-5, HEAD-9). **Blinking:** W3C's guidance accepts content that blinks *"for less than 5 seconds"* [E], but the retro theme has **no blinking content of any duration**, so it does not lean on that allowance.
- **SC 2.3.1 Three Flashes or Below Threshold (Level A):** *"do not contain anything that flashes more than three times in any one second period"* [E]. Nothing in any theme flashes. The retro theme's colour pairs are never alternated.
- **Reduce motion (HEAD-10, a CEO decision, BLOCKING in requirements).** The retro ticker drops to the still Line under iOS Reduce Motion and Android Remove animations, live and without relaunch, exactly as in the default. **SC 2.3.3 is Level AAA** and not part of the baseline (`requirements.md` HEAD-10 records this); the obligation here comes from the CEO's decision, not from WCAG.
- **Screen readers and large text (HEAD-11).** The ticker becomes the still Line while VoiceOver or TalkBack runs and at accessibility text sizes.
- **SC 1.4.4 Resize Text (AA) and A11Y-4.** Everything scales with Dynamic Type. **The pixel face has a ceiling:** above a named size constant, and whenever Bold Text is on, Silkscreen labels render in DejaVu Sans Bold. The words are the same; only the face changes. Pixel capitals are hard to read at length [J], which is why they are limited to short labels in the first place.
- **SC 1.4.1 Use of Color (A) and A11Y-2.** Links are underlined; the selected tab differs in weight and fill; "Unconfirmed" is a word with a dashed outline; ratings are always also text ("4/5").
- **SC 2.5.8 Target Size (Minimum) and A11Y-5.** Bevel buttons, tabs, chips, the pause and options controls are all at least 44 × 44 pt in the mockups, comfortably above the minimum.
- **SC 2.4.11 Focus Not Obscured.** The title bar behaves as the default's header does. It is never a sticky overlay above focused content.
- **Screen-reader output is identical to the default's.** Same labels, same order, same roles, and no decorative glyph is spoken. This follows from §2's rule that a theme changes no copy.

**What would make the retro theme fail, stated so QA can look for it:** a gradient step or texture behind text that was never measured; a pixel label that does not swap at large sizes; a period animation that sneaks back as "delight"; a count set in LED digits because it "looks fun"; and any retro string that is not in the one string table.

---

## 9. Draft requirements, for the PM/BA to lift after the CEO signs off a direction

In `requirements.md`'s column layout. **Drafts only**: they enter through a §24 scope-change row (D38(4)), and priorities are proposals.

| # | Requirement | Acceptance criteria (QA-verifiable) | Priority | Source |
|---|---|---|---|---|
| **THEME-1** | **Themes change appearance only.** A theme may set colour, type, shape, iconography, texture, motion style and the styling of each headline appearance, and nothing else. | (a) For each theme, capture the VoiceOver and TalkBack reading of every primary screen; assert the transcripts are identical across themes. (b) Assert every screen's element order and position is identical across themes (layout snapshot diff, colour-blind). (c) Assert the string table is identical: no theme-specific strings. | **MUST** | D38; this note §2 [J] |
| **THEME-2** | **Every theme meets the accessibility requirements in light and dark.** | (a) CI runs `contrast.py --check` over every token pair of every theme and mode; the build fails on any failure. (b) A11Y-10's per-release checklist runs in every theme. (c) No text is placed over texture or an unmeasured gradient. | **BLOCKING** | Constitution Article 4 (WCAG 2.2 AA); D38(1) — *"A retro theme is a look, not an exemption"* |
| **THEME-3** | **The theme never selects the headline appearance.** | Set Line, switch to each theme and back; assert Line persists. Repeat for Card, Ticker and Off. | **BLOCKING** | HEAD-2 (persistence); HEAD-10 (no motion by side effect) |
| **THEME-4** | **Every theme is equally still under Reduce Motion / Remove animations, and adds no motion outside §6.3's budget.** | (a) HEAD-10's device tests, in every theme. (b) Assert no theme defines an animation absent from the default. | **BLOCKING** for (a); **MUST** for (b) | HEAD-10; A11Y-9 |
| **THEME-5** | **Theme and light/dark are chosen in Settings → Appearance, persist, and are never promoted.** Defaults: the modern default theme; *Match phone*. | (a) Assert no prompt, banner, badge, tip or "NEW" label refers to themes, ever. (b) Assert both settings persist across relaunch and update and round-trip through export. (c) Settings register (DFLT-1) records both, with *"neither value is more protective"* as the reason. | **MUST** | DFLT-1; HEAD-7, HEAD-8 by analogy [J] |
| **THEME-6** | **No theme is a reward, and every theme is available in every entitlement state.** | (a) Assert no theme's availability depends on usage, time or visit counts. (b) Run ENT-14's entitlement fixtures; assert the theme list and the rendering are identical in every state. | **BLOCKING** for (a); **MUST** for (b) | (a) **MEM-1**; (b) this seat's recommendation, **a pricing choice for the CEO** (Constitution 5.4) |
| **THEME-7** | **Privacy surfaces are theme-independent in content.** The app-switcher cover, the Privacy screen, the transmission sentence, the backup and export flows and the passphrase moment show identical content in every theme. | Per theme: repeat HEAD-12(a)–(b) and PRIV-2(a); assert identical content. | **BLOCKING** | HEAD-12; PRIV-1; PRIV-2 |
| **THEME-8** | **Homepage carries none of the out-list in §8.3.** | QA inspects every Homepage screen against §8.3's table and records the result per row in the release pack. | **BLOCKING** | MEM-1; HEAD-6, HEAD-8, HEAD-9; D38(2) |
| **THEME-9** | **Bundled font notices ship with the app.** | Assert the About or Licences screen lists each bundled font's copyright statement, licence notice and licence text (or a link to the full text shipped in the app). | **MUST** | OFL FAQ 1.20 [E]; a LIC-section row |

---

## 10. Disagreement, and negative findings

### 10.1 One disagreement with the commission's wording, recorded once

The commission lists *"headline presentation (Ticker/Line/Card)"* among the things a theme may change. **I read that as the styling of each appearance, and I have written the system that way.** If it was meant as "a theme may choose which appearance is shown", for example Homepage switching the ticker on, **I disagree**, for three reasons:

1. It would switch **motion** on as a side effect of a choice about colours. Reduce Motion still protects users who have set it, but everyone else gets moving text they did not ask for, and a user who turned the ticker *off* would find it back on.
2. It would break **HEAD-2's persistence** (*"the choice persists across relaunch and update"*) through the back door.
3. The CEO's own route to the retro ticker costs one tap: choose Homepage, then choose Ticker in the headline options. **Nothing is lost by keeping the two choices separate.**

If the CEO wants Homepage to *suggest* the ticker, the honest version is a still preview of the ticker in the theme picker, with no automatic change. I would accept that.

### 10.2 Negative findings

| Finding | What would overturn it | Where I looked |
|---|---|---|
| **Two themes at launch, not more** | The CTO's sizing showing the per-theme verification cost is much lower than my 15–25% guess, for example because snapshot and accessibility tests can be run per theme automatically | My own estimate; A11Y-10's checklist; no CTO input yet |
| **No alternate app icons per theme at launch** | A sizing showing it is cheap, and the CEO wanting it | Platform capability is [K]; not retrieved |
| **Verdana and Georgia cannot be bundled** | The Microsoft licence, retrieved, permitting redistribution in a paid app | Not retrieved; the exclusion is cautious. Gelasio and DejaVu make the question moot |
| **Themes should not be sold separately** | The CEO's pricing decision | A recommendation, not a finding under any clause |

**Honesty statement:** no one has used either theme. Whether the retro theme reads as delightful or as a joke that wears thin is exactly the question a five-to-eight-person preference test would answer (`requirements.md` §22 item 1).

---

## 11. Evidence register (retrieved 2026-09-26 by this seat)

| # | Claim | Source |
|---|---|---|
| E1 | SC 2.2.2 text, Level A; blinking vs flashing; blinking under five seconds acceptable | [W3C Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) |
| E2 | SC 2.3.1 text, Level A | [W3C Understanding 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) |
| E3 | SC 1.4.3 and SC 1.4.11 text | [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) |
| E4 | Relative luminance formula | [W3C WAI wiki](https://www.w3.org/WAI/GL/wiki/Relative_luminance) |
| E5 | OFL bundling permission and notice requirement | [OFL FAQ](https://openfontlicense.org/ofl-faq/) 1.4, 1.20 |
| E6 | Gelasio: OFL 1.1; metric-compatible with Georgia | [OFL file](https://raw.githubusercontent.com/google/fonts/main/ofl/gelasio/OFL.txt); [README](https://github.com/SorkinType/Gelasio) (single source) |
| E7 | Silkscreen: OFL 1.1; Kottke, 2001 | [OFL file](https://raw.githubusercontent.com/google/fonts/main/ofl/silkscreen/OFL.txt); [README](https://github.com/googlefonts/silkscreen) (single source) |
| E8 | DejaVu / Bitstream Vera licence terms | [DejaVu LICENSE](https://raw.githubusercontent.com/dejavu-fonts/dejavu-fonts/master/LICENSE) |

**[K], not retrieved:** early-2000s web conventions (Verdana, `<blink>`, `<marquee>`, portal modules); Verdana's licence; Geocities' ownership; platform support for alternate app icons; SC 1.4.2's level; font file sizes.



# Haunts design, round 3: final marks, theme names, the theme picker, and the app-icon question

**Seat:** UX / Design Lead · **Date:** 2026-09-27 · **Slug:** `haunt` · **Commission:** **D44** (CEO, 2026-09-27), read at `decisions/2026-09-16-haunt-gate.md` in the coordinator's worktree.
**What D44 decided:** *"Theme set at launch: Hybrid A ("warm editorial"), Hybrid B ("mono editorial") and Homepage (retro), each selectable by the user."* Hybrid A's wordmark and icon take **Almanac's double underline**; **the A icon is the Masthead h on plum with the double underline**, and the full-stop h is liked as an alternative; **the B icon is the h with the orange bar**. **The default theme is referred to UX and the Research Analyst**, and comes back to the CEO.
**Earlier rounds are unchanged:** `../brand-directions.md`, `../themes.md`, `../icon-brief.md` (round 1), `../round-2/directions.md`. **The round-3 icon brief is a new file**, [`icon-brief.md`](icon-brief.md), superseding round 1's for the final marks only.
**Also covers D45** (CEO, 2026-09-27): Mono's typed headline with a blinking cursor (§6), and Contour texture for Warm only (§7).
**Files:** concepts in [`concepts/`](concepts/); generator `../tools/generate_round3.py`; contrast is unchanged from round 2 (the palettes did not change), re-run with `python3 ../tools/contrast.py --round2`.
**Status:** prepares and flags; certifies nothing (Constitution 6.1). **Evidence:** tagged under `pipeline/evidence-standard.md`; round-3 retrievals were made on 2026-09-27 and are listed in §7.

---

## 0. The answers

1. **Final marks** (§1): **A** is the cream Masthead h on plum over an apricot double rule, thick over thin. **A's alternative** is the full-stop h. **B** is the white h on black with a short orange bar at its foot. Each is drawn for iOS's default, dark and tinted appearances and for Android's adaptive and themed icons. The wordmarks: lowercase "haunts" in Newsreader, **with the double rule for A** and the orange margin rule for B.
2. **Theme names, recommended: "Warm", "Mono" and "Retro"** (§2). Alternatives are given for each.
3. **The theme picker** (§3): Settings → Appearance, three theme cards with **live previews on sample content**, one tap to apply, and no confirmation step. It is a proper radio group for screen readers, and it becomes a single column at large text sizes.
4. **The app icon** (§4): three options. **My recommendation:** ship with **one icon** at launch, then offer **a separate, user-chosen "App icon" setting** (A's mark or B's) once the CTO confirms the cost. **Never tie the icon to the theme automatically.**
5. **The default theme** (§5): the Research Analyst's to research and the CEO's to decide. **My own recommendation is Warm (Hybrid A)**, because it is the clearest for a first-time user and the most recognisable in the store.
6. **Mono's typed headline** (§6), per D45: **25 characters a second, held 4 s, cursor blinking once a second, at most 3 facts per open**. The pause control stops everything. It **replaces Mono's crawl**. **One reading to confirm:** D45's "announces each sentence once" should mean "read once when focused", since HEAD-16 says headlines are never announced.
7. **Contour texture is Warm's alone** (§7).

**The next decision for the CEO: the three theme names** (§2), because the picker, the store listing and the copy all use them.

---

## 1. The final marks

**Sheets:** `concepts/icons-final.svg` (every icon in every appearance, with Android's safe zone shown) and `concepts/wordmarks-final.svg`. **1024 px masters:** `concepts/a-icon-masthead.svg`, `concepts/a-icon-fullstop.svg`, `concepts/b-icon-bar.svg`.

### 1.1 A (Warm): Masthead h, double underline

- **Plum** `#5B2A86` field; **cream** `#FFF8F1` slab-serif lowercase h; beneath it an **apricot** `#F2A65A` **double rule: thick (36 px) over thin (16 px), 16 px apart**, the same width as the h's feet.
- **Why these weights** [J]: at 60 px the thin rule is about 0.9 px and the thick about 2 px, so both still read. At 29 px the thin rule blurs into the thick one, which reads as a single rule and does no harm. On iOS the system scales one 1024 px master, so there is no separate small-size drawing (round 1, `icon-brief.md` §2.1).
- **Dark appearance (iOS):** the plum field becomes near-black plum `#1A1422`, while the h stays cream and the rules apricot. **Tinted and themed (iOS tinted, Android monochrome):** the h and both rules as one silhouette.
- **Android adaptive:** the h and rules as the foreground, scaled to **90%** so the whole mark sits inside the 66/108 safe zone (shown on the sheet); plum as the background.

### 1.2 A's alternative: the full-stop h

A plum h with an **apricot full stop**, on cream. It is kept fully worked, as D44 asked: dark (cream h on dark plum), tinted and adaptive. **Its strength** [J]: it reads best of all at 29 px and needs no rule. **Its weakness:** on a cream field it is the paler icon on a busy home screen, and it matches the Warm theme's page rather than its brand colour.

### 1.3 B (Mono): h with the orange bar

- **Black** `#111111` field, **white** h, a **short orange bar** `#C2410C` at the h's right foot, like a text cursor that never blinks.
- **Dark appearance:** already dark, so the field deepens to `#0F0F10` and nothing else changes. **Tinted and themed:** the h and bar as one silhouette.
- **The mark's bar is never animated** (the launch screen, onboarding, marketing) [J]. D45's blinking cursor belongs to Mono's typed headline alone, under D45's conditions. It does not license animating the icon or the wordmark.

### 1.4 Wordmarks

- **A:** "haunts" in lowercase Newsreader semibold, with the **apricot double rule** under it. **At credit sizes** (the LOOK-5 recap footer, anywhere the wordmark is under about 32 px tall) the double rule becomes a single hairline, because a thin rule below 1 px is noise [J].
- **B:** "haunts" in the same face, preceded by **the orange margin rule** (round 2).
- **The SVG wordmarks use a stand-in** for Newsreader (New York or Georgia); final artwork draws them from Newsreader and outlines them (round-3 `icon-brief.md` §4).
- **Contrast:** the logotype is exempt (*"Text that is part of a logo or brand name has no contrast requirement"*, SC 1.4.3 [E, round 1]), and both still exceed 4.5:1 on their own backgrounds (round 2, appendix A).

---

## 2. Theme names

**What a good name does here** [J]: it tells a stranger what they will see, in one plain word; it translates easily; it does not imply one theme is better (so no "Classic", "Pro" or "Premium"); and it never uses "Default", because the default may change.

| Theme | Recommended | Alternatives | Against the alternatives |
|---|---|---|---|
| **Hybrid A** (cream, plum, apricot, serif headlines) | **Warm** | *Colour*; *Paper* | "Colour" is accurate but flat; "Paper" describes the old Almanac more than A |
| **Hybrid B** (black and white, monospace details) | **Mono** | *Monochrome*; *Black & white* | "Monochrome" is the same word, longer; "Black & white" is two words and awkward in dark mode, where it is white on black |
| **Homepage** (early-2000s web) | **Retro** | *Homepage*; *Early web* | "Homepage" is my round-1 working name and a nice joke, but people don't all get it [J]; "Early web" is clear but less friendly |

**Each name carries one line of description in the picker** (§3), so the name does not have to do all the work:

- **Warm**: *"Cream and plum, with serif headlines."*
- **Mono**: *"Black and white, with typewriter details."*
- **Retro**: *"Styled like a website from the early 2000s."*

These lines are **draft copy**. They join the string table and go through the same MEM-1 and HEAD-6 string search as every other string (MEM-1(a)).

---

## 3. The theme picker

**Sheet:** `concepts/theme-picker.svg`: (1) Warm in use, light; (2) Mono in use, dark; (3) the largest text size, as one column.

**Where:** Settings → **Appearance**, holding two things: **Theme** (three cards) and **Light or dark** (*Match phone*, *Light*, *Dark*, per round 1 §6.1). The headline appearance stays in the headline options, where it is today (HEAD-5).

**Live previews, on sample content.** Each card renders **the real theme** from its tokens, so it is always accurate in light, dark and at the user's text size. But it renders on **fixed sample content** (the fictional venues from the mockups), **never the user's own journal**, for two reasons: HEAD-13 keeps headlines to the home screen (*"Headlines appear only on the in-app home screen"*), and a settings screen full of the user's places is one more surface for someone glancing at the phone [J]. **The cards are labelled by name and description, not by the preview**, so the preview can stay decorative.

**Choosing:** one tap applies the theme immediately. There is **no Save and no confirmation**, and it is reversible with one more tap. **Nothing is locked, earned, promoted or marked "NEW"** (THEME-5, THEME-6; HEAD-8 by analogy). The change cross-fades over 200 ms, or instantly under Reduce Motion.

**Accessibility, as requirements** (for the PM/BA's §24 row):

| Need | Design |
|---|---|
| Screen reader structure | The three cards are **one radio group**. Each card is one element: *"Warm. Cream and plum, with serif headlines. Selected. 1 of 3."* **Previews are hidden from assistive technology** (they duplicate the name and description) |
| Not by colour alone (A11Y-2) | Selected = **a 3 pt border and a check mark**; unselected = a 1 pt outline. The segmented control's selected segment has a border and bold text |
| Large text (A11Y-4) | At accessibility text sizes the three columns become **one column**: a small preview left, the name and description right, wrapping freely (third phone) |
| Targets (A11Y-5) | Each card is far larger than 44 pt; each segment is 44 pt tall |
| Focus (SC 2.4.11) | The screen scrolls clear of the floating tab bar, as on the home screen (round 2 §4.3) |
| Contrast | Every label is an ordinary token pair, already measured (round 2, appendix A) |

---

## 4. Should people choose the app icon too?

D44(4): *"Whether users may also choose the app icon (alternate app icons) is a question for the CEO, with the CTO on feasibility."* Three options; **feasibility is the CTO's to confirm, and nothing below asserts it.**

**What Apple says, retrieved** [E, HIG App icons, 2026-09-27]: *"it's possible to let people visit your app's settings to choose an alternate version of your app icon"*; *"make sure each icon you design remains closely related to your content and experience. Avoid creating one someone might mistake for another app"*; and *"Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants… all alternate and variant icons are subject to app review."* The API *"Changes the icon the system displays for the app"*, and the alternates are declared in the build [E, UIKit `setAlternateIconName`].

| Option | For | Against |
|---|---|---|
| **1. One icon for everyone** (the store icon) | Simplest; one recognisable mark on every home screen and in every screenshot; no extra assets or review | A Mono user sees a plum icon (or a Warm user a black one), which is the mismatch D44 notices |
| **2. A separate "App icon" setting the user chooses**, independent of the theme; default = the store icon (`concepts/app-icon-setting.svg`) | Fits the CEO's reason for themes (*"they can view it as they want"*); a Mono user can have a black icon; no surprises, because nothing changes unless the user asks | Every alternate needs its own **dark, clear and tinted** variants [E], so about 4 × 3 = 12 icon renders instead of 4; more store review surface; **iOS may show a system notice when the icon changes** [K, medium confidence, not in the retrieved page]; Android does it differently and may have launcher caveats [K, low confidence]; QA on both |
| **3. The icon follows the theme automatically** | Always matches | **Rejected** [J]. The home screen changes as a side effect of a settings choice; on iOS a system notice may interrupt a theme change [K]; and it ties together two choices people make for different reasons. **Round 1's rule stands: a theme never changes the app icon** |

**My recommendation** [J]: **option 1 at launch, then option 2 in a later release**, if the CTO confirms it is modest. Offer the three final marks (Plum, Cream, Black; draft names describing what people see). It is a real, cheap delight that matches the CEO's customisation point, and it can follow launch without anything being taken away from anyone. **One guardrail, from Apple's own text:** no "discreet" or disguised icon that looks like another app (a calculator, say), however privacy-minded the motive. *"Avoid creating one someone might mistake for another app"* [E].

**Which icon is the store icon** follows from the default theme (§5): the store listing should show the icon of the theme people will first see.

---

## 5. The default theme: my recommendation, for the Research Analyst and the CEO

**This is not a decision.** D44 refers it to UX and the Research Analyst, and it returns to the CEO. D44(1) also sets the test: *"the theme most appealing and clearest to a new user, never one chosen to increase time in the app."*

**My recommendation: Warm (Hybrid A)** [J], for four reasons:

1. **Clearest for a first-time, non-technical user**, the charter's first question. Plain section words (*"To confirm"*), one accent, and the headline in a card that says what it is. Mono's `//` and `>` are a small puzzle to some people; Retro can read as a joke, or as an old and unmaintained app, in a store screenshot [J].
2. **The most recognisable store presence.** Plum and apricot stand out among app icons, which is why the CEO preferred Doorway's colours (D42). A black icon is common [K, medium confidence].
3. **It carries the brand story**: a warm journal of places, with memories set like headlines.
4. **The customisation is easier to show from Warm outward.** A store screenshot can show all three themes side by side as a feature (sample data only, HEAD-13) [J]. Starting on Mono or Retro makes the other two look like the exceptions.

**What would change my mind:** the CVO's point (2) stands. **A small preference test with real people**, showing the three home screens and the three icons to five to eight people who have not seen them and asking which they would choose and why, would settle this better than desk research or my judgment. It needs the CEO's authorisation (`requirements.md` §22 item 1).

---

## 6. Mono's typed headline ("like a console")

**Sheet:** `concepts/b-typed-headline.svg`: six frames (typing, held, the blink's off phase, next, rest, paused), light and dark, with a timeline.

**The CEO's idea:** *"Hybrid B actually typing it in like a console with an underscore flashing, stays on screen for a few seconds before moving on."*

### 6.1 The amendment, and one reading to confirm

**HEAD-8 was BLOCKING against this** (*"No … flashing, entry animation …"*). **D45 (CEO, 2026-09-27) amends it for Mono's typed headline only**: *"I do not believe the flash would provide urgency or make it compulsive, it is just for style."* The cursor **keeps blinking when the typing stops**, at the CEO's express preference. *"HEAD-8 itself stands for every other appearance and theme."* D45's conditions bind as acceptance criteria, and this design meets each of them (§6.3). The PM/BA owes the §24 row.

**One reading to confirm, stated once.** D45 says *"a screen reader announces each sentence once, never letter by letter"*. **HEAD-16 (BLOCKING) says headlines are "Never a live region; never announced"**, and D45 does not amend HEAD-16. **I read D45 as: when a screen reader reaches the headline, it reads each sentence once, whole.** It is not a spoken announcement pushed as each sentence arrives. Under HEAD-11 the typed headline never runs while a screen reader is on anyway: the full sentence is shown still. If D45 meant a live announcement, it would conflict with HEAD-16, and I would argue against it: an announced headline is a spoken push, the thing HEAD-16 exists to prevent. **The coordinator should confirm the reading with the CEO**; the design follows mine.

**It also narrows one of my own round-1 rules**, not a constitutional one: THEME-4(b) says no theme adds an animation the default lacks. I propose restating it as *"a theme may restyle the motion of the moving headline appearance, provided every HEAD-9 to HEAD-11 guardrail holds identically"*. That is my rule to change, and I say so.

### 6.2 How it behaves

- **Only if the user chose the moving headline appearance** (HEAD-2). In Mono, the moving appearance **is** the typed headline: **it replaces Mono's crawl** rather than sitting beside it as a fifth appearance, because two moving options in one theme is one choice too many [J]. It fits best as **Mono's styling of round 2's Rotate** (one whole fact at a time), which already needed a §24 change.
- **Set in monospace** (Plex Mono), so it reads as a console and the cursor sits exactly after the last character. The cursor is a short **orange underscore**, the same orange as B's icon bar.
- **Always visible:** the pause control and the options control (HEAD-5, HEAD-9).

**Proposed timings** (named constants, [J], for UX to sign off on a device, as D45 asks):

| Constant | Proposed | Why |
|---|---|---|
| Typing rate | **25 characters a second, constant** (40 ms a character; ~2.8 s for a 70-character fact) | Brisk enough to feel alive, slow enough to read along with. **No jitter, no acceleration, no dramatic pauses** (D45: *"no variation in typing speed for effect"*) |
| Cursor while typing | **Steady** | It moves with the text; blinking as well would be two motions at once |
| Hold after each fact | **4.0 s**, cursor blinking | Time to read a 12-word sentence once, comfortably [J] |
| Clear between facts | **Instant** (no wipe or backspace effect) | A backspacing animation is a trick |
| Facts per pass | **All eligible facts in the fixed daily order (HEAD-3), capped at 3 per open** | Keeps one pass under about 21 s [J] |
| Cursor blink period | **1.0 s: 0.5 s on, 0.5 s off** | One flash a second, a third of SC 2.3.1's limit of three |
| At rest | **The last full sentence, cursor blinking** (D45) | **Blinking stops when the user pauses, when the headline scrolls off screen, or when the app leaves the foreground** [J]: no one is looking then, so it stops |
| Pause | **Stops typing and blinking at once**; if paused mid-sentence, the **full sentence appears immediately** with a steady cursor. **Paused persists** across launches (HEAD-9); later opens show the full sentence still | D45: *"the visible pause control stops the typing and the blinking"*. Freezing on half a sentence would be unreadable |

### 6.3 D45's conditions, checked

| Condition | Status |
|---|---|
| **One pass per open, then rest on a full sentence** (HEAD-9) | Yes: at most 3 facts, then it rests on the last one, whole |
| **Blink rate far below three flashes a second** (SC 2.3.1: *"do not contain anything that flashes more than three times in any one second period"* [E, round 1]) | **1 flash a second.** The cursor is a few pixels in area as well [I] |
| **The visible pause control stops the typing and the blinking; paused persists** (SC 2.2.2 requires a way to pause blinking that lasts more than five seconds [E, round 1]) | Yes. The blinking lasts longer than 5 s, so the pause control is what makes it conform, and it is always visible |
| **Reduce Motion, Remove animations or a screen reader: the full sentence at once, with a steady cursor** (HEAD-10, HEAD-11) | Yes, and also at accessibility text sizes (HEAD-11). HEAD-10(b)'s Android device test applies |
| **A screen reader reads each sentence once, never letter by letter** | Yes. **The accessible label is always the complete sentence**, never the partly typed text; read on focus, not announced (§6.1) |
| **No sound, nothing marking a headline as new or unseen, no variation in typing speed for effect** | Yes: no sound, no colour change, no "new" marker, constant speed |
| **MEM-1 and HEAD-6** | The words are the same template catalogue; only their arrival is styled |
| **Never the default appearance** | Line stays the default headline appearance in every theme (HEAD-2) |

### 6.4 Cost [J]

About **1–2 days** on top of the Rotate work, plus a device check of both reduce-motion paths (HEAD-10(b)'s Android trap applies).

---

## 7. The Contour touch is Warm's only

Per the CEO's note: **the contour-line texture in the self-portrait and heatmap header bands belongs to Warm (Hybrid A) only. Mono has none**, and Retro has none. Round 2 §7's rules are unchanged: open lines only, never behind text or controls, never on the home screen. Mono's equivalent restraint is the point of Mono.

---

## 8. Cost, evidence and open items

**Cost** [J], new in round 3, none of it in the 2,090-hour estimate: the theme picker **2–3 days**; alternate app icons (option 2), if chosen, **2–4 days plus 8 extra icon renders and store review**; the typed headline **1–2 days**. D44(3)'s three-theme cost stands: roughly 2–3 days per extra theme plus 15–25% more UI verification each.

**Evidence retrieved in round 3 (2026-09-27):**

| # | Claim | Source |
|---|---|---|
| E1 | Alternate icons are chosen in the app's settings; must stay *"closely related to your content"*; *"Avoid creating one someone might mistake for another app"*; each needs *"dark, clear, and tinted variants"*; all are subject to app review | [Apple HIG, App icons (JSON of the page)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json) |
| E2 | `setAlternateIconName` *"Changes the icon the system displays for the app"*; alternates are declared in the build; `supportsAlternateIcons` | [UIKit documentation (JSON)](https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setalternateiconname(_:completionhandler:).json) |

**[K], not retrieved:** whether iOS shows a notice when the icon changes (the retrieved page is silent); how Android handles alternate icons; how common black app icons are.

**Open, and whose:**
1. **The theme names** (§2), the CEO's, and the next decision.
2. **The default theme** (§5): the Research Analyst, then the CEO.
3. **Alternate icons** (§4): the CEO, with the CTO on feasibility.
4. **The typed headline** (§6): HEAD-8 was amended by D45. Still owed: the PM/BA's §24 row, UX's on-device sign-off of the timings, and **confirmation that D45's "announces" means "read once when focused"** (HEAD-16).
5. **Rotate** as a replacement for the crawl (round 2 §5): a §24 row for the PM/BA.
6. **Rights in a tool-made mark** (`requirements.md` §22 item 18): the CGO, before any artwork spend (round-3 `icon-brief.md` §6).

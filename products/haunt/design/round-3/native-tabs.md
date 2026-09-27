# Native Tabs: what the system tab bar means for the design

**Seat:** UX / Design Lead · **Date:** 2026-09-27 · **Slug:** `haunt`
**Asked:** the CEO proposes **Expo Router Native Tabs** for the tab bar. **Decisions read:** D48 (floating bar in every theme; *"Retro's bar is always solid and bevelled"*) and D52 (theme-specific components allowed, *"kept to a minimum"*), in the coordinator's worktree copy of `decisions/2026-09-16-haunt-gate.md`.
**Status:** prepares and flags; certifies nothing (Constitution 6.1). **Feasibility is the CTO's**; nothing here asserts what React Native can do beyond what the Expo page says.
**Evidence:** [Expo, Native Tabs](https://docs.expo.dev/router/advanced/native-tabs/), retrieved 2026-09-27 (read through a summarising retrieval tool, so the CTO should read the page itself). Apple's HIG Materials and Tab bars pages were retrieved in round 2 (§4.1).

---

## 0. Recommendation

**Adopt Native Tabs in all three themes, and accept the system bar everywhere, Retro included**, with each theme's colours applied where the platform allows [J]. It gives real Liquid Glass for free, lets the platform handle legibility and the accessibility settings, and removes the CTO's ~22 hours plus a per-release device check for a custom bar. It costs some brand control over one component the user barely looks at. **Two parts of D48 would change, so they go back to the CEO:** Android's bar becomes the docked Material bar rather than a floating pill, and Retro's bar is no longer bevelled.

---

## 1. What Native Tabs gives, per the Expo page

- **iOS 26:** *"the system draws the tab bar with Liquid Glass and derives its background from the content behind it. The `backgroundColor`, `blurEffect`, `shadowColor`, and `disableTransparentOnScrollEdge` props affect the iOS tab bar only on iOS 18 and earlier."* Colours: *"Liquid glass on iOS automatically changes colors based on if the background color is light or dark… you need to use a `PlatformColor` or `DynamicColorIOS` to set the color of the icon"*, and *"the tab bar does not follow a color scheme that exists only in JavaScript."* [E]
- **Android:** the Material tab bar; *"a maximum of 5 tabs"* (we have 4). [E]
- **Limits that touch us:** *"Cannot measure tab bar height"*; limited FlatList support (no scroll-to-top or minimise-on-scroll with it; we did not want minimise anyway, round 2 §4.3). [E]

**For the CTO to confirm** [K]: whether iOS 26 respects a custom label font (probably not: expect the system font); how theme tint colours are passed as dynamic colours when the theme changes at runtime; and how list content is inset so the last row clears the bar, given its height cannot be measured (SC 2.4.11).

---

## 2. The five questions

### 2.1 Retro's bevelled bar

On iOS 26 the background is not ours to set, so **a bevelled bar is impossible with Native Tabs** [I, from §1]. There are two ways out:

| Option | What it takes | Verdict [J] |
|---|---|---|
| **R1. Keep a bevelled bar**, a Retro-only custom bar, as D48 says | Either hide the system bar and overlay our own when Retro is active, or switch navigator at runtime. Neither is confirmed possible, and both mean two tab-bar code paths, two accessibility implementations and two device checks | **This is the "complicates things" D52 warns against**, for one opt-in theme |
| **R2. Accept the system bar in Retro**, tinted in Retro's link blue on iOS, and in Retro's colours (solid background) on Android, where `backgroundColor` works | Nothing beyond the other themes | **Recommended.** Retro's character lives in its content (the navy title bar, boxed modules, bevelled buttons, underlined links, the portal ticker), and those all stay. A glass bar under a 2003 page is a mild anachronism, and a kind one: it is the one element that behaves exactly like every other iPhone app |

**R2 reverses D48's "Retro's bar is always solid and bevelled"**, so it is the CEO's call. If he keeps D48, R1 needs the CTO to confirm a contained way to do it first.

### 2.2 The floating pill on Android

Native Tabs renders the **Material** bar on Android, which is **docked full-width** with a pill behind the selected icon, not floating [K, medium confidence: the Expo page names it the Material tab bar but does not describe its shape]. **Recommendation: accept it** [J]. It is native, accessible and familiar to Android users, and `backgroundColor` works there, so each theme's bar is simply opaque in its own colours (which is what D48 already wanted on Android). **What is lost:** on Android only, the extra vertical space the floating bar gave. **This also amends D48** (*"a floating tab bar in every theme"*), for Android.

### 2.3 Do Warm and Mono still feel distinct?

**Yes** [J]. The bar was never what distinguished them. The difference is in the content: Warm's apricot headline card, cream page and rounded cards against Mono's black and white, monospace times and margin column, with Newsreader in both. On iOS 26 the glass also **takes its tint from the content behind it** [E], so a Warm bar will look faintly warm and a Mono bar neutral. The selected-tab colour (plum or black and white) comes through the tint colours. Warm, Mono and Retro will share one bar *shape*, and that is fine: it is the platform's, and people know it.

### 2.4 The accessibility floors

My floors (**≥ 80% opaque in light, ≥ 90% in dark**, round 2 §4.2) were written for **a translucent bar we draw ourselves**, where we choose the opacity and must prove the worst case. With the system bar we **cannot** set opacity. Apple's regular glass *"blurs and adjusts the luminosity of background content to maintain legibility"*, and its appearance changes when people *"reduce transparency or increase contrast"* [E, HIG Materials, round 2]. **Recommendation: accept the platform's legibility handling, and verify it rather than trust it** [J]:

- **Add a row to A11Y-10's per-release checklist:** tab labels and icons legible over the worst content we produce (a white photo thumbnail, Warm's apricot card, Mono's white Review button), in light and dark, **with Reduce Transparency on and with Increase Contrast on**, on the oldest supported iPhone.
- **If it fails,** the fix available to us is content-side: keep bright blocks from sitting under the bar at rest, since the list's bottom inset leaves clear space. Record the failure honestly. **Candour's WCAG 2.2 AA claim stays ours even when the component is Apple's** (Constitution Article 4) [J].
- **The CTO's 22 hours and the per-release glass measurement go away**; this lighter check replaces them.

### 2.5 Mono's margin column

D52 settles it: **Mono's margin column of times is allowed**, as a reusable component variant (§3). It changes the row's presentation, not its information: every row still carries the same venue, category, times, duration, rating and note, read in the same order by screen readers (A11Y-6).

---

## 3. Theme-specific components, as few as possible

D52's conditions: each is *"easy to use, reusable"*, **a variant of a shared component, never a fork of a screen**, and changes no information architecture, copy, accessibility, privacy surface or behaviour.

| # | Component (one shared component, with a theme variant) | Variants | Why it earns an exception |
|---|---|---|---|
| **1** | **`MovingHeadline`**: how the Ticker appearance moves (only when the user chose Ticker, HEAD-2) | **Rotate** (Warm, D49) · **Typed** (Mono, D45) · **Crawl** (Retro, the portal marquee) | Decided by D45 and D49. **One component, three modes, identical controls** (pause, options), and identical fallbacks (HEAD-9 to HEAD-11). *To save one mode, Retro could use Rotate in portal styling; I keep Crawl because Retro is where the marquee the CEO first asked for (D20) belongs* [J] |
| **2** | **`TimelineRow`**: time placement | **Inline** (Warm, Retro) · **Margin column** (Mono) | Mono's log-like identity (D42, D52). One prop; same content, same accessible label |
| **3** | **`HeaderTexture`**: an optional decorative band at the top of the self-portrait and heatmap screens | **Contour lines** (Warm only, D45) · none | Decoration only: no text, no controls, never on the home screen |

**Not components, only styling through tokens** (no exception needed): the headline container (Warm's apricot card, Mono's left rule, Retro's portal module); section-label prefixes (Mono's `//` and `>`, drawn as decoration and hidden from screen readers); Retro's bevelled edges and gradient title strips (round 1's shape tokens); corner radii, fonts and colours.

**Explicitly not proposed:** a Retro tab bar (§2.1); any theme-specific screen, navigation, setting or copy.

---

## 4. What goes back to whom

1. **CEO:** amend D48 for (a) **Retro accepting the system bar** (R2) and (b) **Android's docked Material bar**. My recommendation is both.
2. **CTO:** confirm §1's open points (label font, dynamic tint colours on a theme change, the bottom inset for SC 2.4.11), and whether `MovingHeadline`'s three modes and `TimelineRow`'s variant are contained components (D52).
3. **PM/BA:** amend the theme requirements for D52's variants (THEME-1 and THEME-4(b)), and add the §2.4 row to A11Y-10.

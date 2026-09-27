# Design feasibility and sizing: Haunts themes, floating bar, glass, headline motion, app icons

**Seat:** Chief Technology Officer · **Date:** 2026-09-27 · **Slug:** `haunt`
**Commissioned by:** the main session (orchestrator), on the CEO's design decisions **D38 and D42–D51** (`decisions/2026-09-16-haunt-gate.md`, read in the coordinator's worktree `agent-ab036df5635019c94`).
**Inputs read:** `products/haunt/design/themes.md`, `round-2/directions.md` §4–§6 and §10, `round-3/finalise.md` (UX, in worktree `agent-abc1fa15ec5982aa0`); `requirements.md` HEAD-9 to HEAD-16, A11Y-9, A11Y-10, PLAT-7, PLAT-8, §22 items 20–22; `subscription-sizing-note.md` (the unit of the 2,090-hour estimate).
**Stack assumed:** React Native with Expo, TypeScript, native Swift and Kotlin modules, iOS 26 minimum (D23, PLAT-8), Android minimum open (SPK-03).
**Status:** feasibility and sizing note. **It prepares and flags; it does not certify** (Constitution 6.1). It decides nothing reserved to the CEO under Constitution 5.4. D51 says that if the CTO finds the icon setting *"infeasible at launch, it comes back to the CEO rather than being dropped silently"*. §0 answers that directly.
**Template note:** `pipeline/templates/` has no feasibility or sizing template, so this note follows the layout of the CTO's earlier notes (`feasibility-note.md`, `android-and-stack-note.md`) and says so.
**Evidence:** tagged under `pipeline/evidence-standard.md`. Every [E] was retrieved by this seat on **2026-09-27**, and the link travels with the claim and again in the register at §9. Hours are [J] throughout. **Hours use the unit of the 2,090-hour estimate: focused solo hours, at 37.5 h a week and 7.5 h a day** (`subscription-sizing-note.md`). UX's day estimates are converted at 7.5 h.

---

## 0. The answer on one page

**Nothing the CEO decided is infeasible at launch.** Every item can be built on the stated stack from components that exist today. Three items carry conditions the CEO should know about, and none of them needs a new decision.

| Decision | Verdict | The one thing to know |
|---|---|---|
| **D48 floating bar, every theme** | **Feasible** | It must be **our own tab bar**, not the system one. Expo's native tabs cannot draw Retro's bevels, cannot draw Android's floating pill, and on iOS 26 ignore every background setting [E]. §1.2 |
| **D48 real Liquid Glass on iOS** | **Feasible, as real glass under our own frost layer** | Expo ships `GlassView`, a wrapper round Apple's native glass, for iOS 26 [E]. The 80% and 90% opacity floors are **guaranteed by a frost layer we draw over the glass**, not by the material, so they hold by construction. **Candidly, at 80–90% frost the glass shows only as a faint moving tint and a lit edge.** It will look close to the opaque bar, for about 22 h and a device check every release. §1.3 |
| **D48 under Reduce Transparency and Increase Contrast** | **Feasible** | React Native reads Reduce Transparency live on iOS [E]. It can read **Increase Contrast** but gives **no change event** for it [E], so a small native listener is needed (about 3–6 h). §1.4 |
| **D51 user-chosen app icon, at launch** | **Feasible on both platforms. Not infeasible, so nothing returns to the CEO on feasibility grounds** | On iOS, **an unsuppressible system alert** appears on every change [E]. On Android, the icon is switched by enabling a different launcher alias. **Some launchers are slow to refresh, and pinned shortcuts can be lost** [E, secondary sources]. The Expo library does not yet support Icon Composer icons as alternates [E], so we write a small config plugin. §2 |
| **D45 Mono's typed headline** | **Feasible** | Every setting it depends on can be read. **The Android reduce-motion defect is real**: React Native reads only the transition animation scale, and Android's *Remove animations* switch sets a different one [E]. The fix is a small Kotlin check that HEAD-10 already needs. §3 |
| **D49 Warm's Rotate** | **Feasible** | Simpler than a crawl. §3 |
| **Themes, fonts** | **Feasible** | Three themes × light, dark and Increase Contrast is **24 visual configurations per screen instead of 8**. The fonts are **3.3 MB unsubsetted (measured)**, which subsetting can reduce. §4 |

**Hours, outside the 2,090-hour estimate** (§5, [J]):

- **One-off build: 256–535 h, point estimate 376 h.** That is **+12% to +26% on 2,090 h (+18% at the point)**. It is about 1.3–1.7× the sum of UX's own day estimates (≈ 200–320 h), because this sizing adds design coverage of every screen in every theme, the test harness, fonts, template engineering and the icon pitfalls.
- **Ongoing: about 5–10.5 h per release**, plus **10–24 h a year** for OS and Expo upgrades. At 6–10 releases a year [J] that is **roughly 40–130 h/yr (point ≈ 76 h/yr)**, or **+11% to +36% on the 360 h/yr fixed maintenance**.
- **Not included:** the headline system itself (HEAD-1 to HEAD-18: the crawl, the pause control, the fallbacks). It is already owed to SPK-08. This note sizes only what the design decisions **add** to it.

**What goes back to the CEO:** no feasibility item. Three things he should see, one at a time, none urgent:

1. **Real glass is a value question, not a feasibility question.** It is the smallest visible gain for the cost in this list (§1.3). D48 stands as decided, and I am not blocking it.
2. **Retro is now the only theme with a crawl.** Styling Retro's ticker as Rotate would remove a whole motion implementation (§3.4). That is a question for UX and the CEO.
3. **Ongoing theme verification is +11% to +36% on fixed maintenance.** The CFO must cost it (SPK-09).

**Flags to other seats** (§7): UX's Mono *"margin column of times"* may break THEME-1's identical-layout rule. The *Neighbourhood* headline template may need data the venue index does not carry. An icon change on iOS 26.1+ makes the app resign active, which can trigger the app-switcher privacy cover (HEAD-12).

---

## 1. The floating bar and real Liquid Glass (D48)

### 1.1 What was asked

D48: a floating tab bar in Warm, Mono and Retro. Real Liquid Glass on iOS *"is conditional on the CTO confirming that React Native can render it"*. Where glass renders it is frosted, *"at least 80% opaque in light mode and 90% in dark, measured against the worst content beneath it"*. The bar is solid on Android, under Reduce Transparency or Increase Contrast, and wherever glass isn't feasible. Retro's bar is always solid and bevelled. UX's four questions are at `round-2/directions.md` §4.5.

### 1.2 Route rejected: the system tab bar (Expo Router native tabs)

This is the cheapest route to real glass, and it is the one UX hoped for (§4.5 item 1). **It does not fit this design, for three independent reasons.**

1. **The opacity floor cannot be set.** Expo's documentation says: *"On iOS 26 and later, the system draws the tab bar with Liquid Glass and derives its background from the content behind it. The `backgroundColor`, `blurEffect`, `shadowColor`, and `disableTransparentOnScrollEdge` props affect the iOS tab bar only on iOS 18 and earlier"* [E, [Expo, Native tabs](https://docs.expo.dev/router/advanced/native-tabs/)]. With iOS 26 as the minimum (D23), we could never impose the 80% and 90% floors. We would be relying on Apple's adaptive luminosity, which UX's model deliberately does not rely on (`round-2/directions.md` §4.2).
2. **Retro's bevelled bar cannot be drawn.** The native bar *"cannot be replaced with custom React components"*, and Expo points to custom tabs for *"a fully custom design that is not possible using system tabs"* [E, same page].
3. **Android would get a different bar.** Native tabs on Android use *"the platform's Material Tabs component"*, with a five-tab limit [E, same page], not the floating pill UX designed. THEME-1 and `themes.md` §2 require identical geometry on every platform and in every theme.

**So the bar is a custom tab bar component, the same on every platform and in every theme**, with only its material varying: glass, opaque or bevelled. This is not a loss. It is the only route that meets THEME-1 [I, from the three facts above].

**The price of a custom bar** [J]: it loses the native bar's free accessibility semantics. Tab roles, selected state, 44 pt targets (A11Y-5), VoiceOver and TalkBack order, Full Keyboard Access and Switch Control all have to be built and tested. The list must also carry bottom padding so no focused row sits entirely beneath the bar. SC 2.4.11 is UX's criterion at `round-2/directions.md` §4.3. That work is in the floating-bar hours (§5).

### 1.3 Real glass inside the custom bar: feasible

- **The component exists.** `expo-glass-effect` provides *"React components that render a liquid glass effect using iOS's native UIVisualEffectView"*. It supports iOS and tvOS and is *"Included in Expo Go"*. On other platforms, *"GlassView will fallback to regular View"*. It takes `glassEffectStyle` (`regular`, `clear`, `none`), `tintColor`, `isInteractive` and `colorScheme`. It has runtime checks, `isLiquidGlassAvailable()` and `isGlassEffectAPIAvailable()`, the second for crashes in *"some iOS 26 beta versions"* [E, [Expo, GlassEffect](https://docs.expo.dev/versions/latest/sdk/glass-effect/)]. Underneath it is Apple's `UIGlassEffect`, *"A visual effect that renders a glass material"*, available from **iOS 26.0** [E, [Apple, UIGlassEffect](https://developer.apple.com/tutorials/data/documentation/uikit/uiglasseffect.json)]. That matches our minimum exactly.
- **Someone is already doing exactly this.** `expo-glass-tabs` is a floating pill tab bar for Expo Router built on `expo-glass-effect`, with a *"solid fallback on older iOS and Android"* [E, [davidmokos/expo-glass-tabs](https://github.com/davidmokos/expo-glass-tabs), **single source**]. **I do not recommend adopting it:** three commits on its main branch, and no accessibility handling documented. It proves the pattern, not a dependency.

**How the opacity floor is met: by construction, not by trust.** The bar is three layers:

1. A `GlassView` in the regular style. UX specifies the regular variant only (`round-2/directions.md` §4.1). `isInteractive` is off, because interactive glass is press motion we would then have to switch off under Reduce Motion.
2. **A frost layer: the theme's `surface` colour at 80% alpha in light mode and 90% in dark.**
3. Labels and icons in full-strength text colour, with the selected pill, as UX designed.

Whatever the glass renders, it is some colour. UX's `glass.py` swept every colour in a 16-step sRGB cube beneath the tint at those opacities, and found every label passing (`round-2/directions.md` §4.2, appendix B). **So the floor holds whatever the material does, and whatever Apple changes about it in a later iOS** [I, from UX's model and the layer order]. It still needs one on-device measurement (§5), because the model is a model.

**The honest consequence** [J]: at 80–90% frost, the glass contributes a faint living tint and Apple's lit edge. Content beneath does not read. **It will look close to the opaque pill.** UX said the same (*"It is not see-through glass"*, §4.2). The vertical-space gain, the reason for D48, comes from the floating geometry, and every theme gets that anyway. **Real glass buys a finish, not function**, for about 22 h once and 1–2 h a release (§5, §6). That is a legitimate choice for the CEO to have made. I record the price, and I am not re-opening D48.

**Two known issues to design around:**

- *"Setting `opacity` to `0` on `GlassView` or any of its parent views causes the glass effect to not render at all"*. Fades must use the component's own `animate` props [E, [Expo, GlassEffect](https://docs.expo.dev/versions/latest/sdk/glass-effect/)]. This matters for the 200 ms theme cross-fade (`finalise.md` §3).
- A report of glass views flickering on screen transitions, on SDK 54 and iOS 26.1 with native tabs. It was **closed as "incomplete issue: missing or invalid repro" and "outdated"**, with no fix documented [E, [expo/expo #41025](https://github.com/expo/expo/issues/41025), **single source, unconfirmed**]. It goes on the device checklist, not the risk register.

**Performance** on the oldest iOS 26 phones (iPhone SE 2nd generation and iPhone 11, per a secondary compatibility list [E, [itechguides](https://www.itechguides.com/ios-26-supported-devices-full-list-of-compatible-iphones/), **secondary, single source**; Apple's own page was not retrieved]) is **not known** and must be measured on a device, as UX asked (§4.5 item 3). One small glass view over a scrolling list is Apple's intended use, and I expect it to be fine [J, low-to-medium confidence].

### 1.4 Reduce Transparency and Increase Contrast

| Setting | iOS: can React Native read it? | Live change event? | What we do |
|---|---|---|---|
| **Reduce Transparency** | Yes: `AccessibilityInfo.isReduceTransparencyEnabled()` | **Yes:** `reduceTransparencyChanged` | Swap the glass for an opaque `surface` bar. Expo's page confirms the need: the glass *"may"* be limited by accessibility settings, and points to this very API [E, [Expo, GlassEffect](https://docs.expo.dev/versions/latest/sdk/glass-effect/)] |
| **Increase Contrast** | Yes: `isDarkerSystemColorsEnabled()` | **No event listed** | (a) Colours can switch live without code: `DynamicColorIOS` accepts `highContrastLight` and `highContrastDark`, and *"the system will choose which of the colors to display depending on the current system appearance and accessibility settings"* [E, [RN, DynamicColorIOS](https://reactnative.dev/docs/dynamiccolorios)]. (b) Switching the **material** from glass to opaque needs a change signal. That means a small native listener, or re-querying when the app returns to the foreground. **I recommend the listener: about 3–6 h** [J] |
| **Android high-contrast text** | `isHighTextContrastEnabled()` (Android only) | Yes. The Android module registers a `ContentObserver` and emits `highTextContrastDidChange` [E, [RN source, AccessibilityInfoModule.kt](https://raw.githubusercontent.com/facebook/react-native/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.kt)] | The Android bar is always opaque, so this only selects the higher-contrast token set. **Whether this is the right Android counterpart to Increase Contrast is UX's call** (A11Y-10 names Increase Contrast on both platforms) |

Every method above is listed at [E, [React Native, AccessibilityInfo (0.87)](https://reactnative.dev/docs/accessibilityinfo)].

**The user's Light or Dark override** (Settings → Appearance) works with all of this. `Appearance.setColorScheme('light' | 'dark' | 'auto')` *"Forces the application to always adopt a light or dark interface style… an app-level override"* [E, [RN, Appearance](https://reactnative.dev/docs/appearance)]. That is what makes `DynamicColorIOS` and `GlassView` (which also takes `colorScheme`) follow the user's choice rather than the phone's [I].

**One inconsistency in the sources, recorded rather than smoothed over:** the Expo versions table lists **SDK 57.0.0** (React Native 0.86) as the latest. The native-tabs and fonts pages describe **SDK 58** features, and the React Native pages are for **0.87** [E, [Expo, versions](https://docs.expo.dev/versions/latest/)]. Nothing in this note depends on SDK 58, except variable fonts (§4.2), and that has a fallback.

---

## 2. User-chosen app icons at launch (D51)

### 2.1 Verdict: feasible on both platforms, at launch

**This does not go back to the CEO as infeasible.** It goes back only as a price (§5) and a list of behaviours he should expect (§2.4).

### 2.2 iOS

- **The API.** `setAlternateIconName(_:completionHandler:)` is available from iOS 10.3. The app *"can change the icon only if the value of the `supportsAlternateIcons` property is `true`"*. Alternates are named in the *"Alternate App Icon Sets"* build setting, which generates `CFBundleAlternateIcons` [E, [Apple, setAlternateIconName](https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setalternateiconname(_:completionhandler:).json)].
- **The variants.** *"Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants… all alternate and variant icons are subject to app review"*. The appearances are **default, dark, clear light, clear dark, tinted light, tinted dark**. Icon Composer lets you *"annotate for default, dark, and mono appearance variants"* [E, [Apple HIG, App icons](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json)]. **The practical route on iOS 26 is one Icon Composer `.icon` file per mark**, which carries the appearances in one file [I].
- **Icon Composer files as alternates.** In June 2025 a developer reported that `.icon` files could not be set as alternates. A reply of July 2025 lists *"Unable to set Icon Composer icon as alternate iOS icon"* among issues **fixed in Xcode 26 beta 3** [E, [Apple Developer Forums 788466](https://developer.apple.com/forums/thread/788466), **single source**; the replier's Apple affiliation is as reported by the retrieval, not independently confirmed]. **This must be proved in the first build, not assumed.** The fallback is PNG sets per appearance in the asset catalog.
- **Expo.** Expo's `ios.icon` accepts an Icon Composer `.icon` directory *"in SDK 54 and later"*, **for the primary icon only**. The page does not mention alternates [E, [Expo, Splash screen and app icon](https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon.md), modified 2026-06-26]. The main community package, `expo-alternate-app-icons` (MIT, SDK 51+), takes **light, dark and tinted PNGs** per alternate [E, [pchalupa/expo-alternate-app-icons](https://github.com/pchalupa/expo-alternate-app-icons)]. **It has open, unresolved requests for Icon Composer support:** #187 (August 2025), #274 (June 2026) and #277 (July 2026) [E, [its issues](https://github.com/pchalupa/expo-alternate-app-icons/issues)]. **PNGs with no clear variant may not meet the HIG's "require their own dark, clear, and tinted variants"** [I].
- **So the plan:** **our own small config plugin** that copies the three `.icon` files into the iOS project and sets the alternate-icon build settings, plus a Swift function of a few lines in our existing native module that calls `setAlternateIconName`. This is simpler than patching a third-party library, and it adds no dependency for the CSO to approve [J].
- **The alert cannot be suppressed.** An Apple forum reply of January 2023: *"`setAlternateIconName` always presents an alert after the change, so you can't quietly change the icon without the user noticing"* [E, [Apple Developer Forums 723928](https://developer.apple.com/forums/thread/723928)]. A 2025 article on an Expo icon package says the same (*"There's no way around this"*) [E, [Variant Systems](https://variantsystems.io/blog/dynamic-app-icons-expo/)]. **For D51 this is harmless:** the change is always one the user just asked for, in Settings. It is also a further reason for UX's rule that the icon never follows the theme automatically (`finalise.md` §4, option 3).
- **The guideline has moved.** The same 2023 reply cited App Review Guideline 4.6's bar on *"dynamic, automatic, or serial changes"* and its requirement that *"the app includes settings to revert to the original icon"*. **Today 4.6 reads "Intentionally omitted"** [E, [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)]. D51's design (user-chosen, in Settings, revertible, never automatic) meets the old text anyway, so nothing turns on it. The HIG's *"Avoid creating one someone might mistake for another app"* still binds [E, HIG above]. UX already rules out a disguised icon (`finalise.md` §4).

### 2.3 Android

- **The mechanism.** Android has no alternate-icon API. The established route declares **one `activity-alias` per icon** in the manifest, each with its own icon, and enables one while disabling the others through `PackageManager.setComponentEnabledSetting`. `expo-alternate-app-icons` does exactly this, with *"foreground image path and background color"* for adaptive icons [E, [its README](https://github.com/pchalupa/expo-alternate-app-icons)].
- **The themed monochrome layer.** PLAT-7(c) requires one (retrieved by the PM/BA from [Android adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive), 2026-09-22). **The retrieved README mentions no monochrome option** [E, same]. Our own config plugin (§2.2) writes each alias's adaptive-icon XML with foreground, background and monochrome layers. The layer format is standard Android [K, high confidence].
- **`DONT_KILL_APP`.** Changing enabled components can restart the app. The flag *"stops the system from restarting the app right away"* [E, [abizareyhan.com, 2021](https://blog.abizareyhan.com/dynamic-app-icon-on-android/), **secondary**. Android's own reference page did not render its method text for the retrieval tool].

### 2.4 The pitfalls, named

| # | Pitfall | Platform | Evidence | What we do |
|---|---|---|---|---|
| P1 | **The system alert on every change**, which cannot be suppressed | iOS | [E, forum 723928] | Nothing: it confirms the user's own action. The copy on our picker should not duplicate it [J] |
| P2 | **From iOS 26.1, the icon change makes the app resign active** before the alert appears. The alert moved to a system overlay | iOS 26.1+ | [E, [Apple Developer Forums 822359](https://developer.apple.com/forums/thread/822359), April–May 2026, **single source**. The same thread reports a localisation bug in the alert, fixed by iOS 26.4.1] | **This matters for HEAD-12:** if the app-switcher privacy cover is triggered on *resign active*, it will flash over the Settings screen when the user changes the icon. Test it. If it happens, trigger the cover on *entered background* instead, provided the CSO and UX accept that |
| P3 | **Launchers are slow to refresh the icon**, especially OEM launchers, and *"on Samsung phones, the icon might update slower than on Google Pixel"* | Android | [E, [abizareyhan.com](https://blog.abizareyhan.com/dynamic-app-icon-on-android/); [dev.to, 2025](https://dev.to/anandankur16/let-users-change-your-app-icon-a-guide-to-dynamic-icons-on-android-with-activity-alias-3okp); both secondary] | Say so in one plain line under the picker, and test on a Pixel and a Samsung (§5) |
| P4 | **Pinned home-screen shortcuts can be removed** when the launcher component changes (*"the shortcut is deleted from the home screen"*) | Android | [E, [GeeksforGeeks](https://www.geeksforgeeks.org/activity-aliases-in-android-to-preserve-launchers/), secondary]. A search summary said this affects **only API 28 and below**. **I could not retrieve a page that says so, so the version limit is unverified** | Test on the minimum Android version once SPK-03 sets it. If the icon is lost there, the picker says so before the user switches |
| P5 | **Anything that names the launcher activity** (notification taps, deep links, the Expo dev client's launch command) can break when that activity's alias is disabled | Android | [K, medium confidence]. The library has an open issue *"[Android] Expo deep link not working"* (#260, March 2026) [E, issues list; cause not read] | Route every intent to the real activity, never to an alias. Test notification taps (NOT-n) with each icon enabled |
| P6 | **The icon resets on reinstall**, and the enabled alias is package state, not app data. So **a restore from export (DATA-3) brings back the setting but not the icon** | Android; the restore half is both | [E for reinstall, abizareyhan.com, secondary]; the restore half is [I] | On first launch after a restore, re-apply the saved icon. On iOS this raises the alert once. That is acceptable, and the user expects it |
| P7 | **Every alternate is reviewed by Apple**, with every variant | iOS | [E, HIG] | Submit the alternates in the first TestFlight build (PLAT-7(d)'s *"before the release-candidate build"* applies) |

**Also binding, by analogy with THEME-5 and THEME-6** [J]: the icon choice persists, round-trips through export, is never promoted, and is available in every entitlement state. The PM/BA writes it as a requirement through a §24 row.

---

## 3. Mono's typed headline (D45) and Warm's Rotate (D49)

### 3.1 Detecting the settings live

| What | iOS | Android | Evidence |
|---|---|---|---|
| **Screen reader on** (HEAD-11 fallback) | `isScreenReaderEnabled()` and a `screenReaderChanged` event | The same, for both platforms | [E, [RN, AccessibilityInfo](https://reactnative.dev/docs/accessibilityinfo)] |
| **Reduce Motion** (HEAD-10) | `isReduceMotionEnabled()` and a `reduceMotionChanged` event. Also `prefersCrossFadeTransitions()` for the cross-fade preference | **Defective for our purpose.** See below | [E, same page] |
| **Accessibility text sizes** (HEAD-11) | The font scale is readable | The same | [K, high confidence]. Covered by A11Y-4 work already in the estimate |

**The Android defect UX found is real, and its cause is now confirmed in the code.** React Native's Android module computes reduce-motion from **`Settings.Global.TRANSITION_ANIMATION_SCALE`** only, and watches that one key with a `ContentObserver` [E, [RN source, AccessibilityInfoModule.kt](https://raw.githubusercontent.com/facebook/react-native/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.kt)]. The docs describe the event the same way: true when reduce motion is on *"(or when "Transition Animation Scale" in "Developer options" is "Animation off")"* [E, RN AccessibilityInfo]. **Android's accessibility switch, *Remove animations*, sets the animator duration scale to 0** (*"The animation duration scale is `0f` if reduced motion-setting is enabled"*, read from `Settings.Global.ANIMATOR_DURATION_SCALE`) [E, [Eevis Panula, 2022](https://eevis.codes/blog/2022-12-12/android-animations-and-reduced-motion/), secondary but specialist]. The original report found *Remove animations* missed on Android 10 and 11, while the developer-options animator scale was detected. The issue was closed with no fix shown [E, [RN #31221](https://github.com/facebook/react-native/issues/31221)].

**Whether *Remove animations* also zeroes the transition scale on some devices is not established.** If it does, React Native would catch it, but only there. **The remedy is cheap either way:** a small Kotlin function in our native module that reads `ANIMATOR_DURATION_SCALE`, registers a `ContentObserver` on it, and emits an event. The final result is reduce-motion **or** animator-scale-zero. **About 4–8 h** [J]. **It is owed by HEAD-10(b) regardless of this design**, so it is sized under SPK-08, not in §5. HEAD-10(b)'s physical-device test stays the arbiter.

### 3.2 Read once on focus, never announced (HEAD-16, D45's clarified condition)

**Feasible with standard props. There is no platform obstacle** [I, from the API surface above]:

- The headline container is **one accessibility element** whose label is **always the complete sentence**, fixed before the typing starts. The partly typed text is a visual child hidden from assistive technology.
- **No live region.** The Android live-region property stays at its default of none, and **`announceForAccessibility` is never called.** HEAD-16(b) asserts that no announcement fires [K for the Android prop default, high confidence].
- **In practice the typing never runs under a screen reader anyway.** HEAD-11 renders the full, still sentence while VoiceOver or TalkBack is on. So the "read once" guarantee rests on the fixed label, and the animation cannot interfere with it [I].
- **One edge to test** [J]: if a screen reader is switched on while the headline is mid-type, the `screenReaderChanged` event must snap the sentence to full before focus reaches it. That is a HEAD-11 device test.

### 3.3 Pausing the blink, and the rest of D45's conditions

- **The blink is a timed loop the app owns**, 0.5 s on and 0.5 s off per UX (`finalise.md` §6.2), so stopping it is trivial. The pause control stops it and the typing. The loop also stops when the app leaves the foreground, and when the headline scrolls out of view, which needs a visibility check on the home list [J].
- **Why the pause control is not optional:** SC 2.2.2 applies to *"any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content"*. W3C's escape is technique G11, *"Creating content that blinks for less than 5 seconds"* [E, [W3C, Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)]. The cursor keeps blinking at rest (D45), so it lasts over five seconds, and the pause control is what makes it conform. UX said the same.
- **A layout trap worth naming** [J]: typing a sentence letter by letter makes the text **reflow and the card change height** as words wrap, which would push the timeline down on every character. **Fix: lay out the whole sentence from the start, with the untyped part transparent**, so the box never moves. The same trick keeps the cursor after the last visible character. This matters at large Dynamic Type sizes, although HEAD-11 falls back to the still Line at accessibility sizes.
- **No sound, no speed variation, no "new" marker:** these are design constraints with no platform dimension.

### 3.4 Rotate, and a possible saving in Retro

**Rotate** shows one whole sentence for about 6 s, cross-fades to the next, runs round once, then rests on the first (D49). It is a small state machine plus an opacity cross-fade, **simpler than a crawl**: no text-width measurement, no scroll timing, no edge fades. The typed headline is Mono's styling of the same cycle (`finalise.md` §6.2). **Build the cycle once** (fact index, hold timer, one pass, pause persistence, fallbacks) and give it two renderers [J].

**The crawl survives only in Retro** (`themes.md` §5, the portal ticker *"text moving right to left"*). After D49 and D45, the crawl, the most expensive single piece of HEAD work (`requirements.md` §20.2, *"the most expensive piece"*), serves one of three themes. **Offered, not recommended over UX's judgment:** styling Retro's ticker as Rotate inside the navy-and-yellow portal strip would remove the crawl from the codebase. **By my rough judgment that saves 15–30 h once and a motion path in every release** [J]. Whether a portal ticker that does not scroll still looks like the period is UX's question and the CEO's taste. §6 item 2.

---

## 4. The theme system, the fonts, and the verification burden

### 4.1 Token theming: feasible, and the architecture is fixed here

**The standard I will set for the Engineers** [J]. It is UX's rule (`themes.md` §3.1) turned into mechanism:

1. **One token schema, one typed object per theme.** Colour, type (family, weight, tracking, case), shape (radius, rule weight, `edge_style: flat | bevel`, `title_fill: solid | gradient`), texture, motion (easing, duration within the 100–250 ms budget) and the bar material (`glass | opaque | bevel`). TypeScript makes a missing token in any theme a **compile error**. This is the cheapest guard against a theme nobody finished.
2. **Each colour token carries four values**: light, dark, higher-contrast light, higher-contrast dark. On iOS they become `DynamicColorIOS` objects, so Increase Contrast and light or dark switch without code (§1.4). On Android the provider selects the set from the colour scheme and `isHighTextContrastEnabled()`.
3. **Components read tokens through one theme context, and never branch on a theme name.** This is enforced by a lint rule banning theme-name literals outside the theme files, so UX's *"no 'if retro then…'"* is a failing build, not a hope.
4. **Light or dark is `Appearance.setColorScheme`** (§1.4). The theme and the mode persist and round-trip through export (THEME-5).
5. **Headline appearances are components with per-theme renderers** (Line, Card, the moving appearance). That is the one declared exception to "no branching": the moving appearance has three renderers (Rotate, typed, crawl) over one cycle (§3.4).

**Nothing here is novel.** React Native's colour APIs, the context pattern and TypeScript do all of it with **no new runtime dependency**. Retro's gradients need one: a gradient view such as `expo-linear-gradient` [K, high confidence that it exists; not retrieved]. **The CSO approves it as a new dependency** (D40's rule).

### 4.2 Fonts: size measured, bundling feasible

**Families required** (`round-2/directions.md` §1–§2, `themes.md` §8.2): Newsreader and Inter (Warm and Mono), IBM Plex Mono (Mono's metadata and typed headline), and Gelasio, DejaVu Sans and Silkscreen (Retro).

**Sizes, measured on 2026-09-27** from the Google Fonts repository through the GitHub contents API, and for DejaVu from jsDelivr's metadata for the `dejavu-fonts-ttf@2.37.3` npm package [E, measured. Sources: [google/fonts `ofl/`](https://github.com/google/fonts/tree/main/ofl), [jsDelivr dejavu-fonts-ttf](https://www.jsdelivr.com/package/npm/dejavu-fonts-ttf)]:

| File | Bytes | Used by |
|---|---:|---|
| `Newsreader[opsz,wght].ttf` (variable) | 451,664 | Warm, Mono |
| `Newsreader-Italic[opsz,wght].ttf` (only if italics are used) | 495,684 | (Warm, Mono) |
| `Inter[opsz,wght].ttf` (variable) | 876,576 | Warm, Mono |
| `IBMPlexMono-Regular.ttf` + `-Medium.ttf` | 135,580 + 136,704 | Mono |
| `Gelasio[wght].ttf` (variable) | 168,556 | Retro |
| `DejaVuSans.ttf` + `DejaVuSans-Bold.ttf` | 757,076 + 705,684 | Retro |
| `Silkscreen-Regular.ttf` | 32,220 | Retro |
| **Total, no italics, unsubsetted** | **3,264,060 (≈ 3.3 MB)** | |
| Total with Newsreader Italic | 3,759,744 (≈ 3.8 MB) | |

By theme: **Warm 1.33 MB, Mono +0.27 MB, Retro 1.66 MB. Retro is the heaviest theme to bundle.** Against the 21.3 MB venue index (`feasibility-note.md` §0), fonts add about 15% unsubsetted. UX's *"0.5–1.5 MB"* [K, low confidence] (`themes.md` §7) was **low for the unsubsetted set**, and is reachable only with subsetting.

- **Subsetting is modification under the OFL.** *"Removing any parts of the font… including unused glyphs… is considered modification"* (FAQ 2.6). Modified versions may be bundled in commercial software (FAQ 1.4) but may not use a Reserved Font Name [E, [OFL FAQ](https://openfontlicense.org/ofl-faq/)]. **IBM Plex Mono reserves the name:** *"Copyright © 2017 IBM Corp. with Reserved Font Name "Plex""* [E, [Plex Mono OFL.txt](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/OFL.txt)]. **So Plex Mono ships unmodified.** At 0.27 MB it is not worth subsetting and renaming. Newsreader, Inter, Gelasio and Silkscreen carry no RFN, and DejaVu's licence restricts only the words "Bitstream" and "Vera". Both are UX's readings (`themes.md` §7, round 1 E2), **not re-retrieved by me**. The CGO confirms them before any subset ships.
- **Where subsetting pays** [K, medium confidence]: Inter and DejaVu Sans cover many scripts. A Latin subset of those three files should shrink them several-fold. Whether Haunts needs more than Latin is a venue-name question: UK venue names include accented and non-Latin names. **The subset must be tested against the whole venue index's character set before it ships**, or names render as missing-glyph boxes [J].
- **Variable fonts depend on the SDK.** Expo: *"Android and iOS support variable fonts in SDK 58 and later. On earlier versions, use static font files."* Android reads the `wght` axis on **Android 10+**, and iOS picks *"the named instance whose weight is closest"* [E, [Expo, Fonts](https://docs.expo.dev/develop/user-interface/fonts/), modified 2026-09-23]. On SDK 57 we ship **static instances**, one file per weight. That multiplies file count, and the size per weight is not measured [K]. **Input to SPK-03:** an Android minimum below 10 would force static fonts on those devices.
- **Embed with the `expo-font` config plugin**, so fonts are *"available immediately when the app starts"* with no loading flash [E, same page]. Fonts scale with the system text size like any text [K, high confidence]. Retro's rule, that Silkscreen swaps to DejaVu Sans Bold above a size constant and under Bold Text, reads `isBoldTextEnabled()` and its `boldTextChanged` event on iOS [E, RN AccessibilityInfo].
- **Notices:** each family's copyright line and licence text go on the Licences screen (THEME-9). That is minutes of work.

### 4.3 The verification burden per theme

**The matrix** [I, arithmetic]: 3 themes × light and dark × standard and higher contrast × 2 platforms = **24 visual configurations per screen, against 8 for one theme**. On top of that: glass, Reduce Transparency and Increase Contrast states of the bar in Warm and Mono on iOS; three moving-headline renderers, each with its reduce-motion, screen-reader and large-text fallbacks; and three icons.

**What makes it affordable** is automating everything that does not need eyes [J]:

| Check | How | Marginal cost per extra theme |
|---|---|---|
| Every token pair's contrast, every theme and mode (THEME-2(a)) | Port `contrast.py`'s check to run on the TypeScript tokens in CI | ≈ 0 after the port |
| Identical screen-reader tree and element order across themes (THEME-1(a), (b)) | An automated test renders each screen per theme and diffs the accessibility tree and layout | ≈ 0 after the harness |
| One string table (THEME-1(c)) | Already true by construction: themes hold no strings. QA's MEM-1 search covers it | 0 |
| **What still needs a person** | Visual inspection per theme × mode × platform of the key screens; Retro against `themes.md` §8.3's out-list (THEME-8); the glass device check; the motion renderers on a device | **This is the recurring cost in §6** |

This gives **roughly 20–35% more manual UI verification per extra theme** [J]. That is close to UX's 15–25% (`themes.md` §7), a little higher because three motion renderers and the glass states are verified per theme too. **The saving from automation is real only if the harness is built in M1, before screens multiply.** That is why it is a line in §5 and not a later nicety.

---

## 5. Sizing: one-off build hours [J]

**Every figure in this section is [J], outside the 2,090-hour estimate, and additional to it.** It is kept apart from the 2,090 here, and the CFO should keep it apart on the cost sheet, as scope added after the estimate (`backlog-plan.md` "Estimate basis": *Added after the estimate*). **Unit: focused solo hours**, including design coverage and first verification wherever those are part of delivering the item. **Assumption about the baseline:** the 2,090 h builds every screen once, in one visual style. I take that style to be Mono's base, because Mono is the default (D46). So Mono's line below is only what Mono adds beyond a plain, well-built UI.

| # | Item | Low | Point | High | UX's estimate (converted at 7.5 h/day) | What drives my figure |
|---|---|---:|---:|---:|---|---|
| 1 | **Theme machinery**: token schema, four-value colours, `DynamicColorIOS` mapping, theme context, lint rule, runtime switch with glass-safe cross-fade, light/dark override, shape and texture tokens, persistence and export round-trip | 32 | 44 | 60 | 5–8 d = 38–60 h (with #3) | Close to UX's figure |
| 2 | **Appearance screen**: three live-preview cards as one radio group, one column at large sizes, light/dark control | 14 | 20 | 28 | 2–3 d = 15–22 h | As UX |
| 3 | **Theme test harness**: contrast CI on tokens, accessibility-tree and layout diff across themes | 12 | 18 | 26 | (in #1) | Built in M1, or §4.3's saving does not exist |
| 4 | **Fonts**: embedding six families, static-or-variable decision, Latin subsetting checked against the venue index's character set, Plex unmodified, Bold Text and pixel-face swap, Licences screen | 10 | 15 | 22 | "minutes" (notices only) | UX costed notices, not bundling |
| 5 | **Mono** beyond the base: Plex metadata, the `//` and `>` marks as drawn glyphs hidden from assistive technology, orange focus ring, token values in four sets, first verification | 10 | 16 | 24 | 2–3 d = 15–22 h (as an extra theme) | Now the base, so only its extras count |
| 6 | **Warm**: token values in four sets, rounded card and pill shapes, the apricot headline card, **design coverage of every screen**, first verification | 20 | 30 | 42 | 2–3 d = 15–22 h | Design coverage of every screen, which UX's own caveat notes is not yet done |
| 7 | **Retro**: tokens, gradient dependency, bevels, pixel-face rules, Retro styling of Line, Card and ticker, bevelled bar, design coverage of every screen, first verification against the §8.3 out-list (THEME-8) | 40 | 56 | 76 | 4–6 d + 1–2 d = 37–60 h | As UX, plus the out-list inspection |
| 8 | **Floating bar**, custom, every theme and platform: tab roles and selected state, 44 pt targets, bottom inset and focus-not-obscured (SC 2.4.11), Android opaque pill, material from tokens | 16 | 24 | 34 | 1–2 d = 7.5–15 h | **A custom bar must rebuild the native bar's accessibility** (§1.2) |
| 9 | **Real glass on iOS**: `GlassView` with the frost layer and hairline, Reduce Transparency switch, Increase Contrast native listener, **one on-device worst-case contrast measurement**, performance on the oldest iOS 26 phone, transition-flicker check | 14 | 22 | 32 | 2–4 d = 15–30 h | As UX |
| 10 | **Rotate** (Warm): the shared cycle plus the cross-fade renderer. **Net of the HEAD work already owed** | 8 | 12 | 18 | 1–2 d = 7.5–15 h | As UX |
| 11 | **Typed headline** (Mono): typing renderer, blink loop and stops, transparent-remainder layout, full label, device check of both reduce-motion paths | 12 | 18 | 26 | 1–2 d = 7.5–15 h | The reflow fix and the stop conditions (§3.3) |
| 12 | **Template additions** (D50): deterministic phrasing selection by date (once), plus **UX's five drafted templates** with their data queries, a §24 row each, UX review and QA string search | 30 | 45 | 65 | ≈ 0.5 d each = ≈ 19 h for five | UX sized the writing. The **queries** are engineering: *on this day* is cheap, a *pairing as a ritual* needs sequence detection with a threshold, and *Neighbourhood* may need data we lack (§7) |
| 13 | **Contour texture** (Warm only): one open-line asset per mode in two header bands, never behind text | 4 | 6 | 10 | 1 d = 7.5 h | As UX |
| 14 | **App-icon setting**: our config plugin (iOS `.icon` alternates, Android aliases with monochrome layers), the native call on both platforms, a picker screen, re-apply after restore, intent routing, device tests on iOS plus a Pixel and a Samsung | 28 | 40 | 56 | 2–4 d = 15–30 h | The pitfalls in §2.4 are where the hours go |
| 15 | **Alternate icon artwork**: two extra marks as Icon Composer files (default, dark, mono) plus Android adaptive layers. *"A human or tooling task"* (PLAT-7), but labour all the same | 6 | 10 | 16 | "8 extra renders" | Constitution Definitions: labour is *"valued at a published market benchmark whether or not it is actually paid"* |
| | **Total** | **256** | **376** | **535** | ≈ 200–320 h (sum of UX's rows, counting Warm and Mono each as an extra theme) | |

**Against the 2,090 h: +12% (low), +18% (point), +26% (high).** Summing every low and every high overstates the spread, since not everything lands at an extreme at once. I show the plain sums so a reader can re-derive them.

**What the total excludes, so nothing is counted twice:**
- **HEAD-1 to HEAD-18 themselves**: the Line, the Card, the crawl, the pause control, the fallbacks, the Android remove-animations check (§3.1). They are **owed to SPK-08** and unsized there. UX's 4–6 d stands until then.
- The heatmap, photos and LOOK-8/9, also SPK-08.
- **The primary app icon** (PLAT-7). It is in the launch scope already; only the alternates are here.

**Where the hours are, for a reader who wants to trim** [J; a list, not a recommendation to cut anything the CEO decided]: Retro (≈ 56 h plus its share of §6), the icon setting with its art (≈ 50 h), templates (≈ 45 h, scalable by writing fewer), and real glass (≈ 22 h plus 1–2 h each release, for the least visible gain, §1.3).

---

## 6. Ongoing maintenance [J]

**Per release**, in addition to today's A11Y-10 pass:

| Item | Hours per release |
|---|---:|
| Visual pass of the key screens in the two extra themes × two modes × two platforms, including Retro's out-list | 3–6 |
| Glass device check: default, Reduce Transparency, Increase Contrast, worst content, oldest phone | 1–2 |
| Motion renderers on a device: Rotate, typed, crawl, each with its reduce-motion fallback (the Android physical-device test per HEAD-10(b)) | 0.5–1.5 |
| App-icon switch: iOS alert and resign-active behaviour, Android on two launchers | 0.5–1 |
| **Total per release** | **5–10.5** |

**Per year, not per release:** the annual iOS and Android releases and each Expo SDK upgrade touch exactly the parts this design leans on: the glass material, Icon Composer and alternate icons, launcher behaviour, and font loading. **Allow 10–24 h a year** [J].

**Per new screen after launch:** it is designed and checked in three themes and two modes. **Add roughly 25–40% to that screen's UI cost** [J]. This cannot be annualised without a roadmap.

**Annualised:** at **6–10 releases a year** [J, an assumption the CFO should replace with the real cadence], that is **about 40–130 h/yr, point ≈ 76 h/yr**. **Against the 360 h/yr fixed maintenance (`subscription-sizing-note.md` §9.2) that is +11% to +36%.** This is the number UX called *"the cost that matters"* (`themes.md` §7), and I agree. **The CFO must cost it (SPK-09).**

---

## 7. Flags to other seats, and one disagreement

Each item is a **flag, not a block**. None fails a build-commencement checklist item (my blocking ground, `roles/cto.md`).

1. **To UX: Mono's "margin column of times on the timeline"** (`round-2/directions.md` §2) sits awkwardly with THEME-1's rule that *"every screen's element order and position is identical across themes"* (`themes.md` §9, THEME-1(b)). If Warm and Retro have no margin column, it is a layout difference. **Either every theme gets the column, styled differently, or Mono's times stay inline, in monospace.** This is UX's rule to interpret. I only noticed the collision.
2. **To UX and the CEO: Retro's crawl** is now the only crawl (§3.4). Rotating Retro would save about 15–30 h and a motion path per release [J]. That is taste, not engineering.
3. **To the PM/BA and UX: the *Neighbourhood* template** (*"Most of the cafés in your journal are around Mill Road"*, `round-2/directions.md` §6) needs a street or area name per venue. **I have not established that the venue index carries one**, and I did not re-read the index schema for this note [I]. The optional basemap pack carries place names (LOOK-2), but it is optional, so a template cannot depend on it. **Don't write it into requirements until the index's fields are confirmed.** If they are absent, it is out, or it costs index work that §5 does not include.
4. **To the CSO and UX: the icon change and HEAD-12** (§2.4 P2). On iOS 26.1+ the app resigns active when the icon changes. If the privacy cover keys on resign-active, it will flash. Moving it to did-enter-background is a security-relevant change, so it is the CSO's call.
5. **To the CGO:** the RFN and DejaVu readings behind subsetting (§4.2) are UX's, not re-retrieved by me. Confirm before a subset ships (Constitution 6.1: *"third-party licence terms whose interpretation determines a product's architecture or cost"* receive qualified human review).
6. **One disagreement, stated once: with UX's hope in `round-2/directions.md` §4.5 item 1 that the system tab bar would carry the glass.** It cannot, on the evidence in §1.2. I don't think this changes UX's design at all, since the custom bar was always what Retro and Android needed. It does mean **the system's automatic handling of Reduce Transparency and Increase Contrast is not ours for free.** We detect both ourselves, and the hours in §5 #9 include that.

---

## 8. Negative findings, with what would overturn them and where I looked

The charter asks, *"have I established that nobody is doing it — or only that the platform does not hand it to me?"* Where the platform does not hand it over, §1.3 and §2.2 show it is still being done.

| Finding | What would overturn it | Where I looked |
|---|---|---|
| **The system tab bar (Expo native tabs) cannot meet D48** | An Expo or Apple API that sets the iOS 26 tab bar's background opacity, or allows a custom bar view, in a version we can ship | Expo native-tabs docs (current); `expo-glass-effect` docs; `UIGlassEffect` reference |
| **React Native gives no live event for Increase Contrast on iOS** | A later RN release adding a `darkerSystemColorsChanged` event, or `DynamicColorIOS` proving enough on a device, because the material switch could then key off a colour change | RN AccessibilityInfo (0.87) event table; RN DynamicColorIOS |
| **React Native's reduce-motion check misses Android's *Remove animations*** | An on-device test in which *Remove animations* also zeroes `TRANSITION_ANIMATION_SCALE` on every device in the matrix, or an RN change that reads the animator scale | RN Android source on `main`; RN docs; RN #31221; one specialist article |
| **The Expo alternate-icon library does not support Icon Composer alternates** | A release closing #187, #274 or #277 | Its README and open issues, 2026-09-27 |
| **Real glass at 80–90% frost looks close to opaque** | An on-device look at the finished bar (a judgment, not a measurement) | UX's `glass.py` results; my reading of the layer order |
| **Android pinned shortcuts are lost only on API 28 and below** is **unverified**, and I treat it as possible on any version | A retrieved Android source or documentation stating the limit | One secondary article (no version stated); a search summary I could not trace to a page |

---

## 9. Evidence register (all retrieved 2026-09-27 by this seat)

| # | Claim | Source |
|---|---|---|
| E1 | `expo-glass-effect`: native `UIVisualEffectView` glass, iOS and tvOS, fallback to `View`, props, availability checks, the opacity-0 issue, pointer to `isReduceTransparencyEnabled` | [Expo, GlassEffect](https://docs.expo.dev/versions/latest/sdk/glass-effect/) |
| E2 | Native tabs: the iOS 26 system glass bar ignores background props; no custom React bar; Material Tabs and a five-tab limit on Android; import paths by SDK | [Expo, Native tabs](https://docs.expo.dev/router/advanced/native-tabs/) |
| E3 | Latest Expo SDK 57.0.0, RN 0.86, minimums Android 7+ and iOS 16.4+ | [Expo, SDK versions](https://docs.expo.dev/versions/latest/) |
| E4 | `UIGlassEffect`, iOS 26.0+, `tintColor`, `isInteractive` | [Apple, UIGlassEffect](https://developer.apple.com/tutorials/data/documentation/uikit/uiglasseffect.json) |
| E5 | `isReduceTransparencyEnabled`, iOS 8.0+ | [Apple, isReduceTransparencyEnabled](https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/isreducetransparencyenabled.json) |
| E6 | RN AccessibilityInfo methods and events by platform, including the Android reduce-motion note | [React Native, AccessibilityInfo (0.87)](https://reactnative.dev/docs/accessibilityinfo) |
| E7 | RN Android reads `TRANSITION_ANIMATION_SCALE` for reduce motion; high-text-contrast observer and event | [RN source, AccessibilityInfoModule.kt](https://raw.githubusercontent.com/facebook/react-native/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/accessibilityinfo/AccessibilityInfoModule.kt) |
| E8 | *Remove animations* not detected by RN; closed with no fix shown | [RN issue #31221](https://github.com/facebook/react-native/issues/31221) |
| E9 | *Remove animations* zeroes `ANIMATOR_DURATION_SCALE` (secondary) | [Eevis Panula, 2022](https://eevis.codes/blog/2022-12-12/android-animations-and-reduced-motion/) |
| E10 | `DynamicColorIOS` with high-contrast variants | [RN, DynamicColorIOS](https://reactnative.dev/docs/dynamiccolorios) |
| E11 | `Appearance.setColorScheme` as an app-level override | [RN, Appearance](https://reactnative.dev/docs/appearance) |
| E12 | Glass flicker report, closed as incomplete (single source) | [expo/expo #41025](https://github.com/expo/expo/issues/41025) |
| E13 | A custom floating glass tab bar exists (single source) | [davidmokos/expo-glass-tabs](https://github.com/davidmokos/expo-glass-tabs) |
| E14 | Oldest iOS 26 iPhones (secondary, single source) | [itechguides](https://www.itechguides.com/ios-26-supported-devices-full-list-of-compatible-iphones/) |
| E15 | `setAlternateIconName`: availability, `supportsAlternateIcons`, build settings | [Apple, setAlternateIconName](https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setalternateiconname(_:completionhandler:).json) |
| E16 | Alternates need dark, clear and tinted variants and pass app review; the six appearances; Icon Composer | [Apple HIG, App icons](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json) |
| E17 | The alert cannot be suppressed; the old guideline 4.6 text (January 2023) | [Apple Developer Forums 723928](https://developer.apple.com/forums/thread/723928) |
| E18 | Guideline 4.6 now *"Intentionally omitted"* | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) |
| E19 | iOS 26.1+ resign-active on icon change; alert localisation bug fixed by 26.4.1 (single source) | [Apple Developer Forums 822359](https://developer.apple.com/forums/thread/822359) |
| E20 | `.icon` alternates fixed in Xcode 26 beta 3 (single source) | [Apple Developer Forums 788466](https://developer.apple.com/forums/thread/788466) |
| E21 | Expo `ios.icon` accepts `.icon` from SDK 54, primary icon; adaptive icon fields | [Expo, Splash screen and app icon](https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon.md) |
| E22 | `expo-alternate-app-icons`: features, activity-alias, PNG variants | [pchalupa/expo-alternate-app-icons](https://github.com/pchalupa/expo-alternate-app-icons) |
| E23 | Its open issues: Icon Composer #187, #274, #277; Android deep link #260 | [its issues](https://github.com/pchalupa/expo-alternate-app-icons/issues) |
| E24 | iOS alert; *"some launchers may take a moment to refresh"* (secondary) | [Variant Systems, 2025](https://variantsystems.io/blog/dynamic-app-icons-expo/) |
| E25 | `DONT_KILL_APP`; Samsung refresh lag; reset on reinstall (secondary) | [abizareyhan.com, 2021](https://blog.abizareyhan.com/dynamic-app-icon-on-android/) |
| E26 | Launcher icon caching by OEM launchers (secondary) | [dev.to, 2025](https://dev.to/anandankur16/let-users-change-your-app-icon-a-guide-to-dynamic-icons-on-android-with-activity-alias-3okp) |
| E27 | A shortcut deleted when the launcher activity changes (secondary) | [GeeksforGeeks](https://www.geeksforgeeks.org/activity-aliases-in-android-to-preserve-launchers/) |
| E28 | SC 2.2.2 normative text; G11 (blinks under 5 s) | [W3C, Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) |
| E29 | Font file sizes (measured) | [google/fonts `ofl/`](https://github.com/google/fonts/tree/main/ofl) (GitHub contents API); [jsDelivr, dejavu-fonts-ttf 2.37.3](https://www.jsdelivr.com/package/npm/dejavu-fonts-ttf) |
| E30 | Plex Mono's Reserved Font Name | [Plex Mono OFL.txt](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/OFL.txt) |
| E31 | OFL FAQ 1.4 (bundling) and 2.6 (subsetting is modification) | [OFL FAQ](https://openfontlicense.org/ofl-faq/) |
| E32 | Expo fonts: variable fonts from SDK 58, the Android 10+ `wght` axis, the config plugin | [Expo, Fonts](https://docs.expo.dev/develop/user-interface/fonts/) |

**Tried and failed:** the Android `PackageManager` and `ValueAnimator` reference pages returned navigation only, with no method text, so every `setComponentEnabledSetting` and animator-scale-listener detail rests on secondary sources or [K]. A Medium article on activity aliases returned HTTP 403.
**[K], not retrieved:** the Android live-region default; `expo-linear-gradient`; font scaling of custom fonts; the static font sizes per weight; Latin-subset sizes.

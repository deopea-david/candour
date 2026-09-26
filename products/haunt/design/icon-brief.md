# Haunts icon and mark: the PLAT-7 brief

**Seat:** UX / Design Lead · **Date:** 2026-09-26 · **Slug:** `haunt`
**Owed by:** **D11(d)** (CEO, 2026-09-21/22): *"The mark is owed and it is a launch dependency… **UX / Design Lead owns the brief and usage constraints**… Producing the artwork is a human or tooling task and is a spending decision for the CEO. The brief excludes ghost, eye and tracking imagery, for the reason D9 records."* Commissioned now by **D38** (2026-09-26).
**Requirement it serves:** **PLAT-7** (`requirements.md` §16, BLOCKING): *"the app icon at every size both stores and both OSes require, and the small in-image mark for the generated recap (LOOK-5) — one mark, used in both places."* Also **LOOK-5**, and the usage constraints the PM/BA wrote beneath PLAT-7, which this brief adopts and extends.
**Companion files:** [`brand-directions.md`](brand-directions.md) (which direction the mark belongs to), [`themes.md`](themes.md), [`concepts/`](concepts/) (twelve icon concepts, each at 1024 px and on a sheet at 60 and 29 px).
**Status:** prepares and flags; certifies nothing (Constitution 6.1). **This brief commissions no artwork and spends nothing.** Final artwork is a CEO spending decision (Constitution 5.4, *"spending real money"*), and D38(5): *"Artwork is concept work only. Paying for final artwork is a separate CEO decision."*
**Evidence:** tagged under `pipeline/evidence-standard.md`. My own retrievals are dated 2026-09-26. **Where PLAT-7 cites a retrieval by the PM/BA (2026-09-22) that I did not repeat, I say so.**

---

## 0. The brief in one screen

- **Make one mark** that works as the app icon on iOS and Android, as the Play Store icon, and as a small, hideable credit on the recap image.
- **It must work** at 1024 px and at 29 px, in full colour and in one colour, on light and dark wallpapers, and in greyscale.
- **It must not show** a ghost, an eye, a pin, a crosshair, a radar or concentric rings, footprints, a dotted route, or anything that reads as being followed or watched (D9, D11(d)); nor a glass, bottle, "cheers", confetti, trophy, star-as-reward or anything about nightlife (MEM-1); nor a headstone (my own draft's failure, §3).
- **It should not contain the name**, and nothing containing the name is finalised until PLAT-6's three checks pass.
- **Before anything is commissioned:** the CEO chooses a direction (`brand-directions.md`), and the CGO answers who would own the result (§6).
- **The first deliverable is a test submission to both stores, before the release-candidate build** (PLAT-7(d)).

---

## 1. What the mark is for

| Use | Where it appears | What it must do |
|---|---|---|
| **App icon** | iOS and Android home screens, app switcher, Settings, Spotlight or search, notifications | Be recognised at 29–60 px among dozens of other icons; survive the OS's mask, dark, tinted and themed modes |
| **Store icon** | App Store (from the build's 1024 px icon) and Google Play (a separate 512 px upload) | Represent the product honestly to someone who has never heard of it |
| **Recap credit** (LOOK-5) | The margin or footer of a recap image the user chooses to save | Be small, quiet, a credit and not a call to action, hideable with one control, legible on light and dark (LOOK-5(e)) |
| **In-app** | Launch screen, About screen | Same mark; nothing new |

**One mark, several renderings.** Full colour, one colour (Android's themed icon and iOS's tinted appearance), and a flat single-colour version for the recap credit. They must all be recognisably the same thing.

---

## 2. Store and platform requirements

### 2.1 Apple (iOS 26 and later, PLAT-8)

Retrieved from Apple's Human Interface Guidelines, *App icons* [E, [HIG App icons, JSON of the page](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json), retrieved 2026-09-26; the [HTML page](https://developer.apple.com/design/human-interface-guidelines/app-icons) does not render for the retrieval tool, as the PM/BA also found on 2026-09-22]:

- **Canvas: 1024 × 1024 px** for iOS.
- **Layers and Liquid Glass.** *"iOS, iPadOS, macOS, and watchOS app icons include a background layer and one or more foreground layers that coalesce to create dimensionality. These icons take on Liquid Glass attributes like specular highlights, refraction, and translucency."* Layers are assembled in **Icon Composer**, *"a design tool included with Xcode"*, in which you *"annotate for default, dark, and mono appearance variants"*.
- **Appearances:** *"people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance"*. The page lists **default, dark, clear light, clear dark, tinted light and tinted dark**. **The mark must be designed for all six**, which in practice means a clean silhouette that survives losing its colours.
- **Edges:** *"Prefer clearly defined edges in foreground layers… avoid soft and feathered edges."*
- **Simplicity:** *"express it in a simple, unique way with a minimal number of shapes."* Also *"avoid extremely thin line weights"*.
- **Text:** *"Include text only when it's essential to your experience or brand."* A mnemonic first letter is tolerated: *"displaying a mnemonic like the first letter of your app's name can help people recognize your app"*. This matters for the letter concepts (Almanac B, Ledger C).
- **No photos, no UI:** *"Prefer illustrations to photos and avoid replicating UI components."*
- **Upload validation.** PLAT-7(a) records that a build without a 1024 × 1024 icon is rejected with *"ITMS-90704: Missing App Icon"*, from a **secondary, single source** retrieved by the PM/BA on 2026-09-22 ([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/1336789/itms-90704-missing-app-icon-an-app-icon-measuring)). **Not re-retrieved by me.** The test submission in §4 settles it at first hand.

**How Icon Composer relates to the Expo build is a CTO question** (`requirements.md` §2: React Native with Expo). Whether a layered `.icon` file from Icon Composer flows through Expo's prebuild, or whether a flat 1024 px PNG is supplied and the system applies its own effects, I have not retrieved [K, low confidence]. **The brief asks for layered source either way (§4), so the answer changes the pipeline, not the artwork.**

### 2.2 Android launcher (adaptive and themed icons)

Retrieved from Android's developer documentation [E, [Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive), retrieved 2026-09-26; also cited by PLAT-7(c)]:

- **Three layers**, foreground, background and **monochrome**, each **108 × 108 dp**.
- **Safe zone:** *"The inner 66x66 dp of the icon appears within the masked viewport"*; the outer 18 dp on each side is reserved for masking and effects.
- **Logo size:** *"Use a logo that's at least 48x48 dp. It must not exceed 66x66 dp."*
- **Monochrome layer** for user theming: *"Provide a single layer for the monochrome version if you want to support user theming of app icons."* The PM/BA's constraint 3 makes this required for Haunts: the mark must work in one colour.
- **Clean edges:** layers *"must not have masks or background shadows around the outline of the icon"*.
- **Masks vary by manufacturer.** Design for a circle, a rounded square and a squircle. The concept sheets preview the circle and an approximation of Apple's rounded square.

### 2.3 Google Play store listing

Retrieved [E, [Google Play icon design specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications), retrieved 2026-09-26]; PLAT-7(b) also cites [Play Console Help](https://support.google.com/googleplay/android-developer/answer/9866151) for *"You must provide an app icon to publish your store listing"* (retrieved by the PM/BA, not by me):

- **512 × 512 px, 32-bit PNG, sRGB, at most 1024 KB.**
- **Full square**: *"Google Play dynamically handles masking. Radius will be equivalent to 30% of icon size."*
- **No drop shadow** on the asset; *"You can create shadows and lighting within the artwork."*
- **Prohibited content** that matters here: *"Don't use text or graphic elements to indicate ranking"*, *"…to promote deals or incentivize installs"*, *"…that can mislead users"*. These agree with MEM-1 and with LOOK-5's no-call-to-action rule.

### 2.4 Other assets the build will need [K, not retrieved; for the CTO to confirm]

- **Android notification small icon.** If Haunts sends any notification (CAP-8 and CAP-9 allow a few, off by default), Android needs a small single-colour status-bar silhouette [K, high confidence]. The monochrome layer is its natural source.
- **Launch or splash screen.** Android 12 and later draw the app icon on the system splash screen [K, medium confidence]; iOS uses a launch screen the app supplies [K, high confidence].
- **Play feature graphic** (a wide banner for the store listing) [K, medium confidence on its dimensions, so none are stated here]. It is store marketing and falls under PLAT-6 (no name until the checks pass) and HEAD-13 (no real user data in store assets).

---

## 3. Exclusions and constraints

**From the decisions, binding:**

1. **No ghost, eye or tracking imagery** (D11(d)). D9's reason: *"for a location-history product, being invisibly followed is precisely the association the product exists to refuse."* The PM/BA's constraint 1 spells it out as *"no ghost, no eye, no crosshair, no tracking pin, nothing that reads as being followed or watched."*
2. **MEM-1:** *"Haunts never encourages drinking, and never rewards the frequency or volume of visits — anywhere in the product"*, which includes *"store and marketing copy"*. **So: no pint, wine glass, cocktail, bottle, "cheers", neon bar sign, confetti, trophy, medal, ribbon, level, streak flame or star-as-reward.**
3. **Not narrowed to pubs.** D9: the product covers **346,184** venues, not **42,407** pubs. The mark must be as true for a café, a theatre or a bakery as for a pub.
4. **No text where the mark must be legible at launcher size**, and **nothing containing the name is finalised until PLAT-6 passes** (the PM/BA's constraint 2). A single mnemonic letter is permitted by Apple (§2.1) but is a weaker choice, because a rename would take the icon with it.
5. **Works in one colour**, and **does not rely on colour alone** to be recognised (the PM/BA's constraint 3; A11Y-2's principle).
6. **The same mark serves as the recap credit** (the PM/BA's constraint 4; LOOK-5).

**Added by this seat, as judgment [J], from drawing the concepts:**

7. **No map pin anywhere**, including in the interface: the Places tab is an awning in every mockup. **No concentric rings, radar, target, sonar, Wi-Fi-like arcs, footprints, dotted routes or breadcrumb trails.** Each reads as tracking.
8. **No headstone, tombstone, grave or cross.** An arch on a plinth, or a row of arches, reads as a headstone. **My own first drawings of the Doorway icons did**, and I only saw it on the rendered sheet (`brand-directions.md` §3). In a product whose name the CEO changed because *"Haunt seems a bit dark"*, this is the most likely accidental failure.
9. **No moon, stars-and-night sky, or neon.** Evening imagery narrows the product to a night out (constraint 3) and drifts towards MEM-1.
10. **No padlock, shield or key as the main idea.** Privacy is the product's differentiator, but a padlock reads as a password manager or a VPN, and it promises a kind of security the product does not claim [J].
11. **Avoid a bookmark ribbon** (close to a leading journalling app's mark [K, medium confidence, not retrieved]), **paired arches, and any yellow arch** (close to a famous fast-food mark [K, high confidence]).

---

## 4. Deliverables and sizes

**Source files (the thing Candour must own):**

| # | Deliverable | Specification |
|---|---|---|
| S1 | **Master mark, vector** | SVG or equivalent, layered: background, foreground (one or more layers), and a one-colour silhouette |
| S2 | **iOS icon source** | Layers suitable for Icon Composer, on a 1024 × 1024 canvas, annotated for default, dark and mono (§2.1). If the CTO confirms a flat PNG route instead, a 1024 × 1024 PNG as well |
| S3 | **Android adaptive icon** | Foreground, background and monochrome layers at 108 × 108 dp, with the mark inside the 66 dp safe zone and at least 48 dp (§2.2); vector preferred |
| S4 | **Google Play icon** | 512 × 512 px, 32-bit PNG, sRGB, ≤ 1024 KB, full square, no drop shadow (§2.3) |
| S5 | **Recap credit** | The one-colour mark as a vector, plus a version for light and a version for dark backgrounds (LOOK-5(e)); at 3× the LOOK-5 size constant if raster (PLAT-7(e)) |
| S6 | **Notification small icon** | A single-colour silhouette, if the CTO confirms notifications ship (§2.4) |
| S7 | **Wordmark** | Only after PLAT-6 passes. Outlined (converted to paths) so no font licence travels with it |
| S8 | **Usage sheet** | One page: clear space, minimum size, colours, what not to do (the §3 list) |

**The LOOK-5 size constant, proposed** [J]: the credit's height is **4% of the recap image's short side, never below 24 px**, placed in the footer margin, outside the content area, with clear space equal to its own height. That is small enough to be a credit and large enough to be legible. UX signs it off on a real recap at build.

**Verification before acceptance** (these become PLAT-7's (d) and a new check):

1. **A test submission to both stores, before the release-candidate build** (PLAT-7(d)), which settles ITMS-90704 and Play's validation at first hand.
2. **The misreading test** [J]: show the icon, without the name and without explanation, to **five people who have not seen it before**, and ask *"What do you think this app does?"* and *"What does this picture show?"*. **Any answer involving a grave, a ghost, being watched or tracked, a map, or drinking fails the icon.** This is the check that would have caught my own headstone drafts. It costs nothing if Candour asks people it knows; paid recruitment would be a spending decision.
3. **The 29 px, greyscale and one-colour checks**, as on the concept sheets.

---

## 5. What to hand a human designer or a tool

**The pack** (everything a stranger needs, nothing they have to ask for):

1. **This brief**, §0 to §4.
2. **The chosen direction** from `brand-directions.md`: its palette with measured contrast, its type, its idea, and **its three concept icons** from `concepts/`, labelled as starting points, not as the answer.
3. **The product in two sentences:** *"A private, on-device journal of the places you have been. It never leaves your phone unless you turn on backup, and it has no ads, accounts or tracking."* **This is my draft, not approved copy.** Store copy is bound by PRIV-1's canonical sentence and by the CGO's contract-term check under CRA 2015 s.36(3), so the designer gets it as context, never as copy to put on anything.
4. **The exclusions list** (§3) on its own page, with the reasons, because a designer who knows *why* the pin is out will not draw a stylised pin.
5. **The deliverables table** (§4) and the acceptance checks.
6. **The working-name warning**: "Haunts" may change (PLAT-6). Nothing containing the name is final.

**If a human designer is used.** Commissioning is spending real money and the CEO's decision (Constitution 5.4); the CFO adds it to the cost sheet as a third-party cost (Article 2.1). **The contract must assign copyright in the artwork to Candour** (or to the CEO while Candour is unincorporated) **and include the source files**, not only exports. That is the CGO's to draft or confirm (§6). **I have not estimated a price**: I retrieved no market rates, and a guessed figure would anchor a spending decision on nothing. The CFO can price it if the CEO wants this route.

**If a tool is used** (an image generator, or an agent such as this seat drawing vector geometry). Two cautions:

- **The ownership question is open and is the CGO's** (below). **It applies to the concepts in this folder**: they were drawn by an AI agent, so adopting one of them as final artwork is itself "a mark produced by a tool".
- **Raster image generators produce images, not layered vectors.** Every deliverable in §4 is a vector or a layered source, so a generated image would still have to be redrawn [K, high confidence].

---

## 6. Ownership, spending and the open CGO question

**`requirements.md` §22 item 18, open, owned by the CGO:** *"Rights in the icon and mark — who owns artwork a person is commissioned to make, and whether a mark produced with a tool can be owned and registered."* Its reason: *"A trademark filed on a mark Candour does not own is wasted money; Constitution 6.1 puts IP-determining terms before a qualified human."*

**What this brief does about it:** nothing that pre-empts it. **I recommend the CGO answers item 18 before the CEO decides between a human designer and a tool**, because the answer may decide the route. If a tool-made mark cannot be protected, a human designer (or a human who substantially redraws a tool's concept) may be the only route to a registrable mark. Constitution 6.1 applies: the CGO's view is preparation, and the answer that is relied on should come from a qualified human.

**Spending:** none is proposed here. The artwork, any paid recruitment for the misreading test, and any trademark filing are each CEO decisions under Constitution 5.4.

**Sequencing, so the critical path is visible** (PLAT-7: *"it should be briefed now, because nothing about it can be done in the week before submission"*):

1. CEO chooses a direction (`brand-directions.md`).
2. CGO answers §22 item 18.
3. CEO decides the route (human, tool, or a hybrid), and any spend.
4. Artwork is made; the misreading test runs.
5. PLAT-6's three name checks pass (only then is anything with the name finalised).
6. Test submission to both stores, **before** the release-candidate build.

---

## 7. Evidence register

| # | Claim | Source | Retrieved by |
|---|---|---|---|
| E1 | Apple app-icon guidance: 1024 px canvas, layers, Liquid Glass, Icon Composer, six appearances, text, simplicity, no photos or UI | [Apple HIG App icons (JSON)](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json) | This seat, 2026-09-26 |
| E2 | Android adaptive icons: 108 dp layers, 66 dp safe zone, 48–66 dp logo, monochrome layer, clean edges | [Android developers, Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) | This seat, 2026-09-26 (and the PM/BA, 2026-09-22) |
| E3 | Google Play icon: 512 px, 32-bit PNG, sRGB, 1024 KB, full square, 30% radius, no shadow, prohibited elements | [Google Play icon design specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) | This seat, 2026-09-26 (and the PM/BA, 2026-09-22) |
| E4 | *"You must provide an app icon to publish your store listing"* | [Play Console Help](https://support.google.com/googleplay/android-developer/answer/9866151) | **PM/BA, 2026-09-22; not re-retrieved by me** |
| E5 | ITMS-90704 "Missing App Icon" | [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/1336789/itms-90704-missing-app-icon-an-app-icon-measuring), **secondary, single source** | **PM/BA, 2026-09-22; not re-retrieved by me** |

**[K], not retrieved:** Expo's handling of Icon Composer files; Android notification icon and splash-screen specifics; the Play feature graphic's size; platform support for alternate icons; the marks of other apps named in §3.

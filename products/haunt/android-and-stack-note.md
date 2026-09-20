# Android and stack note — Haunt

**Seat:** Chief Technology Officer · **Date:** 2026-09-16
**Commissioned by:** CEO, in response to `products/haunt/feasibility-note.md` §1 and §6
**Status:** technical note. Amends the feasibility note where it says so. Feeds Condition 1 of `decisions/2026-09-16-haunt-gate.md`. **Prepares, does not certify** (Constitution 6.1).
**Evidence:** every substantive claim tagged per `pipeline/evidence-standard.md`. All [E] sources were retrieved on **2026-09-16** during the session that produced this note. Nothing is cited from memory. Effort figures are [J].

---

## 0. The three answers, before the working

**1. The CEO is right and I was wrong about the shape of the Android problem.**

My finding — that no first-party Android equivalent of `CLVisit` exists — survives retrieval intact. My *conclusion* did not. I wrote that the gap was "structural rather than a matter of effort." That was too strong, and the Google Maps counter-example is the right way to expose it. Retrieval this session found **third-party Android apps shipping automatic stay-detection today, on the Play Store, offline, built by small teams** — DayTrace is the direct product analogue [E] — and **three commercial SDK vendors** (Foursquare, Radar, Sentiance) whose entire business is third-party visit detection on Android [E]. The primitive is absent. The capability is not. Those are different claims and I conflated them.

I also overstated one supporting fact. I wrote that a few background fixes an hour "is not enough to bound arrival and departure well." Android's own documentation says the batched Fused Location Provider gives "access to more time-frequent location history after your app receives a batch update" [E, quoted below]. Dense samples delivered sparsely is a much better input than sparse samples, and for a journal read hours later, delivery latency is nearly free. I got that wrong in the product's disfavour.

**Corrected verdict: a third-party Android build of Haunt is feasible at acceptable reliability.** Not at iOS's reliability, not for free, and not without one thing the iOS build does not need — *the app must show the user when capture was off*, because with no server we cannot detect the failure any other way. §1.7 states the cost.

**2. React Native with Expo is the right call — but only because Android is now in scope, and it saves far less than it looks like it saves.**

The load-bearing fact: **`expo-location` does not expose `CLVisit` or `startMonitoringVisits` at all** [E, retrieved]. The single API this product exists for is not in the framework. It requires a local Expo module written in Swift, which requires prebuild and a development build. The same is true on Android, where the capture layer is Kotlin regardless.

So React Native shares the UI and does not share the part that costs the money. On my sizing it saves **about 1.5 weeks on a two-platform build — roughly 4%**, not the half that "write once" implies, because the shared UI is about a tenth of this particular product. It is still the right choice *given two platforms*, because the rows it does share are the ones that would otherwise be written twice. **If the CEO reverts to iOS-only, I recommend native Swift instead**, and §2.7 says why. Stack follows platform scope; it should not be chosen first.

Under Constitution 5.4 the stack is not a CEO-reserved decision, so the recommendation in §2.7 is mine. I am **not** blocking — a block is a checklist item failing, not a preference, and nothing here fails a checklist. If the CEO directs a different stack, that is a direction to record, not an overrule, and it changes the hours in §3.

**3. The consequence nobody has priced: the build roughly doubles, and break-even goes with it.**

For a two-platform React Native build at the scope the gate's conditions actually require, **the figure I want the CFO to use is 1,160–1,500 hours of build, point estimate 1,330 hours, plus 75 hours for the Android capture-reliability spike that Block 2 requires and that must be carried separately because it may return "don't."** Against the CFO's 810 hours for both platforms, that is **+44% to +85%, and +64% at the point estimate**. §3 gives the decomposition, the maintenance and support figures, the O11 reconciliation, and the new Android-side fixed costs.

**I am not producing the break-even number.** Condition 1 assigns that to the CFO and this note exists so she derives it once, on these hours. §3.6 states the order of magnitude only, tagged as an indication and not a price.

---

## 1. The Google Maps Timeline counter-example, answered directly

### 1.1 What Google actually documents

Very little, and that is itself the finding. Google's own Timeline help page says:

> "Timeline helps you go back in time and remember where you've been by **automatically saving your visits and routes** to your Google Maps Timeline on each of your signed-in devices."

> "When you turn on Timeline, you consent to Google **regularly saving each of your devices' precise locations to that device**, to show you where you've been, **including when Google apps aren't open**."

[E, quoted verbatim — [Google, Manage your Google Maps Timeline (Android)](https://support.google.com/maps/answer/6258979?hl=en&co=GENIE.Platform%3DAndroid)]

Read what that says and what it does not. It describes **continuous sampling of precise location into on-device storage**, and an outcome ("visits and routes"). It does **not** describe an event API. Google does not publish a "the user has settled somewhere" callback for Maps any more than it publishes one for us — Maps is doing the same thing the SDK vendors in §1.3 do: sampling, then clustering the samples into stays. The visit is *computed*, not *delivered*.

**So the honest answer to "Timeline does it, therefore it is possible" is: yes, and the mechanism is not an API you are missing. It is work you would have to do.**

### 1.2 Is Maps using privileged APIs? Partly — and it matters less than I assumed

The CEO's question was whether Timeline relies on privileged, private or Play-Services-internal capability. I could not close this, and I am going to say so rather than assert the convenient answer.

**What I could not retrieve:** any Google document stating which APIs Google Maps or Google Play services use for Timeline, and any Google document stating that Play services is exempt from the background location limits that bind third-party apps. I looked. Google publishes the outcome and not the mechanism. **Flagged as unverifiable, not assumed** (evidence standard).

**What is inferable, and tagged as inference:** Timeline's collection is performed by Google Play services, a component preinstalled as part of the system image on GMS-certified devices rather than installed by the user. A first-party system component does not have to solve the two problems that bind us — the Android 8.0 background throttle, and OEM battery managers — because it is not a third-party app subject to either [I, from the structure of the platform; **not evidenced**, and the Skeptic should treat this as the weakest sentence in this note]. The community scorecard on OEM killing describes exactly this asymmetry: "Some OEMs keep a whitelist of their associate apps while rampantly killing others" [E, single source, community-maintained — [dontkillmyapp.com](https://dontkillmyapp.com/)].

**But here is why the question turned out not to decide anything.** I set out to show that Maps is privileged and therefore no guide. Retrieval showed something better and more inconvenient: **third parties do this anyway, without privilege.** Whether Maps has an advantage is now beside the point. §1.3 is the real answer to the CEO's challenge.

### 1.3 What third-party Android apps actually use — four retrieved examples

**a) DayTrace (Play Store, `com.mbitsoftware.daytrace`) — the direct product analogue.** A German one-developer Android app that "automatically records your daily routes and **places you stay** — **fully offline**, without cloud services," and that "uses a **lightweight foreground service** to ensure consistent location updates — without aggressive battery drain" [E — [alternativeto.net listing for DayTrace](https://www.alternativeto.net/software/daytrace--gps-and-timeline/about/); I was unable to retrieve the Play Store listing itself, which truncated, so this is **single source and secondary** — the Skeptic should install it, exactly as Condition 3 requires for Arc]. This is Haunt's Android build, shipped, by someone smaller than Candour, on the same offline architecture. Its existence is the strongest single rebuttal of my original conclusion.

**b) GPS Logger (northforceapps).** "Runs as a **foreground service** so recording continues when the screen is off or you switch apps, with a **persistent notification** while it tracks"; "**Motion-adaptive sampling keeps battery use low**"; builds a daily timeline of "walks, rides, **stops** and moments"; data "stay[s] on your phone unless you choose to live-share or export" [E, quoted — [GPS Logger](https://northforceapps.com/gpslogger/)]. Note also that it tells users to follow "in-app battery guidance so Android does not suspend it" [E, same source] — the OEM problem, handled as a user-facing instruction because there is no other way to handle it.

**c) Foursquare Movement SDK (formerly Pilgrim) — the commercial specialist.** Uses "**stop detection technology and dwell time** to capture true visits," distinguishing a real stay from driving by or sitting in traffic, from "GPS, bluetooth, accelerometer, time of day" plus "wifi signals, and information from the compass, accelerometer, and barometric sensors." On power: "**uses less than 0.5% of daily battery** when running in the background," because "when a user is stationary (at a visit) the SDK **shuts down background location usage and is idle**" [E, quoted — [Foursquare, Movement SDK FAQs](https://docs.foursquare.com/developer/docs/movement-sdk-faqs); [Movement SDK overview](https://docs.foursquare.com/developer/docs/movement-sdk-overview)]. Treat the 0.5% as **vendor marketing, not measurement** — it is unqualified by device or duty cycle [J].

**d) Radar — the published tracking-preset design, which is the most useful document of the four.** Its `RESPONSIVE` preset "detects whether the device is stopped or moving. When moving, it tells the SDK to send location updates… every 2-3 minutes. **When stopped, it tells the SDK to shut down to save battery.** Once stopped, the device will need to move more than 100 meters to wake up." Only the `CONTINUOUS` preset "starts a **foreground service with a notification**." And critically: background tracking "will work **even if the app has been backgrounded or killed**, as Android location services will wake up the app to deliver events and the SDK uses `JobScheduler` to schedule network requests" [E, quoted — [Radar, Android SDK](https://docs.radar.com/sdk/android)].

Radar also publishes the honest caveat, which no vendor has to and which I take as the most credible sentence retrieved this session: updates "may be **delayed significantly by Doze Mode, App Standby, and Background Location Limits**, or if the device has connectivity issues, low battery, or wi-fi disabled" [E, quoted, same source].

**e) Sentiance — corroborates the OEM problem from a second, independent, commercial source.** Names "OnePlus and Nokia (HMD Global)" as performing "aggressive battery optimization, keeping the device in Doze mode longer than intended"; warns that Android's Adaptive Battery bucketing "**can impact the detection quality of the SDK**"; recommends calling `disableBatteryOptimization()` to trigger the system dialog **and in the same breath quotes the Play prohibition on doing so unless core functionality is affected** [E — [Sentiance, Android battery optimization](https://docs.sentiance.com/sdk/appendix/android/android-battery-optimization.md)].

**This upgrades my §1.2(f) claim from single-source to corroborated.** dontkillmyapp is a community list; Sentiance is a vendor with commercial reason to downplay the problem and documents it anyway. Independent origins. The OEM problem is real and it is not a forum complaint.

### 1.4 The corrections I owe my own note

Stated plainly, because the evidence standard makes a wrong load-bearing claim my problem to fix and not the Skeptic's to find.

| Feasibility note §1.2 said | Correction |
| --- | --- |
| The gap is "**structural** rather than a matter of effort" | **Wrong.** The missing primitive is structural; the missing *capability* is effort. Four shipped examples say so (§1.3). The sentence should have read: "Android gives away none of what iOS gives away; all of it has to be built and tuned." |
| A few fixes an hour "is not enough to bound arrival and departure well" | **Overstated.** Android documents that "by using the **batched** version of FLP… you have access to **more time-frequent location history** after your app receives a batch update, which also occurs only a few times each hour" [E, quoted — [Android, Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits)]. Dense history delivered a few times an hour bounds a two-hour dinner well. Latency is not accuracy, and for a journal, latency is cheap. |
| "A capture layer that works on Pixel and fails quietly on a Xiaomi is… the opposite of [the promise]" | **Half right, and the wrong half was load-bearing.** Failing *quietly* is the opposite of the promise. Failing *visibly* is not — it is an honest product with a stated limitation, which is what Article 1.3 actually requires. This changes the design, not the decision: see §1.6. |
| The Play background-location gate presented as near-prohibitive for a solo operator | **Overstated.** Every fact I quoted is still true and still retrieved [E, feasibility note §1.2(e)]. But DayTrace and GPS Logger are on the Play Store doing this, which proves the gate is *passable* for this exact category. It is a cost and a schedule risk, not a wall. |

### 1.5 What holds, now against the counter-example rather than around it

1. **There is still no first-party Android visit API.** Retrieval this session found none, and Google Maps does not use one — it samples and clusters (§1.1). The Awareness Fence API remains deprecated with "no direct replacement" [E, feasibility note §1.2(a)]. Geofencing remains pre-registration, which cannot fence the unknown. The Activity Recognition Transition API remains transitions, not visits — `STILL`/`WALKING`/`IN_VEHICLE` enter and exit, delivered by `PendingIntent` when the app is not running, requiring Play services 12.0.0+, with "the latency of event detection might vary by device" [E — [Android, Detect when users start or end an activity](https://developer.android.com/develop/sensors-and-location/location/transitions)].
2. **The asymmetry with iOS is unchanged and is the whole of the extra cost.** iOS hands you the visit and relaunches your terminated app to deliver it. Android hands you ingredients. Everything in §3's Android rows is the price of that sentence.
3. **The OEM problem is real, corroborated (§1.3e), and has no fix available to us** — only a user-facing mitigation, which every vendor in this category uses and which Play policy constrains.
4. **The foreground service is a visible product cost.** Both shipped analogues run one [E, §1.3a-b]. Radar shows a non-FGS path exists but publishes the caveat that it can be "delayed significantly" [E].

### 1.6 The design that makes Android substantiable — and it is not the one I assumed

I assumed the choice was *invisible-and-unreliable* versus *don't ship*. There is a third option and it is better on Article 4 grounds than the iOS design:

> **Run the location foreground service. Make its notification the honest surface. And record capture gaps as first-class data.**

Three parts:

- **Foreground service, declared properly.** `android:foregroundServiceType="location"`, `FOREGROUND_SERVICE_LOCATION` in the manifest, `ACCESS_FINE_LOCATION` at runtime, and `ACCESS_BACKGROUND_LOCATION` because the service must be creatable while the app is backgrounded [E — [Android, foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types)]. Inside it: Activity Recognition transitions as the cheap trigger, batched FLP for the fixes, clustering for the stay. This is the Radar `RESPONSIVE` shape with the reliability of `CONTINUOUS`.
- **The notification is not a tax, it is the product telling the truth.** "Haunt is watching for places — 3 today" is a more honest artefact than a journal that silently reads your location with nothing on screen. I would ship this on Android and I would not apologise for it in the copy. Article 4 prohibits "deliberately buried settings"; a permanent, tappable, honest status line is the opposite of one.
- **Capture gaps are data.** When the service is killed, restarted, denied permission, or Doze-suspended past a threshold, Haunt records a gap row and the timeline renders it: *"Haunt wasn't running between 14:10 and 19:40. Anything you did then isn't here."* This is the mechanism that makes "automatic" substantiable under Article 1.3 on a fleet we cannot control — we are not claiming we never miss; we are claiming **we always tell you when we missed**, and that claim we can substantiate and test.

I now think the gap surface should ship on **iOS too**, where it covers the provisional-`Always` downgrade I flagged in feasibility §1.1. Android forced out a better design for both platforms. That is recorded as a scope *addition* in §3 and it is not free.

### 1.7 Straight verdict on Android

> **Feasible. At acceptable reliability, conditional on the Block 2 spike. At a real and non-trivial cost in effort, battery and support.**

- **Effort:** the Android capture layer is the largest single line in §3 at **5–7 focused weeks**, and it is the line React Native does not shrink. Plus the 2-week spike, plus 1–2 weeks of Play policy work, plus device-matrix testing.
- **Battery:** measurably worse than iOS and **I will not put a number on it.** The only figures published are vendor marketing (§1.3c), and Apple publishes none for `CLVisit` either [E, feasibility §1.1]. Both platforms' battery cost must be measured in the spike and the field-test rows, and **no marketing claim about battery may be made before that lands** (Article 1.3). This is open question 3 from the feasibility note, unchanged and now doubled.
- **Support:** a standing, permanent, unfixable-by-us category of case — "it stopped recording on my Xiaomi" — for which the only answer is a battery-allowlist walkthrough. Priced in §3.4 as a raised Android contact rate, not hidden.
- **The condition:** Block 2 stands, unmodified. The spike runs before product code, on at least a Pixel, a Samsung and a Xiaomi, over ≥2 real weeks, with a minimum capture rate agreed with PM/BA and QA **before** it runs. What §1.6 changes is the measurement: the spike must now also measure **how accurately the app knows it missed something**, because the gap surface is what carries the honesty claim. A spike that shows 80% capture with reliable gap detection is a pass; 95% capture with silent failures is not.

**My §1.4 disagreement on the record is withdrawn in part.** I asked that the platform line be restated as "iOS at launch; Android an intention." On this evidence I no longer think Android is unsubstantiable. **The disagreement that survives, narrowed:** the word "automatic" is substantiable on Android only alongside the gap surface in §1.6. Ship the gap surface and I have no objection to claiming automatic capture on both platforms. Ship without it and I do.

---

## 2. React Native with Expo, and EAS

### 2.1 The load-bearing question, answered: Expo does not expose visit monitoring

I retrieved the current `expo-location` API surface rather than recalling it.

**`expo-location` exposes `Location.startLocationUpdatesAsync(taskName, options)` — "registers for receiving location updates that can also come when the app is in the background" — and `Location.startGeofencingAsync(taskName, regions)`. It exposes `ActivityType` and `Accuracy` enums for tuning background updates. It contains no reference to `CLVisit`, `startMonitoringVisits`, or visit monitoring of any kind** [E — [Expo, Location SDK reference](https://docs.expo.dev/versions/latest/sdk/location/)].

So on iOS — the platform already gated for build — **the single API the product is built around is not available through the framework the CEO wants to use.** Expo gives you the two things my feasibility note specifically ruled out as substitutes: continuous background updates (the power-hungry ladder rung Apple's own guidance tells you to avoid) and geofencing (which solves the opposite problem).

### 2.2 What that costs, exactly

**A local Expo module in Swift.** `npx create-expo-module@latest --local` generates a module with `android/`, `ios/`, `src/`, `expo-module.config.json` and `index.ts`; you write `MyModule.swift` and `MyModule.kt` and edit them in Xcode and Android Studio directly; and if the project has no native directories you must run `npx expo prebuild --clean` first [E — [Expo, Get started with modules](https://docs.expo.dev/modules/get-started/)]. Consequences, each of which the CEO should see named:

- **No Expo Go.** The project moves to prebuild / Continuous Native Generation and a development build. This is normal and supported; it is not the "managed workflow" experience.
- **The native directories become real.** Config plugins keep them generatable, but every native edit is a plugin to write or a directory to check in. Expo does not remove Xcode and Gradle from this project; it defers them.
- **The capture layer must never depend on JavaScript.** This is the architectural point and it is the one I feel strongest about. `startMonitoringVisits` relaunches a *terminated* app to deliver a visit [E, feasibility §1.1, quoted from Apple]. In React Native, "relaunch the app" means booting Hermes and the bridge before a single byte is recorded. The correct design is: **the Swift module receives the `CLVisit`, writes it straight into SQLite in Swift, and returns — JavaScript is never started.** The JS layer reads that table later, when the user opens the app. Same on Android: the Kotlin foreground service owns capture and writes to the same file.

  That means the shared SQLite file is a **contract between three implementations** (Swift, Kotlin, JS), needing a written schema spec, a migration owner, and concurrency discipline (WAL, one writer). It is entirely doable. It is also the thing that will cause the subtle bugs, and it is a row in §3.

**Net:** React Native leaves the hard half of this product native on both platforms. What it shares is the timeline, the venue picker, editing, notes, ratings, search, settings, export/import UI and onboarding — which is genuinely most of the *screens* and genuinely worth having, once there are two platforms.

### 2.3 How the rest of the specified architecture fares

| Piece (feasibility note ref) | Verdict under Expo | Evidence |
| --- | --- | --- |
| **SQLite store** (§3) | **Good.** `openDatabaseSync`/`openDatabaseAsync`; FTS3/4/5 enabled by default (`enableFTS`, defaults `true`); `customBuildFlags` for extra compile options. | [E — [Expo SQLite](https://docs.expo.dev/versions/latest/sdk/sqlite/)] |
| **Bundled ~21 MB venue index as an app asset** (§2.4) | **Good, with one caveat.** `SQLiteProvider` takes an `assetSource` to open "a new SQLite database using an existing `.db` file you already have," with `forceOverwrite`. The caveat: it copies the asset out of the bundle, so the device holds ~21 MB twice until we manage it. Trivial against Apple's limit of **4 GB uncompressed** for iOS 9+. | [E — Expo SQLite, as above; [Apple, Maximum build file sizes](https://developer.apple.com/help/app-store-connect/reference/maximum-build-file-sizes/)] |
| **Spatial index on 346k venues** | **Caveat, with a cheap way round it.** R-Tree is not documented as available in `expo-sqlite`; `customBuildFlags` is the escape hatch but is an unverified path [E, absence noted]. **Don't rely on it.** Use an integer grid-cell column (quantised lat/lng) with a plain B-tree index and a 9-cell neighbourhood query. Boring, portable across all three implementations, and fast enough at this size [J, high confidence]. | — |
| **Passphrase-based encryption** (§4.2) | **Partial — and the gap is the security-critical half.** `expo-crypto` now exposes `aesEncryptAsync`/`aesDecryptAsync`, `AESEncryptionKey`, `getRandomBytes` and digests. It exposes **no key derivation function** — no PBKDF2, no scrypt, no Argon2id. My §4.2 design specifies Argon2id or scrypt, so the KDF must come from a native module or a third-party dependency. A memory-hard KDF in JavaScript is not a real option at usable parameters [J]. **CSO owns this choice; it is a security-critical dependency and should not be picked by whoever is nearest the keyboard.** | [E — [Expo Crypto](https://docs.expo.dev/versions/latest/sdk/crypto/)] |
| **iCloud backup target** (§4.1) | **Weak — and I am using it as a reason to cut scope.** There is no first-party Expo or React Native iCloud/CloudKit module. The community option is `react-native-cloud-store`, which does have an Expo install path [E, single source — [react-native-cloud-store](https://react-native-cloud-store.vercel.app/docs/install/with-expo)]. Making the backup path of a privacy product depend on one community maintainer is a supply-chain and longevity risk I would rather not take [J]. **Recommendation in §2.5.** | — |
| **Android backup target** (§4.1) | **Fine.** Auto Backup is manifest configuration, expressible as a config plugin; the Drive `appDataFolder` route is an ordinary OAuth HTTP call needing no native module [I, from feasibility §4.1 which retrieved both]. | — |
| **Platform-mediated crash reporting** (§5 Layer 1) | **Degraded, and this partly erodes a finding I called "free."** The process still crashes and Apple/Google still collect it. But a JS exception yields a Hermes stack like `p@1:132161`, and React Native's own documentation states: "**Source maps are required to symbolicate stack traces**" [E, quoted — [React Native, Symbolicating a stack trace](https://reactnative.dev/docs/symbolication)]. Candour must therefore **retain per-build source maps for the life of every shipped version** and symbolicate by hand with `metro-symbolicate`. That is a permanent operational obligation and a new row in §3.4. | — |
| **MetricKit** (§5 Layer 2) | **Another native shim.** No Expo module; `MXDiagnosticPayload` needs Swift. Small, but real. [I] | — |
| **iOS Data Protection class on the store file** (§3) | **Native shim.** `NSFileProtectionCompleteUntilFirstUserAuthentication` is set natively; not exposed by `expo-sqlite`. Small. [I] | — |
| **WCAG 2.1 AA** (UX note §5) | **Harder, not blocked.** React Native maps to platform accessibility APIs but not identically to SwiftUI. The UX seat's per-feature acceptance criteria get more expensive to satisfy and must be verified on both platforms rather than reasoned about once [J]. **Flagged to UX; this is a cost of the stack decision that lands in her seat.** | — |

### 2.4 EAS — build, submit, and what the CFO must carry

Retrieved this session [E — [Expo pricing](https://expo.dev/pricing)]:

| Tier | Price | Included |
| --- | --- | --- |
| **Free** | **$0/month** | "15 Android and 15 iOS builds", "low-priority queue", 60 min CI/CD workflows, **EAS Submit included** |
| Starter | **$19/month** plus usage | "$45 of build credit, then usage-based pricing", 1 concurrency ($50/extra) |
| Production | $199/month plus usage | $225 build credit, 2 concurrencies |
| Enterprise | custom | $1,000 build credit, 5 concurrencies |

Per-build overages on paid tiers are "$1–$2 (Android), $2–$4 (iOS)". EAS Submit is included on every tier including Free [E, same source].

**My assessment for the CFO, plainly:**

- **The right number to carry is £0/year.** 15 iOS + 15 Android builds a month is generous for a product shipping a handful of releases a year plus TestFlight/closed-test iterations. The low-priority queue costs waiting, not money.
- **EAS is optional, not load-bearing.** `npx expo prebuild` then Xcode and Gradle on the founder's own Mac produces the same binaries for nothing, and `eas build --local` exists. **The stack decision does not commit Candour to a subscription**, and that matters given Constitution 1.5 and a £83/year fixed cost.
- **Carry a named contingency, not a certainty.** If the free tier's build allowance proves tight, the step is Starter at **$19/month = $228/year**. That is **roughly double or more Candour's entire current annual fixed cost** [I; the CFO sets the FX rate, not me]. It should appear on the cost sheet as a contingency with a stated trigger ("if monthly builds exceed 15 per platform"), not as a line item and not as zero-with-no-note.
- **EAS does not remove the Mac.** iOS builds still need Apple signing assets and App Store Connect; EAS hosts the build, not the Apple relationship.

**New Android-side fixed costs the CFO does not currently carry** (not EAS, but they arrive with this decision):
- **Google Play developer registration, one-off** — US$25, one-time, no annual renewal [E, **secondary source**, flagged — [ConsoleMint](https://consolemint.com/google-play-console-price/); I could not retrieve this from Google's own page and it must be confirmed at signup, not assumed].
- **The closed-test gate, which is a schedule cost, not a fee.** New personal developer accounts must run a closed test with "a minimum of **12 testers** who have been opted in continuously for at least **14 days**" before applying for production access, then complete a three-part application, with review "usually… seven days or less" [E, quoted — [Play Console, Get ready to publish (production access)](https://support.google.com/googleplay/android-developer/answer/14151465)]. **Candour must recruit twelve real testers and keep them for a fortnight.** For a company whose Skeptic has repeatedly found that *reach* is the binding constraint, that is not a formality — it is the first real test of whether twelve people can be found at all. I would treat it as a cheap, early, honest signal and run it before the build is finished, not after.

### 2.5 One scope cut the stack analysis paid for

The iCloud gap (§2.3) is an opportunity, not just a risk. My feasibility §4.2 already lists a **"save encrypted backup file to Files / Drive / anywhere"** option as the third route, and notes it is also the Article 7.2 discontinuation path.

**Recommendation: make the user-saved encrypted file the *only* backup at MVP, on both platforms.** It drops a community native dependency, drops a native module, drops the CloudKit/Advanced-Data-Protection honesty caveat I had to write in §4.1, works identically on iOS and Android, and is *more* transparent — the user can see the file, move it, and open it with our published format. Automatic cloud sync becomes a post-launch addition if users ask for it.

This lands at the low end of the backup row in §3 and removes a risk the CSO would otherwise have to review. It does not fully pay for Android, but it is the one place this analysis found scope worth returning.

### 2.6 What I am *not* claiming about React Native

- I am not claiming it is faster to build in. On this product it is faster only because there are two platforms; §3.3 shows the margin is about 4%, not 50%.
- I am not claiming it is more boring. Constitution 1.5 and my charter both push toward boring, and a React Native app with four local native modules, prebuild, config plugins, a Hermes symbolication runbook and an annual Expo SDK upgrade is **not** more boring than one Swift app. It is more boring than *two* native apps.
- I am not claiming the performance is fine. I believe it will be [J, moderate confidence] — this is a list, a map and a form — but the venue picker searching 346k rows with a map behind it is the one screen I would build first as a spike.

### 2.7 Recommendation, with the reason

> **Build Haunt as React Native with Expo (prebuild/CNG, development builds, local Expo modules in Swift and Kotlin for the capture layers, EAS on the free tier) — conditional on two platforms being in scope.**
>
> **If the CEO reverts to iOS-only, build it in Swift instead.**

**The reason, in one sentence:** React Native's entire benefit on this product is writing the screens once, and the screens are only written twice if there are two platforms — while every one of React Native's costs (a Swift module for `CLVisit`, a KDF gap in the crypto, a native shim for MetricKit and file protection, a community dependency or a cut for iCloud, a source-map obligation on the diagnostics promise, and an annual SDK upgrade) is paid whether or not Android ships.

On iOS-only you pay all of that and collect none of it. That is the whole argument, and it is why I say the stack question is downstream of the platform question rather than beside it.

**Two conditions I attach to my own recommendation:**

1. **The capture layers are native and JS-independent** (§2.2). If the design ever has JavaScript in the path of recording a visit, I will raise it as a block under my charter — that is an architecture that is unsustainable by design, and it is the one place I would use the word.
2. **The CSO picks the KDF** (§2.3) before the crypto is written, not after.

**Constitutional note, stated once.** Constitution 5.4 reserves kill/proceed decisions, spending real money, pricing, user-data policy and release to real users. **The stack is not on that list**; Article 6 gives "technical architecture… keeps the stack boring and cheap" to this seat. So this recommendation is mine to make. It is also the CEO's to direct otherwise, and I want to be precise about the mechanism: a direction to use React Native on an iOS-only build would **not** be an overrule of a block under 5.6, because I am not blocking — nothing here fails a checklist, and my charter says a block is "a checklist item failing, never a feeling of unease." It would be a direction against a recorded recommendation. It should be written into the decision record anyway, because it changes the hours in §3 and therefore the price.

---

## 3. Build hours for the CFO — Condition 1 input

Everything in this section is **[J]** — my estimate as CTO, not evidence. The unit is a **focused solo week = 37.5 hours**, stated explicitly because the Skeptic's O2 finding (that my weeks and the CFO's hours diverged by 33–58%) only resolves if the conversion is written down. It was not, and that was my omission.

### 3.1 The figure I want the CFO to use

> **SUPERSEDED, 2026-09-19 (CTO), by `products/haunt/subscription-sizing-note.md` §10.2.** The 1,160–1,500 / point 1,330 figure below is correct for the scope it was decomposed against and **that scope has since grown four times, in four documents, none of them re-based against the others**: the subscription ladder, session segmentation and the venue page, the DMCCA requirements, and the venue-index remediation the Engineer's spike made necessary. **The current figure is 1,770–2,410 hours, point estimate 2,090**, plus **188 hours** of separately-carried pre-build spikes (the 75-hour Android capture spike below, plus a new 113-hour venue-index remediation spike). **Fixed annual maintenance moves from 220 to 360 h/yr (§3.4 below is superseded by that note's §9.2), and the fixed support floor from 78 to 115 h/yr.**

> **Two-platform React Native / Expo build: 1,160–1,500 hours. Point estimate 1,330 hours.**
>
> **Plus 75 hours (2 focused weeks) for the Android capture-reliability spike required by Block 2 — carried as a separate pre-build line, because it may return "don't build."**

Against the CFO's current 810 hours for both platforms, that is **+44% to +85%, and +64% at the point estimate.**

### 3.2 The decomposition

| # | Workstream | Weeks (low–high) |
| --- | --- | --- |
| 1 | Project and tooling setup: signing for both stores, App Store Connect, Play Console, Expo prebuild/CNG, config plugins, development client, EAS, CI | 1.5–2 |
| 2 | **iOS capture** — local Expo module in Swift: `CLVisit`, authorization state machine incl. the provisional-`Always` downgrade, candidate-visit queue, native-side persistence with **no JS in the recording path** (§2.2) | 3–3.5 |
| 3 | **Android capture** — Kotlin: Activity Recognition transitions, batched FLP, stay clustering, location foreground service and its notification, boot/restart resilience, per-OEM behaviour work | **5–7** |
| 4 | **Capture-gap detection and the timeline gap surface, both platforms** (§1.6) — *new scope, and the thing that makes "automatic" substantiable* | 1–1.5 |
| 5 | Venue index: extract pipeline, bundled `.db` asset, grid-cell spatial index + FTS5 name search, category mapping, confidence filtering, **duplicate merge / sticky choice / rename-in-place** (UX §2.3, accepted — see §3.5), "not listed" path | 4–5 |
| 6 | Timeline UI, entry editing, notes, ratings, search — React Native, **one implementation**, with per-platform polish | 3.5–4 |
| 7 | Data layer: schema, migrations, the three-implementation SQLite contract (§2.2), export **and** import | 1.5–2 |
| 8 | Encrypted backup: crypto, recovery-code UX, user-saved encrypted file (§2.5) | 1.5–2 |
| 9 | KDF selection, integration and CSO review (§2.3) | 0.5 |
| 10 | Onboarding, **two** permission flows, honesty surfaces, foreground-service notification copy | 2 |
| 11 | Accessibility to WCAG 2.1 AA — **distributed into rows 5, 6, 8 and 10, not a standalone line** (§3.5); shown here only as its aggregate | 1.5–2 |
| 12 | Diagnostics: redaction test, MetricKit shim, **source-map retention and symbolication runbook** (§2.3), Android vitals | 1–1.5 |
| 13 | Play policy: background-location declaration, FGS-type declaration, demonstration videos, prominent disclosure; App Store privacy and review prep | 1–2 |
| 14 | Field testing over real weeks on both platforms, battery measurement, ≥3-OEM device matrix, App Review and Play review cycles, the 12-tester closed test (§2.4) | 4–5 |
| | **Total** | **31–40 weeks** |
| | **In hours at 37.5 h/week** | **1,163–1,500** |
| | *Separate: Android capture-reliability spike (Block 2)* | *2 weeks / 75 h* |

**Row 3 is the honest centre of this table.** It is the largest line, it is the one Android adds, and it is the one React Native does not shrink by a single hour.

**Calendar is not effort.** Rows 13 and 14 carry weeks of waiting that are not hours worked: Play background-location review "up to several weeks" [E, feasibility §1.2(e)], the 14-day continuous closed test plus a review "usually… seven days or less" [E, §2.4], and App Review. The CFO models cost; the PM/BA should model the calendar separately, and it is longer than the hours suggest.

### 3.3 What React Native is actually worth, shown rather than asserted

The CEO should be able to see the stack decision's value on its own, separated from the scope additions. Same scope, two stacks:

| | Weeks | Hours |
| --- | --- | --- |
| Two platforms, **native** (Swift + Kotlin), same scope as the table above | 32–42 | 1,200–1,575 |
| Two platforms, **React Native / Expo** (the table above) | 31–40 | 1,163–1,500 |
| **React Native saving** | **≈1.5 weeks** | **≈56 hours (~4%)** |

The native figure replaces row 6 (3.5–4 weeks of shared UI) with two native UI implementations (2.5–3 iOS plus 4–5 Android, per feasibility §6.1 and §6.3, so **+3 to +4 weeks**) and deletes the React-Native-specific overheads spread across rows 1, 7, 9 and 12 (**−2 weeks**: Expo tooling setup, the third implementation in the SQLite contract, the KDF row that native platforms supply for free, and the symbolication obligation).

**React Native saves roughly 4% of a two-platform build, not 50%.** The reason is arithmetic rather than ideological: on *this* product the shared UI is about a tenth of the work, and capture, the venue index, field testing and store policy are the other nine tenths — and none of those are shared. I want that on the record before anyone treats the stack choice as the thing that makes Android affordable. It is not. Nothing makes Android affordable; it is simply worth buying or it is not, and that is a Constitution 5.4 judgement.

**This does not change my recommendation** (§2.7), because a 4% saving is still a saving and the alternative is maintaining two codebases for a decade. It does change what the saving is *for*: React Native is a maintenance-surface decision, not a build-cost decision.

**And for completeness, the iOS-only figures, in case the CEO reverts:**

| | Weeks | Hours |
| --- | --- | --- |
| iOS-only native, **original** feasibility §6.1 scope | 16–19 | 600–713 |
| iOS-only native, **at current scope** (adds merge/sticky/rename, the iOS gap surface, distributed accessibility) | 18–21 | 675–788 |

The first row is what the Skeptic's O2 was measuring, and it reproduces: 600–713 against the CFO's 450 is **+33% to +58%**, exactly as O2 stated. The conversion, not the estimate, was the missing piece.

### 3.4 Annual maintenance and support — and the O11 reconciliation

The Skeptic's O11 found the CFO and I modelling support on incompatible bases. Here is my half of the reconciliation, and I concede the ambiguity was mine: **my "~2 hours/week" was a fixed founder-attention floor, and the CFO's contact-rate model is a variable per-user cost. They are different things and they add. Neither replaces the other.**

**Fixed annual maintenance, two platforms, React Native** [J]:

| Item | Hours/year |
| --- | --- |
| Venue dataset refresh (~0.5 day/month) | 45 |
| iOS annual OS release compatibility | 37.5 |
| Android annual OS release + Play policy churn | 37.5 |
| **Expo SDK / React Native major upgrade** — the recurring tax of this stack choice | 37.5–75 |
| OEM regression chasing (new devices, new vendor battery behaviour) | 30–45 |
| Source-map retention and symbolication upkeep | 7.5 |
| **Total** | **195–247** (point estimate **220**) |

Against the CFO's 180 h/year for both platforms, that is **+8% to +37%**. The gap is mostly the Expo/RN upgrade row, which is a direct and honest cost of the stack the CEO has asked for.

**Support, restated as two components:**

- **Fixed floor: 78 hours/year (1.5 h/week)** [J] — inbox, store and policy churn, reproducing reports, the diagnostic-bundle loop. This exists at ten users and at ten thousand.
- **Variable: keep the CFO's contact-rate basis, with Android amended.** iOS: 5% annual contact rate × 45 min, as the CFO has it. **Android: 12% × 60 min** [J] — because the OEM battery-allowlist case is predictable, recurring, unfixable by us, and conducted blind on a device we do not have. That case does not exist on iOS.

**Note the circularity, because it changes how the CFO should solve it:** variable support scales with sales, and sales are what break-even is solving for. Break-even is a fixed point, not a division. Solving it by assuming a cohort and dividing will understate it.

### 3.5 Two UX disagreements I am accepting, because they are scope and scope is hours

Both are recorded in `ux-note.md` §8 and both are correct.

1. **Merge, sticky choice and rename-in-place are MVP scope, not polish** (UX §2.3, disagreement 1). She is right, and the reason is specifically constitutional: Overture's documented duplicate rate corrupts an accumulated record silently, and with no server there is no repair path. Carried in row 5.
2. **The standalone accessibility week is an audit, not the work** (UX §5.8, disagreement 2). She is right. The standalone line is deleted and the effort distributed into rows 5, 6, 8 and 10, aggregated on row 11 for visibility only. On two platforms the distributed total is larger than the standalone week it replaces, which is the point she was making.

I also accept her disagreement 3 (an always-visible Backup status row instead of a recurring reminder); it changes no hours.

### 3.6 Order of magnitude only — the CFO owns the number

Condition 1 assigns the re-derivation to the CFO and I am not going to pre-empt it. But the CEO asked what this does to break-even and deserves the shape of the answer rather than a referral.

Three-year benchmarked labour, **excluding variable support**, at the CFO's £32.71/hour: build 1,330 + spike 75 + fixed maintenance (220 × 3) + fixed support (78 × 3) = **2,299 hours ≈ £75,200**. At £14.99 inc. VAT the CFO's net-per-sale is £10.62, giving **roughly 7,100 sales over three years** — before variable support, which pushes it up.

The cost sheet currently shows **4,159** at that price for both platforms. **The order of magnitude is therefore around 70% higher than the figure in front of the CEO**, and higher again once §3.4's variable component is solved as the fixed point it is.

Three flags on that indication, all of which cut against treating it as a number:
- It is **[I] from [J] premises, which makes it [J]**. It is an indication, not a price. Constitution 5.4 and Condition 9 both put price with the CEO, after the CFO's work.
- **The £32.71 benchmark is itself unverified** — Condition 5 and the Skeptic's O6 are open, and no cost sheet may be published under Article 3 until the ONS ASHE figure is retrieved at primary.
- **It says nothing about whether Haunt should be built.** The gate already decided PROCEED on a recorded reason that was explicitly not a commercial case. Doubling a build that was never justified commercially does not change the decision's logic; it changes its size. That is the CEO's call and it is the one thing in this note I have no standing to make.

---

## 4. Blocks — restated

**Block 1 (places-API venue records)** — unchanged, still avoided rather than lifted by the zero-network architecture, and it re-engages on any architecture that touches a places API. Adding Android does not touch it.

**Block 2 (Android MVP on undocumented OEM behaviour)** — **now engages**, because Android is back in scope. Restated with one amendment:

*Breach:* Constitution 1.3 and Article 4 — shipping "automatic capture" we know will fail on part of the fleet [E, §1.3e, now corroborated across two independent sources].
*Lifted by:* a published device-matrix spike over ≥2 real weeks on at least a Pixel, a Samsung and a Xiaomi, with a minimum capture rate agreed with PM/BA and QA **before** it runs — **and, new, a measured gap-detection accuracy**, because §1.6 makes the honesty claim rest on knowing when we missed rather than on never missing. A spike showing 80% capture with reliable gap detection lifts this block. One showing 95% capture with silent failures does not.

**New Block 3 — JavaScript in the visit-recording path.** *Breach:* my charter's "unsustainable by design." If recording a visit requires the Hermes runtime to boot, the product's central promise depends on the slowest, least reliable part of the stack at the moment the OS is least willing to give us time. *Lifted by:* a capture design in which the Swift and Kotlin modules write to SQLite directly and JavaScript reads later.

**Not a block: the stack choice.** §2.7 says why, and says what the CEO directing otherwise would be instead.

---

## 5. Open questions this note did not close

| # | Question | Owner | Why it matters |
| --- | --- | --- | --- |
| 1 | Whether Google Play services is in fact exempt from background location limits and OEM battery managers | Skeptic / unresolved | My §1.2 inference is the weakest claim in this note. It no longer decides anything (§1.3 does), but it should not be repeated as fact. |
| 2 | **Install DayTrace.** Its Play listing would not retrieve; my strongest counter-example is currently single-source and secondary | Skeptic | Same defect Condition 3 identified for Arc. It is £0 and it is the closest thing to a live prototype of Haunt's Android build. |
| 3 | R-Tree availability in `expo-sqlite`, or confirmation that the grid-cell approach is sufficient | Engineer, 1-day spike | Cheap; decides a schema detail before it is expensive |
| 4 | Which KDF, at which parameters, from which dependency | **CSO**, before crypto is written | Security-critical, and `expo-crypto` does not supply one [E] |
| 5 | Measured battery cost of `CLVisit` on iOS **and** of the Android foreground service | Engineer, in the spike and field-test rows | No vendor-independent figure exists for either; no marketing claim until both land (Article 1.3) |
| 6 | Whether React Native accessibility can meet the UX seat's per-feature criteria on both platforms | **UX**, at requirements | A cost of the stack decision that lands in her seat, not mine |
| 7 | Google Play's US$25 registration fee, confirmed at Google rather than from a secondary source | CFO, at signup | Small, but it is on the cost sheet |
| 8 | Whether twelve testers can be recruited for fourteen days (§2.4) | CEO / CVO | The Skeptic has repeatedly found reach to be the binding constraint. This is the cheapest available test of it, and it is now mandatory anyway. |

---

## 6. Evidence register

Every link below was retrieved on **2026-09-16** during the session that produced this note. Nothing is cited from memory. Sources carried over from `feasibility-note.md` are cited there with their own retrieval date of 2026-09-09 and are not repeated.

**Google Maps Timeline**
- [Google — Manage your Google Maps Timeline (Android)](https://support.google.com/maps/answer/6258979?hl=en&co=GENIE.Platform%3DAndroid) — "automatically saving your visits and routes"; "regularly saving each of your devices' precise locations to that device… including when Google apps aren't open". Google publishes the outcome, not the mechanism.

**Third-party Android visit/stay detection — shipped products**
- [DayTrace — listing](https://www.alternativeto.net/software/daytrace--gps-and-timeline/about/) — Android; "places you stay"; "fully offline"; "lightweight foreground service" *(single source, secondary — the Play listing would not retrieve; flagged, see §5 q.2)*
- [GPS Logger (northforceapps)](https://northforceapps.com/gpslogger/) — foreground service, persistent notification, motion-adaptive sampling, daily timeline of stops, on-device data

**Third-party Android visit detection — commercial SDKs**
- [Foursquare — Movement SDK FAQs](https://docs.foursquare.com/developer/docs/movement-sdk-faqs) — stop detection and dwell time; sensor list; "<0.5% of daily battery" *(vendor claim, unqualified)*; idle while stationary
- [Foursquare — Movement SDK overview](https://docs.foursquare.com/developer/docs/movement-sdk-overview)
- [Radar — Android SDK](https://docs.radar.com/sdk/android) — RESPONSIVE / CONTINUOUS presets; only CONTINUOUS needs a foreground service; works "even if the app has been backgrounded or killed"; JobScheduler; and the honest caveat on Doze, App Standby and Background Location Limits
- [Sentiance — Android battery optimization](https://docs.sentiance.com/sdk/appendix/android/android-battery-optimization.md) — OnePlus and Nokia/HMD named; Adaptive Battery bucketing "can impact the detection quality"; `disableBatteryOptimization()`; quotes the Play prohibition. *Independent corroboration of the OEM finding, previously single-source.*
- [dontkillmyapp.com](https://dontkillmyapp.com/) — OEM allowlisting of "associate apps" *(single source, community-maintained)*

**Android platform**
- [Android — Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits) — "only a few times each hour", "regardless of an app's target SDK version"; **batched FLP gives "more time-frequent location history"**; foreground-service and Android 11 `ACCESS_BACKGROUND_LOCATION` rules
- [Android — Foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types) — `location` type: manifest declaration, `FOREGROUND_SERVICE_LOCATION`, runtime permissions, Android 14 requirement, background-start restriction
- [Android — Detect when users start or end an activity](https://developer.android.com/develop/sensors-and-location/location/transitions) — Activity Recognition Transition API; `PendingIntent` delivery; Play services 12.0.0+; device-varying latency
- [Play Console — Get ready to publish / production access](https://support.google.com/googleplay/android-developer/answer/14151465) — "a minimum of 12 testers who have been opted in continuously for at least 14 days"; three-part application; review "usually… seven days or less"
- [ConsoleMint — Google Play Console price](https://consolemint.com/google-play-console-price/) — US$25 one-off registration fee *(secondary source, flagged; confirm at signup)*

**React Native, Expo and EAS**
- [Expo — Location SDK reference](https://docs.expo.dev/versions/latest/sdk/location/) — `startLocationUpdatesAsync`, `startGeofencingAsync`, `ActivityType`, `Accuracy`; **no `CLVisit` / `startMonitoringVisits` / visit monitoring**
- [Expo — SQLite](https://docs.expo.dev/versions/latest/sdk/sqlite/) — `openDatabaseSync`/`Async`; `SQLiteProvider` `assetSource` for a pre-populated `.db`; `enableFTS` defaults true (FTS3/4/5); `customBuildFlags`
- [Expo — Crypto](https://docs.expo.dev/versions/latest/sdk/crypto/) — AES encrypt/decrypt, `AESEncryptionKey`, random bytes, digests; **no KDF**
- [Expo — Get started with modules](https://docs.expo.dev/modules/get-started/) — `npx create-expo-module@latest --local`; Swift and Kotlin; `npx expo prebuild --clean` required
- [Expo — Pricing](https://expo.dev/pricing) — Free: $0, "15 Android and 15 iOS builds", low-priority queue, EAS Submit included; Starter $19/month + usage
- [React Native — Symbolicating a stack trace](https://reactnative.dev/docs/symbolication) — "Source maps are required to symbolicate stack traces"; obfuscated Hermes example
- [react-native-cloud-store — Install with Expo](https://react-native-cloud-store.vercel.app/docs/install/with-expo) — community iCloud Drive module *(single source)*

**Apple**
- [Apple — Maximum build file sizes](https://developer.apple.com/help/app-store-connect/reference/maximum-build-file-sizes/) — 4 GB uncompressed for iOS 9.0+

---

## Change log

- **2026-09-16** — created. Amends `feasibility-note.md` §1.2 (four corrections, §1.4 of this note), §1.3 (verdict reversed), §1.4 (disagreement withdrawn in part), §4.2 (iCloud dependency, §2.5 of this note), §5 Layer 1 (symbolication, §2.3), §6.1 and §6.3 (superseded by §3 of this note), and §7 (Block 2 amended, Block 3 added).

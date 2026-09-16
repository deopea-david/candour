# Feasibility note — Haunt

**Seat:** Chief Technology Officer · **Date:** 2026-09-09 · **Commissioned by:** CVO, 2026-09-09
**Input artifact:** `/Users/davidparrish/Documents/candour/proposals/haunt/idea-brief.md`
**Status:** discovery artifact. Feeds the CFO cost model and the gate pack. **Prepares, does not certify** (Constitution 6.1).
**Evidence:** every substantive claim tagged per `pipeline/evidence-standard.md`. All [E] sources were retrieved on 2026-09-09 during this session; links travel with the claims and are repeated in the register at the end.

---

## 0. Summary — five findings and one recommendation

1. **Android does not ship at MVP.** Not because Android is hard, but because the specific thing Haunt needs — the OS telling an app "the user has been sitting somewhere for a while" — has no supported first-party equivalent on Android, and the nearest thing Google ever shipped is deprecated with shutdown as early as January 2027 and no replacement [E]. Ship iOS first. §1.
2. **The venue-naming question is already settled by licence, not by preference.** Google's terms permit permanent storage of a `place_id` and nothing else; venue names are Google Maps Content and "Customer will not cache Google Maps Content except as expressly permitted" [E]. Foursquare's paid API is the same shape [E]. A journal that keeps a venue record forever cannot be built on either. §2.
3. **The offline dataset is small — and I measured it, not guessed it.** A UK food-and-drink venue index built from Overture Places release 2026-08-19.0 is **346,184 venues, 21.3 MB as an indexed SQLite file, 10.8 MB compressed** [E, measured this session]. The idea brief assumed the zero-network variant carried "materially higher build cost." On the evidence, it does not. §2.4, §6.
4. **The online variant is the expensive one.** Google Places Nearby Search is $32.00 per 1,000 calls above a 5,000/month free tier [E]. At 5,000 monthly-active users and 12 confirmed visits each, that is roughly **$1,760/month** — against a product whose whole cost-sheet pitch is "no server, no running cost." It also eats a one-off purchase price inside about a year. §2.5. **CFO: this is the number that decides the pricing question.**
5. **Diagnosis without telemetry is a solved problem, and it is free.** Apple and Google both operate platform-mediated, user-opt-in crash reporting that requires no SDK and sends Candour nothing the user has not already agreed to share with the platform [E]. Add a user-initiated, user-readable diagnostic export and the promise holds without a blind spot. §5.

**Recommendation in one line:** build **iOS-only, zero-network, bundled Overture-derived venue index, SQLite store, user-passphrase-encrypted backup to iCloud** — and drop the online places API from the architecture entirely rather than shipping it and retrofitting later.

---

## 1. Background visit detection on both platforms

### 1.1 iOS — a first-class API exists and it is the right one

`CLLocationManager.startMonitoringVisits()` is current, not deprecated, available since iOS 8 [E — [Apple, startMonitoringVisits()](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits())]. It delivers `CLVisit` objects carrying `coordinate`, `horizontalAccuracy`, `arrivalDate` and `departureDate` [E — [Apple, CLVisit](https://developer.apple.com/documentation/corelocation/clvisit)]. That is, almost exactly, the record Haunt wants: a place, a time in, a time out.

Two properties make it decisive for this product:

- **Relaunch after termination.** "If your app is terminated while this service is active, the system relaunches your app when new visit events are ready to be delivered" [E, quoted verbatim — [Apple](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits())]. The app does not need to stay resident, does not need a persistent notification, and does not need to fight the scheduler.
- **Power.** Apple's own energy guidance ranks it: "Region and visit monitoring are sufficient for most use cases and should always be considered before significant-change location updates," and warns that significant-change updates "run continuously, around the clock… and can actually result in higher energy use if not employed effectively" [E — [Apple, Energy Efficiency Guide — Location Best Practices](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/LocationBestPractices.html)]. Visit monitoring is at the cheap end of the ladder Apple publishes.

Apple publishes no milliampere figure for visit monitoring, so I will not invent one. **The battery cost must be measured, not asserted, before any marketing claim is made about it** [J]. Budget a two-week field measurement inside the build (§6) and hold the marketing copy until it lands — Article 1.3 forbids the claim we cannot substantiate.

**Three real constraints on iOS, all of which change the UX rather than the feasibility:**

- **`Always` authorization is required, and it arrives in two prompts.** The app must request When-In-Use first, then Always. If it requests Always directly, the system shows a second prompt later, "typically… when your app isn't running," and only then grants permanent Always [E, quoted — [Apple, requestAlwaysAuthorization()](https://developer.apple.com/documentation/corelocation/cllocationmanager/requestalwaysauthorization())]. **The user can decline that second prompt while Haunt is not on screen, and background capture stops silently** [I, from the above]. The app must detect the authorization downgrade and say so plainly on the timeline — "capture is off, here is why" — rather than presenting an empty week as if nothing happened. This is an Article 4 dark-pattern-adjacent honesty requirement, not a nicety.
- **Reduced accuracy is permitted and usable.** "Your app can monitor for visit events without calling `requestTemporaryPreciseLocationAuthorization`… the visit events use reduced accuracy" [E, quoted — Apple, as above]. Haunt should work, degraded, for users who refuse precise location. Design the venue-confirm step to widen its candidate radius from `horizontalAccuracy` rather than assuming a tight fix.
- **Visits arrive incomplete.** "Visit objects contain as much information about the visit as possible but may not always include both the arrival and departure times" [E, quoted — [Apple, CLVisit](https://developer.apple.com/documentation/corelocation/clvisit)]. The confirm queue must handle an open-ended visit and let the user close it.

### 1.2 Android — the API Haunt needs does not exist

I looked for the equivalent. There isn't one, and the gap is structural rather than a matter of effort.

**a) The closest thing Google built is being switched off.** The Awareness API's Fence API could fire callbacks on combined context conditions "even when the app wasn't actively running." Its documentation now carries: "Google Play services will stop supporting the Awareness API in a future release, as early as January 2027," and "There is no direct replacement" [E, quoted — [Google, Awareness API overview](https://developers.google.com/awareness/overview)]. Building Haunt's Android capture layer on it in 2026 would be building on a scheduled demolition.

**b) Geofencing solves the opposite problem.** Geofences are pre-registered, capped at "100 per app, per device user," and support a `DWELL` transition with a loitering delay [E — [Android, Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing)]. That is excellent for *"tell me when I reach the places I already told you about."* Haunt's problem is the reverse: it must notice the user has settled somewhere **it does not know about yet**. You cannot pre-fence the unknown. Geofencing is not a substitute [I].

**c) Without a foreground service, background location is throttled by design.** "Android preserves device battery life by setting background location limits… if your app is running in the background, it can receive location updates only a few times each hour," and this "appl[ies] to all apps… regardless of an app's target SDK version" [E, quoted — [Android, Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits)]. A few fixes an hour is arguably enough to *infer* a two-hour dinner [J, moderate confidence] but not enough to bound arrival and departure well, and the inference has to be written and tuned by hand — the work iOS gives away.

**d) With a foreground service, the product stops being invisible.** A location foreground service means a persistent notification, an Android 14 foreground-service-type declaration in the manifest **and** a Play Console declaration with a demonstration video per type [E — [Android, Foreground service types are required](https://developer.android.com/about/versions/14/changes/fgs-types-required); [Play Console, foreground service requirements](https://support.google.com/googleplay/android-developer/answer/13392821)]. A journal that runs a permanent notification bar item to remember your dinners is a worse product than one that doesn't.

**e) The Play gate is a real gate with a real cost.** `ACCESS_BACKGROUND_LOCATION` requires a Permissions Declaration Form, a prominent in-app disclosure, and "a video demonstration (≤30 seconds)"; "Background location may only be used when it provides a significant benefit to users and is relevant to the core functionality of the app"; approval takes "up to several weeks"; and without it "app updates may be blocked and your app may be removed from Google Play" [E, quoted — [Play Console, Understanding location in the background permissions](https://support.google.com/googleplay/android-developer/answer/9799150)]. A solo operator with no server has no way to route around a rejection or a multi-week review sitting between a bug fix and its users [J].

**f) OEM battery management will break it on most of the installed base, and Play forbids the standard workaround.** Vendors that aggressively kill background work are rated 5/5 for Huawei, Xiaomi, OnePlus and Samsung, and 4/5 for Oppo, Asus and Meizu, with only AOSP/Pixel/Nokia/HTC rated clean [E, single source — [dontkillmyapp.com](https://dontkillmyapp.com/); this is a community-maintained list, treat the ratings as directional and the vendor list as reliable]. The obvious mitigation is a battery-optimisation exemption. It is not available to this product: "Google Play policies prohibit apps from requesting direct exemption from Power Management features—Doze and App Standby—in Android 6.0 and above unless the core function of the app is adversely affected," and the published acceptable-use table covers messaging/calling, safety, task automation and peripheral companion apps — a location journal is on none of those rows [E, quoted — [Android, Optimize for Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby)]. Doze itself "suspends network access, ignores wake locks… doesn't let `JobScheduler` run" [E, same source].

**g) What Android *does* give you.** Honesty demands stating the buildable path rather than declaring defeat. The Activity Recognition Transition API detects `STILL`/`WALKING`/`IN_VEHICLE` enter and exit transitions via a `PendingIntent`, needs `com.google.android.gms.permission.ACTIVITY_RECOGNITION`, and warns only that "the latency of event detection might vary by device" [E — [Android, Detect when users start or end an activity](https://developer.android.com/develop/sensors-and-location/location/transitions)]. A workable Android design is: on `STILL` enter, request throttled fused-location fixes; cluster; on `STILL` exit, close the candidate visit. That is a hand-built version of what `CLVisit` gives free — plus per-device tuning, plus a device matrix, plus a Play review, plus a support inbox for the phones where the OEM killed it anyway [J].

### 1.3 Recommendation, with the reason

> **Android does not ship at MVP. Ship iOS-only, and change the promise now rather than later.**

The reason is not "Android is more work." It is that **on iOS the OS makes the product's central promise and on Android the developer does**. iOS guarantees relaunch-on-visit and publishes visit monitoring as a low-power service. Android offers a deprecated API, a pre-registration API that solves a different problem, a throttle, a notification-bar tax, a multi-week policy gate, and a fleet of vendors who will silently kill the capture while explicitly forbidding the standard exemption. Haunt's value proposition is *"it remembers so you don't have to."* A capture layer that works on Pixel and fails quietly on a Xiaomi is not a lesser version of that promise — it is the opposite of it, and with no server there is no way to detect the failure or fix it remotely.

**The honest cost of this recommendation, stated plainly:** UK mobile OS share is iOS 51.47% / Android 48.51% (August 2026) [E, single source — [StatCounter, UK mobile OS share](https://gs.statcounter.com/os-market-share/mobile/united-kingdom)]. iOS-first forfeits roughly half the addressable UK market at launch. That is a real price and it is the **CEO's** decision to pay it, not mine (Constitution 5.4). What I am saying is that the alternative is not "half the market later" — it is *shipping a promise on Android we cannot substantiate*, which Article 1.3 forbids.

**Sequenced path for Android, if the CEO wants it:** a separately-gated phase, opened by a published **two-week device-matrix spike** measuring actual capture rates on at least a Pixel, a Samsung and a Xiaomi over real weeks, before a line of product code is written. Ship Android only if the spike shows capture rates a user would recognise as "automatic."

### 1.4 Disagreement on the record (Constitution: dissent is a deliverable)

The idea brief records the scope decision: *"Both iOS and Android are in scope of the promise."* I am putting a disagreement in writing, once, now.

**Being in scope of an *intention* is fine. Being in scope of a *promise* is not, and the word matters under Article 1.3.** Candour cannot substantiate reliable automatic capture on Android today, and on this evidence will not be able to for the foreseeable OEM fleet. I ask the CVO and CEO to restate the platform line as: **"iOS at launch. Android is an intention, gated on a published spike, and we will not claim it until it works."** Marketing "coming to Android" before the spike would be a claim we cannot substantiate, which Article 4 lists as prohibited without qualification.

---

## 2. Venue naming: online lookup vs bundled dataset

### 2.1 The licence question is not a footnote — it is the architecture

The idea brief flagged this as `[K, medium confidence, must be verified]`. It is verified, and it is worse than the brief feared.

**Google Maps Platform, General Service Terms:** *"Google ID Caching. Customer may cache the Google ID values from the Services that return such field and allow caching… For example, Customer may cache (a) `place_id` from Places API…"* [E, verbatim — [Google Maps Platform Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms), section A.3].

**Places API-specific:** *"14.3 Caching. Customer may temporarily cache latitude and longitude values from the Places API for up to 30 consecutive calendar days, after which Customer must delete the cached latitude and longitude values."* [E, verbatim — same source, section 14.3].

**General prohibition:** *"No Caching. Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms."* [E, verbatim — [Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms), section 3.2.3(b)].

**Developer documentation, in plain English:** *"You must not pre-fetch, cache, or store Places API content beyond the allowed exceptions, although the `place_id` is exempt from caching restrictions"*, and *"The place ID… is exempt from the caching restrictions. You can therefore store place ID values indefinitely."* [E, verbatim — [Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies)].

**What that means for a journal, concretely** [I, from the four [E] quotes above]:

| Field the journal needs | Permitted permanent storage? |
| --- | --- |
| `place_id` | Yes, indefinitely |
| Venue **name** | **No** — it is Google Maps Content and no exception permits it |
| Latitude / longitude | 30 days, then must be deleted |
| Category, address, hours | No |

A five-year-old entry that reads *"The Crown, 12 March 2021"* would therefore have to be reconstituted by re-querying Place Details against the stored `place_id` **every time the user scrolls their own timeline**. That is (a) a network dependency in the middle of reading your own diary, (b) a per-view API bill, (c) broken offline and broken forever if the app is discontinued (Article 7.2 requires the export to keep working for 90 days after shutdown — a journal of opaque `place_id` strings does not satisfy that), and (d) it fails outright when Google retires a place ID.

**Two further Google clauses worth the gate's attention:**
- *"No Use with a non-Google map. Customer must not use Google Maps Content from the Places API in conjunction with a non-Google map."* [E, verbatim, section 14.2] — this constrains any future map view.
- *"No Re-Creating Google Products or Features. Customer will not use the Services to create a product or service with features that are substantially similar to or that re-create the features of another Google product or service."* [E, verbatim, section 3.2.3(d)]. Haunt is a private timeline of visited places. Google Maps Timeline is a private timeline of visited places. I am not a lawyer and this is not a legal opinion (Constitution 6.1), but **an architecture whose defensibility depends on a favourable reading of that clause by the counterparty is not an architecture I will sign off** [J].

**Foursquare's paid API is the same shape:** pay-as-you-go accounts may cache `fsq_place_id`, photo IDs and address IDs indefinitely — names, categories, hours and ratings may not be retained [E, single source, secondary — [Foursquare Places API pricing/terms analysis](https://openplacesapi.com/compare/foursquare-places-api); Foursquare's own [Usage Guidelines](https://docs.foursquare.com/docs/usage-guidelines) and [API License Agreement](https://foursquare.com/legal/terms/apilicenseagreement/) are the primary sources and **should be verified by the Skeptic at the gate** if any online-API route survives].

**The one paid route that does permit permanent storage** is Mapbox Permanent Geocoding: temporary geocoding results are "intended for use during the current user session only" and "you cannot store the coordinate results for future use", while the permanent endpoint means "you can store coordinate results in databases or local storage" [E, verbatim — [Mapbox, Temporary vs Permanent Geocoding](https://docs.mapbox.com/help/dive-deeper/understand-temporary-vs-permanent-geocoding/)], priced at $5 per 1,000 requests with no free tier [E, single source, secondary — search-result summary of Mapbox pricing; **flagged as unverified against Mapbox's own pricing page**]. It is a legitimate option. It is also a per-user recurring network dependency in the core loop, for a product whose selling point is that the core loop needs no network.

### 2.2 The open datasets, and their licences

| Dataset | Licence | Permanent local storage & redistribution? |
| --- | --- | --- |
| **Overture Maps — Places theme** | CDLA Permissive 2.0 | Yes. Attribution required. No share-alike. [E — [Overture attribution & licensing](https://docs.overturemaps.org/attribution/)] |
| **Foursquare OS Places** | Apache 2.0 | Yes. Preserve `NOTICE.txt`, note modifications. [E — [Foursquare OS Places notice](https://opensource.foursquare.com/places-notice-txt/)] |
| **OpenStreetMap** | ODbL 1.0 | Yes, but **share-alike**: a derived database must be offered under ODbL. [E — ODbL notice returned with the Overpass response below] |

Overture's Places theme carries CDLA Permissive 2.0 and is fed by Meta, Microsoft, PinMeTo, Krick, RenderSEO, DAC, BrightQuery, Foursquare (Apache 2.0) and AllThePlaces (CC0); notably **"The places theme does not include OpenStreetMap data"** [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/)]. Four other Overture themes (base, buildings, divisions, transportation) *are* ODbL [E, same source] — so the rule for Haunt is **use the Places theme only**; pulling in an ODbL theme drags a share-alike obligation onto the bundled database.

**This is the decisive licence difference.** CDLA-Permissive-2.0 and Apache-2.0 both permit shipping a derived venue index inside a closed-source app with attribution. ODbL would work too but obliges Candour to publish the derived database under ODbL — survivable, arguably even *welcome* under Article 8's open-source preference, but it is a commitment the gate should make knowingly rather than inherit by accident.

### 2.3 UK coverage — measured, not assumed

I retrieved counts rather than reasoning about them.

**OpenStreetMap, United Kingdom, via Overpass API, 2026-09-09** [E, measured this session; source data © OpenStreetMap contributors, ODbL; endpoint `https://overpass-api.de/api/interpreter`, data timestamp `2026-09-09T21:05:56Z`]:

| `amenity` | Count |
| --- | --- |
| pub | 38,555 |
| fast_food | 45,928 |
| cafe | 39,879 |
| restaurant | 37,253 |
| bar | 7,424 |
| nightclub | 1,094 |
| **Combined (incl. biergarten)** | **170,256** |

**Overture Places release `2026-08-19.0`, UK bounding box (−8.65,49.86 → 1.77,60.86), via DuckDB over the public S3 bucket** [E, measured this session]:

| Measure | Count |
| --- | --- |
| All places in UK bbox | 3,325,607 |
| Named, confidence ≥ 0.5 | 2,900,349 |
| Food-and-drink category match | 346,184 |
| — of which `pub` | 42,407 |
| — of which `cafe` | 33,215 |
| — of which `restaurant` (generic leaf only) | 22,886 |
| — of which `coffee_shop` | 19,875 |

**Reality check against an independent trade source:** Britain had **98,914 licensed premises** at December 2025, of which 35,534 food-led and 4,721 bars, per CGA by NIQ's Hospitality Market Monitor [E, single source, secondary — [The Spirits Business](https://www.thespiritsbusiness.com/2026/01/new-openings-boost-bar-numbers-in-britain/), [Morning Advertiser](https://www.morningadvertiser.co.uk/Article/2025/10/21/uk-licensed-premises-fall-by-572-amid-tough-hospitality-climate/); the underlying CGA report is paywalled and was not retrieved].

OSM's pub + bar + nightclub + restaurant total is 84,326 against a licensed-premises universe of ~99,000, and Overture's food-and-drink match is 346,184 across a broader category set [I]. **Neither open dataset looks materially deficient for UK "going out."** The idea brief's assumption that an offline dataset means "worse coverage" is not supported for this market and this category.

**The honest caveat, in Overture's own words:** *"Places is known to contain duplicates, a high junk rate, and low property completeness"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/)]. Overture ships a 0–1 `confidence` score as the intended filter. Data-quality work — dedupe, confidence thresholding, category mapping to labels a UK user recognises — is real build cost and is priced in §6. It is also *bounded and one-off*, unlike an API bill.

### 2.4 Bundle size — measured, not assumed

I built the candidate artefact and weighed it [E, measured this session]:

| Artefact (346,184 UK food-and-drink venues: name, category, lat/lon @ 1e-5) | Size |
| --- | --- |
| Trimmed Parquet, zstd-19 | **3.6 MB** |
| **SQLite, indexed on (lat, lon)** | **21.3 MB** |
| Same SQLite, gzipped (≈ App Store transfer size) | **10.8 MB** |
| *For comparison:* all 2.9M named UK places, zstd Parquet | 119.8 MB |

**~21 MB on disk, ~11 MB over the wire, for every pub, bar, restaurant, café and nightclub in the United Kingdom.** That is a rounding error against a modern app download. The "bundle size" objection to the offline variant does not survive measurement.

Design consequence [J]: bundle the **food-and-drink subset** in the binary; offer the full 2.9M-place index as an optional in-app download for users who want to log the gym and the barber. Ship UK only at launch and add territories as datasets, not as code.

### 2.5 Cost — the comparison the CFO needs

Google Maps Platform, retrieved 2026-09-09 [E — [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing)]:

- Places API **Nearby Search (Pro)**: 5,000 free events/month, then **$32.00 per 1,000** up to 100K.
- Places API **Place Details (Essentials)**: 10,000 free/month, then **$5.00 per 1,000**.

Modelling one Nearby Search per candidate visit and 12 confirmed visits per active user per month [J, assumption — the CFO should substitute a researched figure]:

| Monthly active users | Lookups/month | Billable | Monthly bill | Per user / month |
| --- | --- | --- | --- | --- |
| 100 | 1,200 | 0 | **$0** | $0 |
| 1,000 | 12,000 | 7,000 | **$224** | $0.22 |
| 5,000 | 60,000 | 55,000 | **$1,760** | $0.35 |
| 10,000 | 120,000 | 115,000 | **$3,680** | $0.37 |

Arithmetic, not evidence — but the inputs are [E] and the conclusion is stark. **At ~$0.37/user/month, a one-off purchase is consumed by the API bill inside roughly a year of use**, and re-querying place details on every timeline view (which §2.1 shows the terms *require*) multiplies it further. The idea brief's cost-sheet story — *"the cost sheet is founder labour, an App Store cut, and a venue-lookup API bill, and nothing else"* — is right about the line items and wrong about their size. The venue-lookup line is the whole cost sheet.

**Offline variant running cost:** Apple Developer Program $99/year; Google Play $25 one-off (if/when Android ships); dataset refresh delivered inside app updates, so **£0 marginal cost per user, at 10 users and at 10,000** [I]. This is the Constitution 1.5 answer, and it is the answer that lets the CFO model a one-off price honestly under Article 2.1.

### 2.6 Recommendation

> **Bundle an offline venue index derived from Overture Places (CDLA-Permissive-2.0), Places theme only. No places API in the MVP.**

Rationale, ranked: (1) the online route cannot legally hold the record the product exists to hold; (2) the offline route is 21 MB and free where the online route is $1,760/month at modest scale; (3) it makes the marketing claim *fully* true — nothing leaves the device, no caveat, no privacy-boundary explainer to design — which removes the "honesty problem" the idea brief identified as needing solving first; (4) it works on the Tube, in a basement bar, and on a phone in aeroplane mode, which is where a night out actually happens [J].

The MVP still needs a **"this venue isn't listed" path** — a user-entered name, stored locally, never uploaded. That is a required feature, not a fallback: it is what converts a dataset gap from a bug into a shrug [J].

---

## 3. The local store and its export

Article 4 requires export "in a usable, machine-readable format, available at any time, at no charge and with no penalty." UK GDPR Article 20 uses "a structured, commonly used and machine-readable format" [E — [Article 20 GDPR](https://gdpr-info.eu/art-20-gdpr/)]. This costs almost nothing if decided now and a great deal if retrofitted, because the expensive part is not the exporter — it is having a schema worth exporting.

**Storage: SQLite.** One file, ACID, on every platform, readable in 30 years, no licence, no vendor. On iOS use GRDB or the C API directly rather than Core Data, because Core Data's store is an implementation detail Apple may change and its schema is not a thing a stranger can read [J]. Protect the file with iOS Data Protection class `NSFileProtectionCompleteUntilFirstUserAuthentication` (or `Complete` if background writes allow) rather than rolling application-layer encryption for data already at rest behind the device passcode [J — CSO to confirm at threat-model stage].

**The rule that makes export nearly free:** *the export format is the schema, and the schema is designed to be exported.* Three commitments taken now:

1. **Venue identity is a Candour-owned local row**, carrying the venue name as text, plus the upstream identifier (Overture GERS ID) as an *attribute*, never as the only handle. If the dataset changes, the journal survives.
2. **No opaque blobs.** Notes are text, ratings are numbers, timestamps are ISO-8601 with an explicit offset. Nothing in the store requires Haunt to interpret it.
3. **The export is a lossless dump of the store, not a report.** Every user-authored field round-trips.

**Export format: a single `.zip` containing**
- `haunt-export.json` — JSON Lines or a single JSON document; the canonical, complete, round-trippable form. Documented schema published alongside the app.
- `visits.csv`, `venues.csv` — flat, spreadsheet-openable. Article 4 says *usable*; a JSON file is machine-readable but is not what a non-technical user means by "my data."
- `README.txt` — plain-English field descriptions and the dataset attribution notice.
- Optionally `haunt.gpx` for the location spine, since GPX is the boring interchange format for exactly this [J].

**Import of the same archive must ship at MVP.** Export without import is a gesture; export *with* import is what makes leaving genuinely free, and it is also the restore path for §4 and the migration path for a future Android build. One serialiser, three jobs.

**Cost of doing this now vs later** [J, high confidence]: roughly 3–5 days as part of the initial data-layer work. Retrofitting a documented, round-trippable export onto a Core Data model designed for a UI is a multi-week job that usually ends in a lossy exporter nobody trusts.

---

## 4. Opt-in encrypted backup to the user's own cloud

**The constraint from the idea brief: Candour holds no key and no data at any tier.** That constraint is satisfiable, and the way to satisfy it is to *stop depending on platform E2EE claims altogether*.

### 4.1 What the platforms actually give you

**iOS / CloudKit.** A CloudKit private database is available at no cost to Candour, and `CKRecord.encryptedValues` encrypts field values on-device before upload [E — corroborated across [Apple Platform Security: iCloud encryption](https://support.apple.com/en-gb/guide/security/sec3cac31735/web) and [WWDC21 "What's new in CloudKit"](https://developer.apple.com/videos/play/wwdc2021/10086/)]. But the E2EE guarantee is conditional: Apple's own data-security overview says *"Third-party app data stored in iCloud is always encrypted in transit and on server,"* and that **under Advanced Data Protection** *"third-party app data stored in iCloud Backup and CloudKit encrypted fields and assets are end-to-end encrypted"* [E, verbatim — [Apple, iCloud data security overview](https://support.apple.com/en-gb/102651)]. For end-to-end encrypted services, *"the relevant CloudKit service private keys are never made available to Apple servers"* [E, verbatim — Apple Platform Security, as above].

**Read that carefully.** For a user who has **not** turned on Advanced Data Protection — the default — Apple holds keys capable of decrypting the container. That is *nominal* E2EE, not real E2EE. Candour would still hold nothing, so the letter of the promise survives; the spirit does not, and Article 1.3 says we describe capability plainly.

**Android.** Two viable routes:
- **Auto Backup for Apps**: 25 MB per app, to a private folder in the user's Drive that does not count against their quota, nightly on Wi-Fi when idle, only the most recent backup retained, and *"end-to-end encrypted on devices running Android 9 or higher using the device's PIN, pattern, or password"* [E, verbatim — [Android, Back up user data with Auto Backup](https://developer.android.com/identity/data/autobackup)]. Free, zero UI, genuinely E2EE where a screen lock is set — but 25 MB is a hard ceiling and the app cannot read or verify its own backup.
- **Google Drive `appDataFolder`**: a hidden per-app folder via the `drive.appdata` OAuth scope, which Google classifies as a **non-sensitive** scope requiring only basic OAuth verification [E — [Drive appDataFolder guide](https://developers.google.com/workspace/drive/api/guides/appdata); [Choose Drive API scopes](https://developers.google.com/workspace/drive/api/guides/api-specific-auth)]. No size ceiling of consequence, app-controlled, and the OAuth-verification burden is the light one — a material finding for a solo operator. Google can read what is stored there unless Candour encrypts it first.

### 4.2 The design that makes the promise true on both platforms

> **Encrypt in the app, with a key the user holds, and treat the cloud as dumb storage.**

1. On enabling backup, generate a random 256-bit data key. Wrap it with a key derived from a **user passphrase** (Argon2id or scrypt; parameters set with the CSO).
2. Store the passphrase-derived material in the platform keychain (iOS Keychain with `WhenUnlockedThisDeviceOnly`; Android Keystore) so day-to-day use needs no typing.
3. Present the user with a **printable recovery code** at setup — the only way back in on a new device. Make them acknowledge it in a way that is honest and not a dark pattern: a plain statement, not a scare modal, not a pre-ticked box (Article 4).
4. Encrypt the export archive from §3 with AES-256-GCM (or the platform's authenticated-encryption primitive) and upload the **ciphertext**: CloudKit private DB (also using `encryptedValues`, belt and braces) on iOS; `appDataFolder` on Android, with Auto Backup as a zero-config fallback for stores under 25 MB.

**Why this is the right answer:** it makes "Candour holds no key and no data" true *by construction* rather than by relying on Apple's or Google's tiering. It is identical on both platforms, so one crypto implementation serves both. It works with a plain **"Save encrypted backup to Files/Drive/anywhere"** button as a third option — a user-chosen file the user controls entirely, which is also the Article 7.2 discontinuation path. And the ciphertext is the same archive as the Article 4 export, so §3 and §4 share one code path.

**What the user loses if they lose the key.** Everything in the backup. There is no recovery, there is no reset link, and Candour cannot help — that is what "no Candour-held key" means. **This must be stated in the app at the moment of setup, in the plainest possible words, and repeated in the marketing copy** [J]. Selling absolute privacy while burying the irreversibility of key loss in a help page would itself be the "deliberately buried settings" dark pattern Article 4 prohibits. Mitigations that do not weaken the promise: the local store remains intact and unencrypted-at-app-level on the original device (losing the backup key does not lose the journal, only the backup); the plain export in §3 always remains available; and a periodic, dismissible reminder to check the recovery code is stored somewhere real.

**Backup is opt-in and off by default.** Nothing leaves the device until the user chooses it, and the choice screen says exactly what leaves and in what form.

---

## 5. Diagnosis without telemetry

This is the question the idea brief asked to be priced rather than admired. Priced: **it is cheaper than the alternative, and it is a marketing asset.** Three layers, none of which sends Candour anything the user has not personally handed over.

**Layer 1 — platform-mediated crash reporting (free, no SDK, already opt-in).**

- **iOS:** *"TestFlight and the App Store collect crash reports for every submitted version of your app… The Crashes organizer presents crash reports from customers who share diagnostic and usage information"* [E, verbatim — [Apple, Acquiring crash reports and diagnostic logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs)]. Apple collects it, the user has already consented at OS level, Candour ships no telemetry code and integrates no third party. Known gaps, stated by Apple: watchdog events, invalid-code-signature crashes, thermal events and Jetsam (high-memory) events are not in the organizer [E, same source] — and Jetsam matters for a background-location app, so that gap must be covered by Layer 3.
- **Android (when it ships):** *"Data is collected from users who have opted in to automatically share usage and diagnostics data from a subset of Android devices and OS versions"*, and Android vitals *"exclude technical issues that occur on uncertified device models, or on versions of your app that were not installed through Google Play"* [E, verbatim — [Play Console, Android vitals](https://support.google.com/googleplay/android-developer/answer/7385505)]. Note the second clause quietly re-states §1.2(f): the OEM-modified fleet most likely to break Haunt is partly the fleet least likely to report it.

**Layer 2 — MetricKit, on-device, opt-in to share.** `MXDiagnosticPayload` delivers crash, hang and CPU-exception diagnostics *to the app itself, on the device*, arriving immediately on iOS 15+ [E — [Apple, MXDiagnosticPayload](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload), [MXCrashDiagnostic](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic)]. Haunt should **receive these payloads and write them into a local, capped, user-readable diagnostics log — and never transmit them**. That gives the app self-knowledge (it can say "I crashed twice last week") with zero collection.

**Layer 3 — the user-initiated diagnostic bundle (the part Candour builds).** A `Settings → Report a problem` screen that:
1. Assembles a bundle: app version, OS version, device model, location-authorization state, capture statistics (counts, not places), recent structured `OSLog` entries from a capped rolling buffer, and any MetricKit payloads.
2. **Shows the user the entire bundle as readable text before anything happens**, with a copy/save/share sheet. No hidden fields.
3. Contains **no venue names, no coordinates, no note text, no ratings** — enforced by construction: the diagnostics buffer is a separate logging channel that the journal layer is architecturally unable to write into, with a test that fails the build if journal strings appear in it.
4. Lets the user attach it to an email *they* send, from *their* client, to a published support address. Candour receives it because a human chose to send it, which is the only lawful basis needed and the only one worth having.

Apple's own documentation already tells users how to do the manual version of this — Settings → Analytics & Improvements → Analytics Data → share the log [E — [Apple, Acquiring crash reports](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs)]. Layer 3 is that flow, made humane and pre-redacted.

**Layer 4 — what Candour gives up, honestly.** No funnel analytics, no retention cohorts, no A/B tests, no "which screen do people abandon." The idea brief is right that this removes the feedback loop. The replacements are qualitative and cost founder time rather than money: a TestFlight cohort of real users on real nights out (TestFlight users share crash reports automatically regardless of device settings [E, same Apple source]), a published changelog that invites replies, and support email read personally. Budget **~2 hours/week of founder time on support and diagnosis** from launch [J] — that is the honest operating cost, and the CFO should carry it as a labour line under Article 2.1 rather than pretending it is zero.

**One line for the marketing copy that is fully true under the §2.6 architecture:** *"Haunt has no analytics. If something breaks, you send us a report you have read first — or you don't."*

---

## 6. Build sizing

All figures below are **[J] — my estimate as CTO, not evidence.** They are "focused solo weeks": weeks where building is the main activity. The CFO should apply a calendar multiplier for a part-time operator, and note that some of this is calendar-bound rather than effort-bound — you can only test a Friday night on a Friday night.

### 6.1 MVP as recommended (iOS only, offline venue index)

| Workstream | Weeks |
| --- | --- |
| Project setup, signing, CI, App Store Connect admin | 1 |
| Visit capture: `CLVisit` integration, authorization state machine incl. the provisional-Always downgrade (§1.1), candidate-visit queue, persistence | 2.5–3 |
| Venue index: extract pipeline, on-device SQLite with spatial + name search, category mapping, confidence filtering, "not listed" path | 3–4 |
| Timeline UI, entry editing, notes, ratings, search | 2.5–3 |
| Data layer: schema, migrations, export **and import** (§3) | 1 |
| Encrypted backup + restore + recovery-code UX (§4) | 1.5–2 |
| Onboarding, permission flows, honesty surfaces | 1 |
| Accessibility to WCAG 2.1 AA baseline: VoiceOver, Dynamic Type, contrast, motion | 1 |
| Diagnostics (§5) incl. the redaction test | 0.5 |
| Field testing across real weeks + battery measurement + App Review cycles | 2 |
| **Total** | **16–19 weeks** |

**The battery measurement and multi-week field testing are not padding.** A visit-detection product cannot be verified in a simulator, and the QA seat should refuse a release-readiness sign-off that has not seen a month of real capture [J].

### 6.2 Delta: online places API instead of the offline index

**Roughly cost-neutral on build, and worse on everything else** — this is the finding that contradicts the idea brief's premise.

- **Removes:** the extract pipeline, on-device search, category mapping, dataset update delivery (≈ −3 to −4 weeks).
- **Adds:** API key management and secret handling, network error and offline states throughout the core loop, rate limiting and cost alarms, the 30-day cache-eviction machinery §2.1 requires, re-query-on-view for stored entries, attribution surfaces, and the in-app privacy-boundary disclosure the idea brief identified as needing design (≈ +3 to +4 weeks).
- **Then adds permanently:** the running cost in §2.5, a terms-of-service exposure at the centre of the data model, and a product that stops working in a basement.

**The idea brief's assumption that the zero-network variant costs materially more to build is not supported.** I am recording that as a correction, not a preference.

### 6.3 Delta: Android addition (as a separate later phase)

| Workstream | Weeks |
| --- | --- |
| Capture layer: Activity Recognition + fused location, hand-built visit clustering, per-OEM behaviour work | 4–6 |
| App rebuild: UI, timeline, editing (native Kotlin/Compose against the §3 schema spec) | 4–5 |
| Backup: `appDataFolder` + Auto Backup fallback, same crypto | 1 |
| Play policy: background-location declaration, FGS-type declaration, two demonstration videos, prominent disclosure, review cycles | 1–2 (plus **weeks of calendar** waiting on review [E, §1.2e]) |
| Device-matrix testing across ≥3 OEMs over real weeks | 2–3 |
| **Total** | **12–17 weeks, plus a recurring support tax** |

Plus the pre-build spike (§1.3): **2 weeks**, which may return the answer "don't."

**Architectural hedge that costs almost nothing now:** do *not* adopt Kotlin Multiplatform for an iOS-only MVP — it is a toolchain liability against a boring-stack mandate, and the hard part (capture) is not shareable anyway. Instead, publish the SQLite schema and the JSON export format as a written spec (§3). A future Android build then implements against a document rather than reverse-engineering an app. Cost: ~2 days. Saving if Android ships: weeks [J].

### 6.4 Ongoing, post-launch

| Item | Cost |
| --- | --- |
| Venue dataset refresh (re-run pipeline, ship with app update) | ~0.5 day/month [J] |
| Support and diagnosis (§5) | ~2 hours/week [J] |
| iOS annual-release compatibility | ~1 week/year [J] |
| Apple Developer Program | $99/year [E — standard programme fee, widely published; not retrieved this session, tag as [K, high confidence] pending CFO verification] |
| Per-user infrastructure | **£0 at 10 users and at 10,000** [I] |

---

## 7. What I would block, and what lifts it

Per my charter, a block cites a specific breach and states what lifts it. Neither of these is active today — the build has not been proposed — but the gate should know them in advance.

**Block 1 — an architecture that persists places-API venue records in the local journal.**
*Breach:* Google Maps Platform Terms 3.2.3(b) ("Customer will not cache Google Maps Content except as expressly permitted") together with Service Specific Terms A.3 and 14.3, which permit only `place_id` indefinitely and lat/lng for 30 days [E, §2.1]. Constitution 1.5 (operating-cost discipline) and Article 7.2 (export must survive discontinuation) are engaged as consequences.
*Lifted by:* adopting a dataset whose licence permits permanent local retention (Overture Places, FSQ OS Places, or OSM under ODbL); **or** Mapbox Permanent Geocoding with its terms verified against the CFO's cost model; **or** written confirmation from the provider that the intended retention is permitted.

**Block 2 — an Android MVP whose capture reliability rests on undocumented OEM behaviour.**
*Breach:* Constitution 1.3 and Article 4 (no claims we cannot substantiate) — shipping "automatic capture" that we know will fail silently on a large share of the fleet [E, §1.2f].
*Lifted by:* a published device-matrix spike measuring real capture rates over ≥2 real weeks on at least Pixel, Samsung and Xiaomi, with a stated minimum rate agreed with the PM/BA and QA seats before the spike runs.

---

## 8. Open questions I could not close, and who owns them

| # | Question | Owner | Why it matters |
| --- | --- | --- | --- |
| 1 | Verify Foursquare's own Usage Guidelines and API License Agreement on caching (my §2.1 claim rests on a secondary source) | Skeptic, at gate | Only matters if any online-API route survives |
| 2 | Verify Mapbox Permanent Geocoding pricing against Mapbox's own pricing page | CFO | The one paid route that permits permanent storage |
| 3 | Measured battery cost of `startMonitoringVisits` over a real week | Engineer, during build | Apple publishes no figure; no marketing claim until measured |
| 4 | Overture UK data quality *as a user experiences it* — how often is the right venue in the top three candidates? | Engineer, 2-day spike **before** the gate | Decides whether the offline index is shippable; a cheap, high-value spike |
| 5 | Realistic visits-per-user-per-month | Research Analyst | My §2.5 model uses 12/month as an assumption [J] |
| 6 | Whether users read the offline architecture as *more* trustworthy (worth marketing) or merely as *fewer venues* | Research Analyst | Feeds the honesty-problem question the idea brief raised |
| 7 | Whether an ODbL-licensed derived index (and Article 8 open-sourcing) is desirable rather than merely permitted | CEO, at gate | Constitution 8 encourages it; it is a decision, not a default |

---

## 9. Evidence register

Every link below was retrieved on **2026-09-09** during the session that produced this note. Nothing here is cited from memory.

**iOS background location**
- [Apple — `startMonitoringVisits()`](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits()) — relaunch-after-termination; reduced-accuracy operation; not deprecated (iOS 8+)
- [Apple — `CLVisit`](https://developer.apple.com/documentation/corelocation/clvisit) — properties; incomplete arrival/departure
- [Apple — `requestAlwaysAuthorization()`](https://developer.apple.com/documentation/corelocation/cllocationmanager/requestalwaysauthorization()) — two-prompt flow, provisional Always
- [Apple — Energy Efficiency Guide, Location Best Practices](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/LocationBestPractices.html) — visit/region monitoring preferred over significant-change

**Android background location**
- [Google — Awareness API overview](https://developers.google.com/awareness/overview) — deprecated, shutdown "as early as January 2027", "no direct replacement"
- [Android — Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing) — 100 geofences/app; DWELL; responsiveness; latency
- [Android — Detect when users start or end an activity](https://developer.android.com/develop/sensors-and-location/location/transitions) — Activity Recognition Transition API
- [Android — Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits) — "only a few times each hour", regardless of target SDK
- [Android — Access location in the background](https://developer.android.com/develop/sensors-and-location/location/background)
- [Android — Optimize for Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby) — Play prohibits exemption requests; acceptable-use table
- [Android — Foreground service types are required (Android 14)](https://developer.android.com/about/versions/14/changes/fgs-types-required)
- [Play Console — Understanding location in the background permissions](https://support.google.com/googleplay/android-developer/answer/9799150) — declaration, video, core-functionality test, removal risk
- [Play Console — Foreground service requirements](https://support.google.com/googleplay/android-developer/answer/13392821)
- [dontkillmyapp.com](https://dontkillmyapp.com/) — OEM background-kill ratings *(single source, community-maintained)*
- [StatCounter — UK mobile OS market share, Aug 2026](https://gs.statcounter.com/os-market-share/mobile/united-kingdom) *(single source)*

**Venue data — terms and licences**
- [Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms) — 3.2.3(b) No Caching; 3.2.3(d) No Re-Creating Google Products; No Use With Non-Google Maps
- [Google Maps Platform Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms) — A.3 Google ID Caching; 14.2; 14.3
- [Google — Places API policies and attributions](https://developers.google.com/maps/documentation/places/web-service/policies) — place_id exempt, everything else not
- [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing) — Nearby Search $32/1,000 (Pro, 5,000 free); Place Details $5/1,000 (Essentials, 10,000 free)
- [Mapbox — Temporary vs Permanent Geocoding](https://docs.mapbox.com/help/dive-deeper/understand-temporary-vs-permanent-geocoding/)
- [Foursquare Places API comparison](https://openplacesapi.com/compare/foursquare-places-api) *(single source, secondary — flagged for Skeptic verification)*; primaries: [Usage Guidelines](https://docs.foursquare.com/docs/usage-guidelines), [API License Agreement](https://foursquare.com/legal/terms/apilicenseagreement/)
- [Overture — Attribution and licensing](https://docs.overturemaps.org/attribution/) — Places = CDLA Permissive 2.0; base/buildings/divisions/transportation = ODbL
- [Overture — Places guide](https://docs.overturemaps.org/guides/places/) — sources; "duplicates, a high junk rate, and low property completeness"; no OSM data
- [Foursquare OS Places notice](https://opensource.foursquare.com/places-notice-txt/) — Apache 2.0

**Venue data — measurements taken this session**
- OpenStreetMap UK counts via `https://overpass-api.de/api/interpreter`, data timestamp 2026-09-09T21:05:56Z. © OpenStreetMap contributors, ODbL.
- Overture Places release `2026-08-19.0` via `s3://overturemaps-us-west-2/release/2026-08-19.0/theme=places/type=place/`, queried with DuckDB 1.5.5 + httpfs/spatial. UK bbox −8.65,49.86 → 1.77,60.86. Artefacts weighed locally.
- UK licensed-premises denominator: [The Spirits Business, Jan 2026](https://www.thespiritsbusiness.com/2026/01/new-openings-boost-bar-numbers-in-britain/) and [Morning Advertiser, Oct 2025](https://www.morningadvertiser.co.uk/Article/2025/10/21/uk-licensed-premises-fall-by-572-amid-tough-hospitality-climate/), both reporting CGA by NIQ *(single origin — two outlets, one underlying report; the report itself was not retrieved)*

**Storage, export, backup, diagnosis**
- [Article 20 GDPR — right to data portability](https://gdpr-info.eu/art-20-gdpr/)
- [Apple — iCloud data security overview](https://support.apple.com/en-gb/102651) — third-party app data E2EE only under Advanced Data Protection
- [Apple Platform Security — iCloud encryption](https://support.apple.com/en-gb/guide/security/sec3cac31735/web) — CloudKit Service key hierarchy
- [WWDC21 — What's new in CloudKit](https://developer.apple.com/videos/play/wwdc2021/10086/) — `encryptedValues`
- [Android — Back up user data with Auto Backup](https://developer.android.com/identity/data/autobackup) — 25 MB; nightly; E2EE with screen lock on Android 9+
- [Google — Drive appDataFolder](https://developers.google.com/workspace/drive/api/guides/appdata) and [Choose Drive API scopes](https://developers.google.com/workspace/drive/api/guides/api-specific-auth) — `drive.appdata` is a non-sensitive scope
- [Apple — Acquiring crash reports and diagnostic logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs) — opt-in App Store crash reports; TestFlight always shares; Jetsam/watchdog/thermal gaps
- [Apple — MXDiagnosticPayload](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload) / [MXCrashDiagnostic](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic)
- [Play Console — Android vitals](https://support.google.com/googleplay/android-developer/answer/7385505) — opt-in users only; excludes uncertified devices

---

*Prepared by the CTO seat under `roles/cto.md`. This note prepares and flags; it does not certify. Kill/proceed/park is the CEO's decision (Constitution 5.4), due 2026-10-07 per the anti-drift rule. [Date corrected by CVO 2026-09-10; written when the deadline was believed to be 2026-10-28. Nothing technical in this note depends on it.]*

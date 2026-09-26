# Haunts: the heatmap's map, compared: offline basemap, platform maps, provider offline packs and privacy-focused providers

**Seat:** Chief Technology Officer · **Date:** 2026-09-23, updated 2026-09-26 (Zoomstack measured; Overture added) · **Status:** A comparison and a recommendation. **It prepares and flags. It does not certify** (Constitution 6.1). Which option ships is a user-data policy decision, and Constitution 5.4 reserves *"anything affecting user data policy"* to the CEO.

**Slug:** `haunt` · **Follows:** `products/haunt/map-tiles-note.md` (2026-09-22), which the CEO has read. **His stated preference, based on that note, is offline.** Before committing he asked for four things: (1) both options weighed evenly, with platform maps given their strongest case; (2) his third route, offline packs from the providers themselves, tested; (3) the trimmed basemap measured if possible; (4) a recommendation that says whether (2) changes it. **A later addition from the CEO:** survey privacy-focused map providers against the real constraints and put them in the same table.

**Decisions bearing on it:** D1 (both platforms), D10(c) and LOOK-2 (the heatmap), D12 (the photo fetch, and the line it draws at map tiles), D13 (the ranked list is the base view; the heatmap is a second view), D14(c) (the approved privacy wording at `requirements.md` §12.2.8). D15 to D18 are pricing decisions and none of them moves this question. The one link: every build hour added here is capitalised build labour under the Definitions and moves the volume at which D18's recomputed prices are honest (`cost-sheet-v3.md` §4.6).

**Template note.** None of the nine templates in `pipeline/templates/` is a technical comparison or an ADR. This document uses the structure of the note it follows. I say so here so the choice of format is visible.

**Method.** Every term, price and privacy statement below was retrieved in this session, 2026-09-22/23, and the link sits next to the claim. Items carried over from `map-tiles-note.md` were re-retrieved where they are load-bearing. Where one was not, I say so. **Search-engine summaries are not primary retrievals**, and every claim that rests on one is flagged.

---

## 0. The answer, before the working

**Recommendation: keep the offline OS Open Zoomstack basemap, rendered on the device by MapLibre.** Deliver it as a **one-time, whole-country download through the App Store or Google Play**, not bundled in the app. Give Northern Ireland the no-basemap view at launch, and say so on the map. **The provider-offline route does not change this.**

1. **Size, now measured on Zoomstack itself: about 0.76–0.84 GB.** This is Great Britain with roads, water, green space, outline and names, and street zoom 14 kept in built-up areas. I downloaded the real file (2.85 GB, checksum matching OS's) on the CEO's approval and trimmed every tile (§5).
   - **To zoom 13 only:** 0.55 GB.
   - **Zoom 14 everywhere:** 0.97 GB.
   - **Cheapest usable cut:** 0.59 GB.

   **My note's 100–400 MB estimate was wrong, and so was my later guess that Zoomstack would be smaller than OpenStreetMap: it is slightly larger.** [E, measured, §5.2] **Bundling in the app (about 150 MB or less) is out. A one-time pack through the store is in**, because Google Play allows up to 1.5 GB per pack.
2. **The CEO's third route has the right principle, but no provider sells the product it needs.** A download of the whole UK depends on nobody's data, so it passes limb (b) of the rule I proposed, whoever supplies it. **Apple and Google do not offer offline maps to third-party apps at all.** Apple's DTS engineer says so, and Apple's licence limits caching to *"a temporary and limited basis"*. Google's terms forbid it: *"No Caching"*, and no *"bulk download"* of tiles. **Mapbox does sell offline packs, but with four catches.**
   - A whole-UK pack at street zoom needs about 2,600 "tile packs". The default cap is 750.
   - The downloaded map can be kept for at most 30 days.
   - The SDK sends *"location and usage data"*, and Candour is forbidden to block it.
   - The pack cannot be bundled in the app. It must come from Mapbox's servers.

   **HERE and TomTom** keep offline maps behind a paid licence or a request to their sales team. §3.
3. **The CEO was right that storage would come back, for the providers.** Mapbox's 30-day limit means downloading the UK again every month, **roughly 15 GB per user per year** at the measured size [I]. HERE only supports offline map versions for one year. **On the Zoomstack route there is no expiry.** Updating is Candour's choice: at most twice a year, or less often, at about 0.8 GB each time [I]. §3.4.
4. **Platform maps win on five of the nine points, and I say so plainly.** They are better on UX quality, Northern Ireland coverage, app size, build effort and upkeep of the map data. **They lose on the one point the product is sold on.** Each map request tells Apple or Google which area this person is looking at, and on a heatmap that area is their most-visited place. Their best form is a map the user turns on, with that disclosed. That is a fair choice for the CEO to make, but it is a change to the privacy wording, not a technical detail. §2.
5. **No privacy-focused provider beats Zoomstack plus MapLibre, and I looked.** OpenFreeMap, Protomaps and VersaTiles are all OpenStreetMap data. If Candour downloads it once and ships it, **it works as well as Zoomstack and also covers Northern Ireland, but it is ODbL**, the licence the CGO has marked as a boundary. Used live as an online service, it sends tile requests like any other provider. MapTiler charges for consumer use. Organic Maps cannot be embedded in another app. OsmAnd is GPLv3. **Overture Maps (added 2026-09-26) is the same answer:** its Base, Transportation and Divisions themes are ODbL at source. The only non-ODbL parts are Places, satellite land cover and sea depth, which have no roads and no coastline. §4, §4.4.

**No decision is needed now (§8).** The download the CEO approved on 2026-09-26 is done, and the size limb of the spike is settled. **What remains is a render test on two phones (§5.4).** It needs no decision, only about a day of build time.

---

## 1. The comparison at a glance

**How to read it.** "Limb (b)" is the second test of the rule proposed in `map-tiles-note.md` §0: a network request fits the product's claim if its content does not depend on the user's data. "Heatmap both" asks whether a heatmap layer draws on iOS **and** Android from React Native without hand-building. Sizes are for the UK. Every cell is backed by tagged evidence in the section named in the last column.

| Option | What leaves the device / limb (b) | Telemetry, keys, licence checks | UK coverage incl. NI | Licence | Heatmap both, from RN | Size on device | Money cost at 5k–10k users | Can a solo operator rely on it for 5 years? | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **A. OS Open Zoomstack + MapLibre, offline (recommended)** | **Nothing** if bundled. **If store-delivered:** one request to Apple or Google for a whole-GB pack. **Passes (b)** | **None.** MapLibre removed telemetry; no key | **GB only**, down to street level. **NI not covered** | **OGL v3.0. Attribution only, no share-alike** [E] | **Yes**, `HeatmapLayer` on both [E] | **Measured: 0.76–0.84 GB** (GB, z14 in built-up areas); 0.55 GB to z13; 0.97 GB z14 everywhere [E] | **£0** running | **Yes.** Government open data, six-monthly; MapLibre updated 2026-09-19 [E] | §2, §5 |
| **B. OSM basemap (Protomaps / OpenFreeMap / VersaTiles downloads) + MapLibre, offline** | Same as A. **Passes (b)** | None | **GB and NI** | **ODbL.** The Produced Work reading is unsettled. **Hits the CGO's boundary** | Yes | **Measured: 0.69–0.79 GB** to z14 (GB+NI) [E] | £0 | Yes on the data; three small operators on the tooling | §4, §5 |
| **B′. Overture Maps (Base + Transportation themes) + MapLibre, offline** | Same as A if built into one downloaded file. **Passes (b)** | None in the data; GeoParquet releases, no key [E] | GB and NI | **ODbL for Base, Transportation, Divisions and Buildings** at source; only Places (CDLA-Permissive-2.0 / Apache-2.0 / CC0) and, within Base, ESA WorldCover land cover (CC BY 4.0) and bathymetry are not. **No non-ODbL combination has roads or a coastline.** **Hits the CGO's boundary exactly as B does** [E] | Yes, via MapLibre (after Candour builds tiles) | Not measured; no ready-made tiles, so Candour would build them [I] | £0 | Strong backers; monthly releases [K]. **Adds a tile-building pipeline Candour must own** [I] | §4.4 |
| **C. Platform maps: MapKit (iOS) + Google Maps SDK (Android)** | **Viewport tiles on every open and pan.** Apple receives *"Boundaries of the map area visible"*; Google receives the IP address, a pseudonymous ID and pan/zoom data [E]. **Fails (b)** | Google API key; Google SDK identifier; Google terms make Candour a **controller** [E] | **Full UK incl. NI**, current, with points of interest | Vendor terms. Apple can *"revoke"* access at *"sole discretion"* [E] | **No.** The RN heatmap is *"Supported on Google Maps only"* [E]; iOS needs a hand-built layer, or Google on iOS too | **~0 MB** | **£0**. Google's Maps SDK is *"Unlimited"* [E]; MapKit free [E, 2020, single source] | Yes technically; **terms can change unilaterally** | §2 |
| **C′. Platform maps, turned on by the user each time, disclosed (the strongest case for C)** | Nothing until the user taps "show street map"; then as C. **Fails (b), with consent** | As C | As C | As C | As C | ~0 MB | £0 | As C | §2.3 |
| **D. Apple offline packs for third-party apps** | **Not offered.** *"not possible with the APIs available today"* [E, Apple DTS] | n/a | n/a | Apple licence §2.5 bars caching except *"temporary and limited"* [E] | n/a | n/a | n/a | n/a | §3.1 |
| **E. Google offline packs for third-party apps** | **Not offered, and forbidden:** *"No Caching"*; no *"bulk download"* of tiles [E] | n/a | n/a | Terms §3.2.3(a)–(b) [E] | n/a | n/a | n/a | n/a | §3.2 |
| **F. Mapbox offline tile regions** | Download of the whole UK **passes (b)**, **but** the SDK *"will periodically send location and usage data"* and Candour *"shall not… interfere"* [E]. **Fails PRIV-8** | Access token; MAU accounting; licence ends with the account [E] | Full UK | Mapbox terms; **may not be bundled**; **30-day cache limit** [E] | Yes (`@rnmapbox/maps`) [K] | Comparable to B's full-layer ~1.3 GB [I]; **re-fetched every 30 days** | £0 up to 25,000 MAU [E] | **No.** 750-pack cap (UK needs ~2,600) [E/I]; SDK must be at most 12 months old [E] | §3.3 |
| **G. HERE SDK offline (Navigate edition)** | Country download passes (b); **telemetry** that must be disclosed [E] | OAuth credentials; paid Navigate licence [E] | Full UK | Commercial | **No RN SDK** found [I] | *"several hundreds of megabytes"* and up [E] | **Unpriced** (pricing page did not render) | Map versions supported for **one year** [E] | §3.5 |
| **H. TomTom offline** | Manual updates pass (b); **automatic updates use *"the user's location"*** [E] | Key; **iOS offline *"only available upon request"*** [E] | Full UK | Commercial | No RN SDK found [I] | Not stated | Not established | Gated by sales | §3.5 |
| **I. OpenFreeMap public service, online** | Viewport tiles to one operator's servers behind Cloudflare. **Fails (b)** | No key, no cookies [E] | Full UK | OSM / ODbL | Yes (MapLibre) | 0 | £0 | **No SLA**; *"may discontinue it at any time"* [E] | §4 |
| **J. MapTiler (hosted or on-prem)** | Hosted: viewport tiles, **fails (b)**. On-prem: passes (b) | Hosted: API key | Full UK (includes OS OGL data) [E] | ODbL + OpenMapTiles attribution [E] | Yes (MapLibre) | As B | On-prem consumer use needs a **custom annual contract**; Standard is $2,500/yr and *"internal app only"* [E] | Commercial vendor | §4 |
| **K. Organic Maps / OsmAnd** | n/a | n/a | Full UK | Organic Maps' API **opens their app** [E]; OsmAnd is **GPLv3** [E] | **Cannot be embedded** | n/a | n/a | n/a | §4 |
| **L. No basemap (fallback)** | Nothing | None | Everywhere, equally thin | Venue index only (CDLA already carried) | Yes | 0 | £0 | Yes | `map-tiles-note.md` §6 |

**Reading across the rows, in one line each:**

- **Offline wins on:** what leaves the device, telemetry, licence clarity, running cost and five-year dependability.
- **Platform maps win on:** map quality, Northern Ireland, size on the phone, build effort, and never having to refresh a map file.
- **Provider offline packs:** Apple and Google do not offer them. The one provider that does, Mapbox, brings back telemetry, storage that has to be refreshed and a cap on area.

---

## 2. Offline basemap versus platform maps, weighed evenly

### 2.1 Axis by axis

| Axis | Offline Zoomstack + MapLibre | Platform maps (MapKit + Google) | Who wins |
| --- | --- | --- | --- |
| **Privacy: what leaves the device** | Bundled: nothing. Store pack: one request for a whole-UK file, the same for every user, sent once. The store learns only that this person opened the heatmap [I] | Every open and every pan requests the tiles on screen. **Apple** lists *"Boundaries of the map area visible on your device"* and *"the places you view"* among what it receives [E, [Apple Maps & Privacy](https://www.apple.com/legal/privacy/data/en/apple-maps/)]. **Google's Android SDK** collects the *"IP address"*, a *"Maps SDK-specific pseudonymous identifier"* and *"interaction data, such as panning and zooming the map"* [E, [Maps SDK for Android data disclosure](https://developers.google.com/maps/documentation/android-sdk/play-data-disclosure)]. Google *"may use and retain this data to provide and improve Google products and services"* [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms) §4.4(a)] | **Offline, decisively** |
| **Privacy: how bad the platform case really is** | n/a | **Apple's published practice is good:** usage identifiers that rotate *"multiple times per hour"* and are not tied to the Apple Account, and precise locations blurred *"within 24 hours"* [E, same Apple page]. **That page covers Apple's Maps app. It does not say the same for MapKit inside another developer's app.** Google has no equivalent assurance, and its terms bring in controller-to-controller data terms (§4.4(b)) [E] | Apple is a much better third party than Google. It is still a third party |
| **Build effort** | 55–95 h for a store-delivered pack (tile pipeline, MapLibre style with local fonts and icons, pack download, first-run copy, network-capture tests) [J, `map-tiles-note.md` §7.2, restated for the delivery route the measurement now points to] | **25–50 h** [J, same]. `react-native-maps` is mature (v1.29.8, 2026-09-20 [E, GitHub API]). **The catch:** its heatmap is *"Supported on Google Maps only"* [E, [react-native-maps heatmap doc](https://github.com/react-native-maps/react-native-maps/blob/master/docs/heatmap.md)], so iOS needs a hand-built MapKit overlay. The alternative is Google Maps on iOS too, which the library supports (*"Google Maps on iOS and Android"*, [E, README](https://github.com/react-native-maps/react-native-maps)) but which puts Google on iPhones. `expo-maps` is *"currently in alpha"* and its documentation does not mention heatmaps [E, [Expo Maps](https://docs.expo.dev/versions/latest/sdk/maps/)] | **Platform maps, by about 30–45 hours (£981–£1,472)** |
| **Complexity** | Two moving parts Candour owns: the tile file and the style. **Trap:** a style that fetches fonts or icons from a URL makes a silent network call [K, high confidence; `map-tiles-note.md` §5.5] | A few lines to show a map. The complexity sits in the terms: Google Cloud project and API key; Apple §2.6 on fees; the controller question | Platform maps on code; offline on contracts |
| **Size (download / on device)** | **0.76–0.84 GB** for Great Britain at street zoom in built-up areas, downloaded once (0.55 GB to z13) [E, measured on Zoomstack, §5.2] | **~0.** The OS or Play services supply the map [K] | **Platform maps, clearly** |
| **UX quality** | A map Candour designs for one job: streets, water, parks, place names, no business labels. Readable, calm and up to six months old. **No shops or landmarks for orientation**, apart from the user's own venues [J] | The full map people already know: landmarks, labels, current data, dark mode, smooth pan and zoom [K]. **Better for orientation**, noisier under a heatmap [J] | **Platform maps** |
| **Upkeep of the map data** | Zoomstack is updated *"June, December"* [E, [OS Zoomstack docs](https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-open-zoomstack)]. Rebuild and re-ship the pack on the release train. 8–12 h/yr [J, `map-tiles-note.md` §7.2] | **None.** The vendor refreshes. SDK upgrades in the annual pass [J]. **But:** vendor restyling can break A11Y-3's contrast measurement without notice [I] | **Platform maps** on the data; offline on predictability |
| **Maintenance risk / lock-in** | MapLibre (BSD-2-Clause, [E, GitHub API](https://github.com/maplibre/maplibre-native)) and OGL data. Nobody can switch it off [I] | Apple *"reserves the right to revoke Your access to MapKit… at any time in its sole discretion, even if Your use… meets the Documentation"* [E, [Apple DPLA](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/), Attachment 6]. Google's terms change often: the page lists revisions to *"August 26, 2026"* [E, Google terms] | **Offline** |
| **Licence and attribution** | OGL v3.0: *"copy, publish, distribute and transmit… adapt… exploit the Information commercially"*, provided you acknowledge the source. **No share-alike** [E, [OGL v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)]. The OS attribution string is still to be confirmed at primary (`map-tiles-note.md` §5.1) | Vendor attribution, handled by the SDK. **Google §4.4(b)** makes Candour an independent controller by contract [E]. **Google §3.2.3(d)** bars re-creating *"features of another Google product"*, and Maps Timeline is one [E, `map-tiles-note.md` §3.3, same terms page]. **The CGO's Constitution 6.1 trigger is pulled** (a map-data API) | **Offline** |
| **Coverage (Northern Ireland)** | **Zoomstack: "Great Britain"**, and NI is not included [E, OS docs]. NI gets the no-basemap view until a layer is added (§4.3) | **Full UK** [K] | **Platform maps** |
| **Cost** | £0 running. Build **£1,799–£3,107** at £32.71/h. Upkeep **£262–£393/yr** [J hours × benchmark] | £0 running [E, [Google pricing](https://developers.google.com/maps/billing-and-pricing/pricing): Maps SDK *"Unlimited"*]. Build **£818–£1,636**. **Plus an unpriced 6.1 legal review and unpriced CGO controller work** | Platform maps on build labour; **unknown overall**, because two of its costs are unpriced |
| **The privacy wording (§12.2.8)** | Bundled: **unchanged.** Store pack: one added sentence (§6) | **Must be rewritten.** *"Haunts sends your data nowhere else"* becomes contestable, because the viewed area is derived from the journal (§6) | **Offline** |

**Score on the nine points the CEO listed:**

- **Platform maps win five:** build effort, size, UX, Northern Ireland, and upkeep of the map data.
- **Offline wins four:** privacy, licence, cost certainty, and the privacy wording.
- **The four offline wins are the four the product's claim rests on.** That is why I still recommend offline, and it is a weighting, not a tally [J].

### 2.2 The strongest honest case for platform maps

Put as well as I can make it:

1. **The person already trusts Apple with more than this.** On iPhone, Apple made the OS, runs the store, takes payment, and may hold the user's photos and backup. A map request tells Apple which area the user is looking at, but on an iPhone Apple already knows far more than that. Apple also publishes that it rotates identifiers and blurs precise locations within 24 hours [E]. [I]
2. **The request is coarse, and the journal never leaves.** A zoom-14 tile is about 1.5 km across (`map-tiles-note.md` §2.2). The provider learns a neighbourhood. It never learns venues, times, companions or notes. [I]
3. **It is the better map.** It covers Northern Ireland, adds nothing to the download, has current data and familiar landmarks, and needs no refresh process to maintain for five years (D2). [K/J]
4. **It is cheaper to build**, by roughly 30–45 hours [J].
5. **It can be made a consented, per-use choice.** For example, a heatmap that opens with no basemap and has a clearly labelled control: *"Show street map. Your phone will ask Apple (or Google) for map images of the area on screen."* Nothing is sent until the user asks. [J]

**Where the case breaks, and why I still do not recommend it:**

- **Point 1 is true for iOS and false for Android.** D1 requires both platforms, and on Android the provider is Google, under controller terms and a clause barring the re-creation of Google's own features. [I]
- **Point 2 understates the problem.** The screen opens on the user's densest cluster, so the first request on every opening names the square their life centres on. That is a hotspot, repeated, together with an IP address and an SDK identifier. [I]
- **Point 5 is the honest form**, and it costs the product its simplest sentence. It also still pulls the CGO's 6.1 trigger, because a map-data API gets linked either way. [I]

**If the CEO chooses platform maps, choose C′ (opt-in each time), not C.** [J]

### 2.3 What platform maps would require first

These are unchanged from `map-tiles-note.md` §8:

1. PRIV-1, PRIV-8 and DATA-6 are rewritten through a scope change, because as written they fail the build.
2. The CGO's 6.1 trigger is pulled, and a qualified human legal review is priced before launch.
3. The CGO determines Candour's controller position under Google §4.4(b) before Android ships.

**None of this is a block.** My charter blocks build commencement only on architectures that are *"unsustainable, needlessly expensive, or insecure by design"* (`roles/cto.md`). Platform maps are none of those.

---

## 3. The CEO's third route: offline packs from the providers themselves

### 3.0 The principle is right

**A download whose content is "the whole UK" is the same request for every user.** It reveals only that this user opened the heatmap. It passes limb (b) whoever serves it, even Apple or Google. **I agree with the CEO's reasoning without reservation.** The question is whether any provider actually sells that. [I]

### 3.1 Apple: not offered

- **No API exists.** Asked in October 2024 whether MapKit supports offline maps, Apple's DTS engineer answered that bringing your own tiles works, but *"If you're looking to use Apple's own offline maps provided by the Maps app and then load that data in your app, that is not possible with the APIs available today"* [E, [Apple Developer Forums thread 765857](https://developer.apple.com/forums/thread/765857). **Single source, but it is Apple's own engineer, and it is two years old**].
- **The licence forbids it anyway:** *"Map Data may not be cached, pre-fetched, or stored by You or Your Application… other than on a temporary and limited basis solely as necessary (a) for Your use of the Apple Maps Service… and/or (b) to improve the performance… after which, in all cases, You must delete any such Map Data"* [E, [Apple DPLA](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/), Attachment 6 §2.5].
- **Finding: no whole-UK Apple pack is possible for a third-party app.** What would overturn it: a new MapKit offline API, or written permission from Apple, since §2.5 opens with *"Unless otherwise expressly permitted in writing by Apple"*. I found neither.

### 3.2 Google: not offered, and forbidden

- **The terms:** *"Customer will not… (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services; (ii) bulk download Google Maps tiles…"* and *"(b) No Caching. Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms"* [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms) §3.2.3(a)–(b)].
- **The Service Specific Terms allow caching only for IDs** (place ID, pano ID, video ID) and Address Validation results. I searched the retrieved text for the Maps SDK and for "offline" and found **no provision for either** [E, [Maps Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms)].
- **The raw Map Tiles API says the same:** *"you must not pre-fetch, index, store, or cache any Content except under the limited conditions stated in the terms"*, and it treats offline use as outside its permitted purpose [E, [Map Tiles API policies](https://developers.google.com/maps/documentation/tile/policies)].
- **Finding: no Google offline pack is available to Haunts.** What would overturn it: a Service Specific Term permitting offline Maps SDK content. I found none in the version on the page.

### 3.3 Mapbox: offered, with four catches

**Offline is a real, supported feature**, done through "tile regions" downloaded into a TileStore [E, [Mapbox offline concepts, iOS](https://docs.mapbox.com/ios/maps/guides/offline/concepts/)]. Against the CEO's test:

| Test | Finding | Source |
| --- | --- | --- |
| **Can the region be the whole UK?** | **Not at street zoom within the default cap.** *"The cumulative number of unique tile packs used in the tile regions cannot be greater than 750."* Packs are grouped by zoom range, *"Town information: zoom 11-14"*, and *"each tile pack covers the area of its lowest zoom level map tile"*. So the street-level packs are zoom-11 tiles, about 12 km across. **The UK needs about 2,600 of them** (2,448 for GB and 153 for NI on my land mask, counted in §5). **That is about 3.5 times the cap.** The cap covers roughly 40% of the UK at street zoom. A search summary says the limit is *"subject to change"* on request; I could not find that sentence at primary | [E, [concepts](https://docs.mapbox.com/ios/maps/guides/offline/concepts/); [tile pack glossary](https://docs.mapbox.com/help/glossary/tile-pack/)]; count [I] from §5's tile enumeration; *"subject to change"* **search summary only** |
| **Can Candour ship it in the app?** | **No.** *"Terms of service do not allow developers or end users to redistribute offline maps downloaded from Mapbox servers."* Each phone downloads its own copy from Mapbox | [E, same concepts page] |
| **Does it expire?** | **Yes, 30 days.** *"Customer may cache that Licensed Map Content on an End User's device but caching is limited to thirty (30) days on the same device making the Mapping API request… the Licensed Application is required to populate any on-device cache… directly from the Mapping APIs."* Tile regions carry expiry dates, and refreshing them *"require[s] network connectivity"*. **Whether §2.8.1 governs offline TileStore regions, rather than only the ambient cache, is my reading and should be confirmed with Mapbox. The words cover any on-device cache of Mapping API content.** | [E, [Mapbox Product Terms, 21 July 2026](https://www.mapbox.com/legal/product-terms) §2.8.1 (PDF read in full); [Manage offline data](https://docs.mapbox.com/ios/maps/guides/offline/manage-offline-data/)]; applicability [I] |
| **Does anything phone home?** | **Yes, and contractually.** *"The Mobile SDKs will periodically send location and usage data to Mapbox… Customer shall not modify, interfere with or limit the data that a Mobile SDK sends to Mapbox… (except for implementing an End User opt-out as required below)"*. Candour *"shall not modify the billing or accounting code"*. The Maps SDK v10+ licence *"terminates automatically upon termination of Customer's account"*. Mobile apps *"shall use the most recent version of the Mobile SDK or a version released within the immediately preceding twelve (12) months"* | [E, Product Terms §§2.9.1, 2.9.3, 2.9.4, 2.9.2] |
| **Is offline billed?** | *"Resources downloaded for offline use are included in the regular monthly active user (MAU) billing"*. **£0 up to 25,000 MAU**, then $4.00 per 1,000 | [E, [Mapbox offline help](https://docs.mapbox.com/help/dive-deeper/mobile-offline/); [Mapbox pricing](https://www.mapbox.com/pricing)] |

**Finding:** the downloads themselves pass limb (b). **The SDK does not.** It sends location and usage data that Candour may not suppress, which fails PRIV-8 (*"No analytics, no telemetry SDK"*) as written. The 30-day limit also brings the storage cost back every month (§3.4). **Mapbox's offline route is the cleanest that any major provider offers, and it is still worse than Zoomstack on every one of the CEO's tests except map quality.** What would overturn this: a written Mapbox agreement that raises the pack cap, permits bundling or a long expiry, and turns SDK telemetry off entirely. That would be an enterprise negotiation, and I found no public offer of it.

### 3.4 Does the storage issue come back? Yes for the providers, and only if Candour chooses for Zoomstack

| Route | Size of one whole-UK copy | How often it must be fetched again | Per user per year | Source |
| --- | --- | --- | --- | --- |
| **Mapbox offline** | ~1.3 GB (proxy: the full-layer OSM measurement, z0–14, §5; Mapbox Streets is not measured) | **Every 30 days** (§2.8.1) | **~15 GB** of downloads, plus about 1.3 GB held on the phone at all times | [I] from [E] terms and [E] measurement |
| **HERE offline** | *"several hundreds of megabytes"* or more for a country | Map versions older than a year are not guaranteed: *"Backward compatibility of installed offline maps is supported for one year"* | At least one full re-download a year | [E, [HERE offline maps](https://docs.here.com/here-sdk/docs/android-offline-maps)] |
| **TomTom offline** | Not stated | Updates over the air, automatic or manual | Not established | [E, [TomTom offline setup, iOS](https://docs.tomtom.com/navigation/ios/guides/offline/offline-map-setup)] |
| **Zoomstack pack (recommended)** | **~0.76–0.84 GB** [E, §5.2] | **Never required.** Candour may refresh on the six-monthly OS cycle, or less often | **0–1.7 GB**, on Candour's schedule | [I]; release cadence [E] |

**The CEO's expectation is confirmed for the providers and refuted for the recommended route.** Zoomstack has no expiry, and a six-month-old road map is harmless under a heatmap [J]. **What does recur on every route is the space on the phone.** About 0.8 GB stays on the device for anyone who opens the heatmap [E, §5.2]. That is a real cost, and it must be stated before the download (§6) [I].

### 3.5 HERE, TomTom and Esri, briefly

- **HERE:** *"Offline maps are only available with the Navigate license"*, and regions run *"from entire continents and countries"* down to cities [E, [HERE offline maps](https://docs.here.com/here-sdk/docs/android-offline-maps)]. The app must tell users that *"Technical, non-personal telemetry data related to map rendering and data usage may be processed by HERE"*, and the SDK uses OAuth credentials [E, [HERE legal and privacy](https://docs.here.com/here-sdk/docs/android-about)]. **Navigate pricing was not retrieved:** the pricing page returned no figures. **No React Native SDK was found** [I, from the absence of one in HERE's docs; not proven]. **Fails PRIV-8 on telemetry.**
- **TomTom:** *"Offline functionality for the Maps and Navigation SDKs for iOS is only available upon request"*. Automatic updates are driven by the user's location and route, which fails limb (b); manual updates would pass [E, [TomTom](https://docs.tomtom.com/navigation/ios/guides/offline/offline-map-setup)]. **Gated behind sales; not a solo-operator dependency** [J].
- **Esri ArcGIS:** permits developers to *"Embed or bundle basemap tile packages in an app"* [E, [ArcGIS licensing considerations](https://developers.arcgis.com/net/license-and-deployment/licensing-considerations/), .NET SDK page]. **This is the only major commercial provider I found whose terms allow bundling.** It needs an ArcGIS licence or account, has no React Native SDK [K, moderate], and its UK basemap's data sources were not established. Not pursued further. It offers nothing Zoomstack lacks except NI coverage, and it adds a commercial licence [J].

---

## 4. Privacy-focused providers, against the real constraints

"Privacy-focused" is treated as a marketing claim until the terms back it.

| Provider | Offline, or one-time whole-UK download? | Telemetry, keys, licence checks | UK incl. NI | Licence | RN heatmap both | Size | Cost | Solo-operator dependability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **OpenFreeMap** | **Public service is online only.** Downloading a UK pack tile by tile from it would breach its terms, which prohibit attempts to *"collect data from the service in automated ways without permission"*. **But it publishes *"Weekly full planet downloads both in Btrfs and MBTiles formats"***, from which Candour could cut the UK once and ship it (= row B) | Public service: *"no registration, no user database, no API keys, and no cookies"*. Logs *"do not contain IP addresses"* outside incidents, but it sits behind Cloudflare [E, `map-tiles-note.md` §2.1, single source] | Full | Software MIT; **data is OpenStreetMap, so ODbL**; schema OpenMapTiles | Yes, via MapLibre | Planet file sizes not stated; UK comparable to row B [I] | £0 | **One person** (Zsolt Ero), donations; *"I don't offer SLA guarantees"*; ToS: *"may discontinue it at any time without notice"* | 
| **Protomaps (PMTiles)** | **Yes.** Daily planet builds; `pmtiles extract` cuts a region. **Measured in §5** | None in the data. `.pmtiles` is *"an open specification in the public domain"* | Full | Tiles are *"Produced Works of the OpenStreetMap dataset under the Open Database License"* and need *"© OpenStreetMap"* on the map. Software BSD-3; styles CC0 | Yes, via MapLibre | **0.69–0.79 GB (z14, trimmed), measured** | £0 | Good activity (basemaps pushed 2026-09-11, PMTiles 2026-09-16 [E, GitHub API]); a small company [K]. **The file keeps working even if the project stops** [I] |
| **VersaTiles** | Yes: downloads *"for the whole world"*; self-hostable | *"Does not track your users"* (a self-description) | Full | FLOSS; data OSM, so ODbL [I] | Yes, via MapLibre | Not stated | £0 | Grant-funded (NLnet NGI0 Commons Fund); `versatiles-rs` MIT, pushed 2026-09-22 [E, GitHub API] |
| **MapTiler** | Hosted API is online. On-prem data can be self-hosted | Hosted: API key | Full; UK data *"Contains OS data © Crown copyright"* under OGL [E] | ODbL plus OpenMapTiles attribution; must show *"© MapTiler"* and *"© OpenStreetMap contributors"* [E] | Yes, via MapLibre | Not retrieved | **On-prem Standard $2,500/yr, "internal app only (no B2B or B2C)"**, max 500 MAU. Consumer use needs a **custom annual contract** [E] | Commercial vendor |
| **Organic Maps** | Offline by design, **but only in its own app.** The iOS API *"Open[s] Organic Maps Application"* to *"Show one or more points"* [E] | n/a | Full | API BSD-2 | **Cannot be embedded** | n/a | n/a | n/a |
| **OsmAnd** | Offline by design, inside its own app | n/a | Full | *"covered by GPLv3 (for code)"*; artwork CC-BY-NC-ND [E] | No; GPLv3 would reach Haunts' own code if embedded [K, high] | n/a | n/a | n/a |

**Sources for the table:** [OpenFreeMap](https://openfreemap.org/), [OpenFreeMap ToS](https://openfreemap.org/tos/), [Protomaps downloads](https://docs.protomaps.com/basemaps/downloads), [Protomaps basemaps README](https://github.com/protomaps/basemaps), [VersaTiles](https://versatiles.org/), [MapTiler copyright](https://www.maptiler.com/copyright/), [MapTiler on-prem pricing](https://www.maptiler.com/data/pricing/), [Organic Maps iOS API](https://github.com/organicmaps/api-ios), [OsmAnd LICENSE](https://github.com/osmandapp/OsmAnd/blob/master/LICENSE). All retrieved 2026-09-22/23. **OpenFreeMap's and VersaTiles' privacy statements are single-source self-descriptions.**

### 4.1 The finding, stated plainly

**None beats Zoomstack plus MapLibre, and Overture does not change that (§4.4).**

- **The genuinely private ones, used offline, are all OpenStreetMap data.** They are Protomaps, OpenFreeMap's downloads and VersaTiles. Offline, each is as private as Zoomstack. **Each carries ODbL.**
- **Protomaps asserts "Produced Work".** The OSMF guideline's own test is *"If the published result of your project is intended for the extraction of the original data, then it is a database and not a Produced Work"*, and the guideline *"does not mention vector tiles"* [E, [OSMF Produced Work guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Produced_Work_-_Guideline)].
- **That reading would decide the architecture, and that is Constitution 6.1's trigger:** *"third-party licence terms whose interpretation determines a product's architecture or cost, receives review by qualified human professionals."* The CGO has marked ODbL as a boundary. **Zoomstack's OGL has no share-alike term to interpret.**
- **The online ones fail limb (b)** for the same reason every viewport request does.

### 4.2 Where OSM beats Zoomstack: Northern Ireland

Row B covers NI and Zoomstack does not. **This is the only axis on which a privacy-focused OSM source beats the recommendation.** [I]

### 4.3 Northern Ireland options

| Option | Licence | Size | Verdict |
| --- | --- | --- | --- |
| No basemap in NI, stated on the map's face (LOOK-2(h)) | n/a | 0 | **Recommended for launch** [J] |
| OSM-derived NI-only layer | ODbL | ~28 MB full to z14, less trimmed [E, §5] | **CGO to rule.** Small, but it brings ODbL into the product for 3% of UK users |
| OSNI Open Data StreetMaps | OGL (*"UK Open Government Licence (OGL)"*) | 492,227,713 bytes, **raster**, cities and towns only | Too heavy and raster; not recommended [J] |

**Why there is no OGL vector road layer for NI.** The OSNI product list offers vector gazetteers and boundaries, but **no open vector road network** [E, [nidirect OSNI product list](https://www.nidirect.gov.uk/articles/osni-open-data-product-list); [OSNI StreetMaps](https://www.opendatani.gov.uk/@land-property-services-ordnance-survey-of-northern-ireland/osni-open-data-streetmaps)].

### 4.4 Overture Maps (added 2026-09-26 at the CEO's request)

**Why it is worth asking.** Overture is backed by Amazon, Meta, Microsoft and TomTom, and Candour already uses its Places theme for the venue index. Its Base and Transportation themes carry land, water and roads.

**The licence of each theme, checked at source** [E, Overture's attribution and licensing page, generated per-theme text, [docs.overturemaps.org/attribution](https://docs.overturemaps.org/attribution/) and its source in [OvertureMaps/docs](https://github.com/OvertureMaps/docs); theme guides for [Base](https://docs.overturemaps.org/guides/base/), [Transportation](https://docs.overturemaps.org/guides/transportation/) and [Divisions](https://docs.overturemaps.org/guides/divisions/); all retrieved 2026-09-26]:

| Theme | What it would give a basemap | Licence at source | Non-ODbL parts |
| --- | --- | --- | --- |
| **Base** | Land (the coastline), water, land use (parks), land cover, infrastructure, bathymetry | **"License for theme: ODbL"**. The guide: *"the base theme is published under the ODbL license"*. Land, water, land use and infrastructure come from OpenStreetMap | **Land cover** from ESA WorldCover (*"CC BY 4.0"*); **bathymetry** from ETOPO1 (PDDL) and GLOBathy (*"CC0 1.0 (assumed)"*) |
| **Transportation** | Roads | **"License for theme: ODbL"**. *"Because it includes OpenStreetMap data, the transportation theme is published under the ODbL license"*. Its sources: OpenStreetMap, *"enhanced with commercial road data from TomTom"* | **None published separately.** TomTom's contribution is inside the ODbL theme |
| **Divisions** | Boundaries, and country and land outlines | **"License for theme: ODbL"** | geoBoundaries and others (CC BY 4.0) are mixed into the ODbL theme |
| **Buildings** | Not needed | **ODbL** | n/a |
| **Places** | Points only (already used for the venue index) | **No single theme licence.** CDLA Permissive 2.0 (Meta, Microsoft and others), Apache 2.0 (Foursquare), CC0 (AllThePlaces) | All of it |

**The CGO's earlier note is confirmed at source**, with one refinement. Base is ODbL as a theme, but two of its feature types (land cover and bathymetry) come from permissively licensed sources.

**Does any combination avoid ODbL? Only one, and it is not a usable basemap.** Places points, ESA WorldCover land cover and bathymetry together give:

- **Included:** coarse land-cover patches (trees, grass, built-up and similar, from 10 m satellite classification [K, moderate]), sea depth, and venue points.
- **Missing:** roads, and a coastline (Base's land polygons are OpenStreetMap).

A city-centre heatmap needs the street grid, so this fails the job [I].

**Two further cautions:**

1. **Extracting WorldCover features from an ODbL-published theme and treating them as CC BY 4.0** is itself an interpretation of the theme's licence. That is Constitution 6.1 territory [I].
2. **Candour already has every non-ODbL piece it would take from Overture.** Zoomstack's woodland and greenspace layers cover land cover, and the venue index covers places [I].

**Finding: Overture does not give a basemap without ODbL. Its roads, water and coastline are ODbL for the same reason the OpenStreetMap providers' are: they are OpenStreetMap.** [E for the licences, I for the conclusion]

- **Against row B:** Overture adds TomTom road enrichment and a well-funded foundation, but no ready-made vector tiles. Candour would have to build tiles from GeoParquet [K, moderate: Overture distributes GeoParquet; I did not retrieve a tile product].
- **Size:** I did not measure an Overture-built tileset. I expect it close to row B's, since the geometry is largely the same OpenStreetMap geometry [J].

**What would overturn this:** Overture relicensing a theme away from ODbL, or publishing a permissively licensed road layer separately (for example TomTom's contribution on its own). I found neither.

---

## 5. The size measurement

### 5.1 What was measured

**OS Open Zoomstack itself, in full.** The CEO approved the download on 2026-09-26 ("Yes please"), relayed by the coordinator. It went into the session scratchpad for measurement only. **Nothing entered the repository, and nothing was spent.**

- **The file:** `OS_Open_Zoomstack.mbtiles`, **2,852,712,448 bytes**, from the OS Downloads API. Its MD5 `04c5ebcfa98447fab9925803dcbf7497` **matches the checksum OS publishes for it** [E, [OS Downloads API, OpenZoomstack](https://api.os.uk/downloads/v1/products/OpenZoomstack/downloads)]. The spec page's *"Approximately 2.6GB"* is 2.6 GiB, the same file.
- **From the file's own metadata** [E, read from the file]:
  - **Zoom 0 to 14.** This settles the maximum zoom, which the docs did not state.
  - **18 layers:** sea, names, rail, waterlines, etl, foreshore, sites, railwaystations, roads, greenspaces, contours, buildings, boundaries, airports, woodland, national_parks, urban_areas, surfacewater.
  - **721,319 tile positions at zoom 14**, served by 185,569 unique tiles (identical tiles are stored once).
- **Method: every tile, not a sample.**
  1. Decode all 185,569 unique vector tiles.
  2. Keep only the heatmap's layers, **byte-for-byte unchanged**, and recompress (gzip, level 9).
  3. De-duplicate the results, then sum for each maximum zoom.
- **Checked against a real file.** I then wrote one variant out as an actual MBTiles file and measured it on disk.
- **Scripts:** `zs/trim.py`, `zs/agg.py`, `zs/agg2.py` and `zs/build.py` in the session scratchpad. They reproduce every figure below in under two minutes [I].

**The layer sets tested:**

| Name | Layers kept | What it gives the heatmap |
| --- | --- | --- |
| **Core** | sea (the outline of Great Britain), surfacewater, waterlines, greenspaces, woodland, roads | Roads, water, green space, outline |
| **Core + names** | Core + names | Adds place and street names |
| **Lean** | Core + names, **without waterlines** (streams and small rivers drawn as lines; wide rivers stay as surfacewater polygons) | Drops the streams |

**Dropped from every set:** buildings, contours, rail, boundaries, sites, airports, railway stations, national parks, urban areas, foreshore, etl.

### 5.2 Results: OS Open Zoomstack, Great Britain (MB = 10⁶ bytes)

| Maximum zoom, and where zoom 14 is kept | Original (all 18 layers) | Core | **Core + names** | Lean |
| --- | --- | --- | --- | --- |
| To zoom 12 | 523 | 255 | 281 | — |
| To zoom 13 | 1,029 | 505 | **551** | 443 |
| **Zoom 14 in built-up areas only**: z14 tiles whose buildings layer is ≥5 KB (35,814 of 721,319) | — | — | **760** | 636 |
| Zoom 14 where the buildings layer is ≥10 KB (22,964 tiles) | — | — | 709 | 592 |
| Zoom 14 everywhere | 2,639 | 899 | **971** | 796 |

**Checked against a real file.** The "core + names, z14 built-up" variant, written out as a real MBTiles file (277,388 tiles), is **839,417,856 bytes on disk**. That is about 10% above the 760 MB sum of its tiles, because of SQLite's index and page overhead. **gzipped for download it is 772 MB** [E, measured]. A PMTiles archive of the same tiles should land near the tile sum, because its directory is compact [K, moderate]. I did not build one: I have no PMTiles tool installed, and I did not install software for this.

**What fills a zoom-14 tile before trimming:**

| Layer | Share |
| --- | --- |
| buildings | 53% |
| contours | 21% |
| roads | 7% |
| woodland | 7% |
| waterlines | 4% |
| surfacewater | 4% |
| names | 2% |

**At zoom 13, contours are the largest layer**, at 25%. **The trim removes about three-quarters of zoom 14, and about half of zooms 12 to 13.** [E, measured]

### 5.3 What it means

1. **The real figure: about 0.76–0.84 GB** for the heatmap's basemap of Great Britain at city-centre street zoom. That is roads, water, green space, outline and names, with zoom 14 in built-up areas. **It replaces the unmeasured range.**
   - **To zoom 13 only:** 0.55 GB.
   - **Zoom 14 everywhere:** 0.97 GB.
   - **The cheapest usable cut** (no streams, zoom 14 only in the densest built-up tiles): **0.59 GB**. [E]
2. **Bundling is ruled out, and a single store pack is confirmed.**
   - **Bundling:** even zoom 12, which cannot draw a street grid (`map-tiles-note.md` §2.2), is 0.28 GB against the ~150 MB bar.
   - **Store pack:** every usable variant fits Google Play's *"1.5GB"* per asset pack [E, [Play size limits](https://support.google.com/googleplay/android-developer/answer/9859372)]. [I]
3. **My 2026-09-23 guess was wrong in the product's disfavour.** I said Zoomstack would *"probably come out somewhat smaller"* than the OSM equivalent. **It is larger.** OSM covered all of the UK at 0.69–0.79 GB (§5.5); Zoomstack covers only Great Britain at 0.76–0.84 GB. **Why it is heavier is not established.** Woodland and waterlines are large shares of Zoomstack's trimmed tiles, but I did not compare the two sources layer by layer [I]. **The difference is not large enough to change the recommendation**, because the licence argument (§4.1) does not depend on size [J].
4. **"Built-up" here is a proxy.** It means zoom-14 tiles with dense building data, about 76,000 km² of Great Britain [I: 35,814 tiles × ~2.1 km² each at 53°N]. That includes towns and many villages. **The build should key zoom 14 to where the venue index has venues** (`map-tiles-note.md` §7.1). That is likely smaller, and it is the right rule. It was not measured here, because the venue index is not on disk in this repository [E, `venue-index-harness/` holds scripts, not data].

**The iOS delivery caveat.** Apple-hosted asset packs (`AssetPackManager`) are available from **iOS 26.0** [E, [Apple documentation](https://developer.apple.com/documentation/backgroundassets/assetpackmanager), platform metadata]. The wider Background Assets framework dates from iOS 16 [search summary only]. **Haunts has no stated minimum iOS version** [E, grep of `requirements.md`]. If it supports iOS 25 or earlier, older phones need another delivery route, and **that must not be a Candour-run server** (`map-tiles-note.md` §5.3).

### 5.4 What the spike still needs (about 1 day now [J])

The download and the size measurement are done. What remains:

1. **Key zoom 14 to the venue index**, and re-measure (§5.3 item 4).
2. **Render the trial file** in MapLibre with the heatmap layer on. Use central London, Manchester and a market town, on a mid-range Android phone and an iPhone, and record frame time. **This is the only remaining gate on the recommended route.**
3. **Confirm the OS attribution string at primary.** The file's metadata carries no attribution field [E: the metadata table holds only centre, format, zoom range, name and the layer list].
4. **Report against the bar.** Size is now known to be in the store-pack band (**150 MB – 1.5 GB**), so the size limb is settled. **If frame time fails, the heatmap waits, and the ranked list ships regardless (D13).**

**Scratchpad housekeeping:** the 2.85 GB original and the 0.84 GB trial file sit in the session scratchpad, not in the repository. They can be deleted after the render test.

### 5.5 The earlier OpenStreetMap measurement (2026-09-23), kept for row B

Made before the Zoomstack download was approved. **It now serves row B (an OSM basemap) and the Mapbox pack count, not row A.** The source was Protomaps' planet build of **2026-09-20**, **138,154,043,428 bytes**, at `build.protomaps.com` [E, HTTP headers and the [build list](https://build-metadata.protomaps.dev/builds.json)]. **Nothing was downloaded to disk as a dataset.**

1. **The file's index.** I read the PMTiles header, the root directory and 32 leaf directories through HTTP range requests. That gave the exact stored byte length of **every UK tile at every zoom from 0 to 15**, with no tile content fetched.
2. **"UK".** Tiles whose centre or corners fall inside a hand-drawn polygon of Great Britain (with Orkney, Shetland and Scilly) and a second of Northern Ireland. The Isle of Man and the Republic are excluded. **The polygon is coarse, about 50 vertices from my own knowledge [K].** It over-counts coastal sea tiles, which are small.
3. **Sampling for the trim.** At each zoom from 10 to 15, I read **six contiguous blocks of about 0.6 MB**, placed at random in proportion to bytes. That came to 64 to 1,634 tiles per zoom and **about 25 MB of range reads** in total, held in memory and not kept. I decoded each vector tile and re-encoded it three ways, compressing each the same way:
   - (i) keep the earth, water, landuse, landcover, roads and places layers, and drop buildings, points of interest, transit and boundaries;
   - (ii) as (i), with landuse cut to **green space only** (parks, woods, grass, reserves, cemeteries and similar);
   - (iii) as (ii), with **footpaths removed** from roads.

   Each ratio was then applied to that zoom's exact total.

**Scripts:** `pm/uk.py`, `pm/sample2.py` in the session scratchpad, not in the repository. They can be re-run [I].

**Results (GB + NI, OSM data, MB):**

| Max zoom kept | All layers (as published) | Layers trimmed (i) | + green space only (ii) | + no footpaths (iii) |
| --- | --- | --- | --- | --- |
| 12 | 295 | 283 | 182 | **177** |
| 13 | 636 | 587 | 412 | **375** |
| **14 (street grid)** | **1,272** | 1,018 | **786** | **689** |
| 15 | 2,559 | 1,758 | 1,459 | 1,282 |

**Other measured figures:**

- **Per-zoom totals, all layers:** z12 168.5 MB · z13 340.2 MB · z14 636.8 MB · z15 1,286.3 MB. **Each zoom roughly doubles**, as Protomaps states.
- **Northern Ireland's share:** 28.0 MB at z14; NI adds about 4% to any row.
- **What fills a z14 tile:** landuse 31%, roads 30%, **buildings 26%**, points of interest 5%, water 5%.
- **Street detail only where tiles are built-up.** Keeping z14 only for tiles of 10 KB or more (11% of z14 tiles, holding 47% of z14 bytes) gives **~520 MB** for (iii). This is [I]: it applies the average trim ratio to urban tiles.
- **Tile counts in the UK mask:** 2,601 at z11 (2,448 GB + 153 NI) · 36,243 + 2,062 at z13 · 143,444 + 8,007 at z14. **The z11 count is the Mapbox pack count used in §3.3.**

**Confidence.**

- **The per-zoom totals are exact** for this build and this polygon [E].
- **The trim ratios are estimates.** They come from 6 clustered samples per zoom, and I would put them at **±20%** [J].
- **The polygon's coast over-count** pushes every figure up slightly [I].


## 6. What each option does to the privacy wording

The approved text is at `requirements.md` §12.2.8 (D14(c)). Its key sentence: *"Haunts sends your data nowhere else. If a photo you attached is kept in iCloud Photos or Google Photos, your phone may fetch it from there to show it to you."*

| Option | Effect on the sentence | Suggested addition (CGO to check as a contract term; CEO to approve) |
| --- | --- | --- |
| **A, bundled** | **None.** | None |
| **A, store pack (the likely case)** | **Stays true.** Adds one disclosed download that contains no user data [I] | *"The first time you open the map, your phone downloads a map of Great Britain from the App Store or Google Play (about [size]). It is the same map for everyone, and it stays on your phone."* |
| **B, OSM pack** | As A, plus an **ODbL attribution** on the map | As A, "the UK" |
| **C, platform maps** | **Contestable.** The viewed area is derived from the journal, and the providers say they receive it (§2.1). §12.2.8 already records that an online source makes the sentence *"false again"* | *"When you open the map, your phone asks Apple (on iPhone) or Google (on Android) for map images of the area on screen. They can see which area you are looking at."* **And PRIV-8 and DATA-6 must be rewritten** |
| **C′, opt-in each time** | As C, but **only after a tap** | *"The map starts without streets. If you choose "Show street map", your phone asks Apple or Google for map images of the area on screen, and they can see which area that is."* |
| **F, Mapbox offline** | **False as written.** The SDK sends location and usage data (§3.3) | Would need to disclose Mapbox telemetry. **PRIV-8 fails** |

---

## 7. Recommendation

**Build the heatmap on a trimmed OS Open Zoomstack basemap, rendered by MapLibre, delivered once through the App Store and Google Play as a whole-Great-Britain pack.**

- **Northern Ireland** gets the no-basemap view at launch, stated on the map's face, pending the CGO's view on an NI-only OSM layer.
- **If the spike fails its bar, the heatmap waits.** If the CEO would rather have a heatmap than wait, **the honest fallback is C′** (platform maps, opt-in each time, disclosed), **not C.**

**The reason, in one sentence:** it is the only option that keeps *"Haunts sends your data nowhere else"* true on the product's most revealing screen, costs nothing to run, has no expiry and no telemetry, and has a licence with nothing to interpret. **Against it:** a worse map than Apple's or Google's, no Northern Ireland, about 0.8 GB on the phone, and 30–45 more hours to build.

**Does the provider-offline route change it? No.** The CEO's principle is correct: a whole-country download passes limb (b) from anyone. But no provider offers it cleanly.

- **Apple and Google do not offer offline maps to third-party apps.** Their terms forbid it (§§3.1–3.2).
- **Mapbox offers it, but not cleanly.** It fails on telemetry that Candour is forbidden to suppress, a 30-day expiry, a pack cap below the UK's size, and a ban on bundling (§3.3).
- **HERE and TomTom** add paid licences, telemetry or a sales gate (§3.5).

**The principle does usefully confirm one thing:** the store-pack delivery of Zoomstack is clean for exactly the reason the CEO gave.

**What the recommendation costs** (at the CFO's £32.71/h; hours are [J]):

| Route | Build | Running | Upkeep |
| --- | --- | --- | --- |
| **A, store pack (recommended)** | 55–95 h = **£1,799–£3,107** | **£0** | 8–12 h/yr = **£262–£393/yr** |
| A, bundled (only if the spike lands ≤150 MB) | 40–70 h = £1,308–£2,290 | £0 | 6–10 h/yr = £196–£327/yr |
| C, platform maps | 25–50 h = £818–£1,636 | £0 in fees | Plus an **unpriced** 6.1 legal review and CGO controller work |
| C′, opt-in platform maps | 30–55 h = £981–£1,799 [J: C plus the opt-in control and its copy] | £0 | As C |

**Constitution 1.5's justification for the extra labour of A over C:** *"Operating cost discipline is an ethical obligation, because our customers pay our costs."* The extra £981–£1,472 of build labour (point estimates) buys the claim customers are paying for. C's saving is not a real saving while two of its costs are unpriced. [J]

**For the CFO:** LOOK-2 is still among the unsized requirements (`cost-sheet-v3.md` §4.6). **Carry 55–95 hours**, not the 40–70 in my previous note, because the measurement points to the store-pack route.

---

## 8. For the CEO: nothing to decide today

**Done:** the download you approved on 2026-09-26. The real size is **0.76–0.84 GB** (§5.2), which puts the basemap in the store-pack band.

**Next, and not a decision:** the render test in §5.4, about a day.

**Decisions that come later, one at a time, and not yet:**

1. After the render test: the store-pack sentence (§6), with the size stated as about 0.8 GB.
2. The CGO's ruling on NI.
3. Only if the spike fails: wait, or C′.

---

## 9. What would overturn these findings, and where I looked

| Finding | What would overturn it | Where I looked |
| --- | --- | --- |
| **Apple offers no offline packs to third-party apps** | A MapKit offline API, or Apple's written permission under §2.5's opening words | Apple DPLA Attachment 6 in full; Apple Developer Forums thread 765857; web searches for MapKit offline. **Not read:** the MapKit framework reference in full |
| **Google offers none, and forbids it** | A Service Specific Term permitting offline Maps SDK content | Google Maps Platform Terms §3.2.3 (retrieved in full as HTML); Service Specific Terms (full text searched for "Maps SDK", "offline", "cach"); Map Tiles API policies; Maps SDK docs search (no offline guide found) |
| **Mapbox offline fails PRIV-8 and forces 30-day refreshes** | A Mapbox agreement lifting §2.9.1's data flow and §2.8.1's 30-day limit; or Mapbox confirming in writing that §2.8.1 does not apply to TileStore regions (the 30-day point only) | Mapbox Product Terms PDF of 21 July 2026, read in full; offline concepts (iOS and Android); tile pack glossary; offline help; manage-offline-data; pricing. **The *"subject to change"* sentence on the 750 cap was seen only in a search summary** |
| **No privacy-focused provider beats Zoomstack** | A provider with OGL-grade (no share-alike) UK vector data including NI, deliverable as one file, with no telemetry. **Or** the CGO or a qualified reviewer ruling that OSM vector tiles are a Produced Work, which would promote row B to equal-or-better, since it covers NI | OpenFreeMap (home, ToS), Protomaps (downloads, README licensing), VersaTiles, MapTiler (copyright, on-prem pricing), Organic Maps API, OsmAnd licence, HERE, TomTom, Esri, OSNI products. **Not surveyed:** Stadia Maps, Geoapify, OS's own online Vector Tile API (online, so it fails limb (b) regardless [I]), Mappable |
| **Bundling is out at street zoom** (Zoomstack, 0.76–0.84 GB) | A basemap that draws a city-centre street grid in ≤150 MB. That would need zoom 14 confined to a small fraction of GB, far below the 35,814 tiles measured, or a lighter data source. Keying z14 to the venue index will shrink the figure, but z13 alone is already 0.55 GB, so **I judge ≤150 MB out of reach** [J] | Every tile of OS Open Zoomstack (June 2026 release file, MD5-verified), §5.2 |
| **No combination of Overture themes gives a usable basemap without ODbL** | Overture relicensing Base, Transportation or Divisions away from ODbL; or a non-OSM road source entering Transportation under a permissive licence *and* published separately | Overture's attribution and licensing page (generated per-theme source, read in full for Base, Buildings, Divisions, Places, Transportation); theme guides for Base, Transportation, Divisions |
| **Platform maps lose on the claim** | A CEO decision (5.4) that the claim may cover a disclosed viewport request. That is policy, not fact, and C′ is the form it should take. Or Apple extending its Maps-app privacy statement to MapKit in writing | Apple Maps & Privacy page; Google Android SDK data disclosure; Google terms §4.4 |

---

## 10. Evidence register

**Read from disk this session:** `constitution.md` v1.3 in full; `roles/cto.md`; `pipeline/evidence-standard.md` v1.1; `products/haunt/map-tiles-note.md` in full; `decisions/2026-09-16-haunt-gate.md` D1 and D9–D18; `products/haunt/requirements.md` (LOOK-2, PRIV-1, PRIV-8, DATA-6, PHOTO-11, §12.2.8, §18); `products/haunt/cost-sheet-v3.md` (§4.6, F2, the labour benchmark); `products/haunt/android-and-stack-note.md` §§0–1.

**Retrieved 2026-09-22/23, all linked in the text:**

- **Apple:** DPLA Attachment 6 §§2.5–2.7 and the MapKit revocation clause; DTS forum thread 765857 (single source); Maps & Privacy page; AssetPackManager platform metadata.
- **Google:** Maps Platform Terms §§3.2.3 and 4.4 (with revision dates); Maps Service Specific Terms; Map Tiles API policies; Android SDK data disclosure; pricing (Maps SDK *"Unlimited"*).
- **Mapbox:** Product Terms (21 July 2026 PDF); offline concepts (iOS and Android); tile pack glossary; offline help; manage-offline-data; pricing.
- **Other commercial providers:** HERE offline maps and legal/privacy; TomTom iOS offline setup; Esri licensing considerations.
- **Open and privacy-focused providers:** OpenFreeMap home and ToS; Protomaps downloads, basemaps README, build list and planet headers; VersaTiles; MapTiler copyright and on-prem pricing; Organic Maps iOS API; OsmAnd LICENSE.
- **Licences and UK data:** OSMF Produced Work guideline; OGL v3.0; OS Zoomstack documentation and technical specification; OSNI product list and StreetMaps; dev.to Zoomstack PMTiles write-up (single source).
- **Stores and libraries:** Play size limits; `maplibre-react-native` source (HeatmapLayer and OfflineManager exports, iOS heatmap style code, v11.4.0 of 2026-09-19); `react-native-maps` heatmap doc and README (v1.29.8); Expo Maps; GitHub API metadata for eight repositories.

**Measured this session:**

- **§5.2 (2026-09-26):** every tile of OS Open Zoomstack, from the MD5-verified OS file, trimmed and recompressed in full, plus one variant written to disk as a real MBTiles file.
- **§5.5 (2026-09-23):** exact per-zoom byte totals for the OSM equivalent, from the PMTiles directories, plus sampled trim ratios.

**Retrieved 2026-09-26:** OS Downloads API listing for OpenZoomstack (size and MD5); Overture attribution and licensing page and its generated per-theme source; Overture theme guides for Base, Transportation and Divisions.

**Search summaries relied on, flagged:** Mapbox's *"subject to change"* on the 750 cap; Background Assets from iOS 16.

**Not re-retrieved this session, carried from `map-tiles-note.md` (retrieved 2026-09-22):** OpenFreeMap's privacy page; Apple DTS thread 127493 on MapKit pricing (single source, 2020); Google §3.2.3(d) and the controller terms. Each is marked where used.

**Re-derivation owed under gate Condition 6:**

- the hour-to-pound conversions in §7;
- the Mapbox pack arithmetic (2,601 ÷ 750 ≈ 3.5);
- the 30-day refresh figure (1.3 GB × 12 ≈ 15 GB);
- the size table in §5.3, which a second seat can recompute from the scripts.

**Clauses quoted in the passage they support:** Constitution 1.5, 5.4 and 6.1; Apple Attachment 6 §§2.5 and 2.7 and the MapKit revocation clause; Google §§3.2.3(a)–(b) and 4.4(a); Mapbox Product Terms §§2.8.1 and 2.9.1–2.9.4; OGL v3.0; the OSMF Produced Work test.

---

## 11. Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | **Created.** Answers the CEO's request to weigh offline against platform maps evenly, test provider offline packs, and survey privacy-focused providers. **Measured** the trimmed UK basemap on OSM data: **~690–790 MB at street zoom**, withdrawing the note's 100–400 MB estimate. **Found** that Apple and Google offer no offline packs to third-party apps, and that Mapbox's offline route fails PRIV-8 on mandatory telemetry and carries a 30-day cache limit and a 750-pack cap. **Recommendation unchanged in kind** (offline Zoomstack + MapLibre); the delivery route moves from bundled to a one-time store pack, and LOOK-2's sizing moves to 55–95 h. Names C′ (opt-in platform maps) as the honest fallback if the CEO prefers a heatmap to waiting. Zoomstack itself not downloaded: it needs the CEO's own go-ahead. **Not a certification.** |
| 2026-09-26 | **Zoomstack measured.** On the CEO's approval of 2026-09-26, relayed by the coordinator, downloaded OS Open Zoomstack (2,852,712,448 bytes, MD5 matching OS) into the scratchpad. Trimmed every tile. **Real figure: 0.76–0.84 GB** for GB (roads, water, green space, outline, names; z14 in built-up areas); 0.55 GB to z13; 0.97 GB z14 everywhere. **Replaces the unmeasured 0.4–0.8 GB range and corrects my guess that Zoomstack would be smaller than OSM: it is slightly larger.** Bundling ruled out; one store pack confirmed. §5 rewritten, with the OSM measurement kept as §5.5. **Overture Maps added** as row B′ and §4.4: Base, Transportation and Divisions are ODbL at source, and no non-ODbL combination yields roads or a coastline. §8 no longer asks for a decision. **Not a certification.** |

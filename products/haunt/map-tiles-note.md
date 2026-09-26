# Haunts: where the heatmap's map tiles come from, and what they cost

**Seat:** Chief Technology Officer · **Date:** 2026-09-22 · **Status:** A technical finding and a recommendation. **It prepares and flags. It does not certify** (Constitution 6.1). Choosing a tile source that sends anything off the device is a change to user-data policy, and Constitution 5.4 reserves *"anything affecting user data policy"* to the CEO.

**Slug:** `haunt` · **Product name:** Haunts (D9) · **Answers:** `cost-sheet-v3.md` §4.6 item 2 and flag **F2** (*"No artifact names a map-tile source"*); the referral at D12 (*"the heatmap's map is referred to the CTO on exactly that question"*); `requirements.md` §12.2.8's closing paragraph.
**Decisions bearing on it:** D1 (both platforms), D10 and LOOK-2 (the heatmap), D12 (photo fetch, and the line it draws), D13 (the ranked list is the base view and the heatmap is a second view of the same data).

**Template note.** `pipeline/templates/` holds nine templates and none is a technical note or an ADR [E, listed from disk 2026-09-22]. This note follows the four questions put to this seat, adds the CEO's position as the coordinator relayed it, and carries the overturn clause my charter requires. I am saying so here so the change of format is visible.

**Method.** Every price, term and privacy statement below was retrieved this session, 2026-09-22, and the link sits next to the claim. Nothing is cited from memory. Where a source could not be retrieved at primary I say so and tag it accordingly. **Two things I did not do** are listed in §1, because the recommendation depends on one of them.

---

## 0. The answer, before the working

**Recommendation: draw the heatmap on an offline basemap built from Ordnance Survey's OS Open Zoomstack, rendered on the device by MapLibre, with no tile server at all. Measure the trimmed size first. If the size will not ship, the heatmap waits. Do not put it on online tiles.**

1. **A tile request on this heatmap does send the user's data somewhere, and both platform vendors say so in their own documents.** It does not send the journal. It sends the map area being viewed, at a known time, from an identifiable connection. **A heatmap opens on the user's most-visited area, so the area viewed is a lossy but faithful copy of where they go.** Apple lists *"Boundaries of the map area visible on your device"* among the things sent to Apple when Maps is used [E, [Apple Maps & Privacy](https://www.apple.com/legal/privacy/data/en/apple-maps/)]. Google's terms say it *"collects and receives data from Customer and End Users… including search terms, IP addresses, and latitude/longitude coordinates"* and *"may use and retain this data to provide and improve Google products and services"* [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms) §4.4(a)]. §2.

2. **Requests cannot be made coarse enough to hide anything and still be useful for a city-centre heatmap.** A zoom-14 tile in a UK city is about 1.5 km across. Tiles large enough to hide a neighbourhood (zoom 11–12, 6–12 km) do not contain the streets that make a city-centre heatmap readable. **The two ranges do not overlap.** §2.2.

3. **Money is not the issue.** Every online option costs about **£0 at Haunts' scale**: Google's mobile Maps SDK is listed as *"Unlimited"* with no charge tier; Mapbox's first 25,000 monthly active users are free; MapKit costs nothing beyond the developer membership; OpenFreeMap is free with no key. §3. **The costs are elsewhere:** the product's privacy claim becomes false again; Google's terms make Candour a **controller** by contract; and the CGO has already said that adding a map-data API **triggers qualified human legal review under Constitution 6.1**, which nobody has priced. §3.3.

4. **Apple is a better third party, but still a third party.** On Apple's own description of Maps it holds requests under identifiers that rotate *"multiple times per hour"* and *"convert[s] precise locations to less-exact locations within 24 hours"* [E, same page]. **That page describes the Maps app. I found no Apple statement that says the same about MapKit inside another developer's app.** Apple does not pass D12's test in any case, because Apple's map servers are not *the user's own storage*. And D1 makes Android a Google problem, where there is no equivalent assurance. §4.

5. **An offline basemap is practical for one developer, and the licence is clean.** OS Open Zoomstack covers Great Britain down to street level. It is published under the **Open Government Licence v3.0**, which requires attribution and has **no share-alike term**, so the ODbL problem the CGO flagged does not arise. It is refreshed **every six months** and is **about 2.6 GB** as supplied [E, §5]. **2.6 GB is too big to bundle. The trimmed size, with roads, water, green space and outline only, is my estimate and has not been measured.** Northern Ireland is not covered. §5.

6. **With no basemap at all, the heatmap is worth little. It is a fallback, not the product.** D13 already puts the full answer to "where do I go most" in the ranked list. A heatmap with no ground under it only shows a shape, and the shape tells the user nothing the list does not. §6.

**My disagreement with the CEO's position, stated once.** The CEO's view, as relayed: *a tile request is a network call to fetch map tiles, not a call that sends the user's data anywhere*, and platform providers are easiest to integrate. **On this particular screen that view is wrong.** A tile request's content depends on what the user is looking at. On a heatmap of their own life, what they are looking at is where they have been, and the providers' own terms treat that as data they receive and keep. The CEO is **right** that the journal itself never leaves the device, and **right** that none of this costs money. **"Easier to integrate" is weaker than it looks for this feature:** the React Native heatmap component in `react-native-maps` is *"Supported on Google Maps only"* [E, [react-native-maps heatmap docs](https://github.com/react-native-maps/react-native-maps/blob/master/docs/heatmap.md)], so Apple Maps on iOS would need a hand-built heatmap. `expo-maps` is *"currently in alpha"* [E, [Expo Maps](https://docs.expo.dev/versions/latest/sdk/maps/)]. MapLibre draws heatmaps natively on both platforms (§5.5).

**The rule I propose, so the next case does not need this note.** A network request fits the product's claim if **either** (a) it goes to the user's own storage (D12, the photo fetch), **or** (b) its content does not depend on the user's data. A whole-country map downloaded once is case (b). **A viewport tile request on the heatmap is neither**, and that is why D12's argument does not carry over to it. *[J, CTO. The wording of the claim belongs to the CGO and approving it belongs to the CEO.]*

**This is not a block.** My block covers build commencement on architectures that are *"unsustainable, needlessly expensive, or insecure by design"* (`roles/cto.md`). Online tiles are none of those. **This is a flag and a recommendation.** Online tiles would still fail three BLOCKING acceptance criteria that already stand (**PRIV-1**, **PRIV-8**, **DATA-6**, §9). Removing those is a scope change for the CEO. I cannot waive them.

---

## 1. What I was asked, what I did, and what I did not do

**Asked:** where the heatmap's tiles come from, and what they cost in money, bundle size and privacy, under four headings (online, offline, no map, platform maps), with a recommendation.

**Did:** read the binding documents (§10). Retrieved at primary the terms, prices and privacy statements of Apple (Maps privacy page and the Developer Program Licence Agreement's Attachment 6), Google (Maps Platform Terms, pricing, Android SDK data disclosure, controller terms), Mapbox (pricing, telemetry), the OSM Foundation (tile policy, privacy policy, Produced Work guideline), OpenFreeMap (home page, privacy policy), Protomaps, Ordnance Survey (Zoomstack documentation and technical specification), the Open Government Licence, Geofabrik, Apple's and Google's store size limits, and the MapLibre projects.

**Did not do, and one of these gates the recommendation:**

- **I did not measure a trimmed basemap.** That requires downloading the 2.6 GB Zoomstack file, and I did not download a multi-gigabyte file in this session without the CEO's say-so. **Every trimmed-size figure below is [J] until someone measures it.** The measurement is the spike at §7.1.
- **I did not capture MapKit's or the Google SDK's network traffic.** What each sends per tile is taken from the vendor's own statements, not from observation. A packet capture from a test build would upgrade §2.1 from what the vendor says to what was measured. It is not needed for the recommendation, because the recommendation sends nothing.

---

## 2. What a tile request discloses, and whether it matters

### 2.1 What goes out with each request

A map drawn from a tile server fetches square images or vector tiles addressed by zoom and position (`z/x/y`). **Each request therefore names a square of ground, at a time, from an IP address**, together with whatever the SDK adds:

| Provider | What it says it receives | Source |
| --- | --- | --- |
| **Apple Maps** (the Maps app) | Time of request; device model and software version; input language; device location if authorised; *"Boundaries of the map area visible on your device"*; interactions, including *"the places you view"*. Usage metrics sit under an identifier that *"rotates multiple times per hour, and is not tied to your Apple Account"*. Precise locations are converted to less-exact ones *"within 24 hours"* | [E, [Apple Maps & Privacy](https://www.apple.com/legal/privacy/data/en/apple-maps/)]. **Scope gap:** the page covers Apple's own app. **I found no statement covering MapKit in third-party apps**, and Attachment 6 of the licence agreement says nothing about what Apple logs (§3.3) |
| **Google Maps SDK for Android** | Device metadata; SDK crash data; **IP address**, *"to understand SDK usage and improve Google services"*; a *"Maps SDK-specific pseudonymous identifier"*; and *"Interaction data, such as panning and zooming the map"* | [E, [Maps SDK for Android data disclosure](https://developers.google.com/maps/documentation/android-sdk/play-data-disclosure)] |
| **Google Maps Platform (all services)** | *"search terms, IP addresses, and latitude/longitude coordinates"*, which Google *"may use and retain… to provide and improve Google products and services"* | [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms) §4.4(a)] |
| **Mapbox SDKs** | *"Whenever your application causes the user's location to be gathered, it sends de-identified location and usage data to Mapbox"*. This is on by default, and the terms *"require that you provide a telemetry opt-out option"* | [E, [Mapbox, Mobile applications](https://docs.mapbox.com/help/dive-deeper/mobile-apps/); [Mapbox Telemetry](https://www.mapbox.com/telemetry)] |
| **OSM Foundation tiles** | General logging of *"IP address… browser and device type… operating system… referring web page… date and time"*. A CDN *"could potentially generate a record of your location"*. No retention period stated for tiles | [E, [OSMF Privacy Policy](https://osmfoundation.org/wiki/Privacy_Policy)] |
| **OpenFreeMap** | Server logs *"do not contain IP addresses"*, except during a security incident (up to 30 days). Anonymised logs are kept *"indefinitely"*. *"We may use Cloudflare as a CDN… Cloudflare may collect certain information"* | [E, [OpenFreeMap Privacy](https://openfreemap.org/privacy/)]. **Single source**: the operator describing itself |

**Two things make these requests worse on Haunts than on an ordinary map screen:**

- **The screen opens where the user goes most.** A heatmap is framed on its densest cluster, which for most people is home, work or their regular pub. The first requests on every opening name that square. [I]
- **The request says what kind of app sent it.** SDK traffic normally carries an app-scoped key or identifier, so the provider sees a location-history app asking for map area around a hotspot. It does not see a random map browse. [K, moderate confidence. I did not capture the traffic (§1), and the Google disclosure above confirms a pseudonymous SDK identifier but not what key is sent.]

### 2.2 Can the requested area be made coarse enough?

Ground width of one tile at UK latitudes, from the Web Mercator formula (40,075 km × cos(latitude) / 2^zoom):

| Zoom | London (51.5°N) | Manchester (53.5°N) | Edinburgh (55.9°N) | What a tile at that zoom shows |
| --- | --- | --- | --- | --- |
| 11 | 12.2 km | 11.6 km | 11.0 km | A city region. No minor streets |
| 12 | 6.1 km | 5.8 km | 5.5 km | A town. Main roads only |
| 13 | 3.0 km | 2.9 km | 2.7 km | A district |
| 14 | 1.5 km | 1.5 km | 1.4 km | A neighbourhood. Full street grid in vector schemas |
| 15 | 0.76 km | 0.73 km | 0.69 km | A few streets |
| 16 | 0.38 km | 0.36 km | 0.34 km | A block |

*Arithmetic, recomputable. Owed to a second seat under gate Condition 6.*

**The coarsest request that still draws a city-centre street grid is about zoom 14**, because vector tiles hold their full street detail at their top zoom and the renderer scales up from there. OpenMapTiles-schema tiles are *"generated on zoom levels 0 to 14, but can be overzoomed to level 18+"* [E, search-result summary of the [OpenMapTiles repository](https://github.com/openmaptiles/openmaptiles). **Not read at primary, so flagged**]. Protomaps' tiles run *"from 0 to 15"* [E, [Protomaps downloads](https://docs.protomaps.com/basemaps/downloads)]. **So the best any online vector route can do is tell the provider which ~1.5 km square this user's life centres on.** A 1.5 km square around a hotspot, repeated across openings and paired with an IP address, is enough to identify a neighbourhood. [I]

**Prefetching a whole city to hide the viewport** (for example every zoom-14 tile in a 20 × 20 km box) would reveal only the city. **It is barred by most providers' terms:** OSMF forbids *"any pre-emptive fetching of tiles other than those a user is actively viewing"* and *"Offline use is not permitted"* [E, [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)]. Apple's Attachment 6 §2.5 says Map Data *"may not be cached, pre-fetched, or stored… other than on a temporary and limited basis"* [E, [Apple Developer Program License Agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/), Attachment 6]. OpenFreeMap has no such rule. **Even there, the request is still a network call made by the app, which PRIV-1 and PRIV-8 forbid (§9).**

**Finding: under every online option, a readable request is not coarse, and a coarse request is not readable.** Online tiling fails on this heatmap whichever provider is used. The reason is that the heatmap's zoom and centre come from the journal. Provider policy is not the reason. [I]

---

## 3. Online tiles, option by option

### 3.1 Cost at Haunts' scale

Scale: the CFO's compliant subscriber band is **3,122–4,988** (Condition 9.3, as corrected by the CFO at §17.3 of the decision record). I test at **5,000** and **10,000** users.

| Provider | Price, as retrieved | At 5,000 users | At 10,000 users | Source |
| --- | --- | --- | --- | --- |
| **Google Maps SDK** (Android, iOS) | Free cap: *"Unlimited"*, with no paid tier listed | **£0** | **£0** | [E, [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing), row "Maps SDK"] |
| Google Map Tiles API (raw tiles, not needed here) | 100,000 free per month, then $0.60 per 1,000 | Not used | Not used | [E, same page] |
| **Apple MapKit** (native) | *"no cost beyond your Apple Developer Program membership"* | **£0 extra** | **£0 extra** | [E, [Apple DTS answer, forum thread 127493](https://developer.apple.com/forums/thread/127493), January 2020. **Single source, six years old**] |
| **Mapbox Maps SDK** | Billed per monthly active user: *"Up to 25,000"* free, then $4.00 per 1,000 | **£0** | **£0** | [E, [Mapbox pricing](https://www.mapbox.com/pricing)] |
| **OSMF tile.openstreetmap.org** | Free. *"best-effort: there is no SLA or guarantee"* | £0 | £0 | [E, [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)] |
| **OpenFreeMap** | *"completely free: there are no limits"*. *"no registration, no user database, no API keys, and no cookies"*. Commercial use allowed | £0 | £0 | [E, [OpenFreeMap](https://openfreemap.org/)] |

**Money is not a reason to choose any of these.** A Google project does need a Google Cloud account and an API key on Android (*"register a Google Cloud API project, enable the Maps SDK for Android"*, [E, [Expo Maps](https://docs.expo.dev/versions/latest/sdk/maps/)]). Whether that account also needs a billing method on file is [K, unverified]. If it does, it is a spending set-up and belongs to the CEO under 5.4.

### 3.2 Terms on logging and use

§2.1 covers what each provider receives. What each is **allowed to do** with it:

- **Google** keeps and uses it *"to provide and improve Google products and services, subject to the Google Privacy Policy"* (§4.4(a)). No retention period is stated.
- **Apple**, for the Maps app, rotates identifiers and blurs locations within 24 hours. **For MapKit in third-party apps, nothing retrieved states Apple's practice.**
- **Mapbox** collects telemetry by default and requires an opt-out. That makes it the worst of the five on privacy. **It is eliminated here.**
- **OSMF** gives no tile-specific retention period and is best-effort for commercial app traffic. Its policy welcomes app use, but a paid product that depends on a donated service with no SLA fails Constitution 1.3's plainness test on availability. [J] **Eliminated.**
- **OpenFreeMap** does not log IP addresses in normal operation, but it runs behind Cloudflare, which does its own collection. **It is the best of the online options, and it still breaks PRIV-1.**

### 3.3 Contract consequences Candour would take on

**(a) Google's terms make Candour a data controller, by contract.** §4.4(b): *"Google and Customer agree to the Controller-Controller Data Protection Terms"* [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms)]. Those terms state that *"each party: (a) is an independent controller of Controller Personal Data"* and cover the UK GDPR [E, [Google Controller-Controller Data Protection Terms](https://business.safety.google/controllerterms/) §4.1]. §4.4(c)(iii) also requires Candour to *"notify End Users in advance of… the type(s) of data that Customer intends to collect"* [E, same terms]. **This conflicts directly with the finding the PROCEED rested on:** *"on this architecture Candour is neither controller nor processor of journal data"* (decision record, "What was decided and why"). That finding is about *journal* data and may survive in a narrow sense. **The product's regulatory position would no longer be "nil" on Android.** *Flag to the CGO. Not a determination.*

**(b) Joint controllership for the transmission, on any provider.** The Court of Justice held in *Fashion ID* (C-40/17, 29 July 2019) that a site embedding a third-party plugin *"can be considered to be a controller jointly with Facebook in respect of the collection and disclosure by transmission"* of visitors' data [E, **secondary, a law firm's report**: [Data Protection Report](https://www.dataprotectionreport.com/2019/08/website-operators-joint-controllers-with-third-party-plugin-providers/); the Curia and GDPRhub primaries did not return content]. Whether that reasoning reaches an SDK in a native app, and how it applies in the UK after EU exit, is **[K, low-to-moderate confidence] and not mine to decide.** *Flag to the CGO.*

**(c) The CGO's Constitution 6.1 trigger is pulled.** The CGO wrote, at the gate: *"If the architecture changes to include any places, geocoding or map-data API, it is pulled, and no agent — including me — can un-pull it"* (`proposals/haunt/gate-pack.md`; `compliance-note.md` §6). Constitution 6.1 requires review by qualified human professionals for *"third-party licence terms whose interpretation determines a product's architecture or cost"*. **Adding platform maps means a paid legal review before launch that no cost sheet contains.**

**(d) Google's "no re-creating" clause.** §3.2.3(d): *"Customer will not use the Services to create a product or service with features that are substantially similar to or that re-create the features of another Google product or service"* [E, [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms), retrieved again this session]. Haunts is a private timeline of visited places, and Google Maps Timeline is one too. My feasibility note (§2.1) said *"an architecture whose defensibility depends on a favourable reading of that clause by the counterparty is not an architecture I will sign off."* **Displaying Google's map inside Haunts puts Haunts under that clause.** [J]

**(e) Apple's Attachment 6, if MapKit is linked.** §2.6: *"You may not charge any fees to end users solely for access to or use of the Apple Maps Service"* [E, DPLA Attachment 6]. The heatmap would have to stay outside any paid gate. It is entitlement-blind today, so this is manageable, but it is a constraint the PM/BA would inherit. §4: Apple *"reserves the right to revoke Your access to MapKit… at any time in its sole discretion"* [E, same]. Apple DTS has already declined to interpret §2.5 (`compliance-note.md` §1.3, thread 807656).

### 3.4 Does any online option fit the product's claim?

**The claim can be reworded so it stays true.** For example: *"When you open the map, your phone asks Apple (on iPhone) or Google (on Android) for the map of the area you're looking at."* Article 4 requires a claim to be substantiable, and that sentence is. **So online tiling is not constitutionally forbidden.**

**But it fails on the product's own terms.** Discovery chose the offline architecture because it made the privacy claim substantiable without an explainer (`feasibility-note.md` §2.5), and the requirements call *"literally no outbound calls"* *"the single honest differentiator that survived discovery"* (`requirements.md` §20.1 item 5). A heatmap tile request gives that differentiator up on the most revealing screen in the product (the CEO's own words at D10) in exchange for about 20 hours of integration saved. [J] **My answer: online tiling fails for this heatmap under every provider. OpenFreeMap fails least badly, and it is the only one I would name if the CEO overrules this.**

---

## 4. Platform maps: is Apple a different case?

The question: does MapKit on iOS, which draws Apple's tiles from Apple's servers, count as a third party when Apple is also the device vendor?

**How Apple differs from a third party, and all of it is real:**

- Apple is already a party to every Haunts install: it made the operating system, it delivers the app from the App Store, it takes payment as merchant of record, and it receives crash reports if the user opts in. **No new company enters the picture.** [I]
- For its own Maps app, Apple states rotating identifiers not tied to the Apple Account and blurring of precise locations within 24 hours [E, §2.1]. **That is a stronger published position than Google's or Mapbox's.**

**How Apple is the same as a third party, and this decides it:**

- **It fails D12's test.** D12 accepted the photo fetch because it runs *"from the user's device to **the user's own** storage"*. The user owns their iCloud Photos library. They do not own Apple's map servers. The user chose iCloud and did not choose MapKit. [I]
- **What Apple says about MapKit is unverified.** The retrieved assurance covers the Maps app. The licence terms for MapKit (Attachment 6) contain no data-handling commitment at all. I would not write "Apple blurs it within 24 hours" into store copy on this evidence. [I]
- **D1 means there are two platforms.** "Platform maps" means Apple on iOS and **Google on Android**, where §3.3(a) and (d) apply in full. The product would then carry two different privacy claims, one per platform, and the weaker one describes a controller relationship with an advertising company. [I]

**A trap worth knowing whichever way this goes.** Laying Candour's own offline tiles over a platform map does **not** stop the platform's tiles loading. The `react-native-maps` documentation says *"For Android: LocalTile is still just overlay over original map tiles"* [E, [react-native-maps](https://github.com/react-native-maps/react-native-maps)]. A hybrid of platform map plus local overlay keeps the network call.

**Finding: Apple is a meaningfully better third party than Google or Mapbox. It is not a different kind of party, and on D1's two platforms the question cannot be answered for iOS alone.** [J]

---

## 5. Offline tiles: coverage, licence, size, updates

### 5.1 Sources, and the ODbL question

| Source | Licence | Share-alike? | Coverage | Update cadence |
| --- | --- | --- | --- | --- |
| **OS Open Zoomstack** (Ordnance Survey) | **Open Government Licence v3.0** | **None.** You may *"copy, publish, distribute and transmit… adapt… exploit the Information commercially"*, provided you *"acknowledge the source"* [E, [OGL v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)] | **Great Britain only.** *"Northern Ireland is not included"* (summary of [OS docs](https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-open-zoomstack)). Scale *"1:5 000 000 to 1:10 000"*, i.e. down to street level | *"updated every six months in June and December"* [E, same] |
| OSM-derived vector tiles (Protomaps, OpenMapTiles / OpenFreeMap downloads) | **ODbL 1.0** | **Possibly.** See below | UK and the rest of the world | Weekly to daily builds |
| OSNI Open Data (Northern Ireland) | *"an Open Data licence"*. Licence text not retrieved | Not established | Northern Ireland, product by product: roads, boundaries, 1:50k | Not established |

**The ODbL question is unsettled, and the unsettledness is itself the problem.** Protomaps describes its basemap as distributed *"under the 'Open Database License' as a Produced Work"* [E, [Protomaps](https://docs.protomaps.com/basemaps/downloads)]. A Produced Work carries attribution only. The OSMF's own guideline does **not** name vector tiles: it says only that *"If the published result of your project is intended for the extraction of the original data, then it is a database and not a Produced Work"* [E, [OSMF Produced Work guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Produced_Work_-_Guideline)]. Vector tiles carry the geometry itself, and the geometry can be extracted. If they count as a Derivative Database, ODbL requires that *"Any Derivative Database that You Publicly Use must be only under the terms of: This License"* [E, quoted verbatim in `block-4-ruling.md` §5.3 from [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), retrieved 2026-09-21]. **The licence reading would then decide the architecture, and that is exactly Constitution 6.1's trigger:** *"third-party licence terms whose interpretation determines a product's architecture or cost, receives review by qualified human professionals."* **Using OS Open Zoomstack avoids the question.** OGL has no share-alike term to interpret. [I]

**Attribution string for OS data:** *"Contains OS data © Crown copyright and database right [year]"* [E, **secondary**: quoted in [a 2023 conversion write-up](https://dev.to/hfu/serve-os-open-zoomstack-2022-12-through-pmtiles-1di1) and in search summaries of Ordnance Survey's licensing pages. **OS's own copyright-acknowledgements page returned 404**, so this must be confirmed at primary before it goes on the licence screen]. OS confirms OS OpenData is available *"under the Open Government Licence (OGL)"* [E, [OS OpenData products](https://www.ordnancesurvey.co.uk/products/open-data)].

**Northern Ireland.** Zoomstack does not cover it. On the recommended design, a Northern Ireland user's heatmap falls back to the no-basemap view (§6) until an OSNI layer is assembled. **That is a real gap in a UK product and must be stated on the heatmap's face where it applies** (Condition 8.6's principle that derived views say when they are partial). I have not costed the OSNI layer. [J]

### 5.2 Size

| Artefact | Size | Tag |
| --- | --- | --- |
| OS Open Zoomstack, vector tiles (MBTiles), all 18 layers, Great Britain | **~2.6 GB** (*"Approximately 2.6GB"*) | [E, [OS Zoomstack technical specification](https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-open-zoomstack/os-open-zoomstack-technical-specification)] |
| Same, converted to PMTiles | 2.4 GB | [E, [dev.to write-up](https://dev.to/hfu/serve-os-open-zoomstack-2022-12-through-pmtiles-1di1), **single source**, 2022-12 data] |
| OSM United Kingdom raw extract (`.osm.pbf`) | **2.1 GB**, data to 2026-09-21 | [E, [Geofabrik](https://download.geofabrik.de/europe/united-kingdom.html)] |
| Full OSM UK basemap, zoom 0–14 | **~2 GB** | [I] from the row above and one blogger's rule that tile output up to zoom 14 is *"very roughly comparable to the size of the OSM extract"* [E, [Rothkranz](https://heiko.rothkranz.net/posts/hosting-static-osm-vector-tiles-on-blob-storage/), **single source**] |
| Protomaps, whole planet, zoom 0–15 | ~120 GB. *"Each additional zoom level roughly doubles the size"* | [E, [Protomaps](https://docs.protomaps.com/basemaps/downloads)] |
| **Heatmap basemap, trimmed**: roads, water, green space, coastline, a few place names; no buildings, contours or POIs; street zoom only where the venue index has venues, coarse zoom elsewhere | **~100–400 MB for GB** | **[J], unmeasured.** The two cuts that do most are dropping buildings (probably the heaviest layer [K]) and keeping zoom 14 only over populated areas, since each zoom level roughly doubles size [E, Protomaps]. **This is the number the spike at §7.1 must replace** |
| For scale: the bundled venue index | 23.3 MB on disk / 11.3 MB gzipped | [E, `feasibility-note.md` §2.4 correction] |

**Store limits:** iOS allows **4 GB** uncompressed per app, and Apple-hosted Background Assets allow a *"200 GB"* asset-pack total [E, [Apple, maximum build file sizes](https://developer.apple.com/help/app-store-connect/reference/maximum-build-file-sizes/); [Apple-hosted asset pack size limits](https://developer.apple.com/help/app-store-connect/reference/apple-hosted-asset-pack-size-limits/)]. Google Play allows a **500 MB** base module, **1.5 GB** per asset pack and **30 GB** of on-demand packs, *"hosted and served on Google Play"* [E, [Play size limits](https://support.google.com/googleplay/android-developer/answer/9859372); [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery)]. **Which iOS versions Background Assets requires, and whether Expo supports it, were not retrieved** [K: I believe it is new in iOS 26. Unverified].

### 5.3 Delivery, applying the rule in §0

- **Bundled in the app:** no network call at all. **Preferred if the trimmed size is at or under ~150 MB** [J. The bar is mine, set on download friction for everyone, including people who never open the heatmap].
- **Between ~150 MB and ~1.5 GB: one whole-GB pack, downloaded once through the store** (Apple-hosted asset pack / Play on-demand pack) the first time the user opens the heatmap. The store learns only that this user opened the heatmap. **Nothing in the request depends on where they go**, so it is case (b) of §0's rule. It **is** a network call the app triggers, so PRIV-1 needs one more sentence (§9). Whether that fits the claim is the CEO's decision under 5.4, with the CGO on the wording. **I judge that it does.**
- **Not recommended: Candour hosting the file itself.** Candour would then hold access logs containing IP addresses and become a controller of them, on a product built to have no server. [I] A third-party host such as GitHub Releases avoids the logs but adds a dependency. It is a worse version of the store route.

### 5.4 Updates

Zoomstack refreshes **every six months** [E]. The venue index already needs a refresh process (D2's promise that the bundled venue index is refreshed, and the maintenance rows in `android-and-stack-note.md` §3). **The basemap should ride on the same release train, at twice a year** [J]. A basemap six months out of date is harmless on a heatmap. Roads rarely move, and nothing on the heatmap claims to be current. [J]

### 5.5 The renderer

- **MapLibre Native**: BSD-2-Clause [E, [GitHub licence API, maplibre/maplibre-native](https://github.com/maplibre/maplibre-native)]. It is the open fork of Mapbox's SDK in which *"Tracking of end-users (telemetry) has been removed"* [E, [MapTiler announcement](https://www.maptiler.com/news/2021/06/maplibre-gl-native-open-source-mobile-sdk-for-android-and-ios/). **Single source, and MapTiler is a founding party of the fork**]. Local PMTiles are read through `pmtiles://file://`, *"Starting MapLibre Android 11.7.0"*. `pmtiles://asset://` (files inside the Android app bundle) is **not supported**, so a bundled file must be copied to app storage first, as the venue index already is [E, [MapLibre Android PMTiles example](https://maplibre.org/maplibre-native/android/examples/data/PMTiles/)].
- **Heatmap as a built-in layer type** on both platforms since Android 6.0.0 and iOS 4.0.0 [E, [MapLibre Style Spec, layers](https://maplibre.org/maplibre-style-spec/layers/)]. Nothing needs hand-building on either platform.
- **`@maplibre/maplibre-react-native`**: MIT licence, *"in Expo and React Native supporting Android & iOS"* [E, [repository](https://github.com/maplibre/maplibre-react-native)]. Latest release **v11.4.0, 2026-09-19** [E, GitHub releases API]. It needs a development build, which Haunts already needs for `CLVisit` (`android-and-stack-note.md` §2.1). **No new build constraint.**
- **The build trap, which becomes an acceptance criterion (§9): a MapLibre style loads fonts ("glyphs") and icons ("sprites") from URLs.** A style copied from any public example will quietly fetch fonts from a server. **Every glyph and sprite must be bundled and referenced locally, or the style must use no text.** [K, high confidence. This is how the style spec works, and it is exactly the silent network call PRIV-8 exists to catch.]
- **One advantage for accessibility.** Candour writes the style, so it controls every colour. A11Y-3's *"measured contrast… against the worst-case tile in **both** map styles"* then becomes a measurement against two palettes Candour wrote, not against Apple's or Google's styling, which changes without notice. [I]

---

## 6. No map at all

**What it would look like.** The heatmap's colour field drawn over either nothing, or a **faint dot for every venue in the bundled index**, with the user's own venues labelled by name. The venue dots trace high streets and town centres, because venues cluster along them. This adds zero bytes, needs no new licence (the index's CDLA-Permissive-2.0 attribution already ships, Condition 7) and makes no network call. [I]

**Is it worth anything?** A little. The user orients by their own venue names ("the blob is round the Crown and the Swan"). There are no streets, rivers or parks, so the view cannot show *where in the city* a cluster sits except relative to other labels. **D13 already gives the ranked list the job of answering "where do I go most", and does it completely.** A basemap-less heatmap adds a shape, and the shape tells the user little the list has not already said. [J]

**Its use:** the **Northern Ireland fallback** (§5.1), and the view shown while a store-delivered pack has not yet downloaded (§5.3). **Not the product.** Shipping it as "the heatmap" would be a weak version of a feature the CEO asked for, sold as the feature, and Article 1.3's *"We say what a product cannot do"* would then need a sentence explaining it. [J]

---

## 7. Recommendation

**Build the heatmap on a trimmed OS Open Zoomstack basemap, rendered by MapLibre, with no tile server. Decide how it is delivered by measuring, not by estimate. If it cannot be delivered, the heatmap waits. It does not go online.**

**The reason, in one sentence:** it is the only option that keeps the product's single differentiator true on its most revealing screen, it costs nothing to run, its licence has no clause to interpret, and it costs a few more build hours than platform maps. Platform maps would also carry an unpriced legal review and a controller relationship with Google.

### 7.1 The spike that gates it: 1–2 days [J]

1. Download OS Open Zoomstack vector tiles (~2.6 GB, from the OS Data Hub). **This needs the CEO's go-ahead as a download; nothing is spent.**
2. Strip it to the heatmap's layers, keep street zoom only where the venue index has venues, convert to PMTiles, and **measure the result.**
3. Render central London, Manchester and one market town on a mid-range Android phone and an iPhone. Record frame time with the heatmap layer on and the file size.
4. **Report against the bar:** at or under ~150 MB, bundle it. Between ~150 MB and ~1.5 GB, deliver it once through the store (§5.3), subject to the CEO's decision on the claim wording. Above that, or if frame time fails, **the heatmap waits** for a later release. The ranked list (D13) ships regardless.

### 7.2 What it costs

At the CFO's benchmark of **£32.71 per hour** (`cost-sheet-v3.md`, labour benchmark):

| Route | Build hours [J] | Build labour | Running cost | Maintenance [J] |
| --- | --- | --- | --- | --- |
| **Recommended: offline Zoomstack, bundled** | 40–70 | £1,308–£2,290 | **£0** | 6–10 h/yr (two refreshes plus the MapLibre SDK upgrade in the annual pass) = £196–£327/yr |
| Offline Zoomstack, store-delivered pack | 55–95 | £1,799–£3,107 | **£0** | 8–12 h/yr = £262–£393/yr |
| Platform maps (MapKit + Google) | 25–50, including a hand-built iOS heatmap, since `react-native-maps`' heatmap is Google-only | £818–£1,636 | **£0** in fees | Plus **a Constitution 6.1 legal review (unpriced)**, the controller work at §3.3 (CGO hours, unpriced), and re-drafting PRIV-1/PRIV-8/DATA-6 |
| No basemap (venue-dot texture) | 10–20 | £327–£654 | £0 | ~2 h/yr |

Hours breakdown for the recommended route [J]: tile pipeline 12–20; MapLibre integration, both palettes, heatmap layer and local glyphs/sprites 20–35; delivery and first-run copy 2–4 if bundled; licence-screen entries 1–2; network-capture and snapshot tests 4–6; plus the §7.1 spike. **Constitution 1.5's justification for the extra ~£500–£1,500 of labour over platform maps:** that money buys the only claim customers are paying for. The platform route's savings are not real savings, because its legal review and controller work are costs no seat has priced. [J]

**None of these hours are in any seat's sizing.** The CFO recorded LOOK-2 among the 16 unsized requirements (`cost-sheet-v3.md` §4.6). This row sizes it, **on my judgment and not a measurement**, for the CFO to carry.

---

## 8. For the CEO: the one decision this needs

**Decision (Constitution 5.4, user-data policy):** does the heatmap stay off the network?

- **If yes (recommended):** approve the §7.1 spike and its one download. Nothing else needs deciding until it reports.
- **If the CEO prefers platform maps:** that is his to decide. This note records it as going against the CTO's recommendation, and three things then follow, in order. (1) PRIV-1, PRIV-8 and DATA-6 are rewritten through a scope change, because as written they fail the build (§9). (2) The CGO's 6.1 trigger is pulled and a legal review is priced before launch. (3) The CGO determines Candour's controller position under Google's §4.4(b) before Android ships. **I would then recommend OpenFreeMap over Apple and Google** on everything retrieved here, and I would say so again in writing at that point.

---

## 9. What this does to the requirements (for the PM/BA)

| Requirement | Effect of the recommended route | Effect of online tiles |
| --- | --- | --- |
| **PRIV-1** (BLOCKING): the claim sentence, as re-proposed in `requirements.md` §12.2.8 | **Unchanged if bundled.** If store-delivered, add one sentence (the CGO to check it, the CEO to approve it), for example *"The first time you open the map, your phone downloads a map of Great Britain from the App Store / Google Play."* | **False.** §12.2.8 already says so: *"If the CTO picks an online tile source for the heatmap's map, the reworded sentence becomes false again."* |
| **PRIV-8** (BLOCKING): CI fails on *"any outbound HTTP call site outside the backup module"* | **Passes.** Add a static check that the MapLibre style references no `http(s)://` glyph, sprite or source URL | **Fails** as written |
| **DATA-6(a)** (BLOCKING): *"assert zero outbound connections in a network capture across the full core loop"* | **Passes.** Extend the capture to cover opening, panning and zooming the heatmap | **Fails** as written |
| **LOOK-2**: the heatmap | Add (g): the network capture above; (h) a partiality statement on the face of the map where the basemap is missing (Northern Ireland, pack not yet downloaded) | Would need a disclosure criterion |
| **A11Y-3** (BLOCKING): contrast against tiles | Becomes a measurement against Candour's two palettes | Remains a measurement against vendor styling that changes without notice |
| **LIC-1…5 / Condition 7**: the licence screen | Add the **OGL v3.0** text and the OS attribution string, **once confirmed at primary (§5.1)** | Vendor attribution rules (Apple Attachment 6 §2.1; Google; Mapbox) |
| **New, proposed as a rule:** *No map framework that fetches remote tiles is linked* | The CGO's recommended condition — *"links no places, geocoding or map framework"* (`compliance-note.md` §1.3) — is kept, narrowed to allow an offline renderer. **The CGO should confirm the narrowing.** | Rule withdrawn |

---

## 10. What would overturn this, and where I looked

**The finding that online tiling fails for this heatmap would be overturned by any of:**

1. **A provider that verifiably receives nothing from which the viewing area can be recovered.** For example, a private-retrieval tile scheme, or one that serves only fixed whole-city bundles at a zoom that is still readable. I found none among the five I examined. I did not survey the whole market.
2. **Traffic capture showing the tile request carries no identifier and cannot be linked to a person,** combined with a published, contractual commitment from the provider to discard the tile coordinates. Apple's statement for its own app comes closest. It has not been extended to MapKit in writing, as far as I found.
3. **A CEO decision (5.4) that the claim may cover a disclosed viewport request.** That is a policy decision and not a factual one, and it would overturn §3.4's conclusion without making any of it false.

**The finding that a no-basemap heatmap is worth little would be overturned by** users preferring it in a usability test. Nobody has watched anyone use any of this (`requirements.md` §22 item 1).

**The recommended route fails if** the §7.1 spike returns a trimmed size or frame time outside the bar, or if OS changes Zoomstack's licence or ends the product. The fallback is then that the heatmap waits. It is not online tiles.

**Where I looked:** Apple's Maps privacy page and the full Developer Program Licence Agreement (Attachment 6 read in full, plus section F on location and maps); Google Maps Platform Terms §§3.2.3, 4.4, the controller terms, the pricing page, and the Android SDK data disclosure (the iOS SDK disclosure page lists no data types, only a pointer to privacy manifests I did not open); Mapbox pricing, telemetry and mobile help pages (the dedicated telemetry help page returned 403); the OSMF tile policy, privacy policy and Produced Work guideline; OpenFreeMap's home page and privacy policy; Protomaps downloads; the OS Zoomstack product, documentation and technical specification; the OGL v3.0 text; the OSNI product list; Geofabrik; Apple's and Google's store size limits; the MapLibre style spec, the Android PMTiles guide and both MapLibre repositories; `react-native-maps` and Expo Maps. **Not reached:** Apple's minimum OS for Background Assets; Zoomstack's vector-tile maximum zoom (not stated on the pages I retrieved); OS's own copyright-acknowledgement page (404); a Curia or GDPRhub primary for *Fashion ID*.

---

## 11. Evidence register

**Read from disk this session:** `constitution.md` v1.3; `roles/cto.md`; `pipeline/evidence-standard.md` v1.1; `decisions/2026-09-16-haunt-gate.md` in full, including D12 and D13; `proposals/haunt/proposal.md` (the claim and its three corrections); `products/haunt/requirements.md` (PRIV-1, PRIV-8, DATA-6, LOOK-2 to LOOK-7, A11Y-1/3/9, VPAGE-9, PHOTO-11, §12.2.8, §20); `products/haunt/cost-sheet-v3.md` (§4.6, F2, labour benchmark); `products/haunt/feasibility-note.md`; `products/haunt/android-and-stack-note.md` §§1–2; `products/haunt/block-4-ruling.md`; `products/haunt/compliance-note.md` §§1.3, 2.5; `products/haunt/ux-note.md` §5.

**Retrieved 2026-09-22, all linked in the text:** Apple Maps & Privacy; Apple DPLA (Attachment 6 and section F); Apple DTS forum thread 127493 (single source); Apple build-size and asset-pack limits; Google Maps Platform Terms; Google Controller-Controller Terms; Google Maps Platform pricing; Maps SDK for Android data disclosure; Mapbox pricing, telemetry and mobile-apps pages; OSMF Tile Usage Policy, Privacy Policy and Produced Work guideline; OpenFreeMap home and privacy (single source); Protomaps downloads; OS Zoomstack documentation and technical specification; OS OpenData page; OGL v3.0; nidirect OSNI list; Geofabrik UK; Rothkranz blog (single source); dev.to Zoomstack conversion (single source); Play size limits and Play Asset Delivery; MapLibre style spec, Android PMTiles guide, GitHub licence and release data; MapTiler on the MapLibre fork (single source); `react-native-maps` README and heatmap doc; Expo Maps; Data Protection Report on *Fashion ID* (secondary).

**Re-derivation owed under gate Condition 6:** the tile-width table in §2.2; the labour conversions in §7.2 (hours × £32.71). **Clauses quoted in the same passage as the claim they support:** Constitution 1.3, 1.5, 5.4, 6.1; gate Condition 7 and 8.6's principle; D12; D13; Google §§3.2.3(d), 4.4(a)–(c); Apple Attachment 6 §§2.5, 2.6, 4; OGL v3.0; ODbL's Derivative Database clause.

---

## 12. Disposition

| Question | Answer | Whose it is now |
| --- | --- | --- |
| **1. Online tiles** | **Fails for this heatmap under every provider**, because the viewing area comes from the journal and a readable request is ~1.5 km square. All options cost ~£0. Google adds controller terms and the anti-re-creation clause; Mapbox has default-on telemetry; OSMF is best-effort; **OpenFreeMap is the least bad** | **CEO** (5.4) if overruled; **CGO** on controller status |
| **2. Offline tiles** | **Recommended: OS Open Zoomstack, OGL, no share-alike, GB only, six-monthly.** Full 2.6 GB [E]; trimmed ~100–400 MB [J, unmeasured]. ODbL sources would pull the 6.1 trigger on an unsettled reading | **CTO** runs the spike; **CEO** approves the download |
| **3. No map** | Worth little as the product; fine as the Northern Ireland and not-yet-downloaded fallback | **PM/BA** for LOOK-2(h) |
| **4. Platform maps / Apple** | **A better third party, not a different kind of party.** Fails D12's own-storage test. Its assurances are published for the Maps app, not for MapKit. D1 turns "platform maps" into Google on Android | **CEO** |
| **Heatmap wait?** | **Only if the spike fails its bar.** The ranked list ships regardless | **CEO**, on the spike's report |

---

## 13. Change log

| Date | Change |
| --- | --- |
| 2026-09-22 | Created. Answers the CFO's F2 and the D12 referral. **Recommends an offline OS Open Zoomstack basemap rendered by MapLibre, gated by a size spike, with the heatmap waiting rather than going online if the spike fails.** Records the CTO's disagreement, once, with the CEO's relayed position that a tile request sends no user data. Proposes a two-limb rule for when a network request fits the claim. Sizes LOOK-2 at 40–70 hours [J] for the CFO. Flags the Google controller-controller terms and the *Fashion ID* reasoning to the CGO. External sources retrieved 2026-09-22. **Not a certification.** |

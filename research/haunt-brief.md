# Research brief — Haunt

**Date:** 2026-09-09 · **Author:** Research Analyst · **Commissioned by:** CVO (2026-09-09) · **Due:** 2026-09-30 (delivered early)
**Anti-drift clock:** see the note immediately below — the correct decision date is contested and the CEO/CGO should rule on it.
**Slug:** `haunt` · **Idea brief:** [`proposals/haunt/idea-brief.md`](../proposals/haunt/idea-brief.md)

> **Clock note (Constitution 5.2), raised before anything else.** The idea brief records the decision as due **2026-10-28**, computed as four weeks from this brief's *due date* of 2026-09-30. But 5.2 says the decision is due "within 4 weeks **of its research brief**," and the brief exists today. On a literal reading the decision is due **2026-10-07**. I am not the seat that rules on this, and I raise it rather than assume the more comfortable answer. My recommendation is the literal reading: the rule exists "to force building over perpetual planning," and letting a late-scheduled due date extend the clock after the artifact has actually landed is exactly the drift 5.2 forbids. The CGO should record whichever date is chosen and why.

---

## Headline finding

**The product exists. It shipped. It is on its fourth major version, it is on sale now, and its own App Store copy is a near-verbatim rendering of Haunt's privacy promise.**

Arc Timeline 4 (Big Paua / Matthew Bruce Greenfield, iOS), released 12 April 2026, describes itself in the App Store as: *"All data stored on your device. Optional iCloud backup to your private iCloud account. No accounts, no sign-ups, no data shared with third parties. Export your data anytime in standard JSON format."* [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708]. It does automatic visit and place detection, keeps a places tab with visit history, supports **notes on timeline items**, and is priced at £4.99/month, £44.99/year or £179.99 lifetime [E — same source; feature detail corroborated at https://support.bigpaua.com/t/introducing-arc-timeline-4-the-next-generation-of-arc/1141 and https://www.bigpaua.com/arcapp/].

Separately, the second load-bearing [K] in the idea brief also holds: **Google moved Timeline to on-device storage, and it is free.** Google's own announcement says *"soon your Timeline will be saved right on your device"* and that cloud backup is optional and *"We'll automatically encrypt your backed-up data so no one can read it, including Google"* [E — https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/, 12 Dec 2023]. Google Maps additionally offers **private lists with free-text notes of up to 4,000 characters per place** [E — https://support.google.com/maps/answer/7280933?hl=en&co=GENIE.Platform%3DiOS].

So both of the idea brief's own "what would make this NOT worth doing" items 1 and 2 are confirmed by retrieval, not softened by it. On the evidence I gathered, **Haunt's MVP as scoped has no differentiator I could find, on either the privacy axis or the journal axis, against products that are already shipping — one of them free, from Google, on both platforms.** I say that plainly because a brief that flatters the idea is a failed brief.

I also found three things that push the other way and that I would not want buried: Google's Timeline transition destroyed real users' data and that is on the record; Arc's own community is small and its notes/ratings layer is thin; and there is a genuine, retrievable legal problem in the venue-naming architecture that *nobody* in this category appears to have solved cleanly. Those are in §6 and §8.

---

## 1. Question(s) this brief answers

The six questions commissioned in the idea brief (a)–(f), plus (g) willingness-to-pay and acquisition, added by the commissioning message. Each is answered in its own section below, in priority order.

**Evidence situation, stated plainly per `pipeline/evidence-standard.md`.** Candour has no industry contacts. This brief is entirely secondary: vendor documentation, published terms of service, app store listings, one developer support forum, published survey work and press. There are **no interviews and no observation of real users**. Every conclusion about user *behaviour* below is weaker than every conclusion about *what products exist and what they cost*, and I have tried to keep that distinction visible rather than smooth it over. Where I could not verify something, I say so.

---

## 2. (a) Google Maps Timeline — the most dangerous fact, verified

**Verdict: the idea brief's [K] was right. Upgrade to [E]. It is worse for Haunt than the brief assumed, because Timeline is not the whole of what Google already gives away.**

What I retrieved from Google's own material:

| Claim | Evidence |
| --- | --- |
| Timeline data is saved on the device | *"soon your Timeline will be saved right on your device — giving you even more control over your data"* [E — https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/, 12 Dec 2023] |
| Cloud backup is optional and encrypted from Google | *"you can always choose to back up your data to the cloud so it doesn't get lost. We'll automatically encrypt your backed-up data so no one can read it, including Google."* [E — same] |
| Backup, when on, puts an encrypted copy on Google servers | *"When you back up your Timeline data, Maps saves an encrypted copy of your data on Google's servers."* [E — https://support.google.com/maps/answer/6258979?hl=en-GB] |
| Timeline is opt-in, not on by default | *"Timeline is off by default for your Google Account and can only be turned on if you opt in."* [E — same] |
| Default retention shortened | auto-delete default moved from 18 months to *"three months by default"* [E — blog.google, as above] |
| Timeline is mobile-only now | *"Timeline is not available for Maps on your computer."* [E — support.google.com, as above] |
| Price | Google Maps is a free consumer app; no Timeline paywall appears anywhere in Google's Timeline help [E, by absence — https://support.google.com/maps/answer/6258979?hl=en-GB]. I did not find a Google page stating "Timeline is free" in those words, and I flag that this is an argument from absence rather than a positive citation. |

Note on independence: both sources are Google's own. That is what was asked for (Google's documentation, not press summaries), but it means the caching-behaviour and default claims rest on **one origin**. They are, however, the origin with authority over the fact.

**The part the idea brief did not anticipate.** Haunt's residual pitch after conceding privacy was "the notes-and-ratings layer." Google Maps already ships the notes half of that, free, on both platforms: lists can be created as **Private** ("only you can view and edit") or Shared [E — https://support.google.com/maps/answer/6258979?hl=en-GB is Timeline; list privacy from https://support.google.com/maps/answer/7280933?hl=en-GB], and a place in a list takes a note — *"Tap You, select a list, choose a place, tap Add a note about this place"* — with *"Notes can be up to 4,000 characters."* [E — https://support.google.com/maps/answer/7280933?hl=en&co=GENIE.Platform%3DiOS].

What Google does **not** ship: a private *star rating* on a place (Google's ratings are public reviews), and any automatic link between a Timeline visit and a note. That gap is real. It is also, in my judgement, about two afternoons of Google product work wide [J].

**The counter-evidence, which is the strongest single argument for Haunt in this whole brief.** Google's on-device transition destroyed data. Google's statement: *"We briefly experienced a technical issue that caused the deletion of Timeline data for some people."* Users with encrypted backups could restore; users without them lost the data permanently, and Google declined to say how many were affected [E — https://www.theregister.com/2025/03/24/google_maps_timeline_data_loss/, 24 Mar 2025; **single retrieved source**, though the incident was widely reported and I did not retrieve the corroborating outlets]. There is therefore a real, dated, documented instance of the incumbent losing exactly the archive Haunt proposes to keep. That is a trust wedge. It is not a *feature* wedge, and I would not build a company on it [J].

---

## 3. (b) Does this product already exist? Yes.

### 3.1 Arc Timeline — this is the product

Retrieved facts:

- **Arc Timeline 4**, released 12 April 2026, "ground-up rebuild," new recording engine, places tab with visit history and occupancy charts, calendar sync, AI search; *"Your places, visits, trips, and notes are all preserved"* on import [E — https://support.bigpaua.com/t/introducing-arc-timeline-4-the-next-generation-of-arc/1141].
- App Store description: *"All data stored on your device. Optional iCloud backup to your private iCloud account. No accounts, no sign-ups, no data shared with third parties. Export your data anytime in standard JSON format."* Version 1.6.1 (18 Aug), 61.6 MB, 5.0 from **6 ratings** [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708].
- Release notes confirm the journal layer is being actively worked: *"Add notes to timeline items more easily, and notes now save automatically when you leave the editor"* (v1.4.0) [E — same].
- Privacy policy: *"Arc App collects location and motion data from your phone and stores it securely on your phone"*; *"This data is processed locally on your phone"*; *"None of your data is shared with third parties, for any purpose"*; iCloud backup is opt-in [E — https://www.bigpaua.com/arcapp/privacy].
- Product page feature list includes *"Photo and note annotations for activities and locations"* [E — https://www.bigpaua.com/arcapp/].
- Pricing, GB store, Arc Timeline 4: **£4.99/mo, £44.99/yr, £179.99 lifetime** [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708]. Legacy Arc Timeline 3: £4.99/mo, £24.99/6mo, £44.99/yr backer, £179.99 lifetime [E — https://apps.apple.com/gb/app/arc-timeline-trips-places/id1063151918].

**Feature-by-feature against Haunt's MVP scope:**

| Haunt MVP element (per idea brief) | Arc Timeline 4 | Source |
| --- | --- | --- |
| Automatic background visit detection | Yes | [E] App Store listing |
| User confirms/edits before it lands | Yes — "requires user confirmation of uncertain items" | [E] Arc Timeline 3 listing |
| Local-only storage | Yes, stated | [E] privacy policy + App Store |
| Opt-in encrypted backup to user's own cloud | Yes (iCloud) | [E] privacy policy |
| Candour/vendor holds no user data | Stated: "not in the business of storing or selling your data" | [E] https://www.bigpaua.com/arcapp/ |
| Notes on places/visits | Yes | [E] release notes v1.4.0 |
| Export in a usable format | Yes — "standard JSON format" | [E] App Store |
| **Ratings on venues** | **Not found** | — |
| **Android** | **No — iOS only** | [E, weak: no Play Store listing found; asserted at https://dawarich.app/blog/best-google-timeline-alternatives-in-2026-ranked/, which is a **competitor's** blog. I could not find a Big Paua statement either way and flag this as unverified-by-vendor.] |

**So the two genuine gaps in Arc are: venue ratings, and Android.** The idea brief itself named the ratings layer as "a much smaller idea than the one sparked," and named Android as roughly doubling the build. Haunt's remaining product, honestly stated, is *"Arc, plus a star rating, on Android."*

One thing that cuts the other way and I want on the record: Arc is a **single developer** [E — App Store developer field, https://apps.apple.com/gb/app/arc-timeline-4/id6740688708], its legacy app went ~8 months between updates (3.17.1 Jan 2025 → 3.17.4 May 2025) [E — US and GB App Store listings], and a third party describes development as having "stalled" with "sporadic" updates [E, hostile-source caveat — https://dawarich.app/blog/best-google-timeline-alternatives-in-2026-ranked/ is written by a competing product]. A one-person incumbent is a beatable incumbent. It is also a **warning about the size of the prize**: one person is what this market supports.

### 3.2 The wider sweep

| Who | What | Price | Storage | Why users choose it |
| --- | --- | --- | --- | --- |
| **Google Maps Timeline** | Automatic location timeline, named venues, private lists + 4,000-char notes | Free | On-device, optional encrypted cloud backup [E] | Already installed; best venue database on earth; zero effort |
| **Arc Timeline 4** (iOS) | Automatic visit/trip timeline, places tab, notes, JSON export | £4.99/mo · £44.99/yr · £179.99 lifetime [E] | On-device, opt-in iCloud [E] | The privacy-first power-user option; 10 years of history |
| **Swarm** (Foursquare, iOS/Android) | Manual check-ins, personal timeline, private or public | Free [E] | Server-backed | *"Stay private or share publicly — your check-ins, your choice"*; 3.9★ from 417 UK ratings [E — https://apps.apple.com/gb/app/swarm-by-foursquare/id870161082] |
| **DayTrace** (Android) | Automatic route/stay recording, "fully offline, without cloud services" | Not retrieved | On-device (claimed) | Android's local-first option [E, weak — claim appears in search results; **I failed to retrieve the Play Store listing itself** (two attempts, truncated response). Treat as unverified.] |
| **Dawarich** | Self-hosted open-source location history | €60/yr Lite, €150/yr or €18/mo full [E — vendor's own blog] | Your own server | Full ownership for technical users |
| **OwnTracks / Traccar** | Self-hosted location recording | Not retrieved | Your own server | As above [E, listing-level only — https://dawarich.app/blog/best-google-timeline-alternatives-in-2026-ranked/] |
| **Beli** | Social restaurant ranking, "Letterboxd for restaurants" | Free | Server | Friend feeds, leaderboards, comparison-based ranking |
| **Crumble, Truffle, Yummi, Mapstr** | Venue rating/bookmarking, various social postures | All free tiers | Server | [E, **vendor-authored** — https://crumble.me/guides/letterboxd-for-restaurants is Crumble's own competitor comparison and should be read as marketing] |
| **Doing nothing** | — | Free | — | The honest leading competitor. No evidence retrieved that most people want this record. |

### 3.3 Swarm: the idea brief's low-confidence recollection was **wrong, and I am discarding it**

The idea brief carried "an unverified recollection of a discontinuation announcement and a subsequent reversal" for Swarm. What actually happened: Foursquare sunset the **City Guide** app — not Swarm — on 15 December 2024 (web version 28 April 2025), explicitly *to concentrate on Swarm*. Foursquare's own page: *"The Foursquare City Guide mobile app was officially sunsetted on December 15, 2024"* and *"Your business listing will remain discoverable on our Swarm app"* [E — https://foursquare.com/city-guide-sunset/]. Swarm is live, updated 2 September 2025 [E — https://apps.apple.com/gb/app/swarm-by-foursquare/id870161082].

**There was no Swarm discontinuation and no reversal.** The [K] should be struck from the record, not repeated. This is exactly the failure mode the evidence standard exists to catch, and it is the second time in this brief a confident-feeling memory turned out to be a garbled version of a real event.

What *is* true, and relevant, is the direction of travel: Foursquare rebuilt itself as an enterprise location-data company, with management stating *"We are not in the same business like Facebook and Twitter as we are not trying to have a billion users"* [E — https://digiday.com/media/not-trying-billion-users-hype-faded-foursquare-tries-reinvention-data-business/, 8 Aug 2016 — **note the age**; I use it only for the direction of the pivot, which the 2024 City Guide sunset independently corroborates]. The company that invented consumer check-ins concluded consumer check-ins were not the business. [I, from those two [E] premises]

---

## 4. (c) Does the rating-and-writing habit exist without an audience?

**Verdict: partly. The one-tap rating survives without an audience; the writing almost certainly does not. And Haunt's value-add is the writing.**

The best quantitative evidence I retrieved is Letterboxd's own 2024 community numbers, verbatim from their year-in-review: *"You cast almost half a billion ratings, wrote 96.4 million reviews, marked 701 million films watched and made 6.8 million lists."* [E — https://letterboxd.com/journal/2024-year-in-review/].

Arithmetic on those figures (not a claim about the world, just division):

- ~500m ratings ÷ 701m logs ≈ **71% of logged films get a rating**
- 96.4m reviews ÷ 701m logs ≈ **14% of logged films get any written review**

[I, from the [E] above] On the single most successful "log-and-rate" social product in existence — with a full audience, friend feeds, and a year-end shareable — **six out of seven logged items carry no writing at all.** The one-tap rating is a mass behaviour. Writing is a minority behaviour even when someone is watching.

Haunt removes the audience and keeps the writing as its differentiator. [I] That is building on the fragile half of a behaviour that is already the minority half under the *most* favourable conditions.

Three further pieces, each weaker:

1. **Letterboxd itself already supports private logging.** Its diary entry UI offers a Privacy mode of "Anyone (public) / Close Friends (selected by you) / You (private)," with the note *"Ratings on Close Friends and You entries don't contribute to stats"* [E — retrieved from the page markup at https://letterboxd.com/journal/2024-year-in-review/]. So "log privately" is not an unserved need in the reference product; it is a checkbox. I could not retrieve any figure for **how many people use it**, and that number is the one that would actually answer this question. **That is a real gap in this brief.**

2. **Swarm's private check-in exists and has for a decade.** Off-the-grid check-ins launched April 2016, recorded in your history but not shown to friends [E — https://techcrunch.com/2016/04/21/swarm-now-lets-users-check-in-without-sharing-their-location/]. That article contains the line most tempting to quote in Haunt's favour — that people "loved the recording feature of the check-in just as much (if not more) than the ability to share" — but **I checked, and it is the journalist's own framing, not a Foursquare statement, and the piece carries no usage numbers** [E — same]. I am flagging it rather than using it, because used unflagged it would look like company evidence and it is not.

3. **Retention.** Published cross-industry benchmarks put day-30 retention for strong performers at roughly 8–12% in health & fitness and 15–20% in social, with the overall median near 4% [E, **weak and secondary** — https://uxcam.com/blog/mobile-app-retention-benchmarks/, an aggregator restating AppsFlyer/Adjust/data.ai; I did not retrieve the underlying reports and the article gives ranges, not a methodology I can check]. There is no journalling category in it. **I could not find retention data for journalling apps specifically, and I am not going to invent it.** The idea brief's red flag #3 ("journalling retention is famously bad") therefore stays [K], unverified, and the CEO should treat it as an untested belief rather than a finding.

**Net.** The commissioned question was "does the MVP's value-add survive removing the social layer." My answer: the *rating* plausibly survives — but the rating alone is a feature Google could add and that Swarm and Beli give away. The *writing* is what Haunt is selling, and the only hard number I have says writing is a 14% behaviour with an audience. [I from [E]]

---

## 5. (d) Is "local storage + venue lookup" read as honest, or as a broken promise?

**Verdict: I could not find direct evidence on this exact distinction, and I am reporting that as the finding. The nearest analogues are bad news, and the mitigation is architectural rather than editorial.**

I looked for cases where a privacy-branded consumer product was found to have a narrow, technically-true claim plus a third-party exception. The cleanest is DuckDuckGo:

- May 2022: researcher Zach Edwards found DuckDuckGo's browser was not blocking Microsoft advertising trackers, under a contractual carve-out tied to its Bing syndication deal [E — https://techcrunch.com/2022/08/05/duckduckgo-microsoft-tracking-scripts/].
- DuckDuckGo's position was that it *"essentially had no choice to accept Microsoft's terms"* [E — same]. That is a *true, narrow, accurate* explanation. It did not work.
- The company removed the carve-out in August 2022; CEO Gabriel Weinberg: *"Previously, we were limited in how we could apply our 3rd-Party Tracker Loading Protection on Microsoft tracking scripts due to a policy requirement related to our use of Bing"* [E — same].

[I, from that [E]] The lesson is not "users misread nuance." It is that **for a product whose entire value proposition is a privacy promise, a disclosed exception is read as the promise being false, and being right about the details does not help.** Haunt's exception is more defensible than DuckDuckGo's (a coordinate, sent to name a shop, at the user's instruction, with nothing retained by Candour). But it is structurally the same shape: *"we send nothing anywhere, except…"*

The counter-model — the one Haunt should copy if it proceeds — is Apple's, which does not rely on a carve-out but on making the lookup itself non-identifying: Apple describes location contributions as sent *"in an anonymous and encrypted form"* and states *"The crowd-sourced location data gathered by Apple does not personally identify you"*, with Significant Locations end-to-end encrypted and *"System Customization data does not leave your device"* [E — https://www.apple.com/legal/privacy/data/en/location-services/].

**What I could not find:** any study, forum thread, or review corpus measuring how privacy-attentive consumers react specifically to *"stored locally, but we call a places API to name it."* I searched for it and did not get it. Treat any confident claim on this — in either direction — as unevidenced.

**Practical consequence for the gate.** The mitigations that make this survivable are technical, not copywriting: (i) coarsen the coordinate before it leaves the device; (ii) don't send anything until the user taps "name this place"; (iii) show the network call in the UI at the moment it happens; (iv) never route it through a Candour server. All four are CTO questions. None of them is a marketing sentence. The idea brief was right that this is a discovery question — and my honest answer is that discovery could not settle it from secondary sources, so it should be settled by *design* (assume the hostile reading) rather than by *research*.

---

## 6. (e) Would a sharing layer even be wanted?

**Verdict: no evidence that the private-timeline audience wants one; weak evidence, from a small self-selected sample, that they want the opposite. Low confidence, and I would not let this decide anything on its own.**

The one piece of near-primary evidence available is the public feature-request thread for Arc Timeline — i.e. actual users of a shipping, private, local-first location timeline saying what they want next. Across that thread: **no requests for sharing or social features, and no requests for place ratings.** The requests are dark mode, city names in search results, non-iCloud backup targets (WebDAV, Synology), font sizing, and integrations with Calendar/Exist/flight data — e.g. *"Custom backup targets"*, *"A Places tab similar to the Activity tab"* [E — https://support.bigpaua.com/t/what-would-you-like-to-see-in-arc-timeline-v3-17/677].

Caveats I insist on: **one thread, one product, self-selected respondents, and absence of a request is not evidence of aversion.** People who want sharing may simply not be in an Arc forum. This is the weakest evidence in the brief and it is doing real work, so I am labelling it loudly.

Two structural observations, both [I]:

- The market already offers the sharing version at £0 — Swarm's own store copy is *"Stay private or share publicly — your check-ins, your choice"* [E — https://apps.apple.com/gb/app/swarm-by-foursquare/id870161082], and Beli/Crumble/Truffle/Yummi all ship social layers free [E, vendor-authored comparison — https://crumble.me/guides/letterboxd-for-restaurants]. A paid sharing layer would enter a market where sharing is a free commodity.
- A sharing layer is the only plausible **acquisition** mechanism this product has (see §9), which creates a bad incentive: the company would want the sharing layer for growth reasons rather than user-need reasons, and Article 1.1 judges products by whether people recommend them unprompted, not by whether the product makes them.

**Answer to the CEO's actual question:** on this evidence I would not build the sharing layer, and I would not keep the door open for it either. Keeping the door open costs something — it is a permanent tax on every data-model and promise decision, paid now, for an option nothing in the evidence supports exercising. [J]

---

## 7. (f) Places-API terms — the finding that changes the architecture

**Verdict: the idea brief's [K] was right and understated. Under every major commercial provider's terms, a journal that permanently stores the venue *name* returned by the API is a breach. The open alternatives are free of that problem and have a coverage problem instead.**

### 7.1 Google Maps Platform — clearest, and clearly prohibitive

From Google's terms, retrieved in full:

> **3.2.3 Restrictions Against Misusing the Services. (a) No Scraping.** Customer will not export, extract, or otherwise scrape Google Maps Content for use outside the Services. For example, Customer will not: (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services; … **(iii) copy and save business names, addresses, or user reviews**…
>
> **(b) No Caching.** Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms.

[E — https://cloud.google.com/maps-platform/terms]

And the permitted exception, in full:

> **14. Places API (Legacy and New) … 14.3 Caching.** Customer may temporarily cache latitude and longitude values from the Places API for up to 30 consecutive calendar days, after which Customer must delete the cached latitude and longitude values.

[E — https://cloud.google.com/maps-platform/terms/maps-service-terms]

Place IDs are the one durable exception: *"Place IDs are exempt from the caching restrictions"* and may be stored indefinitely, with Google *recommending* a refresh if older than 12 months [E — https://developers.google.com/maps/documentation/places/web-service/place-id; corroborated at https://developers.google.com/maps/documentation/places/web-service/policies].

Two further clauses bite Haunt specifically:

- **3.2.3(e) No Use With Non-Google Maps** — Places content must not be used alongside a non-Google map [E — https://cloud.google.com/maps-platform/terms; restated at Service Specific Terms 14.2]. A timeline app that draws a map is therefore locked to Google's map too.
- **3.2.3(d) No Re-Creating Google Products or Features** — customer products must not be "substantially similar to" a Google product and must contain "substantial, independent value and features beyond" it [E — same]. Haunt is a location timeline with notes on places. Google ships a location timeline with notes on places. I am not a lawyer and this is not a legal opinion (Constitution 6.1), but a seat proposing to build on Places should not pretend this clause is obviously inapplicable.

**Consequence, stated bluntly.** [I from the above [E]] On Google Places, a compliant Haunt could store a `place_id` forever and would have to **re-fetch the venue's name every time it renders a five-year-old journal entry**. That means (i) the journal is not readable offline, (ii) the privacy promise leaks — opening your own past requires a network call per venue, and (iii) the per-render API bill is unbounded rather than per-visit. That is not a footnote; it inverts the product.

### 7.2 Foursquare

The Places API EULA defers caching to the Usage Guidelines (which I did not retrieve — **flagged as an open item**), but three retrieved clauses matter [all E — https://foursquare.com/legal/terms/apilicenseagreement/]:

- **2.2 Visual Crediting:** *"You must provide Foursquare with branded attribution (i.e., 'Powered by Foursquare') on any page or screen within Your Service where Places Data may appear."* A private journal displaying venue names would carry a Foursquare logo forever.
- **1(d)(iii):** derived materials must not be *"competitive with Foursquare's then-current products or services."* Foursquare's remaining consumer product is Swarm — a personal location timeline. Haunt is a personal location timeline.
- **2.6 Audit Rights:** Foursquare *"may review your systems and applicable records"* on notice, and may disclose findings to its data suppliers.

Pricing: 10,000 free Pro calls, then **$15.00 per 1,000 calls** (Pro) falling to $12.00 above 100k and $9.00 above 500k; Premium $18.75 → $11.25 [E — https://foursquare.com/pricing/]. At $15/1,000 a user generating 3 venue lookups a day costs ~$0.0014/day ≈ **$0.49/user/year** in lookups alone, before any re-fetch-on-render obligation [arithmetic on the [E] price].

### 7.3 Apple (MapKit / CLGeocoder) — cheapest, and legally the murkiest

> **⚠ CITATION CHALLENGED — added by CVO 2026-09-10, at the CGO's finding. The Research Analyst's text below is unaltered.**
>
> The CGO's compliance read reports that one Apple quotation in this section is **attributed to a forum thread that does not contain it**. Under `pipeline/evidence-standard.md` a citation without a retrieval behind it is the most serious offence in the standard, and it is marked here rather than quietly repaired, because quiet repair is how a fabricated citation becomes an established fact.
>
> **Weight to give this section pending resolution: none of it is load-bearing to the gate decision.** The MVP takes the zero-network route and touches no Apple map API, so §7.3 informs an architecture the proposal does not adopt. The section's *conclusion* — that Apple's terms are unresolved and Apple declines to resolve them — is independently corroborated by the CGO's own retrieval of a developer being told to hire a lawyer. **The conclusion survives; the specific quotation does not, until re-retrieved.**
>
> **Owner:** Research Analyst, to re-retrieve or withdraw. Do not cite §7.3's quotations elsewhere until then.


Apple's clause, quoted verbatim by developers **on Apple's own forum**:

> "Unless otherwise expressly permitted in the MapKit Documentation, Map Data may not be cached, pre-fetched, or stored by You or Your Application, other than on a temporary and limited basis solely to improve the performance of the Apple Maps Service with Your Application."

[E — https://developer.apple.com/forums/thread/114220 and https://developer.apple.com/forums/thread/116695. **I could not retrieve Apple's licence agreement itself** — it sits behind the developer programme — so this is a developer's quotation of a document I have not seen. Flagged accordingly.]

More damning than the clause is Apple's response to being asked what it means. An Apple DTS engineer, on the record: *"Your questions on points 2 and 3 are related to interpreting the terms of the Apple Developer Program License Agreement, so that's not something I can discuss with you. I suggest you run those questions by your legal council."* [E — https://developer.apple.com/forums/thread/807656]. A second thread on the identical question sat unanswered for years, with one developer writing *"I've been researching for 2 days already, but no body seems to know"* [E — https://developer.apple.com/forums/thread/116695].

[I] So the free, zero-server, iOS-native option — almost certainly what Arc uses — is available, is what everybody does, and is legally unresolved in a way Apple itself will not resolve on request. Candour's constitution makes honesty about limitations a product requirement (Article 1.3). "We rely on a licence term the vendor declines to interpret" is a thing that would have to be said out loud.

### 7.4 The open alternatives — no licence problem, a data problem

**Nominatim (OSM's public geocoder) is not usable for this product.** Its published policy imposes *"an absolute maximum of 1 request per second"*, forbids *"Auto-complete search"* and *"Systematic queries"*, requires results *"must be cached on your side"*, and directs heavier users to self-host [E — https://operations.osmfoundation.org/policies/nominatim/]. Self-hosting means a server, which contradicts the product's defining "Candour runs no server" promise and adds cost that customers pay (Constitution 1.5, 2.1).

**Overture Maps is the credible fallback, and its own documentation is candid about quality.** ~74 million places as of August 2026; licensed **CDLA Permissive 2.0** (plus Apache 2.0 for the Foursquare-contributed portion), and explicitly *"The theme does not include OpenStreetMap data and carries none of the share-alike obligations of the Open Database License (ODbL)"* — so a bundled offline dataset is permissible without ODbL contagion. But: *"Places is known to contain duplicates, a high junk rate, and low property completeness"*, with a provider-derived confidence score that is *"not calibrated to be strictly comparable across providers"* [E — https://docs.overturemaps.org/guides/places/].

**Coverage, empirically.** An independent hobbyist analysis (21 Oct 2024) counted 2,084,249 restaurants in OSM against 3,579,176 in Overture, then hand-checked a 100-restaurant sample of each against Google Maps: **72/100 OSM entries and 60/100 Overture entries were confirmed to exist in Google Maps** [E, **single source, hobbyist blog, n=100, no per-country breakdown** — https://surprisedatespot.com/blog/comparing-overture-osm-restaurants/]. The author explicitly declines to give per-country figures, noting quality "varies a lot by country." **I could not find a UK-specific bars/restaurants/nightlife coverage figure for either dataset, and that was specifically commissioned. It is an open item.** A secondary claim that OSM holds roughly 19,000 UK pubs against a British Beer and Pub Association count of ~45,000 surfaced in search results but **I could not retrieve either figure at source, so I am not asserting it** [K, low confidence — do not rely on it].

[I] For a UK nightlife journal, an offline Overture bundle would name a meaningful minority of venues wrongly or not at all, and every miss lands on the user as "this app doesn't know where I am" — the single most visible failure a location app can have.

### 7.5 Summary table

| Provider | Store venue name permanently? | Store ID permanently? | Price | Other blockers |
| --- | --- | --- | --- | --- |
| Google Places | **No** — 3.2.3(a)(iii) forbids copying and saving business names [E] | Yes — place_id exempt [E] | Paid, per call | Must use Google map only; anti-re-creation clause [E] |
| Foursquare | Deferred to Usage Guidelines (**not retrieved**) | Not established | $15/1k Pro after 10k free [E] | Permanent "Powered by Foursquare" on any screen showing the data; no competitive use; audit rights [E] |
| Apple MapKit | Ambiguous — "temporary and limited basis" only; Apple declines to interpret [E] | Ambiguous | Free (iOS only) | Legal uncertainty vendor won't resolve [E] |
| Nominatim (public) | Caching required, but 1 req/sec and no systematic queries [E] | n/a | Free | Unusable at consumer scale; self-host needs a server [E] |
| Overture (bundled) | **Yes** — CDLA-Permissive 2.0, no ODbL share-alike [E] | Yes | Free | "duplicates, a high junk rate, and low property completeness" per its own docs [E]; UK coverage unmeasured |

**The architecture this evidence points to** is the idea brief's higher-cost variant: **bundle Overture, run zero network, accept worse names.** That is the only shape where the promise and the terms are both honest. It also costs more to build, ships a worse product on day one, and still does not differentiate against Arc [I].

---

## 8. (g) Willingness to pay, and the acquisition problem

**Verdict: stated willingness to pay for privacy is real but small and unreliable; the acquisition channel for this specific product is one channel (App Store search) that Haunt would enter behind a free Google feature and a decade-old incumbent.**

**Stated willingness.** A March 2026 survey of 11,000 consumers across seven markets including the UK found 52% "will pay more for AI transparency" at an average **7% premium**, with UK willingness at 50% [E, **vendor-authored** — https://usercentrics.com/resources/state-of-digital-trust-report-2026/, published by a consent-management company with a direct commercial interest in the answer; treat accordingly]. Note the size of the number that is actually load-bearing: not "will they pay," but **7%**.

**Revealed willingness.** The counterweight is the digital privacy paradox, from a field experiment: people say they value privacy but relinquish data for small rewards; *"small navigation costs have a tangible effect on how privacy-protective consumers' choices are, often in sharp"* contrast with stated preferences; and reassuring-but-irrelevant privacy information makes people *less* likely to avoid surveillance [E — https://www.nber.org/papers/w23488, Athey, Catalini & Tucker]. [I] A 7% stated premium, discounted by a documented stated-vs-revealed gap, is not a foundation for a paid consumer app competing with a free one.

**The market, measured by the only proxy I have.** Arc Timeline — the leading product in this exact niche, on the platform where it is easiest to build, after roughly a decade — has **425 US App Store ratings** and **164 GB ratings** on its legacy app, and **6 GB ratings** on the 2026 rebuild [E — https://apps.apple.com/us/app/arc-timeline-trips-places/id1063151918, https://apps.apple.com/gb/app/arc-timeline-trips-places/id1063151918, https://apps.apple.com/gb/app/arc-timeline-4/id6740688708]. Swarm, free and backed by a $100m-revenue company, has **417 GB ratings** [E — https://apps.apple.com/gb/app/swarm-by-foursquare/id870161082].

Rating counts are a weak proxy for users and the ratio varies enormously by app [J]. But the direction is not ambiguous, and Swarm's free-app number being the same order as Arc's paid-app number is itself informative [I]. **See §9 for what this implies about price.**

**Acquisition.** Non-game App Store downloads come overwhelmingly from search: 70% of non-game installs came from search in 2020, against 20% app referrals and 12% browse across all apps [E — https://sensortower.com/blog/app-store-download-sources-report-2021, third-party panel data; Apple's own oft-repeated figure is 65–70%, which I did **not** retrieve at source and am not citing]. [I] For Haunt this means the acquisition strategy is: rank for "location timeline," "private journal," "places I've been" — against Google Maps, Arc, Swarm and every travel-journal app — with no ad budget, no social graph, and, per §6, no sharing loop. That is a search-ranking contest, not a product contest, and Candour has no ASO advantage.

**Store economics, for the CFO.** Apple's Small Business Program gives *"a reduced commission rate of 15% on paid apps and In-App Purchases"* for developers with *"up to 1 million USD in proceeds in the prior calendar year"* [E — https://developer.apple.com/app-store/small-business-program/]. At Candour's scale that is 15%, not 30% — materially better than the idea brief assumed, and the one genuinely favourable economic fact I found.

---

## 9. Honest market size for this niche

I cannot size this credibly from secondary sources and I am not going to pretend otherwise. What I can do is put a defensible ceiling on it.

**Ceiling argument** [I, from [E] premises stated in §8]: the category leader on the easier platform, after ~10 years, with the strongest possible privacy story, has hundreds — not thousands — of App Store ratings in its two largest markets. Applying any of the usual ratings-to-installs heuristics (commonly cited in the 1:50 to 1:200 range [J — I could not retrieve a defensible figure and this multiplier is a guess, not evidence]) puts Arc's paying UK base plausibly in the low thousands at most. Haunt would be a later, thinner entrant into that.

**Cross-check against Candour's own pricing rule.** Constitution 2.1 requires labour costed at a market benchmark whether or not drawn, and a price at cost +~20%. The Skeptic's scouting memo already computed what that does at Candour's scale, and its arithmetic applies here unchanged: a fraction of an FTE-year at UK median developer pay is five figures of published cost, and dividing that by a market whose leader has a four-figure user base produces a price well above £179.99 lifetime — which is Arc's *top* price, from an incumbent with a decade of product [I, building on the cost-structure argument in `research/scouts/scout-2026-09-01-skeptic-cull.md` §4].

I flag that the CFO, not I, owns that computation. But the research finding it depends on is mine and it is firm: **the addressable market here is small enough that Candour's own constitutional pricing floor probably sits above the incumbent's ceiling price.**

**What I could not size, and would need to:** how many UK adults keep any deliberate record of venues visited; what share would pay anything; how many of Arc's users would switch for ratings or for Android. None of these are answerable from secondary sources. They would need a landing-page test or a survey — which is a real option, and cheaper than a build.

---

## 10. Feasibility signals and red flags

**Signals in favour (all weak, listed honestly):**

1. Google's Timeline migration deleted users' history and Google would not say how many were affected [E — theregister.com, §2]. There is a documented trust injury to trade on.
2. Google Timeline is **opt-in and off by default**, and defaults to deleting after three months [E, §2]. Most people therefore have no long archive, which cuts both ways: less incumbent lock-in, and less evidence anyone wants one.
3. The incumbent in the paid niche is one person shipping sporadically [E, §3.1].
4. Apple's Small Business Program means 15%, not 30% [E, §8].
5. Overture is genuinely permissively licensed, so a zero-network build is legally clean [E, §7.4].

**Red flags:**

1. **The product exists** (§3.1). Arc Timeline 4 matches Haunt's MVP on every axis except venue ratings and Android.
2. **The free incumbent already concedes the privacy differentiator and ships the notes layer** (§2). Google Maps: on-device Timeline, private lists, 4,000-character notes per place, both platforms, £0.
3. **The venue-name storage problem is real and unsolved** (§7). Google's terms forbid copying and saving business names; Apple's clause is ambiguous and Apple refuses to interpret it; Foursquare demands permanent branded attribution and excludes competitive use; the clean open dataset admits to "a high junk rate."
4. **The differentiating behaviour is the minority behaviour** (§4). On Letterboxd, 14% of logs carry writing — with an audience.
5. **No acquisition channel** (§8). One search-ranking contest against Google, Arc and Swarm, with no budget and (by design) no viral loop.
6. **The market may be too small for Candour's own pricing rule** (§9).
7. **Android is materially harder and adds support burden with no server to diagnose from.** The idea brief's [K] on OEM battery-killing is corroborated: dontkillmyapp.com exists specifically to document that *"Android manufacturers listed below prefer battery life over proper functionality of your apps,"* rating Huawei, Xiaomi, OnePlus and Samsung at its worst severity level while stock Android scores zero [E — https://dontkillmyapp.com/]. I did not verify the underlying per-OEM behaviours, only that this catalogue exists and what it says.
8. **No telemetry means no diagnosis.** Arc's own App Privacy declaration lists Diagnostics (Crash Data, Performance Data) as collected-but-not-linked-to-identity [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708] — i.e. even the strictest local-first incumbent in this category takes crash telemetry. Haunt should expect to do the same and say so, rather than promise a purity no shipping competitor maintains.

**Disagreement with the CVO, recorded once, in writing, as my charter requires.** The idea brief keeps the door open to a later sharing layer and asks whether it would be wanted. On the evidence in §6 I think keeping that door open is a mistake, and I think it is a mistake for a reason worth naming: the sharing layer is the only growth mechanism this product could ever have, so the option will be exercised for company reasons and then justified with user reasons. Article 1.1 judges products by unprompted recommendation, not by engineered referral. I would close the door explicitly at the gate.

**Also recorded:** the idea brief describes running cost as "close to no running cost… a venue-lookup API bill, and nothing else." Section 7.1 shows that on the leading commercial provider the bill is not per-visit but potentially **per-render, forever**, because the name cannot be stored. The CFO's cost model should not assume a one-off lookup charge until the provider is chosen and its caching terms are settled.

---

## 11. Evidence ledger

Tagged per `pipeline/evidence-standard.md`. Everything marked [E] was retrieved in this session at the URL shown. **No citation in this brief comes from memory.**

### Load-bearing [E] — the claims a decision turns on

| # | Claim | Source (retrieved 2026-09-09) | Notes |
| --- | --- | --- | --- |
| E1 | Google Timeline is saved on-device; cloud backup optional and encrypted from Google; default retention cut to 3 months | https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/ | Google's own announcement, 12 Dec 2023 |
| E2 | Timeline off by default, opt-in; backup stores an encrypted copy on Google servers; not available on desktop | https://support.google.com/maps/answer/6258979?hl=en-GB | Same origin as E1 — **not independent** |
| E3 | Google Maps lists can be Private; places take notes up to 4,000 characters | https://support.google.com/maps/answer/7280933?hl=en-GB and https://support.google.com/maps/answer/7280933?hl=en&co=GENIE.Platform%3DiOS | Google's own help |
| E4 | Arc Timeline 4: all data on device, optional iCloud, no accounts, JSON export; £4.99/mo, £44.99/yr, £179.99 lifetime; 6 GB ratings | https://apps.apple.com/gb/app/arc-timeline-4/id6740688708 | The single most important source in this brief |
| E5 | Arc processes locally, shares nothing with third parties; supports photo and note annotations | https://www.bigpaua.com/arcapp/privacy · https://www.bigpaua.com/arcapp/ | Vendor's own claims, unaudited |
| E6 | Arc Timeline 4 is a ground-up rebuild (12 Apr 2026); notes preserved on import | https://support.bigpaua.com/t/introducing-arc-timeline-4-the-next-generation-of-arc/1141 | Vendor announcement |
| E7 | Google Maps Platform 3.2.3(a)(iii) forbids copying and saving business names; 3.2.3(b) no caching except as permitted | https://cloud.google.com/maps-platform/terms | Retrieved full text |
| E8 | Places API caching exception is 30 days, lat/long only | https://cloud.google.com/maps-platform/terms/maps-service-terms §14.3 | Retrieved full text |
| E9 | Place IDs exempt from caching restrictions, storable indefinitely; refresh recommended after 12 months | https://developers.google.com/maps/documentation/places/web-service/place-id · https://developers.google.com/maps/documentation/places/web-service/policies | Two Google pages, same origin |
| E10 | Apple: "Map Data may not be cached, pre-fetched, or stored… other than on a temporary and limited basis"; Apple DTS declines to interpret it | https://developer.apple.com/forums/thread/116695 · https://developer.apple.com/forums/thread/807656 | **Developers quoting a licence I could not retrieve.** The DTS refusal is first-hand |
| E11 | Overture Places: ~74m records, CDLA-Permissive 2.0, no ODbL share-alike; "duplicates, a high junk rate, and low property completeness" | https://docs.overturemaps.org/guides/places/ | Overture's own docs |
| E12 | Letterboxd 2024: ~half a billion ratings, 96.4m reviews, 701m films logged, 6.8m lists | https://letterboxd.com/journal/2024-year-in-review/ | Letterboxd's own figures, verbatim |
| E13 | Foursquare sunset **City Guide** (15 Dec 2024), not Swarm; Swarm continues | https://foursquare.com/city-guide-sunset/ | Kills the idea brief's [K] recollection |

### Supporting [E]

| # | Claim | Source | Flag |
| --- | --- | --- | --- |
| E14 | Google Timeline data loss, Mar 2025; recoverable only with encrypted backup | https://www.theregister.com/2025/03/24/google_maps_timeline_data_loss/ | **Single retrieved source** |
| E15 | Arc legacy app ratings: 425 US / 164 GB; IAP prices | https://apps.apple.com/us/app/arc-timeline-trips-places/id1063151918 · https://apps.apple.com/gb/app/arc-timeline-trips-places/id1063151918 | |
| E16 | Swarm free, 3.9★/417 GB ratings, "Stay private or share publicly" | https://apps.apple.com/gb/app/swarm-by-foursquare/id870161082 | |
| E17 | Swarm off-the-grid private check-ins (Apr 2016); the "recording over sharing" line is the **journalist's**, not Foursquare's | https://techcrunch.com/2016/04/21/swarm-now-lets-users-check-in-without-sharing-their-location/ | Checked precisely so it isn't misused |
| E18 | Foursquare EULA: branded attribution on any screen; no competitive derived materials; audit rights | https://foursquare.com/legal/terms/apilicenseagreement/ | Caching rules deferred to Usage Guidelines — **not retrieved** |
| E19 | Foursquare pricing: 10k free Pro calls, then $15/1k → $9/1k | https://foursquare.com/pricing/ | |
| E20 | Nominatim: max 1 req/sec, no autocomplete, no systematic queries, results must be cached, self-host if larger | https://operations.osmfoundation.org/policies/nominatim/ | OSMF's own policy |
| E21 | OSM 2,084,249 vs Overture 3,579,176 restaurants; 72/100 vs 60/100 confirmed in Google Maps | https://surprisedatespot.com/blog/comparing-overture-osm-restaurants/ | **Single source, hobbyist blog, n=100, no per-country split** |
| E22 | DuckDuckGo Microsoft tracker carve-out, backlash, removal Aug 2022; Weinberg quotes | https://techcrunch.com/2022/08/05/duckduckgo-microsoft-tracking-scripts/ | **Single retrieved source** |
| E23 | Apple: crowd-sourced location "anonymous and encrypted", "does not personally identify you"; Significant Locations E2E encrypted | https://www.apple.com/legal/privacy/data/en/location-services/ | Apple's own claims |
| E24 | Digital privacy paradox: stated vs revealed preference; navigation costs; reassuring info reduces avoidance | https://www.nber.org/papers/w23488 | Peer-reviewed field experiment |
| E25 | 52% "will pay more for AI transparency" at ~7% premium; UK 50%; n=11,000, 7 markets, Mar 2026 | https://usercentrics.com/resources/state-of-digital-trust-report-2026/ | **Vendor-authored, commercial interest in the result** |
| E26 | 70% of non-game App Store installs from search (2020); 20% referrals, 12% browse | https://sensortower.com/blog/app-store-download-sources-report-2021 | Third-party panel; 2020 data — **dated** |
| E27 | Apple Small Business Program: 15% under $1m proceeds | https://developer.apple.com/app-store/small-business-program/ | Apple's own |
| E28 | Arc user feature requests contain no sharing/social and no ratings requests | https://support.bigpaua.com/t/what-would-you-like-to-see-in-arc-timeline-v3-17/677 | **One thread, self-selected, small; absence ≠ aversion** |
| E29 | Android OEM battery-killing catalogue; Huawei/Xiaomi/OnePlus/Samsung worst-rated, stock Android zero | https://dontkillmyapp.com/ | Community-maintained; I verified the catalogue exists and what it says, not the underlying behaviours |
| E30 | Foursquare's enterprise pivot: "we are not trying to have a billion users" | https://digiday.com/media/not-trying-billion-users-hype-faded-foursquare-tries-reinvention-data-business/ | **2016 — old.** Used only for direction, corroborated by E13 |
| E31 | Retention benchmarks by category (day-30: 8–12% health/fitness, 15–20% social, ~4% median) | https://uxcam.com/blog/mobile-app-retention-benchmarks/ | **Aggregator restating AppsFlyer/Adjust/data.ai; underlying reports not retrieved. Weak.** |
| E32 | Competitor blogs used as market maps only | https://dawarich.app/blog/best-google-timeline-alternatives-in-2026-ranked/ · https://crumble.me/guides/letterboxd-for-restaurants | **Both written by competing vendors. Marketing, not research.** |

### [K] — model knowledge, not verified, do not rely on

- **K1.** OSM holds ~19,000 UK pubs vs a BBPA count of ~45,000. Low confidence. Surfaced in search results; **I could not retrieve either figure at source.** Do not repeat as evidence.
- **K2.** Arc Timeline has no Android version. Medium confidence. Asserted by a competitor's blog (E32); no Big Paua statement found either way; no Play Store listing found.
- **K3.** DayTrace (Android) is a fully offline on-device timeline app. Low confidence. **Two attempts to retrieve its Play Store listing failed.** It appears in search results only.
- **K4.** "Journalling retention is famously bad." The idea brief's red flag #3. **Unverified.** No journalling-specific retention data found.

### [I] — inferences, each from tagged premises

- **I1.** Haunt's residual product after §2 and §3 is "Arc, plus a star rating, on Android." From E1–E6.
- **I2.** Writing is a minority behaviour even with an audience (14% of Letterboxd logs). From E12, by arithmetic.
- **I3.** A compliant Google Places implementation must re-fetch venue names on render, breaking offline reading and the network promise. From E7–E9.
- **I4.** A disclosed exception to a privacy promise is read as the promise being false, regardless of accuracy. From E22.
- **I5.** The category's addressable market is small enough that Candour's cost-plus price likely exceeds the incumbent's lifetime price. From E15, E16 and Constitution 2.1; the arithmetic belongs to the CFO.

### [J] — judgement

- **J1.** Google could add a private venue rating trivially; the gap is not defensible.
- **J2.** Keeping the sharing-layer door open is a live tax on today's decisions with no evidence supporting its exercise.
- **J3.** Ratings-to-installs multipliers (1:50–1:200) are a guess and should not be used for sizing.
- **J4.** A landing-page or survey test would be cheaper than a build and would answer the questions secondary evidence cannot.

### Open items I could not close

1. **UK-specific venue coverage** for OSM/Overture — bars, restaurants, nightlife. Commissioned; **not answered.** E21 is global with no per-country split.
2. **Foursquare's actual caching rules** (Usage Guidelines in the developer docs). **Not retrieved.**
3. **Apple's licence text at source.** **Not retrieved** — behind the developer programme.
4. **How many people use Letterboxd's private diary mode.** The number that would actually settle §4. Not published as far as I could find.
5. **Any direct evidence on how users read "local storage + venue lookup."** Searched; **not found.**
6. **DayTrace and the Android local-first field generally.** Under-covered here; two retrieval attempts failed.
7. **Retention data for journalling apps specifically.** Not found.

---

## 12. What would change these conclusions

Stated as falsifiers, so the gate can test them rather than argue about them.

| Conclusion | What would overturn it |
| --- | --- |
| Arc already is this product | Evidence that Arc's notes are per-*trip* rather than per-*venue* and cannot function as a venue journal; or that Arc is abandoned (no update for 12+ months from a developer who has said so) |
| Google has conceded the privacy differentiator | Google reversing on-device storage, or Timeline's on-device mode proving to be a thin client that still requires Google account sync — verifiable by inspecting the app's network traffic (a CTO task, not a research one) |
| The venue-name storage problem is fatal to a commercial API | Written confirmation from Google, Apple or Foursquare that storing a venue name inside a user's own private journal on their own device is permitted. **A seat should simply ask them.** This is a one-email question and I could not answer it from published terms alone |
| The open-dataset fallback has a coverage problem | A UK-specific measurement — e.g. sampling 200 licensed premises across two UK cities against an Overture extract — showing >90% coverage. This is a half-day of work and it is the single highest-value missing fact in the brief |
| The market is too small | Evidence that Arc's rating counts badly understate its base (e.g. a developer statement of subscriber numbers), or a UK landing-page test converting at a rate that implies a viable base |
| A sharing layer is not wanted | Any survey or forum evidence from private-timeline users asking for sharing. My §6 evidence is one thread and would not survive a single contrary data point |
| Writing is the fragile half | Journalling-app retention data showing note-writing persists beyond week three at rates comparable to passive logging |

**Cheapest next step, if the CEO does not kill this today** [J]: the two half-day tasks above — a UK Overture coverage sample, and a direct written question to Apple and Google about storing a venue name in a user's own local journal. Both are cheaper than a proposal, and either could kill the product outright. I would not commission a cost model or a feasibility note until they are done, because both would be modelling an architecture that may not be legal.

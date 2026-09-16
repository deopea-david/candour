# Compliance and regulatory note — Haunt

**Seat:** Chief Governance Officer · **Date:** 2026-09-10 · **Commissioned by:** gate preparation, ahead of the `haunt` gate
**Status:** Draft for the gate pack. **This is not a legal opinion and is not assurance** (Constitution 6.1).
**Slug:** `haunt` · Closes the gap flagged in [`proposals/haunt/proposal.md`](../../proposals/haunt/proposal.md) § "Constitution check → Regulatory exposure (CGO input)".

> **Template note.** `pipeline/templates/` holds no compliance-note template. This document is structured as the compliance register my charter requires ("what applies, current status, evidence") plus the six specific questions the commission asked. If the shape is useful it should be templated afterwards; I have not created a template unilaterally.

> **Standing of this document.** My charter says agent reviews *prepare and flag; they do not certify*. Constitution 6.1 says so too, and adds the harder rule: *"Before launch, anything involving personal data at scale, payments, health information, or regulated domains receives review by qualified human professionals."* Nothing below is a clearance. Where I say "compliant," read "I found no breach on the evidence I retrieved, and here is the evidence so you can check me."

---

## 0. Verdict in one page

**I do not block gate passage on regulatory grounds.** [J] Reasons and the one thing that would change that are in §8.

| # | Question | Finding | Blocking? |
| --- | --- | --- | --- |
| 1 | Does on-device storage of a venue name count as caching by Candour? | **Not avoided — deferred, and on the strongest retrieved evidence the answer is "yes, it counts."** Foursquare's own usage guidelines regulate *"local-device caching"* by name and cap it at 24 hours (Enterprise) or forbid it entirely (Pay as You Go). The MVP avoids the question only for as long as it ships no places API. §1 | Not at gate. **Blocking at build if any places API re-enters the architecture.** |
| 2 | Overture Places / CDLA-Permissive-2.0 attribution | The pack **overstates** the CDLA obligation and **understates** the Apache-2.0 one. CDLA-Permissive-2.0 contains *no attribution clause at all* — it requires the licence text to travel with shared data. The real hard obligation comes from the Foursquare-contributed portion under Apache-2.0. Both are cheap and neither is met by the design as currently written down. §2 | Not blocking. **Condition on PROCEED.** |
| 3 | UK GDPR posture | On the zero-network architecture Candour is, in my assessment, **neither controller nor processor** of journal data. That is an unusually strong position and it is entirely contingent on the architecture. §3 | Not blocking. |
| 4 | Consumer law | Apple is merchant of record; the 14-day statutory cancellation right is **lawfully waivable** for immediately-supplied digital content and Apple's flow does that. Constitution Article 4's "cancellation as easy as signup" has **little live meaning** here, and I say so rather than manufacture a finding. **I concur with the CFO's Article 4 block** and find an independent consumer-law hook for it. §4 | Not blocking. |
| 5 | Accessibility (WCAG 2.1 AA) | No UX seat has assessed this. **This is a condition on PROCEED, not a reason the gate cannot pass.** §5 | **Conditional.** My non-block depends on the decision record naming the UX commission as a condition of any PROCEED. |
| 6 | "Nothing leaves the device" | **Still not accurate**, even after the 2026-09-10 correction — the opt-in iCloud backup is itself a network call made by the app, and the corrected wording misses it. A precise claim is available and I have drafted it. §6 | Not blocking. **Asked to be fixed before the CEO decides**, since the pack rests its differentiator on this claim. |

**Constitution 6.1 — does this need qualified human legal review before launch?** My answer, stated plainly as commissioned: **on the MVP as proposed, no** — but only because the MVP removes the two triggers. **On any architecture that touches a places API, yes, unavoidably.** Full reasoning in §1.5.

---

## 1. The licence question with a cost consequence

**Commissioned question:** does storing a venue *name* on the user's own device, in the user's own journal, constitute "caching" by Candour under Google Maps Platform and Foursquare terms? Is the MVP's offline design genuinely avoiding this, or deferring it?

### 1.1 What I retrieved myself

I did not rely on the CTO's or the Research Analyst's retrievals for this. Where my retrieval failed, I say so.

| Source | What it says | Tag |
| --- | --- | --- |
| Foursquare **Usage Guidelines** — the primary document the CTO, the CFO and the Research Analyst all flagged as *not retrieved* | Unlimited caching is permitted for `venue_id`, `photo_id`, `fsq_addr_id` only. For **all other attributes**: Enterprise customers get *"24-hour local-device caching only (no server-based caching is permitted)"*; **Pay as You Go & Sandbox customers: "no caching permitted."** | [E] — [Foursquare, Usage Guidelines](https://docs.foursquare.com/developer/reference/usage-guidelines-personalization-apis) |
| Foursquare **API Licence Agreement** §2.1 | *"You must comply with the Places API caching and query rate limitations applicable to your Account-type (Self-Service 'Pay as You Go') set forth in our Usage Guidelines in the Developer Documentation."* | [E] — [Foursquare API Licence Agreement](https://foursquare.com/legal/terms/apilicenseagreement/) |
| Foursquare API Licence Agreement §2.2 | *"You must provide Foursquare with branded attribution (i.e., 'Powered by Foursquare') on any page or screen within Your Service where Places Data may appear."* | [E] — same |
| Google **Places API policies** | *"the **place ID**, used to uniquely identify a place, is **exempt from** the caching restrictions. You can therefore store place ID values indefinitely."* and *"You must not pre-fetch, cache, or store Places API content beyond the allowed exceptions."* | [E] — [Google, Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies) |
| Google Maps Platform Terms of Service §3.2.3 and Service Specific Terms §§A.3, 14.3 | **I could not retrieve these verbatim myself** — both pages exceeded my fetch tool's length limit and returned truncated content on two attempts. I therefore rely on the CTO's verbatim quotations at `feasibility-note.md` §2.1 and the Research Analyst's at `haunt-brief.md` §7.1, which are consistent with each other and with the developer-documentation page I *did* retrieve. | [E, second-hand within Candour — flagged. **Skeptic should re-retrieve at the gate if any online route survives.**] |
| Apple developer forum, DTS engineer **Ed Ford**, on whether short-TTL `sessionStorage` of geocoding results is permitted "temporary caching" under **Schedule 6 §2.5** of the Apple Developer Program Licence Agreement | *"Your questions on points 2 and 3 are related to interpreting the terms of the Apple Developer Program License Agreement, so that's not something I can discuss with you. I suggest you run those questions by your legal council."* | [E] — [Apple Developer Forums thread 807656](https://developer.apple.com/forums/thread/807656) |

**One correction to the pack.** The research brief attributes the *"may not be cached, pre-fetched, or stored by You or Your Application… temporary and limited basis"* wording to Apple Developer Forums thread 114220. **I fetched that thread and the passage is not in it** — the only licence text quoted there is the definition of "Apple Maps Service" [E — [thread 114220](https://developer.apple.com/forums/thread/114220)]. The clause may well exist (thread 807656 cites "Schedule 6 section 2.5" as its home), but **the citation as written in `haunt-brief.md` §7.3 does not support the quote**. Under `pipeline/evidence-standard.md` a citation without a retrieval behind it is the most serious offence in the standard, so I am recording this rather than letting it pass. It does not change any conclusion; the Apple route is dead on the DTS refusal alone.

### 1.2 The answer: on the best retrieved evidence, on-device storage **is** caching

**Foursquare settles it in Candour's disfavour, in its own words.** Foursquare does not treat "on the user's device" as an exemption — it treats it as a *category of caching with its own, shorter, allowance*. "24-hour **local-device caching** only" is a permission granted to Enterprise customers and withheld from Pay as You Go customers, who get *"no caching permitted"* [E, above]. A drafter who thought device-side storage fell outside "caching" would have had no reason to write that sentence. [I]

**Google's terms give no locus-based exemption either.** The permitted exceptions are defined by *field* (`place_id` indefinitely, lat/lng for a limited window) and not by *where the bytes sit* [E]. There is no clause I retrieved, and none quoted by any other seat, that turns on device versus server. [I]

**Apple's position is the strongest evidence of all, and it is evidence of unresolvability rather than of permission.** A developer asked Apple, in writing, whether storing geocoding results in the *user's own browser session storage* for a few minutes counted as permitted temporary caching. Apple's own Developer Technical Support declined to answer and told him to hire a lawyer [E]. If a few minutes in `sessionStorage` is a question Apple will not answer, "forever, in a SQLite file, on the user's phone" is not a question Candour gets to answer for itself. [I]

**The structural argument, stated so the CEO can weigh it rather than take it from me.** [I, from the [E] above] The "it's the user's device" theory requires arguing that the persistence is the *user's* act rather than Candour's. It is not. The user does not hold the API key; Candour does. The user does not issue the query; Candour's code does. The user does not design the schema that writes `venue_name TEXT` to disk and keeps it for a decade; Candour does. To succeed, the argument has to characterise Candour's own application as the user's agent rather than Candour's — and Candour would be advancing that characterisation against the party that drafted the contract, in a dispute it cannot afford to have. [J] That is not a position a one-person unincorporated brand should build a product on.

**My finding, stated plainly:** storing a venue *name* returned by Google Places or Foursquare in a permanent local journal is, on the retrieved evidence, **a breach of both providers' terms**, and the fact that the file lives on the user's phone does not rescue it. I hold this at **high confidence for Foursquare** (their own text regulates local-device caching by name) and **medium-high for Google** (their exceptions are field-scoped with no locus carve-out, but I could not retrieve §3.2.3 verbatim myself). [J on the confidence levels]

### 1.3 Is the MVP genuinely avoiding the question, or deferring it?

**Genuinely avoiding it — for exactly as long as the app makes zero places calls.** This is not a technicality. With no API call there is no Google Maps Content, no Places Data, no acceptance of either provider's terms, and Candour is not a "Customer" under either agreement at all. The question does not get answered; it stops existing. That is a real and unusually clean legal position, and it is the strongest thing about this architecture. [I]

**But four specific tripwires reopen it, and three of them are the most likely things to happen next.** [I/J]

1. **The "venue not found" fallback.** Overture's own documentation concedes *"duplicates, a high junk rate, and low property completeness"* [E — [Overture Places guide](https://docs.overturemaps.org/guides/places/), retrieved by CTO and Research Analyst; I did not re-retrieve]. Every miss lands on the user as "this app doesn't know where I am." The obvious, cheap, universally-requested fix is "let me search online for it." That single feature reimports the entire licence problem, and it will be proposed by a sympathetic user rather than by a cynical one. **This is the tripwire I would bet on.**
2. **Any use of Apple's `CLGeocoder`, `MKLocalSearch` or `MKMapItem`** — including a reverse-geocode to show a street name, or a map view behind the timeline. That is Apple Map Data under Schedule 6, which is the clause Apple will not interpret [E]. The zero-network promise and the licence cleanliness both depend on the app never touching these APIs, and **that is an architectural constraint, not a preference.** It needs to be written into the requirements document as a rule, and ideally enforced by a build-failing test in the same way the CTO proposes for diagnostic exports.
3. **Android.** The proposal makes Android an aspiration. If Android ever ships, the venue source question is re-opened on a platform where Overture's UK index has to be re-bundled or re-sourced.
4. **The CTO's own Block 1 lists "written confirmation from the provider that the intended retention is permitted" as a lifting condition** [`feasibility-note.md` §7]. That is a *deferral mechanism written into the pack*. It is a legitimate one, but the gate should understand that it parks the question rather than answering it, and that obtaining such confirmation from Google or Foursquare is, on the Apple precedent, unlikely to succeed. [J]

**Recommended condition if the CEO proceeds:** a one-line architectural rule in the requirements document — *"Haunt makes no network request of any kind and links no places, geocoding or map framework. Adding one is a gate-level change, not a feature."* Cheap now; a multi-week compliance retrofit later.

### 1.4 The cost consequence, since the commission asked for one

The CFO's §5 already shows it: on Google Places a one-off purchase "can never honestly be sold below about £62" [CFO, `cost-sheet.md` §5]. The licence finding above is what forces that. If on-device storage of names were permitted, the per-render re-query disappears, the metered cost collapses, and a £14.63 one-off works on a hosted API. It is not permitted, so it does not. **The £14.63 price in the proposal is downstream of this compliance finding, and if the finding is wrong the whole cost sheet changes.** That makes it load-bearing under the evidence standard, and it is why I re-retrieved it rather than accepting it.

### 1.5 Constitution 6.1 — does this require qualified human legal review before launch?

Stated plainly, as commissioned.

**6.1's text:** *"Before launch, anything involving personal data at scale, payments, health information, or regulated domains receives review by qualified human professionals. The company never represents an AI compliance opinion as assurance."*

**On the MVP exactly as proposed — zero network, bundled Overture index, no places API — my answer is NO, 6.1 does not require qualified legal review of the licence question**, for the simple reason that there is no licence to interpret. Candour is not a party to Google's or Foursquare's terms, and holds no personal data at all, at any scale. The three substantive triggers are absent. [I]

**On any architecture that queries a places, geocoding or map-data API and retains any returned field beyond a bare identifier, my answer is YES, unavoidably** — and I would not accept an agent's reading, *including this one*, as sufficient. Three reasons, and I want them separable so the CEO can reject one without rejecting all: (a) the money at stake is the entire pricing model, not a detail; (b) the counterparty in the one case where a developer asked directly refused to interpret its own clause and said "run those questions by your legal council" [E]; (c) Article 10 commits Candour to not implying legal force it does not have, and a seat writing "I think this is fine" over a contract-interpretation question is exactly the thing 6.1 was written to stop. [J]

**One trigger I am flagging rather than resolving, because it is genuinely arguable and it is the CEO's call.** 6.1 lists **"payments"**. Haunt takes a payment. On a narrow reading the trigger means *handling payment instruments* — card data, PCI scope, refunds — none of which Candour does, because Apple is merchant of record (§4.1). On a broad reading, any product that charges money engages it. I read it narrowly and think that is right [J], but I am not going to quietly adopt the reading that creates less work for me. **If the CEO reads 6.1 broadly, a professional review of the App Store commercial terms is required before launch, and that is a cost line nobody has priced.**

---

## 2. Overture Places, CDLA-Permissive-2.0, and what actually has to be in the app

### 2.1 I retrieved the licence, and the pack has it backwards

CDLA-Permissive-2.0 is five short sections. I retrieved the whole thing.

| Clause | Verbatim | Source |
| --- | --- | --- |
| 1.1 | *"A Data Recipient may use, modify, and share the Data made available by Data Provider(s) under this agreement if that Data Recipient follows the terms of this agreement."* | [E] — [SPDX, CDLA-Permissive-2.0](https://spdx.org/licenses/CDLA-Permissive-2.0.html) |
| **2.1 — the only obligation in the licence** | *"A Data Recipient may share Data, with or without modifications, so long as the Data Recipient makes available the text of this agreement with the shared Data."* | [E] — [cdla.dev](https://cdla.dev/permissive-2-0/), corroborated at [SPDX](https://spdx.org/licenses/CDLA-Permissive-2.0.html) (independent origins: Linux Foundation project site and SPDX licence list) |
| 3.1 | *"This agreement does not impose any restriction or obligations with respect to the use, modification, or sharing of Results."* | [E] — [cdla.dev](https://cdla.dev/permissive-2-0/) |
| 5.4 | *"Results"* means *"any outcome obtained by computational analysis of Data, including for example machine learning models and models' insights."* | [E] — same |

**There is no attribution clause in CDLA-Permissive-2.0.** The CDLA project says so itself: the attribution requirement that existed in version 1.0 was **deliberately removed** in 2.0, because *"attribution-style provisions… add an additional process step that may introduce complexity into the resharing of open data sets"* — while noting that this *"does not imply that recipients should not provide attribution"* [E — [CDLA FAQ](https://cdla.dev/faq-resources/faq/), retrieved via search summary of that page; **flagged: I read this through a search-result rendering of the FAQ rather than a clean fetch of the page itself, and the Skeptic should re-retrieve it directly**].

**So the pack is wrong in both directions, and the errors happen to cancel out into roughly the right behaviour:**

- `feasibility-note.md` §2.2's table records Overture Places as *"Yes. Attribution required."* under CDLA-Permissive-2.0. **Attribution is not required by that licence.** Overture *requests* the citation `"Overture Maps Foundation, overturemaps.org"`, which is a request, not a condition of the grant [E — [Overture attribution & licensing](https://docs.overturemaps.org/attribution/)].
- What *is* required, and what the pack does not name, is **§2.1: the text of the CDLA agreement must travel with the shipped data**. That is a different obligation from attribution and it is not satisfied by a credit line.

This is a correction, not a gotcha: the practical remedy is the same file either way. But a compliance register that records the wrong obligation will, at some later point, be used to justify the wrong design.

### 2.2 The obligation the pack understates: Apache-2.0 on the Foursquare portion

Overture's Places theme is fed by contributors on **different licences**, and the Foursquare-contributed portion is **Apache-2.0**, not CDLA [E — [Overture attribution & licensing](https://docs.overturemaps.org/attribution/)]. Apache-2.0's redistribution conditions are materially heavier than CDLA-Permissive-2.0's:

> **4(a)** *"You must give any other recipients of the Work or Derivative Works a copy of this License"*
> **4(b)** *"You must cause any modified files to carry prominent notices stating that You changed the files"*
> **4(d)** *"If the Work includes a 'NOTICE' text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file… in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, **within a display generated by the Derivative Works, if and wherever such third-party notices normally appear**."*

[E — [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)]

And Foursquare's own NOTICE.txt for OS Places requires the recipient to *"provide recipients with a copy of the License"*, to include prominent notices of changes made, and to *"preserve attribution to Foursquare, including preserving the full content of this NOTICE.txt file"* — with explicit guidance that a **flat-file distribution should include NOTICE.txt itself** [E — [Foursquare OS Places NOTICE](https://opensource.foursquare.com/places-notice-txt/)].

**A 21.3 MB SQLite file inside an iOS app bundle is a flat-file distribution.** [I] Candour is shipping a modified derivative of Apache-2.0 data to every user who installs the app.

**AllThePlaces contributions are CC0 1.0** and carry no obligation at all [E — [Overture attribution & licensing](https://docs.overturemaps.org/attribution/)].

### 2.3 Is the derived index "Data" or "Results"?

This is the one genuinely interpretive call in this section, and it decides whether §2.1 applies at all. [I]

The CTO's pipeline dedupes, confidence-thresholds and category-maps 346,184 records. An advocate could call that *"an outcome obtained by computational analysis of Data"* (5.4) and claim the Results exemption in 3.1, which would leave Candour with no CDLA obligation whatsoever.

**I do not accept that reading and I recommend the gate does not either.** 5.4's own examples are *"machine learning models and models' insights"* — outputs *about* the data. Haunt ships the records themselves: the same venue names, at the same coordinates, in a different container. That is Data shared "with modifications," which is precisely what 2.1 contemplates. [I]

The practical point that ends the argument: **complying costs one text file.** Constructing a Results argument to avoid shipping a licence text is the kind of clever-reading Article 9 exists to name. Ship the licence.

### 2.4 Does the proposed design meet these obligations? No — but only because nobody has written them down

I searched the pack for what the app actually displays. `feasibility-note.md` §3 specifies a `README.txt` inside the **export archive** carrying *"the dataset attribution notice."* That is the export, not the app, and it reaches only users who export. **There is no in-app licences or acknowledgements surface specified anywhere in the proposal, the feasibility note, or the cost sheet.** As written down, the design does not discharge CDLA §2.1, Apache §4(a), §4(b) or §4(d), or the Foursquare NOTICE.

It is a half-day of work, and it is the cheapest compliance item in this document. **Concrete remedy, which I recommend be attached as a PROCEED condition:**

1. **An in-app "Data sources and licences" screen**, reachable from settings in at most two taps. This is the Apache §4(d) *"display generated by the Derivative Works… wherever such third-party notices normally appear"* location — for an iOS app that is the Acknowledgements screen, and Apple ships apps with them routinely. It must contain: the **full text of CDLA-Permissive-2.0**; the **full text of Apache-2.0**; the **full, unaltered Foursquare OS Places NOTICE.txt**; and a **modification notice** naming what Candour did to the data (Overture release ID, UK bounding box, category filter, dedupe, confidence threshold) — that notice discharges Apache §4(b) and Foursquare's change-notice requirement at the same time.
2. The **same bundle of texts inside the export archive's `README.txt`**, since the export redistributes venue names too.
3. The Overture citation `"Overture Maps Foundation, overturemaps.org"` included as a courtesy, labelled internally as a request rather than an obligation so nobody later mistakes it for the compliance step.
4. **Publish the Overture release identifier** (`2026-08-19.0`) alongside it, so a reader can reproduce the index.

**Cost impact:** none worth modelling. It adds a static screen and no running cost. Constitution 1.5 is untouched.

### 2.5 The theme boundary — confirmed, and the specific way it will be crossed by accident

**Confirmed by my own retrieval.** Overture's attribution page lists the licences by theme: **Places is CDLA-Permissive-2.0**; **Base, Buildings, Divisions and Transportation are ODbL** [E — [Overture attribution & licensing](https://docs.overturemaps.org/attribution/)]. The CTO's §2.2 is correct on this.

**The concrete accident to guard against, which the pack does not name.** ODbL is share-alike: a Derivative Database must be offered under ODbL. The realistic way Haunt crosses that line is not a reckless decision — it is a UI requirement. The moment someone wants the timeline to read *"The Eagle, **Cambridge**"* rather than just *"The Eagle"*, the tempting source for the town name is Overture's **Divisions** theme, which is ODbL. Joining Divisions to Places to produce the shipped index makes the shipped index a derivative of ODbL data, and Candour must then publish it under ODbL. [I]

**The safe route is already available and free:** Overture Places records carry their own address fields within the Places theme. Locality must be taken from **inside Places**, never from Divisions. This belongs in the requirements document as a stated rule with the reason attached, not as tribal knowledge in one seat's head.

### 2.6 Article 8 and Article 7.2 interaction

**Article 8** (*"Open-source and self-hostable design is encouraged wherever possible, decided per initiative at its gate and recorded with reasons"*) applies only if the CEO designates Haunt a non-profit initiative — which is Model 4 in the CFO's cost sheet. **There is no licence conflict either way.** CDLA-Permissive-2.0 and Apache-2.0 both permit shipping the derived index in a closed-source app *and* both permit open-sourcing it. The licence choice does not constrain the Article 8 decision, and the Article 8 decision does not constrain the licence. [I]

**The interaction that does matter is with Article 7.2, and it is good news that nobody in the pack has claimed.** Article 7.2 requires that on discontinuation *"the product's code is open-sourced where third-party rights allow; where they don't, that is stated publicly with the reason."* On the Overture architecture, third-party rights **do** allow — CDLA-Permissive-2.0 §2.1 and Apache-2.0 §4 impose notice conditions, not publication bars [E, §2.1–2.2 above]. **So Haunt can actually keep the Article 7.2 promise in full, with no embarrassing carve-out.** On a Google Places architecture it could not: a journal of opaque `place_id` strings is neither open-sourceable as a working product nor exportable in a form that survives shutdown, which the CTO already identified [`feasibility-note.md` §2.1]. That is a second, independent constitutional reason the offline architecture is the right one, and I think it strengthens the pack rather than the case for killing it — I note it even though it cuts against the CVO's recommendation.

**If the CEO takes the CVO's "salvage the index" suggestion** and publishes the derived UK venue index as a standalone Candour artifact, that is itself "sharing Data" under CDLA §2.1 and a redistribution under Apache §4. The same four items in §2.4 must travel with it. The salvage is legal and I support it; it is not obligation-free.

---

## 3. UK GDPR

### 3.1 First, a correction to the commission's framing

The commission describes the location data as *"special category-adjacent, high-sensitivity."* The second half is right; the first half needs precision, because it changes what the law requires.

**Location data is expressly named as personal data** — UK GDPR Article 4(1) defines an identifiable person as one identifiable *"in particular by reference to an identifier such as a name, an identification number, **location data**, an online identifier…"* [E — [UK GDPR Art. 4, legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/article/4)].

**Location data is not special category data.** Article 9's closed list covers racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic and biometric data, health, sex life and sexual orientation. Location is not on it. [I from the Art. 4/Art. 9 structure]

**But a nightlife journal is a machine for inferring three of them.** A timeline of confirmed visits will, for some users, record attendance at a gay bar, a mosque, a synagogue, an addiction support meeting, a sexual health clinic or a trade union hall. Those inferences are Article 9 material even though the raw field is not. [I] So "special category-adjacent" is a fair description of the *risk*, and a wrong description of the *classification* — and the distinction matters, because if Candour ever processed this data itself it would need an Article 9(2) condition, realistically explicit consent, on top of an Article 6 basis. On the proposed architecture it needs neither, because it processes nothing. That is the whole finding, and §3.2 explains why.

### 3.2 Controller, processor, or neither?

**My assessment: neither.** I hold this at high confidence and it is still an assessment, not a certification (Constitution 6.1).

The reasoning, from the retrieved definitions:

- **Article 4(7):** a controller is the body *"which… determines the purposes and means of the processing of personal data"* [E — [UK GDPR Art. 4](https://www.legislation.gov.uk/eur/2016/679/article/4)].
- **Article 4(8):** a processor *"processes personal data on behalf of the controller"* [E — same].
- **Article 4(2):** processing means *"any operation or set of operations which is performed on personal data"* — collection, storage, retrieval, disclosure, erasure, and so on [E — same].

**Candour is not a processor**, plainly: there is no controller on whose behalf it could act, and it performs no operation on the data. [I]

**Candour is not a controller** for one blunt reason that survives every clever argument: **on the zero-network architecture Candour never has the data and has no technical means of obtaining it.** It writes software; the software runs on hardware Candour does not own, writing to a file Candour cannot read, backed up under a key Candour does not hold. Writing the code that a person uses to keep their own diary does not make the author of the code a controller of the diary, any more than the manufacturer of a notebook controls what is written in it. [I]

**And the user is out of scope too.** Article 2(2) excludes *"the processing of personal data by an individual in the course of a purely personal or household activity"* [E — [UK GDPR Art. 2](https://www.legislation.gov.uk/eur/2016/679/article/2)]. A person keeping a private journal of their own evenings out is the paradigm case. **So on this architecture there is no controller in the picture at all.** [I]

**This is a genuinely strong position and I want the gate to see how rare it is.** Most consumer apps arrive at "we're a controller, here's our lawful basis, here's our DPIA, here's our retention schedule." Haunt arrives at "there is nothing to be a controller of." That is not a compliance achievement Candour can take much credit for — it is a property of the architecture, exactly as Constitution 1.5 is — but it is real and it is worth stating in the decision record whichever way the decision goes.

**The three things that would destroy it**, each of which is an architectural choice and not an accident:
1. Any Candour-operated or Candour-contracted server that journal content transits or rests on — including a "sync between my own devices" relay.
2. Any Candour-held key, escrow, or recovery mechanism for the encrypted backup. The moment Candour *can* decrypt, it is arguably a controller of whatever it can reach. The proposed design's refusal to hold a recovery path is therefore a **compliance feature**, not just a security one, and the pack should say so.
3. Any telemetry SDK, however anonymised. Anonymisation is a judgement call that someone has to defend; "we transmit nothing" is not.

### 3.3 What Candour *is* a controller of — and the cost line nobody has priced

Candour is not a controller of journal data. It **will** be a controller of other personal data, and the pack currently ignores this entirely. [I]

- **Support correspondence.** The feasibility note budgets *"~2 hours/week of founder time on support"* [CTO §5]. That is an inbox full of named individuals describing their use of a location-tracking app. It is personal data, held by Candour, for Candour's purposes.
- **TestFlight testers.** Apple's own documentation records that *"TestFlight users share crash reports automatically regardless of device settings"* [E, quoted by CTO from [Apple, Acquiring crash reports and diagnostic logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs)]. Tester identities and their crash data land with Candour.
- **Any user-initiated diagnostic export a user emails in** (feasibility note §5, Layer 3). Pre-redacted, but sent to Candour's inbox.

**Consequence 1 — the ICO fee.** The Data Protection (Charges and Information) Regulations 2018 provide that *"A data controller must comply with the requirements of this regulation unless all of the processing of personal data they undertake is exempt processing"* and that *"Within the first 21 days of each charge period a data controller must pay a charge to the Information Commissioner"* [E — [reg. 2, legislation.gov.uk](https://www.legislation.gov.uk/uksi/2018/480/regulation/2/made)]. **I could not retrieve the tier amounts** — regulation 3 and the Schedule were not in the page I fetched, and the ICO's own site returned HTTP 403 to my tool on two attempts. So: **the obligation is [E]; the amount is not retrieved and I will not quote a figure from memory.**

**This is a missing line on the cost sheet.** `cost-sheet.md` §3 puts fixed annual running cost at £83 (Apple Developer Program plus a domain) and calls it *"a structural property of the architecture."* An annual ICO fee, whatever its exact amount, is a fixed annual cost of the same kind and it is not on the sheet. It is small. It is also precisely the sort of quiet omission Article 9's cost-inflation loophole works in reverse on — a published cost sheet that misses a real cost is inaccurate in the direction that flatters us. **Recommendation: CFO adds the line, with the retrieved amount, before any price is published.**

**Consequence 2 — a privacy notice is required, and it is not the one you'd expect.** Under Article 13 the notice has to cover the processing Candour actually does: support email and tester data. The temptation will be to publish a privacy policy that talks at length about the journal — which Candour does not process — and is silent on the inbox, which it does. That would be honest-sounding and wrong. **The notice should say, in this order: (1) the app itself sends nothing to Candour and Candour holds none of your journal; (2) here is the data Candour does hold, which is what you send us when you email us or join TestFlight; (3) here is how long we keep it and how to have it deleted.** Separately, App Store Connect requires a privacy policy URL for every app [K, high confidence — not retrieved this session; verify before submission].

### 3.4 DPIA — not owed, and I recommend writing something anyway

**Article 35(1):** *"Where a type of processing… is likely to result in a high risk to the rights and freedoms of natural persons, **the controller** shall, prior to the processing, carry out an assessment…"* [E — [UK GDPR Art. 35](https://www.legislation.gov.uk/eur/2016/679/article/35)]. The duty attaches to a controller. Candour is not one for this data (§3.2), so **no DPIA is legally required.** The Article 35(3) mandatory triggers are not met either: 35(3)(c) covers *"systematic monitoring of a publicly accessible area on a large scale"* [E — same], and Haunt monitors one consenting person's own movements on their own phone, not a public area, and not by Candour. [I]

**My charter says I produce "DPIA drafts where processing warrants one." This processing does not, and I am not going to manufacture one to look diligent.** Calling a document a DPIA when no DPIA is owed would overstate Candour's obligations and, worse, imply an assurance exercise that has not happened — which Article 10 and 6.1 both forbid.

**What I recommend instead, and would attach as a PROCEED condition:** a short, public **data protection position statement** — one page — setting out the architecture, the Article 2(2) and Article 4(7) analysis above in plain English, what Candour does hold (§3.3), and the specific things that would change the answer (§3.2's three destroyers). Reasons: it costs a morning; Article 3 makes transparency the default; and it is the cheapest available *evidence* for the marketing claim in §6. A claim backed by a published, checkable analysis is substantiated in the Article 4 sense. A claim backed by a slogan is not.

### 3.5 Constitution Article 4's export and deletion requirements

Two of Candour's own rules bind harder here than the law does, and the gate should notice that this is the constitution doing real work rather than restating statute. [I]

- **Export.** UK GDPR Article 20 portability runs to controllers. Candour is not one, so **Article 20 does not apply to Haunt.** Constitution Article 4 applies anyway: *"export in a usable, machine-readable format, available at any time, at no charge and with no penalty."* The CTO's design (documented JSON + CSV zip, lossless, with matching import) satisfies it, and the *import* half exceeds anything the law would ask for [`feasibility-note.md` §3]. Good. Keep it.
- **Deletion.** Constitution Article 4: *"Collect the minimum data necessary, state why, and delete it when no longer needed."* Candour collects nothing, so on the face of it this is free. **It is not free, and here is the gap I found:** the pack specifies backup creation and restore in detail [`feasibility-note.md` §4] and **specifies no deletion path for the backup at all.** A user who enables encrypted iCloud backup and later changes their mind must be able to delete the remote copy from inside the app, and must be told what happens to it if they simply delete the app. As written, ciphertext of a person's location history would sit in their iCloud indefinitely with no in-app way to remove it. That is not a legal breach — it is the user's own iCloud — but it is a plain Article 4 minimum-data failure and a trivially avoidable one. **Recommendation: "Delete my backup" is a launch requirement, and the backup-setup screen must state what deleting the app does and does not remove.**

### 3.6 PECR — the one nobody has looked at

Regulation 6 of the Privacy and Electronic Communications (EC Directive) Regulations 2003 — **substituted on 5 February 2026 by the Data (Use and Access) Act 2025** — now provides that *"a person must not store information, or gain access to information stored, in the terminal equipment of a subscriber or user,"* with paragraph (2) extending that to *instigating* such storage and to information automatically emitted by terminal equipment [E — [PECR reg. 6, legislation.gov.uk](https://www.legislation.gov.uk/uksi/2003/2426/regulation/6)].

Haunt stores information in the terminal equipment of a user, and it is Candour's software that instigates it. PECR binds "a person," not "a controller," so the §3.2 analysis does **not** dispose of it. [I]

**I assess the residual risk as low**, because a journalling app storing the user's journal in order to be a journalling app falls squarely within the strictly-necessary-for-a-requested-service exemption that this regime has always carried. **But I am flagging it rather than waving it through, for one honest reason: I could not retrieve the current exemption wording.** The page I fetched returned only paragraphs (1) and (2) of the substituted regulation and did not display the exemptions. The regulation was rewritten seven months ago and I will not assert the shape of an exemption I have not read. **Open item: retrieve the post-DUAA regulation 6 exemptions in full.** If a Constitution 6.1 human review happens for any reason, this is a cheap thing to put in front of it.

### 3.7 What reopening the sharing door would cost

The proposal closes this door deliberately and the Research Analyst's disagreement is on the record. My job is to price the reopening, not to reargue it. [I/J throughout]

**The instant any journal content touches infrastructure Candour operates or contracts for, Candour becomes a controller** — and every one of the following attaches at once, not gradually:

| Obligation | Why it bites here specifically |
| --- | --- |
| Article 6 lawful basis | Consent, realistically. Consent must be freely given, specific and withdrawable — which means a working withdrawal path, built. |
| **Article 9 condition** | This is the expensive one. A shared list of venues visited can reveal sexual orientation, religion or health (§3.1). Processing that requires an Article 9(2) condition — realistically **explicit** consent — and a defensible answer to "you knew what this data reveals." |
| **Article 35 DPIA — now mandatory** | Large-scale location data, new technology, high risk. Not optional, and it must precede the processing. |
| ICO registration and fee | Already owed for support data (§3.3); now unambiguous and at a higher tier. |
| Articles 13–14 privacy notice | A real one, covering the real processing. |
| Articles 15–22 rights machinery | Subject access, erasure, portability, objection — with statutory deadlines a solo operator must meet while also shipping. |
| Article 32 security | A server holding UK nightlife location histories is a target with a clear motive attached: blackmail. |
| **Articles 33–34 breach notification** | 72 hours to the ICO. And Constitution Article 3 already commits Candour to *"prompt disclosure to affected users; public summary after resolution"* — stricter than the statute, and self-imposed. |
| International transfers | Any US-hosted component brings a transfer risk assessment. |
| Children's code | A sharing product needs an answer on under-18 users that a private journal does not. |

**And three constitutional costs on top of the legal ones:**
1. **The marketing claim dies.** §6's claim is only available to an architecture with no outbound calls. It cannot be walked back gracefully; it can only be contradicted.
2. **Constitution 1.5 and 2.1.** A server is running cost, and running cost is price, and price is what the customer pays. The £83/year figure — the single strongest fact in the whole pack — stops being true.
3. **The Article 9 loophole the CVO already named.** The CVO's own words: the sharing layer *"is the only growth mechanism this product could ever have, so the option would be exercised for company reasons and then justified with user reasons."* That is a correct diagnosis and it is the reason to write the closure into the requirements document rather than leave it as a proposal-stage intention.

**My recommendation, whichever way the gate goes:** if Haunt proceeds, "no sharing layer" is recorded as a **gate-level commitment**, so that adding one requires a fresh gate with a fresh Skeptic memo — not a product decision made by whoever is looking at the retention numbers in eighteen months.

---

## 4. Consumer law

### 4.1 Merchant of record — and this closes an open item on the cost sheet

`cost-sheet.md` §2.1 flags as **not retrieved** that *"Apple acts as merchant of record and collects/remits UK VAT,"* records it as `[K, high confidence, unverified]`, and correctly says *"It affects the shelf price by 20% and must be verified before any price is published."*

**Retrieved.** Apple's own UK Media Services terms identify the contracting entity for UK users as **Apple Distribution International Ltd., Hollyhill Industrial Estate, Hollyhill, Cork, Republic of Ireland**, as merchant of record [E — [Apple Media Services Terms and Conditions (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html)].

**What that means, and it is more than a VAT technicality:** [I]

- **The consumer's contract of sale is with Apple, not with Candour.** Candour is not the consumer's counterparty for the purchase.
- **Candour cannot process a refund.** There is no mechanism. Refund requests go to Apple, are decided by Apple against Apple's criteria, and Candour learns of them only as a negative line in its proceeds. **This is a limitation that Article 1.3 requires Candour to state plainly** — *"We say what a product cannot do"* — rather than leave a customer to discover when they ask us for their money back and we cannot give it to them. It belongs in the app's support text and on the pricing page.
- **UK VAT is Apple's to collect and remit**, which is why the CFO's ex-VAT/inc-VAT split is the right presentation. [I] The CFO's arithmetic stands; the assumption under it is now [E] rather than [K]. **The `[K, unverified]` tag on `cost-sheet.md` §2.1 can be upgraded.**

### 4.2 Cancellation and refund obligations

The statutory position, retrieved from both ends:

- **Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, reg. 37** — a consumer loses the right to cancel a digital content contract where *"supply of the digital content has begun after the consumer has given the consent and acknowledgement required"*, and the consumer bears no cost where they did not agree to early supply, or were not told they would lose the right, or did not receive the required confirmation [E — [reg. 37, legislation.gov.uk](https://www.legislation.gov.uk/uksi/2013/3134/regulation/37)].
- **Apple's UK terms already operate that waiver:** *"If you choose to cancel your order, you may do so within fourteen (14) days of when you received your receipt, without giving any reason"* — followed by *"You cannot cancel your order for the supply of Content if the delivery has started upon your request and acknowledgement that you thereby lose your cancellation right."* [E — [Apple Media Services Terms (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html)]

[I] So: the 14-day right exists, it is lawfully waivable for immediately-delivered digital content, and Apple's purchase flow performs the waiver. **Candour has no cancellation obligation of its own to discharge, and no ability to discharge one.** What Candour retains is the Consumer Rights Act quality regime — s.36 provides that *"Every contract to supply digital content is to be treated as including a term that the digital content will match any description of it given by the trader to the consumer,"* and s.36(3) treats pre-contract information about *characteristics and functionality* as a contractual term [E — [CRA 2015 s.36, legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/15/section/36)]. That matters for §6: App Store description copy is not marketing, it is a term.

### 4.3 Does "cancellation as easy as signup" have live meaning here? Mostly no — and I am not going to invent one

**The honest answer:** for a one-off purchase with no account, no subscription and no server, Constitution Article 4's *"Make cancellation as easy as signup"* has **almost no literal application**. There is no signup. There is nothing to cancel. Cancellation of the *purchase* is Apple's process, not Candour's, and Candour could not make it harder or easier if it tried. [I]

I could dress this up into a finding. I would rather record that a clause aimed at subscription traps does not bite on a product that is not a subscription — and note that the clause **will** bite hard if the CFO's Model 3 (subscription) is ever revived, which is a reason to record the reading now while nothing depends on it.

**What survives is the clause's purpose**, and this part *is* live: *leaving must be no harder than arriving*. Mapped onto a one-off, accountless, serverless app, that produces four testable requirements:

1. **Export works at any time, free, complete** — already designed [`feasibility-note.md` §3]. ✅
2. **The encrypted backup can be deleted from inside the app** — **not designed** (§3.5 above). ❌ Fix before launch.
3. **Nothing impedes uninstall**, and no re-engagement mechanics fire when the user stops using it. Article 4's dark-pattern prohibition covers this and the pack's "no engagement mechanics" stance already implies it.
4. **Nothing continues to exist after uninstall except what the user chose to keep** — and the app says so, at the moment backup is enabled, in plain words.

Those four are what Article 4's cancellation clause means for this product. I recommend they go in the requirements document as acceptance criteria rather than being carried forward as a clause everyone agrees is inapplicable.

> **⚠ CORRECTED 2026-09-16 — see Correction C1 in `decisions/2026-09-16-haunt-gate.md`.** The reasoning in this section is **conceded and superseded**. It read Article 4's export clause as prohibiting a read-cap. The clause's modifiers ("at any time, at no charge and with no penalty") attach to **export**, not to the user's data generally (C1.1), and its "costs Candour nothing" argument substituted marginal cost for the Constitution's defined total cost, which includes benchmarked build labour (C1.2). **A clearly-disclosed, non-retroactive read-cap with complete free export and no compulsion machinery is not prohibited by the Constitution.** The text below is preserved unaltered so the error remains inspectable; **do not cite it.**

> **⚠ AMENDED 2026-09-17 — see Correction C2.** When written, the sentence above claimed something about the **whole** Constitution while resting on a correction that disposed of one clause and never mentioned the other clause this same document had cited. It happened to be true; it was not supported. **Correction C2.2 now supports it**, having disposed of Article 1.2 on its own words and checked all four of its limbs. **Two dependencies travel with the sentence and it is false without either:** it holds **only** while export remains complete and unconditional under Condition 8.3 — if export ever ships against the visible set rather than the full set, Article 1.2's lock-in limb revives — and **only** while the cap is disclosed before the first entry under 8.1. C2.3 also records what it does **not** establish: the real objection was withholding rather than lock-in, and **no clause of the Constitution reaches that** — a gap now named in Article 10.

### 4.4 The free-tier read-cap: I concur with the CFO, and I go further

**The CFO's finding**, at `cost-sheet.md` §8.2: a free tier showing only the last 30 days or last 50 entries *"Withholds the user's own local data behind a paywall. Article 4 (data at any time, no penalty), Article 1.2 (lock-in). This is the most tempting design and the clearest breach."* The CFO states it as a launch-blocking defect and reserves the block.

**I concur, without qualification, and I record my own block on the same facts.** My charter's block is gate passage; the CFO's is unpriced or uncosted launches; the UX seat holds one on Article 4 grounds. Three independent seats can stop this design and I would expect all three to. The article text is unambiguous: *"Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge and with no penalty."* A read-cap is a penalty, applied at any time, to the user's own data.

**Where I go further than the CFO.** [I] On a hosted product, a read-cap at least withholds something the vendor is paying to store. **Here it does not.** The entries sit in a SQLite file on hardware the customer owns, which Candour has never seen, cannot see, and pays nothing to hold. A read-cap would be Candour's software refusing to render a file on the customer's own device in order to extract a payment. There is no cost basis, no service being withheld, and no honest way to describe it. It is closer to a hostage than to a paywall, and I want that in writing before anyone proposes it under commercial pressure in eighteen months.

**And the finding the pack has not joined up.** The CFO's compliant free-tier design — *"Cap the automatic venue lookups (the only thing that costs money per use) and leave entries, history, editing and export unlimited forever"* — was engineered against the **metered-API** architecture. The proposal then adopts the **offline** architecture, and observes in passing that *"on the offline architecture there is no per-lookup cost at all, so the only compliant basis for a free tier disappears with it."* Nobody has drawn the conclusion. **I draw it: on the MVP as proposed there is no cost-aligned free tier available, because there is no marginal cost to align one to.** Any cap would gate something that costs Candour nothing, which makes it arbitrary scarcity rather than a pricing mechanism.

That does not make every free tier unlawful or unconstitutional — a **time-limited full-feature trial** is neither a dark pattern nor a read-cap, and remains available. But the compliant space is narrow and worth stating exactly:

> **Permitted:** a trial limited in *time* or in *future creation*, disclosed before the user writes anything, after which everything already written remains readable, editable and exportable forever, at no charge.
> **Not permitted:** any limit on reading, editing, or exporting entries the user has already created — in any tier, at any price, ever.

**Recommendation: the second line becomes a standing product rule for Haunt, recorded at the gate**, so it binds without needing three seats to re-derive it each time.

### 4.5 Does UK consumer law reach the read-cap independently?

**Partly — and the honest answer is more interesting than a clean yes.** [I]

**Where the law does reach it:** if the cap is not disclosed before the user starts writing. DMCCA 2024 s.227 makes a commercial practice a misleading omission where it *"omits material information"* — defined as *"information that the average consumer needs to take an informed transactional decision"* — and expressly catches information given *"in a way that is unclear or untimely, or in such a way that the consumer is unlikely to see it"* [E — [DMCCA 2024 s.227, legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2024/13/section/227)]. "You may write freely; we will later stop you reading what you wrote" is material information, and revealing it after the writing is the definition of untimely. s.226 would also be engaged if the free tier were presented as offering something it does not [E — [s.226](https://www.legislation.gov.uk/ukpga/2024/13/section/226)]. These provisions came into force on **6 April 2025** and the CMA now has direct enforcement powers with penalties reaching 10% of global turnover [E, **secondary sources, law-firm briefings, single underlying origin — flagged for verification**: [Hill Dickinson](https://www.hilldickinson.com/our-view/articles/digital-markets-competition-and-consumers-act-2024-new-consumer-law-protections-now-in-force/), [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2026/04/subscription-contracts)].

**Where the law does not reach it:** if the cap is disclosed clearly and up front. A plainly-stated "free tier shows 30 days" is not a misleading omission, because nothing is omitted. A consumer who buys with full knowledge has been told the truth, and CRA s.36 is satisfied because the digital content matches its description.

**So the answer the gate needs:** in the disclosed case, **Constitution Article 4 is the only thing standing in the way — and it stands there alone.** UK law permits a clearly-signposted read-cap. Candour's constitution forbids it. That gap is not a drafting accident; it is the entire point of having written the constitution down before there was money at stake, and it is exactly the kind of moment Article 10 anticipated. **I would want the decision record to say that explicitly**, because "we didn't do the legal thing because our own rules forbid it" is the most valuable sentence a governance document can produce, and it is worth nothing if it is not written down when it happens.

**Not applicable, recorded so nobody re-derives it:** the DMCCA subscription-contracts regime does not bite, both because Haunt is a one-off purchase and because commencement has been pushed to **spring 2027** [E, secondary — [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2026/04/subscription-contracts), [Hogan Lovells](https://www.hoganlovells.com/en/publications/uk-subscription-law-shakeup-new-rules-pushed-to-autumn-2026); **single underlying origin (DBT consultation response, 2 April 2026), not retrieved at source**]. If the CFO's Model 3 is ever revived, this regime is a material new cost and must be re-priced, not assumed.

---

## 5. Accessibility

### 5.1 A precision point about the standard itself, which nobody has made

Constitution Article 4 requires products to *"Meet accessibility standards (WCAG 2.1 AA as the working baseline)."*

**WCAG 2.1 is a standard for web content.** W3C states the guidelines apply to *"web content on any kind of device (including desktops, laptops, kiosks, and mobile devices)"* [E — [W3C, WCAG 2.1](https://www.w3.org/TR/WCAG21/)]. **Haunt is a native iOS application, not web content.**

The bridge exists and is called **WCAG2ICT**: *"This document describes how the Web Content Accessibility Guidelines (WCAG) versions 2.0, 2.1, and 2.2 principles, guidelines, and success criteria can be applied to non-web Information and Communications Technologies (ICT), specifically to non-web documents and software"*, and it acknowledges that *"the application of WCAG 2 to documents and software in non-web contexts necessitates some interpretation"* and that *"addressing accessibility for non-web documents and software may involve requirements and considerations beyond those included in this document"* [E — [W3C, WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/)].

**This is not a loophole and I am not offering it as one.** The constitution says "working baseline," which is exactly the right phrase for a standard that needs interpretation to apply. But "meet WCAG 2.1 AA" is not a self-executing instruction for an iOS app, and if nobody writes down what it means here, it will be discharged by whatever the engineer happened to do. **The operative target should be recorded as: WCAG 2.1 AA as interpreted by WCAG2ICT for non-web software, implemented through Apple's accessibility APIs** — VoiceOver, Dynamic Type, contrast, Reduce Motion, and the rest. That is a one-line addition to the requirements document and it makes the QA seat's job possible, because "verify WCAG 2.1 AA" is not testable and that sentence is.

### 5.2 UK and EU legal position, briefly

- **Equality Act 2010 s.29(7):** *"A duty to make reasonable adjustments applies to— (a) a service-provider…"* [E — [s.29, legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2010/15/section/29)]. Whether a one-off paid app is "a service" for s.29 is arguable [J]; the prudent working assumption for a UK trader selling to UK consumers is that it is, and the duty is anticipatory. Meeting the Article 4 baseline discharges it in practice.
- **European Accessibility Act (Directive (EU) 2019/882).** Not UK law, and relevant only if Haunt is sold into EU storefronts. Even then: Article 4(5) — *"Microenterprises providing services shall be exempt from complying with the accessibility requirements referred to in paragraph 3 of this Article and any obligations relating to the compliance with those requirements"* — and Article 3(23) defines a microenterprise as *"an enterprise which employs fewer than 10 persons and which has an annual turnover not exceeding EUR 2 million or an annual balance sheet total not exceeding EUR 2 million"* [E — [Directive 2019/882, EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng)]. Candour is one person. **The exemption is available on the services limb; the products/services boundary for an app is not something I can resolve** [J, flagged]. Two cheap dispositions, and the CEO should pick one at the gate rather than discover it at submission: restrict storefront availability to the UK at launch, or accept the residual and rely on the microenterprise exemption. Meeting WCAG 2.1 AA properly makes the question largely academic either way. **Public-sector accessibility regulations do not apply** — Haunt is not a public sector body.

### 5.3 The commissioned question: bar to gate passage, or condition on PROCEED?

**My answer: a condition on PROCEED. It is not a reason the gate cannot pass, and I will not manufacture one.**

The reasoning, because the CEO should be able to disagree with it:

1. **WCAG conformance is a property of a built artifact.** Haunt has no screens. A conformance assessment now would be fiction. Constitution 5.1 puts the gate *before* build for exactly this reason, and reading Article 4 to require conformance evidence at the gate would make every gate un-passable for every product Candour ever builds. That cannot be the meaning. [I]
2. **But something assessable *is* missing**, and I want to be precise about what: not conformance, but a **UX seat's view on whether this product concept has accessibility problems and what conformance will cost**. That is entirely possible today, takes a day, and has not been done. The Skeptic makes the same point at O7 and lists it among the harmed parties: *"On the proceed branch this is the cheapest gap in the pack to close and the most expensive to discover late."* I agree with the Skeptic in full.
3. **So why condition rather than block?** Because the CVO's standing recommendation is **KILL**, and blocking gate passage to commission a UX read for a product the proposing seat wants killed spends a seat's week and a slice of the Constitution 5.2 clock producing an artifact for something that will not be built. 5.2 exists to stop process consuming the calendar. [J]

**The precise form of my position, so it is not mush:**

> I do not block gate passage. **My non-block is conditional on the decision record naming the UX commission as an explicit condition of any PROCEED.** If the CEO decides PROCEED without that condition attached, my block under Constitution 5.6 engages, and what lifts it is the commission.

That gives the CEO a real choice with a stated consequence, which is what a block is supposed to be.

### 5.4 What I would put in front of the UX seat, so the commission is not a blank page

Six things I can already see from the artifacts, offered so the UX read is cheap when it happens [J, all of them]:

1. **A chronological timeline is a VoiceOver ordering problem**, and dense rows (venue, time, rating, note preview) are where reading order goes wrong.
2. **Star ratings are the single most common accessible-name failure in consumer apps.** "Three stars" must be announced, and settable, without sight.
3. **The "were you here?" prompt is time-sensitive**, which engages WCAG 2.2.1 Timing Adjustable. A prompt that expires is a prompt some users cannot answer.
4. **Dynamic Type at the largest accessibility sizes** against a timeline row that wants to show four things at once.
5. **Confirmed vs unconfirmed state must not be encoded in colour alone** (1.4.1).
6. **The passphrase and recovery-code flow is the highest-stakes screen in the product**, and it is the one where a mistake is permanently unrecoverable by design — the CTO says so plainly: *"There is no recovery, there is no reset link, and Candour cannot help."* **An accessibility failure on any other screen is an inconvenience; an accessibility failure on that screen is permanent data loss for a disabled user.** If the UX commission does only one thing, it should do that screen. I regard this as the most important single sentence in this section.

---

## 6. Marketing claims — "nothing leaves the device"

### 6.1 The proposal has already been corrected once, and the correction is not yet sufficient

Between my commission and this draft, the proposal was amended (2026-09-10) after the Skeptic caught the CVO overstating the claim. The proposal now carries the correction on its face and offers this substantiable version:

> *"Your timeline, notes and ratings never leave your device. The app makes no network calls of its own. If you opt in to Apple's crash reporting, Apple receives crash diagnostics — never your journal."*

**That correction is right, well-made, and I endorse the reasoning behind it. It is also still not accurate, and I have to say so.** It fixes the crash-reporting omission and leaves a larger one standing.

### 6.2 The omission the correction missed: the backup is a network call, made by the app

`feasibility-note.md` §4 specifies opt-in encrypted backup **to CloudKit** — the app encrypts the export archive and *"upload[s] the **ciphertext**: CloudKit private DB (also using `encryptedValues`, belt and braces)"*.

**An upload is a network call, and Haunt is the thing making it.** [I] So:

- *"The app makes no network calls of its own"* is **false whenever backup is enabled**. It is not a network call made by the platform on Haunt's behalf; it is Haunt's own code sending Haunt's own bytes to a remote server.
- *"Your timeline, notes and ratings never leave your device"* is **false whenever backup is enabled** — the timeline leaves the device, as ciphertext, at the user's instruction, to the user's own iCloud. Encrypted departure is still departure.

The amended headline sentence — *"No network calls of any kind **in the app's own operation**"* — hedges with a qualifier that does not survive contact: a user-enabled backup running inside the app is the app's own operation. **I would rather Candour dropped the qualifier and stated the truth**, which is genuinely impressive without any hedging at all.

This is the third iteration of the same mistake in one pack: a claim gets stated absolutely, someone finds the exception, the claim is narrowed, and the narrowed claim has its own exception. [J] That pattern is worth naming as a pattern, because the fix is not another edit — it is to write the claim from the architecture rather than from the marketing instinct, once, and then hold it.

### 6.3 What may be said

Drafted from the architecture. Every clause is checkable against a named artifact.

> **Haunt makes no network calls except the ones you switch on. Out of the box it makes none at all — no account, no sign-up, no analytics, no venue lookups, no servers of ours anywhere, because we don't have any. Venue names come from a database that ships inside the app, so it works in a basement, on the Tube, and in aeroplane mode.**
>
> **Two things can leave your phone, and only if you choose them. If you turn on backup, Haunt uploads an encrypted copy of your journal to your own iCloud. It is encrypted on your phone with a passphrase only you hold: Apple can't read it, and we never receive it at all. And if you leave Apple's crash reporting switched on, Apple — not us — receives crash diagnostics. Those never contain anything you wrote.**
>
> **We hold no key and no copy. If you lose your passphrase, we cannot recover your backup, and nor can anyone else. That is what this promise costs.**

### 6.4 What may not be said

| Claim | Why not |
| --- | --- |
| "Nothing leaves the device." | False on two counts (§6.2). Under DMCCA 2024 s.226 a misleading action includes *"the provision of false or misleading information relating to a product… relevant to a transactional decision"* [E — [s.226](https://www.legislation.gov.uk/ukpga/2024/13/section/226)]. And App Store description copy is not merely marketing: CRA 2015 s.36 makes description a **term of the contract**, with s.36(3) capturing pre-contract information about characteristics and functionality [E — [s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36)]. This claim would be a false statement in a contractual term, not a bit of enthusiastic copy. |
| "Zero network calls" / "no network calls of any kind", unqualified. | Same defect. |
| "End-to-end encrypted" without qualification. | Apple's own documentation makes third-party CloudKit E2EE **conditional on Advanced Data Protection** [E, quoted by CTO from [Apple, iCloud data security overview](https://support.apple.com/en-gb/102651)]. Candour's *own* passphrase encryption is what makes the promise unconditional — so the honest claim is "we encrypt it before it leaves, with your key," not a borrowed platform term. |
| "We never collect any data." | Candour collects support email and TestFlight data (§3.3). The claim is about the app; stating it about the company is false. |
| Anything about Android. | Already closed by the proposal: Android may not be marketed before the device-matrix spike. I endorse this without reservation and note it is the same Article 4 rule as everything else in this section. |
| "£83 a year to run." | Not until the ICO fee line is on the cost sheet (§3.3). A published cost sheet with a real cost missing is inaccurate in the direction that flatters us, and Article 3 makes it public. |

### 6.5 The App Privacy label — and a recommendation that costs us a differentiator

Apple's rules would let Haunt declare **Data Not Collected**:

- *"'Collect' refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time."*
- *"Data that is processed only on device is not 'collected' and does not need to be disclosed in your answers."*
- *"You are not responsible for disclosing data collected by Apple."*

[E — all three verbatim from [Apple, App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/)]

That is a real competitive fact: Arc Timeline 4's own App Privacy declaration lists **Diagnostics (Crash Data, Performance Data) as collected** [E — verified independently by the Skeptic at dissent-memo verification item #1]. A clean "Data Not Collected" label would be visibly stronger than the strictest incumbent in the category.

**I recommend Candour does not take it, and declares Diagnostics → Crash Data anyway.** [J]

The reasoning: Apple's two rules are in tension for exactly Haunt's case. *"You are not responsible for disclosing data collected by Apple"* points one way; *"transmitting data off the device in a way that allows you… to access it"* points the other, because Candour **does** access those crash reports, in the Xcode Organizer, for as long as they sit there. I cannot resolve that tension from the published rules and I am not going to pretend I can. What I can see is the asymmetry: **over-declaring costs one line in a label; under-declaring means the label says "Data Not Collected" while the marketing copy in §6.3 truthfully tells the user Apple receives crash diagnostics.** A sceptical reader who notices that will not conclude Candour read Apple's exemption carefully. They will conclude Candour took the flattering option.

Declaring it still leaves Haunt ahead of Arc — crash data only, not linked, versus crash *and* performance — and it makes the label and the sentence agree. Article 1.3 says *"Pricing, capability, and limitations are stated plainly."* This is a limitation. State it.

**The alternative disposition, which is also honest:** don't receive crash reports at all, decline the Organizer, and rely solely on the user-initiated diagnostic export. Then "Data Not Collected" is unarguable. The CTO's §5 gives a real reason not to — Jetsam events matter for a background-location app and are the gap Layer 3 exists to cover — so I do not recommend it. **But it is the CEO's call under 5.4, because it is a user-data-policy decision, and it should be made deliberately rather than inherited from the CTO's diagnosis design.**

### 6.6 Making the claim evidence rather than assertion

Article 4: *"claims we cannot substantiate are claims we do not make."* The clause is about substantiation, not phrasing, so the strongest response is evidence a stranger can check. Three cheap ones, all of which I'd attach as PROCEED conditions:

1. **A build-failing test that no networking symbol is linked into the app except the backup module.** The CTO already proposes exactly this pattern for the diagnostic export — *"a build-failing test that journal text can never enter it."* Extend it. Then "the app makes no network calls except backup" stops being a promise and becomes a property of the build.
2. **Publish the backup's cryptographic design** — KDF, parameters, cipher, what is encrypted and when. It costs a page, it is what "Candour holds no key" means in checkable terms, and Article 3 already commits to publishing everything except *"security-sensitive implementation details"* — which a published crypto design is not, since the security rests on the key and not on the design being secret.
3. **Publish the data protection position statement** from §3.4. Same reason.

---

## 7. Compliance register — Haunt

What applies, current status, evidence. This is the artifact my charter requires per product; it should be updated at every phase end, not rewritten.

| # | Obligation | Applies? | Status | Evidence / where |
| --- | --- | --- | --- | --- |
| C1 | Google Maps Platform terms | **No**, on the MVP | Not a party — no API calls | §1.3 |
| C2 | Foursquare API Licence + Usage Guidelines | **No**, on the MVP | Not a party | §1.3 |
| C3 | Apple Developer Program Licence, Schedule 6 (Map Data) | **No**, on the MVP | Only if MapKit/CLGeocoder/MKLocalSearch are linked. **Architectural tripwire** | §1.3(2) |
| C4 | CDLA-Permissive-2.0 §2.1 — licence text ships with the data | **Yes** | ❌ **Not met as designed** | §2.1, §2.4 |
| C5 | Apache-2.0 §4(a)(b)(d) — licence copy, change notices, NOTICE contents | **Yes**, via the Foursquare-contributed portion of Overture Places | ❌ **Not met as designed** | §2.2, §2.4 |
| C6 | Foursquare OS Places NOTICE.txt preserved in full | **Yes** | ❌ **Not met as designed** | §2.2, §2.4 |
| C7 | ODbL share-alike | **No**, provided only the Places theme is used | Rule needed in requirements; Divisions is the accident to guard against | §2.5 |
| C8 | UK GDPR — controllership of journal data | **No** — Candour is neither controller nor processor | Assessed, not certified | §3.2 |
| C9 | UK GDPR — controllership of support/tester data | **Yes** | ⚠️ Unaddressed in the pack | §3.3 |
| C10 | ICO registration and annual charge | **Yes**, following from C9 | ⚠️ **Missing cost line.** Amount not retrieved | §3.3 |
| C11 | Art. 13 privacy notice | **Yes**, scoped to C9 | ⚠️ Not drafted | §3.3 |
| C12 | Art. 35 DPIA | **No** — duty attaches to a controller | Voluntary position statement recommended instead | §3.4 |
| C13 | Art. 20 portability | **No** — duty attaches to a controller | Constitution Art. 4 binds harder and is met | §3.5 |
| C14 | Constitution Art. 4 — export | **Yes** | ✅ Met, and exceeded (import at MVP) | `feasibility-note.md` §3 |
| C15 | Constitution Art. 4 — deletion / minimum data | **Yes** | ❌ **No backup-deletion path designed** | §3.5 |
| C16 | PECR reg. 6 (as substituted 5 Feb 2026) | **Yes**, on its face | ⚠️ Low risk; exemption wording **not retrieved** | §3.6 |
| C17 | CCR 2013 — 14-day cancellation | **Yes**, discharged by Apple's flow | ✅ No Candour obligation; must be *stated* | §4.2 |
| C18 | Merchant of record / UK VAT | **Yes** — Apple Distribution International Ltd | ✅ Verified; closes a cost-sheet `[K]` | §4.1 |
| C19 | CRA 2015 ss.34–36 — quality, description | **Yes** | Bites on App Store copy as a contractual term | §4.2, §6.4 |
| C20 | DMCCA 2024 ss.226–227 — misleading actions/omissions | **Yes**, in force 6 Apr 2025 | Bites on the claim (§6) and on any undisclosed cap (§4.5) | §4.5, §6.4 |
| C21 | DMCCA subscription regime | **No** — one-off purchase; commencement spring 2027 | Re-price if Model 3 revives | §4.5 |
| C22 | Constitution Art. 4 — WCAG 2.1 AA (per WCAG2ICT) | **Yes** | ❌ **No UX assessment exists** | §5 |
| C23 | Equality Act 2010 s.29(7) reasonable adjustments | **Probably** | Discharged in practice by C22 | §5.2 |
| C24 | European Accessibility Act | **Only if sold in EU storefronts**; microenterprise services exemption available | CEO to pick a disposition at the gate | §5.2 |
| C25 | Constitution Art. 4 — honest marketing | **Yes** | ⚠️ Corrected once; **still inaccurate** | §6 |
| C26 | Constitution Art. 3 — cost sheet published, accurate | **Yes** | ⚠️ Blocked by C10 | §3.3 |
| C27 | App Store privacy label accuracy | **Yes** | Decision required (declare or not) | §6.5 |
| C28 | Constitution Art. 7.2 — open-source on discontinuation | **Yes**, on discontinuation | ✅ Deliverable in full on this architecture | §2.6 |

**Eight items are red or amber and every one of them is cheap.** None requires a server, a lawyer, or a redesign. That is the honest headline of this register, and it cuts in favour of the architecture rather than against it.

---

## 8. My position on gate passage (Constitution 5.6)

### 8.1 The power, stated before I say whether I'm using it

Constitution 5.6 and my charter give the CGO a block on **gate passage**, for *"constitutional breach, unanswered dissent, or missing compliance evidence."* My charter also constrains how I may use it: *"Every block must cite the specific article, standard, or acceptance criterion breached and state what would lift it — a block is a checklist item failing, never a feeling of unease."* A block halts the blocked action; only the CEO may overrule, and the overrule is recorded publicly.

### 8.2 I do not block. Here is why, and here is what my non-block is conditional on

**I do not block gate passage on regulatory grounds.** [J]

There is no constitutional breach to cite, because nothing has been built. Every red item in §7 is a *design* defect in an unbuilt product — a licence screen that has not been specified, a deletion path that has not been drawn, a claim that has not yet been printed anywhere a customer can read it. Blocking a gate for defects that build has not yet had the chance to introduce would be a block on a feeling of unease, which my own charter forbids.

**Three conditions, and I state the consequence of omitting each:**

> **Condition 1 — UX commission on the PROCEED branch.** The decision record must name it. If a PROCEED issues without it, my block engages (§5.3).
>
> **Condition 2 — the marketing claim is corrected again, in the proposal, before the CEO decides.** The claim as it currently stands is inaccurate (§6.2), it is a claim the pack rests its only differentiator on, and CRA s.36 makes it a contractual term rather than copy. This one I would like fixed *before* the decision rather than after it, because the CEO is being asked to weigh a differentiator and should be weighing the true version of it. If the pack reaches the CEO uncorrected, that is a defect in the pack and I will record it as one in the review pack.
>
> **Condition 3 — the C4/C5/C6 licence surface and the C15 backup-deletion path are written into the requirements document on the PROCEED branch.** These are half-day items that become expensive only if discovered after the schema and the settings tree exist.

**And one thing I want on the record as not being a condition, because it would be easy to add and wrong.** I am **not** requiring qualified human legal review before launch on the MVP as proposed. I could have. It would have been the cautious-looking answer and it would have cost the company money for nothing. There is no licence to interpret, no personal data held, and no payment instrument touched (§1.5). The trigger is real and it is not pulled here. **If the architecture changes to include any places, geocoding or map-data API, it is pulled, and no agent — including me — can un-pull it.**

### 8.3 What I would say if asked which way to decide

I was not commissioned to recommend kill or proceed and I am not going to smuggle one in. Two observations that belong to my seat and that the gate should weigh alongside the CVO's KILL and the Skeptic's memo:

1. **The compliance position of this architecture is the best I expect to see at Candour.** Neither controller nor processor; no third-party terms accepted; Article 7.2's open-sourcing promise deliverable in full; the marketing claim, once stated accurately, still stronger than the strictest incumbent's. That is a genuine finding and it does not appear in the CVO's Article 1 fit assessment, which measures only demand. It does not rescue the volume problem — nothing in my remit does — but the CEO should know that the thing being considered for a kill is also the cleanest thing this company has designed.
2. **The regulatory case for killing it is nil.** Nothing in this document is a reason not to build Haunt. If it dies, it should die on the market evidence — Arc, Google, 164 ratings, 14% — and the decision record should say so, so that nobody in two years mistakes a demand judgment for a compliance judgment and reopens it on the wrong grounds.

### 8.4 Anti-drift clock (Constitution 5.2) — recorded, as the proposal asks

The proposal instructs: *"CGO to record the date and the reason."* Recorded.

> **Kill / proceed / park decision on `haunt` is due 2026-10-07.**
>
> **Reason.** Constitution 5.2 sets the decision "within 4 weeks of its research brief." `research/haunt-brief.md` was commissioned and delivered on 2026-09-09; four weeks from delivery is 2026-10-07. The idea brief's 2026-10-28 was computed from the brief's scheduled *due* date of 2026-09-30, not from the artifact. The Research Analyst raised the conflict unprompted and recommended against the more comfortable reading; the CVO accepted it. **I confirm the earlier date.** 5.2's own words are that the rule exists "to force building over perpetual planning," and 5.2 already forecloses the argument in the other direction — it provides that where a brief is *late*, "the decision clock starts at its due date regardless." A rule that refuses to let lateness extend the clock cannot coherently let earliness extend it. **Delivering early does not buy slack.** As of this note's date, **27 days remain**.

### 8.5 Open items I could not close

Recorded honestly rather than left to look closed. Under `pipeline/evidence-standard.md`, "we could not verify X" is a finding.

| # | Item | Who | Why it matters |
| --- | --- | --- | --- |
| 1 | **Google Maps Platform ToS §3.2.3 and Service Specific Terms §§A.3, 14.3, verbatim.** My fetches truncated twice; **the Skeptic reports the identical failure** at verification item #15. Three seats have now quoted these clauses and two of us could not retrieve them directly. | Skeptic / whoever revisits an online route | Moot on the MVP; load-bearing the moment an API returns |
| 2 | **ICO annual charge tier and amount.** Regulation 3 and the Schedule were not in the page I fetched; ico.org.uk returned HTTP 403 to my tool twice. | CFO, before publishing a price | A missing line on a published cost sheet (§3.3, C10) |
| 3 | **PECR reg. 6 exemptions as substituted 5 Feb 2026 by the Data (Use and Access) Act 2025.** Only paragraphs (1)–(2) were displayed. | Any 6.1 review, if one occurs | Low residual risk, recently rewritten (§3.6, C16) |
| 4 | **CDLA FAQ on the removal of the 1.0 attribution requirement** — read through a search rendering, not a clean fetch. | Skeptic | Supports §2.1's correction; the licence text itself is [E] and independently sufficient |
| 5 | **Foursquare Usage Guidelines scope.** The page I retrieved carrying the *"24-hour local-device caching"* rule is titled for the **Personalization APIs**. The EULA §2.1 points generally at *"our Usage Guidelines in the Developer Documentation,"* but that the same table governs the core Places API for a PAYG account is my inference, not the page's statement. | Skeptic, if any online route returns | It is the strongest single piece of evidence in §1.2 and I do not want its scope overstated |
| 6 | **App Store Connect privacy-policy-URL requirement** — [K], not retrieved. | Before submission | Trivial, but unverified (§3.3) |
| 7 | **Citation defect in `research/haunt-brief.md` §7.3** — the Apple "You or Your Application" caching quote is attributed to forum thread 114220, which does not contain it. | Research Analyst | Evidence-standard integrity, not substance (§1.1) |
| 8 | **DMCCA commencement and CMA penalty figures** — law-firm briefings, single underlying origin (DBT consultation response, 2 Apr 2026), not retrieved at source. | Only if Model 3 revives | Not load-bearing here (§4.5) |

### 8.6 Where I disagree with another seat, stated once and in writing

Per the universal charter clause. None of these changes a decision; all of them change a document.

1. **CTO, `feasibility-note.md` §2.2** records Overture Places under CDLA-Permissive-2.0 as *"Attribution required."* **The licence contains no attribution clause.** The real obligation is §2.1 (ship the licence text), and the real *attribution* obligation comes from the Apache-2.0 portion, which the note does not carry through to any design requirement. §2.1–2.2.
2. **CVO, `proposal.md`.** The corrected claim still asserts *"The app makes no network calls of its own"* while the architecture uploads to CloudKit. The correction fixed the crash-reporting exception and left the larger one. §6.2.
3. **CFO, `cost-sheet.md` §3.** The £83/year fixed running cost omits the ICO annual charge. Small, real, and on a document Article 3 makes public. §3.3.
4. **Research Analyst, `haunt-brief.md` §7.3.** A quotation is attributed to a source that does not contain it. Under the evidence standard this is the offence the standard treats most seriously, and I record it even though it changes nothing — because a standard enforced only when the conclusion is wrong is not a standard. §1.1.

### 8.7 Note on Skeptic objection O7

The Skeptic records that *"the CGO has had no part in a gate the Constitution makes it responsible for"* and asks for confirmation that the CGO step exists before the CEO reads the pack. **This document is the regulatory half of that step**; the review-pack compilation under Constitution 5.5 is a separate commission and has not yet run. The other half of O7 — that no UX seat has assessed the product — I **concur with in full** and have made a condition of my non-block (§5.3). O7 is dissolved as to the CGO limb and **live as to the UX limb.**

---

## Sources retrieved this session

Grouped as the evidence standard asks, with independence noted.

**Licences and data terms**
- [CDLA-Permissive-2.0, cdla.dev](https://cdla.dev/permissive-2-0/) and [SPDX licence list](https://spdx.org/licenses/CDLA-Permissive-2.0.html) — *two independent origins for the operative §2.1 text*
- [CDLA FAQ](https://cdla.dev/faq-resources/faq/) — *read via search rendering; flagged*
- [Apache License 2.0, §4](https://www.apache.org/licenses/LICENSE-2.0)
- [Foursquare OS Places NOTICE](https://opensource.foursquare.com/places-notice-txt/)
- [Overture Maps — attribution and licensing](https://docs.overturemaps.org/attribution/) — theme/licence boundary confirmed
- [Foursquare — Usage Guidelines](https://docs.foursquare.com/developer/reference/usage-guidelines-personalization-apis) — *"24-hour local-device caching"*; **scope flagged, open item 5**
- [Foursquare — API Licence Agreement](https://foursquare.com/legal/terms/apilicenseagreement/)
- [Google — Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies)
- [Apple Developer Forums thread 807656](https://developer.apple.com/forums/thread/807656) — DTS declines to interpret Schedule 6 §2.5
- [Apple Developer Forums thread 114220](https://developer.apple.com/forums/thread/114220) — *retrieved and found not to contain the quote attributed to it*

**Data protection**
- [UK GDPR Article 2](https://www.legislation.gov.uk/eur/2016/679/article/2) · [Article 4](https://www.legislation.gov.uk/eur/2016/679/article/4) · [Article 35](https://www.legislation.gov.uk/eur/2016/679/article/35)
- [Data Protection (Charges and Information) Regulations 2018, reg. 2](https://www.legislation.gov.uk/uksi/2018/480/regulation/2/made)
- [PECR 2003, reg. 6 (as substituted 5 Feb 2026)](https://www.legislation.gov.uk/uksi/2003/2426/regulation/6)

**Consumer law**
- [Apple Media Services Terms and Conditions (UK)](https://www.apple.com/legal/internet-services/itunes/uk/terms.html) — merchant of record; 14-day right and its waiver
- [Consumer Contracts Regulations 2013, reg. 37](https://www.legislation.gov.uk/uksi/2013/3134/regulation/37)
- [Consumer Rights Act 2015, s.36](https://www.legislation.gov.uk/ukpga/2015/15/section/36)
- [DMCCA 2024, s.226](https://www.legislation.gov.uk/ukpga/2024/13/section/226) · [s.227](https://www.legislation.gov.uk/ukpga/2024/13/section/227)
- [Hill Dickinson](https://www.hilldickinson.com/our-view/articles/digital-markets-competition-and-consumers-act-2024-new-consumer-law-protections-now-in-force/) · [Taylor Wessing](https://www.taylorwessing.com/en/insights-and-events/insights/2026/04/subscription-contracts) · [Hogan Lovells](https://www.hoganlovells.com/en/publications/uk-subscription-law-shakeup-new-rules-pushed-to-autumn-2026) — *secondary, single underlying origin, flagged*

**Accessibility**
- [W3C — WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [W3C — WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/)
- [Equality Act 2010, s.29](https://www.legislation.gov.uk/ukpga/2010/15/section/29)
- [Directive (EU) 2019/882 (European Accessibility Act), EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng)

**Platform rules**
- [Apple — App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/)

**Relied on from other seats' retrievals, not re-retrieved by me** (flagged where load-bearing): Google Maps Platform ToS §3.2.3 and Service Specific Terms §§A.3/14.3 (CTO §2.1, Research Analyst §7.1 — see open item 1); Overture Places guide quality caveat; Apple iCloud data security overview; Apple crash-report documentation; Arc Timeline 4 App Privacy declaration (Skeptic verification #1).

---

*Prepared by the Chief Governance Officer under Constitution Articles 4, 5.6 and 6.1. Agent reviews prepare and flag; they do not certify. The decision is the CEO's (5.4).*

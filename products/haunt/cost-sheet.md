# Cost sheet — Haunt — discovery model (pre-gate)

> **⚠ SUPERSEDED IN LARGE PART, 2026-09-17 — see `products/haunt/window-conversion-model.md`.**
>
> This sheet was written on **450 build hours**, iOS-only, with a metered places API. All three premises are now wrong: the CTO's measured figure is **1,160–1,500 hours** for the two-platform React Native build the CEO directed, the architecture is offline so there is no API meter, and variable support was modelled on a basis since reconciled with the CTO.
>
> **Sections 1, 3–10, 12 and 14 are superseded.** The re-derivation owed under Condition 1 of `decisions/2026-09-16-haunt-gate.md` is complete and lives in the conversion model: three-year cost **£75,627**, and break-even at £14.99 of **~10,564 sales** rather than the ~2,400–2,700 this sheet's figures produced.
>
> **Objection O10 is located and it is not a table.** Every §5 table reproduces to the penny. The failure is a single prose sentence — *"adding £4,000 of build moves £14.63 to about £26"* — where the correct answer is **£15.99**; £26 would require roughly £33,600. One unchecked sentence beneath correct arithmetic, which is precisely what Condition 6 exists to catch.
>
> **O11** (two incompatible support bases) is reconciled on the CTO's basis — the two figures add, neither replaces the other. **O12** is relabelled: 16.5% is a **justified deviation of 3.5pp below** the ~20% target, recorded with its direction, per Constitution 2.1 as amended in v1.2.
>
> Preserved unaltered so the errors remain inspectable. **No figure here is a price.**


**Seat:** Chief Financial Officer · **Date:** 2026-09-09 · **Commissioned by:** CVO, 2026-09-09
**Status:** **Discovery cost model, not a published cost sheet.** Nothing here is a price. Under Constitution 5.4 pricing is the CEO's decision; under 2.1 a published cost sheet accompanies a real product, and Haunt has no requirements document, no CTO feasibility note and no research brief yet. This document exists so the gate on **2026-10-07** can argue about numbers instead of adjectives. *[Date corrected by CVO 2026-09-10: this document was written when the anti-drift deadline was believed to be 2026-10-28. Constitution 5.2 counts four weeks from the research brief, which was delivered 2026-09-09. No figure in this document depends on the date.]*

**Template note:** `pipeline/templates/cost-sheet.md` assumes a monthly hosting-shaped cost table. Haunt has no hosting and its dominant cost is one-off build labour, so the template's sections are preserved below but the itemisation is restructured into fixed / per-user / per-lookup. This deviation is stated rather than made silently.

---

## 0. Executive answer, before the arithmetic

1. **The premise is confirmed with one large exception.** Haunt's fixed infrastructure cost is genuinely near zero — **£73/year** for the Apple Developer Program plus a domain. There is no hosting line and no database line, and that is a structural property, not a discipline. Constitution 1.5 is satisfied by the architecture. [I, from [E] fee data below]
2. **The exception is the places API, and it is not small.** At the retrieved 2026 rate for Google's Nearby Search (Pro), a *typical* user costs **£11.05/year** and a *heavy* user costs **£44.22/year** in lookups alone. That is not "almost nothing"; it is larger than every other running cost combined, it grows with use, and Candour does not set the price. [I, from [E] pricing below]
3. **Which provider is chosen changes the viable business model, not just the margin.** The same product costs £0.00, £1.73, £5.18 or £11.05 per typical user per year depending on the venue-data source. The floor price of a one-off purchase moves from **£6.23 to £62.42** on that choice alone. This is the single most consequential number in the discovery phase and it belongs to the CTO note, not to marketing.
4. **A subscription can be justified under 2.1 — and the honest price is about £6–£11 a year.** See §7. I make the case rather than assuming it, and then explain why making the case is not the same as recommending it.
5. **A compliant free-tier cap exists, and it is not an entry cap.** See §8. Any cap on *reading entries the user already wrote* is an Article 4 breach and I would block a launch that shipped one.
6. **Every model requires four-figure sales volumes to cover benchmarked labour** — 1,155 to 6,941 sales over three years depending on price, iOS-only; roughly double for two platforms (§6). Against the idea brief's own objection 6 (no acquisition channel, no sharing surface), that is the number the gate should stare at.

---

## 1. The labour-treatment question, answered explicitly

`research/scouts/scout-2026-09-01-skeptic-cull.md` §4 costs build labour as a **year-one operating cost**. `research/scouts/scout-2026-09-01.md` §6 disputes this and argues build labour is **capital, amortised over product life**. The CVO recorded it as CEO decision 2 and assigned preparation to this seat. It is still open.

**The treatment used in this document, and why:**

> Build labour is **capital, amortised straight-line over the product's declared supported life**, which for Haunt I set at **3 years**. Ongoing maintenance and support labour are **operating costs**, costed separately and never folded into the build figure.

Three conditions make that treatment honest rather than convenient, and I recommend the CEO adopt them together or reject the treatment entirely:

- **(a) The amortisation period must equal a published support commitment.** Candour may amortise over three years only if it promises three years of support. Amortising over a life it has not promised is the Article 9 loophole "inflating costs to raise the allowable price" run in reverse — deflating cost to justify a low price it cannot sustain.
- **(b) Unamortised build must be written off publicly on discontinuation.** Constitution 7.2 already requires a closing cost sheet. The remaining capital goes in it, visibly.
- **(c) The period, once published, may not be lengthened.** Lengthening it mid-life lowers published cost, which under 2.3.3.1 ratchets the price down permanently — a one-way move that looks generous and is actually a way of hiding an overrun.

**Why I side with the CVO, against the Skeptic's arithmetic:** a build is consumed by every customer over the product's life, not by the first year's customers. Charging year-one buyers the whole build makes the published cost a function of *when someone bought*, which breaks 2.1's promise that "each product's customers get that product's honest number."

**Why it matters much less here than it did for candidate F:** for a **one-off purchase**, the two treatments converge, because the full build must be recovered from the buying cohort regardless of how it is booked. §5 therefore models the one-off case as a **three-year total cost**, which is treatment-neutral. The treatment only bites on the subscription model (§7), where it moves the honest annual price from £19.00 to £10.69 at 1,000 subscribers.

**Both figures are shown throughout.** This is a Constitution 5.4 / Article 9 definitional decision. If adopted it changes the meaning of a defined term ("Cost") and therefore needs a public amendment under Article 11, not a footnote in this file.

---

## 2. Retrieved inputs

Every figure below was retrieved on **2026-09-09**. Nothing in this section is from memory.

### 2.1 Store commission and fees

| Item | Figure | Tag |
|---|---|---|
| Apple App Store Small Business Program commission | **15%** on paid apps and IAP, for developers with **up to $1m proceeds** in the prior calendar year and developers new to the App Store | [E] [source](https://developer.apple.com/app-store/small-business-program/) |
| Apple standard commission (above threshold) | 30% — "If a participating developer surpasses the 1 million USD threshold in the current calendar year, the standard commission rate will apply to future sales" | [E] [source](https://developer.apple.com/app-store/small-business-program/) |
| Apple Developer Program membership | **$99/year** | [E] [source](https://developer.apple.com/programs/) |
| Google Play developer registration | **$25 one-time** | [E] [source](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en) |
| Google Play service fee — EEA/UK/US, effective 30 June 2026, **new installs** | **10% service fee + 5% billing fee** on the first $1m USD annual earnings | [E] [source](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) |
| Google Play — global 15% tier (markets not yet on the new card) | 15% on first $1m USD annually, 30% above | [E] [source](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) |
| UK standard VAT rate | **20%** | [E] [source](https://www.gov.uk/vat-rates) |
| GBP/USD spot, 9 Sept 2026 | **1.3547** | [E] [source](https://tradingeconomics.com/united-kingdom/currency) |

**Modelling decision:** both stores land on an effective **15%** for a developer at Candour's scale, so a single 15% figure is used throughout. It is a coincidence of two different fee architectures, not one rule, and it will drift.

**Not retrieved — flagged:** that Apple acts as merchant of record and collects/remits UK VAT. Apple's own help confirms it collects and remits for **Mexico** and **Taiwan** [E, [source](https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information/)] but the page did not confirm the UK/EU position. The UK merchant-of-record treatment is **[K, high confidence, unverified]**. It affects the shelf price by 20% and must be verified before any price is published. Ex-VAT and VAT-inclusive figures are shown separately throughout so the reader can see exactly which number the assumption moves.

### 2.2 Places / venue lookup — retrieved prices

| Provider / SKU | Price per 1,000 calls | Free monthly allowance | Tag |
|---|---|---|---|
| Google **Nearby Search (Pro)** | **$32.00** | 5,000 | [E] [source](https://developers.google.com/maps/billing-and-pricing/pricing) |
| Google Nearby Search (Enterprise) | $35.00 | 1,000 | [E] [same](https://developers.google.com/maps/billing-and-pricing/pricing) |
| Google Text Search (Pro) | $32.00 | 5,000 | [E] [same](https://developers.google.com/maps/billing-and-pricing/pricing) |
| Google **Place Details (Essentials)** | $5.00 | 10,000 | [E] [same](https://developers.google.com/maps/billing-and-pricing/pricing) |
| Google Place Details (Pro) | $17.00 | 5,000 | [E] [same](https://developers.google.com/maps/billing-and-pricing/pricing) |
| **Foursquare Places** (from 1 June 2026) | $0.00 to 500 calls; **$15.00** 501–100k; $12.00 100k–500k; $9.00 500k–1m | 500 Pro calls | [E] [source](https://docs.foursquare.com/developer/reference/upcoming-changes) |
| **Mapbox Search Box** | **$1.00** (introductory, 50k–500k band) | 50,000 | [E] [source](https://www.mapbox.com/pricing) |
| Mapbox Temporary Geocoding | $0.75 | 100,000 | [E] [same](https://www.mapbox.com/pricing) |
| **Mapbox Permanent Geocoding** | **$5.00** | **none** | [E] [same](https://www.mapbox.com/pricing) |
| Geoapify | Free 3,000 credits/day; API 10 $59/mo (10k/day); API 25 $109/mo; API 50 $179/mo | 3,000/day | [E] [source](https://www.geoapify.com/pricing/) |
| LocationIQ | Free 5,000/day (2 req/s); Developer $100/mo (25k/day); Startup $200/mo (60k/day) | 5,000/day | [E] [source](https://locationiq.com/pricing) |
| OSM public Nominatim | £0, but **"an absolute maximum of 1 request per second"** and "Applications and services whose primary function is related to geocoding must run their own service" | n/a | [E] [source](https://operations.osmfoundation.org/policies/nominatim/) |
| **Overture Maps places** (bundled offline dataset) | **£0** — open data, CDLA Permissive 2.0 / Apache 2.0, ~74m places (Aug 2026) | n/a | [E] [source](https://docs.overturemaps.org/guides/places/) |

### 2.3 The storage terms, which are a cost fact and not only a legal one

This is the finding I would put in front of the CEO first, because it changes the arithmetic rather than decorating it.

- **Google:** "You must not pre-fetch, cache, or store Places API content beyond the allowed exceptions." The **place ID** is "exempt from the caching restrictions… You can therefore store place ID values indefinitely." [E] [policies](https://developers.google.com/maps/documentation/places/web-service/policies), [place ID](https://developers.google.com/maps/documentation/places/web-service/place-id)
- **Mapbox Search Box:** "all data returned by the Search Box API endpoints is only available for temporary use." [E] [source](https://docs.mapbox.com/api/search/search-box/)
- **Mapbox Geocoding:** "Temporary results are not allowed to be cached, while Permanent results are allowed to be cached and stored indefinitely" — permanent storage requires a card on file or an enterprise contract, and is the **$5.00/1,000** SKU with no free tier. [E] [source](https://docs.mapbox.com/api/search/geocoding/)
- **Foursquare:** the licence requires compliance with "the Places API caching and query rate limitations applicable to your Account-type" and forbids making Places Data "available to third parties in bulk" or systematically querying "to obtain all or substantially all Places Data." [E] [source](https://foursquare.com/legal/terms/apilicenseagreement/)
- **LocationIQ:** free accounts may cache "for upto 48 hours"; paid customers may cache "for as long as you're a customer." [E] [source](https://locationiq.com/pricing)
- **Overture:** open data under CDLA Permissive 2.0 / Apache 2.0 — no caching restriction at all. The documentation warns it is "known to contain duplicates, a high junk rate, and low property completeness." [E] [source](https://docs.overturemaps.org/guides/places/)

**Could not verify this session:** the specific Foursquare Pay-As-You-Go caching allowance (secondary sources say `fsq_place_id`, photo IDs and address IDs indefinitely and nothing else, but I did not retrieve Foursquare's primary usage guidelines and I am not repeating it as evidence). This is already commission item **(f)** on the research brief; it should be treated as load-bearing.

**Why this is a cost fact.** Haunt's whole proposition is a permanent local journal that says "The Eagle, Cambridge" next to a note the user wrote in 2027. Under Google's, Mapbox Search Box's and (probably) Foursquare's terms, that venue **name** may not be stored indefinitely — only the opaque ID may. If names must be re-resolved on display rather than stored once on capture, the API bill stops scaling with *visits written* and starts scaling with *the journal being read*, and grows with the age of the timeline. That converts a bounded per-user cost into an unbounded one.

**Three responses, all with prices attached:**

| Response | Per-lookup cost | Storage lawful? | Consequence |
|---|---|---|---|
| Mapbox **Permanent** Geocoding | $5.00/1,000 | Yes, explicitly indefinite [E] | 5× the Search Box rate; no free tier; verify POI/venue coverage is adequate (CTO) |
| Bundled **Overture** dataset on device | $0 | Yes, open licence [E] | Zero-network variant; higher build cost; app size; "high junk rate" per Overture's own docs |
| Store IDs only, re-resolve names on read | $32/1,000 (Google Pro) | Yes | **Unbounded per-user cost.** Structurally incompatible with a one-off purchase |

**CFO position (a recommendation, not a block at this stage):** the third response should not survive discovery. A lifetime unlock or one-off purchase funded by a per-read API meter is a liability without a matching asset. If the CEO wants the one-off model the idea brief leans toward, the venue data must come from **Mapbox Permanent Geocoding or a bundled open dataset**. The "zero network, offline venue dataset" variant the idea brief treats as a fallback is, on these numbers, a **precondition** for the pricing model the CEO prefers — not a retreat from it.

### 2.4 Labour benchmark

| Item | Figure | Tag |
|---|---|---|
| Median UK full-time software developer salary | **£56,914** | [E, **single source, secondary**] [payprecision.co.uk](https://payprecision.co.uk/salaries/software-developer/), citing ONS ASHE Table 14, 2025 provisional, reference period April 2025 |
| Same source, 25th / 75th percentile | £42,289 / £75,794 | [E, same single source] |
| Working hours basis | 1,740 h/yr (37.5 h × 46.4 weeks, after 5.6 weeks statutory leave) | [J] — stated so it can be argued with |
| **Derived hourly benchmark** | **£32.71/hour** | arithmetic |

**Flag, repeating the Skeptic's own flag from 2026-09-01:** the ONS table itself was **not** retrieved — only a secondary page citing it. Constitution 2.2 makes this benchmark the anchor of every published number Candour produces. It should be upgraded to a primary ONS citation before any cost sheet is published, and I am not going to keep re-flagging it in later documents; it needs fixing once.

**A second definitional item for the CEO:** £56,914 is a *salary*, not an employment cost. A real employer also pays employer's NI and pension, adding roughly 15–18% [K, medium confidence, not retrieved]. Constitution 2.2 names "the median UK software developer salary" as the default benchmark, so I have used the bare salary. If the CEO prefers full employment cost, every figure in this document rises by that percentage. I do not have a strong view; I have a strong view that it should be decided once, in public, and not per product.

---

## 3. Effort assumptions — the weakest part of this model

**There is no CTO feasibility note yet.** These are my estimates, not engineering's, and they are the input most likely to be wrong.

| Item | Hours | Cost @ £32.71 | Tag |
|---|---|---|---|
| Build — iOS only (visit clustering, confirm flow, local store, export, encrypted user-cloud backup, venue lookup, journal UI) | 450 (≈12 weeks FT) | **£14,719** | [J] |
| Build — iOS + Android | 810 (≈22 weeks FT) | **£26,494** | [J] |
| Annual maintenance — iOS only (OS releases, permission-model changes, privacy manifests, SDK bumps, store compliance) | 100 /yr | **£3,271/yr** | [J] |
| Annual maintenance — both platforms | 180 /yr | **£5,888/yr** | [J] |
| Support — paying user | 5% contact rate/yr × 45 min | **£1.23/user/yr** | [J] |
| Support — free-tier user | 2% contact rate/yr × 30 min | **£0.33/user/yr** | [J] |

The 45-minute support case is deliberately long. The idea brief's objection 5 is correct: with no telemetry and no server, every support case starts from a user's prose description of a background-location bug that Candour cannot reproduce and cannot inspect. That is the honest cost of the pitch, and it is priced here rather than admired.

**The Android decision is a pricing decision.** Shipping both platforms adds £11,775 of build and £2,617/year of maintenance, and roughly **doubles the sales volume needed to break even** (§6). The idea brief calls this a "CTO/CFO question". My half of the answer: iOS-only at MVP, and Android added only after the iOS cohort demonstrates the sales volume in §6 is reachable. Committing to both up front doubles the bet on the one thing nobody has evidence for — that anyone will buy it.

### Usage assumptions

| Profile | Confirmed visits/month | Lookup calls/month (at 1.3 calls/visit) | Tag |
|---|---|---|---|
| Light | 10 | 13 | [J] |
| **Typical** | 30 (≈1/day) | **39** | [J] |
| **Heavy** | 120 (4/day) | **156** | [J] |

1.3 calls per visit allows for one automatic nearby-search plus occasional manual re-search when the user corrects the guess. These are guesses. They should be replaced with instrumented figures from a TestFlight build before a price is published — which is itself awkward, because instrumenting them requires telemetry the product promises not to have.

---

## 4. Itemised costs

### 4.1 Fixed, independent of users (iOS-only)

| Item | Provider | Cost | Notes |
|---|---|---|---|
| Hosting | — | **£0.00** | No server exists. This is the point of the product. |
| Database | — | **£0.00** | All state on the user's device. |
| Apple Developer Program | Apple | **£73.08/yr** | $99 @ 1.3547 [E] |
| Google Play registration (if Android) | Google | £18.45 one-off | $25 [E] |
| Domain + static support/landing page | Cloudflare Registrar (at-cost, no markup [E](https://www.cloudflare.com/products/registrar/)) + free static tier | **~£10/yr** [J] | .com price **not retrieved this session**; immaterial at <0.1% of total cost, but stated rather than hidden |
| Crash/analytics tooling | — | **£0.00** | Deliberately absent (Article 4 minimum data). The cost reappears as support labour above. |
| **Total fixed recurring, iOS-only** | | **~£83/yr** | |

That £83 figure is the answer to the commissioning question. **Yes — the non-labour, non-API running cost is genuinely almost nothing, and it is a structural property of the architecture rather than a discipline that could slip.** Haunt is the first candidate on the backlog where Constitution 1.5 is satisfied by design.

### 4.2 Per-user, per-year — the places API bill

Cost per user per year, GBP, at the retrieved rates:

| Profile | Overture offline | Mapbox Permanent | Foursquare Pro | Google Nearby Pro |
|---|---|---|---|---|
| Light (13 calls/mo) | £0.00 | £0.58 | £1.73 | £3.68 |
| **Typical (39 calls/mo)** | **£0.00** | **£1.73** | **£5.18** | **£11.05** |
| **Heavy (156 calls/mo)** | **£0.00** | **£6.91** | **£20.73** | **£44.22** |

**Where the free allowance runs out** — the number of typical users a free tier covers before the meter starts:

| Provider | Free calls/month | Typical users covered | Storage lawful? |
|---|---|---|---|
| Mapbox Search Box | 50,000 | **~1,282** | No — temporary use only [E] |
| Google Nearby Search Pro | 5,000 | **~128** | Place ID only [E] |
| Foursquare Pro | 500 | **~12** | Unverified |
| Mapbox Permanent Geocoding | 0 | **0** | Yes [E] |
| Overture offline | n/a | unlimited | Yes [E] |

Read that table honestly: **the only provider whose storage terms match the product is the only one with no free tier at all.** The API bill on Mapbox Permanent starts at user number one. It is small — £1.73/user/yr typical — but it is never zero, which matters for a one-off purchase.

**The heavy user is the load-bearing case.** On Google Nearby Pro a heavy user costs **£44.22/year, £132.66 over three years**. A £14.99 one-off purchase from that user is exhausted in **under three months**. There is no throttle Candour controls, no server-side rate limit that isn't also a broken feature, and no way to identify heavy users before they buy. Under Article 4 ("no hidden fees, no drip pricing") Candour cannot bill them later. This is a genuine adverse-selection problem: the people who love the product most are the ones who lose money, and they are also the ones most likely to buy.

---

## 5. Model 1 — Plain one-off purchase

Three-year total-cost basis (treatment-neutral per §1). iOS-only. Three-year fixed cost = build £14,719 + 3 × maintenance £3,271 + 3 × Apple £73 + domain = **£24,781**.

**Pricing arithmetic used throughout, stated so it can be checked:**
- Store commission is a **cost of sale passed through at zero markup**, not a cost that earns margin: `ex-VAT price = (other costs × 1.20) ÷ 0.85`.
- Shelf price shown to a UK customer adds 20% VAT: `shelf = ex-VAT × 1.20`.
- Effective margin over *total published cost including commission* is therefore **16.5%**, comfortably inside 2.1's ~20% target and far below the 30% cap. The alternative treatment — taking 20% on the commission too — yields 20.0% and a ~4% higher price. **I recommend the pass-through version**, because it is the lower price and because charging the customer a margin on Apple's fee is not something I could defend to a sceptical reader. This is a definitional choice and it belongs with the CEO alongside the labour question.

### Shelf price (inc. VAT) by venue-data source and cohort size

| Buyers (3 yrs) | Overture offline | Mapbox Permanent | Foursquare Pro | Google Nearby Pro |
|---|---|---|---|---|
| 250 | £174.16 | £182.94 | £200.50 | £230.35 |
| 1,000 | £48.22 | £56.99 | £74.55 | £104.40 |
| 2,500 | £23.03 | £31.81 | £49.36 | £79.21 |
| 5,000 | £14.63 | £23.41 | £40.97 | £70.82 |
| 10,000 | £10.43 | £19.21 | £36.77 | £66.62 |
| 25,000 | £7.91 | £16.69 | £34.25 | £64.10 |
| **Floor (infinite users)** | **£6.23** | **£15.01** | **£32.57** | **£62.42** |

**The floor row is the finding.** The variable per-user cost does not go away with scale, so each column has a hard price floor no matter how successful Haunt is:

- **Google Places: a one-off purchase can never honestly be sold below about £62.** That is not a market price for a journal app. Google Places and a one-off purchase are mutually exclusive under Constitution 2.1. Stated flatly so nobody has to infer it.
- **Foursquare: floor ~£33.** Also unlikely to be a market price.
- **Mapbox Permanent: floor ~£15**, reaching ~£23 at 5,000 buyers. Plausible.
- **Overture offline: floor ~£6**, reaching ~£15 at 5,000 buyers. Comfortable — and note that build cost would rise by an amount the CTO has not yet estimated (dataset preparation, on-device index, update pipeline, app size). Adding £4,000 of build to that column moves the 5,000-buyer price from £14.63 to about £26.

**Deviation from the 20% target: none required.** The honest price is achievable in two of four columns. The problem is not margin; it is volume (§6).

---

## 6. Volume required to cover benchmarked labour

The CEO asked for this directly. Labour only — excluding API, store fees and VAT. Net proceeds per sale = `shelf ÷ 1.20 × 0.85` = **70.83%** of shelf.

Three-year benchmarked labour: **iOS-only £24,532** (build £14,719 + 3 × £3,271). **Both platforms £44,157** (build £26,494 + 3 × £5,888).

| Shelf price (inc VAT) | Net per sale | Sales to cover labour, iOS-only | Sales to cover labour, both platforms |
|---|---|---|---|
| £4.99 | £3.53 | **6,941** | 12,493 |
| £9.99 | £7.08 | **3,467** | 6,240 |
| £14.99 | £10.62 | **2,310** | 4,159 |
| £19.99 | £14.16 | **1,733** | 3,119 |
| £24.99 | £17.70 | **1,386** | 2,495 |
| £29.99 | £21.24 | **1,155** | 2,079 |

**These figures are the honest centre of this document.** They say: Haunt must sell **roughly 1,200–3,500 copies over three years**, at a price in the £10–£30 band, on iOS alone, to pay its founder the ONS median for the hours spent. Two platforms roughly doubles it.

The idea brief's own objection 6 states there is no acquisition channel, no sharing surface at MVP, and no organic loop. The Skeptic's 2026-09-01 memo went further and argued the binding constraint on this company is reach, not ideas. **I am not competent to say whether 2,000 sales is reachable — that is the research brief's job — but I am competent to say that no pricing structure in this document rescues Haunt if it isn't.** The pricing question is downstream of the reach question, and the gate should sequence them that way.

---

## 7. Model 3 — Free tier + subscription: can it be justified under 2.1?

The commissioning note asked me to make the case or refute it, not to assume it. Here is the case, then the refutation, then my answer.

### The case *for*

Article 2.1 prices at cost + ~20%, and a recurring price needs a recurring cost to be 20% of. **Haunt has genuine recurring costs**, and they are not trivial:

1. **The places API bill recurs, per user, forever, and is not under Candour's control.** [E, §2.2] It is the archetype of a cost that justifies a recurring price. A user who journals for five years consumes five years of lookups.
2. **Maintenance labour recurs.** iOS and Android ship annually and break background-location apps; store compliance requirements change. £3,271/year, iOS-only. [J]
3. **Support labour recurs**, and is expensive per case precisely because the product has no telemetry. [J]
4. **The Apple Developer Program fee recurs.** £73/year. [E]

So the answer to "is there something to take 20% of?" is **yes**. A subscription is not structurally forbidden here, and the idea brief's objection 9 slightly overstates the case when it says a product with no server has "almost no recurring cost." It has no *infrastructure* recurring cost. It has a real *usage* recurring cost, and it is the one cost that grows.

Indeed there is a positive argument that a subscription is the **more honest** structure for the metered-API architecture: a recurring cost matched by a recurring payment is exactly aligned, whereas a one-off payment against a perpetual per-user liability is a promise Candour cannot fund (§2.3, §4.2).

### The honest number

Steady-state annual cost per subscriber, iOS-only, at typical usage, and the resulting shelf price at 20% margin:

| Subscribers | Overture offline | Mapbox Permanent | Foursquare Pro | Google Nearby Pro |
|---|---|---|---|---|
| **Years 1–3 (build amortised)** | | | | |
| 250 | £58.05/yr | £60.98/yr | £66.83/yr | £76.78/yr |
| 1,000 | £16.07/yr | **£19.00/yr** | £24.85/yr | £34.80/yr |
| 2,500 | £7.68/yr | £10.60/yr | £16.45/yr | £26.40/yr |
| 5,000 | £4.88/yr | £7.80/yr | £13.66/yr | £23.61/yr |
| **Year 4+ (build fully recovered)** | | | | |
| 1,000 | £7.76/yr | **£10.69/yr** | £16.54/yr | £26.49/yr |
| 5,000 | £3.21/yr | £6.14/yr | £11.99/yr | £21.94/yr |

(Shelf prices, inc. VAT, at cost + 20% with commission passed through.)

**So: an honest Haunt subscription is about £10.69 a year — 89p a month — at 1,000 subscribers on Mapbox Permanent, falling to about £6.14 at 5,000.** On an offline Overture dataset it falls to **£3.21–£7.76 a year**, i.e. under 65p a month.

Two features of that number deserve emphasis:

- **It ratchets down and cannot come back up.** Once the build is amortised, published cost drops, and Constitution 2.3.3.1 makes price reductions for existing customers the first call on surplus. A Haunt subscription is contractually a *declining* subscription. That is a genuinely unusual and rather admirable thing to publish, and it is also a business that gets worse every year by construction.
- **The one column where a subscription looks like a normal consumer subscription — Google Nearby Pro at £21.94–£34.80/yr — gets there entirely by passing through an expensive API choice.** Charging users £2.90/month because Candour picked the most expensive venue provider is, under Article 9's first loophole ("inflating costs to raise the allowable price"), precisely the thing the cost sheet exists to expose. I would not sign that off without the CTO demonstrating that the cheaper providers are functionally inadequate.

### The refutation, and my answer

**A subscription is justifiable under 2.1. It is not viable as a business at the price 2.1 permits.** Both halves are true and neither cancels the other.

At £6–£19 per year Candour would be running annual billing, renewal notices, cancellation flows, dunning, churn measurement and involuntary-churn recovery — the entire operational apparatus of a subscription business — against a sum that, at 1,000 subscribers on the honest number, is roughly £10,690 of gross revenue a year against £19,000 of benchmarked cost in years 1–3. It does not clear its own labour until roughly 2,000–2,500 subscribers, and then it is required by 2.3.3.1 to cut the price.

There is also a plain Article 1.3 problem. The pitch is "your data never leaves your phone." A recurring charge for a product that runs entirely on hardware the customer already owns will read to a sceptical customer as rent, and the cost sheet's honest defence — "the venue lookups genuinely cost us 89p a month" — is *true* but invites the obvious reply: then remove the venue lookups.

**CFO recommendation:**

> **The one-off lifetime unlock is the honest structure for Haunt, conditional on the venue data being unmetered or permanently-storable.** A subscription is defensible only in the metered-API architecture, and in that architecture the honest price is so low that the subscription is not worth operating. Choose the architecture and the pricing shape follows; do not choose the pricing shape and then reverse-engineer an architecture that justifies it — that is the Article 9 loophole running in the direction it usually runs.

**And the corollary the CEO should not miss:** a lifetime unlock is only honest if Candour can actually serve that user for life. On Google Nearby Pro it cannot (§4.2 — the heavy user exhausts a £14.99 payment in three months). **A lifetime unlock plus a metered per-lookup API is the one combination this cost sheet says Candour must not ship.** If both are chosen anyway, I would expect to block the launch under my charter's "unpriced or uncosted launches" power, and the thing that would lift the block is either an unmetered venue source or a plainly-stated, pre-purchase fair-use cap on automatic lookups.

---

## 8. Model 2 — Free tier + lifetime unlock, and the Article 4 cap question

### 8.1 What a free tier actually costs

A free user consumes API calls and support labour and returns nothing. Paying users must carry them. Three-year cost per free user, and the resulting shelf price for the unlock:

Free-tier design modelled: **5 automatic venue lookups per month**, unlimited manual entry, unlimited history, unlimited export.

| Free:paid ratio | Paid users | Overture offline | Mapbox Permanent | Foursquare Pro | Google Nearby Pro |
|---|---|---|---|---|---|
| 4:1 (20% conversion) | 1,000 | £54.87 | £68.15 | £94.71 | £139.86 |
| 4:1 | 5,000 | £21.28 | £34.56 | £61.12 | £106.28 |
| 9:1 (10% conversion) | 1,000 | £63.18 | £82.09 | £119.90 | £184.19 |
| 9:1 | 5,000 | £29.59 | £48.50 | £86.32 | £150.61 |
| 19:1 (5% conversion) | 1,000 | £79.80 | £109.96 | £170.29 | £272.85 |
| 19:1 | 5,000 | £46.22 | £76.38 | £136.71 | £239.26 |

Compare against the no-free-tier column in §5 (£14.63–£23.41 at 5,000 buyers on the two viable providers). **A free tier at a realistic 5% conversion rate roughly triples the honest unlock price.** At 19:1 on Mapbox Permanent the honest price is £76.38 — worse than the pure one-off at any volume.

This is the least intuitive result in the document and it is worth stating plainly: **because Haunt has no server, its free tier has no marginal-cost-of-zero to hide behind.** The classic SaaS logic — free users cost fractions of a penny, so give it away — does not apply, because Haunt's marginal costs are a metered third-party API and a human answering email. Both are real money per user.

**The free tier is only affordable if it does not consume the metered API.** That is not a constraint I invented to make a point; it falls straight out of the table. And it happens to point at exactly the design that also solves the Article 4 problem.

> **⚠ CORRECTED 2026-09-16 — see Correction C1 in `decisions/2026-09-16-haunt-gate.md`.** The reasoning in this section is **conceded and superseded**. Its alignment test — "the paywall sits precisely on the cost" — is a **heuristic of this seat, not a constitutional requirement** (C1.4): Article 2.1 constrains the price *level*, not where a paywall sits. Its "costs nothing per entry" reasoning uses marginal rather than defined Cost (C1.2). And the launch block reserved here was on **Article 4 grounds, outside the CFO charter**, which covers unpriced or uncosted launches (C1.3). The text below is preserved unaltered so the error remains inspectable.

> **⚠ AMENDED 2026-09-17 — see Correction C2.4.** The original banner ended "do not cite it." **That was too broad and buried a correct finding.** One row of this section **stands and is still authority**: *"Cap tightened for existing free users after launch | Retroactive; Article 1.2."* It was right when written, it is right now, and it is the direct ancestor of Condition 8.2 — retroactive tightening engages Article 1.2's lock-in and information-asymmetry limbs where a disclosed cap does not, because the distinguishing variable is **sequence, not severity**. A blanket retraction that swallows a surviving protection is the quiet kind of loss Article 9 is written against. **Everything else in this section is superseded; that row is not.**

### 8.2 Can a free-tier cap be designed without breaching Article 4?

**Yes. One design is compliant, and it is not an entry cap.**

The relevant text is Article 4: "Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge and with no penalty" — plus "no dark patterns" and Article 1.2's prohibition on profiting from lock-in.

**A sharpening specific to Haunt, which the CEO should hold on to:** because Haunt stores everything on the user's own device, any cap on *reading existing entries* means Candour's software is refusing to display a file that sits on the customer's own hardware, that the customer wrote, that Candour has never seen and does not hold. That is not a paywall. That is a hostage, and the hostage is being held on the victim's premises. I do not think there is a form of words that survives a sceptical reader.

#### Compliant — the recommended design

> **Free tier: unlimited entries, unlimited history, unlimited editing, unlimited export, forever. Capped automatic venue lookups (e.g. 5/month). Paid unlock: unlimited automatic venue naming, plus conveniences.**

Why this passes:
- It caps **a metered service Candour pays for per use**, not the customer's access to the customer's own words. When the cap is hit, the user names the venue by typing it — the entry still exists, is still searchable, still exports.
- It is **honest under 2.1**, because the paywall sits precisely on the cost. The cost sheet and the pricing page describe the same thing. That alignment is rare and worth having.
- It is **never retroactive**. Nothing the user already wrote changes state when the cap is reached.
- Export remains free, complete and always available, per Article 4.

#### Defensible but not recommended

> A forward-only cap on **creating new entries** (e.g. 100 entries free).

This can be made compliant, but only with all four of: (a) stated in plain language *before* the user writes anything; (b) never retroactive; (c) export always free and complete including every entry; (d) all existing entries remain fully readable and editable forever. Even then it fails the alignment test above — the number of entries is not what costs Candour money, so the price no longer describes the cost — and it creates a live incentive to make the cap tighter over time. I would rather Candour did not ship it.

#### Not compliant — I would block these

| Design | Breach |
|---|---|
| Free tier shows only the last 30 days / last 50 entries | Withholds the user's own local data behind a paywall. Article 4 (data at any time, no penalty), Article 1.2 (lock-in). **This is the most tempting design and the clearest breach.** |
| Entries beyond the cap become read-only or greyed out | Retroactive penalty on already-created data. Article 4. |
| Export limited by tier, capped, watermarked, or delayed | Article 4 explicitly: "at any time, at no charge and with no penalty." |
| Cap disclosed only after the user has written entries | Article 4 dark patterns; Article 1.3. |
| Cap tightened for existing free users after launch | Retroactive; Article 1.2. |

**Formal position, per my charter's requirement that a block cites a specific clause:** I am not blocking anything today, because there is nothing to block — no requirements document exists. But I am stating in advance, in writing, that a free tier which restricts access to entries the user has already created breaches Constitution Article 4 and I will treat it as a launch-blocking defect. What would lift it: a cap that restricts only future creation or only metered lookups, with complete export available at every tier at all times.

This aligns with the CVO's objection 8 in the idea brief. **It is now two seats saying the same thing before anyone has designed anything**, which is the cheapest possible moment to settle it.

---

## 9. Model 4 — Article 8 non-profit variant

The CEO did not choose this. The gate should see the number anyway, because it fits a zero-server privacy tool unusually well and because it dissolves three of this document's four hard problems at once.

**Designation under Article 8:** zero distribution, permanent, open-source and self-hostable, transferable only to an asset-locked body.

| Item | Cost | Notes |
|---|---|---|
| Build labour (iOS) | **£14,719 one-off** | Unrecovered. There is no price to recover it from. |
| Maintenance labour | £3,271/yr | [J] |
| Apple Developer Program | £73/yr | [E] |
| Domain | ~£10/yr | [J] |
| Community support (issues, PRs, triage — 50 h/yr) | £1,635/yr | [J], lower than the commercial figure because contributors absorb some |
| Places API | **£0.00** | See below |
| **Annual running cost** | **£4,989/yr** | plus the one-off build |

**Why the API cost goes to zero, which is the interesting part.** In an open-source, self-hostable build, the "self-host" analogue for a serverless app is **bring-your-own API key**: the user supplies their own Google/Foursquare/Mapbox key, or uses the bundled Overture dataset. Candour's metered liability becomes zero and the heavy-user adverse-selection problem in §4.2 disappears entirely, because the heavy user pays their own meter. The one cost Candour cannot control is the one cost the non-profit variant removes.

**What the variant costs Candour, honestly:** £14,719 of unrecovered founder labour plus £4,989/year forever, funded from the Article 2.3 waterfall — of which Candour currently has **£0**, because no product has ever earned anything. Article 8 designation is permanent and irreversible. So the honest description is: **this variant costs one full build and about £5k/year of benchmarked labour, indefinitely, with no recovery mechanism.**

**What it buys:** it deletes the pricing question, the free-tier question, the Article 4 cap question, the store-commission question, the adverse-selection question and the "can we honestly promise lifetime support" question. Everything difficult in sections 5 through 8 of this document is an artifact of trying to charge for it.

**CFO note, offered as judgment and clearly labelled as such [J]:** if the research brief comes back confirming the idea brief's own objection 1 — that Google Maps Timeline already ships the local-only pitch free — then the commercial case for Haunt is thin regardless of pricing shape, and the choice is between killing it and designating it. Designation is the only structure in which "we cannot beat free, and we are not going to pretend we can" is a coherent thing for Candour to say and still ship the product. That is a Constitution 5.4 decision and it is the CEO's alone; I am flagging that it should be a live option at the gate rather than a rhetorical one.

---

## 10. All four models side by side

At **5,000 users**, iOS-only, typical usage, **Mapbox Permanent Geocoding** (the cheapest source whose terms permit permanent storage), shelf prices inc. VAT:

| | 1. One-off purchase | 2. Free + lifetime unlock (9:1) | 3. Free + subscription | 4. Article 8 non-profit |
|---|---|---|---|---|
| **Honest price** | **£23.41** one-off | **£48.50** unlock | **£7.80/yr** yrs 1–3, **£6.14/yr** after | **£0** |
| Margin vs 2.1 target | 16.5% (within ~20%) | 16.5% | 16.5% | n/a (zero distribution) |
| Recurring cost it recovers | 3 yrs only | 3 yrs only | indefinitely | n/a |
| Volume to cover labour (3 yr, iOS) | ~1,480 sales | ~715 unlocks | ~1,480 subscribers held 3 yrs | n/a |
| Heavy-user exposure | **Unfunded after 3 yrs** | **Unfunded after 3 yrs** | Funded, matched | None (user's own key) |
| Article 4 exposure | None | **High — cap design is the risk** | Medium — cancellation flow | None |
| Survives Google Places pricing? | **No** (floor £62) | **No** (£150+) | Yes, at £21.94–£34.80/yr | Yes |
| Survives offline Overture? | Yes (£14.63) | Yes (£29.59) | Yes (£3.21–£4.88/yr) | Yes |

Read across the bottom three rows. **The venue-data decision determines which pricing models remain available.** The pricing question cannot be answered before the CTO answers the architecture question, and I would resist any attempt to settle price at the gate without that note in hand.

---

## 11. Related-party disclosures

**None.** No payment to the founder, family or any affiliated entity is contemplated in this model. All founder labour is costed at the published external benchmark (§2.4) and is currently **unpaid and undrawn**; it appears here as cost because Constitution 2.1 requires it to, "whether or not it is actually drawn."

---

## 12. Price, margin, and justification

- **Price:** none set. Pricing is a Constitution 5.4 decision reserved to the CEO.
- **Margin treatment:** cost + 20%, with store commission passed through at zero markup, giving an effective **16.5%** margin over total published cost including commission. Within the ~20% target, far inside the 30% cap.
- **Deviation from target:** none proposed.
- **The honest reason a deviation might later be needed:** none of the four models generates a reserve at plausible volumes. Constitution 2.3 puts reserve top-up first in the waterfall, and at 1,000–5,000 users Haunt does not clear its own benchmarked labour, let alone fund 6–12 months of operating costs. If the CEO wants Haunt to contribute to a reserve, that is a written deviation on a future cost sheet and it must be argued for explicitly — not smuggled in as a rounded-up price.

---

## 13. What this seat could not establish, stated rather than estimated silently

| Gap | Why it matters | Owner |
|---|---|---|
| ONS ASHE Table 14 not retrieved primary | The benchmark anchors every published number in the company | CFO, before first publication |
| Apple's UK merchant-of-record / VAT position not confirmed on an Apple page | Moves every shelf price by 20% | CFO / CGO |
| Foursquare PAYG caching allowance not retrieved primary | Determines whether Foursquare is even eligible | Research Analyst (commission item f) |
| Whether Mapbox Permanent Geocoding has adequate UK **venue/POI** coverage | The entire Mapbox column depends on it | CTO feasibility note |
| Build and maintenance hours are CFO guesses, not engineering estimates | The largest single cost in every model | CTO feasibility note |
| Visits/user/month and calls/visit are guesses | The only cost that scales | Research brief / TestFlight — and instrumenting it conflicts with the product's own promise |
| Whether storing a venue name on the *user's* device counts as Candour caching under Google/Foursquare terms | Legal question with a direct cost consequence | CGO; Constitution 6.1 may require qualified human review |
| Cloudflare .com renewal price | Immaterial (<0.1%) but listed for completeness | CFO |
| Achievable sales volume | Determines whether any of this matters | Research brief |

---

## 14. Decisions this document puts to the CEO (Constitution 5.4)

1. **How build labour is costed** — capital amortised over declared supported life (this document's treatment, with the three conditions in §1), or year-one operating cost. Definitional; needs a public amendment if adopted.
2. **Whether the benchmark is salary or full employment cost** — moves every number by ~15–18%.
3. **Whether store commission earns margin or is passed through at cost** — moves every price by ~4%. This document passes it through.
4. **iOS-only at MVP, or both platforms** — doubles the break-even volume.
5. **Whether a free tier exists at all** — it roughly triples the honest unlock price at realistic conversion rates (§8.1).
6. **Whether Article 8 designation is on the table at the gate** (§9).

Items 1–3 are not Haunt questions. They will recur on every cost sheet this company ever publishes, and settling them now — while no price depends on the answer — is the honest moment, exactly as the CVO argued on 2026-09-01.

---

## Change log

| Date | Change |
|---|---|
| 2026-09-09 | First discovery cost model. Prices retrieved 2026-09-09. Not a published cost sheet. |

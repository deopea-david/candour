# Idea brief — Haunt

**Date:** 2026-09-09 · **Origin:** CEO spark (direct, not via `/scout`) · **Status:** spark → awaiting research

## The idea in two sentences

A private timeline of where you've been — a night out, a weekend, a year — built automatically from your phone's own location and stored only on your phone, where you can add notes and rate the places you went. It is a journal of venues rather than a map of coordinates: Letterboxd's *habit* of rating and writing up what you experienced, applied to bars, restaurants and everywhere else, with none of Letterboxd's audience.

## Scope decisions taken at spark (CEO, 2026-09-09)

These were open forks; they are closed now so that discovery costs money on one product rather than four.

| Fork | Decision |
| --- | --- |
| **Solo ↔ social** | **Solo journal only for MVP.** No sharing surface at launch. The door is deliberately left open to a later sharing layer, and the research brief is asked whether such a layer would even be wanted — but nothing in the MVP's data model or promise may assume it. |
| **Capture** | **Hybrid: auto-detect, user confirms.** Background location clusters into candidate visits; nothing enters the timeline until the user confirms or edits it. |
| **Privacy promise** | **Local storage with disclosed venue lookups**, plus **opt-in encrypted backup to the user's own cloud** (iCloud on iOS, equivalent on Android). Candour runs no server and holds no user data at any tier. |
| **Money** | **Unresolved by instruction — model several.** CEO is interested in free-with-optional-subscription, a one-off lifetime unlock, and a plain one-off purchase. The CFO is commissioned to model each rather than assume one. |
| **Platform** | **Both iOS and Android are in scope of the promise** (the CEO named an Android backup alternative explicitly). Whether both ship at MVP is a CTO/CFO question, not a settled fact. |

## Who it's for, and what they do today instead

The user is someone who wants a record of their own life's places and does not want that record to be a marketing asset. What they do today, as far as I can state without retrieval:

- **Google Maps Timeline** — free, automatic, already knows every venue in the world, and Google moved Timeline data to on-device storage rather than the cloud [K, medium-high confidence — **load-bearing, must be verified**]. If accurate, the largest incumbent already ships the local-only pitch, for free, with a venue database Candour cannot match. This is the single most dangerous fact in the brief.
- **Arc Timeline / Arc Timeline Recorder (Big Paua, iOS)** — an app that appears to do automatic on-device location timelines, local-first, and moved to a subscription [K, medium confidence — **load-bearing, must be verified**]. If it does what this brief describes, Haunt is not a new product and the brief should say so plainly.
- **Swarm (Foursquare)** — manual check-ins with a history. I have an unverified recollection of a discontinuation announcement and a subsequent reversal [K, low confidence — verify or discard; do not repeat this claim until retrieved].
- **Beli** and similar restaurant-ranking apps — positioned in the press as "Letterboxd for restaurants" [K, medium confidence]. Social and server-backed, so not a privacy competitor, but a direct competitor for the *rating habit* the idea depends on.
- **Day One** and general journalling apps — the note-and-rate behaviour without the location spine [K, high confidence].
- **Apple Significant Locations** — on-device, invisible, not a product [K, high confidence].
- **Nothing.** Most people keep no record at all and don't miss one. This is the honest baseline and the research brief must treat it as the leading competitor, not a rounding error.

**No citation in this brief was retrieved this session.** Every claim above is tagged [K] deliberately and none may be repeated as [E] until the Research Analyst retrieves it (`pipeline/evidence-standard.md`).

## Why this fits Candour (which principles it serves)

- **1.5 / 2.1 — cheap to run.** A product with no server has close to no running cost. That is unusually clean: the cost sheet is founder labour, an App Store cut, and a venue-lookup API bill, and nothing else. It is the first candidate on the backlog where "cheap to run" is a structural property rather than a discipline.
- **4 — minimum data.** "We collect nothing" is not a policy here; it is an architecture. Article 4's data-export requirement is nearly free when the data is already a local file.
- **1.3 — honest by default.** The promise has to survive contact with the venue lookup (below), and saying so plainly *is* the product's differentiator against every competitor whose privacy page is a lawyer's paragraph.

## The honesty problem this product must solve first

The pitch is "never sent anywhere." The MVP as scoped sends a coordinate to a places API every time it names a venue. Both things cannot be said. Under Article 1.3 the marketing claim has to be the narrow true one — *your timeline, notes and ratings never leave your device; naming a venue asks a map provider what's at this spot* — and the product has to make that boundary visible in the app rather than in a privacy policy. If the research shows users read that distinction as a broken promise, the "zero network, offline venue dataset" variant returns to the table as the real product, at materially higher build cost. **This is a discovery question, not a copywriting one.**

## What would make this NOT worth doing

Written before any research, and deliberately not sandbagged.

1. **Google Maps Timeline is free, automatic, on-device and already knows every venue.** If [K] above holds, the entire privacy differentiator has already been conceded by the incumbent, and what remains for Haunt is the notes-and-ratings layer alone — a much smaller idea than the one sparked.
2. **Arc Timeline may already be this product**, shipping, on iOS, with years of head start. If so this is a kill on arrival unless the journal layer is a genuine gap in it.
3. **Journalling retention is famously bad.** The location spine is automatic and will keep working; the notes and ratings are manual and are exactly the behaviour people abandon in week three. The product's whole value-add sits on the fragile half.
4. **Two platforms, one operator.** Background location is not portable: iOS has a cheap first-class visit-detection API, Android's equivalents are weaker, and its OEM battery-killers are hostile to background work [K, medium-high confidence]. Promising Android roughly doubles the build and imports a support burden with no server to fix anything from.
5. **The promise destroys the feedback loop.** If nothing is sent anywhere, there is no analytics, no crash telemetry by default, and no way to learn how the app is actually used. That is the honest cost of the pitch and it must be priced, not admired.
6. **Privacy-first consumer apps monetise badly** [K, medium confidence]: no ads, no data, no viral loop, no social graph, and — with no sharing surface at MVP — no organic acquisition channel at all, against a 20% margin that cannot fund paid acquisition. This is the same structural growth problem that sank the Postcard growth story, and it is not solved by the product being better.
7. **The venue-data dependency may not be legal in a local-first app.** Major places APIs restrict caching and long-term storage of place records [K, medium confidence, **must be verified**]. A journal that keeps a venue record forever may be in breach of the terms of the API that named it — which would force either an offline open dataset (OSM/Overture) with worse coverage, or a legal problem at the heart of the architecture.
8. **A free tier that caps journal entries is an Article 4 hazard.** I am flagging this as CVO disagreement rather than waiting for the gate: capping *creation* is defensible, but if a user writes entries and later loses access to entries they already wrote, that is holding a customer's own data hostage, and Article 4 requires free export at any time regardless. Any freemium model must be specified so that the paywall never sits between a user and words they have already written.
9. **A subscription is hard to justify under 2.1.** Article 2.1 prices at cost + ~20%. A product with no server has almost no recurring cost, so a recurring price has almost nothing to be 20% *of*. A lifetime unlock or one-off purchase fits the cost structure honestly; a subscription needs a written justification on the cost sheet or it should not ship. The CFO is asked to make that case or refute it, not to assume it.

## Commissioned discovery

- [ ] **Research brief** (Research Analyst) — commissioned **2026-09-09**, **due 2026-09-30**. Must close, in priority order: (a) exactly what Google Maps Timeline now does and where its data lives; (b) whether Arc Timeline (or any other shipping app) already is this product, and at what price; (c) whether the notes-and-ratings-on-venues habit exists outside social apps, or only exists *because* of the audience; (d) whether users read "local storage + venue lookup" as an honest promise or a broken one; (e) whether a later sharing layer is wanted by the people who want the private version — the CEO explicitly asked whether it would even be a useful addition; (f) places-API terms on caching and retention.
- [ ] **Cost model** (CFO) — **model three shapes side by side**: plain one-off purchase; free tier plus lifetime unlock; free tier plus subscription. Include the App Store/Play cut, per-lookup places-API cost at realistic usage, and benchmarked founder labour amortised over the product's life. State plainly whether a subscription can be justified under 2.1 for a product with no server, and whether an entry cap can be designed without an Article 4 breach.
- [ ] **Feasibility note (CTO)** — **warranted.** Background visit detection on both platforms and its battery cost; the local data store and its export format; opt-in encrypted backup to a user-held cloud with no Candour-held key; offline vs online venue naming, including the cost of a bundled dataset if the zero-network variant is revived. Also: how a product that sends nothing anywhere gets diagnosed when it breaks.

**Anti-drift (Constitution 5.2):** kill / proceed / park decision due **2026-10-07**.

*Corrected 2026-09-09.* This brief originally recorded 2026-10-28, computed as four weeks from the research brief's *due* date. The Research Analyst delivered on 2026-09-09, three weeks early, and flagged that 5.2 says four weeks "of its research brief" — which, once the brief exists, is four weeks from delivery. The literal reading is adopted and the deadline moves **21 days earlier**. Flagged to the CGO to record. Delivering early must not be allowed to buy slack.

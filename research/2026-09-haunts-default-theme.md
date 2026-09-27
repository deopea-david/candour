# Research brief — Haunts default theme (Hybrid A vs Hybrid B)

**Date:** 2026-09-27 · **Author:** Research Analyst · **Commissioned by:** CEO, decision **D44** (`decisions/2026-09-16-haunt-gate.md`), jointly with UX
**Slug:** `haunt` · **Not on the anti-drift clock** — this is a design sub-question inside an already-decided PROCEED, not a new idea's research brief (Constitution 5.2 does not apply here).
**Inputs read:** D38, D42, D44 (`decisions/2026-09-16-haunt-gate.md`); UX's `products/haunt/design/round-2/directions.md` and its SVGs; `research/haunt-brief.md` (original discovery); `products/haunt/design/themes.md` (MEM-1 and theme rules); `products/haunt/requirements.md` §MEM-1.

## 0. The question, read inside Candour's rules

D44 asks UX and Research to recommend which of Hybrid A ("warm editorial": cream/plum/apricot) or Hybrid B ("mono editorial": black/white/one orange) is the **default** theme, and so what the store listing shows first. The CEO framed the test as *"what would stand out most and be most eye catching and keep people engaged."*

**"Engaged" is read inside the rules, not as time-in-app.** The CVO recorded this at D44 and I apply it as a constraint on my own method, not just a quote: the default must be judged on **appeal and clarity to a new user**, never on anything that would extend a session or reward return visits. Constitution Article 4 bans *"engagement mechanics designed to exploit compulsion,"* and `requirements.md` MEM-1 states the product-wide rule verbatim: Haunts *"never rewards the frequency or volume of visits — anywhere in the product."* Nothing below scores a theme by predicted session length, streak-formation, or return rate. Where "eye-catching" and "engagement-as-compulsion" could be confused, I say so.

**Both hybrids already pass accessibility.** UX's `directions.md` §9 appendix shows 76 measured contrast pairs, all passing WCAG 2.2 AA, for both hybrids. This brief does not re-litigate that; it is silent on accessibility because UX has already closed it, and a default chosen for appeal cannot reopen a question Article 4/WCAG already settled the other way.

---

## 1. Store listing and first impression

**Verdict: on the evidence I could retrieve, Hybrid B's icon is the more distinctive against the actual App Store neighbourhood; Hybrid A's icon has a real, specific collision risk with the nearest direct competitor.**

### 1.1 What the neighbourhood actually looks like, retrieved

I searched the App Store (via the in-app browser, screenshots taken 2026-09-27) for the four products the original `haunt-brief.md` already identified as the closest neighbours for "location history" / "journal" / "diary" search terms, plus checked one more that surfaced under "location history":

| App | Icon, as retrieved | Category signal |
|---|---|---|
| **Arc Timeline 4** — the single closest direct competitor (automatic location timeline, on-device, notes) | Purple-to-violet gradient rounded square, a white upward arrow/compass triangle | [E — https://apps.apple.com/gb/app/arc-timeline-4/id6740688708, screenshot retrieved] |
| **Timeline: Location History** — appears directly under the term "location history" | Blue rounded square, a literal folded map with red location pins | [E — https://apps.apple.com/ca/app/timeline-location-history/id6795713266, screenshot retrieved] |
| **Day One** — the category leader for "journal"/"diary" (118K ratings, Editors' Choice) | Light pastel-blue rounded square, a white bookmark/ribbon glyph | [E — https://apps.apple.com/us/app/day-one-daily-journal-diary/id1044867788, screenshot retrieved] |
| **Daylio** — "Private Diary," second-largest journal-adjacent app I checked (62K ratings) | Green rounded square, a white circular smiley face | [E — https://apps.apple.com/us/app/daylio-journal-mood-tracker/id1194023242, screenshot retrieved] |

**Note on method:** the App Store's web search page would not render results for me (it returned "page not found" for both a direct search URL and typed search — I tried both and record the failure rather than papering over it). I retrieved individual listing pages instead, which is a narrower sample than a live search grid. I did not attempt to reconstruct what a real search-results grid looks like at icon size (roughly 60×60pt on device); the colours above are as shown on each app's own product page, which is the same icon asset.

**The pattern across all four, independent of my priors:** every one is a **saturated, cool-toned colour** (violet, blue, blue, green) **on a rounded square, carrying one simple white glyph.** This is a real, retrieved convention, not a guess — three of four are shades of blue/blue-green, and the fourth (Arc) is violet.

### 1.2 What this means for Hybrid A vs Hybrid B

I then looked directly at the two candidate icons (`products/haunt/design/round-2/concepts/hybrid_a-icon-h.svg` and `hybrid_b-icon-h.svg`, opened and screenshotted in-browser):

- **Hybrid A's icon is plum (`#5B2A86`) with a cream "h."** Plum is a violet. **Arc Timeline 4 — the one app in this list that does the same job as Haunts — is also a violet gradient icon.** Two saturated violet icons in the same search result, for the same product category, is the closest thing to a genuine collision risk this exercise found. It is not identical (Arc's is a gradient with a white triangle; Hybrid A is flat with a lowercase serif-adjacent "h"), but hue family is what separates icons fastest at 60pt in a scrolling list, before shape registers. [I, from the retrieved colours above]
- **Hybrid B's icon is near-black (`#111111`-range) with a white "h" and one orange bar.** **None of the four retrieved competitors uses black.** Against a field of violet/blue/blue/green, a near-black icon is the single largest value (light/dark) jump available, which is also the cheapest kind of distinctiveness to get right — it survives greyscale and colour-blind simulation by construction, because it is not relying on hue at all. [I]

**Finding, stated as the charter requires:** on icon distinctiveness specifically, the retrieved neighbourhood favours **Hybrid B**. This is a narrower claim than "Hybrid B is the better icon" — it is a claim about how it will sit in a grid of the four nearest retrieved competitors, nothing else.

### 1.3 Screenshot/listing distinctiveness — I could not retrieve anything specific here

I looked for evidence on what makes a *screenshot set* (as opposed to the icon) stand out in App Store search, beyond generic ASO advice. I did not find product-specific data; §1.4 explains why I am discounting the generic advice I did find. I have no retrieved basis to prefer A or B on screenshot composition, and I am not going to invent one.

### 1.4 A claim I checked and am discounting

ASO industry blogs assert large, specific lifts from icon design — e.g. "37% higher tap-through," "distinctive silhouettes have 34% higher recognition," "up to 25% more installs" [multiple ASO vendor blogs, search results 2026-09-27]. I fetched one of these articles in full (apptweak.com) to check its sourcing. **Its only concrete, attributed figure was a single vendor's case study reporting a 21.5% install lift for one mobile game's icon change** — everything else was asserted as general industry knowledge with no citation. I am treating the round-number percentage claims across this genre of article as **marketing content, not evidence**, and I am not using them anywhere in this brief's reasoning. [E, checked and rejected — https://www.apptweak.com/en/aso-blog/how-to-design-an-app-icon] What *is* solid: Apple's own Product Page Optimization documentation confirms icon and screenshots are both directly A/B-testable **after launch**, with real conversion data [E — description of the mechanism corroborated across multiple ASO-tool documentation pages, e.g. https://appfigures.com/resources/guides/how-to-ab-test-app-store-connect]. That is a genuinely free, real-world test Haunts can run once it has traffic — see §4.

---

## 2. Customisation as a selling point

**Verdict: real and organically valued by some users, but not what the category leader leads with. "You choose how it looks" is a credible secondary selling point, not established as a primary acquisition driver.**

I checked what the two most relevant competitors actually say about appearance customisation, in their own live App Store copy — not what a blog claims about them.

- **Day One (118K ratings, Editors' Choice, the market leader)**: I read its full, current App Store description in full (retrieved 2026-09-27). Its ~20 feature bullets cover privacy/security, rich content, reminiscing, and habit formation. **Visual theme or appearance customisation is not mentioned anywhere in the live listing.** [E — https://apps.apple.com/us/app/day-one-daily-journal-diary/id1044867788]. This is a finding, not an absence I'm inferring: the single most successful product in this exact category does not currently market "how it looks" as a reason to choose it.
- **Daylio (62K ratings, "Private Diary")**: its description lists **"Customize color themes"** as one bullet among roughly fifteen, well below privacy, mood-tracking and habit features in emphasis [E — https://apps.apple.com/us/app/daylio-journal-mood-tracker/id1194023242]. More telling: **one of its own displayed user reviews volunteers it unprompted** — *"[the app is] customizable to every person, even down to the color scheme"* is named as a genuine point of delight, alongside the mood-tracking core feature [E, same page, a real displayed review — single review, anecdotal]. That is the strongest piece of evidence in this brief that theme choice is a real, felt benefit for at least some users in this exact category — but it is one reviewer, cited as a supporting detail in a long review about something else.

**On alternate app icons specifically** (the open question D44(4) leaves for the CEO, separate from this decision): the ASO-industry framing I found describes rotating/seasonal alternate icons as **a re-engagement nudge** — "nudge users to open the app through the surprise of a fresh icon" [E — https://medium.com/@deepakjangra91313/the-icon-illusion-how-your-favourite-apps-change-their-look-without-you-noticing-e3ba73d25cf0, a single blog, unverified methodology]. **I flag this because it is the opposite of what MEM-1 permits.** If alternate icons are ever built, "new icon as a surprise/reward" is explicitly the wrong frame for this product; a user-chosen, static icon tied to their chosen theme is a different thing and not what that source is describing. This is a flag for whoever picks up D44(4), not a finding about the default-theme question.

**Net:** I found no evidence that theme/appearance customisation moves a first-time install decision. I found modest, real evidence that it is valued after people are already using a journal-type app, and that a competitor's own displayed review treats it as a delight. "It's for people... and they can view it as they want" (the CEO's reason, D44) is a genuine and defensible product idea; the evidence available to me says it is table stakes-adjacent — a nice bullet, not a headline — rather than a proven differentiator. Neither hybrid gains or loses on this question **relative to each other**; it is a finding about the theme-set decision generally, already taken at D44, not about which is the default.

---

## 3. The audience fit — and a real tension I am not going to smooth over

**Verdict: the evidence points in two different directions depending on which part of the audience it is read against, and I think the honest thing is to say so rather than pick the reading that makes the brief tidy.**

`research/haunt-brief.md` (the original discovery brief) already characterises this audience in retrieved detail: people already using Arc Timeline, or self-hosting Dawarich/OwnTracks/Traccar — i.e. **a technical, privacy-literate minority**, not a mass consumer audience (haunt-brief.md §3.2, §9). That brief's own ceiling argument put Arc's UK paying base in the low thousands at most.

**Reading 1 — trust literature favours the monochrome, precise register (Hybrid B).** What I found on privacy-product design and trust: minimalist, monochrome interfaces are read by privacy-conscious users as a **visual statement of restraint** — "no tracking, no ads, no distractions... the clean interface feels trustworthy" — with Signal repeatedly cited as the reference case for security-through-visible-simplicity [E, a design-commentary piece rather than a controlled study — https://blakecrosley.com/guides/design/signal; corroborated in direction by https://medium.com/@harsh.mudgal_27075/privacy-first-ux-design-systems-for-trust-9f727f69a050, same genre of source, **not independent** — both are design-blog commentary, not empirical research]. Hybrid B's code-like details (`//`, monospace times) are the kind of register this audience already trusts elsewhere — it visually rhymes with the technical tools (self-hosted dashboards, terminal-adjacent apps) this exact audience already uses, per the original brief's own competitor list.

**Reading 2 — UX's own usability finding favours the warmer, plainer register (Hybrid A), and for the audience Candour says it is building for.** UX's `directions.md` (§2, "Risks," and §10) found Hybrid B is *"more distinctive and less friendly. For a first-time, non-technical user, `// to confirm` is a small puzzle the plain words don't pose"* — and rated Hybrid A *"the kinder of the two for everyday users, the charter's first test."* Constitution 1.1 defines the mission as building for "everyday people," not a technical subculture — even where the realistic first buyers skew technical, the constitution's own bar is the everyday user, not the most-likely early adopter.

**I am not resolving this tension by picking a side — it is a genuine trade-off between "what today's realistic buyer already trusts" and "what the constitution says the product is for," and no desk evidence I retrieved settles which should win for a default.** What I can say: neither reading is about which theme is more "eye-catching" in the CEO's casual sense — both are about **credibility to two overlapping but distinct slices of the same small audience**, which is exactly the sort of question this seat cannot settle from published sources (§4).

**One point that cuts across both readings:** whichever is the default, **both stay available at launch (D44)**, selectable in-app. The stakes of getting the *default* wrong are lower than they would be if only one theme shipped — a user who bounces off the store listing never sees the in-app choice, but a user who installs sees both within seconds. The default mainly matters for the store listing and first ninety seconds, not for the long-run relationship with the product.

---

## 4. Honest limits, and the cheapest honest preference test

**What desk research cannot settle, stated plainly:** I have no retrieved evidence of real people's reaction to *these specific* two designs. Nobody has seen either — `requirements.md` §22 item 1 records that no usability testing of any kind has happened on Haunts, and D44's own recorded note says the same. Everything in §1–3 is either (a) a structural fact about the competitive icon field, which is solid but indirect, or (b) general literature about trust and minimalism, which is suggestive but not about this product. **Appeal is a property of people looking at something, and no desk method substitutes for that.** This is the limit the CEO's own instinct (D44 note 2) already named, and I am not going to pretend I closed it from a browser.

**The cheapest honest instrument, specified:**

- **Method:** a **preference test** — show two static App Store listing mock-ups (icon + first two screenshots) for Hybrid A and Hybrid B, side by side or in random order, and ask which they would tap on and why, plus a one-line "does this look trustworthy with your location data" prompt.
- **Tool:** **Lyssna** (formerly UsabilityHub) supports exactly this test type, and its free plan includes **15 self-recruited responses per month at £0** — no panel credits required, only the cost of recruiting participants yourself [E, confirmed by direct retrieval of the pricing page, 2026-09-27 — https://www.lyssna.com/pricing]. This is £0 in tool cost, matching the CEO's own suggested scale (10–15 people) almost exactly.
- **Recruitment, and its honest bias:** self-recruited means friends, a relevant subreddit (e.g. r/privacy, r/degoogle, or Arc Timeline's own user forum — the same forum the original brief already cites, `support.bigpaua.com`), or a small personal network. **This is not a random sample of App Store browsers.** Recruiting from privacy-focused communities specifically would oversample the technical end of the audience (§3, Reading 1) and undersample the "everyday, first-time user" the constitution's mission targets — the opposite bias to be aware of, not a reason not to run it. **State this bias in the write-up whichever way the result goes.**
- **Cost:** £0 in tool fees at n≤15/month; the only cost is the CEO's or UX's time to recruit and to read the free-text answers. This satisfies the CEO's explicit question of whether it can be done at £0 — **yes, at this scale, with this tool.**
- **What it cannot give:** statistical significance (n=10–15, one round, self-selected), a real installation decision (people are looking at a mock-up, not choosing among twenty search results while distracted), or resolution of the Reading-1-vs-Reading-2 tension in §3, since that tension is about *which slice of the audience* is recruited. It is a **directional read**, not a verdict — which is exactly the honesty D44 note 2 already asked for.
- **Who runs it:** this is a UX instrument (it operationalises a UX artifact) as much as a research one; I specify the method and cost as commissioned, and recommend UX own execution, with the CEO's authorisation to spend the (near-zero) time, per D44.

---

## 5. Recommendation, confidence, and what would overturn it

**Recommendation: Hybrid B as the default and what the store listing shows first, at moderate-low confidence.**

**Why, briefly:** §1 is the only place in this brief with a retrieved, specific, product-relevant finding rather than general literature — and it is a clean one: Hybrid A's icon sits in the same colour family as the one app in the retrieved set that does the identical job (Arc Timeline 4), while Hybrid B's is the only near-black icon against four retrieved competitors that are all saturated blue/green/violet. That is a real, checkable fact about the store shelf Haunts will actually sit on, not a matter of taste. §3's trust-literature reading (Reading 1) points the same way for the audience most likely to convert first (the technical, already-privacy-motivated buyer the original discovery brief sized as the realistic market). §2 does not distinguish the two.

**Why only moderate-low confidence, stated honestly:** this goes against UX's own recommendation (`directions.md` §10, Hybrid A, on usability-for-everyday-users grounds) and against Reading 2 in §3, which is arguably the more constitutionally-grounded reading (Article 1.1's "everyday people," not the realistic-early-adopter's already-technical taste). It rests on **one retrieved icon comparison** (§1.2) as its load-bearing fact — a real fact, but a single data point about four competitors, not a study. And it is exactly the kind of appeal question §4 says desk research cannot close.

**What would overturn it, stated as falsifiers:**

1. **The §4 preference test, run on 10–15 people, showing a clear majority for Hybrid A.** This is the single most direct overturn available and it is nearly free — I would weight a real result from real eyes over my own shelf-adjacency reading without hesitation.
2. **A wider icon sample** (I checked four; a proper search-results screenshot, if the App Store's search UI can be reached some other way, might show the neighbourhood is more colour-diverse than these four suggest, which would weaken §1's central claim).
3. **Evidence that the realistic first buyers are less technical than the original discovery brief found** — if Haunts' actual early customers turn out to be ordinary Arc-curious users rather than the self-hosting crowd, Reading 2 in §3 (Hybrid A, friendlier) gets stronger and my icon-adjacency argument gets relatively weaker.
4. **A finding that Arc Timeline is not, in practice, a co-occurring search result** for the terms Haunts will actually rank for (I did not verify Haunts and Arc would appear in the same App Store search results page — I inferred proximity from category and function, not from a retrieved search-results screenshot).

I would not call this settled, and I do not think it should be. It is the honest read of a thin evidence base, on a question the CEO already correctly identified needs real people to answer properly.

---

## Evidence ledger

Tagged per `pipeline/evidence-standard.md`. Every [E] was retrieved in this session (2026-09-27) and the link travels with the claim. No citation is from memory.

### Load-bearing [E]

| # | Claim | Source | Notes |
|---|---|---|---|
| E1 | Arc Timeline 4's icon: violet/purple gradient square, white arrow/compass glyph | https://apps.apple.com/gb/app/arc-timeline-4/id6740688708 — screenshot retrieved via in-app browser, 2026-09-27 | The closest direct competitor |
| E2 | "Timeline: Location History" icon: blue square, literal map with red pins | https://apps.apple.com/ca/app/timeline-location-history/id6795713266 — screenshot retrieved | Surfaces under the exact search term "location history" |
| E3 | Day One's icon: pale blue square, white bookmark glyph; and its full live App Store description contains no appearance/theme-customisation bullet | https://apps.apple.com/us/app/day-one-daily-journal-diary/id1044867788 — full page text and screenshot retrieved | Category leader, 118K ratings, Editors' Choice |
| E4 | Daylio's icon: green square, white smiley; description lists "Customize color themes" as one of ~15 bullets; a displayed user review names colour-scheme customisation as a delight | https://apps.apple.com/us/app/daylio-journal-mood-tracker/id1194023242 — full page text and screenshot retrieved | 62K ratings |
| E5 | Hybrid A icon colours: plum background (`#5B2A86`), cream "h" | `products/haunt/design/round-2/concepts/hybrid_a-icon-h.svg`, opened and screenshotted directly | Confirms `directions.md`'s stated palette |
| E6 | Hybrid B icon colours: near-black background, white "h," orange bar | `products/haunt/design/round-2/concepts/hybrid_b-icon-h.svg`, opened and screenshotted directly | Confirms `directions.md`'s stated palette |
| E7 | Lyssna's free plan includes 15 self-recruited test/survey responses per month at £0, no card required | https://www.lyssna.com/pricing, retrieved 2026-09-27 | Directly answers the CEO's £0 question |
| E8 | Apple's Product Page Optimization supports A/B-testing icons and screenshots post-launch with real conversion data | Corroborated across ASO-tool documentation, e.g. https://appfigures.com/resources/guides/how-to-ab-test-app-store-connect | Mechanism confirmed across multiple sources describing the same Apple feature; **not independent of Apple's own documentation**, which I did not separately retrieve |

### Supporting [E], with flags

| # | Claim | Source | Flag |
|---|---|---|---|
| E9 | Minimalist/monochrome UI is read as a trust signal for privacy-conscious users; Signal cited as the reference case | https://blakecrosley.com/guides/design/signal ; https://medium.com/@harsh.mudgal_27075/privacy-first-ux-design-systems-for-trust-9f727f69a050 | **Design commentary, not empirical research. Both sources are the same genre of blog and should be read as one perspective, not two independent findings.** |
| E10 | Alternate/rotating app icons are framed in ASO literature as a re-engagement nudge | https://medium.com/@deepakjangra91313/the-icon-illusion-how-your-favourite-apps-change-their-look-without-you-noticing-e3ba73d25cf0 | **Single blog, unverified methodology. Used only to flag a future MEM-1 risk, not as evidence for this decision.** |
| E11 | ASO blogs' large percentage claims (e.g. "37% higher tap-through") trace, where checked, to a single vendor case study rather than a general study | https://www.apptweak.com/en/aso-blog/how-to-design-an-app-icon, fetched in full | **Checked and explicitly discounted — recorded so the same claim isn't repeated uncritically elsewhere** |

### [K] — model knowledge, not verified, do not rely on

- **K1.** General impression that App Store search-result grids show icons small enough that hue/value separates faster than fine detail. Plausible, consistent with general design principles, but I did not retrieve a controlled study of App Store scanning behaviour specifically.

### [I] — inference, from tagged premises

- **I1.** Hybrid A's plum icon risks hue-family collision with Arc Timeline 4's violet icon in a shared search context. From E1, E5.
- **I2.** Hybrid B's near-black icon is the largest value-contrast option against the four retrieved competitors. From E1–E4, E6.
- **I3.** The realistic first-buyer audience (technical, already privacy-motivated, per `haunt-brief.md`) overlaps with the audience E9's minimalist-trust literature describes. From `haunt-brief.md` §3.2/§9 and E9.

### [J] — judgment

- **J1.** The default matters mainly for the store listing and the first ~90 seconds in-app; the in-app theme choice (both ship at launch) limits the downside of getting the default "wrong."
- **J2.** A single retrieved icon-adjacency fact (Hybrid A vs Arc Timeline) is real but thin as the sole load-bearing reason for a recommendation — hence "moderate-low," not "high," confidence.

### Open items I could not close

1. **A genuine App Store search-results grid**, rather than individual listing pages — the web search UI did not render results for me (tried a direct search URL and an in-page search box; both returned "page not found" / no results). This is the single biggest gap in §1; a wider, in-context sample could weaken or strengthen the collision finding.
2. **Whether Haunts and Arc Timeline would actually co-occur** on the same App Store search-results page for Haunts' likely keywords — inferred from category/function, not observed.
3. **Any primary research on App Store icon scanning at small size** (colour vs. shape vs. value) — I found only vendor marketing content, which I have explicitly discounted (§1.4).
4. **Screenshot-level (not icon-level) distinctiveness** — no retrieved evidence either way; not used to break the tie.

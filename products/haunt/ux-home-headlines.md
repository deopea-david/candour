# UX note: home-screen headlines (Haunts)

**Seat:** UX / Design Lead · **Date:** 2026-09-23 · **Slug:** `haunt`
**Commissioned by:** the coordinator, on **D20** (CEO, 2026-09-22) and its **refinement of 2026-09-23**, both in `decisions/2026-09-16-haunt-gate.md`.
**Input artifacts, all read from disk this session:** `constitution.md` v1.3 (Articles 1 and 4 in full), `roles/ux-lead.md`, `pipeline/evidence-standard.md`, `decisions/2026-09-16-haunt-gate.md` (D10, D11, D13, D19, D20 and the D20 refinement), `products/haunt/requirements.md` (DEF-1 to DEF-3, VPAGE-3, VPAGE-6, VPAGE-10, VPAGE-11, LOOK-1 to LOOK-8, ENT-9, ONB-1, ONB-2, PRIV-7, PRIV-8, A11Y-1 to A11Y-10, §17), `products/haunt/ux-note.md` §5, `products/haunt/ux-note-pricing.md` §4.
**Output scope:** this file only. **`requirements.md` is not edited**, because the PM/BA is working on it. Section 9 is written so the PM/BA can lift it directly as a new `HEAD-` block.
**Status:** this note prepares and flags. It does not certify (Constitution 6.1). The defaults below are this seat's proposal, which D20 asked for (*"Defaults are UX's to propose"*). They are not decisions. The CEO may overrule any of them without an overrule record, because none is a block.
**Template note:** `pipeline/templates/` has no UX-note template. The directory, listed this session, holds `cost-sheet.md`, `decision-record.md`, `dissent-memo.md`, `gate-pack.md`, `idea-brief.md`, `proposal.md`, `requirements.md`, `research-brief.md` and `review-pack.md`. This note follows the charter's named outputs (flows, usability review notes, the Article 4 conformance check and accessibility audit notes) and states that it departs from a template rather than doing so silently. Section 9 uses the column layout of `requirements.md`, so it can be pasted in unchanged.
**Evidence:** tagged under `pipeline/evidence-standard.md`. I retrieved every [E] on **2026-09-23** and give its link in §13. Every assertion about what the Constitution or a decision requires quotes the clause in the same passage. Where I give my own judgment, the tag says [J].

**The honesty statement, unchanged from my two earlier notes.** I have run **no usability test**, drawn no clickable prototype and watched no user. Whether people find a line of facts about themselves warm or cheesy is an empirical question, and I am answering it with judgment. §10 says what evidence would overturn each judgment.

---

## 0. The answers, before the reasoning

1. **Default: on, as a static line.** The line shows one fact and changes **once a day** in a fixed order. The ticker the CEO described is **one tap away** and is not the default. Card and Off are the other two appearances. §2.
2. **Eligible facts:** a fixed, enumerated set of **nine templates**, covering places, ratings, dates and spans. Following the CEO's refinement, **nothing is held behind an opt-in on privacy grounds.** Three things are excluded for other reasons: other people's names (third-party data, pending the CGO ruling), note text, and anything that counts or rates volume. §3.
3. **The one privacy precaution:** headlines never appear in the **app-switcher snapshot**. The user also gets a per-place and per-category "leave out of headlines" control, which is their own choice and not a gate. §8.
4. **Motion:** the ticker drops to the static line **automatically** under iOS Reduce Motion, under Android "Remove animations", while a screen reader is running, and at the largest text sizes. A **visible pause control** is always present whenever the ticker is moving. **Implementation trap:** React Native's documented reduce-motion check on Android reads a *developer-options* setting, and a reported bug says the Android accessibility switch did not trigger it. **The ticker must be tested against the accessibility switch on a real Android device.** §7.
5. **Memories, never volume.** Warmth may attach to a place, a span of time or a ritual. It never attaches to a count, a rate, a run or a record. §4 gives 10 permitted and 18 prohibited example phrasings.
6. **Small numbers:** a headline is a selection the app makes for the user, so selection carries a higher bar than display. No fact is headlined below its threshold, and every figure carries its count. D19's weighted order is used to pick the "top" place. The number shown is the true mean. §5.
7. **Before there is enough data, the slot does not exist.** There is no placeholder, no progress bar and no "3 more visits to unlock". §6.
8. **LOOK-8(e) is superseded for this one element.** Requirements currently keep the self-portrait off launch screens. D20 and its refinement put portrait facts on the home screen. The app-switcher, widget, onboarding and preview exclusions all still stand. §1.2.

---

## 1. What was decided, and what this note changes

### 1.1 The governing decision, quoted

**D20 (CEO, 2026-09-22):** facts from the local self-portrait are shown *"like headlines/marquee at the top of the homescreen, bit like news channels"*, **toggleable, with its appearance changeable**.

**Refined by the CEO, 2026-09-23**, quoted from the record:

> *"**(1) Privacy:** the home-screen concern is overstated — personal information on screen is ordinary in banking and maps apps — and is withdrawn, **except the app-switcher preview**, which banking apps blur and so should Haunts. **(2) Motion:** the platform's reduce-motion setting is **detected and applied automatically**, with a manual pause kept for users who have not set it. **(3) "Never celebratory" was too broad.** Warmth is permitted; the prohibition is on **celebrating frequency or volume**. … **The rule: celebrate memories, never volume.**"*

The coordinator added one instruction: **do not gate facts behind an opt-in on privacy grounds alone.** This note follows that instruction. The one place where I would have done otherwise is recorded once, in §11, as a disagreement. It is not built into any criterion.

### 1.2 Reconciliation owed in `requirements.md`, stated explicitly for the PM/BA

**LOOK-8** was written on 2026-09-22, before D20, and currently says:

> *"Like the heatmap it summarises a life, so it is **not rendered on launch, onboarding, previews, widgets or the app-switcher snapshot** (**LOOK-2**(a), (e))."*

**This note supersedes LOOK-8(e) for one element only: the home-screen headline slot (HEAD-1 onward).** Three reasons. First, the home screen is the launch screen. Second, D20 puts portrait facts there. Third, the refinement withdraws the privacy concern that LOOK-8(e) rested on. **The following LOOK-8 exclusions still stand for the headline too:**

| LOOK-8(e) surface | Status for headlines | Why |
|---|---|---|
| Launch / home screen | **Superseded**, and permitted per HEAD-1 | D20 as refined |
| App-switcher snapshot | **Still excluded** (HEAD-12) | The CEO kept it in terms: *"except the app-switcher preview"* |
| Widgets, lock screen, notifications | **Still excluded** (HEAD-13) | Not a privacy gate. These are **push surfaces**. D19(d) says the portrait is *"pulled, never pushed"*, and B1 bars notifications on a cadence the user did not set. D20 moved the portrait onto the user's own open app, not outside it |
| Onboarding screens | **Still excluded** (HEAD-13) | ONB-1 governs first run. Headlines have nothing to say before data exists anyway (§6) |
| Store / marketing previews made from real data | **Still excluded** (HEAD-13) | LOOK-2(a) sets this for all derived views |

**Two consequential edits to LOOK-8 that the PM/BA should make when folding this in.** Neither is a disagreement with the PM/BA's drafting. Both follow from D20's refinement.

- **LOOK-8's example sentence** *"You've been going there for three years"* makes a claim of continuity, and that claim is false for a place the user stopped visiting. Reword it to the since-date form (§5.4, template T3).
- **LOOK-8's "no … comparisons"** should read *"no comparisons with anyone else and none of the user's own periods against each other"*. The CEO's own example, *"You rate pubs 4.1 and cafés 3.2"*, contrasts two kinds of **place**, and it is the founding example of the feature. §4.3 draws the line.

### 1.3 The tension with D19(d), named so nobody rediscovers it

D19(d) says the portrait carries *"the same constraints as the recap: pulled, never pushed"*. A headline the user sees on opening the app is neither fully pulled nor pushed. **I read D20 as the CEO's deliberate, narrow exception, and I find it compatible with Article 4.** The ground is Condition 8.4 as clarified at C1-O11: *"What 8.4 forbids is **interruption and urgency**: anything that reaches for the user's attention, or counts down. It does **not** forbid **static, in-context disclosure**."* A static line inside an app the user chose to open is in-context. **What would take it outside that clarification** is motion that competes for the eye, content that changes to reward reopening, or a slot that carries anything other than portrait facts. Sections 2, 4 and 9 (HEAD-7, HEAD-8) exist to keep it inside.

---

## 2. Defaults and appearances

### 2.1 The four appearances

| Appearance | What it is | Changes when |
|---|---|---|
| **Line** *(default)* | One fact, one or more lines of text, full width, at the top of the home screen, scrolling away with the content | **At most once per calendar day**, at the first open of the day, in a fixed cycle through the eligible facts. **Never while on screen** |
| **Card** | Up to three facts at once in a static card | Same as Line |
| **Ticker** | All eligible facts in one horizontal line that scrolls slowly, news-channel style | Moves while displayed. Pausable. Falls back to Line automatically (§7) |
| **Off** | Nothing. The slot collapses to zero height | Never. The portrait itself stays reachable from the journal (LOOK-8(a)) |

### 2.2 Why on by default

**[J]** The alternative is off by default, discoverable in Settings. That makes the feature one almost nobody finds, and D20 plainly wants it seen. Three points about on-by-default:

- **Article 4's "no pre-ticked boxes" is not engaged.** The clause reads *"Employ **no dark patterns**: no false urgency, no confirm-shaming, no pre-ticked boxes, no deliberately buried settings, no engagement mechanics designed to exploit compulsion."* A pre-ticked box is a pre-selected **agreement**. A display preference that ships on is not the user agreeing to anything. With the privacy concern withdrawn, no fact carries a consent question that a default could pre-answer. **This is my reading of the clause, and I say so.** It is the kind of interpretive claim Condition 6 lets another seat re-derive.
- **"No deliberately buried settings"** is met because the control that turns headlines off sits **on the headline itself**, at most two taps from Off, as well as in Settings (HEAD-5).
- **Turning it off is final.** It is never re-offered, and nothing counts or reacts to it (ONB-1's no-punishment principle, applied here).

### 2.3 Why the static line is the default, and not the ticker the CEO described

This is **judgment, not a block**. The ticker is compliant if HEAD-9 to HEAD-11 are met, and the CEO may make it the default. My reasons for proposing the line:

1. **A ticker carries a standing accessibility duty that a static line does not.** WCAG 2.2 SC **2.2.2 Pause, Stop, Hide (Level A)**: *"For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is essential"* [E, W3C Understanding 2.2.2]. A home-screen ticker meets all three conditions, so a pause control must be on screen whenever it moves. W3C's own example of such content is *"scrolling stock tickers"* [E, same]. WCAG2ICT says 2.2.2 *"applies directly as written"* to software, replacing "web page" with "non-web document or software" [E, WCAG2ICT]. **A line that changes only on open, and never while displayed, is not moving or auto-updating content, so 2.2.2 does not engage** [I, from the SC's own conditions].
2. **Moving text is the hardest text to read.** W3C again: *"Content that moves or auto-updates can be a barrier to anyone who has trouble reading stationary text quickly as well as anyone who has trouble tracking moving objects. It can also cause problems for screen readers"* [E, W3C Understanding 2.2.2]. The default should suit the widest range of readers.
3. **Motion competes for the eye on every open, and that is where a headline starts to become an engagement mechanic** [J]. C1-O11's line is *"anything that reaches for the user's attention"*. A ticker on a launch screen gets closer to that line than static text does.
4. **It is cheaper.** The line is the fallback the ticker needs anyway (§7), so building the line first costs nothing extra.

### 2.4 Why "once a day, fixed order" and not "a new fact on every open"

**[J]** A new, unpredictable fact on every open is a small variable reward for opening the app, which is the mechanism slot machines use. It is the most direct route by which this feature could become *"engagement mechanics designed to exploit compulsion"* (Article 4) without any bad intent. Two limits remove the reason to reopen the app just to see what comes up: at most one change a day, and a **fixed** cycle. There is also no novelty signal ("new", a dot, a highlight, an entry animation) (HEAD-8).

---

## 3. Which facts are eligible

### 3.1 The rule: a fixed catalogue of templates, nothing generated freely

Every headline is rendered from **one of a fixed, enumerated set of templates** in the string table. This is the design choice that lets QA check everything else in this note: QA can list every sentence the slot can ever produce. **Adding a template is a requirements change** under `requirements.md` §24, reviewed by UX against §4 and §5.

### 3.2 The v1 catalogue

Thresholds are in §5. Example venue names are illustrative.

| # | Template (example rendering) | Source data |
|---|---|---|
| **T1** | *"You rate pubs 4.1 and cafés 3.2, across 23 and 11 rated visits."* (two categories), or *"You rate cafés 3.2, across 11 rated visits."* (one) | True mean of the user's ratings by venue category |
| **T2** | *"Your most-visited place: The Eagle, 41 visits recorded since March 2023."* | Visit count per venue |
| **T3** | *"Three years of The Eagle. Your first visit was in March 2023."* | First-visit date plus a visit in each year of the span |
| **T4** | *"Sundays at The Eagle, since 2023."* | Weekday concentration over a long span |
| **T5** | *"A year ago today: your first visit to Fitzbillies."* | First-visit anniversary (1, 2, 3 … years) |
| **T6** | *"Your highest-rated café: Fitzbillies, ★ 4.6 from 9 visits."* | VPAGE-11 weighted order to **select**. True mean and count to **display** |
| **T7** | *"You've rated The Eagle 3, 4, 4, 5: going up."* | VPAGE-10's trend rule, unchanged |
| **T8** | *"Your journal goes back to March 2024: 64 places."* | Earliest entry date and distinct venues |
| **T9** | *"The place you've known longest: The Eagle, since March 2021."* | Earliest first-visit among venues still visited in the last 12 months |

**A note on the CEO's own example.** *"Three years of Sunday roasts at The Eagle"* is the register the CEO wants, and T3 and T4 reach it. **The words "Sunday roasts", though, are not something the journal knows.** A template can know the place, its category, the day and the span. It cannot know what the user ate or drank. So the headline **never asserts an activity the journal does not record** (HEAD-4(d)). *"Sundays at The Eagle, since 2023"* is warm and true. *"Sunday roasts"* would be invented. The same rule keeps any template from inferring drinking.

### 3.3 Excluded, and the ground for each (none is the withdrawn privacy ground)

| Excluded | Ground |
|---|---|
| **Companion names** (CONF-19) | **Other people's personal data, not the user's.** The CGO's household-exemption ruling on companions is still open (`requirements.md` §22 item 14), and LOOK-7 excludes companions from the recap image on the same ground. The CEO withdrew the concern about *the user's* information on screen, and I do not read that as reaching third parties. **The CEO may widen this after the CGO ruling.** It is a one-template change |
| **Note text, quoted** | Two grounds, neither of them privacy. (1) **It cannot be reviewed.** The catalogue can only be checked because every sentence is a template, and a quoted note could say anything. (2) **Unbidden resurfacing of the user's own writing can hurt** [J]: a note about someone who has since died, or about an ex. A fact about a place is gentler than the user's own words about that night. Overturned by: usability evidence that people want it, plus a design in which the user marks notes as eligible |
| **The home inference and anything from LOOK-1 that is not a venue** | Not a fact about a place. Headlines are about venues, ratings and time. *"You spent 400 nights at home"* is a statement about the user's life with no memory in it |
| **Durations summed** (*"212 hours at The Eagle"*) | **Volume**: §4. On a product that records nights out, cumulative hours in pubs edges towards exactly what the refinement names |
| **Any count over a recent window** (*"this week"*, *"this month"*) | **Volume and rate**: §4 |
| **Any consecutive-period run** | **Streak**: §4 |
| **Anything about pricing, the trial, lapse, the recap, new features, tips, rating prompts or sharing** | **The slot is not a message channel.** HEAD-7 |

---

## 4. Memories, never volume

### 4.1 The rule, as the CEO set it, and the test that makes it checkable

The refinement: *"Warmth is permitted; the prohibition is on **celebrating frequency or volume**… rewarding more of the behaviour is the mechanism of a streak, which Article 4 bars, and on a product that records nights out it edges towards encouraging drinking."*

The Article 4 clause behind it: *"no engagement mechanics designed to exploit compulsion."*

**A test QA and an implementer can apply without me** [J, this seat's operationalisation of the CEO's rule]:

> **Warmth may attach to a place, a span of time, a date or a ritual. It never attaches to a number.** A count may appear as a plain fact (*"41 visits recorded"*). It is never the subject of praise, a milestone, a record, a rank, a rate per period, a run of consecutive periods, or a comparison with another period. **If the user could "beat" it or "break" it, it is out.**

The last sentence is the sharpest test. Nobody can beat "since March 2023", and nobody can break "Sundays at The Eagle". A user can beat "5 pubs this week" next week, and can break "4 Fridays in a row".

### 4.2 Examples on both sides of the line

**Permitted: memories, places, spans, rituals, plain facts**

| Phrasing | Why it is on this side |
|---|---|
| *"Three years of The Eagle. Your first visit was in March 2023."* | Warmth attaches to a span. Nothing to beat |
| *"Sundays at The Eagle, since 2023."* | A ritual, described |
| *"A year ago today: your first visit to Fitzbillies."* | A memory, dated |
| *"The place you've known longest: The Eagle, since March 2021."* | A span |
| *"Your most-visited place: The Eagle, 41 visits recorded since March 2023."* | A count stated as a fact about a place, with no praise |
| *"You rate pubs 4.1 and cafés 3.2, across 23 and 11 rated visits."* | The CEO's own example. It contrasts places, not periods or people |
| *"Your highest-rated café: Fitzbillies, ★ 4.6 from 9 visits."* | A judgment the user made, reported back |
| *"You've rated The Eagle 3, 4, 4, 5: going up."* | A trend in the user's opinion of a place (VPAGE-10), not in how much they go out |
| *"Your journal goes back to March 2024: 64 places."* | A span, with a count as a plain fact |
| *"Fitzbillies has been one of yours since 2022."* | Warmth about belonging to a place, not about frequency |

**Prohibited: volume, rate, runs, records, comparisons, urgency, nudges**

| Phrasing | Why it is out |
|---|---|
| *"You've been out 3 times this week!"* | **The line not to cross**, per the brief. A count over a recent window, celebrated. It sets a pace the user can match or miss |
| *"5 pubs this week — a new record!"* | The refinement's own example. Volume, record, celebration |
| *"4 Fridays in a row at The Eagle"* | A consecutive run. A streak by construction. Breakable |
| *"Your busiest month yet"* | A comparison of the user's own periods by volume, with a record framing |
| *"More nights out than last month"* | A comparison between periods, by volume |
| *"Your 100th visit to The Eagle!"* | A milestone. Celebrates the number, not the place |
| *"You've spent 212 hours at The Eagle"* | Cumulative volume. On a nights-out product it edges towards encouraging drinking |
| *"You're a proper regular at The Eagle"* | A label earned by frequency. It praises volume dressed as identity |
| *"You're in the top 10% of pub-goers"* | Comparison with others. Also uncomputable: there is no telemetry (PRIV-8) |
| *"12 days since you last visited The Eagle"* | An absence count. Reads as an obligation to return |

**Also prohibited, for reasons other than volume** (HEAD-7, HEAD-8):

| Phrasing | Why it is out |
|---|---|
| *"BREAKING: a new favourite pub"*, or any "NEW", red or flashing treatment | False urgency. The news-channel **typography** is permitted. The news-channel **urgency conventions** are not |
| *"3 more rated visits to unlock café stats"* | A goal and an unlock. It turns a threshold into a target |
| *"Your September recap is ready"* | LOOK-3(a) already forbids any banner that announces the recap |
| *"Rate last night's visit"* | A prompt. The slot is not a nudge channel |
| *"Share your headlines"* | LOOK-6, which is BLOCKING |
| *"Subscribe to keep your headlines"* | The slot is not a commerce channel. It is also false, because headlines are entitlement-blind (HEAD-14) |
| *"You rate cafés 5.0"* (from one visit) | Small numbers: §5 |
| *"You've been going to The Eagle for three years"* (last visit two years ago) | Asserts a continuity the journal does not show: §5.4 |

### 4.3 "Comparative", made precise

D20 as first recorded said *"never … comparative"*, and LOOK-8 says *"no … comparisons"*. The CEO's founding example compares pubs with cafés. The precise rule, **as this seat reads the intent** [J]: **forbidden** are comparisons with anyone else, and comparisons between the user's own time periods (this month against last, this year against last). **Permitted** are contrasts between places or kinds of place within the user's own ratings. The first group rates the user as a performer. The second describes their taste.

### 4.4 On "is it cheesy?"

**[J]** A headline earns its place when it tells the user something true that they had half-forgotten. It becomes cheesy when it performs excitement about that fact. So the design direction is a **newspaper masthead, not a rolling-news ticker**: a quiet kicker label ("From your journal"), a well-set sentence, and no exclamation marks, emoji, red, "BREAKING" or animation on arrival. That register fits a product called Haunts and suits the CEO's "Three years of…" example. It also makes the Article 4 line easier to hold, because a calm register has no volume to turn up. **Only a clickable prototype put in front of five to eight people can settle this properly** (§10).

---

## 5. Small-numbers honesty

### 5.1 The principle: selection carries a higher bar than display

D19(a) as written into VPAGE-6 lets a venue page show *"★★★★★ 5.0 · 1 visit"*, because the user navigated there and the count sits beside the number. **A headline is different, because the app chose it.** Choosing *"You rate cafés 5.0"* to show the user on opening the app amounts to an editorial claim that the figure means something. So headlines apply thresholds to **selection**, and every figure still carries its count, as VPAGE-6 requires. **The displayed number is always the true mean. The weighted score is never shown** (VPAGE-6(c), VPAGE-11(e)).

### 5.2 Thresholds (proposed [J], as named constants the PM/BA may tune)

| Template | Threshold before a fact is eligible | Reasoning |
|---|---|---|
| **T1** category mean | **≥ 5 rated visits in the category, across ≥ 2 distinct venues**. For the two-category form, both categories must qualify | Five keeps a single bad night from defining a category. Two venues stops one café posing as "cafés" |
| **T2** most-visited | **≥ 5 visits**, and a **strict leader**. On a two-way tie, name both. On a wider tie, the template is ineligible | "Most-visited" is false if it is shared |
| **T3** "N years of X" | First visit ≥ N years ago **and at least one visit in each of those N years** | "Three years of" asserts continuity. The check makes it true |
| **T4** weekday ritual | **≥ 6 visits on that weekday, ≥ 50% of visits to that venue, spanning ≥ 12 months** | A ritual needs a pattern and a span. Six Sundays in one summer is not "since 2023" |
| **T5** anniversary | First visit exactly N years ago today, N ≥ 1 | A date is a date. No small-numbers issue |
| **T6** top-rated | **Selected by VPAGE-11's weighted order, C = 3**, from venues with **≥ 3 rated visits**. Shows the true mean and count | D19(a) exists for exactly this: one five-star visit must not headline as the best place |
| **T7** trend | **VPAGE-10 unchanged:** no direction from fewer than three rated visits | Reuses the PM/BA's criterion |
| **T8** journal span | ≥ 1 entry, dated ≥ 30 days ago | A journal a week old has no span worth stating |
| **T9** known longest | The venue has a visit in the last 12 months and a first visit ≥ 12 months ago | Otherwise "known longest" describes a place the user has left |

### 5.3 What counts, and the words that keep counts honest

- **Every computation is over the complete entry set** (Condition 8.6: *"Aggregate and derived views… compute over the **complete** set of the user's entries, or state plainly on their face that they are partial"*). That includes seeded entries (ONB-2), imported entries (DATA-15) and entries written in any entitlement state (VPAGE-4).
- **Counts are phrased as recorded** (*"41 visits recorded"*), not as life-facts (*"you've been 41 times"*). Capture gaps (DEF-5) mean the journal can under-count real life, and a headline is too short to carry VPAGE-3's partiality statement. **Tapping the headline opens the self-portrait, which does carry it in body text** (VPAGE-3(b)'s standard). [J] "Recorded" costs one word and keeps the claim true.
- **Unrated visits count toward visit totals and never toward rating means.**

### 5.4 Continuity claims

*"You've been going there for three years"* (LOOK-8's example and the CEO's original D19 phrasing) says the user **still** goes. For a place last visited two years ago, it is false. The rule: **spans are stated with their start date** (*"since March 2023"*), and *"N years of X"* needs a visit in each of the N years (T3). This is Article 1.3 (*"Honest by default"*) applied to a sentence the app writes about the user's life.

---

## 6. Before there is enough data

A new user in the two-week trial almost always has no eligible fact. They will have **one or two visits** (`ux-note-pricing.md` §5.3), below every threshold in §5.2.

**The design: the slot does not exist until one fact qualifies.** Zero height, no border, no placeholder. In particular:

- **No teaser, progress indicator or countdown to headlines** (*"Headlines appear after 5 rated visits"*, *"2 of 5"*, a greyed empty card). Each of these turns a threshold into a goal, which is the §4 test failing before the first headline has appeared.
- **Where the thresholds are explained, it is as documentation, not as a counter.** The headline options in Settings may say, in body text, what the headlines are and that they appear *"once your journal has enough in it to say something true"*. They never say how far the user has got.
- **The self-portrait screen's own empty state** (LOOK-8) says plainly that there is not enough yet. It says so there because the user went to look.
- **Seeded (ONB-2) or imported (DATA-15) entries can make a headline eligible during the trial.** That is correct: they are entries.
- **The first headline appears without ceremony.** No entry animation, "new" marker, coach-mark or tooltip. The kicker "From your journal" and the options control on the element (HEAD-5) explain it in context.
- **ENT-9's trial and lapse statuses keep their positions.** State 1's static line stays in the home header. State 2's banner stays at the top of the queue. Where both exist, the headline sits below them and never displaces them.
- Headlines usually first appear after the trial. For many users that will be in the unpaid, read-only state. **Headlines are entitlement-blind** (VPAGE-4) and appear identically in every state (HEAD-14).

---

## 7. Motion and accessibility

**Baseline:** Constitution v1.3 Article 4: *"Meet accessibility standards (**WCAG 2.2 AA** as the working baseline, read through **WCAG2ICT** where the product is native software rather than a web page, since WCAG is written for the web)."*

### 7.1 What is required by the baseline, and what is required by the CEO

| Requirement | Source | Blockable by this seat? |
|---|---|---|
| A pause, stop or hide mechanism for the moving ticker | **SC 2.2.2, Level A** [E], applied to software *"directly as written"* by WCAG2ICT [E] | **Yes.** Level A is within the AA baseline, so a ticker without a pause mechanism fails the accessibility baseline under the charter's block |
| Reduce-motion detected and applied automatically | **The CEO's refinement**, point (2). **SC 2.3.3 Animation from Interactions is Level AAA** [E], so the baseline does not carry it, and a ticker that starts on its own is arguably not "triggered by interaction" in any case [I] | **No.** It binds as a **CEO decision**, which by `requirements.md` §1's definition makes it BLOCKING in requirements. That priority comes from the CEO's decision, not from a UX block. I record the difference rather than stretching the baseline |
| Text resizes to 200% without loss | **SC 1.4.4, AA** [E] | Yes |
| Contrast 4.5:1 for headline text | **SC 1.4.3, AA** [E] | Yes |
| No information by colour alone | **SC 1.4.1, A** [E] | Yes |
| Focus not hidden behind the slot | **SC 2.4.11, AA** [E], which is why the slot scrolls with content and is never a sticky overlay | Yes |
| Targets at or above the minimum (the pause control, the options control) | SC 2.5.8, AA, carried by **A11Y-5**. I did not re-retrieve its text this session; the retrieval of 2026-09-18 is recorded in `ux-note-pricing.md` §10 | Yes |

### 7.2 Automatic fallbacks: when the ticker becomes the line

When the user has chosen **Ticker**, it renders as the **Line** (static, with no motion of any kind) whenever **any** of these is true, and it re-evaluates live when a setting changes:

1. **iOS Reduce Motion is on.** UIKit exposes `isReduceMotionEnabled`, *"A Boolean value that indicates whether the Reduce Motion setting is in an enabled state"* [E, Apple].
2. **Android "Remove animations" is on.** This is the accessibility setting, not only the developer option. **See the trap at §7.3.**
3. **A screen reader is running** (VoiceOver or TalkBack). React Native exposes `isScreenReaderEnabled()` and a `screenReaderChanged` event [E, React Native]. Moving text cannot usefully be read by a screen reader. W3C: *"It can also cause problems for screen readers"* [E].
4. **The text size is in the accessibility range** (iOS larger accessibility sizes, or the Android equivalent). **[J]** A ticker at very large text shows only a few words at a time. The static line wraps and shows all of them.

**The options screen says why, in body text**, when the user has picked Ticker and a fallback is active. For example: *"Your phone is set to reduce motion, so headlines stay still."* The choice is still honoured the moment the setting changes back.

### 7.3 The implementation trap on Android, and why it needs a device test

React Native's own documentation for `isReduceMotionEnabled()` says: *"On Android, it reflects the 'Transition Animation Scale' setting in 'Developer options' — when set to 'Animation off', this returns `true`"* [E, React Native docs]. **That names a developer setting, not the accessibility switch an ordinary user would turn on.**

A reported React Native issue says: *"When removing animations through 'Android settings' -> 'Accessibility' -> 'Remove animations', it doesn't seem to result in `AccessibilityInfo.isReduceMotionEnabled()` returning `true` or the change event to fire"* [E, GitHub issue #31221, **single source**]. The issue is **closed**. Its page as retrieved **shows no fix, version or linked PR**, so I cannot say whether current React Native is affected. **I am flagging it as unresolved, not asserting it is still broken.**

A secondary source says the accessibility setting sets `ANIMATOR_DURATION_SCALE` to 0, and gives a native check against `Settings.Global.ANIMATOR_DURATION_SCALE` [E, eevis.codes, **secondary and single source**; not confirmed against Android's own documentation this session].

**Consequence, as a requirement rather than a design guess:** HEAD-10(b) requires the fallback to be verified **on a physical Android device with Settings → Accessibility → Remove animations switched on**, and **not** through Developer options. If the React Native call misses it, the Engineer adds a native check (CTO to choose the mechanism). **Owner: Engineer, verified by QA.** This is exactly the kind of defect no telemetry would ever reveal (`ux-note.md` §5.8).

### 7.4 The ticker's own controls (for users who have not set reduce-motion)

- **A visible pause control** sits on the ticker whenever it moves. It is labelled *"Pause headlines"* for assistive technology, meets A11Y-5, is separate from the headline text, and never needs to hold focus to keep the ticker paused. W3C: a pause mechanism *"must not monopolize focus"* [E, Understanding 2.2.2, as rendered by the retrieval tool; paraphrase-level].
- **Paused stays paused** across launches until the user resumes it. [J] A pause that resets on every open is a pause the user has to keep performing.
- **The ticker stops by itself after one full pass per open**, then rests showing the first fact. It is still pausable during that pass. [J] This keeps the news-channel feel on arrival without motion running continuously beside the user's journal. The number of passes is a named constant. The CEO may prefer continuous looping, which is compliant with the pause control present.
- **Speed is a named constant**, set slow, and UX signs it off on a device.
- **Tapping the headline text opens the self-portrait.** Pausing is a separate control, so the two actions are never confused.

### 7.5 Screen-reader behaviour

- **Line:** one accessibility element. Its label is the full sentence in spoken English (*"From your journal. Three years of The Eagle. Your first visit was in March 2023."*). Its role is button, with the hint *"Opens your self-portrait"*.
- **Card:** one element per fact, in reading order, followed by the options control.
- **Ticker:** never exposed as moving text. With a screen reader running it is the Line (§7.2). If it is ever exposed while moving, its label is the **complete static text** of all facts, never the visible fragment.
- **Never a live region, and never announced.** The content does not change while displayed, so there is nothing to announce. **SC 4.1.3's status-message pattern (A11Y-7) must not be used here.** Announcing a headline on open would turn it into a spoken push.
- **Focus order:** the ENT-9 status (when present), then the headline, then the headline options control, then the timeline or queue.
- **PRIV-7** (CUT-LINE): if the abbreviated-labels setting ships, headline labels follow it. That is the user's own choice about speaking places aloud, not a gate.

### 7.6 Dynamic Type and layout

- **No fixed height and no truncation.** The line wraps at every size. Venue names never truncate (A11Y-4: *"the venue name is the identity of the entry"*).
- **The slot scrolls away with the content**, so at the largest sizes it never permanently occupies the top of the screen or hides a focused element (SC 2.4.11).
- **The Card at accessibility sizes shows one fact**, not three, so the journal stays reachable below it [J].

---

## 8. The app-switcher snapshot and the other surfaces

**The CEO's one kept precaution:** *"except the app-switcher preview, which banking apps blur and so should Haunts."*

**iOS.** Apple: *"After your app enters the background and your delegate method returns, UIKit takes a snapshot of your app's current user interface. The system displays the resulting image in the app switcher"*. Also: *"If your interface contains such information, remove it from your views when entering the background"* [E, Apple, *Preparing your UI to run in the background*]. The requirement is that the headline is **removed or covered before the snapshot**. **One nuance I hold as [K], not verified this session:** the app switcher can show the app while it is *inactive*, before it has entered the background, so the cover should go up when the app resigns active, not only on entering the background. HEAD-12's device test settles this whichever way it falls.

**Android.** `setRecentsScreenshotEnabled(false)`: *"indicates to the system that it should never take a screenshot of the activity to be used as a representation in recents screen… the system may use the window background of the theme instead"*, API 33 onward. Unlike `FLAG_SECURE`, it does **not** stop the user taking their own screenshots [E, Android reference as mirrored at Microsoft Learn under the AOSP CC-BY licence. **The mirror is secondary**; Google's own page did not return the method text on retrieval]. **Two consequences for the CTO:**

1. On a single-activity React Native app, this hides the **whole app** in Recents, not just the headline. That matches what banking apps do, and I consider it acceptable [J].
2. **Below API 33 this call does not exist.** The fallback is `FLAG_SECURE` [K], which also blocks the user's own screenshots of their journal. That is a real cost to the user, and it is the CTO's call against Haunts' minimum Android version, **which I have not found stated in any artifact I read.**

**One mechanism, shared with the heatmap.** LOOK-2(e) already requires the heatmap to stay out of the snapshot. **Build one privacy cover and use it for both** [J]. The simplest version covers the whole app, as banking apps do, which also removes the need to track which screen is showing.

**Other surfaces (HEAD-13).** These are push or out-of-app surfaces, not privacy gates: no headline in widgets, the lock screen, notifications, Live Activities, Siri or Spotlight suggestions (the app donates no headline text for indexing), onboarding, or any store or marketing asset made from real data.

---

## 9. Draft acceptance criteria, for the PM/BA to lift

**Proposed ID block: `HEAD-1` … `HEAD-16`**, as a new §8.2 under LOOK, or as the PM/BA prefers. The priority column follows `requirements.md` §1. Where I propose BLOCKING, the source column names the clause or CEO decision that makes it so. Where the ground is my judgment, I propose MUST and say so.

| # | Requirement | Acceptance criteria (QA-verifiable) | Priority | Source |
|---|---|---|---|---|
| **HEAD-1** | **Self-portrait headlines appear at the top of the home screen**, as the first content element after any ENT-9 status. They scroll with the content, **never sticky**, and **supersede LOOK-8(e) for this element only**. | (a) With eligible data, assert the headline renders at the top of the home screen, below any ENT-9 State 1 line or State 2 banner, and never above or in place of them. (b) Scroll; assert the headline scrolls away and no part of it stays fixed. (c) Assert LOOK-8(e)'s remaining exclusions hold for headlines (HEAD-12, HEAD-13). | **MUST** | **D20** and its refinement, CEO 2026-09-22/23 |
| **HEAD-2** | **Four appearances: Line (default), Card, Ticker, Off.** Line shows one fact. Card shows up to three (one at accessibility text sizes). Ticker scrolls all eligible facts. Off collapses the slot to zero height. | (a) Fresh install with eligible data: assert Line is active. (b) Select each appearance; assert it renders as specified and **the choice persists across relaunch and update**. (c) Off: assert zero height, no border, no placeholder, and the self-portrait still reachable from the journal (LOOK-8(a)). | **MUST** | **D20** — *"toggleable, with its appearance changeable"*. Default proposed by UX [J], §2 |
| **HEAD-3** | **Line and Card change at most once per calendar day**, at the first open of the day, **in a fixed cycle** through eligible facts. **Content never changes while displayed.** | (a) Open, background and reopen the app ten times in one day; assert the same fact each time. (b) Advance the clock a day; assert the next fact in the fixed order. (c) Hold the screen open across midnight; assert no change until the next open. (d) Assert the cycle order is deterministic for a given data set. | **MUST** | [J], §2.4: removes the variable reward for reopening. Article 4 — *"no engagement mechanics designed to exploit compulsion"* is the clause the design protects, but the specific mechanism is this seat's judgment |
| **HEAD-4** | **Headlines come only from the enumerated template catalogue (T1–T9)** and are computed on-device over the complete entry set. | (a) Assert the string table holds exactly the catalogue's templates for this slot, and that adding one fails a CI check unless the catalogue file is updated. (b) Assert every computation reads the same unfiltered query path as the venue page (VPAGE-3(c), VPAGE-4): one path, no entitlement filter. (c) Assert no network call during computation or display (PRIV-8). (d) **Assert no template asserts an activity the journal does not record**: no food, drink or activity words beyond the venue's index category. | **BLOCKING** for (b)–(c), **MUST** for (a) and (d) | (b) Condition **8.6** and VPAGE-4; (c) PRIV-8; (a) and (d) [J], §3.1–3.2 |
| **HEAD-5** | **Options are reachable from the headline itself and from Settings.** A labelled options control on the element opens appearance (Line/Card/Ticker/Off), "Leave this place out of headlines" and "Leave out a category". **Off is at most two taps from the home screen**, at equal weight with the other choices. | (a) Measure taps from the home screen to Off: ≤ 2. (b) Assert the same options exist in Settings. (c) Choose Off; assert nothing ever re-offers headlines: no prompt, badge, banner or "turn headlines back on" after any number of launches or updates. (d) Exclude a place; assert no headline names it and that the exclusion is listed and reversible in Settings. | **BLOCKING** for (a)–(c); **MUST** for (d) | Article 4 — *"no deliberately buried settings"*; ONB-1's no-punishment rule; (d) [J], a user choice, §3.3 and §11 |
| **HEAD-6** | **Memories, never volume.** Warmth may attach to a place, span, date or ritual, never to a number. **No headline praises, ranks, records, rates per period, compares periods, counts consecutive periods, or counts absence.** | (a) **String-table search over the headline templates:** assert zero occurrences of *"!"*, *"record"*, *"best ever"*, *"yet"* (as in "busiest yet"), *"in a row"*, *"streak"*, *"this week"*, *"this month"*, *"more than"*, *"less than"*, *"than last"*, *"top %"*, *"in the top"*, *"days since"*, *"regular"*, *"keep"*, *"don't"*, *"miss"*, *"unlock"*, *"milestone"*, *"th visit"* and emoji. (b) Fixture of a heavy week (10 visits in 7 days) and a 4-week Friday run; assert no headline references either. (c) Assert no template sums durations. (d) QA reads every template against §4.2's two tables and records the result in the release pack. | **BLOCKING** | **D20 refinement**, CEO 2026-09-23 — *"The rule: celebrate memories, never volume"*; Article 4 — *"no engagement mechanics designed to exploit compulsion"* |
| **HEAD-7** | **The slot carries self-portrait facts and nothing else.** No pricing, trial, lapse, subscription, recap announcement, feature announcement, tip, rating or review prompt, reminder, or sharing copy. Ever. | (a) Enumerate every data source that can populate the slot; assert it is only the template catalogue. (b) Run the full ENT-14 entitlement fixture set; assert the slot's content is byte-identical across every state for the same data. (c) Assert the recap period ending changes nothing in the slot (LOOK-3(a)). | **BLOCKING** | LOOK-3(a) — no *"banner… launch-time takeover announces, offers or celebrates"* the recap; LOOK-6(c); B1 (lifecycle announcements are static status in their own places, ENT-9); PRIV-6 |
| **HEAD-8** | **No novelty or urgency treatment.** No "NEW", "BREAKING", dot, badge, count, red or warning colour, flashing, entry animation or coach-mark, and nothing that marks a headline as unseen. | (a) Visual and string inspection of all four appearances. (b) Assert first appearance of the slot (thresholds newly met) renders identically to any later appearance. (c) Assert nothing records whether a headline has been seen. | **BLOCKING** | Article 4 — *"no false urgency"*, *"no engagement mechanics designed to exploit compulsion"* |
| **HEAD-9** | **The Ticker has a visible pause control whenever it moves**, separate from the headline text, labelled for assistive technology, meeting A11Y-5, and not requiring focus to stay paused. **Paused persists across launches.** The ticker **stops after one full pass per open** (named constant). Speed is a named constant signed off by UX on device. | (a) Assert the pause control is present and operable whenever the ticker moves, by touch, VoiceOver, TalkBack, Voice Control and Switch Control. (b) Pause, relaunch; assert still paused. (c) Assert motion stops after one pass. (d) Measure the control's target (A11Y-5). | **BLOCKING** for (a); **MUST** for (b)–(d) | (a) **WCAG 2.2 SC 2.2.2 (A)** — *"there is a mechanism for the user to pause, stop, or hide it"* [E], applied by WCAG2ICT *"directly as written"* [E]; (b)–(c) [J], §7.4 |
| **HEAD-10** | **Reduce-motion is detected and applied automatically.** The Ticker renders as the Line, with no motion of any kind, under iOS Reduce Motion or Android **Remove animations**, and re-evaluates live when the setting changes. The options screen states why in body text. | (a) iOS: enable Settings → Accessibility → Motion → Reduce Motion with the app open; assert the ticker becomes static without relaunch. (b) **Android, on a physical device: enable Settings → Accessibility → Remove animations (not Developer options); assert the ticker becomes static.** If `AccessibilityInfo.isReduceMotionEnabled()` misses it, the build fails this criterion until a native check is added (§7.3). (c) Assert the explanatory line appears on the options screen while the fallback is active. | **BLOCKING** | **D20 refinement (2)**, CEO 2026-09-23 — *"detected and applied automatically"*. BLOCKING **as a CEO decision** under `requirements.md` §1, **not** as a WCAG requirement: SC 2.3.3 is **AAA** [E] |
| **HEAD-11** | **The Ticker also falls back to the Line while a screen reader runs and at accessibility text sizes.** | (a) Start VoiceOver or TalkBack; assert the ticker is static and read as one complete label. (b) Set the largest accessibility text size; assert the Line, wrapped, with no truncation. | **MUST** | W3C Understanding 2.2.2 — moving content *"can also cause problems for screen readers"* [E]; SC 1.4.4 (AA) [E]; A11Y-4. The fallback as the chosen remedy is [J] |
| **HEAD-12** | **Headlines never appear in the app-switcher / Recents snapshot** on either platform. One privacy cover is shared with LOOK-2(e)'s heatmap. | (a) iOS: with a headline on screen, swipe to the app switcher **and** background the app; assert no headline text is visible in either image. (b) Android API 33+: open Recents; assert no headline. (c) Android below the minimum API that supports `setRecentsScreenshotEnabled`, if supported at all: assert the CTO's chosen fallback holds, and that the cost to user screenshots is recorded. (d) Assert the user can still take their own screenshot of the home screen on API 33+. | **BLOCKING** | **D20 refinement (1)**, CEO 2026-09-23 — *"except the app-switcher preview, which banking apps blur and so should Haunts"*; LOOK-2(e) |
| **HEAD-13** | **Headlines appear only on the in-app home screen.** Never in widgets, the lock screen, notifications, Live Activities, Siri or Spotlight suggestions, onboarding, or any store or marketing asset built from real data. | (a) Assert no widget, notification or Live Activity target references headline data. (b) Assert no headline string is donated to Spotlight, Siri or the platform's app-content index. (c) Assert onboarding screens render no headline. | **BLOCKING** for (a); **MUST** for (b)–(c) | (a) B1 and D19(d) — *"pulled, never pushed"*; (b)–(c) LOOK-2(a), ONB-1 |
| **HEAD-14** | **Small-numbers honesty.** Each template is eligible only at its §5.2 threshold (named constants). **Every figure is the true mean with its count.** T6 selects by VPAGE-11's weighted order (C = 3) and displays the true mean. Counts say "recorded". Spans state a start date. "N years of X" requires a visit in each of the N years. **Headlines are entitlement-blind.** | (a) One 5-star café visit: assert no café headline. (b) The VPAGE-11(a) fixture: assert T6 names the ninety-nine-visit venue and displays its true mean and count. (c) Five rated pub visits all at one venue: assert T1 is ineligible for pubs. (d) A venue first visited 3 years ago and last visited 2 years ago: assert no "Three years of" headline. (e) A two-way tie for most-visited: assert both are named. A three-way tie: assert T2 is ineligible. (f) Assert no weighted score appears in any headline string. (g) Assert identical headlines across trial, paid, lapsed and unknown entitlement states for the same data. | **BLOCKING** for (b), (f) and (g); **MUST** for the rest | (b), (f) **D19(a)** — *"The displayed stars remain the true mean; the weighting affects order only"*; VPAGE-6(c), VPAGE-11(e); (g) VPAGE-4; thresholds [J], §5.2; Article 1.3 — *"Honest by default"* |
| **HEAD-15** | **Before any fact qualifies, the slot does not exist.** No placeholder, teaser, progress, count, "N more to unlock" or empty card. Documentation of what headlines are may appear in the options screen as body text, never as a counter. | (a) Fresh install, a trial with two visits: assert zero-height slot and no headline-related string anywhere on the home screen. (b) Assert no string in the build expresses progress towards headline eligibility. (c) Seed five rated café visits across two venues (ONB-2); assert a T1 headline becomes eligible. | **BLOCKING** for (a)–(b); **MUST** for (c) | Article 4 — *"no engagement mechanics designed to exploit compulsion"*; §4.1's test (a threshold shown as progress is a goal); ONB-2 |
| **HEAD-16** | **Screen-reader and layout behaviour.** Line: one element, full sentence in spoken English, button role, hint *"Opens your self-portrait"*. Card: one element per fact. **Never a live region; never announced.** Focus order: ENT-9 status, headline, options, timeline. No fixed height, no truncation, contrast ≥ 4.5:1, nothing by colour alone. | (a) VoiceOver and TalkBack walkthrough: assert the labels and order. (b) Assert no accessibility announcement fires on open or on a headline change. (c) Largest accessibility size: screenshot with no loss (A11Y-4). (d) Measure contrast in light and dark. (e) Greyscale render: assert no information lost (A11Y-2). | **BLOCKING** | SC 1.4.3 (AA), 1.4.4 (AA), 1.4.1 (A), 2.4.11 (AA) [E]; A11Y-2, A11Y-4, A11Y-6; (b) [J], §7.5: an announced headline is a spoken push |

**Mapping to existing requirements, so nothing is double-specified:** HEAD-12 shares its mechanism with **LOOK-2(e)**. HEAD-14 reuses **VPAGE-6**, **VPAGE-10** and **VPAGE-11** without changing them. HEAD-7 extends **LOOK-3(a)** and **LOOK-6(c)** to a new surface. HEAD-16 is **A11Y-2/4/6** applied to the slot. **HEAD-1 supersedes LOOK-8(e) for one element** (§1.2), and the PM/BA should annotate LOOK-8 accordingly.

**Checklist addition for A11Y-10** (the per-release QA gate): add *"Headline ticker: Reduce Motion (iOS) and Remove animations (Android accessibility, physical device) both produce a static line."*

---

## 10. Negative findings: what would overturn each, and where I looked

The charter requires that *"any finding that something is infeasible, prohibited, unaffordable or not worth doing must state (a) what evidence or change would overturn it, and (b) where you looked."*

| Finding | Overturned by | Where I looked |
|---|---|---|
| **The ticker should not be the default** (§2.3) | Usability observation showing people read and like the ticker at least as well as the line, with no increase in reports of distraction; **or** the CEO simply choosing it. It is compliant with HEAD-9 to HEAD-11 met, so this is taste, not a block | WCAG 2.2 and Understanding 2.2.2 (retrieved); WCAG2ICT on 2.2.2 (retrieved); D20 and its refinement |
| **A new fact on every open is out** (§2.4) | Evidence that users do not reopen the app to see new headlines. **Unobtainable by design**, because there is no telemetry (PRIV-8), so only a moderated study could supply it | Article 4 text; `ux-note.md` §3 on habit mechanics; C1-O11's clarification of 8.4 |
| **Quoted notes are excluded** (§3.3) | Usability evidence that people want their own words resurfaced, **plus** a per-note eligibility mark so the user chooses which notes can appear, **plus** a QA method for unbounded content | LOOK-7 (excludes notes from the recap image on a different ground); DEF-1; my own §3.1 reviewability argument |
| **Companion names are excluded** (§3.3) | The CGO ruling at `requirements.md` §22 item 14 confirming the household exemption covers companion names shown in-app, and the CEO widening the catalogue | CONF-19, LOOK-7, D10(a), D11(a) |
| **"Sunday roasts" cannot be rendered honestly** (§3.2) | A data field in the journal that records what the user ate or did. None exists in DEF-1 | DEF-1; the D20 refinement's example |
| **Counts over recent windows are out entirely, even neutrally worded** (§4) | The CEO ruling that a neutral *"2 visits this week"* is a memory rather than volume. I read *"celebrating frequency or volume"* together with the mechanism the CEO names (*"rewarding more of the behaviour is the mechanism of a streak"*) as covering any recent-window count, because showing it daily is what invites matching it [J] | D20 refinement; Article 4; LOOK-3(b) |
| **Android reduce-motion detection may silently fail** (§7.3) | A React Native release note or source showing `isReduceMotionEnabled()` reads `ANIMATOR_DURATION_SCALE` or the accessibility switch on the version Haunts ships; **or** a passing HEAD-10(b) device test | React Native AccessibilityInfo docs (retrieved); GitHub issue #31221 (retrieved; closed, resolution not shown); eevis.codes (retrieved, secondary). **Not found:** Android's own documentation of "Remove animations" |

---

## 11. Disagreement, recorded once

**On sensitive venue categories.** I comply with the instruction not to gate facts behind an opt-in on privacy grounds, and **no criterion above does so.** I record one narrow disagreement, once, as the charter asks.

The banking analogy holds for a balance: it is the user's own number, and knowing it tells a bystander little about their life. It holds less well for **T2, T4 and T9 applied to a clinic, a place of worship or a sexual-health service**. *"Your most-visited place: [clinic], 14 visits recorded"* on a launch screen is a different kind of fact, and one the user never chose to headline. **The cheap mitigation I would have proposed** is to leave a short list of index categories (health, religious, social services) out of **headlines only**, by default, while keeping them fully present in the self-portrait, with one switch to include them.

**What I have written instead** is HEAD-5(d): a user-controlled "leave out a place / category" option, off by default, that gates nothing. That satisfies the instruction. It relies on the user finding the fact on screen before they can remove it. **This is judgment [J], and no clause of the Constitution supports it.** Article 4's data-minimisation clause governs *collection*, and nothing new is collected here. I am not blocking. The CEO may take or leave the default exclusion. This paragraph is the record that it was offered.

---

## 12. Cost, cut line, and handoffs

**Cost [J, not sized by the CTO]:** about **4–6 engineering days**. That covers the template catalogue and selection logic (1–1.5 days), the Line and Card (1 day), the Ticker with pause, fallbacks and the Android native check (1.5–2 days), the snapshot cover shared with LOOK-2(e) (0.5 day, or zero if the heatmap's is built first), and the accessibility pass (1 day). **No running cost.** All of it is on-device (Constitution 1.5 satisfied structurally). **None of it is in the 2,090-hour estimate**, just as the PM/BA recorded for LOOK-8.

**Cut line:** the **Ticker** is the most expensive single piece and the only one with a standing WCAG duty. If it is cut, Line, Card and Off still satisfy D20's *"appearance changeable"*. **Recorded so the cut is a decision rather than a discovery**, not recommended: the ticker is what the CEO asked for.

**Handoffs:**
- **PM/BA:** lift §9 as the `HEAD-` block. Annotate LOOK-8(e) as superseded for HEAD-1. Reword LOOK-8's example sentence (§1.2, §5.4). Add the A11Y-10 checklist line.
- **CTO:** the snapshot mechanism and Haunts' **minimum Android API** (§8; I found it stated nowhere). Whether a native reduce-motion check is needed (§7.3). Sizing.
- **Engineer and QA:** HEAD-10(b) on a physical Android device through the accessibility menu.
- **CGO:** none new. The companion-name ruling at §22 item 14 already covers what would widen T-catalogue eligibility.
- **UX (this seat):** sign off ticker speed, the masthead typography and the kicker label on a device build. **A five-to-eight-person prototype test** of Line against Ticker, and of whether the headlines read as warm or cheesy, is still the highest-value missing fact.

---

## 13. Evidence register

All retrieved by me on **2026-09-23**.

**Standards**
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/): levels and text of SC 1.4.1 (A), 1.4.3 (AA), 1.4.4 (AA), 1.4.10 (AA), 2.2.1 (A), 2.3.3 (**AAA**), 2.4.11 (AA). SC 2.5.8 and 4.1.3 text **did not render** in this retrieval. They are carried at A11Y-5/A11Y-7 from my retrieval of 2026-09-18 and not re-quoted here.
- [W3C: Understanding SC 2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html): the SC text for moving, blinking and scrolling content and for auto-updating content; *"scrolling stock tickers"*; the screen-reader and reading-speed sentence; the pause mechanism must not monopolise focus (paraphrase-level in the retrieval, so not quoted as verbatim above).
- [W3C: WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/): SC 2.2.2 *"applies directly as written"* to non-web software. The note that non-conforming content can interfere with use of the whole software. **No WCAG2ICT guidance on 2.3.3 was found** in the retrieval.

**Platforms**
- [Apple: Preparing your UI to run in the background](https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-background) (retrieved via the documentation JSON endpoint): the snapshot sentence and the "remove it from your views" sentence.
- [Apple: `UIAccessibility.isReduceMotionEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibility/isreducemotionenabled) (JSON endpoint): the abstract only. The change-notification name was not in the retrieved content.
- [React Native: AccessibilityInfo](https://reactnative.dev/docs/accessibilityinfo): `isReduceMotionEnabled` and its Android note (Transition Animation Scale in Developer options), `reduceMotionChanged`, `isScreenReaderEnabled`, `screenReaderChanged`, `prefersCrossFadeTransitions` (iOS only).
- [GitHub: facebook/react-native issue #31221](https://github.com/facebook/react-native/issues/31221): "Remove animations" not reflected. **Closed; resolution not shown. Single source.**
- [eevis.codes: Android, Animations and Reduced Motion (2022)](https://eevis.codes/blog/2022-12-12/android-animations-and-reduced-motion/): "Remove animations" and `ANIMATOR_DURATION_SCALE`. **Secondary, single source, dated 2022.**
- [Microsoft Learn: `Activity.SetRecentsScreenshotEnabled`](https://learn.microsoft.com/en-us/dotnet/api/android.app.activity.setrecentsscreenshotenabled?view=net-android-35.0), which mirrors [Android's reference](https://developer.android.com/reference/android/app/Activity#setRecentsScreenshotEnabled%28boolean%29) under the AOSP CC-BY licence: API 33, the Recents-only scope, the comparison with `FLAG_SECURE`. **Secondary mirror.** Google's own page returned no method text on retrieval.

**[K], carried openly and not load-bearing on any BLOCKING criterion without a device test behind it**
- That the iOS app switcher can show an *inactive* app before it enters the background (§8). HEAD-12(a) tests both paths.
- That `FLAG_SECURE` is the pre-API-33 fallback and blocks user screenshots (§8). This is the CTO's to confirm.

**Sibling Candour artifacts, read from disk 2026-09-23:** `decisions/2026-09-16-haunt-gate.md` (D10, D11, D13, D19, D20, the D20 refinement, C1-O11's clarification of Condition 8.4); `products/haunt/requirements.md` (sections cited throughout, including LOOK-8 and VPAGE-11 as they stood at commit `47c05e0`); `products/haunt/ux-note.md` §5; `products/haunt/ux-note-pricing.md` §4 and §10.

---

*Prepared by the UX / Design Lead seat under `roles/ux-lead.md`, read against `constitution.md` v1.3 where the two differ: the charter still names WCAG 2.1 AA, and the Constitution's 2.2 AA via WCAG2ICT governs, as flagged to the CGO in `ux-note-pricing.md` §4. This note prepares and flags. It does not certify (Constitution 6.1). Every default above is a proposal to the CEO.*

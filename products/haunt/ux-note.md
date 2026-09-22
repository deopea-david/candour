# UX and Article 4 note — Haunt

**Seat:** UX / Design Lead · **Date:** 2026-09-10 · **Commissioned by:** gate preparation, closing the gap recorded in `proposals/haunt/proposal.md` ("Accessibility: not yet assessed — no UX seat has looked at this")
**Input artifacts:** `proposals/haunt/proposal.md`, `research/haunt-brief.md`, `products/haunt/cost-sheet.md`, `products/haunt/feasibility-note.md`
**Status:** discovery/gate artifact. **Prepares and flags; does not certify** (Constitution 6.1). Kill/proceed/park is the CEO's decision (5.4), due **2026-10-07** per the proposal's corrected anti-drift date.
**Template note:** `pipeline/templates/` has no UX-note template. Structure follows the charter's named outputs — usability review notes, Article 4 conformance check, accessibility audit notes — and states the deviation rather than making it silently.

**Evidence:** tagged per `pipeline/evidence-standard.md`. Every [E] below was retrieved by me on **2026-09-10** unless it is explicitly marked as travelling from another seat's artifact, in which case the retrieving seat and date are named and I say I did not re-verify it. Four retrievals **failed** and are recorded as failures in §10 rather than backfilled from memory.

**The honesty statement that governs everything below.** I have run **no usability test, seen no prototype, and spoken to no user.** There is nothing to test — this product does not exist and no wireframe has been drawn. Every claim in this note about *what a standard requires* is [E]. Every claim about *what a real person will do* is [J] or [I], and I have not disguised the second as the first. Candour has no industry contacts (`pipeline/evidence-standard.md`), so the usual remedy — five people and a prototype — was not available at discovery. It is cheap, it is the single thing that would upgrade half this document, and I name it in §10 as the highest-value missing fact.

---

## 0. Summary

1. **The confirmation prompt must be a pull, not a push.** A notification that arrives because the app wants you to open it is an engagement mechanic, and Article 4 forbids those without qualification. The design that works is a queue you find when you open the app, with notifications **off by default** and one narrow carve-out (§1). Apple's own store rules point the same way: an app "may not require users to enable system functionalities (e.g. push notifications, location services...) in order to access functionality" [E].
2. **The "this venue isn't listed" path is necessary and not sufficient.** Absence is the *easy* failure. Overture's documented duplicates are the hard one [E], because a duplicate splits a user's accumulated record silently, forever, with no server to repair it. Three further features are required, not optional: **merge**, **rename in place**, and **sticky choice** (§2). I ask for the CTO's pre-gate spike to be re-specified to measure duplicate and junk rate, not just top-three hit rate.
3. **I do not have a design that makes private writing stick, and I do not believe an Article 4-compliant one exists.** Every mechanism that reliably drives journalling habit is a compulsion mechanic. My honest position is that the **rating** is the product and the **writing** is a field on it — which means the proposal's residual differentiator has to survive on ratings alone. That is a material finding for the gate and it points the same way the CVO's kill recommendation does (§3).
4. **Ordinary people cannot reliably hold an unrecoverable key, and the largest consumer deployment of this exact pattern has already retreated from it.** WhatsApp shipped password-or-64-digit-key E2EE backups in 2021 [E]; in October 2025 it added passkeys because "you have to remember your backup password or have the encryption key handy" [E]. The moment is designable and I design it in §4 — but the honest expectation is a stream of support contacts that **cannot be resolved by anyone**, and the CFO's support-labour assumption should be revisited.
5. **Accessibility: one item is architecturally hard, the rest are merely unaddressed.** The hard one is **map-primary navigation** — if any function is reachable only by touching a map, no amount of labelling fixes it (§5). I also flag a gap in the Constitution's own baseline: **WCAG 2.1 AA contains no target-size criterion** (2.5.5 is AAA [E]) and no accessible-authentication criterion; both arrived at AA in **WCAG 2.2** [E]. Conforming to the letter of Article 4's stated baseline would not require adequate touch targets or a pasteable recovery key.
6. **On the offline architecture, one pricing shape is clean, one is weak, and one cannot be built without a dark pattern.** One-off purchase: clean. Free + unlock: the CFO's compliant basis (capping metered lookups) **disappears with the meter**, and every remaining cap is a cap on the user's own words or on a capability that costs nothing. Free + subscription: **cannot be built honestly**, because the only thing that makes a lapse matter is locking a journal that sits on the user's own phone (§6).

**Blocks:** none active today — there is no requirements document and nothing to block. **Seven become live at build or release**, listed with their lifting conditions in §7, so the gate sees them before anyone designs anything rather than after.

---

## 1. The confirmation loop

This is the product's core interaction and its biggest usability risk, and the proposal is right to name it. Everything below assumes the CTO's capture layer: `CLVisit` objects carrying `coordinate`, `horizontalAccuracy`, `arrivalDate` and `departureDate`, delivered after the fact, sometimes without both times [E, retrieved by the CTO seat 2026-09-09 — [Apple, CLVisit](https://developer.apple.com/documentation/corelocation/clvisit); I did not re-retrieve, Apple's developer docs did not render for me today].

### 1.1 Plainly: is a confirmation prompt a notification?

**No. It is something the user pulls, and notifications are off by default.**

The reasoning is not aesthetic. A push notification in this product would fire because *the user went somewhere*, not because *the user wants to write anything*. Its frequency would therefore be set by how sociable the user is and how chatty the OS's visit detector is — two variables the user did not consent to and cannot see. An alert whose cadence the company controls and the user cannot predict, delivered to bring the user back into an app, is the shape Article 4 names: **"no engagement mechanics designed to exploit compulsion."**

The test I propose the PM/BA write into acceptance criteria, because it is checkable rather than a matter of taste:

> **Would this prompt still exist if Candour had no interest whatsoever in the user opening the app?**

A "capture has stopped working" alert passes that test — the user's expressed intent is being defeated without their knowledge. "You have 4 places to confirm" fails it. So does "You haven't logged anything this week." So does a red badge with a number on it, which is a nag with arithmetic.

Two independent supports for the pull design, both retrieved:

- **Apple's own store rules already forbid the coercive version.** App Store Review Guideline 4.5.4: *"Push Notifications must not be required for the app to function, and should not be used to send sensitive personal or confidential information."* [E, verbatim — [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)]. And 5.1.1(ii): *"Your app may not require users to enable system functionalities (e.g. push notifications, location services, tracking) in order to access functionality, content, use the app, or receive monetary or other compensation..."* [E, verbatim, same source]. Note what the second one does to the product: **manual entry cannot be a fallback mode, it is required by Apple**, because a user who declines location must still be able to use the app. That finding recurs in §2 and §6.
- **The OS has already converged on batch-and-pull as the humane pattern.** iOS ships Scheduled Summary — Apple's own help index carries *"Schedule a notifications summary for a specific time of day"* [E — [Apple, Use notifications on your iPhone or iPad](https://support.apple.com/en-us/108781); I could not retrieve Apple's detailed Scheduled Summary page, only the index entry naming the feature]. A notification a user has to reschedule into a summary is a notification that should not have been sent.

**The one carve-out, tightly bounded.** The CTO records that `Always` authorization arrives in two prompts, that the second can be declined while the app is not on screen, and that background capture then stops silently [E, CTO §1.1, retrieved 2026-09-09]. A product whose entire promise is "it remembers so you don't have to" failing silently is a genuine harm, not a growth opportunity. So: **one** local notification per authorization-loss *event*, never repeated for the same event, permanently dismissible, with the same message shown as a persistent in-app banner for users who have notifications off entirely. If the engineer cannot express the rule as "at most one per state transition," it is not this carve-out.

### 1.2 How often is too often — and who decides

**The app never decides.** Frequency is a user-set property whose default is zero. If a reminder exists at all it must be: created by the user, at a time the user picks, at most once a day, and switchable off **inside Haunt in one tap** without a trip to iOS Settings (Article 4: cancellation as easy as signup; the same principle applies to any switch the app turned on).

I want to be honest about the cost of this position rather than pretend it is free. **Confirmation accuracy decays.** "Were you here?" answered ninety minutes later is recognition; answered eleven days later it is recall, and recall of a Tuesday evening is poor [J, high confidence — this is a general property of episodic memory and I am tagging it as judgment because I did not retrieve a study for it]. A pull-only design therefore trades *data quality* for *not nagging*. I accept that trade and recommend the gate accept it too, because the alternative buys accuracy with the one mechanic Article 4 names by name.

What buys back some of the accuracy, legitimately:

- **Make the queue the home screen.** Opening the app *is* the confirmation surface. There is no separate "you have items" state to advertise, because the first thing the user sees when they open Haunt for any reason at all is the pile.
- **Put enough context in the row to make it recognition again**: the day and weekday, arrival and departure times, dwell duration in plain words ("about 2 hours"), the street, and the two or three candidate venues inline. The user should be able to answer without opening anything.
- **Do not ask a question the data cannot support.** Where `CLVisit` arrived without a departure time [E, CTO §1.1], the row says so ("we did not see you leave") rather than inventing a range.

### 1.3 The backlog: a week away, a festival, a holiday

This is where the design either holds or becomes the thing Article 4 forbids, so I will be concrete.

**Principle: an unconfirmed queue is not a debt, and must never be presented as one.** No count badge on the app icon by default. No "27 unconfirmed" banner. No red. No progress bar toward "all caught up", which is a completion mechanic wearing a helpful face.

**Required behaviours:**

| Situation | Required design |
|---|---|
| Normal use | Queue grouped by day, newest first. No badge. No count in the tab bar unless the user opts in. |
| A week away / a festival — dozens of candidates | Group by day with a day-level header; **"confirm all on this day"** and **"discard the rest of this day"** as equal-weight actions. Bulk discard must never be styled as the destructive/regretful choice. |
| Repeat visits to the same venue in one trip | Collapse into one row per venue per day with a visit count, expandable. Six coffee stops at the same festival bar is one decision, not six. |
| A long absence | Candidates **expire on their own.** Default 30 days, user-adjustable, stated in onboarding. Expiry is silent: no "we deleted 40 of your memories" message, which would be manufactured loss. |
| The user simply does not want the queue | A single setting: **"Do not ask me — I will add places myself."** Capture off, queue empty, product still works. This is also the App Store 5.1.1 path for a user who refuses location [E]. |

**Expiry deserves defending, because it is the counter-intuitive one.** A queue that never empties is a permanent reproach, and the standard fix — nagging until it clears — is the fix Article 4 removes. Silent expiry with a stated, user-visible rule is the only remaining option that does not either nag or accumulate guilt. It costs the user some genuinely forgotten visits. It is still the right trade [J].

**What I would not build, and why, so nobody has to re-litigate it during build:** streaks; "you're on a roll"; completion percentages; a "your timeline is 60% complete" meter; "you haven't written since Tuesday"; a weekly digest notification; a year-in-review push. Each is an engagement mechanic and each is prohibited by the same clause. Retrospective surfaces ("a year ago tonight", "your 6th visit here") are legitimate **only as things the user finds on opening the app** — the identical content delivered as a notification becomes a re-engagement mechanic. The content is not the problem; the delivery is.

---

## 2. Venue disambiguation on an offline index

### 2.1 What the data actually hands the UI

Overture's own documentation, retrieved today: *"Places is known to contain duplicates, a high junk rate, and low property completeness."* The confidence score is *"the primary tool for filtering potential junk data; it does not address duplicates or property completeness"*, and confidence values *"are not calibrated to be strictly comparable across providers"* and should be treated as *"a relative filtering tool rather than a precise probability"* [E, verbatim — [Overture Places guide](https://docs.overturemaps.org/guides/places/)].

Read that as a UI specification, because that is what it is [I]. A candidate list on a British high street will contain, simultaneously: the right venue; **two or three near-duplicates of the right venue** from different upstream providers; several genuinely different venues inside GPS error; and some junk. Confidence sorting helps with the junk and **explicitly does not help with the duplicates**.

The picker's radius is not tight either. The CTO records that visit monitoring works under reduced accuracy when the user declines precise location [E, CTO §1.1, retrieved 2026-09-09], and `CLVisit` carries a `horizontalAccuracy` the design is told to widen from. So the honest list is sometimes "everything within 500 metres," which on Oxford Street is a lot of everything.

### 2.2 The interaction, when the right answer is third

- **Never auto-select.** The proposal's own scope line — *"Nothing enters the timeline without confirmation"* — must extend to the venue, not just the visit. A pre-selected top candidate is a pre-ticked box, and Article 4 names those.
- **One row, three facts:** name, category in words a UK user recognises ("Pub", not `pub.tavern`), and street plus distance in metres. Distance is the discriminator that actually resolves a high street; confidence is not, and must never be shown to the user as a number.
- **The "isn't listed" path is not at the bottom of the list.** It lives in the search field as a persistent affordance — as soon as the user types, the first row offered is *"Use 'The Eagle'"* — and it is repeated at the end of the list. A path that is a required feature must not be laid out like a fallback.
- **Under reduced accuracy, say so in the list header**, in words: *"Precise location is off, so this list covers about 500 m."* Presenting a wide, uncertain list with the confident chrome of a narrow one is a small dishonesty that will be read as a bug.
- **No map required to disambiguate.** See §5: if resolving a venue requires touching a pin, the core loop is unusable with VoiceOver.

### 2.3 The CTO's "not listed" path is necessary and not sufficient — three more required features

I am recording this as a disagreement with the CTO's framing (feasibility note §2.6), stated once, in writing.

Absence is the *benign* failure. The user types a name, and the entry is complete, correct and permanent. **Duplication is the malignant one**, and the "not listed" path does nothing about it. Concretely: a user picks "The Eagle" (provider A) in March and "The Eagle" (provider B) in June. Both rows are real, both are the same pub, and the product now believes the user visited two places once each rather than one place twice. Every downstream feature that gives this product its only long-term value — visit counts, "you've been here 6 times", the rating history that is the proposal's sole surviving differentiator — is silently wrong. There is **no server, no telemetry and no backfill**, so nobody at Candour will ever find out, and the user will discover it only as a vague sense that the app is not very good.

The three features that close it:

1. **Merge venues.** User-facing, reversible, reachable from any venue's detail screen: "this is the same place as…". Visits, notes and ratings move; the merge is recorded so it survives a dataset refresh. Without this, Overture's documented duplicate rate becomes the user's permanent data-quality problem [I from the [E] above].
2. **Sticky choice.** Once a user resolves a coordinate cluster to a venue, the next visit to that cluster offers that venue first, marked as the one they chose before. This is, in my judgment, **the single highest-value interaction in the whole product** [J]: it converts the disambiguation tax from per-visit to once-per-venue, and it is what makes a local regular's timeline pleasant instead of tiring.
3. **Rename in place, permanently.** The user's name for a venue outranks the dataset's, forever, and survives updates. This is already implied by the CTO's data-layer commitment that *"venue identity is a Candour-owned local row"* carrying the Overture GERS ID *"as an attribute, never as the only handle"* [E, CTO §3, retrieved 2026-09-09]; I am making the UI consequence explicit so it is not dropped as polish.

**A fourth hazard nobody has written down: dataset refresh.** The CTO plans to ship venue-index updates inside app updates (feasibility §6.4). An Overture release can rename, move, split or drop a venue. **A user's 2027 diary must not change because of a 2029 data release.** Requirement: once a venue row is referenced by a visit, its user-visible name and coordinate are frozen in the local store; refreshes add and update *unreferenced* rows only, and offer changes to referenced ones as an explicit, optional, reviewable action. This is a data-layer decision, cheap now, and a corruption incident later. It belongs in the PM/BA's acceptance criteria.

### 2.4 The pre-gate spike is measuring the wrong thing

The CTO asks for a 2-day spike on *"how often is the right venue in the top three candidates?"* (feasibility §8, item 4). That is a good spike with an incomplete metric. I ask for it to be re-specified, before the gate if the gate proceeds, to report four numbers over a sample of real UK venues:

| Metric | Why it decides something |
|---|---|
| Top-3 hit rate | The CTO's question. Decides whether the picker is usable at all. |
| **Duplicate rate within the top 5** | Decides whether **merge** is MVP scope or can wait. On Overture's own description of the data, I expect it cannot wait [I]. |
| **Junk rate within the top 5** | Decides how hard confidence filtering has to work, and whether the list is embarrassing on first run. |
| **Miss rate** (right answer absent entirely) | Decides how prominent the "isn't listed" path must be, and sets an honest expectation for the App Store description under Article 1.3. |

The research brief already flags UK-specific coverage as an **open item it could not close**, with its one coverage source a hobbyist blog, n=100, no per-country split [E, research brief §7.4 / E21, retrieved 2026-09-09 — [surprisedatespot.com](https://surprisedatespot.com/blog/comparing-overture-osm-restaurants/)]. So the spike is the only route to these numbers, and three of the four have UX consequences that are expensive to retrofit.

---

## 3. The writing habit — my honest answer is no

**There is no design that makes private writing stick, and I do not believe an Article 4-compliant one exists.** The brief invited me to say so if that was my answer, and it is. I want to set out why I think it, so the gate can disagree with the reasoning rather than with my confidence.

### 3.1 The evidence, and what it actually says

The load-bearing number travels from the research brief: on Letterboxd's own 2024 figures, ~96.4m reviews against 701m logged films — **about 14% of logs carry any writing at all**, and about 71% carry a rating [E, retrieved by the Research Analyst 2026-09-09 — [Letterboxd, 2024 Year in Review](https://letterboxd.com/journal/2024-year-in-review/); **I attempted to re-retrieve this today and the page returned HTTP 403.** The figure is therefore attributed, not re-verified by me, and I flag it as such rather than quietly repeating it].

What that number is evidence *of* matters. It is not "people don't like writing." It is: on the most successful log-and-rate product in existence, **with friend feeds, public profiles and a shareable year-end**, six of every seven logged items carry no writing. Writing is the minority behaviour under the *most* favourable conditions available.

Haunt proposes to remove those conditions and sell the residue. That is not a pessimistic reading; it is the arithmetic.

### 3.2 What is actually left to design with

With no audience, the mechanisms that reliably drive habit reduce to two families:

**(a) Lower the cost of writing.** Legitimate, and worth doing properly:
- The note field is *already open* on the confirm row — no second screen, no title, no "add a note" button to press first. One field, no ceremony.
- The rating is one tap and is never gated behind the note.
- Nothing is ever incomplete. An entry with a venue and a date is a finished entry. There is no empty-state copy implying otherwise, no "add a note to complete this", no greyed placeholder that looks like a task.
- Voice dictation is a first-class input, not an afterthought — a five-word thought said outside a pub is more likely to survive than the same thought typed on a phone in the rain [J].

**(b) Raise the value of re-reading.** Also legitimate, because it rewards writing that already exists rather than demanding more:
- Search across notes, and search that works offline (it has to — there is no network).
- "You have been here 6 times", with the notes stacked in one place.
- Retrospective surfaces — a year ago, this month last year — **found on opening the app, never pushed** (§1.3).

**What neither family does is create a habit in someone who does not already have one.** They make an existing habit cheaper and more rewarding. That is a real and honourable thing for a design to do, and it is not the same thing as the proposal's differentiator.

### 3.3 The mechanisms that would work, and why every one is barred here

I am listing them explicitly so the gate can see that this is a constrained problem and not a failure of effort. Each of these demonstrably drives journalling behaviour, and each is prohibited:

| Mechanism | Why it is barred |
|---|---|
| Streaks | Article 4 — engagement mechanic designed to exploit compulsion. Its whole efficacy *is* the compulsion. |
| Badges / achievements / levels | Same clause. |
| Daily or weekly reminder notifications, on by default | Same clause, plus §1. |
| "You haven't written in 5 days" | Confirm-shaming, named in Article 4. |
| Completion meters ("your timeline is 62% complete") | Manufactured incompleteness — a compulsion mechanic expressed as arithmetic. |
| Loss framing on expiry ("40 memories about to be lost") | False urgency, named in Article 4. |
| A social layer / sharing | Closed by explicit decision in the proposal, and the Research Analyst's reasoning for closing it — that it would be exercised for company reasons and justified with user reasons — is right. |

Remove all of those and what remains is: a nice place to write, that never asks you to. Some people will use it. Most people who install it will rate a few places, write two notes, and stop. **I would design it exactly that way anyway** — but I would not let the gate believe the design is going to change that outcome.

### 3.4 The consequence for the gate, stated as a finding

Three things follow, and the gate should weigh all three:

1. **The rating is the product; the note is a field on it.** The research brief reached this independently: the one-tap rating plausibly survives the loss of the audience, the writing almost certainly does not [E-derived, research brief §4, retrieved 2026-09-09]. If the design is optimised on that basis — and it should be — then the proposal's honest description ("Arc, plus a star rating") has to carry the entire commercial case on the star rating alone.
2. **Candour will never know whether this worked.** The architecture forbids analytics, deliberately and rightly. There is no funnel, no cohort, no "how many users wrote a second note." That is the correct trade for a privacy product, but it means "does the writing habit survive?" is a question this company has structurally disabled itself from answering after launch. It can only be answered **before** the build, by talking to people. It has not been.
3. **This finding points the same way the CVO's kill recommendation does.** I am not the seat that decides, and I am not casting a vote I do not hold. But the proposal names the writing as what it is selling, and the UX seat's honest answer is that design cannot make that stick without breaking Article 4. That belongs in the decision pack next to the other four kill criteria, not underneath them.

---

## 4. The passphrase

The CTO's constraint is right and I endorse it without reservation: Candour holds no key, the cloud is dumb storage, and the promise is true by construction rather than by trusting a platform's tiering [E, CTO §4.2, retrieved 2026-09-09]. The CTO also says the irreversibility *"must be stated in the app at the moment of setup, in the plainest possible words"* and that burying it in a help page would itself be the buried-settings dark pattern [E, CTO §4.2]. Agreed. Here is that moment, designed — and then an honest assessment of whether it is enough.

### 4.1 Can ordinary people be asked to hold a key they cannot recover?

**Mostly, no — and the best evidence available is that the industry has already conceded this.**

- **WhatsApp shipped exactly this pattern at consumer scale in 2021.** Users *"choose to secure the key manually or with a user password"*; with a password *"the key is stored in a Backup Key Vault"*; and *"neither WhatsApp nor the backup service provider will be able to access their backup or their backup encryption key"* [E, verbatim — [Meta Engineering, How WhatsApp is enabling end-to-end encrypted backups](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/)].
- **In October 2025 it added passkeys, and the stated reason is the friction:** *"The trouble with both is that you have to remember your backup password or have the encryption key handy while restoring the backup"* and *"With passkeys, you don't need to look for the password or the key"* [E, **single source** — [TechCrunch, 30 Oct 2025](https://techcrunch.com/2025/10/30/whatsapp-adds-passkey-protection-to-end-to-end-encrypted-backups)]. A product with billions of users spent four years and then engineered around the requirement. That is the strongest signal available on whether ordinary people can hold an unrecoverable key [I].
- **Apple, on its own end-to-end encrypted tier, does not ask people to hold a bare key either.** Advanced Data Protection offers three recovery routes — device passcode, a recovery contact, or a 28-character recovery key — and states plainly *"With Advanced Data Protection turned on, Apple doesn't have the encryption keys needed to help you recover your end-to-end encrypted data"* [E — [Apple, Advanced Data Protection](https://support.apple.com/en-gb/108756)]. Note the shape: the honest sentence about irrecoverability is paired with **redundant human-scale recovery routes**, not with a bare string.

So the pattern that works is not *"hold this key"* but *"put this key somewhere that already holds keys."* That is the design consequence, and it is the one Haunt should copy.

### 4.2 The moment, designed

Backup is **off**, and nothing has ever left the device. The user opens Settings and taps **Set up backup**. Four screens.

**Screen 1 — what leaves, and in what form.** Not a legal notice; a short list in body text.
> *Your journal is encrypted on this phone before anything is uploaded. What arrives in your iCloud is a single scrambled file. Candour never sees it, never receives it, and holds no key to it. Haunt makes no network calls of its own — this backup is the only thing it ever uploads.*
Actions: **Continue** / **Not now**. Equal weight. No colour-coded steering.

**Note on that copy, added after the proposal was corrected on 2026-09-10.** An earlier draft of this screen read *"Nothing else is sent — Haunt makes no other network calls, ever."* That is the same overstatement the Skeptic caught in the proposal at gate: platform-mediated, opt-in crash reporting is a transmission, user-authorised and routed to Apple rather than Candour, but a transmission [E — `proposals/haunt/proposal.md`, CVO correction of 2026-09-10]. The copy above is corrected to the substantiable form, and **§6.6 below carries the UI consequence**, because a claim this product makes in marketing has to be checkable inside the app.

**Screen 2 — the key, and the sentence.** The key is generated and shown. The honest sentence is **at the top, in ordinary body text, before the key**, not in a modal, not in red, not behind an "i":
> *This key is the only way to open your backup on another phone. If you lose it, the backup is gone — we cannot reset it, because we never had it. Your journal on this phone is not affected either way.*

Three actions of **equal visual weight**:
1. **Save to Passwords** (the iOS password manager) — offered first, because a key stored in the thing that stores keys is the design that survives contact with real people [J, and supported by §4.1's evidence].
2. **Print or save a PDF.**
3. **Copy.**

There is a **Not now**, and choosing it **cancels backup setup** rather than proceeding with an unsaved key. That is the honest coupling: the app does not get its backup switched on until the user has actually stored the thing that makes the backup useful.

**Screen 3 — verification, and a standards trap.** Verification must be *"paste it back, or confirm it is in your Passwords"* — never *"type characters 4, 9 and 17."* This is not a preference. **WCAG 2.2 SC 3.3.8 Accessible Authentication (Minimum), Level AA:** *"A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following"* — with the first exception being *"Alternative: Another authentication method that does not rely on a cognitive function test"* and the second *"Mechanism: A mechanism is available to assist the user in completing the cognitive function test"* [E, verbatim — [W3C, Understanding SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)]. **Paste must work.** Blocking paste in the key field — a depressingly common "security" habit — removes the mechanism and fails the criterion outright.

**Caveat I flag rather than bury:** 3.3.8 is a **WCAG 2.2** criterion. It does not exist in 2.1, which is the baseline Article 4 names. So under the Constitution as written I can recommend this but not block on it. See §5.1 and §7.

**Screen 4 — done, and then a status row that is not a nag.** Settings shows a permanent **Backup** row: last backup time, size, and *"Recovery key: saved to Passwords"* or *"Recovery key: not confirmed."* It is a status, in the place a user goes to look. It does not chase them. The CTO proposes *"a periodic, dismissible reminder to check the recovery code is stored somewhere real"* [E, CTO §4.2]; I would replace the periodic reminder with this always-visible status, because a recurring prompt is the shape §1 rules out and the status achieves the same thing without it.

**Explicitly barred from this flow (Article 4):** scare modals; confirm-shaming ("Are you sure? Your memories will be lost forever"); a pre-ticked "I understand" box; a default-on backup; any styling that makes **Not now** look like the wrong answer.

**One circularity to state out loud, per Article 1.3.** If the key is saved to Passwords and Passwords syncs via iCloud, then losing the Apple account loses both the backup *and* the key to it. The honest copy says so in one sentence on Screen 2 and recommends the printed copy as well. Saying it costs nothing; discovering it costs everything.

### 4.3 The support burden, with no server to fix anything from

Concretely: **every key-loss contact is unresolvable, by anyone, forever.** There is no admin console, no reset link, no escalation. The only honest reply is a three-part message — your backup cannot be recovered; your journal on your original device is intact; here is how to export it — and that reply is correct, complete, and will not satisfy the person receiving it.

Three consequences the gate should see:

1. **The volume is unknowable in advance and unmeasurable afterwards.** No telemetry means Candour cannot count key losses. The only signal will be the support inbox, which undercounts.
2. **The CFO's support assumption should be revisited for this flow specifically.** The cost sheet models support at *"2% contact rate/yr × 30 min"* [E, CFO §, retrieved by the CFO seat 2026-09-09, `products/haunt/cost-sheet.md`]. A 30-minute average is plausible for "how do I export?" It is not plausible for a contact where the answer is "your archive is gone and I cannot help" — those are longer, they recur, and a fraction become public one-star reviews on the only acquisition channel the product has [J]. I am not re-modelling the CFO's number; I am flagging that this specific flow is not the average contact and asking that it be modelled separately.
3. **The mitigation that actually matters is architectural, and the CTO already has it right:** the local store is *not* encrypted under this passphrase, so losing the key loses the backup and never the journal [E, CTO §4.2]. **I would block a design that changed that** (§7, B6). The plain export is the real disaster-recovery path, and it should be surfaced in the same support reply and in onboarding — not only as an Article 4 obligation but as the thing that makes key loss survivable.

**Bottom line for the gate.** This is buildable and it can be made honest. It cannot be made painless, and the App Store description should carry the "we cannot recover it" sentence too, not just the app — Article 1.3 makes limitations a marketing obligation, not only a UI one.

---

## 5. Accessibility — WCAG 2.1 AA on a map-and-timeline product

### 5.1 First, a gap in the baseline itself

Article 4 names *"WCAG 2.1 AA as the working baseline."* Two things about that need saying before any Haunt-specific finding, because they are Constitution-level and they affect every product Candour ever ships.

- **WCAG 2.1 AA contains no touch-target requirement.** SC **2.5.5 Target Size** — *"The size of the target for pointer inputs is at least 44 by 44 CSS pixels"* — is **Level AAA** [E, verbatim — [W3C, WCAG 2.1](https://www.w3.org/TR/WCAG21/)]. **WCAG 2.2** added SC **2.5.8 Target Size (Minimum)** — *"For functionality that can be operated using a single pointer, the target size is at least 24 by 24 CSS pixels"* — at **Level AA** [E — [W3C, WCAG 2.2](https://www.w3.org/TR/WCAG22/)]. A product could conform to the letter of Article 4's stated baseline with targets too small for a shaky hand.
- **WCAG 2.1 AA contains no accessible-authentication requirement either.** SC 3.3.8 (§4.2) is new at AA in 2.2, alongside 2.4.11 Focus Not Obscured (Minimum), 2.5.7 Dragging Movements, 3.2.6 Consistent Help and 3.3.7 Redundant Entry [E — [W3C, WCAG 2.2](https://www.w3.org/TR/WCAG22/)].
- Also worth the CEO knowing: **SC 2.3.3 Animation from Interactions is Level AAA in 2.1** [E, verbatim — W3C, WCAG 2.1] — so honouring Reduce Motion is not required by the stated baseline either. On a map product, that is the criterion I would least want to be excused from (§5.6).

**Recommendation to the CGO, for the CEO:** move the working baseline to **WCAG 2.2 AA**, or at minimum adopt 2.5.8, 2.5.7 and 3.3.8 by name. This is not a Haunt request — it is cheaper to fix in the Constitution once than to argue at every gate. It is an amendment and therefore Article 11 territory; it **strengthens** a customer-facing rule, so it is not a weakening amendment under 11.2.

**A second framing point, stated so nobody has to discover it during build:** WCAG is written for the web. Applying it to a native iOS app requires a mapping, and the practical route is Apple's accessibility APIs (VoiceOver labels/traits/values, Dynamic Type, Reduce Motion, Increase Contrast, Voice Control). I could not retrieve Apple's Human Interface Guidelines today — the pages are script-rendered and returned no body text [failure recorded in §10] — so **I make no [E] claim about Apple's own stated 44×44 pt convention**, and every requirement below is grounded in W3C text I did retrieve.

### 5.2 The map without sight — the one architecturally hard item

**SC 1.1.1 Non-text Content (Level A):** *"All non-text content that is presented to the user has a text alternative that serves the equivalent purpose"* [E, verbatim — W3C, WCAG 2.1].

The *equivalent purpose* of Haunt's map is "which places, when, and near what." That is fully expressible as a list — which is the good news. The bad news is the failure mode:

> **If any function is reachable only by touching the map, no amount of labelling fixes it.**

A screen-reader user cannot hit-test a pin cluster. Voice Control cannot name an unlabelled coordinate. A Switch Control user cannot pan. So the requirement is structural, not decorative:

- **Every function reachable from a map pin must be reachable from the timeline or venue list.** Confirming a visit, choosing among candidates, opening a venue, reading and editing a note, rating: all of it, list-first.
- The map is then **decoration over a complete list product**, and 1.1.1 is satisfied by the list rather than by alt text on a canvas.
- **SC 2.5.1 Pointer Gestures (Level A):** *"All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture"* [E, verbatim — W3C, WCAG 2.1]. Pinch-zoom is multipoint; pan is path-based. So: zoom in/out buttons, a "fit to visits" control, and list-based selection. **WCAG 2.2 SC 2.5.7 Dragging Movements (AA)** — *"All functionality that uses dragging movements can be achieved by another single pointer input method, unless dragging is essential"* [E, verbatim — W3C, WCAG 2.2] — says the same thing about pan more directly.

**Why this is architecturally hard rather than merely unaddressed:** list-first and map-first produce different navigation models, different data access patterns, and different screen inventories. Decided at the start it costs approximately nothing. Retrofitted, it is the same shape of problem the CTO describes for the export format — *"roughly 3–5 days as part of the initial data-layer work"* versus *"a multi-week job that usually ends in a lossy exporter nobody trusts"* [E, CTO §3]. **This is the one accessibility item on my list that is architecture. Everything else in §5 is cheap if it is a constraint on every workstream and expensive if it is a workstream.**

### 5.3 Location semantics for screen readers

**SC 1.3.1 Info and Relationships (A):** *"Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text"* [E, verbatim — W3C, WCAG 2.1]. **SC 4.1.2 Name, Role, Value (A)** applies to every control [E — W3C, WCAG 2.1].

The specific failures I expect in this product [J, from the interaction shapes described in the proposal]:

| Failure | Requirement |
|---|---|
| A timeline row that reads as "Confirm, button", with the venue name in an unassociated sublabel | Each row exposes **one** accessible label: *"The Eagle, Cambridge. Tuesday 3 March, 7:12pm to 9:40pm, about 2 hours. Rated 4 out of 5. Note: quiet upstairs room."* |
| Times read as ISO strings or raw numerals | Times and durations exposed as spoken English, not as the visual abbreviation |
| Distances read as "0.2" with the unit as a separate element | *"120 metres away"* as one label |
| A 5-star control read as "star, star, star, star outline, star outline" | A single adjustable control exposing value *"4 of 5"*, settable by increment/decrement, not five independent buttons |
| The candidate picker read as an undifferentiated list of names | Each candidate exposes name, category, street and distance in one label; the "isn't listed" option is a labelled control, not an icon |
| "Visit confirmed", "backup complete", "12 candidates found" announced by moving focus, or not at all | **SC 4.1.3 Status Messages (AA):** *"Status messages are programmatically determinable through role or properties"* [E, verbatim — W3C, WCAG 2.1] — announce without stealing focus |

Two Haunt-specific ones worth naming, because they are not generic:

- **A location record is sensitive spoken aloud.** VoiceOver reads on a speaker in public. A per-app setting to abbreviate row labels ("a venue, Tuesday evening") for users who want it is a two-hour feature and a genuine privacy affordance for exactly the user this product claims to serve [J].
- **Empty and degraded states must be honest to a screen reader too.** The CTO's authorization-downgrade surface [E, CTO §1.1] and my §2.2 reduced-accuracy header must be text in the accessibility tree, not a greyed visual.

### 5.4 Colour-only encoding of ratings

**SC 1.4.1 Use of Color (Level A):** *"Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element"* [E, verbatim — W3C, WCAG 2.1].

- **Filled versus outline stars differ in shape as well as colour — that passes.** A red→amber→green rating scale does not, and neither does a rating shown only as a coloured dot. Simple rule for the build: **every rating must be readable in greyscale and must also be present as text** ("4/5") somewhere on the row.
- **Rating-coloured map pins are the trap.** They are colour-only by construction. If pins encode rating, they need a second channel — numeral inside the pin, or size, or shape.
- **SC 1.4.11 Non-text Contrast (AA):** *"The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s): User Interface Components and Graphical Objects"* [E, verbatim — W3C, WCAG 2.1]. Here is the specific, real hazard: **you cannot guarantee 3:1 for a pin against an arbitrary map tile.** The background is imagery you do not control, and it changes with zoom, region and light/dark map style. Mitigation, which must be a design rule and not a per-screen judgment: every pin and every piece of text over the map carries an opaque contrasting outline or plate, so the contrast is against a surface Candour controls rather than against Ordnance Survey greens. The same applies to **SC 1.4.3 Contrast (Minimum), AA, 4.5:1 for text** [E, verbatim — W3C, WCAG 2.1] wherever a label sits on the map.

### 5.5 Touch targets

Per §5.1, WCAG 2.1 AA imposes nothing here; 2.2 AA imposes 24×24 CSS px [E]. Two Haunt-specific risks:

- **A five-star row puts five adjacent small targets in a line** — the classic mis-tap generator, and the mis-tap silently writes wrong data into a permanent record. Preferred fix: a single adjustable control (segmented, stepper, or a slider with discrete stops) rather than five hit areas. This also fixes the VoiceOver problem in §5.3.
- **Map pins are small by nature and cluster on a high street.** Since §5.2 already requires a list route to everything, the pin does not have to be the primary target — which converts a hard problem into a cosmetic one.

**Requirement I would put in acceptance criteria:** every interactive target meets 24×24 CSS px as a floor and is designed to a comfortable native touch size; no interactive target sits inside another's inflated hit area.

### 5.6 Motion

**SC 2.3.3 Animation from Interactions is Level AAA in WCAG 2.1** [E, verbatim — W3C, WCAG 2.1], so the Constitution's stated baseline does not require it. **I recommend Candour honour Reduce Motion regardless, and I would raise it at pre-release if it is absent**, because a map product is close to the worst case for vestibular triggers: "fly to" camera transitions, auto pan-and-zoom onto a pin, parallax, and momentum scrolling through a long timeline. The cost is one system-setting check and a set of alternative transitions (cross-fade instead of camera flight). The harm, for a susceptible user, is nausea and a headache.

I flag the honest constitutional position: **on 2.1 AA this is a strong recommendation, not a block.** If the CEO adopts 2.2, it is still AAA there and still a recommendation. It is on my list anyway because the charter's question is "does this work for everyday people," not "does it clear the minimum."

**SC 2.3.1 Three Flashes (A)** is not a realistic risk in this product [J].

### 5.7 Text size and reflow

**SC 1.4.4 Resize Text (AA):** *"Text can be resized without assistive technology up to 200 percent without loss of content or functionality"* [E, verbatim — W3C, WCAG 2.1]. Plus **1.4.10 Reflow (AA)** and **1.4.12 Text Spacing (AA)** [E — W3C, WCAG 2.1]. On iOS this means Dynamic Type all the way through the accessibility sizes.

The specific breakage, which is entirely predictable: **a timeline row carrying venue + times + rating + note snippet on one line will clip or truncate at the largest accessibility sizes.** Requirements: no fixed row heights, no truncated venue names ever (the venue name is the identity of the entry), rows reflow vertically, and the confirm actions stay reachable rather than sliding off the row.

### 5.8 Two structural problems, and one disagreement with the CTO's sizing

- **No telemetry means no accessibility field data.** Candour will never learn that VoiceOver users abandon at the venue picker. The compensation is not a one-off audit; it is **VoiceOver, Voice Control, Dynamic Type at the largest accessibility size, Reduce Motion and Increase Contrast run as acceptance criteria on every release**, by the QA seat, against a written checklist. That is a handoff to QA and to the PM/BA, and it should be in the requirements document if this proceeds.
- **The build sizing allocates "Accessibility to WCAG 2.1 AA baseline: VoiceOver, Dynamic Type, contrast, motion — 1 week"** as a standalone workstream [E, CTO §6.1, retrieved 2026-09-09]. **Disagreement, recorded once:** one week is realistic as a *verification pass over an already-accessible design* and is not enough to retrofit accessibility onto a design that ignored it. Accessibility is a constraint on the timeline UI, the picker, the map and the backup flow — four other rows in that table. I ask that the standalone line be deleted and the effort distributed into those rows, with per-feature acceptance criteria. If it stays as a standalone week, treat it as the audit, not the work.

---

> **⚠ CORRECTED 2026-09-16 — see Correction C1 in `decisions/2026-09-16-haunt-gate.md`.** The reasoning in this section is **conceded and superseded**. Its free-tier analysis inherits the CFO's cost-alignment test as though it were constitutional (C1.4) and the marginal-cost reading of Cost (C1.2). **The UX seat's Article 4 block is the one block here that was properly grounded** (C1.3), and its judgment that a read-cap is the wrong product stands — as judgment, not as law. The text below is preserved unaltered so the error remains inspectable; **do not cite it.**

## 6. Dark-pattern audit of the pricing shapes

The starting point is the change the proposal itself flags: **on the fully-offline architecture there is no per-lookup cost, so the CFO's compliant basis for a free tier disappears.** The CFO's recommended free tier was *"unlimited entries, unlimited history, unlimited editing, unlimited export, forever. Capped automatic venue lookups (e.g. 5/month)"*, and its whole justification was that it *"caps a metered service Candour pays for per use, not the customer's access to the customer's own words"* [E, verbatim — `products/haunt/cost-sheet.md` §8.2, retrieved by the CFO seat 2026-09-09]. Delete the meter and the justification goes with it. The cap would then restrict a feature that costs Candour **nothing per use**, which means the paywall no longer describes a cost — and "the paywall sits precisely on the cost" was the entire argument for its compliance.

I audit each shape against Article 4's list — plain-language pricing, no hidden fees, no forced bundles, no drip pricing, cancellation as easy as signup, no false urgency, no confirm-shaming, no pre-ticked boxes, no buried settings, no compulsion mechanics, export free at any time — plus Article 1.2 (no profiting from lock-in) and Article 1.3.

### 6.1 Shape A — one-off purchase (£14.63 at 5,000 on the offline index)

**Can be built with no dark pattern. It is the only shape where the clean version is also the obvious version.**

Nothing to cancel, no tier to compare, no cap to design, no lapse to handle, no upgrade prompt to place. The App Store shows the price before install in plain language, which satisfies Article 4's pricing clause by the platform's own mechanics. Export is free and always available because there is no tier that could restrict it.

Three conditions I would still attach:

1. **Do not use the word "lifetime."** It invites the reading Candour cannot honour. Say: *"Buy once. Yours forever, on your phone, whether or not Haunt continues"* — which is true, because the journal is a local SQLite file with a documented export, and Article 7.2 already promises 90 days' notice plus export for 90 days after shutdown. The CVO's standing decision on published supported life belongs on the same screen.
2. **Paid-up-front makes the trial question acute, and it must not be answered with a dark pattern.** With no free tier and no trial, a buyer cannot know whether the venue index knows their local pub before paying (§2). The honest answer is not a crippled free tier — it is **saying the coverage number out loud** in the store description, from the spike in §2.4. Article 1.3: *"We say what a product cannot do."*
3. **No in-app review prompt timed to catch a happy user.** `SKStoreReviewController` fired after a pleasing moment is a mild manipulation of the only acquisition channel this product has. If a review prompt exists at all, it lives in Settings and the user initiates it.

### 6.2 Shape B — free + lifetime unlock (£29.59 at 9:1, 5,000 paid)

**Can only be built cleanly in one narrow form, and the CFO's own preferred form is no longer available.**

Walking every remaining candidate for what the free tier caps:

| Candidate cap | Verdict |
|---|---|
| Capped automatic venue lookups (the CFO's design) | **No longer available.** The meter is gone; the cap would now restrict a zero-marginal-cost feature and the cost/price alignment that justified it is gone with it. |
| Entry count ("100 entries free") | The CFO calls this *"defensible but not recommended"* [E, cost sheet §8.2]. **On the offline architecture I go further: it is not defensible.** With no per-entry cost, the number is chosen purely to convert. That is manufactured scarcity in a product where the scarce thing is the user's own writing on the user's own phone. |
| History window ("last 30 days free") | **Breach.** Article 4 and Article 1.2. Already blocked by the CFO, endorsed by the CVO; I am the third seat. The CFO's formulation is the right one and I adopt it: *"That is not a paywall. That is a hostage, and the hostage is being held on the victim's premises"* [E, verbatim — cost sheet §8.2]. |
| Entries beyond the cap become read-only | **Breach.** Retroactive penalty on already-created data. |
| Export limited, capped, watermarked or delayed by tier | **Breach.** Article 4 says *"at any time, at no charge and with no penalty."* |
| **Automatic capture is paid; manual entry is free** | **The one defensible remaining form** — it gates a capability, not the user's data. Two conditions, below. |

**On the last one, which is the only survivor.** Gating background capture is not per se a dark pattern: the free product is a complete, honest, manual journal that keeps everything the user writes forever and exports it freely. But it carries a trap. A free user must **not** be asked for `Always` location for a feature they cannot use — Article 4 requires collecting *"the minimum data necessary"*, and App Store 5.1.1(ii) independently forbids requiring system permissions to access functionality [E]. So the free tier must not request `Always` at all, and upgrading then means a fresh permission grant mid-purchase. That is a worse conversion funnel and an honest one. If anyone proposes to solve the funnel by asking for `Always` up front on the free tier, that is the breach and I would raise it.

**And the economics undercut it anyway:** the CFO shows a free tier at a realistic 5% conversion **roughly triples** the honest unlock price — £46.22 at 19:1 on the offline index against £14.63 for a straight purchase [E, cost sheet §8.1]. So Shape B asks the gate to accept a more complicated Article 4 surface in exchange for a worse price. I would drop it.

**One shape nobody has modelled, offered for the CFO rather than asserted by me:** a **free app with an optional unlock that removes nothing** — honesty-box pricing. It has no cap to design, therefore no Article 4 surface at all, and it fits a product whose own proposal says the differentiator is architectural honesty. I have no evidence about its conversion economics and I am not claiming any [J]; the numbers belong to the CFO.

### 6.3 Shape C — free + subscription (£3.21–£4.88/yr on the offline index)

**Cannot be built without a dark pattern. This is a finding, not a preference.**

The test is a single question: **what happens when the user stops paying?**

- **If a lapse locks the journal**, then the subscription is the history-window cap of §6.2 with a clock attached, and everything the CFO, the CVO and I have said about that applies unchanged. Candour's software would be refusing to display a file on the customer's own hardware, that the customer wrote, that Candour has never seen. Article 4 and Article 1.2.
- **If a lapse does not lock the journal**, there is nothing the renewal buys except future updates — and the product then has no mechanism to make anyone renew, which is the CFO's point that it *"is not viable as a business at the price 2.1 permits"* [E, verbatim — cost sheet §7].

There is no third branch. **The only way to make the subscription work on a fully-offline architecture is the way Article 4 forbids**, and that is precisely the condition under which a shape should be ruled out at the gate rather than designed around during build.

Two subsidiary points, in case the gate wants the subscription anyway:

- **Cancellation.** Article 4 requires cancellation as easy as signup. On iOS the cancel control lives in system Settings, not in the app, which is *good* for the user — but Candour must link to it prominently from its own subscription screen and not rely on the platform hiding it. That is satisfiable and cheap.
- **Renewal notices and dunning.** At £3.21–£4.88 a year, the entire renewal apparatus exists to collect a sum smaller than a pint, and every friction-reducing trick in that apparatus is a dark pattern waiting to be adopted under revenue pressure. The cheapest way to never ship one is not to build the machine.

### 6.4 Shape D — the Article 8 non-profit variant

The cost sheet notes this dissolves *"the pricing question, the free-tier question, the Article 4 cap question, the store-commission question"* [E, cost sheet §9]. From a UX seat, that is exactly right and worth one sentence: **it removes every dark-pattern surface in this section**, because there is no conversion to engineer. I hold no view on whether Candour should absorb £14,719 plus ~£4,989/year for it — that is Constitution 5.4 and 8, and it is the CEO's alone.

### 6.5 One Article 4 surface the pricing shapes do not cover: the honesty claim itself

The proposal's corrected sentence — *"Your timeline, notes and ratings never leave your device. The app makes no network calls of its own. If you opt in to Apple's crash reporting, Apple receives crash diagnostics — never your journal"* [E — `proposals/haunt/proposal.md`, CVO correction of 2026-09-10] — is a marketing claim, and Article 4's "honest in marketing" clause makes it a design obligation as well.

The design consequence is small and specific, and it is the one the research brief's DuckDuckGo analogue argues for: **a disclosed exception is read as the promise being false, and being right about the details does not help** [E-derived, research brief §5, retrieved by the Research Analyst 2026-09-09]. The mitigation is not better copy. It is making the claim inspectable:

- A **Privacy** screen in Settings that states, in the same words as the App Store description, exactly what is transmitted and by whom — the backup (if on), and Apple's crash reporting (if the user has it on at OS level).
- That screen **shows the current state of both**, read from the device, not a static paragraph: *"Backup: off. Apple crash reporting: on (you can change this in iOS Settings → Privacy & Security → Analytics & Improvements)."*
- The CTO's user-readable diagnostic bundle, which shows the user the entire contents before anything is sent [E, CTO §5], reachable from that screen.

That converts a claim the user has to trust into a claim the user can check, which is the only version of a purity pitch that survives a sceptical reader. It costs a screen.

### 6.6 Summary

| Shape | Buildable without a dark pattern? | What makes it clean | What would make it a breach |
|---|---|---|---|
| **A. One-off purchase** | **Yes** | Nothing to cap, cancel or convert. Coverage stated honestly before purchase. | "Lifetime" language Candour cannot honour; a timed review prompt. |
| **B. Free + unlock** | **Only in one form** — capture paid, manual free | No cap on entries, history, editing or export at any tier; free tier never requests `Always` location. | Any cap on entries or history; export limited by tier; asking free users for permissions they cannot use. |
| **C. Free + subscription** | **No** | — | Lapse locking the journal is the breach, and without it the model has no mechanism. |
| **D. Article 8 non-profit** | **Yes, trivially** | No conversion exists to engineer. | — |

---

> **⚠ CORRECTED 2026-09-17 — see Correction C2.6 and C2.7 in `decisions/2026-09-16-haunt-gate.md`.** Block **B2** below is **superseded in part**. It forbids any unpaid state restricting reading, editing or exporting entries the user already wrote — which is the withdrawn Condition 8 in substance — and Condition 4 of the decision record would have made it binding at requirements, leaving the PM/BA two conditions that cannot both be executed. **B2's surviving core is Condition 8.3** (export complete and unconditional in every tier) **and 8.4** (no compulsion machinery). Its export-clause limb fell with C1.1 and its Article 1.2 limb with C2.2.
>
> **The block itself is intact and this is not a criticism of this seat.** It is a *release* block on *flows*, and no flow exists yet; it engages on any design breaching Article 4 or Conditions 8.1–8.6, expressly including friction placed on the keep-gesture and any narrowing of what counts as "visible". **B1 and B3–B7 are untouched**, as are this note's other findings.

## 7. What I would block, and what lifts it

I hold a block on **release**, on Article 4 or accessibility grounds (Constitution 5.6; `roles/ux-lead.md`). My charter requires a block to be a checklist item failing, never a feeling of unease, and to state what lifts it.

**Nothing is blocked today.** There is no requirements document, no design and no build; a block needs something to halt. What follows is the list of seven things that **would become blocks** if they reached release, published now so the PM/BA can write them as acceptance criteria at requirements stage — which is the cheapest possible moment — rather than discovering them at pre-release.

| # | Would-be block | Clause breached | What lifts it |
|---|---|---|---|
| **B1** | Any notification that fires to bring the user back into the app on a cadence the user did not set — confirm-queue prompts, digests, "you haven't written in N days", a default-on badge count | **Article 4** — "no engagement mechanics designed to exploit compulsion" | Notifications off by default; every type user-enabled; frequency and time user-chosen; one-tap off inside the app; the authorization-loss carve-out capped at one notification per state transition (§1.1) |
| **B2** | A free tier, trial expiry or subscription lapse that restricts reading, editing or exporting entries the user already wrote | **Article 4** (data "at any time, at no charge and with no penalty"; dark patterns) and **Article 1.2** (lock-in) | The product degrades to a full read/write/export journal in every unpaid state. ~~Third seat to say this: CFO first, CVO endorsed, now UX~~ *(struck 2026-09-17 per C1.3 and C2.6: the CFO's block was outside its charter, this seat adopted the CFO's formulation verbatim rather than reaching it independently, and seats repeating one another do not multiply into independent blocks.)* |
| **B3** | Any function reachable only by interacting with the map — confirming a visit, choosing a venue, opening or editing an entry, rating | **WCAG 2.1 SC 1.1.1** (A) and **SC 2.5.1** (A) [E] | A list route to every map function, demonstrated by QA completing the full core loop with VoiceOver and with Voice Control, screen untouched |
| **B4** | Rating, capture state or any other information encoded by colour alone; text or pins over map tiles without a controlled contrast surface | **WCAG 2.1 SC 1.4.1** (A), **1.4.3** (AA), **1.4.11** (AA) [E] | Every rating readable in greyscale and present as text; measured contrast evidence for pins and map labels against the worst-case tile in both map styles |
| **B5** | Timeline rows that clip, truncate the venue name, or lose actions at the largest Dynamic Type sizes | **WCAG 2.1 SC 1.4.4** (AA) [E] | Screenshots of every primary screen at the largest accessibility text size with no loss of content or function |
| **B6** | A design in which losing the backup passphrase also loses the on-device journal | **Article 4** (export at any time, no penalty) and **Article 1.3** | The local store remains readable and exportable independent of the backup key — the CTO's stated design [E, CTO §4.2], made an acceptance criterion rather than an intention |
| **B7** | In-app or store copy asserting that nothing ever leaves the device, when opt-in platform crash reporting is a transmission | **Article 4** ("honest in marketing: claims we cannot substantiate are claims we do not make") and **Article 1.3** | The corrected wording of 2026-09-10 used verbatim in store copy, onboarding and the backup flow, plus a Privacy screen showing the live state of both transmission paths (§6.5) |

**Two things I am explicitly *not* blocking on, and I want the asymmetry on the record rather than smuggled in:**

- **Reduce Motion** (§5.6). SC 2.3.3 is AAA in WCAG 2.1 [E]. It is a strong recommendation and I will raise it at pre-release, but the Constitution's stated baseline does not carry it and I will not stretch a baseline to reach a result I want.
- **A pasteable, non-memorised recovery key** (§4.2). SC 3.3.8 is AA in WCAG **2.2**, not 2.1 [E]. Under Article 4 as currently written I can recommend it and cannot block on it. **This is the concrete cost of the baseline gap in §5.1**, and it is why I am asking the CGO to put a move to 2.2 AA to the CEO.

---

## 8. Disagreements, recorded once each

Per the universal charter clause. Each is stated once, here, and I proceed either way.

1. **With the CTO (feasibility §2.6).** *"This venue isn't listed"* is correctly called a required feature and is **not sufficient**. Absence is the benign failure; Overture's documented duplicates are the malignant one, and they corrupt the accumulated record silently with no server to repair it. **Merge, sticky choice and rename-in-place are MVP scope, not polish** (§2.3).
2. **With the CTO (feasibility §6.1).** One standalone week for "Accessibility to WCAG 2.1 AA baseline" is the wrong shape. It is an audit, not the work. Distribute it into the timeline, picker, map and backup rows as per-feature acceptance criteria (§5.8).
3. **With the CTO (feasibility §4.2).** Replace the *"periodic, dismissible reminder to check the recovery code"* with an always-visible Backup status row. A recurring prompt is the pattern §1 rules out, and the status achieves the same end without it (§4.2).
4. **With the CFO (cost sheet §8.2).** The compliant free-tier design is architecture-dependent and **its architecture has changed**. On the zero-network build the metered-lookup cap no longer describes any cost, so Shape B needs re-modelling or dropping (§6.2). This is not a contradiction of the CFO's reasoning — it is that reasoning applied to the new architecture.
5. **With the proposal's framing of the differentiator.** The proposal sells the writing. The UX seat's honest answer is that design cannot make private writing stick without a mechanic Article 4 forbids, so the case has to rest on the rating (§3.4). I am not casting a kill/proceed view I do not hold — that is the CEO's under 5.4 — but the gate should not be left believing that a UX pass will rescue the writing thesis. It will not.

---

## 9. Handoffs, if the CEO proceeds

- **To the PM/BA:** the six B-items in §7 become acceptance criteria at requirements stage, not pre-release findings. So do the venue-integrity rules in §2.3 and the dataset-refresh freeze in §2.3.
- **To the CTO / Engineer:** re-specify the pre-gate venue spike to report all four metrics in §2.4. Confirm the list-first navigation decision (§5.2) **before** any screen is built — it is the one accessibility item that is expensive later.
- **To QA:** VoiceOver, Voice Control, largest Dynamic Type, Reduce Motion and Increase Contrast as a per-release checklist, because no telemetry will ever tell us these are failing (§5.8).
- **To the CGO:** put a move from WCAG 2.1 AA to **2.2 AA** to the CEO as an Article 11 amendment. It is strengthening, not weakening, under 11.2, and it closes the target-size and accessible-authentication gaps for every future product (§5.1).
- **To the CVO / whoever owns store copy:** the corrected transmission sentence of 2026-09-10 is now the only substantiable form, and it must appear in the app as well as the listing (§6.5, B7).
- **To the CFO:** model the passphrase-loss support contact separately from the 2%/30-minute average (§4.3); and re-price or drop Shape B on the offline architecture (§6.2).

---

## 10. What I could not close, and the retrievals that failed

**Stated as failures rather than filled in from memory, per `pipeline/evidence-standard.md`.**

| # | Open item | Why it matters | Who owns it |
|---|---|---|---|
| 1 | **No usability testing of any kind.** No prototype, no participants, no observation. | Every claim here about first-time user behaviour is [J] or [I]. Five to eight people with a clickable confirm-queue and a venue picker would upgrade most of §1 and §2 to evidence, and it is **cheaper than the landing-page test the proposal already contemplates.** This is the highest-value missing fact in this note. | CEO to authorise; UX to run |
| 2 | Whether users read the confirm queue as a pleasure or a chore | §1 and §3 both pivot on it, and it is unanswerable from secondary sources | Same test as #1 |
| 3 | Real duplicate and junk rates in the UK Overture extract | Decides whether merge is MVP scope (§2.3) | Engineer, in the re-specified spike (§2.4) |
| 4 | Rate of backup-key loss among ordinary users | Sizes the unresolvable support burden (§4.3). Not measurable post-launch either, by design | CFO, as a modelled range, not a measurement |

**Failed retrievals, recorded:**

- **Apple Human Interface Guidelines (accessibility, layout).** Script-rendered; returned title only, no body, on two attempts. **Consequence: I make no [E] claim about Apple's 44×44 pt convention anywhere in this note**, and every target-size requirement in §5.5 is grounded in W3C text I did retrieve.
- **Letterboxd 2024 Year in Review.** HTTP 403 today. The 14%-of-logs figure in §3.1 travels attributed to the Research Analyst's retrieval of 2026-09-09 and is **not re-verified by me**. It is load-bearing for §3 and the Skeptic should treat it as a verification target at the gate.
- **Apple's Scheduled Summary detail page.** Only the index entry naming the feature was retrievable [E]; the mechanics (12 summaries, per-app selection, user-chosen times) surfaced only in search-result summaries and secondary sites, so I have not asserted them.
- Apple developer documentation for `CLVisit`, `requestAlwaysAuthorization()` and `UNUserNotificationCenter` also failed to render. Where I rely on those facts, the claim is marked as travelling from the CTO's retrieval of 2026-09-09, unverified by me.

---

## 11. Evidence register

Retrieved by me on **2026-09-10** unless stated otherwise.

**Standards**
- [W3C — Web Content Accessibility Guidelines 2.1](https://www.w3.org/TR/WCAG21/) — levels and verbatim text for 1.1.1 (A), 1.3.1 (A), 1.4.1 (A), 1.4.3 (AA), 1.4.4 (AA), 1.4.11 (AA), 2.5.1 (A), **2.3.3 (AAA)**, **2.5.5 (AAA)**
- [W3C — Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — **2.5.8 Target Size (Minimum), AA, 24×24 CSS px**; 2.5.7 Dragging Movements, AA; list of criteria new in 2.2
- [W3C — Understanding SC 3.3.8 Accessible Authentication (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) — **Level AA**, full normative text and the four exceptions

**Platform rules**
- [Apple — App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — 4.5.4 (push notifications must not be required for the app to function); 5.1.1(ii) (may not require users to enable push notifications, location services or tracking to access functionality; must not manipulate, trick or force consent)
- [Apple — Use notifications on your iPhone or iPad](https://support.apple.com/en-us/108781) — index entry naming "Schedule a notifications summary for a specific time of day" *(feature existence only; detail page not retrievable)*

**Encrypted backup, user-held keys**
- [Meta Engineering — How WhatsApp is enabling end-to-end encrypted backups](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/) — password or manual key; "neither WhatsApp nor the backup service provider will be able to access their backup or their backup encryption key"
- [TechCrunch — WhatsApp adds passkey protection to encrypted backups, 30 Oct 2025](https://techcrunch.com/2025/10/30/whatsapp-adds-passkey-protection-to-end-to-end-encrypted-backups) — "you have to remember your backup password or have the encryption key handy" *(**single source**)*
- [Apple — Advanced Data Protection for iCloud](https://support.apple.com/en-gb/108756) — three recovery routes; "Apple doesn't have the encryption keys needed to help you recover your end-to-end encrypted data"

**Venue data**
- [Overture Maps — Places guide](https://docs.overturemaps.org/guides/places/) — "duplicates, a high junk rate, and low property completeness"; confidence "does not address duplicates or property completeness" and is "not calibrated to be strictly comparable across providers"; ~74m records; CDLA-Permissive 2.0 / Apache 2.0, no ODbL share-alike

**Travelling from sibling Candour artifacts — retrieved by another seat on 2026-09-09, not re-verified by me**
- `products/haunt/feasibility-note.md` (CTO) — §1.1 `CLVisit` properties, two-prompt `Always` authorization and silent downgrade, reduced-accuracy operation; §2.6 the "not listed" path; §3 export/schema commitments and the cost of retrofitting; §4.2 user-held key design and the recovery-code reminder; §6.1 build sizing incl. the one-week accessibility line; §8 the venue-candidate spike
- `products/haunt/cost-sheet.md` (CFO) — §7 subscription viability; §8.1 free-tier price multiplication; §8.2 the compliant cap design, the blocked designs, and the "hostage on the victim's premises" formulation; §9 the Article 8 variant; support modelled at 2% contact rate/yr × 30 min
- `research/haunt-brief.md` (Research Analyst) — §4 Letterboxd 14%/71% arithmetic *(source 403 on re-retrieval today)*; §7.4 Overture coverage evidence and its limits; §6 the sharing-layer reasoning; §5 the DuckDuckGo analogue on disclosed exceptions
- `proposals/haunt/proposal.md` (CVO) — the correction of **2026-09-10**, made after this note was drafted: the architecture is "no network calls of any kind **in the app's own operation**", and opt-in platform crash reporting is a transmission. §4.2 and §6.5 above are written against the corrected version; an earlier draft of my Screen 1 copy repeated the overstatement and is marked as corrected rather than silently rewritten

**[K] / [J] carried openly, relied on by nothing load-bearing**
- Apple's 44×44 pt touch-target convention — **[K], not retrieved, not asserted as evidence anywhere above**
- Memory decay between a visit and a delayed confirmation (§1.2) — **[J], high confidence, no study retrieved**
- That sticky choice is the highest-value interaction in the product (§2.3) — **[J]**

---

*Prepared by the UX / Design Lead seat under `roles/ux-lead.md`. This note prepares and flags; it does not certify (Constitution 6.1). It closes the "no UX seat has looked at this" gap recorded in `proposals/haunt/proposal.md` and should travel with the gate pack. Kill / proceed / park remains the CEO's decision (Constitution 5.4), due 2026-10-07.*

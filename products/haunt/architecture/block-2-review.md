# CTO Block 2 review: re-scoped from "before Android code" to "before the Android release build"

**Seat:** Chief Technology Officer · **Date:** 2026-10-10 · **Status:** A decision on my own block, which only I can lift or narrow (Constitution 5.6). **It prepares and flags; it does not certify** (6.1). Decisions this touches that belong to the CEO (Constitution 5.4: *"spending real money"*, *"release to real users"*) are flagged in §5, not taken.
**Asked by:** the Coordinator, on the CEO's "Yes", 2026-10-10, to: *"shall I put your position, quoted as above, and your three options to the CTO, asking whether it would narrow or re-scope Block 2?"*
**Block as it stood** (`android-and-stack-note.md` §4, 2026-09-16): *Breach:* Constitution 1.3 and Article 4, *"shipping 'automatic capture' we know will fail on part of the fleet"*. *Lifted by:* *"a published device-matrix spike over ≥2 real weeks on at least a Pixel, a Samsung and a Xiaomi, with a minimum capture rate agreed with PM/BA and QA **before** it runs — and … a measured gap-detection accuracy"*. Placement: before product code (`android-and-stack-note.md` §1.7; `m1-wave-plan.md` §6).
**Template note:** `pipeline/templates/` has no template for a block review [E: listed from disk, 2026-10-10]. This follows `block-4-ruling.md`.
**Evidence tags** per `pipeline/evidence-standard.md`. Web sources were retrieved on 2026-10-10.

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-10

---

## 0. The answer on one page

**The CEO's question: is the spike for proving it works, or for finding out how to do it? Mostly proving.** The how is designed (§1). The spike measures whether that design, on phones whose makers kill background apps, **either records each visit or tells the user it missed it.** It can still return "don't", but it is not research into an unknown mechanism.

**My decision: the block is re-scoped.** It no longer stops Android code. It stops **the Android release build**. That means the release-candidate work, the Play submission, and any build given to people outside Candour that does not carry the label in §4.2. It stays engaged until the lifting condition below holds.

**Why I am moving it.** The CEO's question exposed something I should have seen. The harm my block names, a claim of automatic capture that the fleet does not bear out, happens **when the claim reaches a user, not when the code is written** (§2). The Kotlin capture layer is also the instrument the measurement needs: nothing can be measured without it. The cost of building first is labour that a bad result might waste, and that is the CEO's money decision (5.4), not an honesty breach. **In September I wrote that narrowing my own block to suit the plan is what the block exists to prevent** (`m1-wave-plan.md` §6). I am narrowing it anyway, for a reason I can state: the earlier placement protected the wrong moment. §2.3 shows the honesty protection is not weakened.

**The new lifting condition, in my words.** Before the Android release build begins, a published measurement exists. It is set against thresholds that the PM/BA and QA write down before it starts. It shows that on **at least one Samsung and at least one Xiaomi-family phone, each carried in ordinary daily use for at least 14 days** with a diary of places visited, the app **recorded each diary visit or recorded a gap covering it**, at or above the agreed rate. Stock Android's Doze and App Standby limb may run on the emulator. **The phones can be anyone's:** the CEO's, a cheap purchase, a friend's, or a labelled volunteer's. Nobody has to carry more than one.

---

## 1. The CEO's question: proving, or finding out how?

**Proving, with a real chance of "don't".**
- **The how is designed** (`android-and-stack-note.md` §1.6): a declared location foreground service, Activity Recognition transitions as the trigger, batched fused-location fixes, stay clustering, a notification as the honest surface, and **capture gaps recorded as data and shown on the timeline**. CAP-3 and CAP-4 specify it (`requirements.md` v1.4).
- **What only real phones can answer:** two numbers. (1) **Capture rate:** what share of real visits becomes a candidate. (2) **Gap-detection accuracy:** for each visit missed, did the app record a gap covering it, or fail silently? The second carries the honesty claim. §1.7 of my note: *"A spike that shows 80% capture with reliable gap detection is a pass; 95% capture with silent failures is not."*
- **What the measurement also settles:** tuning that the design leaves open, such as the transition triggers, the batch interval and the clustering thresholds [J]. That is "how well", not "how".
- **It can return "don't" or "not yet"** (`android-and-stack-note.md` §0.3 carries the spike *"separately because it may return 'don't'"*). The likeliest bad result is not "impossible". It is "the gap surface misses one way the phone fails", which means more design work [J].

**The Coordinator's summary to the CEO, checked:**

| Coordinator said | Check |
|---|---|
| The spike measures capture rate, gap-detection accuracy and battery on real phones; the how is designed (§1.6) | **Right, with one correction.** Battery is measured on the same run, but it is **CAP-10's gate on battery claims**, not part of my lifting condition. My §4 text names capture rate and gap-detection accuracy only. CAP-10's own text says *"This is also CTO Block 2's lifting condition"*, which overstates it (§5, flag to the PM/BA) |
| An emulator is unlikely to reproduce OEM battery killers [I] | **Right, and stronger than "unlikely".** The emulator runs Google's Android without a phone maker's own layer, and Xiaomi's background limits are *"non-standard … There are no APIs and no documentation for those extensions"* [E, [dontkillmyapp, Xiaomi](https://dontkillmyapp.com/xiaomi), community source, single origin; corroborated in kind by Sentiance, `android-and-stack-note.md` §1.3e]. Code that is not there cannot run [I] |
| Wave plan §6 names a narrower reading that I called defensible but did not adopt | **Right.** This decision goes further than that reading (§4) |
| User feedback would have to be voluntary, because PRIV-8 rules out telemetry | **Right.** PRIV-8: *"No analytics, no telemetry SDK, no bundled third-party measurement of any kind, and no networking code in the app"* (`requirements.md` v1.4). A user can choose to export a file through the system share sheet; the app sends nothing itself |

## 2. Does the CEO's position on OS-closed apps change what the block protects?

**The CEO:** *"if for battery management, it closes the app, then that is acceptable, we don't want to affect a user's battery."*

**It does not change what the block protects, because the block never objected to the app being closed.** In September I corrected my own feasibility note on exactly this: *"Failing quietly is the opposite of the promise. Failing visibly is not — it is an honest product with a stated limitation, which is what Article 1.3 actually requires"* (`android-and-stack-note.md` §1.4). The CEO's position and the block agree. The OS may close the app. What the block protects is **the user being told.**

**The clauses:**
- **Constitution 1.3:** *"Honest by default. Pricing, capability, and limitations are stated plainly. We say what a product cannot do."*
- **Article 4:** *"Remain honest in marketing: claims we cannot substantiate are claims we do not make."*

The claim at stake is "automatic". It is substantiable on Android only alongside the gap surface (CAP-4). It stays honest only if gaps are actually detected when the OS or the phone's maker stops the app.

**Where the gap surface can fail silently**, which is what the measurement is for [I, from the platform's behaviour as described in `android-and-stack-note.md` §1.3]:
1. **Killed outright.** A force-stop gives the app no callback. The gap is found later, from the last heartbeat, when the service next starts or the app is opened. This is detectable, and the bounds are approximate.
2. **Alive but starved: the case that matters.** The service is still running, but batched fixes or transitions are deferred or withheld. Radar documents updates *"delayed significantly by Doze Mode, App Standby, and Background Location Limits"* (`android-and-stack-note.md` §1.3d). Nothing looks dead, so no gap is written, and a visit goes missing. **Only a ground-truth diary on a real phone in real use finds this.**
3. **Never restarted.** A force-stopped app stays stopped until the user opens it. The gap is then shown from the last heartbeat to the moment it is opened, which is honest though late [I].

**The CEO's "gather feedback and improve iteratively" works for failures users can see, and cannot find the silent ones.** A user reports what they notice. A visit missed with no gap shown is, by construction, not noticed. And under PRIV-8 the app cannot report it for them. That is why the lifting condition needs a diary, and why voluntary feedback alone cannot lift it. **It is also why the honest moment to require the measurement is before the claim ships, and not necessarily before the code is written.**

**One thing the CEO's position does change:** it moves the weight from capture rate to gap-detection accuracy. If the product accepts the OS closing it, Haunts should not fight phone makers' battery managers. That means no nagging for a battery-optimisation exemption, which Play policy restricts anyway (`android-and-stack-note.md` §1.3e). So the capture-rate threshold the PM/BA sets may be modest, and the gap-detection threshold is the one that must be high [J].

## 3. The options

| Option | Cost | What it gives up | Satisfies a lifting condition I accept? |
|---|---|---|---|
| **An emulator** | Nothing [J] | All phone-maker behaviour. Real motion and Activity Recognition, since locations are replayed, not walked. Battery | **Partly: the stock-Android limb only.** It can force Doze (`adb shell dumpsys deviceidle force-idle`) and App Standby, which Google documents for testing [E, [Android, Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby)]. It can also test reboot (CAP-3(a)) and force-stop (CAP-3(b)). It is the right place for automated tests of the gap logic. **It cannot measure capture rate or silent failure on a Samsung or a Xiaomi** |
| **One cheap device** | Roughly £80–£150 for a recent Redmi or POCO [J, not priced this session]. **Spending real money is the CEO's decision** (5.4). Plus one carrier for 14 days | Every other maker. One phone is one sample | **Partly: one maker's limb**, if it is a Xiaomi-family phone (the worst case in this category [E, dontkillmyapp, above]) or a Samsung, carried in daily use for 14 days with a diary. **Recommended as the first phone:** a Xiaomi-family one |
| **A friend's phone** | No money. A development build on their phone; their 14 days and their diary | Control over the device. Their privacy needs care: their location stays on their phone, and only counts come back | **Partly: one maker's limb**, under the same rules. **Flag to the CGO:** the friend's diary and locations are personal data. The protocol keeps raw locations on the phone, shares only counts by the friend's own export, and records the friend's informed consent |
| **My narrower reading** (Kotlin storage now; capture reliability waits) | Nothing extra | — | **Superseded.** It still held the capture code back. This decision lets the capture code proceed too, because the code is the instrument |
| **Lift at a later point** (before the Android release, not before Android code) | **Labour at risk:** if the result is bad, part of the Android capture layer (sized at 5–7 weeks, `android-and-stack-note.md` §1.7) may need redesign. Labour on work that does not ship is written off as a cost in the year (Constitution, Definitions, *"Cost"*). **Accepting that risk is the CEO's call** | Early warning. A late bad result costs more than an early one | **Adopted** (§4). I recommend running the measurement **as soon as the Android capture story exists** (M1's Android wave), not leaving it until M5, so that a bad result arrives early [J] |
| **Cloud real-device farms** (e.g. Firebase Test Lab) | **About $1,700 per device for 14 days:** 30 free minutes a day, then *"$5 per hour for each physical device"* [E, [Firebase Test Lab pricing](https://firebase.google.com/docs/test-lab/usage-quotas-pricing)] | Real carrying. The devices sit in a rack, probably on charge [K, moderate], and Doze needs a device *"unplugged and stationary"* [E, Android Doze doc, above] | **No.** Good for one cheap thing: checking that the service, the notification and the permission flow start on several makers' systems. Not a lift |
| **A beta to volunteers** (Play closed testing) | No money. **It is a release to real users, so the CEO decides** (5.4); the CGO reviews the data handling | Speed: recruiting takes time | **Yes, and the broadest route.** Two conditions. (1) The build says plainly, in the app and in the invitation, that Android capture is unmeasured and may miss visits, so no unsubstantiated claim is made (Article 4). (2) The app lets a volunteer add a visit Haunts missed and mark it *"Haunts missed this"*, and export a counts-only summary through the share sheet. That produces the diary inside the app, with no telemetry (PRIV-8). It is also the CEO's *"gather feedback and improve iteratively"*, made into a measurement |

**Combination I recommend** [J]: the emulator for the stock-Android limb, in CI, from the Android capture story on. **One cheap Xiaomi-family phone carried by the CEO** (his offer: *"get a cheap android device for testing"*). **One Samsung**, either a friend's or a volunteer's. A labelled closed beta afterwards, if the CEO wants breadth before release.

## 4. Decision: **re-scoped**

### 4.1 Block 2, as it now reads

> **Block 2 — Android capture claimed before it is measured.**
> *Breach:* Constitution 1.3 (*"We say what a product cannot do"*) and Article 4 (*"claims we cannot substantiate are claims we do not make"*). The breach is releasing an Android build that presents capture as automatic without evidence that, on phones whose makers restrict background apps, Haunts either records each visit or records a gap covering it.
> *What it blocks (build commencement, my charter's power):* **commencement of the Android release build**: the release-candidate work, the Play store listing and submission, and any Android build given to people outside Candour unless that build carries the label in §4.2. **It does not block** Android code, the Kotlin capture module, development builds, the emulator, or Candour's own testing.
> *Lifted by:* a **published measurement**, against a **minimum capture rate and a minimum gap-detection rate that the PM/BA and QA write down before it starts** (CAP-11 … CAP-14), showing:
> 1. **At least one Samsung phone and at least one Xiaomi-family phone** (Xiaomi, Redmi or POCO), **each carried in ordinary daily use for at least 14 days.** One person per phone; they may run at the same time; the phones may be anyone's.
> 2. **A diary of places actually visited** on each phone, kept on paper, in a note, or in the app as *"Haunts missed this"* entries. For every diary visit, the app either recorded it or recorded a gap covering it.
> 3. **Gap detection measured for each failure kind in §2**, including "alive but starved".
> 4. **The stock-Android limb** (Doze, App Standby, reboot, force-stop) proved on the emulator or a Pixel, and kept as automated tests.
>
> Both rates at or above their thresholds. The Pixel is no longer required.

### 4.2 The label for builds outside Candour before the lift

Any Android build given to anyone outside Candour before the lift says, **at first launch and in the invitation**, that Android capture has not yet been measured on their kind of phone and may miss visits, and that missed time is shown where Haunts knows about it. **It makes no claim that capture is automatic or reliable on Android.** Giving any such build to real users is still the CEO's decision (5.4).

### 4.3 What would overturn this decision

- **Back to "before code":** evidence that the design in §1.6 cannot detect the "alive but starved" case at all, for example an Android rule that withholds every signal a heartbeat could use. Then the design is unsound, which is my build-commencement ground in its original sense. I have not looked for such a rule beyond the sources cited in `android-and-stack-note.md` §1.3 [K: I know of none].
- **Lifted earlier, or more cheaply:** a published, independent measurement of gap detection on Samsung and Xiaomi by a comparable offline app. I know of none (DayTrace and GPS Logger publish no figures, `android-and-stack-note.md` §1.3).
- **Where I looked for this review:** `constitution.md`; `roles/cto.md`; `android-and-stack-note.md` §0, §1 and §4; `block-4-ruling.md` §2.4; `m1-wave-plan.md` §6 and §7 (candour PR #31); `requirements.md` v1.4, CAP-3, CAP-4, CAP-10, the CAP-11 … CAP-14 reservation, and PRIV-8; `haunts` #280 (SPK-02); and the three web sources linked above.

## 5. Flags, each to the seat that decides

- **CEO (5.4):** (1) whether to accept the labour risk of building Android capture before the measurement (§3, *"lift at a later point"*); (2) the cheap phone, which is spending; (3) any build given to people outside Candour, including a friend or a closed beta, which is a release to real users.
- **PM/BA:** CAP-10 says *"This is also CTO Block 2's lifting condition"*. **It overstates the link.** My lifting condition (`android-and-stack-note.md` §4) never named battery, though §1.7 asked the same run to measure it. CAP-10 gates battery **claims**, and its device list (Pixel, Samsung, Xiaomi) no longer matches this block. The PM/BA decides whether CAP-10 keeps its own device list or follows this one. **Also:** write CAP-11 … CAP-14 (the thresholds) before the measurement starts. I do not edit requirements.
- **CGO:** the data handling for a friend's phone or volunteers' phones (§3): consent, counts-only export, and no raw locations leaving their phones.
- **CFO:** the 75-hour spike line in `android-and-stack-note.md` §0.3 becomes a measurement run plus a little in-app tooling (the *"Haunts missed this"* entry and the counts export). The hours are about the same [J]. The labour-at-risk is new, and it belongs in the cost sheet's risk note.
- **CSO:** the Android capture stories now start without waiting for SPK-02, so condition C11 (*"Android capture not `directBootAware`"*) arrives with them, as `threat-model-m1.md` §6.1 already places it.

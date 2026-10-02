# CSO security review — Haunts code architecture proposals (SPK-20, D59)

**Seat:** Chief Security Officer · **Date:** 2026-09-28 · **Reviews:** `products/haunt/architecture/architecture-proposals.md` (CTO, 2026-09-27, commit `734d3cc` on the SPK-20 worktree branch), options A, B, C and draft ADR-0001.
**Status:** A review. **It prepares and flags; it does not certify** (Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**"*). D59 requires it before adoption: *"A seat other than the CTO reviews it, and the CSO reviews its security."* Nothing here changes the proposals file.
**Blocks exercised: none.** My charter's block is *"Release — for unresolved material vulnerabilities or absent threat modelling"* (`roles/cso.md`). An architecture choice is not a release. Everything below is a **finding**, a **condition** I ask to be written into the ADR, or a **flag** to the seat that owns the decision.
**Template note.** `pipeline/templates/` has no security-review template (cost-sheet, decision-record, dissent-memo, gate-pack, idea-brief, proposal, requirements, research-brief, review-pack). This follows the commission's questions in order, as the security baseline did.
**Evidence tags** per `pipeline/evidence-standard.md`. [E] = retrieved this session, link attached (register at §9). [K] = model knowledge, confidence stated. [I] = inference. [J] = judgment. Vendor documentation is single-source for how the vendor's product behaves, and is flagged once here rather than on every line.
**Read for this review:** the proposals in full; `constitution.md`; `roles/cso.md`; `pipeline/evidence-standard.md`; `products/haunt/repo-security-baseline.md` (D32, with Correction 1); `requirements.md` v1.3 §2, §3.2, §4 (CAP), §12 (DATA), §12.2.8, §14 (PRIV), HEAD-12, LOOK-2; `android-and-stack-note.md` §2.2–§2.5; decision record D27–D60.

---

## Page one — for the CEO

**Verdicts.**

| Option | Security verdict | In one line |
|---|---|---|
| **A — by kind** | **Acceptable with conditions** | Same security controls as B (network ban, one SQLite owner, capture isolation), but its written rule set omits the VPAGE-4 entitlement zone, and nothing stops any hook calling any repository. Security is no worse in kind; it is looser in practice. |
| **B — feature + core** *(CTO's recommendation)* | **Acceptable with conditions — my preferred option** | The storage, capture and network boundaries each have one home a tool can check. The conditions (§3) close gaps that apply to every option. |
| **C — packages** | **Acceptable with conditions, and not stronger than B in practice** | Its "walls, not rules" claim is overstated: with npm workspaces, hoisting lets a package import what it does not declare [K, high confidence], so the walls still rest on a lint tool. It adds manifests, duplicate-dependency hazards and one more dev dependency, for no security gain over B. |

**The three things that matter.**

1. **PRIV-8 is made mechanically true for our own code, not yet for third-party code.** The lint and native scans see only first-party files. What makes it mechanical for dependencies is Android's release build with no `INTERNET` permission, and on iOS there is no equivalent: there it rests on the dependency review and the on-device network capture. Also, **any ESLint rule can be switched off with a comment**, which is exactly the `gitleaks:allow` hole the baseline closed. Fix: CI runs ESLint with inline configuration disabled (§3, C1–C4).
2. **The two-file split is a security gain as well as a corruption fix.** It lets the two files carry different iOS protection classes and different backup treatment, and it keeps entitlement out of the journal file. I support it (§4).
3. **OS backups: my recommendation is to exclude the journal from both platforms' cloud backups by default, and to say so plainly in the app** (§5). **This is your decision** (Constitution 5.4: *"anything affecting user data policy"*), after the CGO's legal view. Left at the default, Android copies the journal to the user's Google Drive and the iPhone copies it into iCloud Backup, which makes PRIV-1's first sentence false for every default user. The cost of excluding is real: **a user who loses their phone without a Haunts backup loses the journal**, so the app must say so.

*(Sections 1–9 follow. §5 holds the OS-backup options; §9.1 lists the 23 conditions.)*

---

## 1. Threat model, in short, because every finding is judged against it

**What is at stake.** A person's confirmed location history: where they went, when, how often, what they thought of it, sometimes with photos. `requirements.md` already treats it as the most sensitive thing the product holds (LOOK-2's design note: *"a heatmap of a person's own life is the single most revealing artifact this product can render"*).

| Who | How they get at the journal | What the architecture controls |
|---|---|---|
| **Someone close to the user** (partner, family, a person with the phone in hand) — the most realistic attacker for a location journal [J] | An unlocked phone; the app-switcher snapshot; a shared cloud account; a family computer holding an unencrypted phone backup | Screen-level surfaces (HEAD-12), file protection classes, OS-backup treatment (§5) |
| **Anyone who gets into the user's Google or Apple account**, or a provider under legal compulsion | OS cloud backups. **Standard iCloud Backup keys *"are secured in Apple data centers"*** [E, Apple 102651], and **Advanced Data Protection cannot be enabled by new UK users** [E, Apple 122234]. Haunts is UK-only (`requirements.md` §16.1) | Whether the journal enters OS backups at all (§5) |
| **A compromised dependency, build tool or update channel** | Code that phones home, shipped inside our own binary. The baseline's §1 names a poisoned build as the worst plausible breach | PRIV-8's five layers (§2), dependency approval (§6) |
| **A hostile file** (an archive the user is sent and imports) | Import parsing: zip bombs, path traversal, malformed JSON, oversized fields | The one serialiser in `core/store/archive/` (§3.4) |
| **A device thief** | A locked phone | OS full-disk / file-based encryption; file protection class (§3.3) |

**Blast radius, stated once.** Because there is no server, there is no breach that exposes many users at once from Candour's side — **except a malicious build or update**, which reaches every install. That is why the supply-chain conditions (§6) matter more than anything about folders [J].

---

## 2. PRIV-8: is the network boundary mechanically true?

**PRIV-8** (BLOCKING): *"No analytics, no telemetry SDK, no bundled third-party measurement of any kind, enforced at build time."* Criterion: *"CI fails the build if the dependency tree contains a known analytics package or any outbound HTTP call site outside the backup module."*

**The CTO's design goes further than PRIV-8, and I agree with that.** It aims for *no* app-owned networking at MVP, because every network path the product has is the operating system's (store asset packs, the platform photo framework, platform crash reports, the share sheet). With the CEO's standing recommendation of a user-saved backup file, there is no backup module that needs the network, so the "single call site" is **zero call sites**, and PRIV-8's exception is unused. The design is the same in all three options (§6.8 of the proposals); options differ only in folder names.

**Layer by layer, what is mechanical and what is not.**

| Layer (proposals §6.8) | What it genuinely enforces | Gap I found | Condition |
|---|---|---|---|
| **1. JS lint** (`no-restricted-globals` with `checkGlobalObject`) | Our own code calling the global `fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource` | **(a) `expo/fetch` is an import, not a global.** Expo documents *`import { fetch } from 'expo/fetch';`* [E, Expo SDK `expo` reference], and `no-restricted-globals` does not see imports [I]. The same applies to any networking reached through an import: `expo-file-system` download functions, `expo-image` / `Image.prefetch` with a remote URI, `react-native-webview`, `expo-web-browser`, `expo-updates` [K, high confidence that each can reach the network]. **(b) Any lint rule can be switched off with an `// eslint-disable` comment.** ESLint documents both *`noInlineConfig`* and the *`--no-inline-config`* CLI option to stop that [E, ESLint "Configure rules"]. That is the same hole as `gitleaks:allow`, which the baseline closed by running CI with `--ignore-gitleaks-allow`. **(c)** The `http` string-literal rule is bypassed by concatenation or a template string [I]. | **C1, C2** |
| **2. Native scan** (`tools/check-network.ts`) | Our own Swift/Kotlin under `modules/` and `plugins/` | The deny list should also name `WKWebView`, `SFSafariViewController`, `CFStream`/`CFNetwork`, `okhttp3` (the package name, not only "OkHttp"), `java.net.URL` with `openConnection`/`openStream`, `android.webkit.WebView`, `DownloadManager`, `Ktor`, `Volley` [K, high confidence each is a network path]. It does not and cannot see third-party native code. | **C3** |
| **3. Dependency list** (`docs/dependencies.md`, CI fails on an unlisted dependency) | That nothing new enters without a reviewed line | **As worded, it covers "every production dependency".** PRIV-8 says *"the dependency tree"*. Transitive npm packages and **autolinked native code** (every `expo-*` package brings Swift/Kotlin) are where a network call would hide. The declared network behaviour is a human judgment, not a mechanical one. | **C4** |
| **4. Android release manifest without `INTERNET`** | **Everything in the app's process, our code and third-party code alike** [K, high confidence: sockets need the permission] | This is the only layer that makes PRIV-8 mechanical for third-party code, and **only on Android**, and only if the spike shows Play asset packs, Play Billing and the photo provider work without it (Play Billing talks to the Play Store app over IPC, so I expect it does [K, moderate]). | **C5** |
| **5. On-device network capture per release** (DATA-6(a), PHOTO-11(b), LOOK-2(g)) | Ground truth, both platforms | On **iOS it is the only check covering third-party code**, so it must be a release gate, not a sample. iOS's App Privacy Report lists the domains an app contacted [K, high confidence], which makes a cheap second check for QA. | **C5** |

**Verdict on PRIV-8.** **Mechanically true for first-party JavaScript and first-party native code once C1–C3 land. Mechanically true for third-party code on Android if the `INTERNET` spike passes. On iOS, third-party code is covered by review (C4) and by device capture (C5), which is evidence rather than a mechanism** [I]. I accept that: no mechanism exists on iOS to deny an app sockets [K, high confidence], and I would rather state the limit than claim more.

**If a cloud backup is ever chosen** (proposals §6.8, last paragraph), the allow-listed folder `features/my-data/backup/transport/` must accept **only ciphertext**: a branded TypeScript type that only the crypto module can construct, plus a lint zone so `transport/` imports nothing from `core/store` except that type. Otherwise "the backup module" becomes a place where plaintext can reach the network by a one-line mistake [J]. **Condition C6, for the ADR's "Revisit when".**

---

## 3. The native-module boundary and the data-at-rest story

### 3.1 The Core/Bridge split (CAP-1(b)) — sound in design, one hole in the check

Splitting the recording path (`Core`) from the Expo module (`Bridge`) is the right shape, and the Expo Modules API over Turbo Modules is the lower-risk choice (less generated code, no Objective-C++). **The hole:** in Swift, files compiled into the same module see each other's types **without any `import`** [K, certain]. If `ios/Core/` and `ios/Bridge/` compile into one pod target, `VisitRecorder.swift` can call `CaptureModule` directly and the proposed check, which greps `ios/Core/` for `import ExpoModulesCore` / `import React`, passes [I]. Kotlin does not have this problem, because `core` and `bridge` are separate packages and a cross-package reference needs an import or a fully-qualified name, both of which the substring check catches [K, high confidence].
**Condition C7:** compile `ios/Core` as its own Swift module (a separate target), so the compiler enforces the direction; **or** extend the check to fail on any Bridge type name appearing in `ios/Core/`. The first is stronger. It is a correctness check for CAP-1 more than a security one, but it is the check the ADR names, so it should be true.

### 3.2 The bridge as a trust boundary

- **Commands from JavaScript into native** (`markAdopted(id)`, `discard(id)`, `recordEntitlement(interval)`) are validated on the native side: typed, bounded, and **every SQL statement on both sides is parameterised** [J, standard practice]. **Condition C8:** a lint rule (JS) and a grep (native) that fail on SQL built by string interpolation or template literals passed to `run`/`all`/`get`/`exec`.
- **`recordEntitlement()` makes capture entitlement writable from JavaScript.** On a device the user controls, local entitlement can always be forged by a determined user, so this is a revenue question, not a user-data one [J]. It is not a finding against the architecture. **Flag to the entitlement spike:** prefer the native side reading the platform's signed entitlement (StoreKit 2 verifies transactions on device [K, high confidence]) over trusting a JS call, which would also answer the CTO's own ENT-2 renewal flag.

### 3.3 Data at rest — where the files live and how they are protected

**Where Expo SQLite puts a database by default** [E, `expo-sqlite` source at `990f8ad`]: on iOS, `documentDirectory` + `/SQLite`; on Android, `context.filesDir` + `/SQLite`. Both open calls accept a `directory` parameter [E, `SQLiteDatabase.ts`, same SHA].

- **iOS `Documents/` is the wrong home for the journal** [J]. It is backed up by default, and it is the directory the Files app and Finder expose if file sharing is ever switched on in `Info.plist` [K, high confidence]. **Condition C9:** `core/store/paths.ts` opens `journal.db` in `Library/Application Support/<bundle id>/`, and the native `CaptureStore` does the same for `capture.db`, using the `directory` parameter. Apple suggests naming such a folder with the bundle identifier [E, Apple, *Optimizing your app's data for iCloud backup*].
- **iOS protection classes, and why two files help.** Apple: *Protected Until First User Authentication* is *"the default class for all third-party app data not otherwise assigned"*; *Complete Protection* discards the key *"shortly after the user locks a device (10 seconds…)"*; *Protected Unless Open* exists because *"some files may need to be written while the device is locked"* [E, Apple Platform Security, Data Protection classes].
  - **`capture.db` must stay at Until First User Authentication.** The recording path is relaunched in the background, often with the phone locked, and must write [I]. Anything stricter loses visits.
  - **`journal.db` could be stricter, but I do not recommend `Complete` at launch.** With WAL, SQLite keeps `-wal` and `-shm` files open; if the phone locks while a connection is open, reads and writes fail [K, high confidence], and whether JavaScript ever runs while locked depends on the SDK 58 life cycle work the CTO has already flagged. **Condition C10:** set **Until First User Authentication explicitly** on both files and their `-wal`/`-shm`/`-journal` companions, and test the class on all of them. A spike may later move `journal.db` to `Complete` if the app closes it on `protectedDataWillBecomeUnavailable`; that would be a genuine gain against a locked, stolen phone [J]. **Under one shared file this choice would not have existed.**
- **Android.** Both files live in credential-encrypted internal storage by default, readable only after first unlock [K, high confidence]. **Condition C11:** the capture service stays **not** `directBootAware`, and nothing is ever placed in device-protected storage, which is readable before the user unlocks [K, high confidence].
- **`venues.db`** is opened read-only (`SQLITE_OPEN_READONLY`, or `immutable=1` once verified). It holds no user data. It is reproducible from the app bundle, so it is excluded from OS backups whichever way §5 goes (it is about 21 MB, most of Android's 25 MB quota, §5.1).
- **Temporary plaintext.** The export `.zip` and any staging file for an encrypted backup file are written to the cache directory and deleted when the share sheet returns. iOS `Library/Caches` and `tmp` are excluded from iCloud Backup [E, Apple]; Android's `getCacheDir()` is excluded from Auto Backup [E, Android]. **Condition C12.**
- **The app-switcher snapshot is data at rest too.** iOS writes it to disk inside the container [K, moderate]. **HEAD-12's cover therefore needs a named home in the architecture, and it has none.** It must run natively before the snapshot is taken: on iOS in the scene / app-delegate hook, not from JavaScript's `AppState`, which may fire too late [K, moderate]; on Android API 33+, `setRecentsScreenshotEnabled(false)` rather than `FLAG_SECURE`, which would break HEAD-12(d)'s user screenshots. **Condition C13:** a small `modules/privacy-cover/` (or a section of the capture module's Bridge) owns it, with its own ticket, and CAP-1's rule. **Flag to PM/BA and UX:** a cover over the **whole app**, as banking apps do, is simpler to build and test than a cover for two screens, and is the protective default under DFLT-1 [J]. That is a product decision, not mine.
- **Considered and not recommended: encrypting the journal file itself** (SQLCipher, which Expo SQLite can vendor [E, README]). It would break DATA-1 (*"Open the file with the `sqlite3` CLI; assert every user-authored field is legible without the app"*, BLOCKING), and the key would sit in the Keychain with the same after-first-unlock availability as the file, so the gain against a device thief is small [J]. Its one real use would be making OS backups unreadable, and §5 handles that more simply.

### 3.4 The one serialiser is the main untrusted-input surface

`core/store/archive/` parses files from outside the app (DATA-5 restore and DATA-15 competitor import). DATA-15(d) already requires a hostile-input fixture. **Condition C14:** the same fixture applies to **DATA-5**, because an own-format archive can also be sent to a user by someone else; entries in the zip are never used as filesystem paths (no zip-slip); sizes are capped before decompression; the JSON is validated against the published schema before any write; and the whole import is one transaction. **The zip library is a production dependency parsing untrusted input**, not named by the architecture; it needs CSO approval at the DATA-3 ticket.

---

## 4. The CTO's finding 1 — two SQLite copies, one file: the security view

**I accept the finding and support the fix** (two files, one owner each). The evidence is at source: SQLite's own page on corruption, and Expo SQLite compiling its own copy on both platforms, which I confirmed separately in the expo-sqlite source (the iOS default directory code and the vendored sources in the README) [E, §9]. The security side:

1. **Corruption is an integrity and availability failure of the user's only copy.** With backups off by default (DATA-6) and possibly excluded from OS backups (§5), a corrupted journal may be unrecoverable. Removing the corruption path by construction is worth more here than in an app with a server [I].
2. **Separate protection classes become possible** (§3.3): `capture.db` must be writable while locked; `journal.db` need not be.
3. **Separate backup treatment becomes possible** (§5): both files are sensitive, and both are excluded under my recommendation, but they can be handled per file.
4. **Entitlement leaves the journal file.** VPAGE-4 (*"no entitlement read is reachable from any journal query"*) becomes structural, as the CTO says.
5. **Minimisation.** `capture.db` holds unconfirmed candidates, which are location points the user has not chosen to keep. **Condition C15:** a written retention rule for `capture.db` — adopted or discarded candidates, and expired ones (CONF-15's 30 days), are deleted from it, not only flagged — so the capture file does not become a second, silent location history. Article 4: *"Collect the minimum data necessary, state why, and delete it when no longer needed."* DATA-4's export must still cover whatever `capture.db` holds while it holds it (the CTO's `archive/` reads both files, which is right).
6. **The idempotent adopt step** (proposals §4.B step 5) has no security downside I can see.

**What I did not check:** whether Expo SQLite's copy and the system copy could share locks in some configuration. The CTO's overturn test stands.

---

## 5. The CTO's finding 2 — OS backups copy the journal by default

**This is user-data policy, and so it is the CEO's decision** (Constitution 5.4: *"The following are never automated: … anything affecting user data policy"*). The CGO adds the legal view afterwards. I set out the facts, the options and my recommendation.

### 5.1 The facts, retrieved at source on 2026-09-28

**Android** [E, Android Developers, *Back up user data with Auto Backup*]:
- *"Apps that target Android 6.0 (API level 23) or higher automatically participate in Auto Backup."* Expo's `android.allowBackup` *"Defaults to the Android default, which is `true`"* [E, Expo app config reference].
- Included by default: files under `getFilesDir()` and *"Files in the directory returned by `getDatabasePath(String)`"*. Excluded: `getCacheDir()`, `getCodeCacheDir()`, `getNoBackupFilesDir()`. **Expo SQLite's default directory is `filesDir/SQLite`** [E, expo-sqlite source], so **the journal and the capture file are in the default backup set.**
- Where it goes: *"a private folder in the user's Google Drive account, limited to 25 MB per app."* Over 25 MB, the system *"doesn't back up data to the cloud"*, and resumes if the size falls back under.
- Encryption: *"end-to-end encrypted on devices running Android 9 or higher using the device's PIN, pattern, or password"*, **only if** the user *"has set a screen lock"*. Apps can set `disableIfNoEncryptionCapabilities` in `<cloud-backup>` *"to make sure the backup happens only if it can be encrypted"*.
- **Cloud backup and device-to-device transfer are configured separately**: *"Each section of the configuration (`<cloud-backup>`, `<device-transfer>`, `<cross-platform-transfer>`) contains rules that apply only to that type of transfer."* And for apps targeting Android 12+, `allowBackup="false"` on some devices *"disables cloud-based backup and restore … but doesn't disable device-to-device transfers"*.
- Backups run when the user has backup enabled, *"At least 24 hours have elapsed"*, the device is idle, and on Wi-Fi (unless mobile data is allowed).

**iPhone** [E, Apple, *Optimizing your app's data for iCloud backup*; Apple Support 102651 and 122234]:
- iCloud Backup *"periodically creates a backup of the user's device, including your app's data"*. `tmp` and `Library/Caches` are excluded by default. **Expo SQLite's default directory on iOS is `Documents/SQLite`** [E, expo-sqlite source], which is backed up.
- Files and directories can be marked excludable, and a whole directory can be marked. **Two caveats in Apple's own words:** *"certain file operations can reset resource values, make sure you set an excluded file's resource values each time you save it"*; and the flag *"exists only to provide guidance to the system … it's not a mechanism to guarantee those items never appear in a backup or on a restored device."*
- Apple also advises developers **not** to exclude user-created data that *"might be difficult, even impossible, for the user to re-create"* on a restored device. That is Apple's guidance about user experience, not a rule, and it cuts against exclusion; I record it so the CEO sees both sides.
- **Who can read an iCloud Backup.** Under Standard Data Protection, *"the keys to your backups are secured in Apple data centers"*; only Advanced Data Protection makes iCloud Backup end-to-end encrypted. **Apple *"can no longer offer Advanced Data Protection in the United Kingdom to new users"*, and iCloud Backup is among the categories that fall back to Standard Data Protection** (Apple Support 122234, published 2025-09-22). A secondary source reports the position unchanged in 2026, with Apple's tribunal complaint still undecided [E, **single source, secondary**, TechTarget / search result; not relied on beyond "unchanged"].
- **Not retrieved:** whether an excluded file is carried by iPhone-to-iPhone Quick Start transfer. Apple's "not a guarantee" sentence means we should not promise either way.

**What this means, plainly** [I, from the above]:
- **Android, default:** after a day or so, a copy of the journal and the capture file goes to the user's Google Drive. It is end-to-end encrypted only if the phone has a screen lock.
- **iPhone, default:** if the user has iCloud Backup on, which is common [K, moderate], a copy goes into iCloud Backup, **which Apple can decrypt for every UK user who has not had ADP since before February 2025**. An unencrypted local backup on a computer would hold it too [K, high confidence].
- **Android's 25 MB quota:** `venues.db` alone is about 21 MB (`android-and-stack-note.md` §2.3). Left in the backup set with a growing journal and photo thumbnails, backups would **silently stop** [I]. So "include" is not even reliable without work.

### 5.2 The options

| | **Option 1 — Exclude from OS cloud backups** *(recommended)* | **Option 2 — Include (the platform default)** | **Option 3 — Let the user choose** |
|---|---|---|---|
| **What it is** | Android: `dataExtractionRules` exclude the journal, capture and venue files from `<cloud-backup>`; `fullBackupContent` equivalent for Android 11 and below. iOS: store directory in `Application Support/<bundle id>/` marked excluded, and the flag re-applied after every file replacement and on each launch. **Device-to-device transfer on Android kept** (`<device-transfer>` includes the journal), because it moves the data phone to phone without a cloud copy. | Do nothing, except exclude `venues.db` and the diagnostics log (they are reproducible or disposable). Optionally `disableIfNoEncryptionCapabilities` on Android. | A setting, **default off** (DFLT-1), "Include Haunts in my phone's backups", with one plain paragraph on who can read each platform's backup. iOS: the flag set at runtime. Android: manifest rules are static, so this needs a small custom `BackupAgent` that checks the setting [K, high confidence it is possible; not built]. |
| **PRIV-1's first sentence** — *"Your timeline, notes and ratings never leave your device unless you switch on backup."* | **True on Android.** On iPhone, true as far as Haunts can make it: Apple calls the flag *"guidance"*, so the wording must not promise more than "Haunts asks your iPhone to leave it out". **CGO to judge.** | **False by default on both platforms.** On Android, the journal leaves the device to Google with no choice made. On iPhone, it leaves inside an Apple-readable backup. D12's test was *who receives your data*; here Google and Apple receive it. | True for users who leave it off; for users who switch it on, it is *their* choice, which matches the sentence's own "unless you switch on" logic, if the CGO agrees the wording covers it. |
| **"Haunts sends your data nowhere else"** (§12.2.8) | Consistent | **Arguably false**, and CRA 2015 s.36(3) makes it a contract term (as recorded under PRIV-1). The CTO's point that the phone's backup "is the phone's" is a real distinction on iPhone; it is weak on Android, where the app's own manifest opts it in [J]. **CGO.** | Consistent, if worded for the choice |
| **DATA-6** (*"Nothing leaves the device until the user chooses it"*) and **DATA-12 / Condition 7** | Consistent | **In tension with both.** The compliance note's objection that led to DATA-12 applies directly: *"ciphertext of a person's location history would sit in their iCloud indefinitely with no in-app way to remove it"* (`compliance-note.md` §3.5, quoted in DATA-12). Here it would not even be ciphertext to Apple. | Consistent; the setting screen must say how to remove it from the phone's backup (the app cannot) |
| **PRIV-2** (Privacy screen shows every transmission path) | Shows "Phone backups: Haunts is left out" | Must show the OS backup as a live transmission path | Shows the setting's state |
| **Data loss** | **The real cost.** A lost, stolen or broken phone loses the journal unless the user saved a Haunts backup file or export. A new iPhone restored from iCloud arrives with an empty Haunts [I]. Android phone-to-phone transfer still carries it if kept. | Lowest, **on paper**: an iCloud restore brings the journal back. On Android, only while under 25 MB and only after a day's delay. | As Option 1 by default; as Option 2 for users who opt in |
| **Build cost** [J] | Small: manifest XML via config plugin, one native call on iOS, one QA test per platform (≈ 0.5–1 day) | Near zero, plus the 25 MB problem to solve | Option 1 plus the setting, the Android `BackupAgent`, and copy for the CGO (≈ 2–4 days more) |
| **Protective default (DFLT-1)** | Yes | No | Yes |

**A fourth route, considered and rejected:** include the files, but encrypt the journal with a key that never leaves the device, so the OS backup holds unreadable ciphertext. It breaks DATA-1 (BLOCKING, *"every user-authored field is legible without the app"*), and a restore to a new phone then yields data nobody can read, so it gives the privacy of Option 1 with none of Option 2's recovery [I].

### 5.3 My recommendation: Option 1, with the honesty that makes it fair

**Exclude the journal, capture and venue files from OS cloud backups on both platforms; keep Android's device-to-device transfer; and say so plainly where it matters** [J]. The reasons, in order:

1. **The promise.** The product's one surviving differentiator is *"Candour receives nothing, and your data goes nowhere but your own cloud"* (`requirements.md` §20.1 item 5). A default that sends a copy to Google, or an Apple-readable copy to iCloud, without the user choosing it, contradicts DATA-6 in substance. With ADP unavailable to new UK users, "your own cloud" on iPhone is not end-to-end encrypted.
2. **The recovery path already exists and is honest.** DATA-5 (import), DATA-3 (export) and the encrypted backup file give the user a copy they can see, move and delete. Option 2's recovery is invisible, undeletable from the app, and on Android silently capped.
3. **It is the protective default** the CEO set at D24.

**What it costs, said plainly:** some users will lose their journal with their phone. That is serious, and Article 1.3 (*"We say what a product cannot do"*) requires the app to say it, **once, in plain words, without nagging** (DATA-9, DATA-11 bar scare modals): a line on the backup screen and the Privacy screen — for example, *"Your phone's own backups don't include Haunts. To keep a copy, save a Haunts backup."* — and a line in onboarding. Wording is UX's and the CGO's.

**If the CEO weighs data loss more heavily**, Option 3 is the one I would accept: default off, the user's informed choice. I recommend it as a **post-launch candidate** rather than MVP, because of the extra Android native code and the copy the CGO would need to clear. **I do not recommend Option 2.**

**What would overturn this recommendation:** evidence that iCloud Backup is end-to-end encrypted for UK users by default (ADP restored), which would weaken reason 1 on iPhone; or user research showing the target user relies on phone backups and would not save a file, which would argue for Option 3 at launch. **Where I looked:** the sources in §5.1, the requirements' DATA and PRIV sections, `compliance-note.md` §3.5 as quoted in DATA-12, and D24.

**Acceptance criteria to hand the PM/BA if Option 1 is chosen** [J]: (a) Android: run a backup with the local test transport (`bmgr`, per Android's *Test backup and restore* page, not retrieved here) and assert none of the three database files, nor their `-wal`/`-shm`, is in the backup set, and that device-transfer includes the journal. (b) iOS: assert the excluded flag is set on the store directory and every file in it after first launch, after a migration and after an import; and inspect a real encrypted local backup for the files' absence. (c) The two sentences are present and are not repeated as prompts.

---

## 6. Dependencies and supply chain, per option

**Common to all three.** The architecture adds **no production dependency of its own** (proposals §6.7), and I confirm that from the design: no ORM, no state library, no HTTP client, no UI kit, no i18n library. That is the single best supply-chain decision in the document [J]. It adds development dependencies: ESLint and Expo's config, an import-boundary plugin, Jest, `jest-expo`, React Native Testing Library, and the Maestro CLI. `tools/check-*.ts` use no dependencies (D41). All are approved per D40/D41 **at the M1 scaffolding PR**, exact-pinned, with licences. I am not approving any here, because none is yet chosen at a version.

| Point | A | B | C |
|---|---|---|---|
| Import-boundary plugin | `eslint-plugin-import` or none | `eslint-plugin-import` or its fork | the plugin **plus** dependency-cruiser |
| Evidence on the candidates [E, npm registry, read 2026-09-28] | — | `eslint-plugin-import` 2.32.0, last published **2025-06-20**, 19 direct dependencies, MIT. `eslint-plugin-import-x` 4.17.1, published 2026-06-28, 9 direct dependencies, MIT. | `dependency-cruiser` 18.4.0, published 2026-09-20, 18 direct dependencies, MIT |
| Manifests to audit | 1 | 1 | 5 (root, app, four packages) |
| Duplicate-copy hazard | none | none | **Yes.** Expo names duplicate dependencies as a monorepo hazard (proposals, citing Expo). Two copies of `react` or `react-native` in one bundle is the same class of bug as two SQLite copies [I]. |
| Do the boundaries hold? | lint only | lint only (**C1** makes it hold in CI) | **Less than claimed.** npm workspaces link packages into the root `node_modules` [E, npm docs], and Node's resolver walks up to the root, so a package can import a dependency it never declared [K, high confidence]. The "walls" need dependency-cruiser's undeclared-dependency rule to be real [K, moderate]. |

**My view** [J]: **prefer `eslint-plugin-import-x`** (fewer dependencies, maintained this year) **or no plugin at all** — ESLint's built-in `no-restricted-imports`, scoped per folder with flat-config `files` globs and combined with a ban on `../` imports that leave a feature, can express B's zones. The CTO chooses; I approve at M1. **Option C adds supply-chain surface for no security gain.**

**Conditions for every option, at M1:**
- **C16. Lockfile discipline.** CI installs with `npm ci` from the committed lockfile. The dependency check (C4) reads the **resolved lockfile**, transitive entries included.
- **C17. Install scripts.** npm packages can run code at install time [K, certain]. At M1, list which installed packages have install scripts, and record the list in `docs/dependencies.md`; a new one appearing fails CI. (Turning scripts off globally may break Expo tooling; that is for the M1 spike to measure, not for me to assume.)
- **C18. Native dependencies are not locked by npm alone.** With continuous native generation, `/ios` and `/android` are generated and ignored (baseline §7), so `Podfile.lock` is not committed [I]. Pods and Gradle artifacts come mostly from versions fixed in `node_modules` podspecs and Gradle files, but a floating one would not be visible. CI should print the resolved pod and Gradle dependency lists for each release build and archive them with the source maps, so a change is visible after the fact [J].
- **C19. ESLint and commitlint run from the lockfile inside `pre-commit`** (`language: system` calling the locally installed binary), not through `pre-commit`'s own Node environment with separately declared `additional_dependencies`, which would be a second, unlocked copy [K, high confidence on pre-commit's `language: node` behaviour]. D41 already runs commitlint inside `pre-commit`; this keeps one version of each tool.
- **C20. Maestro CLI** is installed from a pinned release with a checksum check, not a piped install script, the same rule the baseline applied to gitleaks in CI.
- **Unchanged from the baseline:** EAS Update stays off without code signing (baseline §8.4). The architecture declares no update channel, which is correct.

---

## 7. Where secrets and keys live

**The app carries no runtime secret, and the architecture keeps it that way** [I, from the design]: no server, no API key, no map token (MapLibre with local sources only), no crash SDK key. Signing and distribution credentials stay where the baseline put them (§8.1: EAS-managed credentials, password manager, never a working tree). Three additions:

1. **`app.config.ts` is executed at build time and its `extra` values ship inside the app** [K, high confidence]. **Condition C21:** no `process.env` value is read into `extra` or into `EXPO_PUBLIC_*`, enforced by a grep in `tools/`. The baseline already bans secrets in `EXPO_PUBLIC_*`.
2. **The backup key (SPK-06, still mine and still open).** The architecture gives the KDF its own small native module, which is right. **Condition C22, for SPK-06 to confirm:** at MVP nothing derived from the passphrase is stored on the device; if a later design stores a key or passphrase for convenience, it goes in the Keychain with a `ThisDeviceOnly` accessibility class and in the Android Keystore as non-exportable, so it never travels in a backup or iCloud Keychain [K, high confidence on both platforms' semantics]. **Note for SPK-06:** PBKDF2 is available in both platforms' own libraries with no dependency; Argon2id and scrypt are not [K, high confidence]. That trade-off is SPK-06's to settle, and nothing in this architecture forecloses either.
3. **The recovery key on the clipboard** (DATA-8 offers "Copy"). On iPhone, a copied item can reach the user's other devices through Universal Clipboard unless marked local-only, and it can be given an expiry [K, high confidence]; Android 13+ supports marking clip content sensitive so it is hidden in the clipboard preview [K, high confidence]. **Flag to the DATA-8 ticket and to UX:** copy the key local-only, with an expiry, and marked sensitive. It may need a few lines of native code if `expo-clipboard` does not expose these [K, unverified].

---

## 8. Does anything weaken the security baseline (D32, D43)?

**No control in the baseline is removed or loosened by any option.** Three places where the architecture creates something the baseline's logic should now cover:

1. **Lint suppression is the new `gitleaks:allow`.** Covered by **C1**: CI runs ESLint with `--no-inline-config` (or `linterOptions.noInlineConfig: true`) for at least the boundary, network and SQL rules, and with `reportUnusedDisableDirectives` [E, ESLint]. A local disable comment then passes the hook and fails CI, exactly as the baseline designed for gitleaks.
2. **New guard-rail files.** `eslint.config.js` (its boundary, network and SQL rules and the `http` allow-list), `tools/check-network.ts`, `tools/check-capture-isolation.ts`, `docs/dependencies.md`, and the config plugins that strip `INTERNET` and set backup rules are now security controls. **Condition C23:** add them to the baseline's list of files that change only with a CSO note and CEO approval (`SECURITY.md` "Changes to the guard rails" and the `haunts/CLAUDE.md` agent rule 3). That is a change to the baseline, so it needs the CEO's approval as D43 did; I propose it here and it goes to him with the ADR.
3. **Source maps (DATA-14)** are archived outside the repository and are never shipped in the bundle; they are larger than the 1 MB large-file hook allows, so the hook already stops an accidental commit [I].

---

## 9. Conditions, flags and the evidence register

### 9.1 Conditions for the ADR (whichever option is chosen)

| # | Condition | Why | Owner |
|---|---|---|---|
| C1 | CI runs ESLint with inline configuration disabled for security rules, plus `reportUnusedDisableDirectives` | Closes the lint-comment bypass (§2, §8) | CTO, M1 |
| C2 | `no-restricted-imports` bans `expo/fetch`, `expo-file-system` network functions, `expo-image` remote sources, `react-native-webview`, `expo-web-browser`, `expo-updates` and `Image.prefetch`, alongside the global ban | PRIV-8 layer 1 misses imported networking | CTO, M1 |
| C3 | Widen `check-network.ts`'s native deny list (§2 table) | PRIV-8 layer 2 | CTO, M1 |
| C4 | The dependency check covers the full resolved lockfile and the autolinked native modules, not only direct production dependencies | PRIV-8 says *"the dependency tree"* | CTO, M1; CSO reviews the list |
| C5 | The `INTERNET` spike runs before M1 ends; on iOS, the release network capture is a release gate and QA adds App Privacy Report | Only mechanical third-party layer is Android's | CTO; QA |
| C6 | If cloud backup is ever chosen, the transport accepts only a ciphertext type | Keeps plaintext off the one network path | CTO, at that decision |
| C7 | `ios/Core` compiled as its own Swift module, or the check greps Bridge type names | Swift same-module visibility defeats an import grep | CTO, M1 |
| C8 | No SQL built by string interpolation, JS or native, checked mechanically | Injection | CTO, M1 |
| C9 | Stores live in `Library/Application Support/<bundle id>/` on iOS, via the `directory` parameter | Expo's default is `Documents/` | CTO, M1 |
| C10 | iOS protection class set and tested on each store file and its `-wal`/`-shm`/`-journal` | Data at rest | Engineer; QA |
| C11 | Android capture not `directBootAware`; no device-protected storage | Data at rest before unlock | Engineer |
| C12 | Export and backup staging files in cache, deleted after the share sheet | Temporary plaintext | Engineer |
| C13 | HEAD-12's privacy cover gets a native home and a ticket | Not placed by any option | CTO; PM/BA |
| C14 | DATA-15(d)'s hostile-archive fixture also applies to DATA-5; zip library approved by CSO | Untrusted input | PM/BA; CSO |
| C15 | Retention rule for `capture.db` (delete, not only flag) | Minimisation, Article 4 | PM/BA; CTO |
| C16–C20 | Lockfile, install scripts, native dependency record, lint from lockfile, Maestro pinned | Supply chain (§6) | CTO, M1 |
| C21 | No environment values into `extra` or `EXPO_PUBLIC_*` | Secrets in the binary | CTO, M1 |
| C22 | No stored backup key at MVP; `ThisDeviceOnly` / non-exportable if ever stored | Keys | CSO, SPK-06 |
| C23 | New guard-rail files join the baseline's protected list (needs CEO approval, like D43) | Baseline | CEO |

None of these changes the choice between A, B and C, and none adds running cost. I estimate C1–C23 at **1.5–3 days** of work inside the M1 set-up rows [J].

### 9.2 Flags, to the seat that holds each

- **CEO:** the OS-backup decision (§5), after the CGO. Also C23.
- **CGO:** whether PRIV-1 and §12.2.8's sentence stay true under each backup option, and the iPhone wording given Apple's *"guidance"* caveat (§5.2).
- **PM/BA:** DATA-1/DATA-2 wording (the CTO's §24 row, which I support); C13, C14, C15 as criteria; §5.3's acceptance criteria if Option 1 is chosen.
- **UX / PM/BA:** whole-app privacy cover rather than per-screen (§3.3); the two plain sentences about phone backups (§5.3); the clipboard handling of the recovery key (§7).
- **Entitlement spike:** native, signed entitlement over a JS-written one (§3.2).
- **CTO:** no disagreement with the recommendation of B. **One disagreement, stated once:** §4.C says Option C's boundaries *"are walls, not rules: they cannot be switched off by a lint comment"*. Under npm workspaces they are not walls without a further tool (§6); I would not want the CEO to choose C on that claim.

### 9.3 Evidence register

All retrieved 2026-09-28 by this seat. Vendor pages are single-source for their own products.

| # | Claim | Source |
|---|---|---|
| S1 | Auto Backup participation from API 23; default file set incl. `getDatabasePath`; exclusions; Google Drive, 25 MB limit and behaviour over it; E2E encryption with screen lock from Android 9; `disableIfNoEncryptionCapabilities`; separate `cloud-backup` / `device-transfer` sections; `allowBackup="false"` and device transfer on Android 12+; backup conditions | [Android Developers, Back up user data with Auto Backup](https://developer.android.com/identity/data/autobackup) |
| S2 | `android.allowBackup` defaults to the Android default, `true` | [Expo, app config reference](https://docs.expo.dev/versions/latest/config/app/) |
| S3 | iCloud Backup includes app data; `tmp`/`Caches` excluded; exclusion by resource value, per directory; resource values can be reset by file operations; the flag is guidance, not a guarantee; advice on user-created data; bundle-id folder naming | [Apple, Optimizing your app's data for iCloud backup](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup), read through Apple's documentation JSON endpoint because the page renders client-side |
| S4 | Standard Data Protection: iCloud Backup keys held by Apple; ADP makes it end-to-end | [Apple Support 102651, iCloud data security overview](https://support.apple.com/en-us/102651) |
| S5 | ADP no longer offered to new UK users; iCloud Backup falls to Standard Data Protection | [Apple Support 122234](https://support.apple.com/en-us/122234) (published 2025-09-22) |
| S6 | UK position unchanged in 2026; Apple complaint at the Investigatory Powers Tribunal | Web search summary citing [TechTarget](https://www.techtarget.com/cybersecurity/news/366619638/Apple-pulls-Advanced-Data-Protection-in-UK-sparking-concerns) and others — **secondary, single source, not load-bearing** |
| S7 | Data Protection classes and the default class for third-party app data | [Apple Platform Security, Data Protection classes](https://support.apple.com/guide/security/data-protection-classes-secb010e978a/web) |
| S8 | Expo SQLite default directory: iOS `documentDirectory/SQLite`, Android `filesDir/SQLite`; `directory` parameter on open | [`ios/SQLiteModule.swift`](https://github.com/expo/expo/blob/990f8adff1d9aa350671515fcc32364c1fab8811/packages/expo-sqlite/ios/SQLiteModule.swift), [`SQLiteModule.kt`](https://github.com/expo/expo/blob/990f8adff1d9aa350671515fcc32364c1fab8811/packages/expo-sqlite/android/src/main/java/expo/modules/sqlite/SQLiteModule.kt), [`src/SQLiteDatabase.ts`](https://github.com/expo/expo/blob/990f8adff1d9aa350671515fcc32364c1fab8811/packages/expo-sqlite/src/SQLiteDatabase.ts), expo `main` at `990f8ad` |
| S9 | Expo SQLite vendors SQLite and SQLCipher sources | [expo-sqlite README @990f8ad](https://github.com/expo/expo/blob/990f8adff1d9aa350671515fcc32364c1fab8811/packages/expo-sqlite/README.md) |
| S10 | `import { fetch } from 'expo/fetch'` | [Expo SDK, `expo` package reference](https://docs.expo.dev/versions/latest/sdk/expo/) |
| S11 | `noInlineConfig`, `--no-inline-config`, `reportUnusedDisableDirectives` | [ESLint, Configure rules](https://eslint.org/docs/latest/use/configure/rules) |
| S12 | npm workspaces are symlinked into the root `node_modules` | [npm docs, workspaces](https://docs.npmjs.com/cli/v11/using-npm/workspaces) |
| S13 | Versions, dates, licences and dependency counts of `eslint-plugin-import`, `eslint-plugin-import-x`, `dependency-cruiser` | [npm registry](https://registry.npmjs.org/) (`/eslint-plugin-import`, `/eslint-plugin-import-x`, `/dependency-cruiser`) |

**[K] claims carried, each to be upgraded before it anchors a ticket:** Swift same-module visibility without imports (§3.1, certain); sockets need `INTERNET` and Play Billing works over IPC (§2); iOS App Privacy Report (§2); `-wal`/`-shm` failures under `Complete` when locked (§3.3); iOS snapshot written to disk and JS `AppState` timing (§3.3); direct-boot storage semantics (§3.3); Node resolution of hoisted dependencies (§6); pre-commit `language: node` environments (§6); npm install scripts (§6); `extra` shipped in the app (§7); `ThisDeviceOnly` and non-exportable key semantics, platform PBKDF2 availability (§7); Universal Clipboard local-only and Android sensitive-clip flag (§7); iCloud Backup commonly on (§5.1); the Android custom `BackupAgent` route for Option 3 (§5.2).

**What would overturn this review's main findings, and where I looked.** *PRIV-8 gap (C1, C2):* evidence that CI already runs ESLint without inline config, or that no import-based network API exists in the dependency set. *Option C's walls:* a demonstration that the workspace setup refuses an undeclared import without dependency-cruiser. *OS backups:* see §5.3. **Where I looked:** the proposals in full, the requirements and decision record sections listed at the top, the baseline, and the sources in §9.3.

---

## 10. Change log

| Date | Change |
|---|---|
| 2026-09-28 | First version (CSO), for SPK-20 / D59. Written incrementally after an interrupted session; no earlier draft existed. |

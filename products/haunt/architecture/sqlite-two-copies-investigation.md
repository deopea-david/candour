# Two copies of SQLite in one process — is the corruption hazard real for Haunts?

**Seat:** Engineer (Haunts) · **Model:** Opus · **Date:** 2026-09-28 · **Status:** complete, for the CTO and CEO; not committed
**Commissioned by:** main session, at the CEO's request · **Question:** is the "two SQLite copies, one file" hazard in `architecture-proposals.md` §5 a real issue for Haunts or a theoretical one, and what is the cheapest sound fix?
**Evidence standard:** `pipeline/evidence-standard.md` v1.1. Tags [E]/[K]/[I]/[J]; every [E] carries the link it was retrieved from this session.

## 0. Plain answer

**It is a real issue, not a theoretical one, and it is broader than the CTO's document says.**

- **Both halves of the premise are confirmed at source.** Expo SDK 58 compiles its own SQLite (3.53.3) into the app on iOS and Android, with no option to use the system library (§2.1). Swift and Kotlin would use the phone's own SQLite (§2.2).
- **I reproduced the failure on this Mac and in the iOS Simulator.** Two copies of SQLite on one file, in one process.
- **Between two ordinary SQLite builds (the Android pairing), it fails even with no concurrency.**
  - One side's ordinary close silently deleted the write-ahead log (the `-wal` file) the other side was still using.
  - Later writes that had reported success were lost.
  - SQLite's own `integrity_check` still said `ok`.
  - Under load, 10 of 10 runs lost data or crashed.
- **Apple's own SQLite behaves better (the iOS pairing).** It uses a different kind of lock that happens to see the other copy's locks, so ordinary one-at-a-time use survived. When both sides were busy at once, **8 of 10 runs in the iOS 26 Simulator crashed the process**.

**Likelihood with one shared file** [J]:
- **Android: near-certain.** The capture service runs in the app's process, and a routine app open or capture write is enough.
- **iOS: occasional.** It needs a visit to arrive while the app is actively using the database. The typical outcome is a crash, sometimes a lost write.

**Recommendation:**
- **Keep the CTO's two-file fix.** It is the only option that is sound on both platforms, uses only supported interfaces, and costs no more than the alternatives (§3).
- Add three small guards to the capture tickets (§5).
- Confirm on real phones at M1. That is for measurement, not to decide.

## 1. The mechanism, at source (SQLite)

### 1.1 What the documentation says

SQLite's *How To Corrupt An SQLite Database File* (page dated *"last updated on 2026-04-13"*) has two adjacent sections that together describe the hazard [E, S1]:

- **§2.2, the underlying quirk:** *"any thread in the same process with a file descriptor that is holding a POSIX advisory lock can override that lock using a different file descriptor. One particularly pernicious problem is that the close() system call will cancel all POSIX advisory locks on the same file for all threads and all file descriptors in the process."* It adds that it is *"perfectly safe for two or more threads to access the same SQLite database file using the SQLite library. The unix drivers for SQLite know about the POSIX advisory locking quirks and work around them."*
- **§2.3, the two-copies case:** *"Part of that work-around involves keeping a global list (mutex protected) of open SQLite database files. But, if multiple copies of SQLite are linked into the same application, then there will be multiple instances of this global list. Database connections opened using one copy of the SQLite library will be unaware of database connections opened using the other copy, and will be unable to work around the POSIX advisory locking quirks. A close() operation on one connection might unknowingly clear the locks on a different database connection, leading to database corruption."*
- **§2.3 on whether it happens in practice:** *"The scenario above sounds far-fetched. But the SQLite developers are aware of at least one commercial product that was released with exactly this bug. The vendor came to the SQLite developers seeking help in tracking down some infrequent database corruption issues they were seeing on Linux and Mac."* The fix they report: *"change the application build procedures to link against just one copy of SQLite instead of two."* **(single source** — SQLite's own account of an unnamed vendor; I found no independent report of that incident.)
- **§2.2 on recent defences:** *"Beginning with SQLite version 3.51.0 (2025-11-04), SQLite implements additional defenses to try to avoid problems caused by locks that are broken by close(). These new defenses help when the database is in WAL mode and is being accessed from multiple processes. But they are not a cure-all."* Note the words **"from multiple processes"**. §1.3 shows why the defence does not reach the one-process, two-copies case.

**SQLite forum.** A 2022 thread asks about exactly this: two shared libraries in one app, each with its own SQLite, one file. Richard Hipp (SQLite's author) replies: *"It does seem like you are vulnerable."* On the mechanism: *"SQLite works around this design bug by using global variables and mutexes to keep track of all open file descriptors to the same file … This work-around breaks down if you have two or more copies of SQLite linked, because each copy of SQLite comes with its own set of global variables."* Larry Brasfield (SQLite team) confirms that linking both against one shared SQLite solves it [E, S23]. Hipp also offers an application-level work-around: *"do not close database connections while other database connections to the same database are active."* **That work-around is not enough for Haunts**, where both sides write. My tests (§4.3, T1 and T2) show two writers granted the lock at once with no `close()` involved at all. The questioner's second library only read.

### 1.2 What the source code says — the problem is wider than `close()`

The documentation leads with `close()`. SQLite's own source, `src/os_unix.c` at tag `version-3.53.3` (the version Expo SDK 58 bundles, §2.1), shows a **broader** problem. Ordinary POSIX locks do not exclude anything *within* one process at all, so two copies that both use them never block each other, `close()` or no `close()` [E, S2]. (Apple's own build is the exception; it behaves differently, §4.3.)

> *"POSIX advisory locks are broken by design. … when a process sets or clears a lock, that operation overrides any prior locks set by the same process. … This means that we cannot use POSIX locks to synchronize file access among competing threads of the same process. POSIX locks will work fine to synchronize access for threads in separate processes, but not threads within the same process. To work around the problem, SQLite has to manage file locks internally on its own."*

The internal record is a per-inode structure (`unixInodeInfo`) held on a static list, `static unixInodeInfo *inodeList` [E, S2, line 1349]. The same comment block describes the `close()` work-around: *"When an attempt is made to close an unixFile, if there are other unixFile open on the same inode that are holding locks, the call to close() the file descriptor is deferred until all of the locks clear."* [E, S2].

A second copy of SQLite has its own `inodeList`. So, reasoning directly from the quoted source [I]:

1. **No mutual exclusion between the copies.** When copy B asks for a write lock, it consults only its own list (which does not know copy A holds one) and then calls `fcntl()`, which succeeds because the lock A holds belongs to the same process. Both copies can believe they hold the write lock at once.
2. **`close()` in one copy silently drops the other's locks** (the documented case), because the deferral above only knows about connections in its own list.

### 1.3 In WAL mode, a close can delete a live WAL file — no concurrent write needed

Haunts' requirements specify WAL (DATA-2: *"WAL and one-writer discipline"*). WAL has its own shared-memory locks, but they go through the same process-scoped `fcntl()` locks, and the "am I the last connection?" test on close is a lock test. `src/wal.c`, `sqlite3WalClose`, at the same tag [E, S3]:

> *"If an EXCLUSIVE lock can be obtained on the database file (using the ordinary, rollback-mode locking methods, this guarantees that the connection associated with this log file is the only connection to the database. In this case checkpoint the database and unlink both the wal and wal-index files."*

Within one process, copy A can always get that EXCLUSIVE lock however many connections copy B has open (§1.2, point 1). The 3.51.0 defence is `unixIsSharingShmNode`, which refuses the EXCLUSIVE lock if *"another process still holds locks on the SHM file"* [E, S2, lines 2034–2040]. It detects that with `fcntl(F_GETLK)` [E, S2, lines 4679–4695], and `F_GETLK` does not report locks held by the calling process itself [K, high confidence — POSIX semantics; §4's T3 result, where the 3.53.4 defence did not stop the deletion, is consistent with it]. So the defence cannot see the other copy, and **copy A's ordinary close would checkpoint and unlink the `-wal` and `-shm` files while copy B still has them open.** SQLite's §2.5 says what happens after that: *"unlinking or renaming an open database file results in behavior that is undefined and probably undesirable"* [E, S1].

The **open** path has the mirror-image problem. `unixLockSharedMemory` (line 4850): *"Use F_GETLK to determine the locks other processes are holding on the DMS byte. … if no other process is holding any lock, then this process is the first to open it. In this case take an EXCLUSIVE lock on the DMS byte and truncate the \*-shm file"*, which it does with `robust_ftruncate(pShmNode->hShm, 3)` (line 4902) [E, S2]. A second copy opening in the same process therefore concludes it is first, and truncates the shared-memory file the other copy has mapped.

That matters for likelihood: this route needs no two writes to collide in the same millisecond. It needs only **one copy to close its last connection while the other copy still has one open** — which, in the one-file design, is the normal life of the app (§2.3). §4 tests whether it actually happens.

## 2. Does it apply to Haunts?

### 2.1 Does `expo-sqlite` bundle its own SQLite?

**Yes, on both platforms, with no option to use the system library.** Pinned to **expo-sqlite 58.0.6** (npm `next` tag, published 2026-09-25; `latest` is 57.0.3), whose npm `gitHead` is expo/expo commit `ad41d067bd3df6dd12f1788acc6b54a68e7a650d` [E, S4]. Every file below was read at that SHA.

| Fact | Evidence |
|---|---|
| The bundled copy is **SQLite 3.53.3** (`#define SQLITE_VERSION "3.53.3"`, source id dated 2026-06-26) | `vendor/sqlite3/sqlite3.c`, lines 470–472 [E, S5] |
| Its public symbols are **renamed** from `sqlite3_*` to `exsqlite3_*` (e.g. `SQLITE_API int exsqlite3_libversion_number(void);`) | same file, line 512 [E, S5]; the README's update steps include *"Replace sqlite3 symbols to prevent conflict with iOS system sqlite3"* [E, S6]; `scripts/replace_symbols.ts` rewrites the vendored source, `ios/SQLiteModule.swift`, and the Android JNI files [E, S7] |
| **iOS (CocoaPods):** `vendor_sqlite_src!` copies `vendor/sqlite3/sqlite3.c` and `sqlite3.h` into the pod, which compiles them with `-DSQLITE_ENABLE_LOCKING_STYLE=0` (plain POSIX locking) plus FTS5, session and other flags; `s.static_framework = true`, `DEFINES_MODULE = YES` | `ios/ExpoSQLite.podspec` [E, S8] |
| **iOS (Swift Package Manager, the new prebuild path):** a C target `ExpoSQLite_c` built from `vendor/sqlite3` with the same flags | `spm.config.json` [E, S9] |
| The iOS module opens databases with the renamed symbol: `exsqlite3_open(path.toFilePath(), &db)` | `ios/SQLiteModule.swift`, line 140 [E, S10] |
| **Android:** CMake builds one shared library, `expo-sqlite`, from the JNI sources **and** `"${SQLITE3_SRC_DIR}/sqlite3.c"`; Gradle points `SQLITE3_SRC_DIR` at `vendor/sqlite3` (or `vendor/sqlcipher`) | `android/CMakeLists.txt`, `android/build.gradle` [E, S11, S12] |
| **The only build options** in the config plugin are `customBuildFlags`, `enableFTS`, `useSQLCipher`, `withSQLiteVecExtension`, and a deprecated `useLibSQL` that *"no longer has any effect"*. **There is no option to use the system SQLite.** SQLCipher is also bundled, so it is still a separate copy | `plugin/src/withSQLite.ts` [E, S13] |
| The Kotlin binding class is `internal class NativeDatabaseBinding`; the iOS database class is `final class NativeDatabase` with default (internal) access. **Neither is callable from another module** | `NativeDatabaseBinding.kt`, `NativeDatabase.swift` [E, S14, S15] |

So Expo's copy is a second, private SQLite in the app on both platforms. Renaming the symbols stops the two copies **clashing at link time**; it does nothing about the **run-time** lock problem in §1, because each copy still has its own `inodeList` [I, from S2 and S5].

### 2.2 Which library would the native capture code use?

**The system's, on both platforms, unless we deliberately choose otherwise. On both platforms that is a different copy from Expo's.**

- **iOS.** The iOS SDK ships `usr/include/SQLite3.modulemap` (`module SQLite3 [system] { header "sqlite3.h" … }`) and `usr/lib/libsqlite3.tbd`, the stub for the OS's own library [E, read locally in `iPhoneOS27.0.sdk`]. `import SQLite3` in Swift links that. GRDB's README says the same for its default: *"import SQLite3 // System SQLite"* [E, S16]. SQLite.swift also defaults to the system library [K, medium-high]. On the iOS 26.0 runtime that library is **Apple's SQLite 3.51.0** (§4.1) [E].
- **Android.** Kotlin's `android.database.sqlite` (and Room over it) calls the framework's `libsqlite` [K, high confidence]. AOSP builds `libsqlite` from the upstream amalgamation (`srcs: ["sqlite-autoconf-%s/sqlite3.c"]`, currently 3.44.3/3.44.4 in `dist/`), with ordinary flags [E, S17]. Its Android patch adds fd-ownership tagging (`android_fdsan_…`) and extra error logging, and **does not change locking** [E, S18]. Those flags enable FTS3 and FTS4 but **not FTS5** [E, S17]. That answers the architecture document's open [K] question in the negative, and it matters for one alternative in §3. **Caveat (single source):** read on the `aosp-mirror/platform_external_sqlite` GitHub mirror, which is archived; `android.googlesource.com` returned HTTP 503 when I tried it. Device makers can also ship their own builds.

So the plan as written in DATA-1/DATA-2 puts two copies of SQLite on one file on both platforms: **Apple's plus Expo's upstream copy on iOS**, and **AOSP's upstream copy plus Expo's upstream copy on Android**. The architecture document's [K] premise (native uses the platform library) is now [E] for iOS and AOSP, and [K, high] for the Kotlin→`libsqlite` link.

### 2.3 Are both ever open on the same file, at the same time, in one process?

**Yes, routinely, on both platforms.** No rare coincidence is needed.

- **Android.** The capture foreground service runs in the app's process unless we say otherwise. Android's `<service>` reference: *"Normally, all components of an application run in the default process created for the application"*; only a `process` name beginning with `:` creates *"a new process, private to the application"* [E, S19]. Whenever the user opens the app while capture is running (the normal daily case), JavaScript and Kotlin are in one process, and both hold the file open. Expo's `SQLiteProvider` keeps its connection open for the provider's lifetime [K, medium-high]. A Kotlin `SQLiteOpenHelper` is conventionally held open for the process lifetime [K, high].
- **iOS.** Apple's `startMonitoringVisits()` reference: *"If your app is terminated while this service is active, the system relaunches your app when new visit events are ready to be delivered."* [E, S20]. On a **cold** relaunch, CAP-1(a) itself requires that JavaScript never starts: its test is to *"kill the app, deliver a synthetic visit on each platform, assert the visit is in SQLite and Hermes never started"* (`requirements.md`, CAP-1). In that case only one copy is in the process. But when the app is **already running or merely suspended**, which is the common case, the process and JavaScript's open connection already exist, so the visit's native write lands beside it [I]. CAP-1 keeps JavaScript out of the recording path. It does not keep JavaScript out of the process.
- **What "at the same time" needs.** From §4, "at the same time" does not need two writes in the same millisecond:
  - **Android pairing:** one side merely closing while the other has the file open lost data (T3, T3b). So does one side opening while the other is open, because the opener believes it is the first and rebuilds the shared index (the SIGBUS mechanism).
  - **iOS pairing:** it takes real overlap around a connection opening or closing (T5). That is plausible when a visit arrives while the user has the app open, and unlikely while the app sits idle in the background [J].

### 2.4 Does WAL mode change the risk?

**It makes it worse, not better.**

- WAL's coordination lives in the `-shm` shared-memory file and its locks. Those locks are the same process-scoped `fcntl()` locks, tracked per copy (§1.2).
- WAL adds two single-copy decisions that go wrong when another copy is invisible:
  - on close, *"am I the last connection? then checkpoint and delete the WAL"* (§1.3);
  - on open, *"am I the first? then rebuild the shared index"*.
- T3/T3b show the first; the SIGBUS crashes and the 3-byte `-shm` file show the second (§4.3).
- SQLite 3.51.0's new defence against broken locks is explicitly for access *"from multiple processes"* [E, S1]. Both upstream copies in my test (3.53.4) include it and still failed.
- Rollback-journal mode is not safe either: T1 and T4 fail in it.

**A separate, smaller WAL point that affects the two-file design too.** SQLite's WAL page describes a **WAL-reset bug**:

- It is *"likely present in all version of SQLite from 3.7.0 (2010-07-21) through 3.51.2 (2026-01-09)"* and *"fixed in version 3.51.3"*.
- It *"only affects databases in WAL mode when there are two or more database connections open on the same file, in separate threads or processes, and when those two connections attempt to write or checkpoint at the same instant"*.
- It is *"unlikely to occur in common use"* [E, S21].

The iOS 26.0 system SQLite is **3.51.0** (§4.1), so native code on the system library is exposed if it runs two connections to `capture.db` on different threads. The cheap guard: **one connection, on one serial queue**. Since capture writes are tiny and rare, rollback-journal mode for `capture.db` is another option [J]. This is a note for the capture module's ticket, not a reason to change the design.

## 3. Mitigations other than two files

Each is judged on four things: does it remove the hazard on **both** platforms; is it **supported** (documented, so an SDK upgrade won't silently break it); what it **costs to build**; and what it **costs to run** (Constitution 1.5; all options below are £0 running, so build cost and fragility decide).

### 3.1 Native code calls Expo's own copy (one copy)

- **iOS: technically possible, unsupported.**
  - The pod is a static framework with `DEFINES_MODULE = YES`, and its source files include the vendored `sqlite3.h`, which declares the renamed `exsqlite3_*` functions [E, S8, S5].
  - A Swift capture module that does `import ExpoSQLite` could probably call `exsqlite3_open_v2` and friends directly [I, medium; not built]. Expo's own Swift does exactly that inside the module (`exsqlite3_open(...)`, S10).
  - Nothing in Expo documents this as an interface. The `ex` prefix, the build flags and the packaging (CocoaPods today, an SPM prebuild target `ExpoSQLite_c` too in SDK 58, S9) are all Expo's internal choices.
- **Android: possible only by reaching into Expo's native library.**
  - The Kotlin binding is `internal` [E, S14], so Kotlin cannot use it.
  - expo-sqlite does not publish its headers as a prefab package: `build.gradle` sets `prefab true`, which *consumes* fbjni, and there is no `prefabPublishing` [E, S12].
  - We would need our own JNI C file that `dlopen`s `libexpo-sqlite.so` and looks up ~15 `exsqlite3_*` functions by name. That also assumes they are exported, which I did not verify [I, low-medium].
- **Also:**
  - CAP-1(b)'s capture-isolation check would have to accept a dependency on `expo-sqlite`, a package whose job is the JavaScript bridge.
  - Every Expo SDK upgrade becomes a native-compatibility check on both platforms.
- **Verdict: works in principle, removes the hazard, but is fragile and unsupported.** Build ≈ 2–4 days per platform plus a recurring upgrade check [J]. **Not recommended.**

### 3.2 Configure `expo-sqlite` to use the system SQLite

**Not available.**

- SDK 58's config plugin offers no such option (the full list is in §2.1) [E, S13]; `libSQL` support was removed.
- On Android it could not exist in any form that helps: apps cannot link the framework's `libsqlite` from native code [K, high — it is not an NDK stable API].
- **What would overturn this:** a future Expo option to use the system library. It would fix iOS only.

### 3.3 A different JavaScript SQLite library that uses the iOS system SQLite

- **op-sqlite** (MIT) documents an `iosSqlite` option that *"uses the embedded iOS version from sqlite"*, and adds: *"On Android SQLite is always compiled from source"* [E, S22].
- On iOS, JavaScript and Swift would then share Apple's one copy. **On Android the two-copy problem remains**, and it is the worse platform (§4.3).
- It would also replace a first-party Expo module with a third-party one.
- **Verdict: fixes the easier platform only. Not recommended.**

### 3.4 Native owns the whole database; JavaScript reads and writes only through the native module

- **Removes the hazard if, and only if, `expo-sqlite` never opens that file.** Then only one copy exists.
- The cost is large:
  - a general database bridge (query, transaction, change events) written twice, in Swift and Kotlin;
  - on Android it cannot be the framework library, because FTS5 is not compiled in (§2.2) and VEN-4 and CONF-5 need it, so Kotlin would bundle its own SQLite anyway;
  - Expo SQLite's JavaScript API and change listeners would be lost.
- It inverts the reason React Native was chosen (`android-and-stack-note.md` §2.7, as the architecture document says).
- **Verdict: removes the hazard but costs the most. Not recommended.**

### 3.5 JavaScript does all the writes

**Rejected by requirement.** CAP-1 (BLOCKING): *"The Swift and Kotlin modules receive the platform event, read entitlement, and write to SQLite directly. JavaScript reads later."* (`requirements.md`, CAP-1).

### 3.6 Android capture in its own process (`android:process=":capture"`)

- Separate processes make ordinary POSIX locks work: the source says *"POSIX locks will work fine to synchronize access for threads in separate processes"* [E, S2].
- **Fixes Android only.** iOS has no equivalent for visit delivery [K, medium-high].
- It adds cross-process plumbing for everything else the service touches (entitlement, notifications, diagnostics).
- **Verdict: partial, and heavier than it looks. Not recommended on its own.**

### 3.7 Keep one shared file but make sure the two copies never overlap

For example, JavaScript closes its connection before native writes, or native keeps one connection open for ever.

- **Not credible as a guarantee:**
  - On Android, T3 shows that one side merely *closing* while the other is open loses data. On iOS, T5 shows that overlap around open and close crashes the process.
  - Preventing overlap would need a cross-language lock around every open, close and query. That lock would have to work while JavaScript is not running (CAP-1), which is the problem SQLite's own locking was supposed to solve.
- On iOS, Apple's different lock kind (§4.3) happens to protect sequential use today. That is undocumented behaviour and not something to build on [J].
- **Verdict: rejected.**

### 3.8 Two files, one owner each (the CTO's proposal)

- **Removes the hazard on both platforms by construction:** no file is ever opened by two copies (§1). It is also supported by every library involved, because each library only ever sees its own file.
- **Costs:** ≈ 1–2 days per platform of bridge functions; no transaction spans capture and journal (handled by the idempotent adopt step, `architecture-proposals.md` §4.B step 5); a §24 wording change to DATA-1/DATA-2 [J, the CTO's estimate, which I have no reason to revise].
- **What else it buys:** it also removes the separate migration-ordering hazard (`architecture-proposals.md` §5 item 4), which none of 3.1–3.7 addresses except 3.4.
- **Verdict: the simplest option that is sound on both platforms.**

## 4. Empirical test on this Mac

**Result: the hazard reproduces, reliably, without any special tooling. It is worst between two ordinary builds of SQLite (the Android pairing); Apple's own SQLite behaves differently and fails less often, by crashing rather than silently losing data (the iOS pairing).** All of this is [E], run by this seat on 2026-09-28. Nothing was installed or downloaded; every library used was already on this Mac.

### 4.1 Set-up

- **Machine:** macOS 27.0 (build 26A428), Apple silicon. **iOS proxy:** the iOS 26.0 Simulator (iPhone 17 runtime, 23A8464), booted locally with `xcrun simctl`.
- **Libraries, each loaded with `dlopen(RTLD_LOCAL)` into one test process:**

| Label | Library | Version | Stands in for |
|---|---|---|---|
| Apple (macOS) | `/usr/lib/libsqlite3.dylib`, the system copy | 3.54.0 (Apple build, source id ending `aapl`) | — |
| **Apple (iOS)** | the iOS 26.0 Simulator's `/usr/lib/libsqlite3.dylib` | **3.51.0** (Apple build) | **Swift using the system SQLite on iOS** |
| Upstream | Homebrew `libsqlite3.3.53.4.dylib` (already installed) | 3.53.4 | **Expo's bundled 3.53.3**, same upstream code, same plain POSIX locking |
| Upstream, second copy | a byte-for-byte copy of the Homebrew library at a different path, so it loads as a second image | 3.53.4 | **Android's framework SQLite** (also upstream code with plain POSIX locking, §2.2) |
| Upstream, simulator | the Homebrew library retagged for the iOS Simulator (`vtool -set-build-version iossim`, re-signed ad hoc) | 3.53.4 | Expo's copy inside an iOS process |

- **Program:** `twocopies.c`, a ~300-line C program in the scratchpad (path in §6). Each test opens one database file through library **A** and library **B** in the same process. The control run passes the same library twice, so `dlopen` returns one image: one copy, two connections, which is what SQLite supports.
- **Exact commands** (from the scratchpad `sqlite-test/` folder):
  - `./twocopies <libA> <libB> <workdir> <n> "1,2,3,3b,4,5"` on macOS;
  - `xcrun simctl spawn <iPhone 17 UDID> ./sim-twocopies /usr/lib/libsqlite3.dylib ./libsqlite3-sim.dylib <workdir> 300 "1,2,3,3b,5"` in the iOS Simulator;
  - `./stress.sh <label> 10 300 <runner…>` for the ten-run stress tallies.
- **Independent check** after each test: `/usr/bin/sqlite3` in a separate process counts the rows and runs `PRAGMA integrity_check`.

### 4.2 The tests

| Test | What it does | Why it matters for Haunts |
|---|---|---|
| **T1** | Rollback-journal mode. A takes the write lock (`BEGIN IMMEDIATE`). Can B take it too? Can B commit while A is mid-read? | Basic mutual exclusion |
| **T2** | WAL mode. A holds the WAL write lock. Can B take it too? If so, both insert and commit | Two writers at once: a visit being recorded while the user confirms a visit |
| **T3** | WAL mode. B opens and stays open. A opens, writes one row, **closes**. B writes, A writes again. No two operations overlap | The JavaScript connection is open all day; the capture code opens, writes and closes per event |
| **T3b** | As T3, for three capture "visits", with B writing between each | The same over a few days |
| **T4** | The documented case. B holds a write lock; A opens, reads, closes; a **separate process** then tries to write | Shows the lock loss directly |
| **T5** | Stress. Two threads, one per library, 300 committed inserts each, WAL, 5 s busy timeout, each closing and reopening every 50 inserts. Run ten times | How often it fails when the two sides are busy at once |

### 4.3 Results

**Control (one library, two connections): every test correct.** T1 and T2 refused the second writer with `SQLITE_BUSY`; T3 and T3b kept every row and never deleted the `-wal` file under an open connection; T4's other process was refused both times; T5 was **clean in 10 of 10 runs** (600 of 600 rows each). The test harness is not what fails below.

**Two upstream copies (the Android pairing): everything fails, including with no concurrency at all.**

| Test | What happened |
|---|---|
| T1 | B was **granted** the write lock while A held it, and later **committed a write under A's active read** |
| T2 | Both writers were granted the lock; both `COMMIT`s returned success. Afterwards both connections see **2 rows (0, 2)**. **A's committed row 1 is gone. `integrity_check` says `ok`** |
| T3 | **A's ordinary close deleted the `-wal` and `-shm` files while B was still open.** B's next insert went into the deleted WAL. A then saw rows 1, 2, 4 and B saw 1, 2, 3; after both closed the file holds **3 of 4 rows**. Every insert had returned success; `integrity_check`: `ok` |
| T3b | Three capture visits, sequential: **5 of 7 rows survive**, and during the run the two connections saw two different databases (B: 1, 2, 3, 5, 7; A: 1, 2, 4, 6). `integrity_check`: `ok` |
| T4 | After A's `close()`, the separate process was **granted** a write lock it had been refused a moment before. B's commit then failed with `SQLITE_IOERR` and the other process's committed row was lost |
| T5 | **10 of 10 runs failed:** 8 silently lost 251–300 of about 600 committed rows (`integrity_check` `ok` every time); 2 crashed the process with **SIGBUS** (exit 138) |

**Apple's SQLite with an upstream copy (the iOS pairing): ordinary sequential use survives; concurrent use crashes.**

- **Apple's SQLite does not use ordinary POSIX locks.** After it takes a write lock, a plain `fcntl(F_SETLK)` on the same byte from the same process is **refused** (`EAGAIN`, "Resource temporarily unavailable"); the upstream library's identical lock is **granted**. That is the behaviour of per-open-file locks rather than per-process ones. Same result for the macOS 27 system library and the **iOS 26.0 Simulator** library (`ofdprobe.c`). Both Apple builds also report `ENABLE_LOCKING_STYLE=1` and `ENABLE_SETLK_TIMEOUT`. Apple does not document this, and I could not find its source for these versions, so **the mechanism is inferred from behaviour** [I].
- **Consequence:** the two copies *do* see each other's locks while both hold them. T1, T2, T3 and T3b were **correct** in both directions on macOS and in the iOS Simulator.
- **But `close()` in the Apple copy still drops the upstream copy's locks**, because `close()` releases every ordinary POSIX lock the process holds on the file. T4 on macOS: after the Apple copy closed, a separate process was granted a write lock it should not have had, and the upstream copy's commit failed with `SQLITE_IOERR`.
- **T5 (concurrent), ten runs each:**
  - **macOS:** 5 clean, **4 crashed with SIGBUS**, **1 silently lost 13 of 598 committed rows**.
  - **iOS 26.0 Simulator:** 2 clean, **8 crashed with SIGBUS**.
  - In the Simulator every crash left 50–102 committed rows, i.e. it happened at the first or second point where a thread closes and reopens. The leftover `-shm` file after one crash was **3 bytes long**. SQLite shrinks it to 3 bytes when it believes it is the first connection to open the database and is rebuilding the shared index; the other copy still had it mapped. Touching a memory-mapped file past its end raises SIGBUS [I, from S2 and the evidence above].
- No run produced a file that failed `integrity_check`. The failures are **lost committed writes and process crashes**, not a malformed file. The loss is arguably worse, because nothing detects it.

### 4.4 What the test does and does not show

- **It shows** that the §2.3 hazard is real, easy to trigger, and not limited to a lost `close()` race. Between two ordinary builds, **one routine close by one side** is enough to lose the other side's later writes silently.
- **It does not run on a phone.** The Android pairing is modelled by two upstream copies on macOS, not by Android's framework library on Linux. The model rests on two premises:
  - AOSP builds SQLite from the upstream amalgamation, with a patch that does not touch locking (§2.2) [E].
  - Linux applies the same per-process POSIX lock rules [K, high confidence].

  The iOS pairing ran in the iOS Simulator, which uses Apple's iOS SQLite build on the macOS kernel. A device test at M1 would close both gaps (§5).
- **It uses a stress load for T5.** Haunts writes a handful of rows a day, so T5 overstates how *often* concurrent failures would happen. It does not overstate whether they *can*. T3 and T3b need no concurrency, and they are the Android case.

## 5. Recommendation

1. **Keep the CTO's two-file design** (`capture.db` owned by native code, `journal.db` owned by JavaScript, `venues.db` read-only), and send the DATA-1/DATA-2 wording change to the PM/BA as the CTO proposed. I agree with the CTO's finding and fix. My evidence is stronger than theirs was, and my one correction runs the other way from the CEO's worry: **the problem is broader than the documented `close()` case, not narrower.** [J]
2. **Add three small guards to the capture module's tickets** [J]:
   - **(a)** Native code opens `capture.db` through **one connection on one serial queue** (the WAL-reset bug in iOS 26.0's system SQLite 3.51.0, §2.4), or uses rollback-journal mode for that file.
   - **(b)** A lint or CI check that **only `modules/capture/` opens `capture.db` and only `core/store/` opens `journal.db`**. The architecture's `no-restricted-imports` rules cover imports, not file paths, and a stray `openDatabaseAsync('capture.db')` in JavaScript would recreate the hazard.
   - **(c)** `venues.db`: if native code ever needs it (the CTO's CAP-9 note), open it read-only with `immutable=1` in native code, or have only one side ever open it. The CTO marked `immutable=1` as [K — to verify before use]; I did not test it here.
3. **At M1, run a device test** to close the two gaps in §4.4: `twocopies.c`'s T3 and T5 on a real Android phone (framework SQLite plus Expo's copy) and a real iPhone. **This is not a gate on the design**, which is sound either way. It turns this document's platform inferences into measurements. ≈ half a day [J].

**Cost:** as the CTO estimated. £0 running; no new dependency. The guards in 2(a)–(c) are a few hours inside existing tickets [J].

**Not recommended:** §3.1 (call Expo's private copy), §3.3 (op-sqlite), §3.4 (native owns everything), §3.6 (Android-only separate process), §3.7 (rely on timing). Each either fixes one platform only, depends on undocumented internals, or costs more than the two-file design.

## 6. What would overturn this, and where I looked

**What would overturn "it is a real issue":**
- a documented statement from SQLite that multiple copies in one process are safe from some version on (the current page, dated 2026-04-13, says the opposite);
- a device run of T3/T5 on Android showing no loss. Given the source and the macOS result I would expect it to fail, and if it didn't I would look for what the framework build does differently.

**What would overturn "two files is the best fix":**
- Expo publishing a supported native interface to its SQLite copy on both platforms (then §3.1 becomes cheap and supported);
- Expo adding a system-SQLite option **and** Android gaining an equivalent (it cannot today);
- the §24 wording change to DATA-1/DATA-2 being refused, in which case §3.1 is the least-bad fallback.

**Where I looked:**
- SQLite: *How To Corrupt*, *WAL*, `src/os_unix.c` and `src/wal.c` at `version-3.53.3`, the SQLite forum.
- expo-sqlite 58.0.6 at its npm `gitHead`: podspec, `spm.config.json`, `CMakeLists.txt`, `build.gradle`, config plugin, README, `replace_symbols.ts`, the vendored `sqlite3.c` header, Swift and Kotlin bindings.
- AOSP `external/sqlite/dist` (`Android.bp`, `Android.patch`) on the GitHub mirror.
- Apple's `startMonitoringVisits()` reference; Android's `<service>` reference; the iOS 27.0 SDK's `SQLite3.modulemap`; GRDB's README; op-sqlite's installation docs; this repo's `requirements.md` (CAP-1).
- Five test programs run on macOS 27 and in the iOS 26.0 Simulator.

**What I did not do:**
- run on a physical phone;
- find Apple's source for the lock behaviour in §4.3;
- build a Swift or Kotlin module against Expo's copy to prove §3.1 compiles;
- verify that `libexpo-sqlite.so` exports its symbols.

**Test artefacts** (scratchpad, not committed; session-scoped): `/private/tmp/claude-501/-Users-davidparrish-Documents-candour/1c0db2a6-d671-472b-91d8-5123d15bad48/scratchpad/sqlite-test/`
- `twocopies.c`, `stress.sh`, `lockprobe.c`, `ofdprobe.c`, `kernlock.c`, `step.c`;
- outputs `out-control.txt`, `out-two.txt`, `out-two-b.txt`, `out-samever.txt`, `out-sim-ab.txt`, `out-sim-ba.txt`.

If the CEO wants them kept, they should move into `products/haunt/architecture/evidence/`. That is a small commit, and it is the CEO's or orchestrator's call.

## Sources retrieved this session

All retrieved 2026-09-28.

| # | Source | Link |
|---|---|---|
| S1 | SQLite, *How To Corrupt An SQLite Database File*, §2.2–2.5, §8.1 (page dated 2026-04-13) | https://www.sqlite.org/howtocorrupt.html |
| S2 | SQLite `src/os_unix.c` at tag `version-3.53.3` (commit `92a6c5c3`): lines 1189–1283 (POSIX lock commentary), 1349 (`inodeList`), 2030–2040 (sharing check), 4679–4695 (`unixIsSharingShmNode`), 4850–4902 (`unixLockSharedMemory`) | https://github.com/sqlite/sqlite/blob/version-3.53.3/src/os_unix.c |
| S3 | SQLite `src/wal.c` at tag `version-3.53.3`, `sqlite3WalClose` (line 2507) | https://github.com/sqlite/sqlite/blob/version-3.53.3/src/wal.c |
| S4 | npm registry, expo-sqlite (dist-tags, `gitHead` of 58.0.6) | https://registry.npmjs.org/expo-sqlite |
| S5 | expo-sqlite `vendor/sqlite3/sqlite3.c` @ `ad41d067` (version and renamed symbols) | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/vendor/sqlite3/sqlite3.c |
| S6 | expo-sqlite README @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/README.md |
| S7 | `scripts/replace_symbols.ts` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/scripts/replace_symbols.ts |
| S8 | `ios/ExpoSQLite.podspec` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/ios/ExpoSQLite.podspec |
| S9 | `spm.config.json` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/spm.config.json |
| S10 | `ios/SQLiteModule.swift` @ `ad41d067` (line 140) | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/ios/SQLiteModule.swift |
| S11 | `android/CMakeLists.txt` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/android/CMakeLists.txt |
| S12 | `android/build.gradle` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/android/build.gradle |
| S13 | `plugin/src/withSQLite.ts` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/plugin/src/withSQLite.ts |
| S14 | `NativeDatabaseBinding.kt` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/android/src/main/java/expo/modules/sqlite/NativeDatabaseBinding.kt |
| S15 | `ios/NativeDatabase.swift` @ `ad41d067` | https://github.com/expo/expo/blob/ad41d067bd3df6dd12f1788acc6b54a68e7a650d/packages/expo-sqlite/ios/NativeDatabase.swift |
| S16 | GRDB.swift README (master @ `0d8cf958`) | https://github.com/groue/GRDB.swift/blob/0d8cf958b4b66a0473ec6e6986eb9da462171da9/README.md |
| S17 | AOSP `external/sqlite/dist/Android.bp` (GitHub mirror, archived; last `dist/` commit `181d3d57`, 2025-03-25) **(single source)** | https://github.com/aosp-mirror/platform_external_sqlite/blob/main/dist/Android.bp |
| S18 | AOSP `external/sqlite/dist/Android.patch` (same mirror) **(single source)** | https://github.com/aosp-mirror/platform_external_sqlite/blob/main/dist/Android.patch |
| S19 | Android Developers, `<service>` element, `android:process` (last updated 2026-07-01) | https://developer.android.com/guide/topics/manifest/service-element |
| S20 | Apple Developer, `CLLocationManager.startMonitoringVisits()` | https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits() |
| S21 | SQLite, *Write-Ahead Logging*, §11 "The WAL-Reset Bug" (page dated 2026-08-25) | https://www.sqlite.org/wal.html |
| S22 | op-sqlite installation docs (main @ `08c69137`) | https://github.com/OP-Engineering/op-sqlite/blob/08c691379999ebf2ed98279d5fa66c047535d06f/docs/docs/installation.md |
| S23 | SQLite User Forum, "How to Corrrupt an SQLite DB Section 2.2.1" (2022-08-25; replies by Richard Hipp and Larry Brasfield) | https://sqlite.org/forum/forumpost/dbf245f2b7 |
| — | Empirical tests, §4 (this seat, 2026-09-28, macOS 27.0 and iOS 26.0 Simulator) | scratchpad paths in §6 |
| — | iOS SDK `SQLite3.modulemap`, `libsqlite3.tbd` (read locally, Xcode `iPhoneOS27.0.sdk`) | local |

**Independence note.** S1, S2, S3, S21 and S23 all come from the SQLite project, so on the *mechanism* they are one origin. The independent corroboration is the empirical test (§4), which reproduces the mechanism with nothing borrowed from the SQLite team except the library itself. The Expo facts (S4–S15) are one origin, Expo's repository, and are primary for what Expo ships.

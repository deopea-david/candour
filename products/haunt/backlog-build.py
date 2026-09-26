#!/usr/bin/env python3
"""Generate products/haunt/backlog.csv from the mapping below and check coverage
against products/haunt/requirements.md. Re-runnable; prints the coverage report."""
import csv, re, sys

ROOT = sys.argv[1]
REQ = f"{ROOT}/products/haunt/requirements.md"
OUT = f"{ROOT}/products/haunt/backlog.csv"

# ---- parse requirements.md: id -> (section, priority-cell) -----------------
req = {}
sec = ""
for line in open(REQ, encoding="utf-8"):
    h = re.match(r"^#+\s+(\d+(?:\.\d+)*)", line)
    if h:
        sec = h.group(1)
        continue
    m = re.match(r"^\|\s*\*\*([A-Z0-9]+-\d+)\*\*\s*\|", line)
    if not m:
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 5:          # S-1..S-3 standing-condition table has 4 cells
        continue
    prios = re.findall(r"BLOCKING|MUST|CUT-LINE|PENDING-ESTIMATE", cells[3])
    order = ["BLOCKING", "MUST", "PENDING-ESTIMATE", "CUT-LINE"]
    top = sorted(set(prios), key=order.index)[0]
    req[m.group(1)] = (sec, top, len(set(prios)) > 1)

# ---- the mapping ------------------------------------------------------------
# epic: (key, title, owner, section)
# feature: (key, title, owner, [task ids])
E = []
def epic(key, title, owner, section, features):
    E.append((key, title, owner, section, features))

epic("EP-RULES", "Product-wide rules: memories not volume; protective defaults", "pm-ba", "3.1;3.2", [
    ("FT-RULES-1", "Celebrate memories, never volume, build-wide", "ux-lead", ["MEM-1"]),
    ("FT-RULES-2", "Protective defaults and the settings register", "engineer", ["DFLT-1"]),
])
epic("EP-CAP", "Automatic visit capture", "cto", "4", [
    ("FT-CAP-1", "Native capture pipeline and verifiable teardown", "engineer", ["CAP-1", "CAP-7"]),
    ("FT-CAP-2", "iOS visit capture", "engineer", ["CAP-2"]),
    ("FT-CAP-3", "Android visit capture", "engineer", ["CAP-3"]),
    ("FT-CAP-4", "Capture honesty: gaps, reduced accuracy, location denied", "engineer", ["CAP-4", "CAP-5", "CAP-6"]),
    ("FT-CAP-5", "One capture-failure notification, nothing else", "engineer", ["CAP-8", "CAP-9"]),
    ("FT-CAP-6", "Battery measured on real devices before any claim", "engineer", ["CAP-10"]),
])
epic("EP-CONF", "Confirming visits", "pm-ba", "5", [
    ("FT-CONF-1", "Confirm queue as a pull, not a push", "engineer",
     ["CONF-1", "CONF-12", "CONF-13", "CONF-14", "CONF-15", "CONF-16"]),
    ("FT-CONF-2", "Candidate rows: nearest first, choice never assent", "engineer",
     ["CONF-2", "CONF-3", "CONF-7", "CONF-10", "CONF-11", "VEN-22"]),
    ("FT-CONF-3", "Venue search in the confirm flow", "engineer",
     ["CONF-4", "CONF-5", "CONF-6", "CONF-8", "CONF-9"]),
    ("FT-CONF-4", "Note, rating and companions on the confirm row", "engineer",
     ["CONF-17", "CONF-18", "CONF-19"]),
])
epic("EP-SESS", "Sessions", "cto", "6", [
    ("FT-SESS-1", "Derived sessions with durable overrides", "engineer", ["SESS-1", "SESS-2", "SESS-9"]),
    ("FT-SESS-2", "Session queue, split and merge", "engineer", ["SESS-3", "SESS-4", "SESS-5"]),
    ("FT-SESS-3", "Home inference the user can see and edit", "engineer", ["SESS-6"]),
    ("FT-SESS-4", "Whole sessions across entitlement and gaps", "engineer", ["SESS-7", "SESS-8"]),
])
epic("EP-VEN", "Venue index and venue identity", "cto", "7", [
    ("FT-VEN-1", "Bundled offline venue index", "engineer",
     ["VEN-1", "VEN-2", "VEN-3", "VEN-4", "VEN-5", "VEN-6", "VEN-23"]),
    ("FT-VEN-2", "Venue identity survives every refresh (schema rules)", "engineer",
     ["VEN-7", "VEN-8", "VEN-10", "VEN-11", "VEN-12"]),
    ("FT-VEN-3", "Refresh proposals and quarterly cadence", "engineer", ["VEN-9", "VEN-13", "VEN-19"]),
    ("FT-VEN-4", "Repair layer: merge, rename, reattach, undo", "engineer",
     ["VEN-14", "VEN-15", "VEN-16", "VEN-21"]),
    ("FT-VEN-5", "Venue-identity regression fixture and release bar", "qa",
     ["VEN-17", "VEN-18", "VEN-20", "VEN-24"]),
])
epic("EP-VPAGE", "The venue page", "pm-ba", "8", [
    ("FT-VPAGE-1", "Venue page: every visit, rating, note and verdict", "engineer",
     ["VPAGE-1", "VPAGE-2", "VPAGE-5", "VPAGE-7", "VPAGE-9"]),
    ("FT-VPAGE-2", "Honest, entitlement-blind aggregates at scale", "engineer",
     ["VPAGE-3", "VPAGE-4", "VPAGE-8"]),
    ("FT-VPAGE-3", "Ratings: true mean, trend and weighted order", "engineer",
     ["VPAGE-6", "VPAGE-10", "VPAGE-11"]),
])
epic("EP-LOOK", "Journal-wide views", "pm-ba", "8.1", [
    ("FT-LOOK-1", "What Haunts has worked out about you", "engineer", ["LOOK-1"]),
    ("FT-LOOK-2", "Most-visited list and offline heatmap", "engineer", ["LOOK-2"]),
    ("FT-LOOK-3", "Recap and self-portrait", "engineer", ["LOOK-3", "LOOK-8"]),
    ("FT-LOOK-4", "Save recap as image; no sharing prompts anywhere", "engineer",
     ["LOOK-4", "LOOK-5", "LOOK-6", "LOOK-7"]),
    ("FT-LOOK-5", "Offline search including notes", "engineer", ["LOOK-9"]),
])
epic("EP-HEAD", "Home-screen headlines", "ux-lead", "8.2", [
    ("FT-HEAD-1", "Headline slot, appearances and options", "engineer",
     ["HEAD-1", "HEAD-2", "HEAD-3", "HEAD-5", "HEAD-15"]),
    ("FT-HEAD-2", "Headline content rules and small-numbers honesty", "engineer",
     ["HEAD-4", "HEAD-6", "HEAD-7", "HEAD-8", "HEAD-14"]),
    ("FT-HEAD-3", "Ticker motion and screen-reader behaviour", "engineer",
     ["HEAD-9", "HEAD-10", "HEAD-11", "HEAD-16"]),
    ("FT-HEAD-4", "Headline privacy: surfaces and sensitive places", "engineer",
     ["HEAD-12", "HEAD-13", "HEAD-17", "HEAD-18"]),
])
epic("EP-ENT", "Entitlement, trial, lapse and first run", "cto", "9;9.1", [
    ("FT-ENT-1", "Entitlement as intervals, unknown stated honestly", "engineer", ["ENT-1", "ENT-2"]),
    ("FT-ENT-2", "Trial and lapse: nothing hidden, nothing lost", "engineer",
     ["ENT-3", "ENT-4", "ENT-5", "ENT-9", "ENT-10"]),
    ("FT-ENT-3", "Location use stops at expiry, and says so", "engineer", ["ENT-6", "ENT-7", "ENT-8"]),
    ("FT-ENT-4", "Store lifecycle: cancel, restore, no covert identifier", "engineer",
     ["ENT-11", "ENT-12", "ENT-13"]),
    ("FT-ENT-5", "Entitlement-boundary QA fixtures", "qa", ["ENT-14"]),
    ("FT-ENT-6", "First run and onboarding", "engineer", ["ONB-1", "ONB-2", "ONB-3"]),
])
epic("EP-PRICE", "Pricing presentation and consumer notices", "cfo", "10;11", [
    ("FT-PRICE-1", "Plans screen with honest per-unit prices", "engineer",
     ["PRICE-1", "PRICE-2", "PRICE-3", "PRICE-4", "PRICE-5", "PRICE-6"]),
    ("FT-PRICE-2", "Point-of-sale disclosures", "engineer",
     ["PRICE-7", "PRICE-8", "PRICE-9", "PRICE-10", "PRICE-13", "PRICE-14"]),
    ("FT-PRICE-3", "Published price commitments", "cfo", ["PRICE-11", "PRICE-12"]),
    ("FT-PRICE-4", "In-app notices surface and cancellation", "engineer",
     ["NOT-1", "NOT-2", "NOT-3", "NOT-4", "NOT-5", "NOT-6"]),
])
epic("EP-DATA", "Store, export, import and backup", "cto", "12", [
    ("FT-DATA-1", "One SQLite store as a written contract", "cto", ["DATA-1", "DATA-2"]),
    ("FT-DATA-2", "Lossless export and own-archive import", "engineer", ["DATA-3", "DATA-4", "DATA-5"]),
    ("FT-DATA-3", "Opt-in encrypted backup", "engineer",
     ["DATA-6", "DATA-7", "DATA-8", "DATA-9", "DATA-10", "DATA-11", "DATA-12"]),
    ("FT-DATA-4", "Diagnostics that cannot hold journal content", "engineer", ["DATA-13", "DATA-14"]),
    ("FT-DATA-5", "Import from a competitor's export", "engineer", ["DATA-15"]),
])
epic("EP-PHOTO", "Photos by reference", "cto", "12.2", [
    ("FT-PHOTO-1", "Attach photos by reference with a kept thumbnail", "engineer",
     ["PHOTO-1", "PHOTO-2", "PHOTO-5", "PHOTO-10", "PHOTO-11"]),
    ("FT-PHOTO-2", "Missing-photo state as a designed normal state", "engineer", ["PHOTO-7", "PHOTO-8"]),
    ("FT-PHOTO-3", "Photos in export, backup and import", "engineer",
     ["PHOTO-3", "PHOTO-4", "PHOTO-6", "PHOTO-9"]),
])
epic("EP-LIC", "Licences and attribution", "cgo", "13", [
    ("FT-LIC-1", "Data sources and licences screen", "engineer", ["LIC-1", "LIC-3", "LIC-4", "LIC-6"]),
    ("FT-LIC-2", "Licence texts travel with redistributed data", "engineer", ["LIC-2", "LIC-5"]),
])
epic("EP-PRIV", "Privacy and honesty surfaces", "cgo", "14", [
    ("FT-PRIV-1", "Transmission claim, enforced and shown live", "engineer", ["PRIV-1", "PRIV-2", "PRIV-8"]),
    ("FT-PRIV-2", "Privacy declarations and public statements", "cgo", ["PRIV-3", "PRIV-4", "PRIV-5"]),
    ("FT-PRIV-3", "Quiet by default: review prompt and spoken labels", "engineer", ["PRIV-6", "PRIV-7"]),
])
epic("EP-A11Y", "Accessibility", "ux-lead", "15", [
    ("FT-A11Y-1", "No map-only or colour-only information", "engineer", ["A11Y-1", "A11Y-2", "A11Y-3"]),
    ("FT-A11Y-2", "Screen-reader labels and announcements", "engineer", ["A11Y-6", "A11Y-7", "A11Y-8"]),
    ("FT-A11Y-3", "Text size, touch targets and motion", "engineer", ["A11Y-4", "A11Y-5", "A11Y-9"]),
    ("FT-A11Y-4", "Per-release accessibility gate", "qa", ["A11Y-10"]),
])
epic("EP-PLAT", "Platform, storefront and release", "cto", "16", [
    ("FT-PLAT-1", "React Native app shell on iOS 26+ and Android", "cto", ["PLAT-1", "PLAT-8"]),
    ("FT-PLAT-2", "Store release readiness and schedule", "pm-ba", ["PLAT-3", "PLAT-4", "PLAT-5"]),
    ("FT-PLAT-3", "Name, icon and support statement before launch", "cgo", ["PLAT-2", "PLAT-6", "PLAT-7"]),
])
epic("EP-PLAN", "Build planning and spikes", "cto", "22", [
    ("FT-PLAN-1", "Block lifts owed before build", "cto", ["SPK-01", "SPK-02"]),
    ("FT-PLAN-2", "Platform and device questions", "cto", ["SPK-03", "SPK-05", "SPK-07", "SPK-10", "SPK-14"]),
    ("FT-PLAN-3", "Architecture and security choices", "cto", ["SPK-04", "SPK-06", "SPK-11", "SPK-12", "SPK-13"]),
    ("FT-PLAN-4", "Sizing and costing of scope outside the estimate", "cto", ["SPK-08", "SPK-09"]),
    ("FT-PLAN-5", "Repository conventions and agent scaffolding", "cto", ["SPK-15", "SPK-16"]),
])

# ---- task titles (<=70 chars) ------------------------------------------------
T = {
 "MEM-1": "Never encourage drinking or reward visit frequency, anywhere",
 "DFLT-1": "Protective defaults, user-changeable, with a CI-checked register",
 "CAP-1": "No JavaScript in the visit-recording path",
 "CAP-2": "iOS capture via startMonitoringVisits, with downgrade detection",
 "CAP-3": "Android capture via a declared location foreground service",
 "CAP-4": "Capture gaps are first-class data, shown inline in plain words",
 "CAP-5": "Capture works under reduced accuracy and says so",
 "CAP-6": "Fully usable with location denied, in every tier",
 "CAP-7": "Capture stops verifiably when not entitled; teardown idempotent",
 "CAP-8": "One notification type only, for capture failure",
 "CAP-9": "Uncertain-match notification bounded by CAP-8; works if declined",
 "CAP-10": "Measure battery cost on real devices before any claim",
 "CONF-1": "Confirm queue is a pull: no badge, count or completion meter",
 "CONF-2": "Nearest offered by default; options shown when unclear",
 "CONF-3": "Never auto-select a candidate",
 "CONF-4": "Twenty candidate rows reachable in one action by typing",
 "CONF-5": "Prefix, incremental name search from the first character",
 "CONF-6": "Filter, search and \"isn't listed\" always reachable",
 "CONF-7": "One row, three facts; no confidence number shown",
 "CONF-8": "Suppress the generic-token dragnet in search results",
 "CONF-9": "Near-miss confusability tested; false-pick rate reported",
 "CONF-10": "Mark a previously-chosen venue in its row",
 "CONF-11": "Sticky choice ranks, never selects (150 m gate)",
 "CONF-12": "Row carries enough context to recognise the visit",
 "CONF-13": "Session- and day-level bulk actions at equal weight",
 "CONF-14": "Repeat same-day visits to one venue collapse to one row",
 "CONF-15": "Candidates expire silently on a published schedule",
 "CONF-16": "Setting: \"Do not ask me - I will add places myself\"",
 "CONF-17": "Note field open on the confirm row; venue + date is finished",
 "CONF-18": "Voice dictation into the note field, on-device",
 "CONF-19": "Companions as free text with autocomplete from own history",
 "SESS-1": "Sessions derived and recomputable, never stored rows",
 "SESS-2": "User overrides are durable constraints anchored to visits",
 "SESS-3": "Queue groups by session, falling back to day",
 "SESS-4": "Split and merge reachable, visible and reversible",
 "SESS-5": "Low session confidence is stated, not guessed",
 "SESS-6": "Home inference visible, editable, removable, can be none",
 "SESS-7": "Entitlement evaluated per session, never per visit",
 "SESS-8": "Sessions straddling a gap or boundary state partiality",
 "SESS-9": "Entitlement intervals and gaps are durable, natively readable",
 "VEN-1": "Venue index bundled and offline; no places API ever",
 "VEN-2": "Locality from the Places theme only, never Divisions",
 "VEN-3": "Index scope B: food_and_drink plus committed allow-list",
 "VEN-4": "FTS5 prefix index and grid-cell B-tree column, no R-Tree",
 "VEN-5": "Record the index bundle cost for CFO and CTO before build",
 "VEN-6": "Conservative, auditable near-duplicate clustering",
 "VEN-7": "Copy the venue row on first reference; page never reads index",
 "VEN-8": "Refresh can never write to a referenced row (schema-enforced)",
 "VEN-9": "Changes to referenced rows offered, never applied; decline default",
 "VEN-10": "A user's rename outranks the dataset permanently",
 "VEN-11": "User merges survive refreshes, including upstream re-splits",
 "VEN-12": "Reconciliation never joins on GERS ID alone",
 "VEN-13": "Refresh review surface is not a notification or pressure queue",
 "VEN-14": "Merge is user-facing, reversible, reachable from any venue",
 "VEN-15": "Rename in place keeps the venue identity",
 "VEN-16": "Offer merge for a probable duplicate, statically, once",
 "VEN-17": "Venue-index harness as a committed, reproducible fixture",
 "VEN-18": "Index, ranking or search changes re-run fixture; publish P1-P4",
 "VEN-19": "Refresh the bundled index quarterly inside app updates",
 "VEN-20": "P1-P5 venue-identity release criteria in every release pack",
 "VEN-21": "Reattach a visit; whole repair path reversible and lossless",
 "VEN-22": "No confirmation from a surface without the alternatives",
 "VEN-23": "Grid-cell query unions the nine-cell neighbourhood",
 "VEN-24": "Measure real CLVisit accuracy on the field run (S-1)",
 "VPAGE-1": "Venue is a first-class entity with identity and history",
 "VPAGE-2": "Venue page shows every visit, rating, note and a verdict",
 "VPAGE-3": "Derived views complete or state partiality on their face",
 "VPAGE-4": "Venue page read path is entitlement-blind (CI static check)",
 "VPAGE-5": "Merge, rename and duplicate hint reachable from venue page",
 "VPAGE-6": "Stars always shown with the visit count",
 "VPAGE-7": "Static line: what a venue page becomes over time",
 "VPAGE-8": "Query performance holds over five years of data",
 "VPAGE-9": "Every venue-page function reachable from a list, not a map",
 "VPAGE-10": "Venue page shows the trend of the user's own ratings",
 "VPAGE-11": "Weighted (C = 3) rating order; displayed stars stay true mean",
 "LOOK-1": "\"What Haunts has worked out about you\" inference screen",
 "LOOK-2": "Ranked list plus offline Zoomstack heatmap, list map-free",
 "LOOK-3": "Monthly or yearly recap, pulled never pushed",
 "LOOK-4": "Save recap as image on explicit tap; the app never asks",
 "LOOK-5": "Small hideable logo on the image, never a watermark or CTA",
 "LOOK-6": "Nothing anywhere prompts, nudges or celebrates sharing",
 "LOOK-7": "Limit what a generated recap image may contain",
 "LOOK-8": "Local self-portrait, reachable in and outside the recap",
 "LOOK-9": "Offline search across notes, venues and companion names",
 "HEAD-1": "Headlines at top of home screen, scrolling, never sticky",
 "HEAD-2": "Four appearances: Line (default), Card, Ticker, Off",
 "HEAD-3": "Line and Card change at most once per day, never while shown",
 "HEAD-4": "Headlines only from the T1-T9 catalogue, computed on-device",
 "HEAD-5": "Headline options reachable from the headline and Settings",
 "HEAD-6": "Headlines celebrate memories, never volume",
 "HEAD-7": "Slot carries self-portrait facts only, nothing commercial",
 "HEAD-8": "No novelty or urgency treatment on headlines",
 "HEAD-9": "Ticker pause control, persistent across launches",
 "HEAD-10": "Reduce-motion detected; Ticker renders as Line",
 "HEAD-11": "Ticker falls back to Line for screen readers and large text",
 "HEAD-12": "Headlines never in the app-switcher snapshot",
 "HEAD-13": "Headlines only on the in-app home screen",
 "HEAD-14": "Headline small-numbers honesty and entitlement-blindness",
 "HEAD-15": "No headline slot until a fact qualifies; no teasers",
 "HEAD-16": "Headline screen-reader and layout behaviour",
 "HEAD-17": "Sensitive places out of headlines by default, one switch",
 "HEAD-18": "Per-place headline toggle for uncategorised places",
 "ENT-1": "Entitlement stored as intervals, readable by capture modules",
 "ENT-2": "Unknown entitlement state is conservative and stated",
 "ENT-3": "Two-week full trial; everything written stays usable free",
 "ENT-4": "Manual entry is a first-class composer, forever, unpaid",
 "ENT-5": "Nothing is deleted on lapse",
 "ENT-6": "No capture after entitlement ends; none withheld",
 "ENT-7": "Unpaid state never requests Always location",
 "ENT-8": "Location stops at expiry; app says how to revoke permission",
 "ENT-9": "Expiry moment: exactly the three specified states",
 "ENT-10": "Charge-date disclosure static, never a countdown",
 "ENT-11": "Trial state lost on uninstall; no covert persistent ID",
 "ENT-12": "Nothing between the user and the platform cancel flow",
 "ENT-13": "Restore Purchases only on explicit user action",
 "ENT-14": "QA fixtures for the whole entitlement boundary",
 "ONB-1": "No onboarding or setup step is ever mandatory",
 "ONB-2": "First run offers to seed the journal from memory",
 "ONB-3": "First-run index proof: \"find your local\"",
 "PRICE-1": "Every tier's per-unit cost visible in one view",
 "PRICE-2": "No tier pre-selected; two explicit taps to buy",
 "PRICE-3": "Badges arithmetic, never adjectival",
 "PRICE-4": "Savings only against monthly, rounded down",
 "PRICE-5": "No \"from GBP X\" headline price",
 "PRICE-6": "Pay-once tier named \"Pay once\"; never lifetime or forever",
 "PRICE-7": "State the monthly/pay-once crossover at point of sale",
 "PRICE-8": "Pay-once screen: no share in future price reductions",
 "PRICE-9": "State review cadence, step-downs and 90-day notice at sale",
 "PRICE-10": "State before first sale that no support date is committed",
 "PRICE-11": "Amortisation period never published as a support statement",
 "PRICE-12": "Publish the guaranteed price-rise notice period; deliver it",
 "PRICE-13": "No pricing sentence depends on a support date",
 "PRICE-14": "Amortisation-derived dates labelled accounting dates",
 "NOT-1": "Pre-contract information in store metadata and first run",
 "NOT-2": "Persistent, append-only in-app notices surface",
 "NOT-3": "Reminder and cooling-off notices, local only, no server",
 "NOT-4": "Plain in-app cancel control to Manage Subscriptions",
 "NOT-5": "Answer notification authorization before R2/R3 are built",
 "NOT-6": "Price-rise notice and notices surface are one surface",
 "DATA-1": "One SQLite file, no opaque blobs",
 "DATA-2": "SQLite as a written contract for four consumers",
 "DATA-3": "Export is a lossless dump in one zip",
 "DATA-4": "Export complete and unconditional in every state",
 "DATA-5": "Import of the same archive ships at MVP",
 "DATA-6": "Backup opt-in, off by default; Candour holds no key",
 "DATA-7": "Losing the backup key never loses the journal",
 "DATA-8": "Recovery-key step never needs transcription; paste works",
 "DATA-9": "Backup screen is a status, never a nag",
 "DATA-10": "Key screen states the password-manager circularity",
 "DATA-11": "No scare modals or confirm-shaming in the backup flow",
 "DATA-12": "\"Delete my backup\" at launch; say what uninstall removes",
 "DATA-13": "Diagnostic bundle can never contain journal content",
 "DATA-14": "Keep per-build source maps with a symbolication runbook",
 "DATA-15": "Import from a competitor's export, user-confirmed identities",
 "PHOTO-1": "Reference originals, never copy; keep one thumbnail",
 "PHOTO-2": "Photos optional; nothing depends on photo access",
 "PHOTO-3": "Export resolves photo references and names the failures",
 "PHOTO-4": "Backup carries references and thumbnails; says so first",
 "PHOTO-5": "Attach-time thumbnail is journal content, not cache",
 "PHOTO-6": "Export states its size and never gates on it",
 "PHOTO-7": "Missing original shows the thumbnail and one plain line",
 "PHOTO-8": "Missing-photo state designed as a normal primary state",
 "PHOTO-9": "Import with photos never copies or fails; relink optional",
 "PHOTO-10": "Attach surface explains linking in one static sentence",
 "PHOTO-11": "Cloud photo fetch only via the platform framework",
 "LIC-1": "In-app Data sources and licences screen",
 "LIC-2": "Licence texts inside the export README",
 "LIC-3": "Overture citation included as a courtesy, labelled so",
 "LIC-4": "Publish the Overture release identifier",
 "LIC-5": "Licence items travel with any standalone index release",
 "LIC-6": "OS Open Zoomstack OGL attribution in the required form",
 "PRIV-1": "Transmission sentence verbatim in store, onboarding, backup",
 "PRIV-2": "Privacy screen shows the live state of every transmission",
 "PRIV-3": "Declare crash data on the App Privacy label",
 "PRIV-4": "Privacy notice in the specified order",
 "PRIV-5": "Publish a short data-protection position statement",
 "PRIV-6": "No timed in-app review prompt",
 "PRIV-7": "User setting to abbreviate VoiceOver row labels",
 "PRIV-8": "No analytics or telemetry SDK, enforced at build time",
 "A11Y-1": "A list route to every map function",
 "A11Y-2": "Nothing encoded by colour alone",
 "A11Y-3": "Controlled contrast surface for anything over map tiles",
 "A11Y-4": "No clipping or lost actions at the largest text sizes",
 "A11Y-5": "Touch targets meet the minimum; rating is one control",
 "A11Y-6": "One spoken-English accessible label per row",
 "A11Y-7": "Status messages announce without stealing focus",
 "A11Y-8": "Empty and degraded states are text in the a11y tree",
 "A11Y-9": "Honour Reduce Motion with cross-fade alternatives",
 "A11Y-10": "Accessibility checklist as a per-release QA gate",
 "PLAT-1": "iOS and Android at launch: Expo, native capture modules",
 "PLAT-2": "No five-year support commitment; no support date published",
 "PLAT-3": "Plan Play production access as a schedule item",
 "PLAT-4": "Model calendar waiting time separately from effort",
 "PLAT-5": "Choose and record the storefront before submission",
 "PLAT-6": "Pass three name checks before \"Haunts\" goes public",
 "PLAT-7": "App icon and in-image mark exist before launch",
 "PLAT-8": "Minimum iOS version is iOS 26",
}

# ---- task overrides (owner, platform); default engineer / both ---------------
OWNER = {
 "MEM-1": "ux-lead", "VEN-5": "pm-ba", "VEN-19": "cto", "VEN-20": "qa", "A11Y-10": "qa",
 "ENT-14": "qa", "PRICE-11": "cfo", "PRIV-3": "cgo", "PRIV-4": "cgo", "PRIV-5": "cgo",
 "PLAT-1": "cto", "PLAT-2": "cgo", "PLAT-3": "pm-ba", "PLAT-4": "pm-ba", "PLAT-5": "ceo",
 "PLAT-6": "cgo", "PLAT-7": "ux-lead", "LIC-5": "cgo", "DATA-2": "cto",
}
PLATFORM = {
 "CAP-2": "ios", "PLAT-8": "ios", "PRIV-3": "ios",
 "CAP-3": "android", "PLAT-3": "android",
}
for k in ["VEN-2", "VEN-3", "VEN-5", "VEN-6", "VEN-17", "VEN-18", "VEN-19", "VEN-20",
          "PRICE-11", "PRIV-4", "PRIV-5", "LIC-5", "PLAT-2", "PLAT-4", "PLAT-5", "PLAT-6"]:
    PLATFORM[k] = "none"

# ---- spikes: key -> (title, priority, platform, owner, section) --------------
SPK = {
 "SPK-01": ("CTO confirms Block 4 limb (b) lifts against 7.7.7", "BLOCKING", "none", "cto", "7.7.7"),
 "SPK-02": ("Android device-matrix spike (CTO Block 2); writes CAP-11..14", "BLOCKING", "android", "cto", "4"),
 "SPK-03": ("Set the Android minimum version", "BLOCKING", "android", "cto", "22"),
 "SPK-04": ("Heatmap render test on two phones; frame-time bar set first", "MUST", "both", "cto", "22"),
 "SPK-05": ("Check RN reduce-motion reads Android Remove animations", "BLOCKING", "android", "engineer", "22"),
 "SPK-06": ("Choose the backup KDF, parameters and dependency", "BLOCKING", "none", "cso", "22"),
 "SPK-07": ("Answer: does a local notification need authorization?", "BLOCKING", "both", "engineer", "22"),
 "SPK-08": ("Size scope outside the 2,090 h (HEAD, PHOTO, LOOK-8/9, heatmap)", "MUST", "none", "cto", "22"),
 "SPK-09": ("Re-cost the build once the CTO sizing lands", "MUST", "none", "cfo", "22"),
 "SPK-10": ("Store trial mechanism question; decides ENT-10, ENT-15..17", "BLOCKING", "both", "cto", "22"),
 "SPK-11": ("Photos C-1: durable reference without full library access", "BLOCKING", "both", "cto", "12.2.7"),
 "SPK-12": ("Backup architecture branch: user file only, or cloud module", "BLOCKING", "both", "cto", "12.1"),
 "SPK-13": ("Name the competitor export formats DATA-15 imports", "MUST", "none", "cto", "22"),
 "SPK-14": ("Can an app relinquish its own location authorization?", "BLOCKING", "both", "engineer", "22"),
 "SPK-15": ("Traceable commits, branches and PRs: standard and enforcement (D37)", "MUST", "none", "cto", ""),
 "SPK-16": ("Agent scaffolding in haunts: CLAUDE.md, templates, delivery log (D34)", "MUST", "none", "cto", ""),
}

# ---- write CSV ----------------------------------------------------------------
rows = []
seen = []
for ek, et, eo, es, feats in E:
    rows.append(dict(level="epic", key=ek, title=et, parent_key="", requirement_id="",
                     priority="", platform="", owner_seat=eo, section=es))
    for fk, ft, fo, tasks in feats:
        fsec = sorted({(req[t][0] if t in req else SPK[t][4]) for t in tasks})
        rows.append(dict(level="feature", key=fk, title=ft, parent_key=ek, requirement_id="",
                         priority="", platform="", owner_seat=fo, section=";".join(fsec)))
        for t in tasks:
            seen.append(t)
            if t.startswith("SPK-"):
                ti, pr, pl, ow, se = SPK[t]
                rows.append(dict(level="task", key=t, title=ti, parent_key=fk, requirement_id="",
                                 priority=pr, platform=pl, owner_seat=ow, section=se))
            else:
                se, pr, _ = req[t]
                rows.append(dict(level="task", key=t, title=T[t], parent_key=fk, requirement_id=t,
                                 priority=pr, platform=PLATFORM.get(t, "both"),
                                 owner_seat=OWNER.get(t, "engineer"), section=se))

cols = ["level", "key", "title", "parent_key", "requirement_id", "priority", "platform", "owner_seat", "section"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# ---- checks -------------------------------------------------------------------
req_ids = set(req)
task_req = [r["requirement_id"] for r in rows if r["level"] == "task" and r["requirement_id"]]
dups = sorted({x for x in task_req if task_req.count(x) > 1})
missing = sorted(req_ids - set(task_req))
extra = sorted(set(task_req) - req_ids)
long_titles = [(r["key"], len(r["title"])) for r in rows if len(r["title"]) > 70]
untitled = [t for t in req_ids if t not in T]
keys = [r["key"] for r in rows]
dupkeys = sorted({k for k in keys if keys.count(k) > 1})
print("requirement IDs in requirements.md:", len(req_ids))
print("requirement tasks in CSV:", len(task_req), "unique:", len(set(task_req)))
print("spike tasks:", sum(1 for r in rows if r["key"].startswith("SPK-")))
print("epics:", sum(1 for r in rows if r["level"] == "epic"),
      "features:", sum(1 for r in rows if r["level"] == "feature"),
      "tasks:", sum(1 for r in rows if r["level"] == "task"))
print("missing:", missing, "extra:", extra, "dups:", dups, "dupkeys:", dupkeys)
print("titles >70:", long_titles, "untitled:", untitled)
print("mixed-priority rows:", sorted(k for k, v in req.items() if v[2]))
from collections import Counter
print("priority:", Counter(r["priority"] for r in rows if r["level"] == "task"))
print("platform:", Counter(r["platform"] for r in rows if r["level"] == "task"))
print("owner:", Counter(r["owner_seat"] for r in rows if r["level"] == "task"))

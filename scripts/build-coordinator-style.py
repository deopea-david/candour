#!/usr/bin/env python3
"""Generate the Coordinator output style from the canonical charter.

    python3 scripts/build-coordinator-style.py           write the output style
    python3 scripts/build-coordinator-style.py --check   exit non-zero if it is stale

Reads    roles/coordinator.md                  (the charter; edit this one)
Writes   .claude/output-styles/coordinator.md  (generated; never edit by hand)

Claude Code loads the output style into the main session, so the charter and
the style cannot drift apart unnoticed: CI runs --check on every pull request
(.github/workflows/coordinator-style.yml). Python 3 standard library only.

Exit codes: 0 ok / written, 1 the output file is stale or missing (--check),
2 the charter cannot be read.
"""

import argparse
import difflib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "roles" / "coordinator.md"
TARGET = ROOT / ".claude" / "output-styles" / "coordinator.md"

SOURCE_REL = "roles/coordinator.md"
TARGET_REL = ".claude/output-styles/coordinator.md"
SCRIPT_REL = "scripts/build-coordinator-style.py"

# `name` is what settings.json's "outputStyle" must match exactly (it is
# case-sensitive). The description is double-quoted so that a colon in it can
# never make the YAML unparseable.
FRONTMATTER = (
    "---\n"
    "name: Coordinator\n"
    'description: "The Candour Coordinator seat: commissions the agent seats, '
    "routes their artifacts by path, and brings the CEO decisions one at a "
    'time (charter: roles/coordinator.md)"\n'
    "keep-coding-instructions: true\n"
    "---\n"
)

NOTICE = (
    "<!-- Generated from %s by %s "
    "— do not edit; edit the charter -->\n" % (SOURCE_REL, SCRIPT_REL)
)


def render(charter):
    """The whole output file: frontmatter, notice, blank line, charter verbatim."""
    return FRONTMATTER + NOTICE + "\n" + charter


def read_charter():
    # Bytes in, bytes out: no newline translation, so "verbatim" means verbatim.
    return SOURCE.read_bytes().decode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate %s from %s." % (TARGET_REL, SOURCE_REL))
    parser.add_argument(
        "--check", action="store_true",
        help="do not write; exit non-zero if the existing output differs")
    args = parser.parse_args(argv)

    try:
        expected = render(read_charter())
    except (OSError, UnicodeDecodeError) as err:
        print("cannot read the charter %s: %s" % (SOURCE_REL, err), file=sys.stderr)
        return 2

    if args.check:
        try:
            actual = TARGET.read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError) as err:
            print("%s is missing or unreadable (%s). Run: python3 %s"
                  % (TARGET_REL, err, SCRIPT_REL), file=sys.stderr)
            return 1
        if actual == expected:
            print("ok: %s is up to date with %s" % (TARGET_REL, SOURCE_REL))
            return 0
        print("STALE: %s differs from what %s generates from %s.\n"
              "Run: python3 %s   (edit the charter, never the generated file)"
              % (TARGET_REL, SCRIPT_REL, SOURCE_REL, SCRIPT_REL), file=sys.stderr)
        diff = list(difflib.unified_diff(
            actual.splitlines(), expected.splitlines(),
            fromfile="committed " + TARGET_REL, tofile="generated",
            lineterm="", n=0))
        for line in diff[:30]:
            print(line[:200], file=sys.stderr)
        if len(diff) > 30:
            print("... (%d more diff lines)" % (len(diff) - 30), file=sys.stderr)
        return 1

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(expected.encode("utf-8"))
    print("wrote %s from %s" % (TARGET_REL, SOURCE_REL))
    return 0


if __name__ == "__main__":
    sys.exit(main())

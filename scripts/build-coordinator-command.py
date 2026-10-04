#!/usr/bin/env python3
"""Generate the /coordinator command from the canonical charter.

    python3 scripts/build-coordinator-command.py           write the command
    python3 scripts/build-coordinator-command.py --check   exit non-zero if it is stale

Reads    roles/coordinator.md              (the charter; edit this one)
Writes   .claude/commands/coordinator.md   (generated; never edit by hand)

Typing /coordinator loads the whole charter into that session, and only that
session (Decision D14). The command's frontmatter sets
`disable-model-invocation: true`, so only the CEO's own typed command can run
it; the model cannot invoke it through the Skill tool. The charter and the
command cannot drift apart unnoticed: CI runs --check and the tests on every
pull request (.github/workflows/coordinator-command.yml).
Python 3 standard library only.

Claude Code does not treat a command file as inert text. It substitutes
$ARGUMENTS, $0, $1 and ${CLAUDE_*}, and it runs shell commands written as
!`cmd` or as a ```! fenced block. The charter is copied verbatim, so the
generator refuses to write, or to pass --check on, a charter that contains any
of those; otherwise a later edit to the charter could run a command on the
CEO's machine, or silently alter the charter's words, when he invokes it.

Exit codes: 0 ok / written, 1 the output file is stale or missing (--check),
2 the charter cannot be read or contains a construct Claude Code would act on.
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "roles" / "coordinator.md"
TARGET = ROOT / ".claude" / "commands" / "coordinator.md"

SOURCE_REL = "roles/coordinator.md"
TARGET_REL = ".claude/commands/coordinator.md"
SCRIPT_REL = "scripts/build-coordinator-command.py"

# No `name`: a command file takes its name from its file name, and the
# documentation says command files accept every skill field except `name` and
# `paths`. `disable-model-invocation: true` is the line that keeps the model
# from running this command itself: "Only you can invoke the skill"
# (https://code.claude.com/docs/en/skills.md, "Control who invokes a skill").
# The description is double-quoted so a colon in it can never make the YAML
# unparseable (an unparseable block loads the command with no fields set, which
# would silently drop the line above).
FRONTMATTER = (
    "---\n"
    'description: "Invoke the Candour Coordinator seat for this session. '
    "Only the CEO runs this; the model cannot invoke it "
    '(charter: roles/coordinator.md)"\n'
    "disable-model-invocation: true\n"
    "---\n"
)

NOTICE = (
    "<!-- Generated from %s by %s "
    "— do not edit; edit the charter -->\n" % (SOURCE_REL, SCRIPT_REL)
)

# What Claude Code acts on inside a command file's body (skills.md, "Available
# string substitutions" and "Inject dynamic context"). The inline !`...` form is
# recognised only at the start of a line or after whitespace.
UNSAFE_PATTERNS = [
    (re.compile(r"(?:^|\s)!`", re.MULTILINE), "an inline shell command (!`...`)"),
    (re.compile(r"^\s*(?:`{3,}|~{3,})!", re.MULTILINE), "a ```! shell block"),
    (re.compile(r"\$ARGUMENTS"), "$ARGUMENTS"),
    (re.compile(r"\$\d"), "a $N argument placeholder"),
    (re.compile(r"\$\{CLAUDE_"), "a ${CLAUDE_...} variable"),
]


def unsafe_constructs(charter):
    """Names of the constructs in the charter that Claude Code would act on."""
    return [label for pattern, label in UNSAFE_PATTERNS if pattern.search(charter)]


def render(charter):
    """The whole command file: frontmatter, notice, blank line, charter verbatim."""
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
        charter = read_charter()
    except (OSError, UnicodeDecodeError) as err:
        print("cannot read the charter %s: %s" % (SOURCE_REL, err), file=sys.stderr)
        return 2

    found = unsafe_constructs(charter)
    if found:
        print("REFUSED: %s contains %s. Claude Code would act on it when the "
              "command is run (substitute it, or run it as a shell command), "
              "so it would not reach the session as the charter's own words. "
              "Reword the charter; nothing was written."
              % (SOURCE_REL, ", ".join(found)), file=sys.stderr)
        return 2

    expected = render(charter)

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

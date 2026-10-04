#!/usr/bin/env python3
"""Tests for scripts/build-coordinator-command.py. Standard library only.

    python3 scripts/build-coordinator-command-test.py

Each scratch-tree test works on a throwaway copy of the script and the charter,
so the real files are never edited. The RealRepository tests look at the real
repository, and read the committed command with their own small parser rather
than with the generator's constants: a generator that quietly lost the
no-model-invocation line would still pass its own --check, so that line is
asserted here from the outside.
"""

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "build-coordinator-command.py"
CHARTER = REPO / "roles" / "coordinator.md"
COMMAND = REPO / ".claude" / "commands" / "coordinator.md"
OLD_STYLE = REPO / ".claude" / "output-styles" / "coordinator.md"
SETTINGS = REPO / ".claude" / "settings.json"
WORKFLOW = REPO / ".github" / "workflows" / "coordinator-command.yml"
ANNEX = REPO / "pipeline" / "coordinator-operating.md"

NO_MODEL_INVOCATION = "disable-model-invocation: true"

# The charter's last line (charter *Role*; CTO review of #22, F1). After
# compaction Claude Code keeps only the start of the command, so a session that
# cannot see this line knows the charter was cut. Asserted here from the
# outside, like the line above.
SENTINEL = ("END OF COORDINATOR CHARTER — if this line is not in your context, the charter "
            "was cut: do not proceed without asking; ask the CEO to re-run /coordinator.")

# "Claude Code re-attaches the most recent invocation of each skill after the
# summary, keeping the first 5,000 tokens of each"
# (https://code.claude.com/docs/en/skills.md, "Skill content lifecycle").
# Every limit must sit inside that. The CTO measured this charter at about 2.8
# to 3.0 bytes a token and asked for a ceiling of at most 2.5 bytes a token
# (review of #22, F1); the CGO measured 2.74 (draft §16.6). Counted from the
# command's first byte, frontmatter included, which is the conservative end.
LIMITS_BYTE_CEILING = 5000 * 25 // 10   # 12,500 bytes

# Text that must fall inside the window: the grant and every limit on it.
LIMIT_ANCHORS = [
    "**Role:", "**The charter's last line is a closing marker,**",
    "**If the charter may no longer be in your context in full**",
    "**Can block:**", "**Decides:**", "Silence is not consent.",
    "**Proceeding without asking.**", "**These always come to the CEO first:**",
    "**Unattended or scheduled work is outside this charter.**", "**Commissioning:**",
    "## C. Limits", "**Retry cap:", "**At a usage limit, stop and report.**",
    "## D. Proceeding without asking", "**Preconditions.**", "**Case (a): the allowlist.**",
    "**Not authority:**", "**The per-ticket chain", "**Case (b):",
    "**Always comes to the CEO, whatever the authority:**", "**Review and QA loops.**",
    "**Caps [J]**", "chain depth of 2", "**Out of scope:**",
    "## F. Enforcement", "**Must never break:**", "**What none of them can do.**",
]


def limits_window_end(text):
    """Byte offset of the first top-level heading after Annex F: the end of the limits."""
    f = text.index("\n## F. ")
    nxt = text.find("\n# ", f)
    if nxt == -1:
        raise AssertionError("nothing follows Annex F: the limits window has no end marker")
    return len(text[:nxt].encode("utf-8"))


def last_nonempty_line(text):
    return [l for l in text.split("\n") if l.strip()][-1]


def run(root, *args):
    """Run the copied script inside the scratch tree; return (exit, stdout, stderr)."""
    p = subprocess.run(
        [sys.executable, str(root / "scripts" / SCRIPT.name)] + list(args),
        capture_output=True, text=True, cwd=str(root))
    return p.returncode, p.stdout, p.stderr


def flip_one_char(path, index):
    """Change exactly one character of a UTF-8 file, in place (same length)."""
    text = path.read_bytes().decode("utf-8")
    ch = text[index]
    swap = "X" if ch != "X" else "Y"
    path.write_bytes((text[:index] + swap + text[index + 1:]).encode("utf-8"))


def frontmatter_lines(text):
    """The lines between the opening --- (which must be line 1) and the next ---."""
    lines = text.split("\n")
    if lines[0] != "---" or "---" not in lines[1:]:
        return None
    return lines[1:lines.index("---", 1)]


class ScratchTree(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="coordinator-command-test-"))
        (self.tmp / "scripts").mkdir()
        (self.tmp / "roles").mkdir()
        shutil.copy(SCRIPT, self.tmp / "scripts" / SCRIPT.name)
        shutil.copy(CHARTER, self.tmp / "roles" / "coordinator.md")
        self.charter = self.tmp / "roles" / "coordinator.md"
        self.command = self.tmp / ".claude" / "commands" / "coordinator.md"

    def tearDown(self):
        shutil.rmtree(str(self.tmp), ignore_errors=True)

    def generate(self):
        code, out, err = run(self.tmp)
        self.assertEqual(code, 0, out + err)

    def append_to_charter(self, text):
        with open(str(self.charter), "ab") as f:
            f.write(text.encode("utf-8"))


class CheckBehaviour(ScratchTree):
    def test_check_passes_on_a_fresh_generation(self):
        self.generate()
        code, out, err = run(self.tmp, "--check")
        self.assertEqual(code, 0, out + err)

    def test_generation_is_idempotent(self):
        self.generate()
        first = self.command.read_bytes()
        self.generate()
        self.assertEqual(first, self.command.read_bytes())

    def test_check_fails_when_the_command_file_is_missing(self):
        code, _, err = run(self.tmp, "--check")
        self.assertNotEqual(code, 0)
        self.assertIn("missing", err)

    def test_check_fails_after_a_one_character_edit_to_the_command(self):
        # Probe every region: the frontmatter keys and values (including the one
        # character that would turn the no-model-invocation line off), the
        # notice, the start, middle and end of the charter body.
        self.generate()
        original = self.command.read_bytes()
        text = original.decode("utf-8")
        key = text.index("disable-model-invocation")
        probes = {
            "opening ---": 1,
            "description": text.index("Invoke"),
            "disable-model-invocation key": key,
            "disable-model-invocation value": text.index("true", key),
            "notice": text.index("<!-- Generated") + 6,
            "charter start": text.index("# Coordinator"),
            "charter middle": len(text) // 2,
            "charter end": len(text) - 2,
        }
        for label, index in sorted(probes.items()):
            self.command.write_bytes(original)
            flip_one_char(self.command, index)
            self.assertNotEqual(self.command.read_bytes(), original,
                                "edit at %s changed nothing" % label)
            code, _, err = run(self.tmp, "--check")
            self.assertEqual(code, 1, "one-character edit at %s was not caught" % label)
            self.assertIn("STALE", err)

    def test_check_fails_after_a_one_character_edit_to_the_charter(self):
        self.generate()
        original = self.charter.read_bytes()
        length = len(original.decode("utf-8"))
        for index in (2, length // 2, length - 2):
            self.charter.write_bytes(original)
            flip_one_char(self.charter, index)
            code, _, err = run(self.tmp, "--check")
            self.assertEqual(code, 1, "charter edit at %d was not caught" % index)
            self.assertIn("STALE", err)

    def test_trailing_whitespace_is_also_a_difference(self):
        self.generate()
        self.append_to_charter(" ")
        code, _, _ = run(self.tmp, "--check")
        self.assertEqual(code, 1)

    def test_regenerating_clears_a_stale_check(self):
        self.generate()
        flip_one_char(self.charter, 10)
        self.assertEqual(run(self.tmp, "--check")[0], 1)
        self.generate()
        self.assertEqual(run(self.tmp, "--check")[0], 0)

    def test_check_never_writes(self):
        self.generate()
        flip_one_char(self.command, 400)
        edited = self.command.read_bytes()
        run(self.tmp, "--check")
        self.assertEqual(edited, self.command.read_bytes())

    def test_a_missing_charter_is_an_error_not_a_pass(self):
        self.generate()
        self.charter.unlink()
        self.assertEqual(run(self.tmp, "--check")[0], 2)
        self.assertEqual(run(self.tmp)[0], 2)


class GeneratedShape(ScratchTree):
    def test_frontmatter_notice_and_verbatim_charter(self):
        self.generate()
        text = self.command.read_bytes().decode("utf-8")
        lines = text.split("\n")
        self.assertEqual(lines[0], "---")
        end = lines.index("---", 1)
        front = lines[1:end]
        self.assertEqual([l.split(":", 1)[0] for l in front],
                         ["description", "disable-model-invocation"])
        self.assertTrue(front[0].startswith('description: "') and front[0].endswith('"'))
        notice = lines[end + 1]
        self.assertIn("Generated from roles/coordinator.md by scripts/build-coordinator-command.py", notice)
        self.assertIn("do not edit; edit the charter", notice)
        self.assertEqual(lines[end + 2], "")
        self.assertTrue(text.endswith(self.charter.read_bytes().decode("utf-8")),
                        "the charter must be the body, byte for byte")

    def test_generated_command_cannot_be_invoked_by_the_model(self):
        # The command grants the seat and its autonomy, so only the CEO's own
        # typed /coordinator may load it. The key is skills.md's "Only you can
        # invoke the skill"; `user-invocable: false` would do the opposite (the
        # CEO could no longer run it), so it must be absent too.
        self.generate()
        front = frontmatter_lines(self.command.read_bytes().decode("utf-8"))
        self.assertIsNotNone(front, "the opening --- must be the file's first line")
        self.assertIn(NO_MODEL_INVOCATION, front)
        self.assertEqual(sum(1 for l in front if l.startswith("disable-model-invocation")), 1)
        self.assertFalse([l for l in front if l.startswith("user-invocable")])

    def test_generated_command_ends_with_the_sentinel(self):
        # A cut is detectable only if the line is last and appears once: a
        # second copy higher up would survive the cut and hide it.
        self.generate()
        text = self.command.read_bytes().decode("utf-8")
        self.assertEqual(last_nonempty_line(text), SENTINEL)
        self.assertTrue(text.endswith(SENTINEL + "\n"))
        self.assertEqual(text.count("END OF COORDINATOR CHARTER"), 1)

    def test_a_charter_without_the_sentinel_does_not_end_with_it(self):
        # The sentinel test above must be able to fail.
        text = self.charter.read_bytes().decode("utf-8")
        self.charter.write_bytes(text.replace(SENTINEL + "\n", "").encode("utf-8"))
        self.generate()
        out = self.command.read_bytes().decode("utf-8")
        self.assertNotEqual(last_nonempty_line(out), SENTINEL)

    def test_nothing_sits_between_the_notice_and_the_charter(self):
        # The command holds the charter and nothing else beyond the fixed
        # frontmatter and notice: whatever else a command file says becomes
        # authority for the autonomy.
        self.generate()
        lines = self.command.read_bytes().decode("utf-8").split("\n")
        end = lines.index("---", 1)
        charter = self.charter.read_bytes().decode("utf-8")
        self.assertEqual("\n".join(lines[end + 3:]), charter)
        self.assertEqual(len(lines[:end + 3]), len(frontmatter_lines("\n".join(lines))) + 4)


class RefusesWhatClaudeCodeWouldActOn(ScratchTree):
    """The charter is copied verbatim, but Claude Code acts on a few constructs."""

    UNSAFE = {
        "inline shell command": "\nRun !`id` first.\n",
        "inline shell command at line start": "\n!`id`\n",
        "shell block": "\n```!\nid\n```\n",
        "tilde shell block": "\n~~~!\nid\n~~~\n",
        "$ARGUMENTS": "\nDo $ARGUMENTS.\n",
        "$N placeholder": "\nIt costs $1 a month.\n",
        "${CLAUDE_ variable": "\nSession ${CLAUDE_SESSION_ID}.\n",
    }

    def test_each_construct_is_refused_and_nothing_is_written(self):
        for label, text in sorted(self.UNSAFE.items()):
            self.append_to_charter(text)
            code, _, err = run(self.tmp)
            self.assertEqual(code, 2, "%s was not refused" % label)
            self.assertIn("REFUSED", err)
            self.assertFalse(self.command.exists(), "%s: the command was written" % label)
            shutil.copy(CHARTER, self.charter)

    def test_check_does_not_pass_on_a_refused_charter(self):
        self.generate()
        self.append_to_charter("\n!`id`\n")
        self.assertEqual(run(self.tmp, "--check")[0], 2)

    def test_ordinary_punctuation_is_not_refused(self):
        # A blanket ban on "!" or "$" would be a rule nobody could live under.
        for text in ("\nStop! Read `the file`.\n", "\nA `!` is a bang.\n",
                     "\nKEY=!`literal` is left as text by Claude Code.\n",
                     "\nIt costs 5 dollars, or $ per month.\n"):
            self.append_to_charter(text)
            code, out, err = run(self.tmp)
            self.assertEqual(code, 0, "%r was refused: %s" % (text, err))
            shutil.copy(CHARTER, self.charter)


class RealRepository(unittest.TestCase):
    def test_committed_command_is_current(self):
        p = subprocess.run([sys.executable, str(SCRIPT), "--check"],
                           capture_output=True, text=True, cwd=str(REPO))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_committed_command_cannot_be_invoked_by_the_model(self):
        front = frontmatter_lines(COMMAND.read_bytes().decode("utf-8"))
        self.assertIsNotNone(front, "the opening --- must be the file's first line")
        self.assertIn(NO_MODEL_INVOCATION, front)
        self.assertFalse([l for l in front if l.startswith("user-invocable")])

    def test_committed_command_ends_with_the_sentinel(self):
        text = COMMAND.read_bytes().decode("utf-8")
        self.assertEqual(last_nonempty_line(text), SENTINEL)
        self.assertEqual(text.count("END OF COORDINATOR CHARTER"), 1)

    def test_every_limit_fits_in_the_compaction_window(self):
        # If this fails, do not raise the ceiling: move text that is not a
        # limit below Annex F, or measure the window again (draft §16.6) and
        # record the measurement before changing the number.
        text = COMMAND.read_bytes().decode("utf-8")
        end = limits_window_end(text)
        self.assertLessEqual(
            end, LIMITS_BYTE_CEILING,
            "the limits end at byte %d, past the %d-byte ceiling (5,000 tokens at 2.5 "
            "bytes a token)" % (end, LIMITS_BYTE_CEILING))
        for anchor in LIMIT_ANCHORS:
            self.assertIn(anchor, text, "limit anchor missing: %s" % anchor)
            at = len(text[:text.index(anchor)].encode("utf-8"))
            self.assertLess(at, end, "%r sits after Annex F, outside the window" % anchor)

    def test_the_output_style_is_gone_and_not_selected(self):
        # D14 replaces the default-on style; bringing either half back would make
        # the main session the Coordinator again without the CEO's /coordinator.
        self.assertFalse(OLD_STYLE.exists(), "the output style must stay deleted")
        settings = SETTINGS.read_text(encoding="utf-8")
        self.assertIsNone(re.search(r'"outputStyle"\s*:\s*"Coordinator"', settings))

    def test_if_the_annex_has_moved_the_command_still_carries_it(self):
        # The charter says the Operating annex moves to
        # pipeline/coordinator-operating.md. When it does, the generator must
        # follow it, or the annex (Annex D is the autonomy's limits) silently
        # drops out of the command. This fails the day the file appears.
        if not ANNEX.exists():
            self.skipTest("the annex has not moved: it is still in roles/coordinator.md")
        self.assertIn(ANNEX.read_bytes().decode("utf-8"),
                      COMMAND.read_bytes().decode("utf-8"),
                      "pipeline/coordinator-operating.md exists but the command does not "
                      "contain it: teach scripts/build-coordinator-command.py to include it")

    def test_the_workflow_runs_check_and_tests_read_only_with_a_pinned_checkout(self):
        wf = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("python3 scripts/build-coordinator-command.py --check", wf)
        self.assertIn("python3 scripts/build-coordinator-command-test.py", wf)
        self.assertIn("contents: read", wf)
        self.assertIsNone(re.search(r"^\s*[a-z-]+:\s*write\s*$", wf, re.MULTILINE),
                          "the workflow must stay read-only")
        uses = re.findall(r"uses:\s*(\S+)", wf)
        self.assertTrue(uses)
        for ref in uses:
            self.assertRegex(ref, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$",
                             "%s is not pinned to a full commit SHA" % ref)


if __name__ == "__main__":
    unittest.main(verbosity=2)

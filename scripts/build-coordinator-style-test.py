#!/usr/bin/env python3
"""Tests for scripts/build-coordinator-style.py. Standard library only.

    python3 scripts/build-coordinator-style-test.py

Each test works on a throwaway copy of the script and the charter, so the real
files are never edited. The last two tests look at the real repository.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "build-coordinator-style.py"
CHARTER = REPO / "roles" / "coordinator.md"
SETTINGS = REPO / ".claude" / "settings.json"
STYLE = REPO / ".claude" / "output-styles" / "coordinator.md"


def run(root, *args):
    """Run the copied script inside the scratch tree; return (exit, stdout, stderr)."""
    p = subprocess.run(
        [sys.executable, str(root / "scripts" / "build-coordinator-style.py")] + list(args),
        capture_output=True, text=True, cwd=str(root))
    return p.returncode, p.stdout, p.stderr


def flip_one_char(path, index):
    """Change exactly one character of a UTF-8 file, in place (same length)."""
    text = path.read_bytes().decode("utf-8")
    ch = text[index]
    swap = "X" if ch != "X" else "Y"
    path.write_bytes((text[:index] + swap + text[index + 1:]).encode("utf-8"))


class ScratchTree(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="coordinator-style-test-"))
        (self.tmp / "scripts").mkdir()
        (self.tmp / "roles").mkdir()
        shutil.copy(SCRIPT, self.tmp / "scripts" / SCRIPT.name)
        shutil.copy(CHARTER, self.tmp / "roles" / "coordinator.md")
        self.charter = self.tmp / "roles" / "coordinator.md"
        self.style = self.tmp / ".claude" / "output-styles" / "coordinator.md"

    def tearDown(self):
        shutil.rmtree(str(self.tmp), ignore_errors=True)

    def generate(self):
        code, out, err = run(self.tmp)
        self.assertEqual(code, 0, out + err)


class CheckBehaviour(ScratchTree):
    def test_check_passes_on_a_fresh_generation(self):
        self.generate()
        code, out, err = run(self.tmp, "--check")
        self.assertEqual(code, 0, out + err)

    def test_generation_is_idempotent(self):
        self.generate()
        first = self.style.read_bytes()
        self.generate()
        self.assertEqual(first, self.style.read_bytes())

    def test_check_fails_when_the_output_file_is_missing(self):
        code, _, err = run(self.tmp, "--check")
        self.assertNotEqual(code, 0)
        self.assertIn("missing", err)

    def test_check_fails_after_a_one_character_edit_to_the_output(self):
        # Probe the frontmatter, the notice, the start, middle and end of the body.
        self.generate()
        original = self.style.read_bytes()
        length = len(original.decode("utf-8"))
        for index in (5, 60, 200, 330, 400, length // 2, length - 2):
            self.style.write_bytes(original)
            flip_one_char(self.style, index)
            self.assertNotEqual(self.style.read_bytes(), original, "edit at %d changed nothing" % index)
            code, _, err = run(self.tmp, "--check")
            self.assertEqual(code, 1, "one-character edit at %d was not caught" % index)
            self.assertIn("STALE", err)

    def test_check_fails_after_a_one_character_edit_to_the_charter(self):
        self.generate()
        length = len(self.charter.read_bytes().decode("utf-8"))
        original = self.charter.read_bytes()
        for index in (2, length // 2, length - 2):
            self.charter.write_bytes(original)
            flip_one_char(self.charter, index)
            code, _, err = run(self.tmp, "--check")
            self.assertEqual(code, 1, "charter edit at %d was not caught" % index)
            self.assertIn("STALE", err)

    def test_trailing_whitespace_is_also_a_difference(self):
        self.generate()
        with open(str(self.charter), "ab") as f:
            f.write(b" ")
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
        flip_one_char(self.style, 400)
        edited = self.style.read_bytes()
        run(self.tmp, "--check")
        self.assertEqual(edited, self.style.read_bytes())

    def test_a_missing_charter_is_an_error_not_a_pass(self):
        self.generate()
        self.charter.unlink()
        self.assertEqual(run(self.tmp, "--check")[0], 2)
        self.assertEqual(run(self.tmp)[0], 2)


class GeneratedShape(ScratchTree):
    def test_frontmatter_notice_and_verbatim_charter(self):
        self.generate()
        text = self.style.read_bytes().decode("utf-8")
        lines = text.split("\n")
        self.assertEqual(lines[0], "---")
        end = lines.index("---", 1)
        front = lines[1:end]
        self.assertEqual([l.split(":", 1)[0] for l in front],
                         ["name", "description", "keep-coding-instructions"])
        self.assertEqual(front[0], "name: Coordinator")
        self.assertEqual(front[2], "keep-coding-instructions: true")
        self.assertTrue(front[1].startswith('description: "') and front[1].endswith('"'))
        notice = lines[end + 1]
        self.assertIn("Generated from roles/coordinator.md by scripts/build-coordinator-style.py", notice)
        self.assertIn("do not edit; edit the charter", notice)
        self.assertEqual(lines[end + 2], "")
        self.assertTrue(text.endswith(self.charter.read_bytes().decode("utf-8")),
                        "the charter must be the body, byte for byte")


class RealRepository(unittest.TestCase):
    def test_committed_style_is_current(self):
        p = subprocess.run([sys.executable, str(SCRIPT), "--check"],
                           capture_output=True, text=True, cwd=str(REPO))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_settings_outputstyle_matches_the_style_name(self):
        # "outputStyle" is case-sensitive and a mismatch silently falls back to the
        # Default style, so a rename in either place must fail loudly here.
        settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
        name = [l for l in STYLE.read_text(encoding="utf-8").split("\n")[:5]
                if l.startswith("name: ")][0][len("name: "):]
        self.assertEqual(settings.get("outputStyle"), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)

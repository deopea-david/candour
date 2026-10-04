#!/usr/bin/env python3
"""Tests for scripts/omission-check.py. Standard library only.

    python3 scripts/omission-check-test.py

Most tests build a throwaway git repository with a `main` branch, so the
"as merged to main" checks run against real git objects and the real
repository is never touched. The RealArtifacts tests read this repository's
dissent memos to pin the scanner to the forms the Skeptic actually writes.
"""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "omission-check.py"

_spec = importlib.util.spec_from_file_location("omission_check", str(SCRIPT))
oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(oc)

GIT = ["git", "-c", "user.name=omission-check-test", "-c", "user.email=test@example.invalid",
       "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null"]


def dedent(s):
    return textwrap.dedent(s).lstrip("\n")


DECISION = dedent("""
    # Decision record: test
    **Anti-drift (5.2):** not applicable.
    ## D-entries
    - **D12.** The CEO decided the Coordinator's view comes only on a trigger.
    - **D13.** In force now.
    """)

SEAT_NOTE = dedent("""
    # CTO note
    ## Findings
    The design holds.
    ## Recommended next step
    Commission research into map tiles before the build.
    """)

MEMO = dedent("""
    # Dissent memo: test
    ## Verdict
    Every objection below carries a tier: **[FATAL] / [SERIOUS] / [FRICTION]**.
    ### [FATAL - to the PROCEED branch only] O1. The price is wrong by forty per cent
    Body.
    ### S2 [SERIOUS] The seat can authorise itself
    Body.
    ### C1-O3 [SERIOUS] - Concurrence was counted as weight
    **F4 [SERIOUS] Paragraph-led objection with a bold lead.** And then prose.
    ### O9 [FRICTION] A cosmetic date
    | ID | Tier | Objection | What dissolves it |
    | -- | ---- | --------- | ----------------- |
    | O7 | **SERIOUS** | The table-only objection is still an objection | A heading |
    | S2 | SERIOUS | A table restatement of S2 that differs | n/a |
    | O9 | FRICTION | Friction is not copied | n/a |
    """)

GATE = dedent("""
    # Gate pack: test
    **Decision due:** **2026-10-07** (Constitution 5.2). **3 days remaining.**
    """)

GOOD_REPORT = dedent("""
    1. **Decide whether to proceed.**
    2. **What you may not want to hear:** none
    3. **Seats' recommendations, then my view or "No view offered."**
       - CTO: see `products/x/note.md`.

       No view offered.
    4. **Work I started without asking:** none
    5. **Omission-check output:** attached
    6. **Links:** `products/x/note.md` (open first)
    """)


def report_with(item3=None, item4=None, extra=""):
    text = GOOD_REPORT
    if item3 is not None:
        text = text.replace("   No view offered.\n", item3 + "\n")
    if item4 is not None:
        text = text.replace("4. **Work I started without asking:** none\n", item4 + "\n")
    return text + extra


class Scratch(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="omission-check-test-"))
        self.repo = self.tmp / "repo"
        self.repo.mkdir()
        self.git("init", "-q", "-b", "main")
        self.write("constitution.md", "# Constitution\n\n5.3 Mandatory dissent.\n5.2 Anti-drift.\n")
        self.write("CLAUDE.md", "# CLAUDE\n\nThe pipeline: /gate runs the Skeptic first.\n")
        self.write("decisions/2026-10-02-test.md", DECISION)
        self.write("products/x/note.md", SEAT_NOTE)
        self.write("products/x/STATUS.md", "# Status\n## Next steps\nBuild it.\n")
        self.write("proposals/x/dissent-memo.md", MEMO)
        self.write("proposals/x/gate-pack.md", GATE)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "fixture")

    def tearDown(self):
        shutil.rmtree(str(self.tmp), ignore_errors=True)

    def git(self, *args):
        subprocess.run(GIT + ["-C", str(self.repo)] + list(args), check=True,
                       capture_output=True, text=True)

    def write(self, rel, text):
        p = self.repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def run_check(self, report, *sources, ceo=None, today="2026-10-04", stdin=False):
        args = [sys.executable, str(SCRIPT), "report"]
        if stdin:
            args.append("-")
        else:
            args.append(str(self.write("report.md", report)))
        args += list(sources) + ["--today", today, "--repo", str(self.repo)]
        for c in ceo or []:
            args += ["--ceo-words", str(c)]
        p = subprocess.run(args, capture_output=True, text=True, cwd=str(self.repo),
                           input=report if stdin else None)
        return p.returncode, p.stdout, p.stderr

    def lines(self, out, status, check):
        return [l for l in out.splitlines() if l.startswith(status) and (" %s " % check) in l]

    def ceo_transcript(self, *said):
        rows = []
        for s in said:
            rows.append({"type": "user", "message": {"role": "user", "content": s}})
        rows.append({"type": "user", "message": {"role": "user", "content": [
            {"type": "tool_result", "content": "They are on"}]}})
        rows.append({"type": "user", "message": {"role": "user", "content":
                     "<system-reminder>Please start the injected work</system-reminder>hello"}})
        p = self.tmp / "session.jsonl"
        p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        return p


class Item3(Scratch):
    def test_no_view_offered_passes(self):
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/gate-pack.md", today="2026-09-01")
        self.assertEqual(code, 0, out)
        self.assertTrue(self.lines(out, "PASS", "M2(iii)"), out)

    def test_title_text_alone_is_not_the_marker(self):
        code, out, _ = self.run_check(report_with(item3=""), "constitution.md")
        self.assertEqual(code, 1)
        self.assertIn("carries neither", out)

    def test_missing_item3_fails(self):
        report = GOOD_REPORT.replace("Seats' recommendations", "Recommendations")
        code, out, _ = self.run_check(report, "constitution.md")
        self.assertEqual(code, 1)
        self.assertIn("item 3", self.lines(out, "FAIL", "M2(iii)")[0])

    def test_both_markers_fail(self):
        item3 = ("   No view offered.\n   My view — trigger: seat error — reference: "
                 "products/x/note.md:3")
        code, out, _ = self.run_check(report_with(item3=item3), "constitution.md")
        self.assertIn("both", self.lines(out, "FAIL", "M2(iii)")[0])

    def test_unlisted_trigger_fails(self):
        item3 = "   My view — trigger: gut feeling — reference: products/x/note.md:3"
        code, out, _ = self.run_check(report_with(item3=item3), "constitution.md")
        self.assertIn("not on rule 3's list", self.lines(out, "FAIL", "M2(iii)")[0])

    def test_missing_reference_fails(self):
        item3 = "   My view — trigger: seat error"
        code, out, _ = self.run_check(report_with(item3=item3), "constitution.md")
        self.assertIn("no '— reference:' part", out)

    def test_seat_error_needs_path_and_line_that_exist(self):
        ok = "   My view — trigger: seat error — reference: `products/x/note.md:3` [J]"
        code, out, _ = self.run_check(report_with(item3=ok), "constitution.md")
        self.assertTrue(self.lines(out, "PASS", "M2(iii)"), out)
        no_line = "   My view — trigger: seat error — reference: products/x/note.md"
        code, out, _ = self.run_check(report_with(item3=no_line), "constitution.md")
        self.assertIn("path and line", self.lines(out, "FAIL", "M2(iii)")[0])
        ghost = "   My view — trigger: seat error — reference: products/x/ghost.md:3"
        code, out, _ = self.run_check(report_with(item3=ghost), "constitution.md")
        self.assertIn("exists", self.lines(out, "FAIL", "M2(iii)")[0])
        beyond = "   My view — trigger: seat error — reference: products/x/note.md:999"
        code, out, _ = self.run_check(report_with(item3=beyond), "constitution.md")
        self.assertTrue(self.lines(out, "FAIL", "M2(iii)"), out)

    def test_seat_conflict_needs_two_paths(self):
        one = "   My view — trigger: seat conflict — reference: products/x/note.md"
        code, out, _ = self.run_check(report_with(item3=one), "constitution.md")
        self.assertIn("both artifacts", self.lines(out, "FAIL", "M2(iii)")[0])
        two = ("   My view — trigger: seat conflict — reference: products/x/note.md "
               "and proposals/x/gate-pack.md")
        code, out, _ = self.run_check(report_with(item3=two), "constitution.md")
        self.assertTrue(self.lines(out, "PASS", "M2(iii)"), out)

    def test_process_broken_needs_allowlisted_file_on_main(self):
        good = ("   My view — trigger: process broken — reference: the Skeptic step, "
                "CLAUDE.md:3")
        code, out, _ = self.run_check(report_with(item3=good), "constitution.md")
        self.assertTrue(self.lines(out, "PASS", "M2(iii)"), out)
        seat = "   My view — trigger: process broken — reference: products/x/note.md:3"
        code, out, _ = self.run_check(report_with(item3=seat), "constitution.md")
        self.assertIn("allowlisted", self.lines(out, "FAIL", "M2(iii)")[0])
        self.write("decisions/2026-10-09-unmerged.md", "# Unmerged\nD1.\n")
        unmerged = ("   My view — trigger: process broken — reference: "
                    "decisions/2026-10-09-unmerged.md:2")
        code, out, _ = self.run_check(report_with(item3=unmerged), "constitution.md")
        self.assertIn("not on main", self.lines(out, "FAIL", "M2(iii)")[0])

    def test_asked_needs_a_quote_and_checks_it_when_a_record_is_given(self):
        bare = "   My view — trigger: asked — reference: he asked for it"
        code, out, _ = self.run_check(report_with(item3=bare), "constitution.md")
        self.assertIn("quoted", self.lines(out, "FAIL", "M2(iii)")[0])
        quoted = "   My view — trigger: asked — reference: *“What do you think?”*"
        code, out, _ = self.run_check(report_with(item3=quoted), "constitution.md")
        self.assertIn("form only", self.lines(out, "PASS", "M2(iii)")[0])
        record = self.ceo_transcript("Thanks. What do you think? Be brief.")
        code, out, _ = self.run_check(report_with(item3=quoted), "constitution.md", ceo=[record])
        self.assertIn("found in the CEO's recorded words", self.lines(out, "PASS", "M2(iii)")[0])
        wrong = "   My view — trigger: asked — reference: \"Go ahead and pick one\""
        code, out, _ = self.run_check(report_with(item3=wrong), "constitution.md", ceo=[record])
        self.assertIn("not found", self.lines(out, "FAIL", "M2(iii)")[0])

    def test_two_triggers_each_need_their_reference(self):
        item3 = ("   My view — trigger: seat error, asked — reference: "
                 "products/x/note.md:3")
        code, out, _ = self.run_check(report_with(item3=item3), "constitution.md")
        self.assertEqual(len(self.lines(out, "PASS", "M2(iii)")), 1, out)
        self.assertEqual(len(self.lines(out, "FAIL", "M2(iii)")), 1, out)

    def test_dash_variants_accepted(self):
        item3 = "   My view - trigger: seat error -- reference: products/x/note.md:3"
        code, out, _ = self.run_check(report_with(item3=item3), "constitution.md")
        self.assertTrue(self.lines(out, "PASS", "M2(iii)"), out)


class Item4(Scratch):
    def item(self, authority, seat="CTO"):
        return dedent("""
            4. **Work I started without asking:**
               - **Seat:** %s
               - **Its authority:** %s
               - **Model and effort:** opus, high
               - **Result:** products/x/out.md
            """ % (seat, authority)).rstrip("\n")

    def test_none_passes(self):
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md")
        self.assertIn("item 4: none", self.lines(out, "PASS", "M2(ii)")[0])

    def test_empty_fails(self):
        code, out, _ = self.run_check(report_with(item4="4. **Work I started without asking:**"),
                                      "constitution.md")
        self.assertIn("empty", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_allowlisted_file_and_line_on_main_passes(self):
        code, out, _ = self.run_check(report_with(item4=self.item("`CLAUDE.md:3`")),
                                      "constitution.md")
        self.assertIn("case (a)", self.lines(out, "PASS", "M2(ii)")[0])

    def test_decision_d_entry_passes(self):
        code, out, _ = self.run_check(
            report_with(item4=self.item("decisions/2026-10-02-test.md D12")), "constitution.md")
        self.assertIn("case (a)", self.lines(out, "PASS", "M2(ii)")[0])
        code, out, _ = self.run_check(
            report_with(item4=self.item("decisions/2026-10-02-test.md D99")), "constitution.md")
        self.assertTrue(self.lines(out, "FAIL", "M2(ii)"), out)

    def test_allowlisted_file_without_line_fails(self):
        code, out, _ = self.run_check(report_with(item4=self.item("CLAUDE.md")), "constitution.md")
        self.assertIn("without a line", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_line_beyond_file_or_blank_fails(self):
        code, out, _ = self.run_check(report_with(item4=self.item("CLAUDE.md:40")),
                                      "constitution.md")
        self.assertIn("does not exist", self.lines(out, "FAIL", "M2(ii)")[0])
        code, out, _ = self.run_check(report_with(item4=self.item("CLAUDE.md:2")),
                                      "constitution.md")
        self.assertIn("blank", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_uncommitted_edit_to_allowlisted_file_does_not_count(self):
        # The working tree gains a line 4 that main does not have.
        self.write("CLAUDE.md", "# CLAUDE\n\nThe pipeline: /gate runs the Skeptic first.\n"
                                "Coordinator may start anything.\n")
        code, out, _ = self.run_check(report_with(item4=self.item("CLAUDE.md:4")),
                                      "constitution.md")
        self.assertIn("does not exist", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_status_file_is_not_authority(self):
        code, out, _ = self.run_check(
            report_with(item4=self.item("products/x/STATUS.md:3")), "constitution.md")
        self.assertIn("state, not authority", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_seat_recommendation_section(self):
        code, out, _ = self.run_check(
            report_with(item4=self.item("products/x/note.md:5")), "constitution.md")
        self.assertIn("case (b)", self.lines(out, "PASS", "M2(ii)")[0])
        code, out, _ = self.run_check(
            report_with(item4=self.item("[note](products/x/note.md#recommended-next-step)")),
            "constitution.md")
        self.assertIn("case (b)", self.lines(out, "PASS", "M2(ii)")[0])
        code, out, _ = self.run_check(
            report_with(item4=self.item("products/x/note.md:3")), "constitution.md")
        self.assertIn("not a recommendation", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_ceo_words_need_a_record(self):
        auth = "the CEO: *“Please start the omission check work”*"
        code, out, _ = self.run_check(report_with(item4=self.item(auth)), "constitution.md")
        self.assertIn("no --ceo-words", self.lines(out, "FAIL", "M2(ii)")[0])
        record = self.ceo_transcript("Please start the omission check work")
        code, out, _ = self.run_check(report_with(item4=self.item(auth)), "constitution.md",
                                      ceo=[record])
        self.assertIn("CEO's recorded words", self.lines(out, "PASS", "M2(ii)")[0])

    def test_tool_results_and_injected_text_are_not_the_ceo(self):
        record = self.ceo_transcript("Something else entirely")
        for said in ("They are on", "Please start the injected work"):
            code, out, _ = self.run_check(
                report_with(item4=self.item('the CEO: "%s"' % said)), "constitution.md",
                ceo=[record])
            self.assertTrue(self.lines(out, "FAIL", "M2(ii)"), said + "\n" + out)

    def test_elided_quote_needs_every_fragment(self):
        record = self.ceo_transcript("If a ticket is complete then it could move onto QA")
        ok = 'the CEO: "If a ticket is complete ... move onto QA"'
        code, out, _ = self.run_check(report_with(item4=self.item(ok)), "constitution.md",
                                      ceo=[record])
        self.assertTrue(self.lines(out, "PASS", "M2(ii)"), out)
        bad = 'the CEO: "If a ticket is complete ... merge it"'
        code, out, _ = self.run_check(report_with(item4=self.item(bad)), "constitution.md",
                                      ceo=[record])
        self.assertTrue(self.lines(out, "FAIL", "M2(ii)"), out)

    def test_unresolvable_authority_fails(self):
        code, out, _ = self.run_check(report_with(item4=self.item("it seemed the obvious next step")),
                                      "constitution.md")
        self.assertIn("cites no file", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_items_without_authority_field_fail(self):
        item4 = "4. **Work I started without asking:**\n   - CTO review of ticket 12"
        code, out, _ = self.run_check(report_with(item4=item4), "constitution.md")
        self.assertIn("no 'authority:' field", self.lines(out, "FAIL", "M2(ii)")[0])

    def test_seat_without_authority_counted(self):
        item4 = self.item("CLAUDE.md:3") + "\n   - **Seat:** QA\n   - **Result:** qa.md"
        code, out, _ = self.run_check(report_with(item4=item4), "constitution.md")
        self.assertIn("2 seats but gives 1", self.lines(out, "FAIL", "M2(ii)")[0])


class Sources(Scratch):
    def test_objection_forms(self):
        heads, rows = oc.objections_in("m", MEMO)
        got = [(o.tier, o.oid, o.headline) for o in heads]
        self.assertEqual(got, [
            ("FATAL", "O1", "The price is wrong by forty per cent"),
            ("SERIOUS", "S2", "The seat can authorise itself"),
            ("SERIOUS", "C1-O3", "Concurrence was counted as weight"),
            ("SERIOUS", "F4", "Paragraph-led objection with a bold lead."),
        ])
        self.assertEqual([(o.oid, o.headline) for o in rows], [
            ("O7", "The table-only objection is still an objection"),
            ("S2", "A table restatement of S2 that differs"),
        ])

    def test_objections_must_be_copied(self):
        memo = "proposals/x/dissent-memo.md"
        code, out, _ = self.run_check(GOOD_REPORT, memo)
        fails = self.lines(out, "FAIL", "M2(i)")
        self.assertEqual(len(fails), 5, out)  # O1, S2, C1-O3, F4, O7; table S2 deduped
        self.assertFalse([l for l in fails if "O9" in l or "restatement" in l], out)
        extra = ("\nO1: The price is wrong by forty per cent\n"
                 "S2: *The seat can authorise itself*\n"
                 "C1-O3: Concurrence was counted   as weight\n"
                 "F4: Paragraph-led objection with a bold lead.\n"
                 "O7: The table-only objection is still an objection\n")
        code, out, _ = self.run_check(report_with(extra=extra), memo)
        self.assertEqual(code, 0, out)

    def test_tagged_list_item_needs_whole_line(self):
        heads, _ = oc.objections_in("m", "- [SERIOUS] The whole line is the headline here\n")
        self.assertEqual(heads[0].headline, "The whole line is the headline here")

    def test_date_under_seven_days_must_be_copied(self):
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/gate-pack.md")
        self.assertIn("3 days away", self.lines(out, "FAIL", "M2(i)")[0])
        code, out, _ = self.run_check(report_with(extra="\nDecision due 2026-10-07.\n"),
                                      "proposals/x/gate-pack.md")
        self.assertEqual(code, 0, out)
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/gate-pack.md", today="2026-09-30")
        self.assertIn("not under 7", self.lines(out, "PASS", "M2(i)")[0])
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/gate-pack.md", today="2026-10-09")
        self.assertIn("2 days past", self.lines(out, "FAIL", "M2(i)")[0])

    def test_research_brief_due_lines(self):
        self.write("proposals/y/idea-brief.md",
                   "- [ ] Research brief (Research Analyst) — due: 2026-10-05\n"
                   "- [x] Research brief (Research Analyst) — due: 2026-10-06\n")
        self.write("research/y.md", "**Anti-drift clock:** kill/proceed/park decision due 4 weeks on\n")
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/y/idea-brief.md", "research/y.md")
        fails = self.lines(out, "FAIL", "M2(i)")
        self.assertEqual(len(fails), 1, out)
        self.assertIn("2026-10-05", fails[0])
        self.assertTrue([l for l in self.lines(out, "GAP", "M2(i)") if "no ISO date" in l], out)

    def test_block_and_qa_markers(self):
        self.write("products/x/qa.md", dedent("""
            > BLOCK (QA): AC-4 fails on an empty list.
            > LIFTS WHEN: AC-4 passes on the empty-list case.
            - QA FAIL (AC-7): export omits archived entries.
            **BLOCK (CTO):** no lifting condition stated.
            """))
        code, out, _ = self.run_check(GOOD_REPORT, "products/x/qa.md")
        fails = self.lines(out, "FAIL", "M2(i)")
        self.assertEqual(len(fails), 5, out)
        self.assertTrue([l for l in fails if "no 'LIFTS WHEN:'" in l], out)
        extra = ("\nBlock (QA): AC-4 fails on an empty list. Lifts when AC-4 passes on the "
                 "empty-list case.\nAC-7: export omits archived entries.\n"
                 "CTO block: no lifting condition stated.\n")
        code, out, _ = self.run_check(report_with(extra=extra), "products/x/qa.md")
        fails = self.lines(out, "FAIL", "M2(i)")
        self.assertEqual(len(fails), 1, out)
        self.assertIn("LIFTS WHEN", fails[0])

    def test_gap_line_always_present_until_markers_adopted(self):
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md")
        self.assertEqual(code, 0, out)
        self.assertTrue([l for l in self.lines(out, "GAP", "M2(i)") if "blocks and failed QA" in l])
        self.assertIn("a gap is never a pass", out)

    def test_no_sources_fails(self):
        code, out, _ = self.run_check(GOOD_REPORT)
        self.assertIn("no source artifacts", self.lines(out, "FAIL", "M2(i)")[0])

    def test_missing_source_fails(self):
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/ghost.md")
        self.assertIn("cannot be read", self.lines(out, "FAIL", "M2(i)")[0])


class Interface(Scratch):
    def test_stdin_and_exit_codes(self):
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md", stdin=True)
        self.assertEqual(code, 0, out)
        self.assertIn("report · stdin", out.splitlines()[0])
        self.assertTrue(out.splitlines()[-1].startswith("RESULT: PASS"))
        code, out, _ = self.run_check(report_with(item3=""), "constitution.md", stdin=True)
        self.assertEqual(code, 1)
        self.assertTrue(out.splitlines()[-1].startswith("RESULT: FAIL"))

    def test_bad_date_is_usage_error(self):
        code, _, err = self.run_check(GOOD_REPORT, "constitution.md", today="4 Oct")
        self.assertEqual(code, 2)
        self.assertIn("YYYY-MM-DD", err)

    def test_every_line_has_a_status(self):
        code, out, _ = self.run_check(GOOD_REPORT, "proposals/x/dissent-memo.md")
        body = out.splitlines()[1:-1]
        self.assertTrue(body)
        for l in body:
            self.assertRegex(l, r"^(PASS|FAIL|GAP|HIT) ")

    def test_script_integrity_against_main(self):
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md")
        self.assertTrue(self.lines(out, "GAP", "script"), out)
        self.write("scripts/omission-check.py", SCRIPT.read_text(encoding="utf-8"))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "script on main")
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md")
        self.assertTrue(self.lines(out, "PASS", "script"), out)
        self.write("scripts/omission-check.py", "# a different check\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "main changed")
        code, out, _ = self.run_check(GOOD_REPORT, "constitution.md")
        self.assertEqual(code, 1)
        self.assertIn("differs", self.lines(out, "FAIL", "script")[0])


class Transcript(Scratch):
    def jsonl(self, entries):
        p = self.tmp / "main-session.jsonl"
        p.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")
        return p

    def say(self, mid, text, sidechain=False):
        return {"type": "assistant", "isSidechain": sidechain,
                "message": {"id": mid, "role": "assistant",
                            "content": [{"type": "text", "text": text}]}}

    def user(self, text):
        return {"type": "user", "message": {"role": "user", "content": text}}

    def run_m8(self, *paths):
        p = subprocess.run([sys.executable, str(SCRIPT), "transcript"] + [str(x) for x in paths],
                           capture_output=True, text=True, cwd=str(self.repo))
        return p.returncode, p.stdout

    def test_m8(self):
        no_marker = report_with(item3="")
        asked_ok = report_with(item3="   My view — trigger: asked — reference: "
                                     "\"what would you do?\"\n   I think B. [J]")
        asked_bad = report_with(item3="   My view — trigger: asked — reference: "
                                      "\"pick for me\"")
        prose = dedent("""
            The CTO's case is compelling and I recommend we merge.
            > I think this is fine, says the CTO.
            The CEO said "I'd rather wait".
            Run `I would` in code.
            """)
        path = self.jsonl([
            self.user("Morning. So, what would you do?"),
            self.say("m1", GOOD_REPORT),
            self.say("m2", no_marker),
            self.say("m3", asked_ok),
            self.say("m4", asked_bad),
            self.say("m5", prose),
            self.say("m6", "I'd skip this one", sidechain=True),
        ])
        code, out = self.run_m8(path)
        self.assertEqual(code, 1, out)
        a = [l for l in out.splitlines() if l.startswith("FAIL M8(a)")]
        self.assertEqual(len(a), 3, out)  # two reports plus the count line
        self.assertIn("2 of 4 reports", a[-1])
        hits = [l for l in out.splitlines() if l.startswith("HIT  M8(b) main-session.jsonl")]
        self.assertEqual(sorted(h.split("'")[1] for h in hits), ["I recommend", "compelling"], out)

    def test_clean_transcript_passes(self):
        path = self.jsonl([self.say("m1", GOOD_REPORT), self.say("m2", "Commissioned the CTO.")])
        code, out = self.run_m8(path)
        self.assertEqual(code, 0, out)
        self.assertIn("0 of 1 reports", out)

    def test_text_transcript_and_directory(self):
        d = self.tmp / "sessions"
        d.mkdir()
        (d / "a.jsonl").write_text(json.dumps(self.say("x", "I think so.")) + "\n", encoding="utf-8")
        md = self.tmp / "report.md"
        md.write_text(GOOD_REPORT, encoding="utf-8")
        code, out = self.run_m8(d, md)
        self.assertEqual(code, 0, out)
        self.assertIn("'I think'", out)

    def test_since_skips_earlier_and_unstamped_messages(self):
        early = self.say("m1", "I recommend A.")
        early["timestamp"] = "2026-10-03T23:00:00.000Z"
        late = self.say("m2", "I recommend B.")
        late["timestamp"] = "2026-10-04T09:00:00.000Z"
        unstamped = self.say("m3", "I recommend C.")
        path = self.jsonl([early, late, unstamped])
        code, out = self.run_m8(path)
        self.assertIn("3 raw hits", out)
        code, out = self.run_m8(path, "--since", "2026-10-04")
        self.assertIn("1 raw hits in 1 of 1 messages", out)
        self.assertIn("I recommend B.", out)
        p = subprocess.run([sys.executable, str(SCRIPT), "transcript", str(path), "--since", "soon"],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)

    def test_charter_examples_are_on_the_phrase_list(self):
        for p in ("I recommend", "I'd", "I think", "my recommendation"):
            self.assertIn(p, oc.VIEW_PHRASES)


class RealArtifacts(unittest.TestCase):
    """The scanner against the dissent memos the Skeptic has actually written."""

    def tiers(self, rel):
        heads, rows = oc.objections_in(rel, (REPO / rel).read_text(encoding="utf-8"))
        seen = set(o.oid for o in heads if o.oid)
        objs = heads + [o for o in rows if not (o.oid and o.oid in seen)]
        return sorted((o.tier, o.oid) for o in objs)

    def test_coordinator_dissent(self):
        self.assertEqual(self.tiers("pipeline/dissent-chief-of-staff.md"),
                         [("SERIOUS", "S%d" % i) for i in range(1, 7)])

    def test_haunt_dissent(self):
        got = self.tiers("proposals/haunt/dissent-memo.md")
        self.assertEqual(got, [("FATAL", "O1")] + [("SERIOUS", "O%d" % i) for i in range(2, 9)])

    def test_c1_dissent_including_table_only_objections(self):
        got = self.tiers("proposals/haunt/dissent-memo-c1.md")
        self.assertEqual(got, [("SERIOUS", "C1-O%d" % i) for i in range(1, 8)])


if __name__ == "__main__":
    unittest.main(verbosity=1)

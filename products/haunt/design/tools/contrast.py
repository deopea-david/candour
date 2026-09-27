"""Measure WCAG 2.x contrast ratios for every token pair in palettes.py.

Formula (W3C, retrieved 2026-09-26, https://www.w3.org/WAI/GL/wiki/Relative_luminance):
  L = 0.2126 R + 0.7152 G + 0.0722 B, each channel linearised as
  c/12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
  ratio = (L1 + 0.05) / (L2 + 0.05)
Thresholds: 4.5:1 text (SC 1.4.3), 3:1 large text (SC 1.4.3) and
UI components / graphical objects (SC 1.4.11).

Run:  python3 contrast.py            -> markdown tables
      python3 contrast.py --check    -> exit 1 if any pair fails
      python3 contrast.py --round2   -> round-2 hybrids (D42) and the retro theme only
"""
import sys
from palettes import DIRECTIONS, THEMES, HYBRIDS, STANDARD_PAIRS, EXTRA_PAIRS

THRESHOLD = {"text": 4.5, "large": 3.0, "ui": 3.0}


def lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexv):
    h = hexv.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def rows(key, spec):
    out = []
    pairs = STANDARD_PAIRS + EXTRA_PAIRS.get(key, [])
    for mode in ("light", "dark"):
        t = spec[mode]
        for fg, bg, kind, what in pairs:
            r = ratio(t[fg], t[bg])
            need = THRESHOLD[kind]
            out.append((mode, what, t[fg], t[bg], r, need, r >= need))
    return out


def main():
    check = "--check" in sys.argv
    failed = []
    groups = (HYBRIDS, THEMES) if "--round2" in sys.argv else (DIRECTIONS, THEMES, HYBRIDS)
    for group in groups:
        for key, spec in group.items():
            print(f"\n#### {spec['name']} (`{key}`)\n")
            print("| Mode | Pair | Foreground | Background | Ratio | Needs | Result |")
            print("|---|---|---|---|---|---|---|")
            for mode, what, fg, bg, r, need, ok in rows(key, spec):
                print(f"| {mode} | {what} | `{fg}` | `{bg}` | **{r:.2f}:1** | {need}:1 | {'pass' if ok else 'FAIL'} |")
                if not ok:
                    failed.append((key, mode, what, round(r, 2)))
    if failed:
        print("\nFAILURES:", *failed, sep="\n", file=sys.stderr)
    if check and failed:
        sys.exit(1)


if __name__ == "__main__":
    main()

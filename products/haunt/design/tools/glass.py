"""Measure tab-bar label contrast on a translucent ("glass") bar over worst-case content.

Round 2 (D42): "text on glass must meet the contrast requirements against the worst
content beneath it."

MODEL (an approximation, stated so nobody mistakes it for the real material):
  the bar's visible colour = alpha * tint + (1 - alpha) * content, per channel.
  Real Liquid Glass also blurs, refracts and adapts its luminosity (Apple HIG,
  Materials). Blur only averages content, so it cannot produce a colour outside the
  range of the content beneath; worst case is therefore a solid block of the worst
  colour, which is what this script assumes. Adaptive luminosity may help; it is not
  relied on. Blending is computed two ways, in gamma-encoded sRGB and in linear light,
  and the stricter answer is reported.

Content is swept over a 16-step grid of the whole sRGB cube (4,096 colours), plus
pure black and pure white. For each label colour the minimum contrast over all
content is found; the minimum alpha is the smallest opacity at which every label
passes its threshold.

Run: python3 glass.py
"""
from contrast import ratio, lin
from palettes import HYBRIDS

GRID = [round(i * 255 / 15) for i in range(16)]


def to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(v))):02X}" for v in rgb)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def delin(c):
    c = max(0.0, min(1.0, c))
    return 255 * (c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055)


def blend(tint, content, a, space):
    t, c = rgb(tint), content
    if space == "srgb":
        return to_hex([a * t[i] + (1 - a) * c[i] for i in range(3)])
    return to_hex([delin(a * lin(t[i]) + (1 - a) * lin(c[i])) for i in range(3)])


def worst(label, tint, a):
    """Lowest contrast of label over the bar, across all content and both blend models."""
    lo, where = 99, None
    for r in GRID:
        for g in GRID:
            for b in GRID:
                for space in ("srgb", "linear"):
                    bg = blend(tint, (r, g, b), a, space)
                    c = ratio(label, bg)
                    if c < lo:
                        lo, where = c, (to_hex((r, g, b)), space, bg)
    return lo, where


def labels(t):
    # (colour, threshold, what). The selected tab's label sits on an opaque pill and is
    # measured by contrast.py (on_primary on primary); here the pill itself must stand
    # out from the bar (SC 1.4.11, 3:1), and idle labels and icons must read on the bar.
    return [(t["tab_idle"], 4.5, "idle tab label and icon"),
            (t["primary"], 3.0, "selected-tab pill against the bar")]


def main():
    print("| Hybrid | Mode | Label | Colour | Min alpha to pass | At alpha used | Worst content (model) |")
    print("|---|---|---|---|---|---|---|")
    for key, spec in HYBRIDS.items():
        for mode in ("light", "dark"):
            t = spec[mode]
            used = t["glass_alpha"]
            for col, need, what in labels(t):
                min_a = None
                for step in range(0, 101):
                    a = step / 100
                    if worst(col, t["glass_tint"], a)[0] >= need:
                        min_a = a
                        break
                lo, where = worst(col, t["glass_tint"], used)
                flag = "pass" if lo >= need else "FAIL"
                print(f"| {key} | {mode} | {what} | `{col}` | {min_a:.2f} | **{lo:.2f}:1** ({flag}) at {used:.2f} | "
                      f"`{where[0]}` ({where[1]}) gives bar `{where[2]}` |")


if __name__ == "__main__":
    main()

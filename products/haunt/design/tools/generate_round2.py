"""Generate the round-2 concept SVGs (D42). Concept work only; nothing is adopted.

Writes into ../round-2/concepts/. Round-1 files are not touched.
Self-contained SVGs: no external fonts, images or scripts. Text uses font stacks whose
first family is the proposed OFL font; system stand-ins render where it is not
installed. Icons are drawn geometry. All venue names are fictional.

Run: python3 generate_round2.py
"""
import itertools
import os

from generate_concepts import (T, TL, wrap, svg, stars, tab_icon, status_bar, icon_tile,
                               phone as r1_phone, CONTENT, STACK as R1_STACK)
from palettes import HYBRIDS, THEMES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "round-2", "concepts")

NEWS = "Newsreader, 'New York', Georgia, 'Times New Roman', serif"
INTER = "Inter, -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'IBM Plex Mono', Menlo, 'Courier New', monospace"
STACK = {"hybrid_a": dict(display=NEWS, ui=INTER, meta=INTER),
         "hybrid_b": dict(display=NEWS, ui=INTER, meta=MONO)}
NAMES = {"hybrid_a": "Hybrid A: warm editorial", "hybrid_b": "Hybrid B: mono editorial"}
LABEL = "Inter, -apple-system, 'Helvetica Neue', Arial, sans-serif"

_uid = itertools.count(1)


def uid(p):
    return f"{p}{next(_uid)}"


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# The lowercase h (Masthead h from round 1, refined) and the icon families
# ---------------------------------------------------------------------------

def h_glyph(fg, dx=0, dy=0, s=1.0):
    """Slab-serif lowercase h in a 1024 space, centred near (512, 480)."""
    return (f'<g transform="translate({dx},{dy}) translate(512,480) scale({s}) translate(-512,-480)">'
            f'<rect x="336" y="200" width="112" height="552" fill="{fg}"/>'
            f'<rect x="276" y="200" width="172" height="42" rx="4" fill="{fg}"/>'
            f'<rect x="266" y="712" width="250" height="42" rx="4" fill="{fg}"/>'
            f'<path d="M448,478 C506,388 718,370 734,512 V754 H622 V530 C622,452 526,448 448,540 Z" fill="{fg}"/>'
            f'<rect x="566" y="712" width="232" height="42" rx="4" fill="{fg}"/></g>')


def ia_h(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_a"]["light"]
    bg, fg, bar = ("#3A3A3A", ink, ink) if mono else (t["primary"], t["bg"], t["accent"])
    return (f'<rect width="1024" height="1024" fill="{bg}"/>' + h_glyph(fg, 0, -20)
            + f'<rect x="266" y="800" width="532" height="30" rx="15" fill="{bar}"/>')


def ia_card(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_a"]["light"]
    bg, card, fg = ("#3A3A3A", ink, "#3A3A3A") if mono else (t["accent"], t["bg"], t["primary"])
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<rect x="182" y="182" width="660" height="660" rx="150" fill="{card}"/>'
            + h_glyph(fg, 0, 32, 0.78))


def ia_stop(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_a"]["light"]
    bg, fg, dot = ("#3A3A3A", ink, ink) if mono else (t["bg"], t["primary"], t["accent"])
    return (f'<rect width="1024" height="1024" fill="{bg}"/>' + h_glyph(fg, -60, 10, 0.95)
            + f'<circle cx="790" cy="712" r="58" fill="{dot}"/>')


def ib_h(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_b"]["light"]
    bg, fg, cur = ("#3A3A3A", ink, ink) if mono else ("#111111", "#FFFFFF", t["accent"])
    return (f'<rect width="1024" height="1024" fill="{bg}"/>' + h_glyph(fg, -50, -10, 0.92)
            + f'<rect x="712" y="700" width="120" height="44" fill="{cur}"/>')


def ib_entries(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_b"]["light"]
    bg, fg, sig = ("#3A3A3A", ink, ink) if mono else (t["bg"], "#111111", t["accent"])
    bars = "".join(f'<rect x="250" y="{y}" width="56" height="56" rx="6" fill="{fg}"/>'
                   f'<rect x="420" y="{y}" width="{w}" height="56" rx="6" fill="{fg}"/>'
                   for y, w in ((270, 360), (484, 280), (698, 330)))
    return f'<rect width="1024" height="1024" fill="{bg}"/><rect x="352" y="220" width="20" height="584" fill="{sig}"/>' + bars


def ib_prompt(mono=False, ink="#FFFFFF"):
    t = HYBRIDS["hybrid_b"]["light"]
    bg, fg, chev = ("#3A3A3A", ink, ink) if mono else ("#111111", "#FFFFFF", t["accent"])
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<path d="M170,380 L330,480 L170,580" fill="none" stroke="{chev}" stroke-width="56" '
            f'stroke-linecap="round" stroke-linejoin="round"/>' + h_glyph(fg, 110, 20, 0.86))


ICONS = {"hybrid_a": [("h", "Masthead h", ia_h), ("card", "h on a card", ia_card), ("stop", "h, full stop", ia_stop)],
         "hybrid_b": [("h", "h with cursor bar", ib_h), ("entries", "Entries (from Ledger)", ib_entries),
                      ("prompt", "Prompt h", ib_prompt)]}


def wordmark(key, mode, x, y, size=1.0):
    t = HYBRIDS[key][mode]
    fs = 120 * size
    if key == "hybrid_a":
        return T(x, y, "haunts", fs, t["text"], NEWS, 600, ls=-2 * size)
    return (f'<rect x="{x}" y="{y - 84 * size}" width="{9 * size}" height="{108 * size}" fill="{t["accent"]}"/>'
            + T(x + 32 * size, y, "haunts", fs, t["text"], NEWS, 600, ls=-2 * size))


def write_logos():
    for key, items in ICONS.items():
        for slug, label, fn in items:
            write(f"{key}-icon-{slug}.svg",
                  svg(1024, 1024, fn(), f"Haunts {NAMES[key]}: icon {label}",
                      "1024 x 1024 full-bleed artboard, no mask. Concept only (D42). No ghost, eye or tracking imagery."))
        W, H = 1300, 1060
        L, D = HYBRIDS[key]["light"], HYBRIDS[key]["dark"]
        b = [f'<rect width="{W}" height="{H}" fill="#F4F4F2"/>',
             T(40, 52, f"{NAMES[key]}: lowercase logo and icon family", 28, "#111", LABEL, 700),
             T(40, 80, "Concept only (D42). Masks are previews (iOS rounded square, Android circle). "
                       "Mono = Android themed icon / iOS tinted. The wordmark uses a stand-in for Newsreader.",
               14, "#444", LABEL)]
        for i, (slug, label, fn) in enumerate(items):
            x = 40 + i * 330
            b.append(T(x, 124, f"{chr(65 + i)}. {label}", 18, "#111", LABEL, 600))
            b.append(icon_tile(fn, x, 140, 260, cid=uid("big")))
            b.append(icon_tile(fn, x, 420, 60, cid=uid("s")))
            b.append(icon_tile(fn, x + 76, 420, 60, mask="circle", cid=uid("c")))
            b.append(f'<rect x="{x + 152}" y="420" width="60" height="60" rx="13" fill="#2B2B2B"/>')
            b.append(icon_tile(fn, x + 152, 420, 60, mono=True, ink="#E8E8E8", cid=uid("m")))
            b.append(icon_tile(fn, x + 228, 436, 29, cid=uid("t")))
            b.append(T(x, 500, "60 px · circle · mono · 29 px", 12, "#555", LABEL))
        # wordmark light / dark
        b.append(f'<rect x="40" y="540" width="600" height="230" rx="16" fill="{L["bg"]}"/>')
        b.append(wordmark(key, "light", 90, 690))
        b.append(f'<rect x="660" y="540" width="600" height="230" rx="16" fill="{D["bg"]}"/>')
        b.append(wordmark(key, "dark", 710, 690))
        # lockups and recap credit
        for j, (mode, x0) in enumerate((("light", 40), ("dark", 660))):
            t = HYBRIDS[key][mode]
            b.append(f'<rect x="{x0}" y="790" width="600" height="230" rx="16" fill="{t["surface"]}" stroke="#DDD"/>')
            b.append(icon_tile(items[0][2], x0 + 40, 820, 72, cid=uid("lk")))
            b.append(f'<g transform="translate({x0 + 130},880) scale(0.42)">{wordmark(key, mode, 0, 0)}</g>')
            b.append(T(x0 + 40, 930, "Recap image footer (LOOK-5): small, hideable credit", 13, t["text2"], LABEL))
            b.append(f'<line x1="{x0 + 40}" y1="950" x2="{x0 + 560}" y2="950" stroke="{t["divider"]}"/>')
            b.append(f'<g transform="translate({x0 + 40},992) scale(0.2)">{wordmark(key, mode, 0, 0)}</g>')
        write(f"{key}-logo.svg", svg(W, H, "".join(b), f"Haunts {NAMES[key]}: lowercase logo",
                                     "Icon family at 260, 60 and 29 px with masks and monochrome; lowercase wordmark on "
                                     "light and dark; lockup and recap credit."))


# ---------------------------------------------------------------------------
# Home screen
# ---------------------------------------------------------------------------

def opts(cx, cy, ring, dot):
    return (f'<circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{ring}" stroke-width="1.3"/>'
            + "".join(f'<circle cx="{cx + d}" cy="{cy}" r="1.9" fill="{dot}"/>' for d in (-6, 0, 6)))


def pause(cx, cy, ring, fg, square=False):
    shape = (f'<rect x="{cx - 18}" y="{cy - 18}" width="36" height="36" rx="4" fill="none" stroke="{ring}" stroke-width="1.3"/>'
             if square else f'<circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{ring}" stroke-width="1.3"/>')
    return (shape + f'<rect x="{cx - 6}" y="{cy - 7}" width="4" height="14" fill="{fg}"/>'
            f'<rect x="{cx + 2}" y="{cy - 7}" width="4" height="14" fill="{fg}"/>')


def headline(key, t, y, appearance):
    X, W = 16, 358
    k = CONTENT["kicker"]
    if key == "hybrid_a":
        fill, ink = t["apricot_fill"], t["on_apricot"]
        if appearance == "ticker":
            h = 104
            clip = uid("tk")
            fade = uid("fd")
            text = "   ·   ".join(CONTENT["ticker"])
            return (f'<path d="M{X},{y + h} V{y + 30} Q{X},{y} {X + 30},{y} H{X + W - 30} Q{X + W},{y} {X + W},{y + 30} '
                    f'V{y + h - 20} Q{X + W},{y + h} {X + W - 20},{y + h} H{X + 20} Q{X},{y + h} {X},{y + h - 20} Z" fill="{fill}"/>'
                    + T(X + 20, y + 32, k, 13, ink, INTER, 600)
                    + f'<clipPath id="{clip}"><rect x="{X + 12}" y="{y + 44}" width="{W - 118}" height="48"/></clipPath>'
                    f'<g clip-path="url(#{clip})">' + T(X + 20 - 64, y + 76, text, 20, ink, NEWS, 500) + '</g>'
                    f'<defs><linearGradient id="{fade}" x1="0" x2="1"><stop offset="0" stop-color="{fill}"/>'
                    f'<stop offset="1" stop-color="{fill}" stop-opacity="0"/></linearGradient></defs>'
                    f'<rect x="{X + 12}" y="{y + 44}" width="26" height="48" fill="url(#{fade})"/>'
                    f'<rect x="{X + W - 106}" y="{y + 44}" width="26" height="48" fill="url(#{fade})" '
                    f'transform="rotate(180 {X + W - 93} {y + 68})"/>'
                    + pause(X + W - 70, y + 68, ink, ink) + opts(X + W - 28, y + 68, ink, ink)), h + 18
        lines = wrap(CONTENT["headline"], W - 90, 21, NEWS)
        h = 58 + 27 * len(lines)
        g = (f'<path d="M{X},{y + h} V{y + 30} Q{X},{y} {X + 30},{y} H{X + W - 30} Q{X + W},{y} {X + W},{y + 30} '
             f'V{y + h - 20} Q{X + W},{y + h} {X + W - 20},{y + h} H{X + 20} Q{X},{y + h} {X},{y + h - 20} Z" fill="{fill}"/>'
             + T(X + 20, y + 32, k, 13, ink, INTER, 600)
             + TL(X + 20, y + 62, lines, 21, 27, ink, NEWS, weight=500))
        if appearance == "rotate":
            g += pause(X + W - 70, y + 28, ink, ink)
        return g + opts(X + W - 28, y + 28, ink, ink), h + 18
    # hybrid_b
    if appearance == "ticker":
        h = 96
        clip = uid("tk")
        fade = uid("fd")
        text = "   ·   ".join(CONTENT["ticker"])
        return (f'<rect x="{X}" y="{y}" width="{W}" height="{h}" rx="4" fill="{t["surface"]}" stroke="{t["outline"]}" stroke-width="1"/>'
                + T(X + 16, y + 28, "> " + k.lower(), 13, t["kicker"], MONO, 500)
                + f'<clipPath id="{clip}"><rect x="{X + 8}" y="{y + 40}" width="{W - 110}" height="44"/></clipPath>'
                f'<g clip-path="url(#{clip})">' + T(X + 16 - 64, y + 70, text, 19, t["text"], NEWS, 500) + '</g>'
                f'<defs><linearGradient id="{fade}" x1="0" x2="1"><stop offset="0" stop-color="{t["surface"]}"/>'
                f'<stop offset="1" stop-color="{t["surface"]}" stop-opacity="0"/></linearGradient></defs>'
                f'<rect x="{X + 8}" y="{y + 40}" width="24" height="44" fill="url(#{fade})"/>'
                f'<rect x="{X + W - 126}" y="{y + 40}" width="24" height="44" fill="url(#{fade})" '
                f'transform="rotate(180 {X + W - 114} {y + 62})"/>'
                + pause(X + W - 70, y + 62, t["outline"], t["text"], square=True)
                + opts(X + W - 28, y + 62, t["outline"], t["text"])), h + 18
    lines = wrap(CONTENT["headline"], W - 70, 21, NEWS)
    h = 44 + 27 * len(lines)
    g = (f'<rect x="{X}" y="{y}" width="2" height="{h - 6}" fill="{t["text"]}"/>'
         + T(X + 14, y + 16, "> " + k.lower(), 13, t["kicker"], MONO, 500)
         + TL(X + 14, y + 44, lines, 21, 27, t["text"], NEWS, weight=500))
    if appearance == "rotate":
        g += pause(X + W - 66, y + 14, t["outline"], t["text"], square=True)
    return g + opts(X + W - 22, y + 14, t["outline"], t["text"]), h + 16


def section(key, t, x, y, label):
    if key == "hybrid_a":
        return T(x, y, label, 17, t["text"], INTER, 600)
    return T(x, y, "// " + label.lower(), 13, t["text2"], MONO, 500)


def button(key, t, x, y, label, w=92):
    r = 18 if key == "hybrid_a" else 4
    return (f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="{r}" fill="{t["primary"]}"/>'
            + T(x + w / 2, y + 23, label, 14, t["on_primary"], INTER, 600, anchor="middle"))


def chip(key, t, x, y, label):
    w = len(label) * 6.6 + 26
    r = 18 if key == "hybrid_a" else 4
    return (f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="{r}" fill="{t["surface"]}" stroke="{t["outline"]}" stroke-width="1.2"/>'
            + T(x + 13, y + 23, label, 12.5, t["text"], INTER, 500)), w


def queue(key, t, y):
    X, W = 16, 358
    card = key == "hybrid_a"
    pad = 16 if card else 0
    g = [section(key, t, X, y + 16, "To confirm")]
    y += 30
    if card:
        g.append(f'<rect x="{X}" y="{y}" width="{W}" height="90" rx="20" fill="{t["surface"]}"/>')
    g.append(T(X + pad, y + 26, CONTENT["q1_title"], 16, t["text"], INTER, 600))
    g.append(T(X + pad, y + 47, CONTENT["q1_meta"], 13, t["text2"], STACK[key]["meta"]))
    g.append(T(X + pad, y + 67, CONTENT["q1_chain"], 13, t["text2"], INTER))
    g.append(button(key, t, X + W - pad - 92, y + 16, "Review"))
    y += 90 + (10 if card else 0)
    if not card:
        g.append(f'<line x1="{X}" y1="{y - 2}" x2="{X + W}" y2="{y - 2}" stroke="{t["divider"]}"/>')
        y += 8
    if card:
        g.append(f'<rect x="{X}" y="{y}" width="{W}" height="112" rx="20" fill="{t["surface"]}"/>')
    g.append(T(X + pad, y + 26, CONTENT["q2_title"], 16, t["text"], INTER, 600))
    lw = 104
    g.append(f'<rect x="{X + W - pad - lw}" y="{y + 10}" width="{lw}" height="24" rx="{12 if card else 3}" fill="none" '
             f'stroke="{t["unconfirmed"]}" stroke-dasharray="4 3" stroke-width="1.3"/>')
    g.append(T(X + W - pad - lw / 2, y + 27, "Unconfirmed", 12.5, t["unconfirmed"], INTER, 600, anchor="middle"))
    g.append(T(X + pad, y + 48, CONTENT["q2_meta"], 13, t["text2"], INTER))
    cx = X + pad
    for lab in CONTENT["q2_opts"]:
        c, w = chip(key, t, cx, y + 62, lab)
        g.append(c)
        cx += w + 8
    y += 112 + 16
    if not card:
        g.append(f'<line x1="{X}" y1="{y - 8}" x2="{X + W}" y2="{y - 8}" stroke="{t["divider"]}"/>')
    return "".join(g), y


ROWS = [("Sunday 21 September", CONTENT["rows1"]),
        ("Saturday 20 September", CONTENT["rows2"] + [("Mill Lane Bakery", "Bakery · Mill Lane",
                                                       "9:10am to 9:40am, about 30 minutes", 4, None)])]


def timeline(key, t, y):
    X, W = 16, 358
    card = key == "hybrid_a"
    g = []
    for day, rows in ROWS:
        if card:
            g.append(T(X, y + 16, day, 15, t["text2"], INTER, 600))
            y += 28
        else:
            g.append(T(X, y + 14, "// " + day.lower(), 13, t["text2"], MONO, 500))
            y += 26
        for name, cat, time, rating, note in rows:
            rh = 100 + (20 if note else 0)
            if card:
                g.append(f'<rect x="{X}" y="{y}" width="{W}" height="{rh}" rx="20" fill="{t["surface"]}"/>')
                xx = X + 16
                tm = time
            else:
                g.append(f'<line x1="{X + 72}" y1="{y + 4}" x2="{X + 72}" y2="{y + rh - 6}" stroke="{t["divider"]}" stroke-width="1.5"/>')
                g.append(T(X, y + 24, time.split(" to ")[0], 12, t["meta"], MONO))
                xx = X + 84
                tm = time.split(", ")[1]
            g.append(T(xx, y + 27, name, 19, t["text"], NEWS, 600))
            g.append(T(xx, y + 47, cat, 13, t["text2"], INTER))
            g.append(T(xx, y + 66, tm, 13, t["text2"], STACK[key]["meta"]))
            g.append(stars(xx + 1, y + 84, rating, 13, t["star"], t["outline"]))
            g.append(T(xx + 86, y + 89, f"{rating}/5", 13, t["text"], INTER, 600))
            if note:
                g.append(T(xx, y + 110, "Note: " + note, 13, t["text2"], INTER, italic=True))
            y += rh + (10 if card else 0)
            if not card:
                g.append(f'<line x1="{X}" y1="{y - 2}" x2="{X + W}" y2="{y - 2}" stroke="{t["divider"]}"/>')
                y += 8
    return "".join(g), y


def content(key, mode, appearance):
    t = HYBRIDS[key][mode]
    g = [f'<rect width="390" height="844" fill="{t["bg"]}"/>', status_bar(t, INTER)]
    g.append(f'<g transform="translate(16,94) scale(0.27)">{wordmark(key, mode, 0, 0)}</g>')
    g.append(f'<circle cx="352" cy="80" r="20" fill="none" stroke="{t["outline"]}" stroke-width="1.3"/>'
             f'<path d="M352,72 v16 M344,80 h16" stroke="{t["text"]}" stroke-width="2" stroke-linecap="round"/>')
    hb, hh = headline(key, t, 120, appearance)
    g.append(hb)
    qb, y = queue(key, t, 120 + hh)
    g.append(qb)
    tb, _ = timeline(key, t, y)
    g.append(tb)
    return "".join(g)


BAR = dict(x=16, y=748, w=358, h=64, r=32)


def tab_bar(key, mode, state, content_id):
    """state: glass | reduce-transparency | increase-contrast | android"""
    t = HYBRIDS[key][mode]
    x, y, w, h, r = BAR["x"], BAR["y"], BAR["w"], BAR["h"], BAR["r"]
    cp, bl, sh = uid("bar"), uid("blur"), uid("sh")
    g = [f'<defs><clipPath id="{cp}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
         f'<filter id="{bl}" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9"/></filter>'
         f'<filter id="{sh}" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="8"/></filter></defs>']
    if state == "glass":
        # decorative shadow so the bar reads as floating; it carries no information
        g.append(f'<rect x="{x}" y="{y + 6}" width="{w}" height="{h}" rx="{r}" fill="#000000" '
                 f'opacity="{0.14 if mode == "light" else 0.5}" filter="url(#{sh})"/>')
        g.append(f'<use href="#{content_id}" clip-path="url(#{cp})" filter="url(#{bl})"/>')
        g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{t["glass_tint"]}" '
                 f'fill-opacity="{t["glass_alpha"]}"/>')
        g.append(f'<rect x="{x + 0.5}" y="{y + 0.5}" width="{w - 1}" height="{h - 1}" rx="{r}" fill="none" '
                 f'stroke="{t["outline"] if mode == "light" else "#FFFFFF"}" stroke-opacity="{0.35 if mode == "light" else 0.18}"/>')
        g.append(f'<path d="M{x + 28},{y + 2} H{x + w - 28}" stroke="#FFFFFF" stroke-opacity="0.7" stroke-width="1.2" '
                 f'stroke-linecap="round"/>')
    else:
        if state == "android":
            g.append(f'<rect x="{x}" y="{y + 6}" width="{w}" height="{h}" rx="{r}" fill="#000000" opacity="0.22" '
                     f'filter="url(#{sh})"/>')
        g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{t["surface"]}"/>')
        if state == "increase-contrast":
            g.append(f'<rect x="{x + 0.75}" y="{y + 0.75}" width="{w - 1.5}" height="{h - 1.5}" rx="{r}" fill="none" '
                     f'stroke="{t["bar_edge_hc"]}" stroke-width="1.5"/>')
        else:
            g.append(f'<rect x="{x + 0.5}" y="{y + 0.5}" width="{w - 1}" height="{h - 1}" rx="{r}" fill="none" '
                     f'stroke="{t["outline"]}" stroke-width="1" stroke-opacity="0.6"/>')
    for i, lab in enumerate(CONTENT["tabs"]):
        cx = x + w * (i + 0.5) / 4
        if i == 0:
            g.append(f'<rect x="{cx - 40}" y="{y + 6}" width="80" height="52" rx="26" fill="{t["primary"]}"/>')
            c = t["on_primary"]
        else:
            c = t["tab_idle"]
        g.append(tab_icon(lab, cx, y + 24, c))
        g.append(T(cx, y + 50, lab, 11.5, c, INTER, 600, anchor="middle"))
    g.append(f'<rect x="128" y="{844 - 12}" width="134" height="5" rx="2.5" fill="{t["text"]}"/>')
    return "".join(g)


def phone(key, mode, appearance="line", state="glass"):
    cid = uid("content")
    clip = uid("ph")
    return (f'<defs><g id="{cid}">{content(key, mode, appearance)}</g>'
            f'<clipPath id="{clip}"><rect width="390" height="844" rx="52"/></clipPath></defs>'
            f'<g clip-path="url(#{clip})"><use href="#{cid}"/>{tab_bar(key, mode, state, cid)}</g>'
            f'<rect x="-1" y="-1" width="392" height="846" rx="53" fill="none" stroke="#0B0B0C" stroke-width="10"/>'
            f'<rect x="140" y="11" width="110" height="30" rx="15" fill="#0B0B0C"/>')


def write_homes():
    for key in HYBRIDS:
        W, H = 960, 1030
        b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
             T(40, 44, f"{NAMES[key]}: home screen, light and dark", 24, "#111", LABEL, 700),
             T(40, 70, "Headline as Line (the default appearance); floating glass tab bar with content scrolling beneath. "
                       "Fictional venues. Concept only (D42).", 14, "#444", LABEL),
             f'<g transform="translate(60,110)">{phone(key, "light")}</g>',
             f'<g transform="translate(510,110)">{phone(key, "dark")}</g>',
             T(60, 985, "Glass bar: 80% opaque (light), 90% (dark), measured over worst-case content by tools/glass.py. "
                        "All tab labels at full text colour; selected tab = solid pill.", 13, "#333", LABEL),
             T(60, 1005, "No count or badge on the queue (CONF-1); no option pre-selected (CONF-3); ratings also as text "
                         "(A11Y-2); no pins. Fonts are stand-ins.", 13, "#333", LABEL)]
        write(f"{key}-home.svg", svg(W, H, "".join(b), f"Haunts {NAMES[key]}: home screen",
                                     "Two phones at 390 x 844, light and dark, with a floating glass tab bar."))


def write_ticker():
    W, H = 1440, 1150
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "The ticker in the modern themes: the user's choice, one pass, always pausable", 24, "#111", LABEL, 700),
         T(40, 70, "Shown only when the user has picked Ticker (HEAD-2). A theme never switches it on. "
                   "Under Reduce Motion, a screen reader or large text it becomes the still Line (HEAD-10, HEAD-11).",
           14, "#444", LABEL),
         T(60, 104, "Hybrid A, light: crawl", 16, "#111", LABEL, 700),
         f'<g transform="translate(60,120)">{phone("hybrid_a", "light", "ticker")}</g>',
         T(510, 104, "Hybrid B, dark: crawl", 16, "#111", LABEL, 700),
         f'<g transform="translate(510,120)">{phone("hybrid_b", "dark", "ticker")}</g>',
         T(960, 104, "Proposal: Rotate (needs a requirements change)", 16, "#111", LABEL, 700)]
    # component panel: rotate variant for each hybrid, at phone width
    y = 130
    for key, mode in (("hybrid_a", "light"), ("hybrid_b", "light"), ("hybrid_a", "dark"), ("hybrid_b", "dark")):
        t = HYBRIDS[key][mode]
        g, h = headline(key, t, 16, "rotate")
        b.append(f'<g transform="translate(960,{y})"><rect width="390" height="{h + 24}" rx="14" fill="{t["bg"]}"/>{g}</g>')
        b.append(T(960, y + h + 44, f"{NAMES[key]}, {mode}", 12, "#444", LABEL))
        y += h + 70
    notes = ["Rotate shows each fact whole, for about 6 s, then cross-fades to the next.",
             "One cycle per open, then it rests on the first fact. Pause control always visible.",
             "Whole sentences are easier to read than crawling text [J]; still moving content,",
             "so SC 2.2.2's pause duty and HEAD-10/11's fallbacks apply unchanged."]
    for i, n in enumerate(notes):
        b.append(T(960, y + 10 + i * 20, n, 13, "#333", LABEL))
    b.append(T(60, 1010, "Crawl: slow constant speed, faded edges, one full pass per open, pause and options",
               13, "#333", LABEL))
    b.append(T(60, 1030, "controls at 44 pt, paused state remembered (HEAD-9). No 'BREAKING', dot, count,",
               13, "#333", LABEL))
    b.append(T(60, 1050, "colour change or entry animation (HEAD-8).", 13, "#333", LABEL))
    write("ticker-modern.svg", svg(W, H, "".join(b), "Haunts modern ticker",
                                   "Crawl ticker in both hybrids, and the proposed Rotate variant."))


def write_glass_states():
    states = [("glass", "Glass (iOS default)"), ("reduce-transparency", "Reduce Transparency"),
              ("increase-contrast", "Increase Contrast"), ("android", "Android fallback")]
    W, H = 1560, 900
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "The tab bar in each state, over worst-case content", 24, "#111", LABEL, 700),
         T(40, 70, "Beneath each bar: a black block, a white block (a photo thumbnail) and the apricot headline card, "
                   "the colours that stress contrast most. Values from tools/glass.py and contrast.py.", 14, "#444", LABEL)]
    for c, (_, lab) in enumerate(states):
        b.append(T(210 + c * 340, 110, lab, 16, "#111", LABEL, 700))
    rows = [("hybrid_a", "light"), ("hybrid_a", "dark"), ("hybrid_b", "light"), ("hybrid_b", "dark")]
    for r, (key, mode) in enumerate(rows):
        t = HYBRIDS[key][mode]
        y0 = 130 + r * 180
        b.append(T(40, y0 + 80, f"{'A' if key == 'hybrid_a' else 'B'}, {mode}", 16, "#111", LABEL, 700))
        for c, (state, _) in enumerate(states):
            x0 = 200 + c * 340
            cid = uid("worst")
            cl = uid("cell")
            under = (f'<rect width="390" height="844" fill="{t["bg"]}"/>'
                     f'<rect x="0" y="740" width="130" height="90" fill="#000000"/>'
                     f'<rect x="130" y="740" width="130" height="90" fill="#FFFFFF"/>'
                     f'<rect x="260" y="740" width="130" height="90" fill="{HYBRIDS["hybrid_a"][mode]["apricot_fill"]}"/>')
            cell = (f'<defs><g id="{cid}">{under}</g><clipPath id="{cl}"><rect x="0" y="728" width="390" height="116" rx="12"/>'
                    f'</clipPath></defs><g clip-path="url(#{cl})"><use href="#{cid}"/>{tab_bar(key, mode, state, cid)}</g>')
            b.append(f'<g transform="translate({x0},{y0 - 728 * 0.82}) scale(0.82)">{cell}</g>')
    b.append(T(40, 860, "Glass opacity: 0.80 light, 0.90 dark (minimum to pass). Worst case idle label: A 10.27 / 5.61, "
                        "B 11.76 / 5.87 (need 4.5). Selected pill vs bar: A 6.17 / 3.13, B 11.76 / 5.87 (need 3.0).",
               13, "#333", LABEL))
    b.append(T(40, 880, "Reduce Transparency and Android: opaque surface, labels are ordinary opaque pairs. "
                        "Increase Contrast adds a 1.5 pt edge at 3:1 or better against page and cards.", 13, "#333", LABEL))
    write("glass-tabbar-states.svg", svg(W, H, "".join(b), "Haunts glass tab bar states",
                                         "Tab bar in glass, reduce transparency, increase contrast and Android states."))


def write_retro():
    """Homepage (round 1) with the tab bar floated to the same place as the hybrids' bar, opaque and bevelled."""
    W, H = 960, 1030
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "Homepage (retro): the same floating bar, opaque and bevelled, not glass", 24, "#111", LABEL, 700),
         T(40, 70, "Same place and size as the hybrids' bar (layout never changes between themes). "
                   "Round-1 screen otherwise unchanged.", 14, "#444", LABEL)]
    for i, mode in enumerate(("light", "dark")):
        t = THEMES["homepage"][mode]
        x, y, w, h = BAR["x"], BAR["y"], BAR["w"], BAR["h"]
        cover = f'<rect x="0" y="756" width="390" height="88" fill="{t["bg"]}"/>'
        bar = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{t["button_face"]}" stroke="{t["button_edge"]}" stroke-width="1.5"/>',
               f'<path d="M{x + 1.5},{y + h - 1.5} V{y + 1.5} H{x + w - 1.5}" stroke="#FFFFFF" stroke-opacity="0.7" stroke-width="1.5" fill="none"/>']
        for j, lab in enumerate(CONTENT["tabs"]):
            tx = x + 6 + j * 87
            sel = j == 0
            bar.append(f'<rect x="{tx}" y="{y + 8}" width="83" height="48" fill="{t["tab"] if sel else t["tab_idle"]}" '
                       f'stroke="{t["outline"]}" stroke-width="1.2"/>')
            bar.append(T(tx + 41.5, y + 37, lab, 13, t["on_tab"] if sel else t["primary"], R1_STACK["homepage"]["ui"],
                         700 if sel else 400, anchor="middle", extra='' if sel else ' text-decoration="underline"'))
        clip = uid("rp")
        b.append(f'<g transform="translate({60 + i * 450},110)"><defs><clipPath id="{clip}"><rect width="390" height="844" rx="52"/>'
                 f'</clipPath></defs>{r1_phone("homepage", mode, "line")}'
                 f'<g clip-path="url(#{clip})">{cover}{"".join(bar)}'
                 f'<rect x="128" y="832" width="134" height="5" rx="2.5" fill="{t["text"]}"/></g></g>')
    b.append(T(60, 995, "Why no glass: the period's look is opaque; translucency over pale boxes and gradients adds",
               13, "#333", LABEL))
    b.append(T(60, 1015, "text-on-texture that cannot be measured; and it would double the retro theme's contrast testing.",
               13, "#333", LABEL))
    write("homepage-floating-bar.svg", svg(W, H, "".join(b), "Haunts Homepage with floating bar",
                                           "Retro theme with an opaque bevelled floating tab bar, light and dark."))


def write_contour_touch():
    """Contour lines as texture in the empty band atop the self-portrait screen (Hybrid A)."""
    W, H = 960, 560
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "Keeping a Contour touch: texture in empty space only", 24, "#111", LABEL, 700),
         T(40, 70, "Top of the self-portrait screen (LOOK-8), Hybrid A. Open lines, never closed rings; no pins, no routes;",
           14, "#444", LABEL),
         T(40, 90, "never behind text. The screen's copy is placeholder.", 14, "#444", LABEL)]
    for i, mode in enumerate(("light", "dark")):
        t = HYBRIDS["hybrid_a"][mode]
        clip = uid("ct")
        lines = "".join(
            f'<path d="M-20,{60 + k * 16} C80,{40 + k * 16 - (k % 3) * 6} 180,{92 + k * 16} 260,{62 + k * 16} '
            f'S360,{40 + k * 16} 420,{70 + k * 16}" fill="none" stroke="{t["accent"]}" stroke-width="1.3" '
            f'stroke-opacity="{0.55 if mode == "light" else 0.4}"/>' for k in range(8))
        body = (f'<rect width="390" height="400" fill="{t["bg"]}"/>{status_bar(t, INTER)}'
                f'<clipPath id="{clip}"><rect x="0" y="48" width="390" height="150"/></clipPath>'
                f'<g clip-path="url(#{clip})">{lines}</g>'
                + T(16, 236, "Your self-portrait", 28, t["text"], NEWS, 600)
                + T(16, 262, "Built on this phone from your own journal.", 14, t["text2"], INTER)
                + f'<rect x="16" y="284" width="358" height="100" rx="20" fill="{t["surface"]}"/>'
                + T(32, 314, "Places you've known longest", 15, t["text"], INTER, 600)
                + T(32, 340, "The Brass Kettle, since March 2023", 17, t["text"], NEWS, 500))
        b.append(f'<g transform="translate({60 + i * 450},100)"><clipPath id="{clip}f"><rect width="390" height="400" rx="30"/>'
                 f'</clipPath><g clip-path="url(#{clip}f)">{body}</g>'
                 f'<rect width="390" height="400" rx="30" fill="none" stroke="#0B0B0C" stroke-width="6"/></g>')
    b.append(T(60, 535, "The texture band holds no text and no control, so it has no contrast duty; it is decoration "
                        "(SC 1.4.11 covers only information-bearing graphics).", 13, "#333", LABEL))
    write("contour-touch.svg", svg(W, H, "".join(b), "Haunts Contour touch",
                                   "Contour-line texture confined to an empty header band, light and dark."))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write_logos()
    write_homes()
    write_ticker()
    write_glass_states()
    write_retro()
    write_contour_touch()
    print("written:", sorted(os.listdir(OUT)))

"""Generate the Haunts concept SVGs (D38). Concept work only; nothing is adopted.

Every SVG is self-contained: no external fonts, no images, no scripts.
Text uses generic font stacks. The first family in each stack is the proposed
OFL font; if it is not installed on the viewing machine, a system stand-in
renders instead. Final artwork would outline the text or bundle the font.

All venue names are fictional. Colours come from palettes.py only.

Run: python3 generate_concepts.py   (writes into ../concepts/)
"""
import math
import os
from xml.sax.saxutils import escape

from palettes import DIRECTIONS, THEMES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "concepts")

STACK = {
    "almanac": dict(display="Newsreader, 'New York', Georgia, 'Times New Roman', serif",
                    ui="Inter, -apple-system, 'Helvetica Neue', Arial, sans-serif",
                    meta="Inter, -apple-system, 'Helvetica Neue', Arial, sans-serif"),
    "doorway": dict(display="'Bricolage Grotesque', 'Avenir Next', 'Trebuchet MS', sans-serif",
                    ui="'Instrument Sans', 'Helvetica Neue', Arial, sans-serif",
                    meta="'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"),
    "ledger": dict(display="'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif",
                   ui="'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif",
                   meta="'IBM Plex Mono', Menlo, 'Courier New', monospace"),
    "contour": dict(display="'Source Serif 4', Georgia, serif",
                    ui="'Source Sans 3', 'Gill Sans', 'Helvetica Neue', sans-serif",
                    meta="'Source Sans 3', 'Gill Sans', 'Helvetica Neue', sans-serif"),
    "homepage": dict(display="Gelasio, Georgia, 'Times New Roman', serif",
                     ui="'DejaVu Sans', Verdana, Tahoma, sans-serif",
                     meta="'DejaVu Sans', Verdana, Tahoma, sans-serif",
                     pixel="Silkscreen, 'Courier New', monospace"),
}
# average advance per character, as a fraction of font size (for manual wrapping)
WIDTH = {"serif": 0.50, "sans": 0.54, "mono": 0.61, "verdana": 0.60, "pixel": 0.80}


def kind_of(stack):
    if "Silkscreen" in stack:
        return "pixel"
    if "Mono" in stack or "monospace" in stack:
        return "mono"
    if "DejaVu" in stack:
        return "verdana"
    if "serif" in stack and "sans-serif" not in stack:
        return "serif"
    return "sans"


def wrap(s, width, size, stack):
    per = WIDTH[kind_of(stack)] * size
    maxc = max(8, int(width / per))
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= maxc:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def T(x, y, s, size, fill, family, weight=400, anchor="start", italic=False, ls=0, extra=""):
    st = ' font-style="italic"' if italic else ""
    lsp = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{escape(family, {chr(34): "&quot;"})}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}{lsp}{extra}>'
            f'{escape(s)}</text>')


def TL(x, y, lines, size, lh, fill, family, **kw):
    return "".join(T(x, y + i * lh, ln, size, fill, family, **kw) for i, ln in enumerate(lines))


def svg(w, h, body, title, desc=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t d">\n<title id="t">{escape(title)}</title>\n'
            f'<desc id="d">{escape(desc)}</desc>\n{body}\n</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# ICONS - each draws in a 1024 x 1024 space. mono=True draws the Android
# themed-icon / iOS tinted reading: one ink colour on a neutral tile.
# ---------------------------------------------------------------------------

def arch_path(x0, x1, top, bottom):
    r = (x1 - x0) / 2
    cy = top + r
    return f"M{x0},{bottom} V{cy} A{r},{r} 0 0 1 {x1},{cy} V{bottom} Z"


def icon_almanac_dogear(mono=False, ink="#1C2127"):
    A = DIRECTIONS["almanac"]["light"]
    bg, page, fold, ver, line = (("#3A3A3A", ink, "#3A3A3A", "#3A3A3A", "#3A3A3A") if mono
                                 else (A["primary"], A["bg"], "#D9CBB0", A["accent"], A["text"]))
    # A well-thumbed page: the top corner is folded down onto the page's face (a dog-ear),
    # showing the paper's other side. Tilted slightly so it reads as a page in hand, not a file icon.
    page_path = "M250,236 q0,-30 30,-30 H560 L780,426 V800 q0,30 -30,30 H280 q-30,0 -30,-30 Z"
    flap = "M560,206 L780,426 L588,398 Q566,395 563,373 Z"
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<g transform="rotate(-7 512 512)">'
            f'<path d="{page_path}" fill="{page}"/>'
            f'<path d="{flap}" fill="{ver}"/>'
            + (f'<path d="{flap}" fill="none" stroke="#3A3A3A" stroke-width="14"/>' if mono else "")
            + f'<rect x="318" y="560" width="330" height="30" rx="8" fill="{line}" opacity="{1 if mono else 0.8}"/>'
            f'<rect x="318" y="650" width="250" height="30" rx="8" fill="{line}" opacity="{1 if mono else 0.8}"/>'
            f'</g>')


def icon_almanac_masthead(mono=False, ink="#1C2127"):
    A = DIRECTIONS["almanac"]["light"]
    bg, fg, ver = (("#3A3A3A", ink, ink) if mono else (A["bg"], A["text"], A["accent"]))
    h = (f'<rect x="330" y="200" width="112" height="550" fill="{fg}"/>'
         f'<rect x="270" y="200" width="172" height="42" rx="4" fill="{fg}"/>'
         f'<rect x="262" y="712" width="250" height="42" rx="4" fill="{fg}"/>'
         f'<path d="M442,478 C500,388 712,370 728,512 V750 H616 V530 C616,452 520,448 442,540 Z" fill="{fg}"/>'
         f'<rect x="560" y="712" width="232" height="42" rx="4" fill="{fg}"/>')
    rules = (f'<rect x="232" y="806" width="560" height="26" fill="{ver}"/>'
             f'<rect x="232" y="850" width="560" height="10" fill="{ver}"/>')
    return f'<rect width="1024" height="1024" fill="{bg}"/>' + h + rules


def icon_almanac_leaf(mono=False, ink="#1C2127"):
    A = DIRECTIONS["almanac"]["light"]
    bg, left, gut, leaf, rib = (("#3A3A3A", "#3A3A3A", "#3A3A3A", ink, "#3A3A3A") if mono
                                else (A["bg"], "#EEE6D6", "#D9CBB0", A["accent"], A["bg"]))
    leaf_d = "M0,-310 C175,-205 195,125 0,300 C-195,125 -175,-205 0,-310 Z"
    veins = "".join(
        f'<path d="M0,{y} L{s * 120},{y - 95}" stroke="{rib}" stroke-width="14" stroke-linecap="round"/>'
        for y in (-110, 10, 130) for s in (-1, 1))
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<rect width="512" height="1024" fill="{left}"/>'
            f'<rect x="506" width="12" height="1024" fill="{gut}"/>'
            f'<g transform="translate(520,500) rotate(-28)">'
            f'<path d="M0,290 L0,400" stroke="{leaf}" stroke-width="24" stroke-linecap="round"/>'
            f'<path d="{leaf_d}" fill="{leaf}"/>'
            f'<path d="M0,-265 L0,280" stroke="{rib}" stroke-width="18" stroke-linecap="round"/>{veins}</g>')


def icon_doorway_arch(mono=False, ink="#1C2127"):
    """A Georgian fanlight door. The fanlight's glazing bars and the squared door leaf
    keep the arch reading as a doorway: a plain arch on a plinth read as a headstone
    in the first draft, which is the one association a product called Haunts cannot carry."""
    D = DIRECTIONS["doorway"]["light"]
    if mono:
        bg, frame, fan, bars, door, knob = "#3A3A3A", ink, ink, "#3A3A3A", ink, "#3A3A3A"
    else:
        bg, frame, fan, bars, door, knob = D["primary"], D["accent"], D["bg"], D["primary"], D["bg"], D["accent"]
    cx, r, spring = 512, 170, 440
    fan_d = f"M{cx - r},{spring} A{r},{r} 0 0 1 {cx + r},{spring} Z"
    bar_lines = "".join(
        f'<line x1="{cx}" y1="{spring}" x2="{cx + r * math.cos(math.radians(a)):.1f}" '
        f'y2="{spring - r * math.sin(math.radians(a)):.1f}" stroke="{bars}" stroke-width="18"/>'
        for a in (45, 90, 135))
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<path d="{arch_path(cx - r - 44, cx + r + 44, spring - r - 44, 830)}" fill="{frame}"/>'
            f'<path d="{fan_d}" fill="{fan}"/>{bar_lines}'
            f'<rect x="{cx - r}" y="{spring}" width="{2 * r}" height="18" fill="{bars}"/>'
            f'<rect x="{cx - r}" y="{spring + 18}" width="{2 * r}" height="{830 - spring - 18}" fill="{door}"/>'
            f'<line x1="{cx}" y1="{spring + 18}" x2="{cx}" y2="830" stroke="{bars}" stroke-width="12"/>'
            f'<circle cx="{cx + 40}" cy="{spring + 200}" r="20" fill="{knob}"/>'
            f'<circle cx="{cx - 40}" cy="{spring + 200}" r="20" fill="{knob}"/>')


def icon_doorway_street(mono=False, ink="#1C2127"):
    """An arcade: equal arched openings cut into one continuous wall, so it reads as
    architecture. The first draft's free-standing arches of different heights read as a
    bar chart or a row of headstones."""
    D = DIRECTIONS["doorway"]["light"]
    if mono:
        bg, wall, o1, o2, o3 = "#3A3A3A", ink, "#3A3A3A", "#3A3A3A", "#3A3A3A"
    else:
        bg, wall, o1, o2, o3 = D["accent"], D["primary"], D["bg"], D["accent"], D["bg"]
    openings = "".join(f'<path d="{arch_path(x, x + 170, 430, 800)}" fill="{c}"/>'
                       for x, c in ((177, o1), (427, o2), (677, o3)))
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<rect x="112" y="300" width="800" height="500" fill="{wall}"/>'
            f'<rect x="92" y="272" width="840" height="34" rx="6" fill="{wall}"/>'
            + openings
            + f'<rect x="92" y="800" width="840" height="30" rx="6" fill="{wall}"/>')


def icon_doorway_ajar(mono=False, ink="#1C2127"):
    D = DIRECTIONS["doorway"]["light"]
    bg, frame, leaf, knob = (("#3A3A3A", ink, "#3A3A3A", ink) if mono
                             else (D["teal"], D["bg"], D["primary"], D["accent"]))
    arch = arch_path(322, 702, 230, 810)
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<path d="{arch}" fill="{frame}"/>'
            f'<g transform="translate(322,0) scale(0.64,1) translate(-322,0)"><path d="{arch}" fill="{leaf}"/></g>'
            + (f'<g transform="translate(322,0) scale(0.64,1) translate(-322,0)"><path d="{arch}" fill="none" stroke="{ink}" stroke-width="16"/></g>' if mono else "")
            + f'<circle cx="518" cy="560" r="20" fill="{knob}"/>')


def icon_ledger_card(mono=False, ink="#1C2127"):
    L = DIRECTIONS["ledger"]["light"]
    bg, card, sig, line = (("#3A3A3A", ink, "#3A3A3A", "#3A3A3A") if mono
                           else (L["text"], L["surface"], L["accent"], L["text"]))
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<rect x="262" y="262" width="210" height="110" rx="18" fill="{card}"/>'
            f'<rect x="212" y="330" width="600" height="440" rx="22" fill="{card}"/>'
            f'<rect x="272" y="440" width="480" height="34" rx="4" fill="{sig}"/>'
            f'<rect x="272" y="530" width="400" height="24" rx="4" fill="{line}"/>'
            f'<rect x="272" y="610" width="440" height="24" rx="4" fill="{line}"/>')


def icon_ledger_entries(mono=False, ink="#1C2127"):
    L = DIRECTIONS["ledger"]["light"]
    bg, fg, sig = (("#3A3A3A", ink, ink) if mono else (L["bg"], L["text"], L["accent"]))
    bars = "".join(
        f'<rect x="250" y="{y}" width="56" height="56" rx="6" fill="{fg}"/>'
        f'<rect x="420" y="{y}" width="{w}" height="56" rx="6" fill="{fg}"/>'
        for y, w in ((270, 360), (484, 280), (698, 330)))
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<rect x="352" y="220" width="20" height="584" fill="{sig}"/>' + bars)


def icon_ledger_bracket(mono=False, ink="#1C2127"):
    L = DIRECTIONS["ledger"]["light"]
    bg, fg = (("#3A3A3A", ink) if mono else (L["accent"], "#FFFFFF"))
    s = f'stroke="{fg}" fill="none" stroke-width="54"'
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<path d="M334,240 H248 V784 H334" {s} stroke-linejoin="miter"/>'
            f'<path d="M690,240 H776 V784 H690" {s} stroke-linejoin="miter"/>'
            f'<path d="M430,268 V756 M430,540 C448,452 612,440 614,560 V756" {s} stroke-linecap="round"/>')


def icon_contour_lines(mono=False, ink="#1C2127"):
    C = DIRECTIONS["contour"]["light"]
    bg, fg = (("#3A3A3A", ink) if mono else (C["primary"], C["bg"]))
    lines = []
    for i, y in enumerate((300, 420, 540, 660, 780)):
        a = 90 - i * 12
        lines.append(f'<path d="M-30,{y} C180,{y - a} 330,{y + a * 0.5} 520,{y - a * 0.7} '
                     f'S860,{y + a * 0.2} 1054,{y - a}" fill="none" stroke="{fg}" stroke-width="{30 - i * 2}" '
                     f'stroke-linecap="round"/>')
    return f'<rect width="1024" height="1024" fill="{bg}"/>' + "".join(lines)


def icon_contour_map(mono=False, ink="#1C2127"):
    C = DIRECTIONS["contour"]["light"]
    if mono:
        bg, p1, p2, river = "#3A3A3A", ink, ink, "#3A3A3A"
    else:
        bg, p1, p2, river = C["bg"], C["primary"], "#4E9A6E", "#9FD3EA"
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<polygon points="212,300 412,250 412,780 212,830" fill="{p1}"/>'
            f'<polygon points="412,250 612,300 612,830 412,780" fill="{p2}"/>'
            f'<polygon points="612,300 812,250 812,780 612,830" fill="{p1}"/>'
            + (f'<path d="M412,250 V780 M612,300 V830" stroke="#3A3A3A" stroke-width="12"/>' if mono else "")
            + f'<path d="M212,640 C330,560 380,660 480,580 S700,470 812,540" fill="none" stroke="{river}" '
              f'stroke-width="34" stroke-linecap="round"/>')


def icon_contour_horizon(mono=False, ink="#1C2127"):
    C = DIRECTIONS["contour"]["light"]
    if mono:
        bg, sun, back, front = "#3A3A3A", ink, "#3A3A3A", ink
    else:
        bg, sun, back, front = C["water"], "#F2C58A", "#7CC39A", C["primary"]
    back_hill = "M0,620 C200,520 380,560 520,610 S860,540 1024,590 V1024 H0 Z"
    front_hill = "M0,760 C240,650 460,720 620,700 S900,640 1024,700 V1024 H0 Z"
    extra = (f'<path d="{back_hill}" fill="none" stroke="{ink}" stroke-width="18"/>' if mono else "")
    return (f'<rect width="1024" height="1024" fill="{bg}"/>'
            f'<circle cx="650" cy="560" r="160" fill="{sun}"/>'
            f'<path d="{back_hill}" fill="{back}"/>{extra}<path d="{front_hill}" fill="{front}"/>')


ICONS = {
    "almanac": [("dogear", "Dog-ear", icon_almanac_dogear),
                ("masthead", "Masthead h", icon_almanac_masthead),
                ("leaf", "Pressed leaf", icon_almanac_leaf)],
    "doorway": [("fanlight", "Fanlight door", icon_doorway_arch),
                ("arcade", "Arcade", icon_doorway_street),
                ("ajar", "Door ajar", icon_doorway_ajar)],
    "ledger": [("card", "Index card", icon_ledger_card),
               ("entries", "Entries", icon_ledger_entries),
               ("bracket", "Bracketed h", icon_ledger_bracket)],
    "contour": [("lines", "Landform lines", icon_contour_lines),
                ("map", "Folded map", icon_contour_map),
                ("horizon", "Horizon", icon_contour_horizon)],
}

SQUIRCLE_R = 229  # ~22.4% of 1024, an approximation of the iOS mask for preview only


def icon_tile(fn, x, y, size, mask="squircle", mono=False, ink="#FFFFFF", cid="c"):
    s = size / 1024
    if mask == "squircle":
        clip = f'<clipPath id="{cid}"><rect width="1024" height="1024" rx="{SQUIRCLE_R}"/></clipPath>'
    elif mask == "circle":
        clip = f'<clipPath id="{cid}"><circle cx="512" cy="512" r="512"/></clipPath>'
    else:
        clip = f'<clipPath id="{cid}"><rect width="1024" height="1024"/></clipPath>'
    inner = fn(mono=mono, ink=ink)
    return (f'<g transform="translate({x},{y}) scale({s:.5f})"><defs>{clip}</defs>'
            f'<g clip-path="url(#{cid})">{inner}</g></g>')


def write_icons():
    for key, items in ICONS.items():
        name = DIRECTIONS[key]["name"]
        for slug, label, fn in items:
            body = fn()
            write(f"{key}-icon-{slug}.svg",
                  svg(1024, 1024, body, f"Haunts concept icon: {name} / {label}",
                      "1024 x 1024 full-bleed artboard, no mask applied (stores and OS apply their own). "
                      "Concept only, not final artwork (D38). No ghost, eye or tracking imagery (D9, D11(d))."))
        write_icon_sheet(key, items)


def write_icon_sheet(key, items):
    name = DIRECTIONS[key]["name"]
    W, H = 1200, 900
    b = [f'<rect width="{W}" height="{H}" fill="#F4F4F2"/>',
         T(40, 56, f"{name}: app-icon concepts", 30, "#111", STACK['almanac']['ui'], 700),
         T(40, 86, "Concept only (D38). Masks are previews: iOS rounded square, Android circle. "
                   "Mono = Android themed icon / iOS tinted.", 15, "#444", STACK['almanac']['ui'])]
    colx = [40, 420, 800]
    for i, (slug, label, fn) in enumerate(items):
        x = colx[i]
        b.append(T(x, 136, f"{chr(65 + i)}. {label}", 20, "#111", STACK['almanac']['ui'], 600))
        b.append(icon_tile(fn, x, 156, 300, cid=f"big{i}"))
        # sizes row
        y = 500
        b.append(T(x, y - 12, "60 px (home screen)", 13, "#444", STACK['almanac']['ui']))
        b.append(icon_tile(fn, x, y, 60, cid=f"s60{i}"))
        b.append(icon_tile(fn, x + 80, y, 60, mask="circle", cid=f"c60{i}"))
        b.append(f'<rect x="{x + 160}" y="{y}" width="60" height="60" rx="13" fill="#2B2B2B"/>')
        b.append(icon_tile(fn, x + 160, y, 60, mono=True, ink="#E8E8E8", cid=f"m60{i}"))
        b.append(T(x, y + 84, "iOS mask · Android circle · mono", 12, "#555", STACK['almanac']['ui']))
        y2 = 620
        b.append(T(x, y2 - 12, "29 px (settings list) and on a dark wallpaper", 13, "#444", STACK['almanac']['ui']))
        b.append(icon_tile(fn, x, y2, 29, cid=f"s29{i}"))
        b.append(f'<rect x="{x + 50}" y="{y2 - 6}" width="250" height="84" rx="12" fill="#1B2330"/>')
        b.append(icon_tile(fn, x + 64, y2 + 6, 60, cid=f"w60{i}"))
        b.append(T(x + 140, y2 + 42, "Haunts", 13, "#FFFFFF", STACK['almanac']['ui']))
    b.append(T(40, 760, "Checks against the brief (icon-brief.md): no ghost, eye, crosshair, pin, radar or footprint; "
                        "no text except where a mnemonic letter is the idea;", 14, "#333", STACK['almanac']['ui']))
    b.append(T(40, 782, "works in one colour; recognisable in greyscale; nothing about drinking or nightlife.",
               14, "#333", STACK['almanac']['ui']))
    b.append(T(40, 820, "Fonts: none used in the icons. Every icon shape is drawn geometry.", 14, "#333",
               STACK['almanac']['ui']))
    write(f"{key}-icons-sheet.svg", svg(W, H, "".join(b), f"Haunts {name}: icon concept sheet",
                                        "Three icon concepts at 300, 60 and 29 px, masked and monochrome."))


# ---------------------------------------------------------------------------
# WORDMARKS
# ---------------------------------------------------------------------------

def doorway_letters(x, base, color, sw=34, scale=1.0):
    """Constructed lowercase 'haunts' from arches and stems. Returns (svg, width)."""
    r = 60
    paths = []
    cx = x

    def P(d):
        paths.append(d)

    # h
    P(f"M{cx},{base - 250} V{base}")
    P(f"M{cx},{base - 100} A{r},{r} 0 0 1 {cx + 2 * r},{base - 100} V{base}")
    cx += 2 * r + 44
    # a (bowl + stem)
    P(f"M{cx + 2 * r},{base - 160} V{base}")
    P(f"M{cx + 2 * r},{base - 80} A{r},{r * 0.95} 0 1 0 {cx + 2 * r},{base - 79.9}")
    cx += 2 * r + 44
    # u
    P(f"M{cx},{base - 160} V{base - 60} A{r},{r} 0 0 0 {cx + 2 * r},{base - 60}")
    P(f"M{cx + 2 * r},{base - 160} V{base}")
    cx += 2 * r + 44
    # n
    P(f"M{cx},{base} V{base - 100} A{r},{r} 0 0 1 {cx + 2 * r},{base - 100} V{base}")
    P(f"M{cx},{base - 160} V{base - 100}")
    cx += 2 * r + 40
    # t
    P(f"M{cx + 28},{base - 225} V{base - 40} Q{cx + 28},{base} {cx + 78},{base}")
    P(f"M{cx - 4},{base - 160} H{cx + 80}")
    cx += 100
    # s
    P(f"M{cx + 108},{base - 138} C{cx + 84},{base - 166} {cx + 6},{base - 168} {cx + 6},{base - 118} "
      f"C{cx + 6},{base - 76} {cx + 112},{base - 88} {cx + 112},{base - 40} "
      f"C{cx + 112},{base + 6} {cx + 28},{base + 6} {cx + 2},{base - 22}")
    cx += 120
    body = "".join(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
                   f'stroke-linejoin="round"/>' for d in paths)
    return body, cx - x


def wordmark(key, mode, x, y, size=1.0):
    """Draw the direction's wordmark with its left edge at x and baseline at y."""
    t = DIRECTIONS[key][mode] if key in DIRECTIONS else THEMES[key][mode]
    S = STACK[key]
    if key == "almanac":
        fs = 120 * size
        return (T(x, y, "Haunts", fs, t["text"], S["display"], 600, ls=-1 * size)
                + f'<rect x="{x}" y="{y + 22 * size}" width="{446 * size}" height="{7 * size}" fill="{t["accent"]}"/>'
                + f'<rect x="{x}" y="{y + 36 * size}" width="{446 * size}" height="{2.5 * size}" fill="{t["accent"]}"/>')
    if key == "doorway":
        g, w = doorway_letters(0, 0, t["primary"])
        return f'<g transform="translate({x},{y}) scale({0.62 * size})">{g}</g>'
    if key == "ledger":
        fs = 104 * size
        return (f'<rect x="{x}" y="{y - 92 * size}" width="{10 * size}" height="{120 * size}" fill="{t["accent"]}"/>'
                + T(x + 34 * size, y, "haunts", fs, t["text"], S["meta"], 500, ls=-2 * size))
    if key == "contour":
        fs = 78 * size
        pid = f"cp{mode}{int(x)}{int(y)}"
        return (f'<defs><path id="{pid}" d="M{x},{y} C{x + 140 * size},{y - 34 * size} {x + 300 * size},{y - 34 * size} '
                f'{x + 470 * size},{y}"/></defs>'
                f'<text font-family="{S["ui"]}" font-size="{fs}" font-weight="600" fill="{t["text"]}" '
                f'letter-spacing="{18 * size}"><textPath href="#{pid}">HAUNTS</textPath></text>'
                f'<path d="M{x - 10 * size},{y + 26 * size} C{x + 140 * size},{y - 6 * size} {x + 300 * size},{y - 6 * size} '
                f'{x + 480 * size},{y + 26 * size}" fill="none" stroke="{t["accent"]}" stroke-width="{3 * size}"/>'
                f'<path d="M{x + 20 * size},{y + 42 * size} C{x + 160 * size},{y + 16 * size} {x + 290 * size},{y + 16 * size} '
                f'{x + 450 * size},{y + 42 * size}" fill="none" stroke="{t["accent"]}" stroke-width="{2 * size}" opacity="0.7"/>')
    if key == "homepage":
        # No tagline: a theme may add no words (themes.md section 2).
        return T(x, y, "Haunts", 64 * size, t["on_title"], S["display"], 700)
    return ""


def write_wordmarks():
    for key in DIRECTIONS:
        name = DIRECTIONS[key]["name"]
        W, H = 1200, 760
        L, D = DIRECTIONS[key]["light"], DIRECTIONS[key]["dark"]
        b = [f'<rect width="{W}" height="{H // 2}" fill="{L["bg"]}"/>',
             f'<rect y="{H // 2}" width="{W}" height="{H // 2}" fill="{D["bg"]}"/>',
             T(40, 44, f"{name}: wordmark concept (light / dark)", 22, L["text2"], STACK['almanac']['ui'], 600),
             wordmark(key, "light", 120, 250),
             wordmark(key, "dark", 120, 250 + H // 2)]
        # recap credit at small size, in a margin
        for mode, yoff in (("light", 0), ("dark", H // 2)):
            t = DIRECTIONS[key][mode]
            b.append(f'<rect x="760" y="{150 + yoff}" width="360" height="170" rx="10" fill="{t["surface"]}" '
                     f'stroke="{t["divider"]}"/>')
            b.append(T(780, 182 + yoff, "Recap image footer (LOOK-5)", 14, t["text2"], STACK[key]['ui']))
            b.append(f'<line x1="780" y1="{250 + yoff}" x2="1100" y2="{250 + yoff}" stroke="{t["divider"]}"/>')
            b.append(f'<g transform="translate(780,{262 + yoff}) scale(0.18)">{wordmark(key, mode, 0, 150)}</g>')
            b.append(T(1100, 300 + yoff, "small, hideable credit", 12, t["text2"], STACK[key]['ui'], anchor="end"))
        b.append(T(40, H - 20, "Working name: nothing containing the name is finalised until PLAT-6's checks pass. "
                               "Text uses stand-in fonts (see brand-directions.md).", 13, D["text2"],
                   STACK['almanac']['ui']))
        write(f"{key}-wordmark.svg", svg(W, H, "".join(b), f"Haunts {name}: wordmark",
                                         "Wordmark on light and dark, with the recap-image credit at small size."))


# ---------------------------------------------------------------------------
# HOME SCREEN MOCKUP (390 x 844 content inside a phone frame)
# ---------------------------------------------------------------------------

CONTENT = {
    "kicker": "From your journal",
    "headline": "Three years of The Brass Kettle. Your first visit was in March 2023.",
    "ticker": ["Three years of The Brass Kettle. Your first visit was in March 2023.",
               "You rate cafés 4.2 and restaurants 3.8, across 14 and 9 rated visits.",
               "Sundays at Mill Lane Bakery, since 2024."],
    "q1_title": "Saturday afternoon",
    "q1_meta": "about 2 hours · 2 places",
    "q1_chain": "Mill Lane Bakery → Regent Cinema",
    "q2_title": "Tuesday, 7:10pm to 9:25pm",
    "q2_meta": "Near Kiln Street. Which place was it?",
    "q2_opts": ["Kiln Street Kitchen", "The Anchor", "Search…"],
    "day1": "Sunday 21 September",
    "rows1": [("The Brass Kettle", "Café · Mill Road", "10:05am to 11:20am, about 1 hour", 4,
               "Window seat, rain outside."),
              ("Northgate Theatre", "Theatre · Northgate", "7:30pm to 10:05pm, about 2½ hours", 5, None)],
    "day2": "Saturday 20 September",
    "rows2": [("Kiln Street Kitchen", "Restaurant · Kiln Street", "1:00pm to 2:15pm, about 1 hour", 3, None)],
    "tabs": ["Journal", "Places", "Portrait", "Settings"],
}

STYLE = {
    "almanac": dict(radius=6, rows="ruled", headline="masthead", section_case="smallcaps", card_pad=0),
    "doorway": dict(radius=22, rows="cards", headline="archcard", section_case="title", card_pad=14),
    "ledger": dict(radius=2, rows="margin", headline="prompt", section_case="mono", card_pad=0),
    "contour": dict(radius=14, rows="cards", headline="panel", section_case="caps", card_pad=14),
    "homepage": dict(radius=0, rows="boxes", headline="ticker", section_case="boxtitle", card_pad=10),
}


def stars(x, y, n, size, fill, empty):
    out = []
    for i in range(5):
        cx = x + i * (size + 3) + size / 2
        pts = []
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5
            rr = size / 2 if k % 2 == 0 else size / 4.6
            pts.append(f"{cx + rr * math.cos(ang):.1f},{y + rr * math.sin(ang):.1f}")
        f = fill if i < n else "none"
        out.append(f'<polygon points="{" ".join(pts)}" fill="{f}" stroke="{fill if i < n else empty}" '
                   f'stroke-width="1.2"/>')
    return "".join(out)


def tab_icon(kind, x, y, c, sw=1.8):
    s = f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
    if kind == "Journal":
        return f'<path d="M{x - 8},{y - 10} h13 l4,4 v16 h-17 z M{x - 4},{y - 2} h9 M{x - 4},{y + 3} h9" {s}/>'
    if kind == "Places":  # an awning over a doorway - deliberately not a map pin
        return (f'<path d="M{x - 10},{y - 4} l3,-7 h14 l3,7 z M{x - 8},{y - 4} v12 h16 v-12 '
                f'M{x - 2},{y + 8} v-6 h4 v6" {s}/>')
    if kind == "Portrait":
        return f'<rect x="{x - 9}" y="{y - 10}" width="18" height="20" rx="3" {s}/><path d="M{x - 5},{y + 5} l4,-5 l3,3 l3,-4" {s}/>'
    return (f'<path d="M{x - 9},{y - 6} h18 M{x - 9},{y + 1} h18 M{x - 9},{y + 8} h18" {s}/>'
            f'<circle cx="{x - 3}" cy="{y - 6}" r="2.4" fill="{c}"/><circle cx="{x + 4}" cy="{y + 1}" r="2.4" fill="{c}"/>'
            f'<circle cx="{x - 1}" cy="{y + 8}" r="2.4" fill="{c}"/>')


def status_bar(t, fam):
    return (T(32, 34, "9:41", 16, t["text"], fam, 600)
            + f'<rect x="300" y="24" width="17" height="10" rx="2" fill="{t["text"]}"/>'
            + f'<rect x="324" y="22" width="26" height="13" rx="3.5" fill="none" stroke="{t["text"]}" stroke-width="1.2"/>'
            + f'<rect x="326.5" y="24.5" width="19" height="8" rx="1.5" fill="{t["text"]}"/>')


def section_label(key, t, x, y, label, S, st):
    if st["section_case"] == "smallcaps":
        return (T(x, y, label.upper(), 12, t["text2"], S["ui"], 600, ls=1.6)
                + f'<line x1="{x}" y1="{y + 8}" x2="{390 - x}" y2="{y + 8}" stroke="{t["text"]}" stroke-width="1"/>')
    if st["section_case"] == "mono":
        return T(x, y, "// " + label.lower(), 13, t["text2"], S["meta"], 500)
    if st["section_case"] == "caps":
        return T(x, y, label.upper(), 12, t["text2"], S["ui"], 700, ls=2.2)
    if st["section_case"] == "boxtitle":
        return ""
    return T(x, y, label, 17, t["text"], S["display"], 700)


def headline_block(key, t, S, st, y, appearance):
    """Returns (svg, height). Appearance: line | ticker | line-fallback."""
    X, W = 16, 358
    k = CONTENT["kicker"]
    if appearance == "ticker" and key == "homepage":
        h = 58
        items = "   »   ".join(CONTENT["ticker"])
        g = [f'<rect x="{X}" y="{y}" width="{W}" height="{h}" fill="{t["ticker_bg"]}" stroke="{t["outline"]}"/>',
             f'<rect x="{X}" y="{y}" width="78" height="{h}" fill="{t["title_bottom"]}"/>',
             # the same kicker string as every theme, set in the pixel face: case is presentation, words are not
             T(X + 8, y + 26, "FROM YOUR", 10, t["on_title"], S["pixel"]),
             T(X + 8, y + 42, "JOURNAL", 10, t["on_title"], S["pixel"]),
             f'<clipPath id="tk{key}{y}"><rect x="{X + 80}" y="{y}" width="{W - 80 - 106}" height="{h}"/></clipPath>',
             f'<g clip-path="url(#tk{key}{y})">' + T(X + 86 - 118, y + 35, items, 15, t["on_ticker"], S["ui"]) + "</g>",
             # options control (HEAD-5) and pause control (HEAD-9): bevel buttons, 44 x 44 targets
             f'<rect x="{X + W - 104}" y="{y + 7}" width="46" height="44" fill="{t["button_face"]}" '
             f'stroke="{t["button_edge"]}" stroke-width="1.5"/>',
             T(X + W - 81, y + 34, "···", 16, t["on_button"], S["ui"], 700, anchor="middle"),
             f'<rect x="{X + W - 54}" y="{y + 7}" width="46" height="44" fill="{t["button_face"]}" '
             f'stroke="{t["button_edge"]}" stroke-width="1.5"/>',
             f'<rect x="{X + W - 38}" y="{y + 20}" width="5" height="18" fill="{t["on_button"]}"/>',
             f'<rect x="{X + W - 29}" y="{y + 20}" width="5" height="18" fill="{t["on_button"]}"/>']
        return "".join(g), h + 14
    if key == "homepage":  # line / reduce-motion fallback
        lines = wrap(CONTENT["headline"], W - 110, 15, S["ui"])
        h = 34 + 20 * len(lines)
        g = [f'<rect x="{X}" y="{y}" width="{W}" height="{h}" fill="{t["ticker_bg"]}" stroke="{t["outline"]}"/>',
             T(X + 10, y + 20, "FROM YOUR JOURNAL", 11, t["on_ticker"], S["pixel"]),
             TL(X + 10, y + 42, lines, 15, 20, t["on_ticker"], S["ui"]),
             f'<rect x="{X + W - 54}" y="{y + (h - 44) / 2}" width="46" height="44" fill="{t["button_face"]}" '
             f'stroke="{t["button_edge"]}" stroke-width="1.5"/>',
             T(X + W - 31, y + h / 2 + 5, "···", 16, t["on_button"], S["ui"], 700, anchor="middle")]
        # The explanation of the fallback lives on the options screen (HEAD-10(c)), never on the home screen.
        return "".join(g), h + 14
    def opts_at(cx, cy, ring=t["outline"], dot=t["text"]):
        # "Headline options" control: 44 x 44 target around a 36 px ring (HEAD-5, A11Y-5)
        return (f'<circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{ring}" stroke-width="1.3"/>'
                + "".join(f'<circle cx="{cx + dx}" cy="{cy}" r="1.9" fill="{dot}"/>' for dx in (-6, 0, 6)))

    if st["headline"] == "masthead":
        lines = wrap(CONTENT["headline"], W - 50, 22, S["display"])
        h = 44 + 28 * len(lines)
        g = [f'<rect x="{X}" y="{y}" width="{W}" height="3" fill="{t["text"]}"/>',
             f'<rect x="{X}" y="{y + 6}" width="{W}" height="1" fill="{t["text"]}"/>',
             T(X, y + 30, k.upper(), 11.5, t["kicker"], S["ui"], 700, ls=1.6),
             TL(X, y + 58, lines, 22, 28, t["text"], S["display"], weight=500),
             opts_at(X + W - 22, y + 30)]
        return "".join(g), h + 10
    if st["headline"] == "archcard":
        lines = wrap(CONTENT["headline"], W - 76, 19, S["display"])
        h = 58 + 25 * len(lines)
        r = 40
        d = f"M{X},{y + h} V{y + r} Q{X},{y} {X + r},{y} H{X + W - r} Q{X + W},{y} {X + W},{y + r} V{y + h} Z"
        g = [f'<path d="{d}" fill="{t["apricot_fill"]}"/>',
             T(X + 20, y + 34, k, 13, t["on_apricot"], S["ui"], 700),
             TL(X + 20, y + 62, lines, 19, 25, t["on_apricot"], S["display"], weight=600),
             opts_at(X + W - 30, y + 30, t["on_apricot"], t["on_apricot"])]
        return "".join(g), h + 16
    if st["headline"] == "prompt":
        lines = wrap(CONTENT["headline"], W - 60, 18, S["ui"])
        h = 40 + 24 * len(lines)
        g = [f'<rect x="{X}" y="{y}" width="3" height="{h - 8}" fill="{t["accent"]}"/>',
             T(X + 14, y + 16, "> " + k.lower(), 13, t["kicker"], S["meta"], 500),
             TL(X + 14, y + 42, lines, 18, 24, t["text"], S["ui"], weight=500),
             opts_at(X + W - 22, y + 20)]
        return "".join(g), h + 12
    # contour panel
    lines = wrap(CONTENT["headline"], W - 70, 20, S["display"])
    h = 56 + 26 * len(lines)
    # Texture never sits behind text: the contour lines run in a band down the panel's left edge only.
    tex = "".join(f'<path d="M{X + 2 + i * 3},{y} C{X - 4 + i * 3},{y + h * 0.3} {X + 10 + i * 3},{y + h * 0.6} {X + 2 + i * 3},{y + h}" '
                  f'fill="none" stroke="{t["accent"]}" stroke-width="1.2" opacity="0.7"/>' for i in range(3))
    g = [f'<rect x="{X}" y="{y}" width="{W}" height="{h}" rx="{st["radius"]}" fill="{t["surface"]}"/>',
         f'<clipPath id="pn{key}{y}{t["bg"][1:]}"><rect x="{X}" y="{y}" width="{W}" height="{h}" rx="{st["radius"]}"/></clipPath>',
         f'<g clip-path="url(#pn{key}{y}{t["bg"][1:]})">{tex}</g>',
         T(X + 24, y + 30, k.upper(), 11.5, t["kicker"], S["ui"], 700, ls=2),
         TL(X + 24, y + 58, lines, 20, 26, t["text"], S["display"], italic=True, weight=500),
         opts_at(X + W - 30, y + 28)]
    return "".join(g), h + 16


def button(key, t, S, st, x, y, label, primary=True, w=None):
    w = w or (len(label) * 8.2 + 34)
    if key == "homepage":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="36" fill="{t["button_face"]}" stroke="{t["button_edge"]}" stroke-width="1.5"/>'
                f'<path d="M{x + 1.5},{y + 34} V{y + 1.5} H{x + w - 1.5}" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.7"/>'
                + T(x + w / 2, y + 23, label + " »", 13, t["on_button"], S["ui"], 700, anchor="middle"), w)
    if primary:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="{min(st["radius"], 18)}" fill="{t["primary"]}"/>'
                + T(x + w / 2, y + 23, label, 14, t["on_primary"], S["ui"], 600, anchor="middle"), w)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="{min(st["radius"], 18)}" fill="none" stroke="{t["outline"]}" stroke-width="1.3"/>'
            + T(x + w / 2, y + 23, label, 14, t["text"], S["ui"], 500, anchor="middle"), w)


def chip(key, t, S, st, x, y, label):
    w = len(label) * (7.1 if key == "homepage" else 6.6) + 24
    if key == "homepage":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="34" fill="{t["surface"]}" stroke="{t["outline"]}"/>'
                + T(x + 11, y + 22, label, 12.5, t["primary"], S["ui"], extra=' text-decoration="underline"'), w)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="{18 if st["radius"] > 10 else st["radius"]}" '
            f'fill="{t["surface"]}" stroke="{t["outline"]}" stroke-width="1.2"/>'
            + T(x + 12, y + 23, label, 12.5, t["text"], S["ui"], 500), w)


def box_title(t, X, y, W, label, S):
    gid = f"bt{t['bg'][1:]}{int(y)}"
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{t["box_title_top"]}"/><stop offset="1" stop-color="{t["box_title"]}"/>'
            f'</linearGradient></defs>'
            f'<rect x="{X}" y="{y}" width="{W}" height="28" fill="url(#{gid})" stroke="{t["outline"]}"/>'
            + T(X + 10, y + 19, "» " + label, 14, t["on_box_title"], S["display"], 700))


def queue_block(key, t, S, st, y):
    X, W = 16, 358
    g = []
    if key == "homepage":
        g.append(box_title(t, X, y, W, "To confirm", S))
        y += 28
        top = y
        y += 10
    else:
        g.append(section_label(key, t, X, y + 14, "To confirm", S, st))
        y += 30
        top = y
    # row 1 (session)
    pad = st["card_pad"]
    r1h = 88
    tsz = 14.5 if key == "homepage" else 16
    if st["rows"] == "cards":
        g.append(f'<rect x="{X}" y="{y}" width="{W}" height="{r1h}" rx="{st["radius"]}" fill="{t["surface"]}"/>')
    g.append(T(X + pad + 2, y + 24, CONTENT["q1_title"], tsz, t["text"], S["ui"], 600))
    g.append(T(X + pad + 2, y + 45, CONTENT["q1_meta"], 13.5, t["text2"], S["meta"] if key == "ledger" else S["ui"]))
    g.append(T(X + pad + 2, y + 66, CONTENT["q1_chain"], 13.5, t["text2"], S["ui"]))
    b, _ = button(key, t, S, st, X + W - pad - 96, y + 14, "Review", True, 90)
    g.append(b)
    y += r1h + (10 if st["rows"] == "cards" else 0)
    if st["rows"] in ("ruled", "margin", "boxes"):
        g.append(f'<line x1="{X}" y1="{y - 8}" x2="{X + W}" y2="{y - 8}" stroke="{t["divider"]}" stroke-width="1"/>')
    # row 2 (uncertain visit, options shown, none selected: D8, CONF-2, CONF-3)
    r2h = 108
    if st["rows"] == "cards":
        g.append(f'<rect x="{X}" y="{y}" width="{W}" height="{r2h}" rx="{st["radius"]}" fill="{t["surface"]}"/>')
    g.append(T(X + pad + 2, y + 24, CONTENT["q2_title"], tsz, t["text"], S["ui"], 600))
    # unconfirmed label: word + dashed outline, never colour alone (A11Y-2)
    lw = 104
    g.append(f'<rect x="{X + W - pad - lw}" y="{y + 8}" width="{lw}" height="24" rx="{min(st["radius"], 12)}" '
             f'fill="none" stroke="{t["unconfirmed"]}" stroke-dasharray="4 3" stroke-width="1.3"/>')
    g.append(T(X + W - pad - lw / 2, y + 25, "Unconfirmed", 12.5, t["unconfirmed"], S["ui"], 600, anchor="middle"))
    g.append(T(X + pad + 2, y + 46, CONTENT["q2_meta"], 13.5, t["text2"], S["ui"]))
    cx = X + pad + 2
    for lab in CONTENT["q2_opts"]:
        c, w = chip(key, t, S, st, cx, y + 60, lab)
        g.append(c)
        cx += w + 8
    y += r2h + 14
    if key == "homepage":
        g.insert(0, f'<rect x="{X}" y="{top}" width="{W}" height="{y - top - 4}" fill="{t["surface"]}" stroke="{t["outline"]}"/>')
    return "".join(g), y


def timeline_block(key, t, S, st, y, limit_y):
    X, W = 16, 358
    g = []
    if key == "homepage":
        g.append(box_title(t, X, y, W, "Your journal", S))
        box_top = y + 28
        g.append(f'<rect x="{X}" y="{box_top}" width="{W}" height="{limit_y - box_top}" fill="{t["surface"]}" stroke="{t["outline"]}"/>')
        y = box_top + 8
    for day, rows in ((CONTENT["day1"], CONTENT["rows1"]), (CONTENT["day2"], CONTENT["rows2"])):
        if y > limit_y - 40:
            break
        if key == "homepage":
            g.append(T(X + 10, y + 16, day, 13, t["text"], S["ui"], 700))
            g.append(f'<line x1="{X + 10}" y1="{y + 24}" x2="{X + W - 10}" y2="{y + 24}" stroke="{t["divider"]}" stroke-dasharray="2 2"/>')
            y += 32
        elif st["section_case"] == "mono":
            g.append(T(X, y + 14, "// " + day.lower(), 13, t["text2"], S["meta"], 500))
            y += 28
        else:
            g.append(section_label(key, t, X, y + 14, day, S, st) if st["section_case"] != "title"
                     else T(X, y + 16, day, 16, t["text"], S["display"], 700))
            y += 30
        for name, cat, time, rating, note in rows:
            rh = 96 + (20 if note else 0)
            if y + rh > limit_y:
                return "".join(g), y
            pad = st["card_pad"]
            if st["rows"] == "cards":
                g.append(f'<rect x="{X}" y="{y}" width="{W}" height="{rh}" rx="{st["radius"]}" fill="{t["surface"]}"/>')
            xx = X + pad + 2
            if st["rows"] == "margin":
                g.append(f'<line x1="{X + 74}" y1="{y}" x2="{X + 74}" y2="{y + rh}" stroke="{t["accent"]}" stroke-width="1.2"/>')
                g.append(T(X, y + 22, time.split(" to ")[0], 12, t["text2"], S["meta"]))
                xx = X + 86
            nm_fam = S["display"] if key in ("almanac",) else S["ui"]
            if key == "homepage":
                g.append(T(xx, y + 22, name, 16, t["primary"], S["ui"], 700, extra=' text-decoration="underline"'))
            else:
                g.append(T(xx, y + 22, name, 17 if key == "almanac" else 16, t["text"], nm_fam, 600,
                           italic=(key == "contour")))
            g.append(T(xx, y + 42, cat, 13, t["text2"], S["ui"]))
            tm = time if st["rows"] != "margin" else time.split(", ")[1]
            g.append(T(xx, y + 60, tm, 13, t["text2"], S["meta"] if key == "ledger" else S["ui"]))
            g.append(stars(xx + 1, y + 78, rating, 13, t["star"], t["outline"]))
            g.append(T(xx + 86, y + 83, f"{rating}/5", 13, t["text"], S["ui"], 600))
            if note:
                g.append(T(xx, y + 104, "Note: " + note, 13, t["text2"], S["ui"], italic=(key != "ledger")))
            y += rh + (10 if st["rows"] == "cards" else 0)
            if st["rows"] in ("ruled", "margin", "boxes"):
                g.append(f'<line x1="{X + (10 if key == "homepage" else 0)}" y1="{y - 4}" x2="{X + W - (10 if key == "homepage" else 0)}" '
                         f'y2="{y - 4}" stroke="{t["divider"]}" stroke-width="1"/>')
                y += 6
    return "".join(g), y


def tab_bar(key, t, S, st):
    y0 = 844 - 84
    g = []
    if key == "homepage":
        g.append(f'<rect x="0" y="{y0}" width="390" height="84" fill="{t["box_title"]}"/>')
        g.append(f'<line x1="0" y1="{y0}" x2="390" y2="{y0}" stroke="{t["outline"]}" stroke-width="2"/>')
        for i, lab in enumerate(CONTENT["tabs"]):
            x = 8 + i * 94
            sel = i == 0
            g.append(f'<rect x="{x}" y="{y0 + 8}" width="88" height="44" fill="{t["tab"] if sel else t["tab_idle"]}" '
                     f'stroke="{t["outline"]}" stroke-width="1.2"/>')
            g.append(T(x + 44, y0 + 35, lab, 13, t["on_tab"] if sel else t["primary"], S["ui"], 700 if sel else 400,
                       anchor="middle", extra='' if sel else ' text-decoration="underline"'))
        g.append(f'<rect x="128" y="{844 - 14}" width="134" height="5" rx="2.5" fill="{t["text"]}"/>')
        return "".join(g)
    g.append(f'<rect x="0" y="{y0}" width="390" height="84" fill="{t["surface"] if key != "almanac" else t["bg"]}"/>')
    g.append(f'<line x1="0" y1="{y0}" x2="390" y2="{y0}" stroke="{t["divider"]}" stroke-width="1"/>')
    for i, lab in enumerate(CONTENT["tabs"]):
        cx = 49 + i * 97
        c = t["primary"] if i == 0 else t["text2"]
        g.append(tab_icon(lab, cx, y0 + 24, c))
        g.append(T(cx, y0 + 52, lab, 11.5, c, S["ui"], 600 if i == 0 else 500, anchor="middle"))
    g.append(f'<rect x="128" y="{844 - 14}" width="134" height="5" rx="2.5" fill="{t["text"]}"/>')
    return "".join(g)


def header(key, t, S, st):
    g = []
    if key == "homepage":
        gid = f"hg{t['bg'][1:]}"
        g.append(f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["title_top"]}"/>'
                 f'<stop offset="1" stop-color="{t["title_bottom"]}"/></linearGradient></defs>')
        g.append(f'<rect x="0" y="48" width="390" height="62" fill="url(#{gid})"/>')
        g.append(f'<g transform="translate(16,88) scale(0.5)">{wordmark("homepage", "light" if t["bg"] == THEMES["homepage"]["light"]["bg"] else "dark", 0, 0)}</g>')
        g.append(f'<rect x="318" y="58" width="56" height="42" fill="{t["button_face"]}" stroke="{t["button_edge"]}" stroke-width="1.5"/>')
        g.append(T(346, 85, "+ Add", 12.5, t["on_button"], S["ui"], 700, anchor="middle"))
        return "".join(g), 122
    mode = "light" if t == DIRECTIONS[key]["light"] else "dark"
    g.append(f'<g transform="translate(16,{100 if key == "doorway" else 90}) scale({0.26 if key != "doorway" else 0.2})">'
             f'{wordmark(key, mode, 0, 0)}</g>')
    # add-place control (manual entry, CONF-6), 44x44
    g.append(f'<circle cx="352" cy="78" r="20" fill="none" stroke="{t["outline"]}" stroke-width="1.3"/>')
    g.append(f'<path d="M352,70 v16 M344,78 h16" stroke="{t["text"]}" stroke-width="2" stroke-linecap="round"/>')
    return "".join(g), 116


def phone(key, mode, appearance="line", label=None):
    spec = DIRECTIONS.get(key) or THEMES[key]
    t = spec[mode]
    S, st = STACK[key], STYLE[key]
    clip = f"ph{key}{mode}{appearance}"
    g = [f'<clipPath id="{clip}"><rect width="390" height="844" rx="52"/></clipPath>',
         f'<g clip-path="url(#{clip})">',
         f'<rect width="390" height="844" fill="{t["bg"]}"/>']
    if key == "contour":  # contour texture in the empty part of the header only: never behind text
        g.append(f'<clipPath id="hx{clip}"><rect x="170" y="50" width="150" height="62"/></clipPath>'
                 f'<g clip-path="url(#hx{clip})">'
                 + "".join(f'<path d="M150,{40 + i * 11} C200,{28 + i * 11} 260,{58 + i * 11} 340,{34 + i * 11}" fill="none" '
                           f'stroke="{t["accent"]}" stroke-width="1.2" opacity="0.45"/>' for i in range(8)) + "</g>")
    g.append(status_bar(t, S["ui"]))
    h, y = header(key, t, S, st)
    g.append(h)
    hb, hh = headline_block(key, t, S, st, y, appearance)
    g.append(hb)
    y += hh
    qb, y = queue_block(key, t, S, st, y)
    g.append(qb)
    tb, _ = timeline_block(key, t, S, st, y + 4, 844 - 92)
    g.append(tb)
    g.append(tab_bar(key, t, S, st))
    g.append("</g>")
    g.append(f'<rect x="-1" y="-1" width="392" height="846" rx="53" fill="none" stroke="#0B0B0C" stroke-width="10"/>')
    g.append(f'<rect x="140" y="11" width="110" height="30" rx="15" fill="#0B0B0C"/>')
    return "".join(g)


def write_home_mockups():
    for key in DIRECTIONS:
        name = DIRECTIONS[key]["name"]
        W, H = 960, 1010
        b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
             T(40, 44, f"{name}: home screen (light and dark)", 24, "#111", STACK['almanac']['ui'], 700),
             T(40, 70, "Headline (Line), confirm queue, timeline. Fictional venues. Concept only (D38); fonts are stand-ins.",
               14, "#444", STACK['almanac']['ui']),
             f'<g transform="translate(60,110)">{phone(key, "light")}</g>',
             f'<g transform="translate(510,110)">{phone(key, "dark")}</g>',
             T(60, 990, "No count, badge or progress on the queue (CONF-1). No option pre-selected (CONF-3). "
                        "Rating always also as text (A11Y-2). No pin icons.", 13, "#333", STACK['almanac']['ui'])]
        write(f"{key}-home.svg", svg(W, H, "".join(b), f"Haunts {name}: home-screen mockup",
                                     "Phone frames at 390 x 844 showing headline, confirm queue and timeline, light and dark."))


def write_theme_comparison():
    for mode in ("light", "dark"):
        W, H = 1420, 1040
        b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
             T(40, 44, f"Themes on the same screen ({mode} mode): modern default vs retro", 24, "#111",
               STACK['almanac']['ui'], 700),
             T(40, 70, "Same layout, same copy, same order, same controls. Only colour, type, shape and texture change. "
                       "Default shown as Almanac, the recommended direction; not adopted.", 14, "#444", STACK['almanac']['ui']),
             T(60, 104, "1. Modern default (Almanac), Line", 16, "#111", STACK['almanac']['ui'], 700),
             f'<g transform="translate(60,120)">{phone("almanac", mode, "line")}</g>',
             T(510, 104, "2. Homepage (retro), user chose Ticker", 16, "#111", STACK['almanac']['ui'], 700),
             f'<g transform="translate(510,120)">{phone("homepage", mode, "ticker")}</g>',
             T(960, 104, "3. Homepage, Reduce Motion on: a still line", 16, "#111", STACK['almanac']['ui'], 700),
             f'<g transform="translate(960,120)">{phone("homepage", mode, "line-fallback")}</g>',
             T(60, 1000, "The theme never picks the headline appearance: Line/Card/Ticker/Off is the user's own setting (HEAD-2). "
                         "The ticker has a pause control whenever it moves (HEAD-9)", 13, "#333", STACK['almanac']['ui']),
             T(60, 1020, "and becomes a still line under Reduce Motion, a screen reader or large text (HEAD-10, HEAD-11). "
                         "No blink, no hit counter, no badges.", 13, "#333", STACK['almanac']['ui'])]
        write(f"themes-default-vs-retro-{mode}.svg",
              svg(W, H, "".join(b), f"Haunts themes compared, {mode}",
                  "Modern default and retro Homepage theme on the same home screen, plus the retro reduce-motion fallback."))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write_icons()
    write_wordmarks()
    write_home_mockups()
    write_theme_comparison()
    print("written:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]), "svg files")

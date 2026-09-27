"""Generate the round-3 concept SVGs (D44): final marks, wordmarks, the theme picker,
and the optional app-icon setting. Concept work only; nothing is adopted beyond D44.

Writes into ../round-3/concepts/. Earlier rounds are not touched.
Run: python3 generate_round3.py
"""
import os

from generate_concepts import T, TL, wrap, svg, icon_tile, status_bar, tab_icon, phone as r1_phone
from generate_round2 import h_glyph, content, tab_bar, uid, NEWS, INTER, MONO, LABEL, BAR
from palettes import HYBRIDS, THEMES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "round-3", "concepts")
A_L, A_D = HYBRIDS["hybrid_a"]["light"], HYBRIDS["hybrid_a"]["dark"]
B_L, B_D = HYBRIDS["hybrid_b"]["light"], HYBRIDS["hybrid_b"]["dark"]
PLUM, CREAM, APRICOT, DARKPLUM = A_L["primary"], A_L["bg"], A_L["accent"], A_D["bg"]
ORANGE = B_L["accent"]


def write(name, s):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(s)


def scaled(inner, s):
    return f'<g transform="translate(512,512) scale({s}) translate(-512,-512)">{inner}</g>'


# ---------------------------------------------------------------------------
# Final icons. Each takes (mono, ink) like the earlier rounds, plus dark and
# adaptive (Android foreground scaled into the 66/108 safe zone).
# ---------------------------------------------------------------------------

def a_masthead(mono=False, ink="#FFFFFF", dark=False, adaptive=False):
    bg = "#3A3A3A" if mono else (DARKPLUM if dark else PLUM)
    fg = ink if mono else CREAM
    rule = ink if mono else APRICOT
    mark = (h_glyph(fg, 0, -34)
            + f'<rect x="266" y="760" width="532" height="36" rx="4" fill="{rule}"/>'
            + f'<rect x="266" y="812" width="532" height="16" rx="3" fill="{rule}"/>')
    return f'<rect width="1024" height="1024" fill="{bg}"/>' + (scaled(mark, 0.9) if adaptive else mark)


def a_fullstop(mono=False, ink="#FFFFFF", dark=False, adaptive=False):
    bg = "#3A3A3A" if mono else (DARKPLUM if dark else CREAM)
    fg = ink if mono else (CREAM if dark else PLUM)
    dot = ink if mono else APRICOT
    mark = h_glyph(fg, -60, 10, 0.95) + f'<circle cx="790" cy="712" r="58" fill="{dot}"/>'
    return f'<rect width="1024" height="1024" fill="{bg}"/>' + (scaled(mark, 0.9) if adaptive else mark)


def b_bar(mono=False, ink="#FFFFFF", dark=False, adaptive=False):
    bg = "#3A3A3A" if mono else ("#0F0F10" if dark else "#111111")
    fg = ink if mono else "#FFFFFF"
    bar = ink if mono else ORANGE
    mark = h_glyph(fg, -50, -10, 0.92) + f'<rect x="712" y="700" width="120" height="44" fill="{bar}"/>'
    return f'<rect width="1024" height="1024" fill="{bg}"/>' + (scaled(mark, 0.9) if adaptive else mark)


FINAL = [("a-icon-masthead", "A (Warm): Masthead h, double underline", a_masthead),
         ("a-icon-fullstop", "A alternative: full-stop h", a_fullstop),
         ("b-icon-bar", "B (Mono): h with orange bar", b_bar)]


def v(fn, **kw):
    return lambda mono=False, ink="#FFFFFF": fn(mono=mono, ink=ink, **kw)


def write_icons():
    for slug, label, fn in FINAL:
        write(f"{slug}.svg", svg(1024, 1024, fn(), f"Haunts final icon: {label}",
                                 "1024 x 1024 master, full bleed, no mask. D44. Artwork for final production is a "
                                 "separate CEO decision (round-3 icon-brief.md)."))
    W, H = 1500, 1000
    b = [f'<rect width="{W}" height="{H}" fill="#F4F4F2"/>',
         T(40, 52, "Final marks (D44): every appearance each store and OS asks for", 28, "#111", LABEL, 700),
         T(40, 80, "Concept masters. iOS: default, dark, tinted (one silhouette). Android: adaptive (foreground inside the "
                   "dashed 66/108 safe zone) and themed monochrome.", 14, "#444", LABEL)]
    cols = [("iOS default", {}, "squircle", False), ("iOS dark", {"dark": True}, "squircle", False),
            ("iOS tinted / Android themed", {}, "squircle", True), ("Android adaptive", {"adaptive": True}, "circle", False)]
    for c, (lab, _, _, _) in enumerate(cols):
        b.append(T(330 + c * 230, 124, lab, 15, "#111", LABEL, 600))
    b.append(T(1250, 124, "60 px · 29 px", 15, "#111", LABEL, 600))
    for r, (slug, label, fn) in enumerate(FINAL):
        y = 144 + r * 270
        b.append(T(40, y + 90, label.split(":")[0], 18, "#111", LABEL, 700))
        b.append(T(40, y + 114, label.split(": ")[1], 14, "#444", LABEL))
        for c, (lab, kw, mask, mono) in enumerate(cols):
            x = 330 + c * 230
            if mono:
                b.append(f'<rect x="{x}" y="{y}" width="200" height="200" rx="44" fill="#2B2B2B"/>')
            b.append(icon_tile(v(fn, **kw), x, y, 200, mask=mask, mono=mono, ink="#E8E8E8", cid=uid("i")))
            if kw.get("adaptive"):
                side = 200 * 66 / 108
                o = (200 - side) / 2
                b.append(f'<rect x="{x + o:.1f}" y="{y + o:.1f}" width="{side:.1f}" height="{side:.1f}" fill="none" '
                         f'stroke="#E4572E" stroke-width="1.5" stroke-dasharray="5 4"/>')
        b.append(icon_tile(fn, 1250, y + 40, 60, cid=uid("s")))
        b.append(icon_tile(fn, 1330, y + 56, 29, cid=uid("t")))
        b.append(f'<rect x="1250" y="{y + 118}" width="140" height="76" rx="12" fill="#1B2330"/>')
        b.append(icon_tile(v(fn, dark=True), 1262, y + 126, 60, cid=uid("w")))
    b.append(T(40, 975, "No ghost, eye, pin, radar, route, headstone, glass or bottle (D9, D11(d), MEM-1). "
                        "The B bar is never animated. Dashed square = Android's 66 dp safe zone.", 13, "#333", LABEL))
    write("icons-final.svg", svg(W, H, "".join(b), "Haunts final icons, all appearances",
                                 "The three final icon masters in iOS default, dark, tinted, Android adaptive, at 60 and 29 px."))


# ---------------------------------------------------------------------------
# Wordmarks
# ---------------------------------------------------------------------------

A_WIDTH = 414  # matched by eye to the stand-in's word width at 120 px; final artwork matches Newsreader's


def wordmark(key, mode, x, y, size=1.0, credit=False):
    t = HYBRIDS[key][mode]
    word = T(x + (32 * size if key == "hybrid_b" else 0), y, "haunts", 120 * size, t["text"], NEWS, 600, ls=-2 * size)
    if key == "hybrid_b":
        return f'<rect x="{x}" y="{y - 84 * size}" width="{9 * size}" height="{108 * size}" fill="{t["accent"]}"/>' + word
    w = A_WIDTH * size
    if credit:  # below ~32 px tall the double rule becomes one hairline
        return word + f'<rect x="{x}" y="{y + 16 * size}" width="{w}" height="{max(1.0, 5 * size)}" fill="{t["accent"]}"/>'
    return (word + f'<rect x="{x}" y="{y + 20 * size}" width="{w}" height="{9 * size}" fill="{t["accent"]}"/>'
            + f'<rect x="{x}" y="{y + 35 * size}" width="{w}" height="{3.5 * size}" fill="{t["accent"]}"/>')


def write_wordmarks():
    W, H = 1300, 900
    b = [f'<rect width="{W}" height="{H}" fill="#F4F4F2"/>',
         T(40, 52, "Final wordmarks (D44): lowercase \"haunts\"", 28, "#111", LABEL, 700),
         T(40, 80, "A (Warm): Newsreader with Almanac's double rule, thick over thin. B (Mono): the orange margin rule. "
                   "Stand-in font; final artwork is outlined.", 14, "#444", LABEL)]
    for r, key in enumerate(("hybrid_a", "hybrid_b")):
        y0 = 110 + r * 380
        for c, mode in enumerate(("light", "dark")):
            t = HYBRIDS[key][mode]
            x0 = 40 + c * 620
            b.append(f'<rect x="{x0}" y="{y0}" width="600" height="220" rx="16" fill="{t["bg"]}"/>')
            b.append(wordmark(key, mode, x0 + 70, y0 + 150))
            b.append(f'<rect x="{x0}" y="{y0 + 234}" width="600" height="110" rx="16" fill="{t["surface"]}" stroke="#DDD"/>')
            b.append(T(x0 + 24, y0 + 262, "Recap footer credit (LOOK-5), small and hideable", 13, t["text2"], LABEL))
            b.append(f'<g transform="translate({x0 + 24},{y0 + 318}) scale(0.26)">{wordmark(key, mode, 0, 0, credit=True)}</g>')
            b.append(T(x0 + 576, y0 + 318, "≈ 30 px tall: single hairline" if key == "hybrid_a" else "≈ 30 px tall",
                       12, t["text2"], LABEL, anchor="end"))
    write("wordmarks-final.svg", svg(W, H, "".join(b), "Haunts final wordmarks",
                                     "Lowercase wordmarks for A and B, light and dark, with the recap credit size."))


# ---------------------------------------------------------------------------
# Theme picker (Settings -> Appearance)
# ---------------------------------------------------------------------------

THEMES_UI = [("Warm", "Cream and plum, with serif headlines.", "hybrid_a"),
             ("Mono", "Black and white, with typewriter details.", "hybrid_b"),
             ("Retro", "Styled like a website from the early 2000s.", "homepage")]


def preview(theme, mode, w, h_crop):
    """A live preview: the real theme's home screen rendered on SAMPLE content (never the user's
    own headline, which HEAD-13 keeps to the home screen), cropped to its top part."""
    s = w / 390
    cl = uid("pv")
    if theme == "homepage":
        inner = f'<g transform="translate(-8,-8) scale(1.04)">{r1_phone("homepage", mode, "line")}</g>'
    else:
        inner = content(theme, mode, "line")
    return (f'<clipPath id="{cl}"><rect width="{w}" height="{h_crop}" rx="12"/></clipPath>'
            f'<g clip-path="url(#{cl})"><g transform="scale({s:.4f})">{inner}</g></g>')


def check_badge(cx, cy, t):
    return (f'<circle cx="{cx}" cy="{cy}" r="13" fill="{t["primary"]}" stroke="{t["surface"]}" stroke-width="2.5"/>'
            f'<path d="M{cx - 6},{cy} l4,4 l8,-8" fill="none" stroke="{t["on_primary"]}" stroke-width="2.4" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def segmented(t, x, y, w, sel=0):
    labels = ["Match phone", "Light", "Dark"]
    seg = w / 3
    g = [f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="12" fill="{t["bg"]}" stroke="{t["outline"]}" stroke-width="1.2"/>']
    for i, lab in enumerate(labels):
        if i == sel:
            g.append(f'<rect x="{x + i * seg + 3}" y="{y + 3}" width="{seg - 6}" height="38" rx="9" fill="{t["surface"]}" '
                     f'stroke="{t["primary"]}" stroke-width="2"/>')
        g.append(T(x + i * seg + seg / 2, y + 28, lab, 14, t["text"], INTER, 700 if i == sel else 500, anchor="middle"))
    return "".join(g)


def picker_screen(key, mode, selected, large=False):
    t = HYBRIDS[key][mode]
    g = [f'<rect width="390" height="844" fill="{t["bg"]}"/>', status_bar(t, INTER),
         f'<path d="M24,70 l-8,8 l8,8" fill="none" stroke="{t["primary"]}" stroke-width="2.2" stroke-linecap="round"/>',
         T(36, 84, "Settings", 16, t["primary"], INTER, 500),
         T(16, 132, "Appearance", 34 if not large else 40, t["text"], NEWS, 600)]
    if not large:
        g.append(T(16, 172, "Theme", 17, t["text"], INTER, 600))
        w, gap, top, crop = 110, 14, 186, 190
        for i, (name, desc, theme) in enumerate(THEMES_UI):
            x = 16 + i * (w + gap)
            sel = i == selected
            g.append(f'<rect x="{x - 4}" y="{top - 4}" width="{w + 8}" height="{crop + 8}" rx="15" fill="none" '
                     f'stroke="{t["primary"] if sel else t["outline"]}" stroke-width="{3 if sel else 1}"/>')
            g.append(f'<g transform="translate({x},{top})">{preview(theme, mode, w, crop)}</g>')
            if sel:
                g.append(check_badge(x + w - 6, top + 6, t))
            g.append(T(x, top + crop + 30, name, 16, t["text"], INTER, 700 if sel else 600))
            g.append(TL(x, top + crop + 50, wrap(desc, w, 12.5, INTER), 12.5, 17, t["text2"], INTER))
        y = top + crop + 118
        g.append(T(16, y, "Light or dark", 17, t["text"], INTER, 600))
        g.append(segmented(t, 16, y + 14, 358))
        body = ("Themes change how Haunts looks, never what it does. Your journal, headlines and settings "
                "stay exactly as they are.")
        g.append(TL(16, y + 92, wrap(body, 350, 14, INTER), 14, 20, t["text2"], INTER))
    else:
        g.append(T(16, 184, "Theme", 24, t["text"], INTER, 600))
        y = 204
        for i, (name, desc, theme) in enumerate(THEMES_UI):
            sel = i == selected
            rh = 150
            g.append(f'<rect x="16" y="{y}" width="358" height="{rh}" rx="16" fill="{t["surface"]}" '
                     f'stroke="{t["primary"] if sel else t["outline"]}" stroke-width="{3 if sel else 1}"/>')
            g.append(f'<g transform="translate(28,{y + 12})">{preview(theme, mode, 72, 126)}</g>')
            g.append(T(116, y + 40, name, 26, t["text"], INTER, 700))
            g.append(TL(116, y + 72, wrap(desc, 240, 19, INTER), 19, 25, t["text2"], INTER))
            if sel:
                g.append(check_badge(346, y + 30, t))
            y += rh + 12
        g.append(T(16, y + 30, "Light or dark: Match phone", 24, t["text"], INTER, 600))
    return "".join(g)


def picker_phone(key, mode, selected, large=False):
    cid, clip = uid("pick"), uid("pc")
    # Settings tab selected: reuse the round-2 bar, with the pill moved to the fourth tab
    bar = tab_bar(key, mode, "glass", cid)
    t = HYBRIDS[key][mode]
    x, y, w = BAR["x"], BAR["y"], BAR["w"]
    # redraw the tab items with Settings selected over the round-2 bar's items
    items = [f'<rect x="{x + 6}" y="{y + 4}" width="{w - 12}" height="56" rx="28" fill="{t["glass_tint"]}"/>']
    from generate_concepts import CONTENT
    for i, lab in enumerate(CONTENT["tabs"]):
        cx = x + w * (i + 0.5) / 4
        if i == 3:
            items.append(f'<rect x="{cx - 40}" y="{y + 6}" width="80" height="52" rx="26" fill="{t["primary"]}"/>')
            c = t["on_primary"]
        else:
            c = t["tab_idle"]
        items.append(tab_icon(lab, cx, y + 24, c))
        items.append(T(cx, y + 50, lab, 11.5, c, INTER, 600, anchor="middle"))
    return (f'<defs><g id="{cid}">{picker_screen(key, mode, selected, large)}</g>'
            f'<clipPath id="{clip}"><rect width="390" height="844" rx="52"/></clipPath></defs>'
            f'<g clip-path="url(#{clip})"><use href="#{cid}"/>{bar}{"".join(items)}</g>'
            f'<rect x="-1" y="-1" width="392" height="846" rx="53" fill="none" stroke="#0B0B0C" stroke-width="10"/>'
            f'<rect x="140" y="11" width="110" height="30" rx="15" fill="#0B0B0C"/>')


def write_picker():
    W, H = 1420, 1120
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "Theme picker: Settings → Appearance", 26, "#111", LABEL, 700),
         T(40, 70, "Live previews render each real theme on sample content (never the user's own headline: HEAD-13). "
                   "One tap applies; no confirmation; nothing locked, promoted or marked NEW.", 14, "#444", LABEL),
         T(60, 104, "1. Warm theme in use, light", 16, "#111", LABEL, 700),
         f'<g transform="translate(60,120)">{picker_phone("hybrid_a", "light", 0)}</g>',
         T(510, 104, "2. Mono theme in use, dark", 16, "#111", LABEL, 700),
         f'<g transform="translate(510,120)">{picker_phone("hybrid_b", "dark", 1)}</g>',
         T(960, 104, "3. Largest text size: one column", 16, "#111", LABEL, 700),
         f'<g transform="translate(960,120)">{picker_phone("hybrid_a", "light", 0, large=True)}</g>']
    notes = ["Screen reader: the three themes are one radio group. Each is a single element, e.g.",
             "\"Warm. Cream and plum, with serif headlines. Selected. 1 of 3.\" Previews are hidden from assistive",
             "technology (the name and description carry the meaning). Selection is shown by a thick border and a",
             "check mark, never colour alone (A11Y-2). Every target ≥ 44 pt (A11Y-5). Switching cross-fades in",
             "200 ms, or instantly under Reduce Motion. The choice persists and survives export and restore (THEME-5)."]
    for i, n in enumerate(notes):
        b.append(T(60, 1000 + i * 20, n, 13, "#333", LABEL))
    write("theme-picker.svg", svg(W, H, "".join(b), "Haunts theme picker",
                                  "Settings, Appearance: three theme cards with live previews, light and dark, "
                                  "and a single-column layout at the largest text size."))


def write_app_icon_setting():
    """Only if the CEO chooses option 2 (finalise.md section 4): a separate App icon setting."""
    t = A_L
    W, H = 960, 1030
    g = [f'<rect width="390" height="844" fill="{t["bg"]}"/>', status_bar(t, INTER),
         f'<path d="M24,70 l-8,8 l8,8" fill="none" stroke="{t["primary"]}" stroke-width="2.2" stroke-linecap="round"/>',
         T(36, 84, "Appearance", 16, t["primary"], INTER, 500),
         T(16, 132, "App icon", 34, t["text"], NEWS, 600)]
    rows = [("Plum", "The h on plum, with a double rule.", a_masthead, True),
            ("Cream", "The h with a full stop.", a_fullstop, False),
            ("Black", "The h on black, with an orange bar.", b_bar, False)]
    y = 166
    for name, desc, fn, sel in rows:
        g.append(f'<rect x="16" y="{y}" width="358" height="96" rx="20" fill="{t["surface"]}" '
                 f'stroke="{t["primary"] if sel else t["outline"]}" stroke-width="{3 if sel else 1}"/>')
        g.append(icon_tile(fn, 32, y + 18, 60, cid=uid("ai")))
        g.append(T(110, y + 42, name, 17, t["text"], INTER, 700 if sel else 600))
        g.append(T(110, y + 64, desc, 13, t["text2"], INTER))
        if sel:
            g.append(check_badge(346, y + 48, t))
        y += 108
    body = "The icon on your home screen. Changing it does not change the theme, and the theme never changes it."
    g.append(TL(16, y + 16, wrap(body, 350, 14, INTER), 14, 20, t["text2"], INTER))
    cl = uid("ap")
    phone = (f'<clipPath id="{cl}"><rect width="390" height="844" rx="52"/></clipPath><g clip-path="url(#{cl})">{"".join(g)}</g>'
             f'<rect x="-1" y="-1" width="392" height="846" rx="53" fill="none" stroke="#0B0B0C" stroke-width="10"/>'
             f'<rect x="140" y="11" width="110" height="30" rx="15" fill="#0B0B0C"/>')
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "Option 2 only: a separate App icon setting", 26, "#111", LABEL, 700),
         T(40, 70, "Shown for the CEO's decision (finalise.md §4), not adopted. Default = the store icon. "
                   "Every icon needs dark, clear and tinted variants (Apple HIG).", 14, "#444", LABEL),
         f'<g transform="translate(60,110)">{phone}</g>']
    notes = ["Independent of the theme, in both directions.",
             "Draft copy. Icon names describe what people see.",
             "Radio group for screen readers, as in the theme picker.",
             "No icon is locked, earned or promoted (THEME-6 applies).",
             "iOS may show a system notice when the icon changes [K];",
             "that is expected, and the CTO confirms the behaviour.",
             "Never a disguise: Apple says to avoid an icon",
             "'someone might mistake for another app' [E]."]
    for i, n in enumerate(notes):
        b.append(T(500, 160 + i * 26, n, 14, "#333", LABEL))
    write("app-icon-setting.svg", svg(W, H, "".join(b), "Haunts app icon setting (option 2)",
                                      "A separate, user-chosen app icon setting with three icons, independent of theme."))


# ---------------------------------------------------------------------------
# Mono's typed headline ("like a console"), as a frame sequence
# ---------------------------------------------------------------------------

FACTS = ["Three years of The Brass Kettle. Your first visit was in March 2023.",
         "You rate cafés 4.2 and restaurants 3.8, across 14 and 9 rated visits."]
MONO_W = 0.602  # advance of a monospace glyph, as a fraction of font size (Plex Mono / Menlo)


def typed_frame(t, text, typed_chars, cursor, controls=True, paused=False):
    """One frame of the typed headline, 358 x 150. cursor: 'on' | 'off' | 'none'."""
    X, W, fs, lh = 0, 358, 16, 23
    per_line = int((W - 70) / (fs * MONO_W))
    shown = text[:typed_chars]
    lines = wrap(shown, (W - 70), fs, MONO) if shown else [""]
    # wrap() is approximate; recompute with exact monospace breaking
    lines, cur = [], ""
    for word in shown.split(" "):
        cand = (cur + " " + word).strip() if cur else word
        if len(cand) <= per_line:
            cur = cand
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    g = [f'<rect x="{X}" y="0" width="{W}" height="150" rx="6" fill="{t["surface"]}" stroke="{t["outline"]}" stroke-width="1"/>',
         T(X + 14, 26, "> from your journal", 12.5, t["kicker"], MONO, 500)]
    for i, ln in enumerate(lines):
        g.append(T(X + 14, 54 + i * lh, ln, fs, t["text"], MONO, 500))
    if cursor == "on":
        last = lines[-1]
        cx = X + 14 + len(last) * fs * MONO_W + (2 if last else 0)
        cy = 54 + (len(lines) - 1) * lh + 3
        g.append(f'<rect x="{cx:.1f}" y="{cy}" width="{fs * MONO_W:.1f}" height="3" fill="{t["accent"]}"/>')
    if cursor == "off":  # blink phase with the underscore hidden: draw a faint ghost so the frame reads
        last = lines[-1]
        cx = X + 14 + len(last) * fs * MONO_W + (2 if last else 0)
        cy = 54 + (len(lines) - 1) * lh + 3
        g.append(f'<rect x="{cx:.1f}" y="{cy}" width="{fs * MONO_W:.1f}" height="3" fill="none" stroke="{t["accent"]}" '
                 f'stroke-width="0.8" stroke-dasharray="2 2"/>')
    if controls:
        g.append(f'<rect x="{W - 84}" y="10" width="34" height="34" rx="4" fill="none" stroke="{t["outline"]}" stroke-width="1.2"/>')
        if paused:  # the control now offers Play
            g.append(f'<path d="M{W - 72},19 L{W - 58},27 L{W - 72},35 Z" fill="{t["text"]}"/>')
        else:
            g.append(f'<rect x="{W - 72}" y="20" width="4" height="14" fill="{t["text"]}"/>'
                     f'<rect x="{W - 64}" y="20" width="4" height="14" fill="{t["text"]}"/>')
        g.append(f'<circle cx="{W - 24}" cy="27" r="17" fill="none" stroke="{t["outline"]}" stroke-width="1.2"/>'
                 + "".join(f'<circle cx="{W - 24 + d}" cy="27" r="1.8" fill="{t["text"]}"/>' for d in (-6, 0, 6)))
    return "".join(g)


def write_typed():
    frames = [("1. Typing", "0–2.8 s · 25 chars/s, cursor steady", FACTS[0], 30, "on", False),
              ("2. Held", "2.8–6.8 s · 4 s, cursor blinks (1 s)", FACTS[0], len(FACTS[0]), "on", False),
              ("   (blink off phase)", "cursor hidden 0.5 s of each 1 s", FACTS[0], len(FACTS[0]), "off", False),
              ("3. Next", "6.8 s · clears at once, types next", FACTS[1], 26, "on", False),
              ("4. Rest", "end of pass · full sentence, keeps blinking", FACTS[1], len(FACTS[1]), "on", False),
              ("5. Paused", "pause stops typing and blinking", FACTS[1], len(FACTS[1]), "on", True)]
    W, H = 2200, 920
    b = [f'<rect width="{W}" height="{H}" fill="#E9E9E6"/>',
         T(40, 44, "Mono's typed headline (D45): typed in, held, then the next; the cursor keeps blinking", 24,
           "#111", LABEL, 700),
         T(40, 70, "Mono's styling of the moving headline appearance, only if the user chose it (HEAD-2). One pass per open, "
                   "then it rests on a full sentence. The pause control stops both typing and blinking, and stays paused.",
           14, "#444", LABEL)]
    for r, mode in enumerate(("light", "dark")):
        t = HYBRIDS["hybrid_b"][mode]
        y0 = 110 + r * 300
        b.append(T(40, y0 + 90, mode.capitalize(), 18, "#111", LABEL, 700))
        for c, (lab, sub, text, n, cur, paused) in enumerate(frames):
            x0 = 150 + c * 342
            b.append(T(x0, y0 + 12, lab, 15, "#111", LABEL, 700))
            b.append(T(x0, y0 + 32, sub, 12, "#444", LABEL))
            bg = f'<rect x="-10" y="-10" width="358" height="170" rx="12" fill="{t["bg"]}"/>'
            b.append(f'<g transform="translate({x0 + 10},{y0 + 52}) scale(0.9)">{bg}'
                     f'{typed_frame(t, text, n, cur, paused=paused)}</g>')
    # timeline
    ty = 730
    b.append(T(40, ty - 20, "One open, one pass, at most 3 facts (2 shown). Proposed timings, to be signed off on a device:",
               14, "#111", LABEL, 700))
    segs = [(0, 2.8, "type fact 1 (steady)", "#555555"), (2.8, 6.8, "hold 4 s (blinking)", "#C2410C"),
            (6.8, 9.6, "type fact 2 (steady)", "#555555"), (9.6, 13.6, "hold 4 s (blinking)", "#C2410C"),
            (13.6, 19.5, "rest on full sentence, blinking until paused or off screen", "#E08A5C")]
    scale = 100
    for a, z, lab, col in segs:
        b.append(f'<rect x="{150 + a * scale}" y="{ty}" width="{(z - a) * scale - 3}" height="26" rx="4" fill="{col}"/>')
        b.append(T(150 + a * scale + 6, ty + 46, lab, 12, "#333", LABEL))
        b.append(T(150 + a * scale, ty - 4, f"{a:g} s", 11, "#666", LABEL))
    b.append(T(40, 850, "Screen reader, Reduce Motion or Remove animations: the full sentence at once with a steady cursor "
                        "(HEAD-10, HEAD-11); read once, as a whole, when focused.", 13, "#333", LABEL))
    b.append(T(40, 870, "No sound, no variation in typing speed, no 'new' marker. Blink period 1.0 s (0.5 s on, 0.5 s off) = one "
                        "flash a second, a third of SC 2.3.1's limit. Blinking over 5 s is covered by the pause control "
                        "(SC 2.2.2).", 13, "#333", LABEL))
    write("b-typed-headline.svg", svg(W, H, "".join(b), "Haunts Mono typed headline",
                                      "Frame sequence of Mono's typed headline, light and dark, with a timing diagram."))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write_icons()
    write_wordmarks()
    write_picker()
    write_app_icon_setting()
    write_typed()
    print("written:", sorted(os.listdir(OUT)))

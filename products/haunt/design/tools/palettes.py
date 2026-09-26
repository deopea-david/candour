"""Haunts brand directions and themes: colour tokens.

Single source for every hex value in brand-directions.md, themes.md and the
concept SVGs. contrast.py measures every pair listed here with the WCAG 2.x
relative-luminance formula, so a stranger can re-derive every ratio.

Concept work only (D38). Nothing here is adopted.
"""

# Token meanings (identical across every direction and theme):
#   bg          page background
#   surface     cards, rows, sheets
#   text        primary text
#   text2       secondary text (dates, durations, places)
#   primary     links, primary buttons, selected tab
#   on_primary  text on a primary-filled button
#   accent      the brand's signal colour (mark, headline rule) - decorative unless listed as text
#   kicker      the headline kicker label ("From your journal") - text
#   outline     borders of interactive components (inputs, outline buttons) - UI, 3:1
#   unconfirmed text colour of the "Unconfirmed" state label (always also a word + dashed outline)
#   focus       focus ring - UI, 3:1
#   star        rating star glyphs - graphical object, 3:1 (rating is always also text "4/5")
#   divider     hairline dividers - decorative, no contrast requirement

DIRECTIONS = {
    "almanac": {
        "name": "Almanac",
        "light": dict(bg="#F6F2EA", surface="#FFFDF8", text="#1C2127", text2="#545B64",
                      primary="#1F4E79", on_primary="#FFFFFF", accent="#B3412A",
                      kicker="#A63A24", outline="#8A8375", unconfirmed="#8A5300",
                      focus="#1F4E79", star="#A63A24", divider="#E4DCCB"),
        "dark": dict(bg="#16181B", surface="#202328", text="#EDE8DE", text2="#A9A398",
                     primary="#8DB8E8", on_primary="#0E1A26", accent="#E58A6F",
                     kicker="#E8957C", outline="#7B766D", unconfirmed="#E0B25A",
                     focus="#8DB8E8", star="#E8957C", divider="#33373D"),
    },
    "doorway": {
        "name": "Doorway",
        "light": dict(bg="#FFF8F1", surface="#FFFFFF", text="#241B2F", text2="#5C5266",
                      primary="#5B2A86", on_primary="#FFFFFF", accent="#F2A65A",
                      kicker="#5B2A86", outline="#8C7F99", unconfirmed="#9A4D00",
                      focus="#5B2A86", star="#B45309", divider="#EDE3F3",
                      teal="#0F6E6A", apricot_fill="#F2A65A", on_apricot="#241B2F"),
        "dark": dict(bg="#1A1422", surface="#251D30", text="#F6EFE8", text2="#B9AFC4",
                     primary="#C9A7F0", on_primary="#24123A", accent="#F5B77A",
                     kicker="#F5B77A", outline="#7E7190", unconfirmed="#F5B77A",
                     focus="#C9A7F0", star="#F5B77A", divider="#352A44",
                     teal="#5CC8C0", apricot_fill="#F5B77A", on_apricot="#241B2F"),
    },
    "ledger": {
        "name": "Ledger",
        "light": dict(bg="#FAFAF8", surface="#FFFFFF", text="#111111", text2="#555555",
                      primary="#111111", on_primary="#FFFFFF", accent="#C2410C",
                      kicker="#B93D0B", outline="#767676", unconfirmed="#B93D0B",
                      focus="#C2410C", star="#111111", divider="#E6E6E3"),
        "dark": dict(bg="#0F0F10", surface="#1A1A1C", text="#F2F2F0", text2="#A3A3A0",
                     primary="#F2F2F0", on_primary="#111111", accent="#FB923C",
                     kicker="#FB923C", outline="#76767A", unconfirmed="#FB923C",
                     focus="#FB923C", star="#F2F2F0", divider="#2A2A2D"),
    },
    "contour": {
        "name": "Contour",
        "light": dict(bg="#F3F5F0", surface="#FFFFFF", text="#1D2A24", text2="#4F5E57",
                      primary="#2E6B4A", on_primary="#FFFFFF", accent="#9A6B3F",
                      kicker="#86592F", outline="#7D8A83", unconfirmed="#86592F",
                      focus="#2C6E8F", star="#86592F", divider="#DDE4DC",
                      water="#2C6E8F"),
        "dark": dict(bg="#121815", surface="#1B2420", text="#E6EDE8", text2="#9FB0A7",
                     primary="#7CC39A", on_primary="#0E1F16", accent="#D4A373",
                     kicker="#D4A373", outline="#6F7F77", unconfirmed="#D4A373",
                     focus="#7FC0DE", star="#D4A373", divider="#2B3631",
                     water="#7FC0DE"),
    },
}

# Themes that are not brand directions.
THEMES = {
    "homepage": {
        "name": "Homepage (retro, c. 2001-2004)",
        "light": dict(bg="#DCE4F0", surface="#FFFFFF", text="#1A1A1A", text2="#4A4A4A",
                      primary="#0033CC", on_primary="#FFFFFF", accent="#FF9933",
                      kicker="#1A1A1A", outline="#5E7FA3", unconfirmed="#A33A00",
                      focus="#0033CC", star="#B36B00", divider="#B8C7DA",
                      title_top="#16336B", title_bottom="#2D5AA0", on_title="#FFFFFF",
                      box_title="#D3DFF0", box_title_top="#FFFFFF", on_box_title="#16336B",
                      tab="#F4B860", on_tab="#1A1A1A", tab_idle="#E6ECF5",
                      ticker_bg="#FFFFCC", on_ticker="#1A1A1A",
                      button_face="#ECE9D8", on_button="#1A1A1A", button_edge="#716F64"),
        "dark": dict(bg="#000022", surface="#0B0B33", text="#E8E8E8", text2="#B4B4C8",
                     primary="#66CCFF", on_primary="#000022", accent="#FF9933",
                     kicker="#FFCC66", outline="#6D7FB0", unconfirmed="#FFB870",
                     focus="#66CCFF", star="#FFCC66", divider="#2A2A5A",
                     title_top="#1B1B55", title_bottom="#33337A", on_title="#FFFFFF",
                     box_title="#1B1B55", box_title_top="#2E2E78", on_box_title="#FFCC66",
                     tab="#FFCC66", on_tab="#000022", tab_idle="#16164A",
                     ticker_bg="#1A1A00", on_ticker="#FFFF99",
                     button_face="#2B2B5E", on_button="#E8E8E8", button_edge="#8A8AC0"),
    },
}

# (fg token, bg token, kind, what it is). kind: text 4.5, large 3.0, ui 3.0
STANDARD_PAIRS = [
    ("text", "bg", "text", "Body text on page"),
    ("text", "surface", "text", "Body text on row/card"),
    ("text2", "bg", "text", "Secondary text on page"),
    ("text2", "surface", "text", "Secondary text on row/card"),
    ("primary", "bg", "text", "Link / tab label on page"),
    ("primary", "surface", "text", "Link on row/card"),
    ("on_primary", "primary", "text", "Label on primary button"),
    ("kicker", "surface", "text", "Headline kicker on headline surface"),
    ("kicker", "bg", "text", "Headline kicker on page"),
    ("unconfirmed", "surface", "text", "'Unconfirmed' state label"),
    ("outline", "surface", "ui", "Control border on row/card"),
    ("outline", "bg", "ui", "Control border on page"),
    ("focus", "surface", "ui", "Focus ring on row/card"),
    ("focus", "bg", "ui", "Focus ring on page"),
    ("star", "surface", "ui", "Rating stars (also shown as text 4/5)"),
]

EXTRA_PAIRS = {
    "doorway": [
        ("on_apricot", "apricot_fill", "text", "Text on apricot chip / headline card"),
        ("teal", "surface", "text", "Teal secondary link on card"),
    ],
    "contour": [
        ("water", "surface", "text", "Water-blue link on card"),
    ],
    "homepage": [
        ("on_title", "title_bottom", "text", "Title-bar text on lighter end of gradient"),
        ("on_title", "title_top", "text", "Title-bar text on darker end of gradient"),
        ("on_box_title", "box_title", "text", "Box heading on box title strip (lower end of gradient)"),
        ("on_box_title", "box_title_top", "text", "Box heading on box title strip (upper end of gradient)"),        ("on_tab", "tab", "text", "Selected tab label"),
        ("primary", "tab_idle", "text", "Idle tab label (link colour)"),
        ("on_ticker", "ticker_bg", "text", "Ticker text on ticker strip"),
        ("on_button", "button_face", "text", "Bevel button label"),
        ("button_edge", "surface", "ui", "Bevel button edge on content"),
        ("button_edge", "button_face", "ui", "Bevel button edge on its own face"),
    ],
}

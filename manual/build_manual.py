#!/usr/bin/env python3
"""Build the TypixNode (CyberFly) bilingual manual (HTML) from a single keymap source.

Layout & behaviours decoded from the ZMK shield:
  app/boards/shields/cyberfly_keyboard/cyberfly_keyboard.keymap  (+ .overlay / .conf)

Run:  python3 build_manual.py    ->  manual.html
Then: weasyprint manual.html ../TypixNode_Manual.pdf
"""

G = "glyph"

# Each key: (main, sub, fn, width, css)
#   fn : None | str | {"cn":..,"en":..}   (None = transparent on Fn layer)
#   css: extra classes -> color (sq/tri/...), "gap", "tapd" (tap-dance dots),
#                         "ble" (cyan highlight on Fn view), "sm", "fnk", G
ROWS = [
    # Row 1 — function / symbol row
    [
        ("ESC", None, {"cn": "USB/蓝牙", "en": "USB/BLE"}, 3, "sm tapd ble"),
        ("■", "F1", "BT 1", 3, "sq ble " + G),
        ("▲", "F2", "BT 2", 3, "tri ble " + G),
        ("✕", "F3", "BT 3", 3, "crs ble " + G),
        ("", None, None, 2, "gap"),
        ("●", "F4", "BT 4", 3, "cir ble " + G),
        ("♣", "F5", "BT 5", 3, "clb ble " + G),
        ("◆", "F6", "BT 6", 3, "dia ble " + G),
        ("⌫", None, "DEL", 3, G),
    ],
    # Row 2 — number row
    [
        ("`", "~", None, 2, ""),
        ("1", "!", "F1", 2, ""), ("2", "@", "F2", 2, ""), ("3", "#", "F3", 2, ""),
        ("4", "$", "F4", 2, ""), ("5", "%", "F5", 2, ""), ("6", "^", "F6", 2, ""),
        ("7", "&", "F7", 2, ""), ("8", "*", "F8", 2, ""), ("9", "(", "F9", 2, ""),
        ("0", ")", "F10", 2, ""), ("-", "_", "F11", 2, ""), ("=", "+", "F12", 2, ""),
    ],
    # Row 3
    [
        ("TAB", None, None, 2, "sm"),
        ("Q", None, {"cn": "截图", "en": "Shot"}, 2, ""),
        ("W", None, None, 2, ""), ("E", None, None, 2, ""), ("R", None, None, 2, ""),
        ("T", None, None, 2, ""), ("Y", None, None, 2, ""), ("U", None, None, 2, ""),
        ("I", None, None, 2, ""), ("O", None, None, 2, ""), ("P", None, None, 2, ""),
        ("[", "{", None, 2, ""),
        ("]", "}", {"cn": "外接电源", "en": "Ext Pwr"}, 2, ""),
    ],
    # Row 4
    [
        ("Fn", None, None, 2, "sm fnk"),
        ("A", None, {"cn": "全选复制", "en": "Copy"}, 2, ""),
        ("S", None, None, 2, ""), ("D", None, None, 2, ""), ("F", None, None, 2, ""),
        ("G", None, None, 2, ""), ("H", None, None, 2, ""), ("J", None, None, 2, ""),
        ("K", None, None, 2, ""), ("L", None, None, 2, ""),
        (";", ":", None, 2, ""), ("'", '"', None, 2, ""),
        ("↵", None, {"cn": "清蓝牙", "en": "BT Clr"}, 2, "ble " + G),
    ],
    # Row 5
    [
        ("⇧", None, None, 2, "tapd " + G),
        ("Z", None, None, 2, ""), ("X", None, None, 2, ""),
        ("C", None, {"cn": "重置", "en": "Reset"}, 2, ""),
        ("V", None, None, 2, ""),
        ("B", None, {"cn": "刷机", "en": "Boot"}, 2, ""),
        ("N", None, None, 2, ""),
        ("M", None, "=>", 2, ""),
        (",", "<", None, 2, ""), (".", ">", None, 2, ""), ("/", "?", None, 2, ""),
        ("↑", None, "PgUp", 2, G),
        ("⇧", None, {"cn": "关机", "en": "Off"}, 2, G),
    ],
    # Row 6 — bottom row
    [
        ("CTRL", None, None, 2, "sm"),
        ("GUI", None, None, 2, "sm"),
        ("ALT", None, {"cn": "飞鼠", "en": "Mouse"}, 2, "sm"),
        ("\\", "|", None, 2, ""),
        ("SPACE", None, {"cn": "背光", "en": "Light"}, 10, "sm"),
        ("ALT", None, {"cn": "飞鼠", "en": "Mouse"}, 2, "sm"),
        ("←", None, "Home", 2, G),
        ("↓", None, "PgDn", 2, G),
        ("→", None, "End", 2, G),
    ],
]


def _loc(v, lang):
    if isinstance(v, dict):
        return v.get(lang, v.get("en", ""))
    return v


def render_keymap(mode="base", lang="cn"):
    out = ['<div class="kbd">']
    for row in ROWS:
        out.append('<div class="krow">')
        for (main, sub, fn, w, css) in row:
            if "gap" in css:
                out.append(f'<div class="kgap" style="grid-column:span {w}"></div>')
                continue
            classes = ["key"]
            if w == 3:
                classes.append("k15")
            elif w == 10:
                classes.append("kspace")
            is_glyph = G in css
            small = "sm" in css

            if mode == "fn":
                if fn is None:
                    classes.append("dim")
                    body = _keyface(main, None, is_glyph, small)
                else:
                    classes.append("act2" if "ble" in css else "act")
                    body = f'<span class="main sm">{_esc(_loc(fn, lang))}</span>'
            else:  # base
                if "tapd" in css:
                    classes.append("tapd")
                if "fnk" in css:
                    classes.append("fnk")
                body = _keyface(main, sub, is_glyph, small)

            out.append(f'<div class="{" ".join(classes)}" style="grid-column:span {w}">{body}</div>')
        out.append('</div>')
    out.append('</div>')
    return "\n".join(out)


def _keyface(main, sub, is_glyph, small):
    parts = []
    if sub:
        parts.append(f'<span class="sub">{_esc(sub)}</span>')
    if is_glyph:
        parts.append(f'<span class="glyph">{_esc(main)}</span>')
    else:
        parts.append(f'<span class="main{" sm" if small else ""}">{_esc(main)}</span>')
    return "".join(parts)


def _esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    html = TEMPLATE.format(
        base_cn=render_keymap("base", "cn"),
        fn_cn=render_keymap("fn", "cn"),
        base_en=render_keymap("base", "en"),
        fn_en=render_keymap("fn", "en"),
    )
    with open("manual.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote manual.html")


from manual_content import TEMPLATE  # noqa: E402

if __name__ == "__main__":
    main()

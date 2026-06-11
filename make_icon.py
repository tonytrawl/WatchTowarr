#!/usr/bin/env python3
"""
make_icon.py: generate GuardTowarr's icon.ico from the watchtower design.

Draws the same gold watchtower used by the in-app favicon and tray icon, at
several resolutions, and saves them into a single multi-size icon.ico that
Windows uses for the .exe (Explorer, taskbar, window title bar).

Run once before building:  python make_icon.py
build.bat does this for you automatically.
"""

from PIL import Image, ImageDraw

GOLD = (229, 160, 13, 255)
GOLD_HI = (245, 197, 24, 255)
DARK = (21, 23, 25, 255)
SIZES = [16, 32, 48, 64, 128, 256]


def draw_icon(size):
    """Draw the watchtower at the given square size using proportional coords."""
    # Supersample for clean edges, then downscale.
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def px(frac):  # fraction (0..1) of the canvas -> pixels
        return frac * s

    # Rounded gold tile with a subtle vertical gradient (gold -> lighter gold).
    radius = px(0.22)
    # gradient by drawing horizontal bands
    for y in range(s):
        t = y / s
        r = int(GOLD[0] + (GOLD_HI[0] - GOLD[0]) * t)
        g = int(GOLD[1] + (GOLD_HI[1] - GOLD[1]) * t)
        b = int(GOLD[2] + (GOLD_HI[2] - GOLD[2]) * t)
        d.line([(0, y), (s, y)], fill=(r, g, b, 255))
    # mask to rounded rect
    mask = Image.new("L", (s, s), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([px(0.03), px(0.03), px(0.97), px(0.97)], radius=radius, fill=255)
    tile = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    tile.paste(img, (0, 0), mask)

    # Watchtower in dark, matching the tray/favicon geometry (24x24 viewBox scaled).
    d2 = ImageDraw.Draw(tile)
    def vb(x, y):  # 24-unit viewBox coord -> canvas px
        return (px(x / 24.0), px(y / 24.0))
    # roof (triangle)
    d2.polygon([vb(12, 3.2), vb(16.2, 7.2), vb(7.8, 7.2)], fill=DARK)
    # tower body (slight taper via polygon)
    d2.polygon([vb(9, 8), vb(15, 8), vb(14.5, 19), vb(9.5, 19)], fill=DARK)
    # base
    d2.rounded_rectangle([*vb(7.6, 18.4), *vb(16.4, 20.6)], radius=px(0.02), fill=DARK)
    # watch slit (gold notch in the tower)
    d2.line([vb(12, 11), vb(12, 14.5)], fill=GOLD, width=max(1, int(px(0.012))))

    return tile.resize((size, size), Image.LANCZOS)


def main():
    images = [draw_icon(sz) for sz in SIZES]
    # Save as multi-resolution .ico (largest first; Pillow embeds all sizes).
    images[-1].save(
        "icon.ico",
        format="ICO",
        sizes=[(sz, sz) for sz in SIZES],
        append_images=images[:-1],
    )
    print("[*] Wrote icon.ico with sizes:", ", ".join(f"{s}x{s}" for s in SIZES))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Tile playing card images onto A4 pages for printing.

- Poker card size: 63mm x 88mm
- 3x3 grid per A4 page = 9 cards per page
- 2mm gutter between cards (where cut marks live)
- L-shaped cut marks at every card corner

Accepts PNG or SVG files. PNGs are placed directly (use this mode when
cards have been pre-exported from Inkscape for perfect rendering). SVGs
are rendered via cairosvg as a fallback.

Usage:
    python tile_cards.py cards.txt output.pdf --img-dir ./Cards-png

Config file format (one entry per line):
    Petty-Cash.png 3
    draw_cardback.png 26
    # comments start with hash
    # filename alone defaults to quantity 1
"""
import argparse
import io
import re
from pathlib import Path

import cairosvg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader


# --- Layout constants ---
CARD_W = 63 * mm
CARD_H = 88 * mm
COLS = 3
ROWS = 3
PER_PAGE = COLS * ROWS
GUTTER = 2 * mm        # space between cards (cut marks live here)

# Cut mark settings
MARK_LEN = 3 * mm      # length of each cut mark line
MARK_WIDTH = 0.3       # stroke width in points

PAGE_W, PAGE_H = A4

# Render DPI — overridden by --dpi flag at runtime
DPI = 300


def compute_grid_origin():
    """Return (x0, y0) bottom-left of the grid, centred on the page."""
    grid_w = COLS * CARD_W + (COLS - 1) * GUTTER
    grid_h = ROWS * CARD_H + (ROWS - 1) * GUTTER
    return (PAGE_W - grid_w) / 2, (PAGE_H - grid_h) / 2


def parse_config(config_path):
    """Read 'filename quantity' lines. Bare filename = qty 1.
    Accepts whitespace, ':', '=', or ',' as the separator.
    '#' starts a comment (whole-line or inline)."""
    # Match: <filename> <separator(s)> <integer> at end of line
    pattern = re.compile(r"^(.*?)[\s:=,]+(\d+)\s*$")
    items = []
    with open(config_path) as f:
        for line_num, raw in enumerate(f, 1):
            line = raw.split("#", 1)[0].strip()  # strip inline + whole-line comments
            if not line:
                continue
            m = pattern.match(line)
            if m:
                filename = m.group(1).strip().rstrip(":=,").strip()
                qty = int(m.group(2))
                items.append((filename, qty))
            else:
                items.append((line, 1))
    return items


def expand_cards(items, svg_dir):
    """Turn [(filename, qty), ...] into a flat list of SVG paths."""
    svg_dir = Path(svg_dir)
    cards = []
    for filename, qty in items:
        path = svg_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"SVG not found: {path}")
        cards.extend([path] * qty)
    return cards


def draw_cut_marks(c, x, y):
    """Draw L-shaped cut marks pointing outward at each corner of a card at (x, y)."""
    c.setLineWidth(MARK_WIDTH)
    # The marks start at the card corner and extend outward into the gutter.
    # Each corner gets two lines: one horizontal, one vertical.

    # Bottom-left
    c.line(x, y, x - MARK_LEN, y)
    c.line(x, y, x, y - MARK_LEN)
    # Bottom-right
    c.line(x + CARD_W, y, x + CARD_W + MARK_LEN, y)
    c.line(x + CARD_W, y, x + CARD_W, y - MARK_LEN)
    # Top-left
    c.line(x, y + CARD_H, x - MARK_LEN, y + CARD_H)
    c.line(x, y + CARD_H, x, y + CARD_H + MARK_LEN)
    # Top-right
    c.line(x + CARD_W, y + CARD_H, x + CARD_W + MARK_LEN, y + CARD_H)
    c.line(x + CARD_W, y + CARD_H, x + CARD_W, y + CARD_H + MARK_LEN)


def render_card(img_path):
    """Load a card image into a reportlab ImageReader.

    PNGs are loaded directly — use these when pre-exported from Inkscape
    for perfect rendering of filters, blend modes, and path text.
    SVGs fall back to cairosvg rendering.
    """
    if img_path.suffix.lower() == ".png":
        return ImageReader(str(img_path))

    # SVG fallback via cairosvg
    card_w_px = round(63 / 25.4 * DPI)
    card_h_px = round(88 / 25.4 * DPI)
    png_bytes = cairosvg.svg2png(
        url=str(img_path.resolve()),
        output_width=card_w_px,
        output_height=card_h_px,
    )
    return ImageReader(io.BytesIO(png_bytes))


def draw_card(c, img_reader, x, y):
    """Place a rendered card image at (x, y) on the canvas.

    mask='auto' preserves any transparency in the SVG rather than
    rendering it as black.
    """
    c.drawImage(img_reader, x, y, width=CARD_W, height=CARD_H, mask="auto")


def build_pdf(cards, output_path):
    # Cache rendered images — same SVG path → same PNG bytes, no need to re-render.
    cache = {}

    c = canvas.Canvas(str(output_path), pagesize=A4)
    x0, y0 = compute_grid_origin()
    unique = len(set(cards))

    for i, img_path in enumerate(cards):
        if img_path not in cache:
            print(f"  Loading {img_path.name} ({len(cache)+1}/{unique})")
            cache[img_path] = render_card(img_path)

        slot = i % PER_PAGE
        col = slot % COLS
        row = slot // COLS
        x = x0 + col * (CARD_W + GUTTER)
        y = y0 + (ROWS - 1 - row) * (CARD_H + GUTTER)

        draw_card(c, cache[img_path], x, y)
        draw_cut_marks(c, x, y)

        is_last_on_page = (slot == PER_PAGE - 1)
        is_last_card = (i == len(cards) - 1)
        if is_last_on_page and not is_last_card:
            c.showPage()

    c.save()


def main():
    global DPI
    ap = argparse.ArgumentParser(description="Tile SVG cards onto A4 pages with cut marks.")
    ap.add_argument("config", help="Config file: 'filename quantity' per line")
    ap.add_argument("output", help="Output PDF path")
    ap.add_argument("--img-dir", default=".", help="Directory containing card images (default: .)")
    ap.add_argument("--dpi", type=int, default=300, help="Render resolution (default: 300)")
    args = ap.parse_args()
    DPI = args.dpi

    items = parse_config(args.config)
    cards = expand_cards(items, args.img_dir)
    unique = len(set(str(p) for p in cards))
    pages = (len(cards) + PER_PAGE - 1) // PER_PAGE
    print(f"{len(cards)} cards ({unique} unique), {pages} A4 page(s), rendering at {DPI} DPI.")
    build_pdf(cards, args.output)
    print(f"Done → {args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Tile SVG playing cards onto A4 pages for printing.

- Poker card size: 63mm x 88mm
- 3x3 grid per A4 page = 9 cards per page
- 2mm gutter between cards (where cut marks live)
- L-shaped cut marks at every card corner

Usage:
    python tile_cards.py cards.txt output.pdf --svg-dir ./svgs

Config file format (one entry per line):
    ace_spades.svg 4
    king_hearts.svg 2
    back_red.svg 26
    # comments start with hash
    # filename alone defaults to quantity 1
"""
import argparse
from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from svglib.svglib import svg2rlg


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


def compute_grid_origin():
    """Return (x0, y0) bottom-left of the grid, centred on the page."""
    grid_w = COLS * CARD_W + (COLS - 1) * GUTTER
    grid_h = ROWS * CARD_H + (ROWS - 1) * GUTTER
    return (PAGE_W - grid_w) / 2, (PAGE_H - grid_h) / 2


def parse_config(config_path):
    """Read 'filename quantity' lines. Bare filename = qty 1. '#' starts a comment."""
    items = []
    with open(config_path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.rsplit(None, 1)
            if len(parts) == 2 and parts[1].isdigit():
                items.append((parts[0], int(parts[1])))
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


def draw_card(c, drawing, x, y):
    """Render a pre-scaled svglib Drawing at (x, y)."""
    drawing.drawOn(c, x, y)


def load_and_scale(svg_path):
    """Load SVG and scale it to exactly CARD_W x CARD_H. Cached drawings get reused."""
    d = svg2rlg(str(svg_path))
    if d is None:
        raise RuntimeError(f"svglib could not parse {svg_path}")
    sx = CARD_W / d.width
    sy = CARD_H / d.height
    d.width = CARD_W
    d.height = CARD_H
    d.scale(sx, sy)
    return d


def build_pdf(cards, output_path):
    # Cache scaled drawings so we don't re-parse the same SVG for every copy.
    cache = {}
    def get(svg_path):
        # Each Drawing instance is mutable, so re-load per use (cheap for small SVGs).
        # If perf matters, switch to a deep copy of a cached parsed drawing.
        return load_and_scale(svg_path)

    c = canvas.Canvas(str(output_path), pagesize=A4)
    x0, y0 = compute_grid_origin()

    for i, svg_path in enumerate(cards):
        slot = i % PER_PAGE
        col = slot % COLS
        row = slot // COLS
        x = x0 + col * (CARD_W + GUTTER)
        # PDF coords go bottom-up; we want row 0 at the top visually.
        y = y0 + (ROWS - 1 - row) * (CARD_H + GUTTER)

        drawing = get(svg_path)
        draw_card(c, drawing, x, y)
        draw_cut_marks(c, x, y)

        is_last_on_page = (slot == PER_PAGE - 1)
        is_last_card = (i == len(cards) - 1)
        if is_last_on_page and not is_last_card:
            c.showPage()

    c.save()


def main():
    ap = argparse.ArgumentParser(description="Tile SVG cards onto A4 pages with cut marks.")
    ap.add_argument("config", help="Config file: 'filename quantity' per line")
    ap.add_argument("output", help="Output PDF path")
    ap.add_argument("--svg-dir", default=".", help="Directory containing SVGs (default: .)")
    args = ap.parse_args()

    items = parse_config(args.config)
    cards = expand_cards(items, args.svg_dir)
    pages = (len(cards) + PER_PAGE - 1) // PER_PAGE
    print(f"{len(cards)} cards across {pages} A4 page(s) at 9 cards/page.")
    build_pdf(cards, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()

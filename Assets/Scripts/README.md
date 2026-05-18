# tile_cards

Tiles playing card images onto A4 pages for printing at poker size (63×88mm), 3×3 per page, with cut marks.

## How it works

Inkscape exports your SVGs to PNG at 300 DPI, then `tile_cards.py` places them onto A4 pages and outputs a print-ready PDF. Doing the rendering in Inkscape (rather than a third-party SVG library) means filters, blend modes, path text, and everything else renders exactly as it looks in the editor.

## Requirements

- Python 3.8+
- Inkscape (with CLI access)
- Fish shell (for the export script)

```bash
pip install reportlab cairosvg
```

## Workflow

### 1. Export PNGs from Inkscape

Run from `Scripts/`:

```fish
chmod +x process_cards.fish
./process_cards.fish
```

This reads every `.svg` from `../Cards/`, exports a 300 DPI PNG to `../Cards-png/`, and prints each filename as it goes.

### 2. Write your config file

Create or update `cards.txt` — one card per line, filename then quantity. Bare filename defaults to quantity 1. Lines starting with `#` are comments.

```
# Fronts
Petty-Cash.png 3
Hostile-Takeover.png 2
Monopoly.png 1

# Backs
title_cardback.png 26
draw_cardback.png 26
market_cardback.png 25
```

### 3. Generate the PDF

Run from `Scripts/`:

```bash
python3 tile_cards.py cards.txt output.pdf --img-dir ../Cards-png
```

## Printing

Set your print dialog to **Actual Size / 100%** — not "Fit to page". Otherwise cards won't come out at poker size.

Print single-sided. Run the script twice with separate config files if you want fronts and backs as separate PDFs.

## Cutting

Each card has L-shaped cut marks at its four corners pointing outward into the gutter. Align a metal ruler to the marks and cut with a craft knife or rotary trimmer.

## Options

| Flag | Default | Description |
|---|---|---|
| `--img-dir` | `.` | Directory containing card images |
| `--dpi` | `300` | Render DPI for SVG fallback (ignored for PNGs) |

To change the layout, edit the constants at the top of `tile_cards.py`:

| Constant | Default | Description |
|---|---|---|
| `CARD_W`, `CARD_H` | 63mm, 88mm | Card dimensions |
| `COLS`, `ROWS` | 3, 3 | Grid per page |
| `GUTTER` | 2mm | Space between cards |
| `MARK_LEN` | 3mm | Cut mark length |

## Files

| File | Purpose |
|---|---|
| `process_cards.fish` | Exports SVGs → PNGs via Inkscape |
| `tile_cards.py` | Tiles images onto A4 and outputs PDF |
| `cards.txt` | Your card list with quantities |

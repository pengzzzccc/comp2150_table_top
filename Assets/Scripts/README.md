# tile_cards

Tile SVG playing cards onto A4 pages for printing at poker size (63×88mm).

- 3×3 grid per A4 page (9 cards per page)
- 2mm gutter between cards
- L-shaped cut marks at every card corner
- Vector output — SVGs stay scalable in the final PDF

## Requirements

- Python 3.8+
- Linux, macOS, or Windows

Install dependencies:

```bash
pip install reportlab svglib
```

## Usage

```bash
python3 tile_cards.py <config> <output.pdf> --svg-dir <path/to/svgs>
```

Example:

```bash
python3 tile_cards.py cards.txt deck.pdf --svg-dir ./svgs
```

If your SVGs are in the current directory, `--svg-dir` can be omitted.

## Config file format

Plain text, one entry per line: `filename quantity`. A bare filename defaults to quantity 1. Lines starting with `#` are comments.

```
# Fronts
ace_spades.svg 4
king_hearts.svg 2
queen_diamonds.svg 3

# Backs
back_red.svg 26
back_blue.svg 26
```

## Printing

In your print dialog, set scale to **"Actual size"** or **100%**, NOT "Fit to page". Otherwise cards won't come out at poker size.

Print single-sided. Fronts and backs are treated the same — list them in the same config to get one PDF, or use separate configs if you want separate files.

## Cutting

Cut marks point outward from each card corner into the gutter. Line a ruler up against them and cut with a craft knife or rotary trimmer.

## Adjusting the layout

Constants at the top of `tile_cards.py` control everything:

| Constant | Default | What it does |
|---|---|---|
| `CARD_W`, `CARD_H` | 63mm, 88mm | Card dimensions |
| `COLS`, `ROWS` | 3, 3 | Grid size per page |
| `GUTTER` | 2mm | Space between cards |
| `MARK_LEN` | 3mm | Length of each cut mark |
| `MARK_WIDTH` | 0.3pt | Cut mark line thickness |

## Troubleshooting

**svglib errors or weird rendering** — svglib handles most SVGs but can stumble on filters, complex gradients, or embedded raster images. If your cards don't render correctly, switch to cairosvg + PNG embedding (loses vectors but visually identical at print size).

**Cards come out the wrong size** — check the print dialog scale setting. Must be 100% / Actual Size.

**"SVG not found"** — `--svg-dir` is relative to where you run the command. Use an absolute path if in doubt.

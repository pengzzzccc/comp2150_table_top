#!/usr/bin/env fish

set cards_dir ../Cards
set out_dir ../Cards-png
set dpi 300

mkdir -p $out_dir

for f in $cards_dir/*.svg
    set fname (basename $f .svg)
    inkscape $f \
        --export-filename="$out_dir/$fname.png" \
        --export-dpi=$dpi
    echo "Exported $fname.png"
end

echo "Done — PNGs are in $out_dir"

#!/usr/bin/env fish
#
# export-pages.fish — export each page of a multi-page Inkscape SVG
# as a separate plain SVG, named after the layer's inkscape:label.
#
# Usage: ./export-pages.fish input.svg [output-dir]

if test (count $argv) -lt 1
    echo "usage: "(status filename)" input.svg [output-dir]" >&2
    exit 1
end

set -l input $argv[1]
set -l outdir .
if test (count $argv) -ge 2
    set outdir $argv[2]
end

if not test -f $input
    echo "error: file not found: $input" >&2
    exit 1
end

for cmd in inkscape xmllint
    if not command -q $cmd
        echo "error: required command not found: $cmd" >&2
        exit 1
    end
end

mkdir -p $outdir

set -l count (xmllint --xpath 'count(//*[local-name()="page"])' $input 2>/dev/null)

if test -z "$count"; or test "$count" -eq 0
    echo "error: no <inkscape:page> elements found in $input" >&2
    echo "is this a multi-page Inkscape 1.2+ document?" >&2
    exit 1
end

echo "found $count page(s) in $input"

for i in (seq 1 $count)
    set -l name (xmllint --xpath "string(//*[local-name()='g'][@*[local-name()='groupmode']='layer'][$i]/@*[local-name()='label'])" $input 2>/dev/null)
    test -z "$name"; and set name "page-$i"

    # sanitise: replace filesystem-hostile chars with underscore
    set -l safe (string replace -ra '[/:\\\\<>|?*"]' '_' $name)

    set -l outfile "$outdir/$safe.svg"
    echo "  [$i/$count] $safe.svg"

    inkscape $input \
        --export-type=svg \
        --export-plain-svg \
        --export-area-page \
        --export-page=$i \
        --export-filename=$outfile
end

echo "done."

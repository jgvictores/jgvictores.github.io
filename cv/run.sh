#!/bin/sh
set -u
set -e

# Apply BibTeX cleanups directly to the tracked victores.bib
sed -i '/   note = {/d' victores.bib
sed -i "s/@inbook/@incollection/g" victores.bib
sed -i "s/@article{victores2014thesis/@phdthesis{victores2014thesis/g" victores.bib

# Compile the LaTeX document (Reduced to 3 pdflatex passes)
pdflatex JuanGVictoresCV.tex
bibtex JuanGVictoresCV.aux
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex

# Generate the HTML
make4ht -u JuanGVictoresCV.tex
# Override the modern make4ht thin-column default to mimic the PDF width
echo "body { max-width: 900px !important; margin: 2em auto !important; padding: 0 2em !important; }" >> JuanGVictoresCV.css
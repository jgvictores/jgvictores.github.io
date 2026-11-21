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
# Let the HTML layout expand naturally to fit the screen
sed -i 's/max-width:80ch;/max-width:none;/g' JuanGVictoresCV.css # or custom: sed -i 's/max-width:80ch;/max-width:950px;/g' JuanGVictoresCV.css
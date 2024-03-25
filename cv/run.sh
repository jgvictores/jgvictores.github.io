#!/bin/sh
set -u
set -e

cp ~/export.bib victores.bib
#sed -i "s/{\\\_}/_/g" victores.bib
sed -i '/   note = {/d' victores.bib  # sed -i "s/%2F/2F/g" victores.bib
sed -i "s/@book_section/@incollection/g" victores.bib
sed -i "s/@thesis/@phdthesis/g" victores.bib
sed -i "s/@patent/@misc/g" victores.bib
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex
bibtex JuanGVictoresCV.aux
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex

make4ht -u JuanGVictoresCV.tex

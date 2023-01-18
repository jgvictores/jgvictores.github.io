#!/bin/sh
cp ~/export.bib victores.bib
cat morante2016thesis.bib >> victores.bib
sed -i "s/{\\\_}/_/g" victores.bib
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex
bibtex JuanGVictoresCV.aux
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex

make4ht -u JuanGVictoresCV.tex

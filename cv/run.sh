#!/bin/sh
cp ~/My\ Collection.bib JuanGVictoresCV.bib 
cat morante2016thesis.bib >> JuanGVictoresCV.bib
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex
bibtex JuanGVictoresCV.aux
pdflatex JuanGVictoresCV.tex
pdflatex JuanGVictoresCV.tex


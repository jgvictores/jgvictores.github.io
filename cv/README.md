# cv/

## Workflow

- [email](https://gmail.com) labels: paperAccepted (also in svn:research/papers).
- [Scholar](https://scholar.google.com) ([me](https://scholar.google.com/citations?user=qawKnNkAAAAJ)): Previously check if exists in Scholar or if `.bib` can be exported from official sites.
- [Mendeley](https://www.mendeley.com): Then main workflow begins with [Mendeley Reference Manager for Desktop](https://www.mendeley.com/download-reference-manager). It is important to define an appropriate `Citation Key` at this stage.
- LaTeX: From `Mendeley Reference Manager for Desktop`, go to `My Publications`, sort by `Added` (most recent top), select all, and `File` > `Export All` > `BibTex (*.bib)`. Manually update `JuanGVictoresCV.tex` to include a new `\bibentry` corresponding to the new citation key (and also manually update total count). Run `./run.sh`, which adds SM thesis which is not exported, and also does `make bibtex`.
- [RoboticsLab](roboticslab.uc3m.es/roboticslab/people/jg-victores): If not exist, This has to be done manually.
- [ResearchGate](https://www.researchgate.net/) ([me](https://www.researchgate.net/profile/Juan-Victores)): If not exist, import `.bib` (can be exported from Mendeley).
- [ORCID](https://orcid.org) ([me](https://orcid.org/0000-0002-3080-3467)): If not exist (common case), import `.bib` (can be exported from Mendeley). Update month and day.
- [LinkedIn](https://linkedin.com) ([me](https://linkedin.com/in/jgvictores)): If not exist (common case), This has to be done manually, the ResearchGate interface can help.
- [email](https://gmail.com) labels: paperAccepted -> paperPubished (also in svn:research/papers).

## Helpful Links

- <http://tex.stackexchange.com/questions/60565/separating-two-types-of-articles-from-bibtex-using-printbibliography>
- <http://tex.stackexchange.com/questions/297365/how-to-use-bibtex-for-putting-a-nice-publication-list-in-resume-with-document-cl>
- <https://github.com/bruceravel/My-CV>

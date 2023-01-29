# cv/

## Install Dependencies (Ubuntu 22.04 Jammy)

```bash
sudo apt install texlive-latex-base texlive-latex-recommended \
    texlive-latex-extra texlive-extra-utils texlive-luatex
```

## Workflow

- [email](https://gmail.com): Go to sublabels of `paperAccepted`.
- [Scholar](https://scholar.google.com) ([me](https://scholar.google.com/citations?user=qawKnNkAAAAJ)): Previously check if exists in Scholar or if `.bib` can be exported from official sites.
- [Mendeley Reference Manager for Desktop](https://www.mendeley.com/download-reference-manager) (local, syncs with [Mendeley](https://www.mendeley.com)). The main workflow begins here. It is important to define an appropriate `Citation Key` at this stage (note the convention `lastnameYYYYtitlefirstword`, `lastnameYYYYtitlefirstwordB`, `lastnamecomposedbutnodashYYYYtitlefirstword`).
- LaTeX (local): From `Mendeley Reference Manager for Desktop`, on left go to `My Publications`, sort by `Added` (most recent top), select all, and on bootm `Export` > `BibTex (*.bib)`. Manually update `JuanGVictoresCV.tex` to include a new `\bibentry` corresponding to the new citation key (and also manually update total count). Run `./run.sh`, which adds SM thesis which is not exported, and also does `make bibtex`. If generated and pushed correctly, new citation should appear on <https://jgvictores.github.io/cv/JuanGVictoresCV.html> and <https://jgvictores.github.io/cv/JuanGVictoresCV.html>.
- [RoboticsLab](http://roboticslab.uc3m.es/roboticslab/people/jg-victores): If not exist, This has to be done manually.
- [ResearchGate](https://www.researchgate.net/) ([me](https://www.researchgate.net/profile/Juan-Victores)): If not exist, import `.bib` (can be exported from Mendeley).
- [ORCID](https://orcid.org) ([me](https://orcid.org/0000-0002-3080-3467)): If not exist (common case), import `.bib` (can be exported from Mendeley). Update month and day.
- [LinkedIn](https://linkedin.com) ([me](https://linkedin.com/in/jgvictores)): If not exist (common case), This has to be done manually, the ResearchGate interface can help.
- [email](https://gmail.com): Change sublabel parent from `paperAccepted` -> `paperPubished`.
- Also move in repositories, e.g. svn: `research` or GitHub `papers`.

## Helpful Links

- <http://tex.stackexchange.com/questions/60565/separating-two-types-of-articles-from-bibtex-using-printbibliography>
- <http://tex.stackexchange.com/questions/297365/how-to-use-bibtex-for-putting-a-nice-publication-list-in-resume-with-document-cl>
- <https://github.com/bruceravel/My-CV>

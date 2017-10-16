README.md
=========

## Workflow
- email labels: paperAccepted (also in svn:research/papers).
- Scholar: Previously check if exists in Scholar or if .bib can be exported from official sites.
- Mendeley: Then main workflow begins with Mendeley.
- LaTeX: From Mendeley, select all, sort by Added (most recent top), and Export. Update .tex to include new bibentry (and update number, manually for now). Run ./run.sh, which adds SM thesis which is not exported, and also does make bibtex.
- RoboticsLab: If not exist, This has to be done manually.
- ResearchGate: If not exist, import .bib (can be exported from Mendeley).
- ORCID: If not exist (common case), import .bib (can be exported from Mendeley). Update month and day.
- LinkedIn: If not exist (common case), This has to be done manually, the ResearchGate interface can help.
- email labels: paperAccepted -> paperPubished (also in svn:research/papers).

## Helpful Links
- http://tex.stackexchange.com/questions/60565/separating-two-types-of-articles-from-bibtex-using-printbibliography
- http://tex.stackexchange.com/questions/297365/how-to-use-bibtex-for-putting-a-nice-publication-list-in-resume-with-document-cl
- https://github.com/bruceravel/My-CV


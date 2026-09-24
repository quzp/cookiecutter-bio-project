# manuscript/

Everything aimed at publication.

```
manuscript/
├── notes/        outline, storyline, figure plan, paragraphs cut from drafts
├── drafts/       EVERY version of EVERY text document, one flat folder
│   ├── README.md     version naming rules and status codes
│   └── VERSION_LOG.md
├── main/         major versions of the main text (copies of vXX.00 from drafts/)
├── supplement/   supplementary figures and tables + major versions of supplementary text
├── figures/      hand-assembled final figures, tracked in git
└── submission/   one folder per journal attempt, NN_Journal-Name_YYMMDD/
```

When writing the Methods section, take reagent vendors and catalogue numbers from
`wetlab/protocols/`, cell line and antibody lots from `wetlab/inventory/`, and software
versions from `pixi.lock` — not from memory.

## Three places, three jobs

| Folder | What goes in | How often |
| --- | --- | --- |
| `notes/` | Material you write for yourself: main finding, storyline, figure plan, outline | Freely |
| `drafts/` | Every saved version (major and minor) of every text document — manuscript, supplementary methods, cover letter, response to reviewers — plus returned comments. **No subfolders**; documents are told apart by file name | Every working session |
| `main/`, `supplement/`, `submission/…/` | A **copy** of each major version (`vXX.00`) from `drafts/`: what was shared, finalized or submitted | At each milestone |

The upper-level folders are the clean view of the milestones; `drafts/` is the complete
history.

| Document in `drafts/` | Major versions are copied to |
| --- | --- |
| `Manuscript_…` | `main/` |
| `Supplementary-Methods_…`, `Supplementary-Text_…` | `supplement/` |
| `Cover-Letter_…`, `Response-to-Reviewers_…` | the current `submission/NN_Journal-Name_YYMMDD/` |

## Writing loop

1. **Plan in `notes/`.** Write the one-sentence main finding, the storyline (one line per
   figure) and a figure plan before drafting prose.
2. **Write in `drafts/`.** Save each working session as a new minor version:
   `Manuscript_v00.01-260901_wip.docx`, `…_v00.02-…`.
3. **Milestone.** When the text goes to co-authors, or is finalized, save it as the next
   major version (`v01.00`) in `drafts/`, **copy** that file to `main/`, and add one line
   to `drafts/VERSION_LOG.md`.
4. **Comments** come back into `drafts/` under the version they commented on:
   `Manuscript_v01.00-260922_cmt-JS.docx`.
5. **Revise** in `drafts/` (`v01.01_rev`, …) and repeat from step 3.
6. **Submit.** Copy the exact files sent to the journal into
   `submission/NN_Journal-Name_YYMMDD/`, and record the submission in the root
   `CHANGELOG.md`.

Naming rules and status codes: [`drafts/README.md`](drafts/README.md). Apply the same
pattern to any other document that goes through rounds, such as reports in
`management/reports/`. Dated one-off records whose purpose is chronological order
(experiment folders, meeting notes) keep their date-first names.

# manuscript/

Everything aimed at publication, laid out in the order you write it:
notes → drafts → figures and supplement → submission.

| Subdirectory | Contents |
| --- | --- |
| `notes/` | Outline, storyline, figure plan, key messages, paragraphs cut from drafts |
| `draft/` | **Every saved version of the manuscript text**, plus `VERSION_LOG.md` |
| `figures/` | Hand-assembled final figures, tracked in git |
| `supplement/` | Supplementary figures, tables and methods |
| `submission/` | One folder per journal attempt: what was sent, what came back, the rebuttal |

When writing the Methods section, take reagent vendors and catalogue numbers from
`wetlab/protocols/`, cell line and antibody lots from `wetlab/inventory/`, and software
versions from `pixi.lock` — not from memory.

## Writing workflow

1. **Plan in `notes/`.** Write the one-sentence main finding, the storyline (one line per
   figure), and a figure plan before drafting prose.
2. **Draft in `draft/`.** Never overwrite a version you might want back: save each
   working session as a new minor version (`v00.01`, `v00.02`, …).
3. **Share a round.** When a draft leaves your hands (co-authors, PI, mentor), bump the
   major version (`v01.00`) with status `int`, and add one line to `draft/VERSION_LOG.md`.
4. **Collect comments.** Save each returned copy next to the version it comments on,
   keeping that version number and adding the reviewer's initials: `…_cmt-JS`.
5. **Revise.** Merge comments into the next minor versions (`v01.01_rev`, …). Repeat
   steps 3–5 until the text is final.
6. **Submit.** Copy the exact files sent to the journal into
   `submission/NN_journal_YYMMDD/`, and record the submission in the root `CHANGELOG.md`.

## File naming

```
Document-Name_vXX.YY-YYMMDD_status.ext
```

| Part | Rule | Example |
| --- | --- | --- |
| `Document-Name` | Words joined by **hyphens**; underscores are reserved as field separators | `Manuscript`, `Cover-Letter`, `Response-to-Reviewers` |
| `vXX` | Major version = review round. Bump when the file leaves your hands, is frozen or is submitted; reset minor to `00` | `v01.00` |
| `.YY` | Minor version = working save within a round. Bump for every version worth keeping | `v01.03` |
| `YYMMDD` | Six-digit date the file was saved (or received, for `cmt-`) | `261015` |
| `status` | One word from the table below | `wip` |

Both version fields are two digits, zero-padded, so files sort in the order they were
written. `v00.YY` means the document has not yet been shown to anyone.

| Status | Meaning |
| --- | --- |
| `wip` | Work in progress; only you have seen it |
| `int` | Sent for internal review (co-authors, PI, mentors) |
| `cmt-XX` | Returned with comments by the person with initials `XX` |
| `rev` | Revising in response to comments |
| `final` | Final candidate; all co-authors have approved |
| `submitted` | Exactly the file that was submitted |

A manuscript's life then reads, in file order:

```
Manuscript_v00.01-260901_wip.docx        first rough draft
Manuscript_v00.04-260912_wip.docx
Manuscript_v01.00-260915_int.docx        sent to co-authors
Manuscript_v01.00-260922_cmt-JS.docx     JS's comments on v01.00
Manuscript_v01.00-260923_cmt-AB.docx     AB's comments on v01.00
Manuscript_v01.01-260925_rev.docx        merging comments
Manuscript_v02.00-261003_int.docx        second round
Manuscript_v03.00-261020_final.docx      approved by all authors
Manuscript_v03.00-261021_submitted.pdf   what the journal received
```

Apply the same pattern to any other document that goes through rounds — cover letters,
responses to reviewers, supplementary methods, reports. Dated one-off records whose
purpose is chronological order (experiment folders, meeting notes) keep their
date-first names.

**Git and version files work together.** Git backs up everything, but Word files are not
diffable and git history is invisible to co-authors; the file names are the history you
and your collaborators actually read. If you write in Quarto or Markdown instead, see
`draft/README.md`.

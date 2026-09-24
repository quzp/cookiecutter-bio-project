# manuscript/drafts/ — version rules

Every version of every manuscript text document lives here, in **one flat folder with no
subfolders**. Documents are told apart by the first part of the file name, so sorting by
name groups each document together and lists its versions in the order they were
written. Nothing here is ever overwritten or deleted.

## File name

```
Document-Name_vXX.YY-YYMMDD_status.docx
```

| Part | Rule | Example |
| --- | --- | --- |
| `Document-Name` | Words joined by **hyphens**; underscores are reserved as field separators. Use the same name for every version of a document | `Manuscript`, `Cover-Letter`, `Response-to-Reviewers` |
| `vXX` | **Major version** = milestone. Bump when the document is shared (`int`) or finalized; reset minor to `00` | `v01.00` |
| `.YY` | **Minor version** = working save between milestones. Bump for every version worth keeping | `v01.03` |
| `YYMMDD` | Six-digit date the file was saved (or received, for `cmt-`) | `261015` |
| `status` | One code from the table below | `wip` |

Both version fields are two digits, zero-padded, so files sort correctly. `v00.YY` means
nobody but you has read it yet.

## Status codes

| Status | Meaning | Version number |
| --- | --- | --- |
| `wip` | Work in progress; only you have seen it | minor bump |
| `rev` | Revising in response to comments | minor bump |
| `int` | Sent for internal review (co-authors, PI, mentors) | **major** bump |
| `final` | Final candidate; all co-authors have approved | **major** bump |
| `submitted` | Exactly the file that was submitted | **same** as the `final` it was exported from |
| `cmt-XX` | Returned with comments by the person with initials `XX` | **same** as the version they read |

A `submitted` file keeps its `final` version number because its content is identical,
usually just exported to PDF. If anything changes after `final`, save a new major
version instead.

## Major versions go up one level

Every major version (`vXX.00`: `int`, `final`) and every `submitted` file is **copied** —
not moved — to the folder one level up where that document belongs: `Manuscript_…` to
`main/`, supplementary text to `supplement/`, cover letters and responses to reviewers to
the current `submission/NN_Journal-Name_YYMMDD/`.

## Example

If the project was generated with `include_example_drafts=yes`, the files below really
exist: each `.docx`/`.pdf` is a one-page placeholder that explains its own file name, and
the copies marked `→` are in `main/` and `submission/01_Nat-Commun_261021/`.
`VERSION_LOG.md` has matching example rows. **Delete all of them (and the example log
rows and the example submission folder) before you start writing** — every example
begins with the words "EXAMPLE FILE".

```
drafts/
├── README.md
├── VERSION_LOG.md
├── Cover-Letter_v00.01-261018_wip.docx
├── Cover-Letter_v01.00-261020_final.docx           → copied to submission/01_Nat-Commun_261021/
├── Cover-Letter_v01.00-261021_submitted.docx       → copied to submission/01_Nat-Commun_261021/
├── Manuscript_v00.01-260901_wip.docx               first rough draft
├── Manuscript_v00.04-260912_wip.docx
├── Manuscript_v01.00-260915_int.docx               → copied to main/
├── Manuscript_v01.00-260922_cmt-JS.docx            JS's comments on v01.00
├── Manuscript_v01.00-260923_cmt-AB.docx            AB's comments on v01.00
├── Manuscript_v01.01-260925_rev.docx               merging comments
├── Manuscript_v02.00-261003_int.docx               → copied to main/
├── Manuscript_v03.00-261020_final.docx             → copied to main/
└── Manuscript_v03.00-261021_submitted.pdf          → copied to main/ and submission/01_Nat-Commun_261021/
```

## Writing in Quarto or Markdown instead of Word

Keep one source file, `manuscript.qmd`, plus `references.bib` exported from Zotero, in
this folder. Git holds the history, so the source file is not renamed. At each milestone,
tag the commit and render a named snapshot, then copy it up as usual:

```bash
git tag manuscript-v01.00
quarto render manuscript.qmd --to docx -o Manuscript_v01.00-260915_int.docx
```

## VERSION_LOG.md

One line per version that was shared, received, finalized or submitted — the same files
that get copied up a level. Working saves (`wip`, `rev`) need no entry.

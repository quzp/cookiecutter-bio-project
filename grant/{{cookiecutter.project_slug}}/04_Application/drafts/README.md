# drafts/ — version rules

Every version of every application document lives here, in **one flat folder with no
subfolders**. Documents are told apart by the first part of the file name, so sorting by
name groups each document together and lists its versions in the order they were
written. Nothing here is ever overwritten or deleted.

## File name

```text
Document-Name_vXX.YY-YYMMDD_status.docx
```

| Part | Rule | Example |
| --- | --- | --- |
| `Document-Name` | Words joined by **hyphens**; underscores are reserved as field separators. Use the same name for every version of a document | `Specific-Aims`, `Research-Strategy`, `Project-Summary` |
| `vXX` | **Major version** = milestone. Bump when the document is shared (`int`), frozen or finalized; reset minor to `00` | `v02.00` |
| `.YY` | **Minor version** = working save between milestones. Bump for every version worth keeping | `v02.03` |
| `YYMMDD` | Six-digit date the file was saved (or received, for `cmt-`) | `261015` |
| `status` | One code from the table below | `wip` |

Both version fields are two digits, zero-padded, so files sort correctly. `v00.YY` means
nobody but you has read it yet.

## Status codes

| Status | Meaning | Version number |
| --- | --- | --- |
| `wip` | Work in progress; only you have seen it | minor bump |
| `rev` | Revising in response to comments or review issues | minor bump |
| `int` | Sent for internal review (co-investigators, mentors, mock reviewers) | **major** bump |
| `frozen` | Structure locked; later changes are wording only (Aims at gate G3) | **major** bump |
| `final` | Final candidate, ready for the P7 compliance check | **major** bump |
| `submitted` | Exactly what went into the submitted package | **same** as the `final` it was exported from |
| `cmt-XX` | Returned with comments by the person with initials `XX` | **same** as the version they read |
| `AI-<prompt>` | AI review output (e.g., `AI-D` = Prompt D). Saved in `05_Review/AI_Review/`, never here | **same** as the version the AI read |

A `submitted` file keeps its `final` version number because its content is identical,
usually just exported to PDF. If anything changes after `final`, save a new major
version instead.

## Major versions go up one level

Every major version (`vXX.00`: `int`, `frozen`, `final`) and every `submitted` file is
**copied** — not moved — into its section folder in `04_Application/`
(`Specific_Aims/`, `Research_Strategy/`, …). `drafts/` keeps the complete history; the
section folder shows only the milestones.

## Example

If the project was generated with `include_example_drafts=yes`, the files below really
exist: each `.docx`/`.pdf` is a one-page placeholder that explains its own file name, and
the copies marked `→` are in the section folders. `VERSION_LOG.md` has matching example
rows, and `05_Review/AI_Review/` holds the example AI review. **Delete all of them (and
the example log rows) before you start writing** — every example begins with the words
"EXAMPLE FILE".

```text
drafts/
├── README.md
├── VERSION_LOG.md
├── Research-Strategy_v00.01-261020_wip.docx
├── Research-Strategy_v01.00-261105_int.docx          → copied to Research_Strategy/
├── Specific-Aims_v00.01-261001_wip.docx              first rough page
├── Specific-Aims_v00.05-261008_wip.docx
├── Specific-Aims_v01.00-261010_int.docx              → copied to Specific_Aims/
├── Specific-Aims_v01.00-261015_cmt-JS.docx           JS's comments on v01.00
├── Specific-Aims_v01.01-261017_rev.docx              after comments + Prompt D issues
├── Specific-Aims_v02.00-261022_frozen.docx           → copied to Specific_Aims/ (G3)
├── Specific-Aims_v03.00-261210_final.docx            → copied to Specific_Aims/
└── Specific-Aims_v03.00-261212_submitted.pdf         → copied to Specific_Aims/ and 06_Submission/Submitted/
```

The Prompt D stress test of Aims v01.00 would be
`05_Review/AI_Review/Specific-Aims_v01.00-261012_AI-D.md`.

## VERSION_LOG.md

One line per version that was shared, received, frozen, finalized or submitted — the
same files that get copied up a level. Working saves (`wip`, `rev`) need no entry.

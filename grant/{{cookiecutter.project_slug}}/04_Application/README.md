# 04_Application — the PI's writing workspace (🔴 RED ZONE)

This is where you write the application. Everything here is written by the PI (or
co-authors). AI tools may read these files for critique, audit and itemized line-edit
suggestions, but never write or overwrite anything in this folder; their output goes to
`05_Review/AI_Review/`.

```text
04_Application/
├── notes/                        thinking space: concept page, outlines, cut paragraphs
└── draft/                        every saved version of every document
    ├── VERSION_LOG.md            one line per version shared, frozen or submitted
    ├── Specific_Aims/
    ├── Research_Strategy/        Significance, Innovation, Approach (one file or one per part)
    ├── Summary_Narrative/        Project Summary/Abstract and Project Narrative
    ├── Introduction_Resubmission/  resubmissions only; includes the critique→response table
    └── Other_Attachments/        biosketch, facilities, budget justification, letters, …
```

## notes/ — before and around the prose

Material you write for yourself, not for reviewers:

- the 250–300-word summary used for RePORTER Matchmaker (P1);
- the one-page concept for the program officer (P1);
- the knowledge-gap sentence and central-hypothesis drafts;
- outlines of the Aims page and of each Aim's Approach;
- `parking_lot.md` — paragraphs cut from drafts that may come back.

A note that is sent to someone (e.g., the concept page to the PO) becomes a versioned
document: name it with the rules below.

## draft/ — every version, never overwritten

The newest version is simply the highest version number. Earlier versions stay, so you
can always return to what a colleague, the PO or an AI reviewer actually read.

### File naming

```text
Document-Name_vXX.YY-YYMMDD_status.docx
```

| Part | Rule | Example |
| --- | --- | --- |
| `Document-Name` | Words joined by **hyphens**; underscores are reserved as field separators | `Specific-Aims`, `Research-Strategy`, `Project-Summary` |
| `vXX` | Major version = round. Bump when the file leaves your hands (colleagues, PO), is frozen, or is submitted; reset minor to `00` | `v02.00` |
| `.YY` | Minor version = working save within a round. Bump for every version worth keeping | `v02.03` |
| `YYMMDD` | Six-digit date the file was saved (or received, for `cmt-`) | `261015` |
| `status` | One word from the table below | `wip` |

Both version fields are two digits, zero-padded, so files sort in the order they were
written. `v00.YY` means nobody but you has read it yet.

| Status | Meaning |
| --- | --- |
| `wip` | Work in progress; only you have seen it |
| `int` | Sent for internal review (co-investigators, mentors, mock reviewers) |
| `cmt-XX` | Returned with comments by the person with initials `XX` |
| `rev` | Revising in response to comments or review issues |
| `frozen` | Structure locked; later changes are wording only (Aims at gate G3) |
| `final` | Final candidate, ready for the P7 compliance check |
| `submitted` | Exactly the file that went into the submitted package |

### What a section folder looks like

```text
draft/Specific_Aims/
├── Specific-Aims_v00.01-261001_wip.docx      first rough page
├── Specific-Aims_v00.05-261008_wip.docx
├── Specific-Aims_v01.00-261010_int.docx      sent to two colleagues
├── Specific-Aims_v01.00-261015_cmt-JS.docx   JS's comments on v01.00
├── Specific-Aims_v01.01-261017_rev.docx      revising after comments + Prompt D issues
├── Specific-Aims_v02.00-261022_frozen.docx   G3 passed: architecture frozen
├── Specific-Aims_v03.00-261210_final.docx
└── Specific-Aims_v03.00-261212_submitted.pdf
```

### Rules of thumb

- **New working session → new minor version.** Word's autosave is not a version; a copy
  you might want to return to is.
- **Leaves your hands → new major version** and one line in `draft/VERSION_LOG.md`.
- **Comments come back → keep the version they commented on**, change date and status,
  and save the file in the same section folder. Summarize substantive issues in
  `05_Review/REVIEWER_RISK_REGISTER.md`.
- **Running an AI prompt does not need a new version.** The AI output is saved in
  `05_Review/AI_Review/` under the name of the version it read, with `AI-<prompt>` as
  status: `Specific-Aims_v01.00-261012_AI-D.md` is the Prompt D stress test of Aims
  v01.00, run on 261012.
- When a round is closed and the folder gets crowded, you may move earlier files into an
  `_archive/` subfolder of that section. Move, never delete.
- At submission, copy the `submitted` files into `06_Submission/Submitted/`.

## How the writing maps onto the workflow

| Phase | What you write here | Typical versions |
| --- | --- | --- |
| P1 Positioning | Matchmaker summary, concept page, PO email in `notes/` | `Concept_v01.00-…_int` when sent to the PO |
| P3 Aims | Specific Aims | `v00.xx_wip` → `v01.00_int` → `v01.xx_rev` → `v02.00_frozen` |
| P4 Preliminary data | Preliminary-data text, from `03_Preliminary_Data/FIGURE_REGISTER.md` only | inside Research Strategy |
| P5 Research Strategy | Significance, Innovation, Approach; resubmission Introduction | `v00.xx_wip` → `v01.00` (audit, Prompt F) → `v01.xx_rev` |
| P6 Review | Revisions after AI and human review | `v02.00_int` to mock reviewers → `cmt-XX` → `v02.xx_rev` |
| P7 Submission | Final text | `vNN.00_final` → `vNN.00_submitted` |

Git also backs up every commit, but Word files are not diffable and git history is
invisible to collaborators: the file names are the history you actually read.

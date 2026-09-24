# 04_Application — the PI's writing workspace (🔴 RED ZONE)

This is where you write the application. Everything here is written by the PI (or
co-authors). AI tools may read these files for critique, audit and itemized line-edit
suggestions, but never write or overwrite anything in this folder; their output goes to
`05_Review/AI_Review/`.

```text
04_Application/
├── notes/                      thinking space: concept page, outlines, cut paragraphs
├── drafts/                     EVERY version of EVERY document, one flat folder
│   ├── README.md               version naming rules and status codes
│   └── VERSION_LOG.md          one line per version shared, received, frozen or submitted
├── Specific_Aims/              major versions only (copies of vXX.00 from drafts/)
├── Research_Strategy/          Significance, Innovation, Approach
├── Summary_Narrative/          Project Summary/Abstract and Project Narrative
├── Introduction_Resubmission/  resubmissions only; includes the critique→response table
└── Other_Attachments/          biosketch, facilities, budget justification, letters, …
```

## Three places, three jobs

| Folder | What goes in | How often |
| --- | --- | --- |
| `notes/` | Material you write for yourself: Matchmaker summary, PO concept page, knowledge-gap and hypothesis drafts, outlines, `parking_lot.md` for cut paragraphs | Freely |
| `drafts/` | Every saved version (major and minor) of every document, plus returned comments. **No subfolders** — documents are told apart by file name | Every working session |
| Section folders | A **copy** of each major version (`vXX.00`) from `drafts/`: what was shared, frozen, finalized or submitted | At each milestone |

The section folders are the clean view: open `Specific_Aims/` and you see only the
milestones, with the newest one on the bottom. `drafts/` is the complete history.

## Writing loop

1. **Plan** in `notes/`.
2. **Write** in `drafts/`, saving each working session as a new minor version:
   `Specific-Aims_v00.01-261001_wip.docx`, `…_v00.02-…`.
3. **Milestone** — when the document is shared, frozen or finalized, save it as the next
   major version (`v01.00`) in `drafts/`, **copy** that file into its section folder, and
   add one line to `drafts/VERSION_LOG.md`.
4. **Comments** come back into `drafts/` under the version they commented on:
   `Specific-Aims_v01.00-261015_cmt-JS.docx`. Summarize substantive issues in
   `05_Review/REVIEWER_RISK_REGISTER.md`.
5. **Revise** in `drafts/` (`v01.01_rev`, …) and repeat from step 3.
6. **Submit** — copy the `submitted` files into the section folder and into
   `06_Submission/Submitted/`.

Naming rules and status codes: [`drafts/README.md`](drafts/README.md).

## How the writing maps onto the workflow

| Phase | What you write | Milestones copied to the section folder |
| --- | --- | --- |
| P1 Positioning | Matchmaker summary, concept page, PO email in `notes/` | `Concept_v01.00-…_int` in `notes/` when sent to the PO |
| P3 Aims | Specific Aims | `v01.00_int` (to colleagues) → `v02.00_frozen` (gate G3) |
| P4 Preliminary data | Preliminary-data text, from `03_Preliminary_Data/FIGURE_REGISTER.md` only | inside Research Strategy |
| P5 Research Strategy | Significance, Innovation, Approach; resubmission Introduction | `v01.00` (audited with Prompt F) → `v02.00` … |
| P6 Review | Revisions after AI and human review | `vNN.00_int` to mock reviewers |
| P7 Submission | Final text | `vNN.00_final` → the same version as `_submitted` |

Git also backs up every commit, but Word files are not diffable and git history is
invisible to collaborators: the file names are the history you actually read.

# Grant workflow template (`grant/`)

A Cookiecutter template for **NIH-compliant, AI-assisted biomedical grant development**, shipped as a subdirectory of [cookiecutter-bio-project](https://github.com/quzp/cookiecutter-bio-project).

**Core principle: the PI thinks and writes; AI retrieves, computes, critiques, and verifies.**

It sets up a gated seven-phase workflow, seven standard AI prompts, and the registers needed to keep every claim, number, and AI interaction traceable. It is designed around NIH [NOT-OD-25-132](https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html) (AI and originality) and the NIH [Simplified Review Framework](https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework).

## Usage

```bash
cookiecutter gh:quzp/cookiecutter-bio-project --directory grant

# non-interactive
cookiecutter gh:quzp/cookiecutter-bio-project --directory grant --no-input \
  project_name="Cone Chromatin R01" mechanism="R01" deadline="2027-02-05" is_resubmission="no"

# pin a version
cookiecutter gh:quzp/cookiecutter-bio-project --directory grant --checkout v2.0.0
```

## Options

| Variable | Meaning |
|---|---|
| `project_name`, `project_id` | Title and short ID; `project_slug` is derived automatically |
| `pi_name`, `institution` | Filled into the brief and templates |
| `sponsor`, `mechanism`, `nofo_number`, `nofo_url` | Funding opportunity |
| `is_resubmission` | `yes` creates `04_Application/draft/Introduction_Resubmission/`; `no` removes it |
| `deadline`, `internal_deadline` | Sponsor deadline (YYYY-MM-DD) and institutional routing deadline |
| `target_program`, `program_officer`, `study_section` | Positioning |
| `coordinator_assistant` | The ONE assistant used as coordinator |
| `analysis_tool`, `analysis_repo` | Where preliminary-data analysis happens (e.g., a project made with the bio template) |
| `init_git` | Initialize a Git repository with a first commit |

## Generated structure

```text
<project_slug>/
├── 00_Admin/        brief, state, decision log, timeline, AI-use log,
│                    data classification, NIH application count, final checklist
├── 01_Funding/      official documents, compliance matrix, landscape, PO contact
├── 02_Evidence/     claims register, evidence matrix, references.bib (Zotero export)
├── 03_Preliminary_Data/  figure register, figures, source data, analysis-repo pointer
├── 04_Application/  RED ZONE — PI writing workspace: notes/ + draft/ (every version kept,
│                    Document-Name_vXX.YY-YYMMDD_status.docx)
├── 05_Review/       AI review, human review, reviewer risk register
├── 06_Submission/   final compliance, submitted package
├── 99_Archive/
└── .ai/             master instructions, prompts A–G, handoff file, workflow
```

## The three writing zones

| Zone | Content | AI role |
|---|---|---|
| 🔴 RED — PI-authored | Specific Aims; Research Strategy arguments; Project Summary & Narrative; resubmission Introduction; PO emails | Questions, critique, verification, itemized edit suggestions only |
| 🟡 YELLOW — limited assistance | Figure legends, factual budget items, facilities lists, reference formatting | First pass from registered facts; PI verifies and revises |
| 🟢 GREEN — AI-led support | Compliance, landscape, literature verification, data analysis, stress tests, audits, reviewer simulation | Full support; no scientific judgment on the PI's behalf |

## Workflow at a glance

| Phase | Output | Prompt |
|---|---|---|
| P0 Setup & rules | Compliance matrix, application count, data classification, timeline | A |
| P1 Positioning & PO | Landscape summary, PI-written concept, PO contact | B |
| P2 Evidence | Claims register, evidence matrix, knowledge-gap sentence | C |
| P3 Aims & stress test | PI-written Aims `v01.00` → issue list → `v02.00_frozen` | D |
| P4 Preliminary data | Figures + source data + code + figure register | E |
| P5 Research Strategy | PI-written strategy, audited | F |
| P6 Review | AI (different vendor) + human mock review → risk register | G |
| P7 Compliance & submission | Final compliance on the PDF package, STOP list, checklist | A (final mode) |

Full documentation: [`docs/GRANT_WORKFLOW_GUIDE.md`](docs/GRANT_WORKFLOW_GUIDE.md) · Changes: [`CHANGELOG.md`](CHANGELOG.md) · Maintenance notes: [`TEMPLATE_NOTES.md`](TEMPLATE_NOTES.md)

## Disclaimer

This template is not legal or compliance advice. Sponsor policies change; the sponsor's current notices and your institution's research office are the authorities. Check non-NIH sponsors' own AI policies and review criteria.

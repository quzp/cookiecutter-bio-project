# {{ cookiecutter.project_name }}

**Project ID:** {{ cookiecutter.project_id }}  
**Sponsor / Mechanism:** {{ cookiecutter.sponsor }} {{ cookiecutter.mechanism }}  
**Resubmission:** {{ cookiecutter.is_resubmission }}  
**Deadline:** {{ cookiecutter.deadline }} (internal: {{ cookiecutter.internal_deadline }})  
**PI:** {{ cookiecutter.pi_name }} — {{ cookiecutter.institution }}  
**Coordinator assistant:** {{ cookiecutter.coordinator_assistant }}  
**Analysis tool:** {{ cookiecutter.analysis_tool }}

## Principle

The PI thinks and writes; AI retrieves, computes, critiques, and verifies. RED-zone content (Specific Aims, Research Strategy arguments, Project Summary, Narrative, resubmission Introduction, PO emails) is written only by the PI.

## Start here

1. Fill `00_Admin/PROJECT_BRIEF.md`, `APPLICATION_COUNT.md`, `DATA_CLASSIFICATION.md`.
2. Put official documents in `01_Funding/NOFO_and_Instructions/`.
3. Paste `.ai/MASTER_INSTRUCTIONS.md` into your coordinator assistant's project instructions.
4. Run `.ai/prompts/A_compliance.md` with `.ai/handoffs/GRANT_HANDOFF.md`.
5. Follow `.ai/workflow/GRANT_WORKFLOW.md`; advance only when each gate passes.

## Canonical files

| Content | Location | Who edits |
|---|---|---|
| Application text (all versions) | `04_Application/draft/` | PI only |
| State / decisions | `00_Admin/PROJECT_STATE.md`, `DECISION_LOG.md` | PI |
| Claim → evidence | `02_Evidence/CLAIMS_REGISTER.md` | AI fills, PI verifies |
| Figure → data → code | `03_Preliminary_Data/FIGURE_REGISTER.md` | AI fills, PI verifies |
| Literature | Zotero collection (`references.bib` is an export) | PI |

AI output goes only to `05_Review/AI_Review/`.

## Versioning

Write in `04_Application/draft/`, plan in `04_Application/notes/`. Every version is kept:

```text
Document-Name_vXX.YY-YYMMDD_status.docx      e.g. Specific-Aims_v01.02-261015_rev.docx
```

Major `XX` = round (bump when a file is shared, frozen or submitted); minor `YY` = working save; `YYMMDD` = six-digit date; status ∈ `wip` / `int` / `cmt-XX` / `rev` / `frozen` / `final` / `submitted`. AI reviews are named after the version they read (`Specific-Aims_v01.00-261012_AI-D.md`). Full rules: `04_Application/README.md`.

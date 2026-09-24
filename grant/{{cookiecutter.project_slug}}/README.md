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
| Application text | `04_Application/` | PI only |
| State / decisions | `00_Admin/PROJECT_STATE.md`, `DECISION_LOG.md` | PI |
| Claim → evidence | `02_Evidence/CLAIMS_REGISTER.md` | AI fills, PI verifies |
| Figure → data → code | `03_Preliminary_Data/FIGURE_REGISTER.md` | AI fills, PI verifies |
| Literature | Zotero collection (`references.bib` is an export) | PI |

AI output goes only to `05_Review/AI_Review/`.

## Versioning

`YYYY-MM-DD_document_vNN_status`, where status ∈ `working` / `PI-review` / `collaborator-review` / `redteam` / `revised` / `final-candidate` / `submitted`.

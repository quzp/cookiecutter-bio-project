# Changelog — grant template

## v2.2.0 — 2026-09-24

### Added
- `include_example_drafts` option: fills `04_Application/drafts/` with self-describing example `.docx`/`.pdf` files and their major-version copies, example `VERSION_LOG.md` rows, and an example AI review.

### Changed
- `04_Application/draft/` renamed to `drafts/` and flattened: every version of every document lives in one folder, told apart by file name. `drafts/` holds only the version rules (`README.md`) and `VERSION_LOG.md` besides the drafts.
- Section folders (`Specific_Aims/`, `Research_Strategy/`, `Summary_Narrative/`, `Introduction_Resubmission/`, `Other_Attachments/`) moved back up to `04_Application/`; they now hold copies of each major version.
- A `submitted` file keeps the version number of the `final` it was exported from.
- `AI-<prompt>` listed as a status code for AI review outputs.

## v2.1.0 — 2026-09-24

### Changed
- `04_Application/` reorganised as the PI's writing workspace: `notes/` for outlines and the concept page, `draft/` for every saved version of each document. Section folders moved to `04_Application/draft/`.
- Version naming changed from `YYYY-MM-DD_document_vNN_status` to `Document-Name_vXX.YY-YYMMDD_status` (major = round, minor = working save, six-digit date); status codes simplified to `wip` / `int` / `cmt-XX` / `rev` / `frozen` / `final` / `submitted`.
- AI review outputs are named after the draft version they read (`…_AI-<prompt>`).

### Added
- `04_Application/draft/Summary_Narrative/` for the Project Summary and Narrative.
- `04_Application/draft/VERSION_LOG.md`.

## v2.0.0 — 2026-09-24

### Changed
- PI drafts, AI reviews: AI no longer drafts Specific Aims or Research Strategy (NIH NOT-OD-25-132). Three writing zones (RED / YELLOW / GREEN) enforced in the master instructions and every prompt.
- Reviewer prompt rebuilt around the NIH Simplified Review Framework (Factors 1/2/3); must run on a different vendor's model and alongside human mock review.
- 12 phases / 8 agents condensed to 7 phases / 7 prompts (A–G); folder tree reduced to ~20 directories.
- Canonical files defined; AI output restricted to `05_Review/AI_Review/`.
- Tool roles made vendor-neutral; one coordinator assistant.

### Added
- `AI_USE_LOG`, `CLAIMS_REGISTER`, `FIGURE_REGISTER`, `DATA_CLASSIFICATION`, `APPLICATION_COUNT`, `TIMELINE`, `PO_CONTACT`, `SUBMISSION_CHECKLIST`.
- `is_resubmission` option with a summary-statement response table.
- Human mock-review request template.
- `.gitignore` rules keeping large/sensitive omics files out of grant repositories.
- Bake test (`tests/bake_test.sh`) and GitHub Actions CI at the repository root.
- Moved into `cookiecutter-bio-project/grant/`; invoked with `--directory grant`.

## v1.0.0
- Initial AI-assisted grant workflow (ChatGPT-generated draft).

# Changelog — grant template

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

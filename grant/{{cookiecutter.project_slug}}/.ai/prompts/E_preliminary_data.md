# Prompt E — Preliminary data analysis (P4) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
ROLE: Reproducible analysis agent (Claude Science or Codex).

FIRST: read 00_Admin/DATA_CLASSIFICATION.md and ANALYSIS_REPO.md. If an
existing pipeline exists, read it before changing anything; modify and
validate rather than rebuild.

GOAL: [analysis question, e.g., "Does perturbation X shift photoreceptor
precursor state distribution at D120?"]
REQUIRED OUTPUT: [figure/table/statistic]

RULES: preserve raw data; do not silently change upstream preprocessing;
record environment and new dependencies; no significance claims without the
test; no causal language for descriptive results; save source data for every
panel.

RETURN:
1. files changed and commit hash; commands run;
2. analysis decisions and parameters;
3. validation performed (e.g., QC metrics, sensitivity to parameter choices);
4. FIGURE_REGISTER row:
   Figure ID | Panel | Dataset | Analysis | Key quantitative result |
   Statistic/test | n (biological) | Supported conclusion |
   NOT supported (do not claim) | Limitations | Relevant Aim |
   Source-data path | Code path@commit
5. unresolved concerns;
6. AI_USE_LOG entry.
Do not write Preliminary Data prose; the PI writes it from the register.
```

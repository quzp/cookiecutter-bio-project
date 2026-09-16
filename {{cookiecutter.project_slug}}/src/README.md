# src/

All code, layered in the order data moves through it: processing, then analysis, then
figures. That ordering is what makes any given figure traceable to its source data.

| Subdirectory | Responsibility |
| --- | --- |
| `data/` | Read `data/raw` and `data/external`; clean, QC, convert; write to `interim`/`processed` |
| `analysis/` | Statistical modelling, differential expression, enrichment; write to `results/tables` |
| `visualization/` | Read `processed`/`results/tables`; write figures to `results/figures` |
| `notebooks/` | Exploratory analysis, not pipeline code |
| `utils/` | Shared helpers: path resolution, config loading, plotting theme |

Conventions:

- Numbered filenames encode execution order: `01_qc.R`, `02_normalize.R`, `10_deseq2.R`.
- **No absolute paths.** In R use `here::here("data", "raw", ...)`; in Python use the
  helpers in `utils/paths.py`. Scripts then run from any working directory.
- **No hard-coded grouping.** Read the design matrix from `data/metadata/samples.tsv`.
- Parameters — thresholds, genome versions, colours — live in
  `management/config/config.yml`, not scattered through scripts.
- Scripts print `sessionInfo()` or equivalent environment details to their log, so the
  run can be reproduced later.

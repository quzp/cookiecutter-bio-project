# src/notebooks/

Exploratory analysis. Naming: `NN_short_description_initials`, e.g.

```
01_qc_overview_zq.qmd
02_pca_batch_check_zq.qmd
```

Conventions:

- **A notebook is a draft, not a pipeline.** Once an analysis settles and is headed for
  the manuscript, rewrite it as a script under `src/` so the figure is produced
  reproducibly into `results/figures/`.
- No irreproducible manual steps inside a notebook — no editing values by hand, no
  deleting rows interactively.
- Rendered output (`*_files/`, HTML) is excluded from git; see `.gitignore`.

Render everything with `pixi run render`.

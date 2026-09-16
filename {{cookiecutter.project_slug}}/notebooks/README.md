# notebooks/

探索性分析。命名规则：`序号_简短描述_姓名缩写`，例如：

```
01_qc_overview_zp.qmd
02_pca_batch_check_zp.qmd
```

约定：

- **notebook 是草稿，不是流水线。** 一旦某段分析定型、要进手稿，就把它重写成
  `src/` 下的脚本，由脚本生成 `results/figures/` 里的图。
- notebook 里不做不可复现的手工操作（临时改数、手动删行）。
- 渲染产物（`*_files/`、html）不进 git，见 `.gitignore`。

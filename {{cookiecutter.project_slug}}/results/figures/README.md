# results/figures/

Figures written directly by scripts in `src/visualization/`:

- **Regenerable** — rerunning the script redraws everything, so these are not in git.
- **Unassembled** — single panels, no multi-panel layout, no letter labels.
- **For you** — self-review and lab meetings.

Figures headed for the manuscript are assembled and annotated by hand and saved to
`manuscript/figures/`, which *is* tracked in git.

Name files after the script that produced them: `10_deseq2_volcano.pdf` comes from
`src/analysis/10_deseq2.R`. Prefer vector formats (PDF, SVG); raster output at 300 dpi
or higher.

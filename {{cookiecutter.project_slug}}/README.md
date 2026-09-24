# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

| | |
| --- | --- |
| Lead | {{ cookiecutter.author_name }}{% if cookiecutter.institution %}, {{ cookiecutter.institution }}{% endif %} |
| Started | __DATE__ |
| Analysis language | {{ cookiecutter.primary_language }} |
| Status | In progress |

## Getting started

```bash
pixi install          # resolve and lock the environment from pixi.toml
pixi run check        # confirm the interpreter and core packages work
pixi shell            # enter the environment interactively
```

## Directory map

```
.
├── wetlab/         Human-written bench records (plain text, tracked in git)
│   ├── protocols/      Reusable SOPs, one method per file
│   ├── experiments/    One directory per experiment, YYYYMMDD_short_name/
│   └── inventory/      Plasmids, primers, antibodies, cell lines, gRNAs
├── data/           Machine-generated data (excluded from git except metadata/)
│   ├── metadata/       Sample sheet linking bench work to sequencing output
│   ├── raw/            Instrument output, read-only
│   ├── external/       Public datasets and references
│   ├── interim/        Intermediate results, always regenerable
│   └── processed/      Analysis-ready datasets
├── src/            All code
│   ├── data/           Preprocessing, QC, format conversion
│   ├── analysis/       Statistics and modelling
│   ├── visualization/  Figure scripts
│   ├── notebooks/      Exploratory analysis
│   └── utils/          Shared helpers: paths, config, plotting theme
├── results/        Script output
│   ├── figures/        Regenerable figures, excluded from git
│   └── tables/         Statistical result tables
├── manuscript/     Everything aimed at publication
│   ├── notes/          Outline, storyline, figure plan
│   ├── draft/          Every saved version of the text, plus VERSION_LOG.md
│   ├── figures/        Hand-assembled final figures, tracked in git
│   ├── supplement/     Supplementary material
│   └── submission/     Per-journal versions and rebuttals
└── management/     Running the project rather than doing the science
    ├── config/         Analysis parameters and external paths
    ├── docs/           Literature notes, meeting minutes, method surveys
    └── reports/        Progress reports, committee updates, grant reporting
```

Every directory contains a `README.md` describing exactly what belongs in it.

## Working conventions

1. **`data/raw/` is read-only.** Any renaming, filtering or conversion is written as a
   script in `src/data/` that outputs to `data/interim/` or `data/processed/`. Raw files
   are never edited in place. If you find yourself wanting to, a script is missing.
2. **One directory per experiment.** Create `wetlab/experiments/YYYYMMDD_short_name/`
   and fill in a copy of `TEMPLATE_experiment.md`.
3. **Register samples the day they exist.** New cells, libraries or sequencing batches go
   into `data/metadata/samples.tsv` immediately. A `sample_id` is never changed or reused.
4. **Figures in `results/figures/` must come from a script in `src/`.** Hand-assembled
   panels go to `manuscript/figures/`. The two are never mixed.
5. **`CHANGELOG.md` records turning points:** new data batches, changed analysis methods,
   submissions and revisions — one line each.
6. **Drafts are never overwritten.** Documents that go through rounds (manuscript,
   cover letter, rebuttal, reports) are saved as `Document-Name_vXX.YY-YYMMDD_status.docx`;
   see `manuscript/README.md` for the version and status rules.
7. **Large files stay out of git.** See `.gitignore`. For mid-size files that genuinely
   need versioning, `.gitattributes` has commented Git LFS rules.

## Data backup

`data/` is not in git, so backup is your responsibility. Suggested practice:

- Mirror `data/raw/` to lab storage or object storage the day it arrives, then set read-only.
- Record the backup location here, e.g. `Raw data mirror: <path or link>`.

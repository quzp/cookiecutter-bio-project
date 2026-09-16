# experiments/

A complete record of one experiment. One directory per experiment:

```
experiments/
├── 20260301_organoid_d30_qc/
│   ├── record.md              <- filled in from TEMPLATE_experiment.md
│   ├── plate_layout.tsv       <- plate maps, loading tables, small tabular data
│   └── notes/                 <- observations (images themselves go to data/raw/)
└── 20260315_crispri_transduction/
```

Naming: `YYYYMMDD_short_description`, dated by the day the experiment **started**.

Conventions:

- **Write the record the same day.** Anything added later is marked
  "added retrospectively on YYYY-MM-DD".
- **Never rewrite history.** If you find an error in an earlier record, append a
  correction at the end rather than editing the original text.
- **Link to the data.** List every sample produced, using `sample_id` values that match
  `data/metadata/samples.tsv` exactly, and give the path under `data/raw/` for the files.
- **Keep failed experiments.** Mark the title `[FAILED]` and write down why. These
  records are worth more than the successful ones.

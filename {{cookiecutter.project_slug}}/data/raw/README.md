# data/raw/

Instrument output. **Read-only; never modified in place.**

Renaming, cleaning, filtering and format conversion are all done by scripts in
`src/data/` that write to `data/interim/`. If you find yourself wanting to edit a file
here directly, a script is missing.

Organise by assay type:

```
raw/
├── rnaseq/
├── scrnaseq/
├── imaging/
├── flow/
└── qpcr/
```

Do two things the moment data arrives:

1. **Make it read-only:** `chmod -R a-w data/raw/<new_directory>`
2. **Record checksums:**
   `find data/raw -type f -exec sha256sum {} + > data/raw/CHECKSUMS.sha256`
   (verify later with `sha256sum -c`, which catches both silent corruption and
   accidental edits)

Each new data directory should contain a `SOURCE.md` recording: origin (facility or
instrument), date received, the corresponding `experiment_id`, and the list of
`sample_id` values it covers.

# data/processed/

Analysis-ready datasets, for example:

- Filtered and normalised expression matrices
- Annotated `SummarizedExperiment` / `AnnData` objects
- Tables already joined with grouping information from `data/metadata/samples.tsv`

Conventions:

- Include a date or version in the filename, e.g. `counts_filtered_20260401.rds`, so a
  figure in the manuscript can be traced to the exact dataset behind it.
- Every file has a generating script; record its path in the file header or in a
  matching `.md` note.

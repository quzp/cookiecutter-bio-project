# data/metadata/

**The most important directory in the project.** It is the only joint between the bench
and the computation: without it, nobody can tell six months later which tube of cells a
given FASTQ file came from.

Unlike the rest of `data/`, this directory **is tracked in git** — the sample sheet is
small, textual, and its edit history is itself evidence.

## samples.tsv fields

| Field | Required | Description |
| --- | --- | --- |
| `sample_id` | yes | Globally unique in the project; **never modified** once written. `S001`, `S002`, ... |
| `experiment_id` | yes | Matches a directory name under `wetlab/experiments/` |
| `condition` | yes | Experimental group; used to build the design matrix downstream |
| `replicate` | yes | Biological replicate number (add `tech_rep` for technical replicates) |
| `cell_line` | | Matches `wetlab/inventory/cell_lines.tsv` |
| `timepoint` | | Sampling timepoint, e.g. `d30` |
| `collection_date` | yes | ISO 8601, the day of collection |
| `assay` | yes | `RNA-seq` / `scRNA-seq` / `ATAC` / `qPCR` / `imaging` / `flow` |
| `library_id` | | Library or sequencing ID as returned by the facility |
| `raw_path` | | Path relative to the project root, e.g. `data/raw/rnaseq/S001_R1.fastq.gz` |
| `batch` | | Library prep batch or sequencing run; used for batch-effect correction |
| `qc_status` | | `pass` / `fail` / `pending`. Failed samples keep their row |
| `notes` | | Anything unusual |

## Conventions

1. **Register a sample the day it exists**, not when sequencing comes back. Fill in
   `library_id` and `raw_path` later.
2. **`sample_id` is never reused or edited.** If one is wrong, add a new row and mark the
   old one `fail`, explaining in `notes`.
3. **Never delete rows.** Failed and discarded samples stay. This table is the only
   evidence for why the final n is what it is.
4. **This file is the source of truth for grouping.** Analysis scripts read the design
   matrix from here; groups are never hard-coded in a script.
5. Tab-separated. Do not save directly from Excel — it rewrites dates and adds a BOM.
   If you must edit in Excel, export as UTF-8 tab-delimited text.

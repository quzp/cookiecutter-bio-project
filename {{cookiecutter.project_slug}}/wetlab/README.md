# wetlab/

**Human-written** records from the bench. Everything here is plain text or a small
table, and everything is tracked in git.

Instrument output — FASTQ files, microscopy images, FCS files, plate reader exports —
does **not** belong here. It goes to `data/raw/`. That keeps exactly one "raw data"
location in the project, so script paths and backup policy never fork. This directory
answers a different question: how those data came to exist.

| Subdirectory | Contents |
| --- | --- |
| `protocols/` | Reusable standard operating procedures, one method per file |
| `experiments/` | A complete record of one experiment, in `YYYYMMDD_short_name/` |
| `inventory/` | Plasmids, primers, antibodies, cell lines, gRNAs |

**Protocols vs. experiments:** `protocols/` describes *how something is done* — reusable,
versioned, revised over time. `experiments/` describes *what was done on a given day*,
which protocol version was used, and what came out. Experiment records are written once
and never rewritten.

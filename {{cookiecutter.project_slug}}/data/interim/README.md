# data/interim/

Intermediate results produced by scripts: aligned BAMs, deduplicated count matrices,
QC reports, temporary objects.

Everything here **must be deletable and fully reconstructible by scripts**. If deleting
a file here would make it unrecoverable, it belongs either in `raw/` (it is primary data)
or in `processed/` (it is a final product) — or the script that generates it is missing.

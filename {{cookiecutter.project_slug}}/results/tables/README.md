# results/tables/

Tabular output from analysis scripts: differential expression results, enrichment
results, QC summaries.

Conventions:

- Use `.tsv` or `.csv`, not `.xlsx` — Excel silently truncates precision and converts
  gene symbols to dates.
- Include a date or the source script number in the filename so supplementary tables can
  be traced back.
- Compress tables above ~50 MB as `.tsv.gz`.

# data/external/

Third-party data: public database downloads, collaborator datasets, reference genomes
and annotations.

**Every dataset needs a `SOURCE.md`** recording:

- Source URL or accession (GEO, ArrayExpress, ENA, Ensembl release)
- Download date and the exact command used
- Version identifiers (genome build such as `GRCh38.p14`, annotation such as `GENCODE v45`)
- License and citation requirements

Reference genomes and annotations are large and usually shared across projects. Rather
than copying them here, keep them in shared lab storage and point to them from
`management/config/config.yml`.

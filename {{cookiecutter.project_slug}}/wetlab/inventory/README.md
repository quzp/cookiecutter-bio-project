# inventory/

Material inventories, stored as `.tsv` — plain text, diffable in git, readable
directly by both R and Python.

Suggested files:

```
plasmids.tsv       ID, backbone, insert, resistance, source, freezer location
primers.tsv        ID, sequence, Tm, purpose, order date
guides.tsv         ID, target gene, protospacer, library / vector
antibodies.tsv     target, vendor, catalogue no., lot, dilution, validation status
cell_lines.tsv     name, source, passage, mycoplasma test date, freezer location
```

Conventions:

- IDs are never reused, even after a stock is exhausted. Keep the row and add a
  `status` column marked `depleted`.
- Sequences are uppercase, 5'->3', no spaces.
- Freezer locations are precise: `-80_A3 / box12 / C4`.

# protocols/

Standard operating procedures. One method per `.md` file, lowercase with underscores:

```
organoid_differentiation.md
lentivirus_packaging.md
rna_extraction_trizol.md
10x_library_prep.md
```

Conventions:

- Each protocol carries a version number and revision date at the top. When revising,
  append to the revision table at the bottom rather than deleting old content —
  experiments already performed under the old version must remain traceable.
- Record vendor and catalogue number for reagents, and model number for instruments.
  This is what the Methods section will need.
- When an experiment record cites a protocol, it cites the version:
  `protocol: organoid_differentiation.md v1.2`.

Start a new protocol by copying `TEMPLATE_protocol.md`.

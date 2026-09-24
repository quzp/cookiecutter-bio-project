# manuscript/draft/

Every saved version of the manuscript text. Nothing here is ever overwritten or deleted;
the newest version is simply the highest version number. Naming rules and status codes
are in `../README.md`.

```
draft/
├── VERSION_LOG.md                        one line per round shared or received
├── Manuscript_v00.01-260901_wip.docx
├── Manuscript_v01.00-260915_int.docx
├── Manuscript_v01.00-260922_cmt-JS.docx
├── Manuscript_v01.01-260925_rev.docx
├── Supplementary-Methods_v01.00-260915_int.docx
└── _archive/                             optional: earlier rounds, once the folder gets crowded
```

Quick rules:

- **New working session → new minor version** (`v01.01` → `v01.02`). Word's autosave is
  not a version; a copy you might want to return to is.
- **Leaves your hands → new major version** (`v01.03` → `v02.00`) and a line in
  `VERSION_LOG.md`.
- **Comments come back → keep the version they commented on**, change date and status:
  `Manuscript_v02.00-261010_cmt-JS.docx`.
- When a round is closed, you may move its files into `_archive/` to keep the latest
  round visible. Move, never delete.

## Writing in Quarto or Markdown instead of Word

Keep one source file, `manuscript.qmd`, plus `references.bib` exported from Zotero.
Git holds the history, so the source file is not renamed. Mark each round with a tag
and render a named snapshot for the people who read it:

```bash
git tag manuscript-v01.00
quarto render manuscript.qmd --to docx -o Manuscript_v01.00-260915_int.docx
```

Returned comments and the submitted file follow the naming rules above.

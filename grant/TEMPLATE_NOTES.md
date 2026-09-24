# Template Notes — grant template (v2.0)

- The template never fetches sponsor rules or writes application text automatically. Official sponsor documents are the only source of rules.
- RED-zone constraints live in `.ai/MASTER_INSTRUCTIONS.md` and in every prompt. If you edit the prompts, keep those constraints.
- Files inside `{{cookiecutter.project_slug}}/` are rendered by Jinja. Avoid literal `{{`, `{%`, or `{#` sequences in them; wrap such content in `{% raw %}...{% endraw %}` if needed.
- Extension ideas:
  - sponsor-specific variants of Prompt G (NIH R21, BrightFocus LOI/full, RPB, FFB) using each sponsor's published criteria;
  - an institution-specific routing checklist and AI-certification step;
  - automatic Zotero → `02_Evidence/references.bib` export (e.g., Better BibTeX auto-export);
  - analysis repositories linked as Git submodules or recorded by path — never store raw data in the grant repository.

- After editing, run `bash tests/bake_test.sh` from the repository root.

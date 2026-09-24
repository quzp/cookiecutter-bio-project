# cookiecutter-bio-project

A lightweight scaffold for biology research projects. One command creates a
**wet-lab + dry-lab** directory structure where every folder carries its own
README explaining what belongs in it — and nothing else.

The repository also ships a second template, [`grant/`](grant/), for **NIH-compliant,
AI-assisted grant development**. Both templates are selected from the same repository:

| Template | Command | Creates |
|---|---|---|
| Bio project (default) | `cookiecutter gh:quzp/cookiecutter-bio-project` | Wet-lab + dry-lab research project |
| Grant workflow | `cookiecutter gh:quzp/cookiecutter-bio-project --directory grant` | Gated grant-writing workspace with AI prompts and registers |

The philosophy follows [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)
and [cookiecutter-reproducible-science](https://github.com/mkrapp/cookiecutter-reproducible-science),
with three changes aimed at bench-plus-computation projects:

1. **Wet lab and dry lab live in one repository.** `wetlab/` holds what people write
   (protocols, experiment records, inventory); `data/` holds what instruments produce.
   There is exactly one "raw data" location, so script paths and backup policy never fork.
2. **`data/metadata/samples.tsv` is the single joint between the two sides.** It forces
   you to record which tube of cells corresponds to which FASTQ, on the day it happens.
3. **Environments are managed with [pixi](https://pixi.sh).** `pixi.lock` pins R,
   Bioconductor and Python dependencies across platforms, and does not require a
   pre-existing conda installation.

## Usage

```bash
# Install cookiecutter (uv or pipx keeps it out of your system Python)
uv tool install cookiecutter        # or: pipx install cookiecutter

# Generate from GitHub
cookiecutter gh:quzp/cookiecutter-bio-project

# ...or from a local clone
cookiecutter path/to/cookiecutter-bio-project
```

You will be prompted for:

| Field | Purpose |
| --- | --- |
| `project_name` | Full project title, e.g. `Retinal Organoid EZH2 Screen` |
| `project_slug` | Directory name; derived from the title by default |
| `project_short_description` | One line; written into README and CITATION.cff |
| `author_name` / `author_email` / `orcid` / `institution` | Author metadata |
| `github_username` | Used to print the remote-setup command at the end |
| `primary_language` | `R` / `Python` / `R + Python`; determines `pixi.toml` dependencies |
| `use_quarto` | Adds Quarto to the environment and ships notebook templates |
| `open_source_license` | `MIT` / `BSD-3-Clause` / `CC-BY-4.0` / `None` |
| `init_git_repo` | Runs `git init` and creates the first commit |

## Generated structure

```
your_project/
├── README.md                 <- Overview, directory map, working conventions
├── CHANGELOG.md              <- Data batches, method changes, manuscript versions
├── AUTHORS.md                <- Contributors, recorded by CRediT role
├── CITATION.cff              <- Machine-readable citation (GitHub / Zenodo)
├── LICENSE
├── pixi.toml                 <- Computational environment
├── .gitignore                <- Excludes bulk data and regenerable figures
├── .gitattributes            <- Line endings + optional Git LFS rules
│
├── wetlab/                   <- Human-written records; all tracked in git
│   ├── protocols/                Reusable SOPs, one method per file
│   ├── experiments/              One directory per experiment, YYYYMMDD_short_name/
│   └── inventory/                Plasmids, primers, antibodies, cell lines, gRNAs
│
├── data/                     <- Machine-generated data; excluded from git
│   ├── metadata/                 Sample sheet — the wet/dry joint (tracked in git)
│   ├── raw/                      Instrument output, read-only
│   ├── external/                 Public datasets, references, collaborator data
│   ├── interim/                  Intermediate results, always regenerable
│   └── processed/                Analysis-ready datasets
│
├── src/                      <- All code
│   ├── data/                     Preprocessing, QC, format conversion
│   ├── analysis/                 Statistics and modelling
│   ├── visualization/            Figure scripts
│   ├── notebooks/                Exploratory analysis (Quarto / Jupyter)
│   └── utils/                    Shared helpers: paths, config, plotting theme
│
├── results/                  <- Script output; regenerable, excluded from git
│   ├── figures/
│   └── tables/
│
├── manuscript/               <- Everything aimed at publication
│   ├── notes/                    Outline, storyline, figure plan
│   ├── drafts/                   Every version of every text, flat (vXX.YY-YYMMDD_status)
│   ├── main/                     Major versions of the main text, copied from drafts/
│   ├── figures/                  Hand-assembled final figures (tracked in git)
│   ├── supplement/
│   └── submission/               Per-journal versions, cover letters, rebuttals
│
└── management/               <- Running the project rather than doing the science
    ├── config/                   Analysis parameters and paths
    ├── docs/                     Literature notes, meeting minutes, method surveys
    └── reports/                  Progress reports, committee updates, grant reporting
```

## Grant workflow template

```bash
cookiecutter gh:quzp/cookiecutter-bio-project --directory grant
```

Creates a grant workspace organised around a seven-phase, gated workflow in which
**the PI writes the application and AI retrieves, computes, critiques, and verifies**,
in line with NIH NOT-OD-25-132 and the NIH Simplified Review Framework:

```
your_grant/
├── 00_Admin/            Brief, state, decision log, timeline, AI-use log,
│                        data classification, NIH application count
├── 01_Funding/          Official documents, compliance matrix, landscape, PO contact
├── 02_Evidence/         Claims register, evidence matrix, Zotero export
├── 03_Preliminary_Data/ Figure register, figures, source data, analysis-repo pointer
├── 04_Application/      PI writing workspace: notes/, flat drafts/, section folders
├── 05_Review/           AI + human review, reviewer risk register
├── 06_Submission/       Final compliance, submitted package
└── .ai/                 Master instructions, prompts A–G, handoff file, workflow
```

A grant's preliminary data usually come from a bio project: record that project's
repository in `analysis_repo`, and the grant's `03_Preliminary_Data/` will point to it
rather than duplicating data. See [`grant/README.md`](grant/README.md) and
[`grant/docs/GRANT_WORKFLOW_GUIDE.md`](grant/docs/GRANT_WORKFLOW_GUIDE.md).

## Customising the template

- **Add or remove directories:** edit the tree under `{{cookiecutter.project_slug}}/`.
  Every directory needs at least one file — git does not track empty directories,
  so an empty folder will never reach the generated project.
- **Add a prompt:** add a key to `cookiecutter.json` and reference it as
  `{{ cookiecutter.your_key }}` in any file content or file name.
- **Post-generation logic** lives in `hooks/post_gen_project.py` (license selection,
  date substitution, git init). Input validation lives in `hooks/pre_gen_project.py`.

- **Grant template** files live under `grant/` and are edited the same way
  (`grant/cookiecutter.json`, `grant/hooks/`, `grant/{{cookiecutter.project_slug}}/`).
- **Test both templates** before pushing: `bash tests/bake_test.sh`
  (GitHub Actions runs the same script on every push).

## License

The template is MIT licensed. Generated projects use whichever license you select.

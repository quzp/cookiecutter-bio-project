# cookiecutter-bio-project

A lightweight scaffold for biology research projects. One command creates a
**wet-lab + dry-lab** directory structure where every folder carries its own
README explaining what belongs in it — and nothing else.

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
cookiecutter gh:YOUR_GITHUB_USERNAME/cookiecutter-bio-project

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
│   ├── main/
│   ├── figures/                  Hand-assembled final figures (tracked in git)
│   ├── supplement/
│   └── submission/               Per-journal versions, cover letters, rebuttals
│
└── management/               <- Running the project rather than doing the science
    ├── config/                   Analysis parameters and paths
    ├── docs/                     Literature notes, meeting minutes, method surveys
    └── reports/                  Progress reports, committee updates, grant reporting
```

## Customising the template

- **Add or remove directories:** edit the tree under `{{cookiecutter.project_slug}}/`.
  Every directory needs at least one file — git does not track empty directories,
  so an empty folder will never reach the generated project.
- **Add a prompt:** add a key to `cookiecutter.json` and reference it as
  `{{ cookiecutter.your_key }}` in any file content or file name.
- **Post-generation logic** lives in `hooks/post_gen_project.py` (license selection,
  date substitution, git init). Input validation lives in `hooks/pre_gen_project.py`.

## License

The template is MIT licensed. Generated projects use whichever license you select.

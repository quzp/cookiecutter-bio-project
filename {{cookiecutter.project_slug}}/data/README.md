# data/

Machine-generated data. **Excluded from git by default** (see `.gitignore`) with two
exceptions: the README files, and all of `data/metadata/`.

Data flows in one direction, becoming more analysis-ready at each step:

```
raw/ ──────┐
           ├──► interim/ ──► processed/ ──► src/analysis/
external/ ─┘
```

| Subdirectory | Writable? | Contents |
| --- | --- | --- |
| `metadata/` | yes, tracked in git | Sample sheet; the joint between bench and computation |
| `raw/` | **no** | Instrument output. Run `chmod -R a-w data/raw` |
| `external/` | **no** | Public datasets, references, collaborator data |
| `interim/` | yes | Intermediate results; deletable and regenerable at any time |
| `processed/` | yes | Analysis-ready datasets |

**Backup:** these files are not in git and need an independent backup policy.
Record where the backup lives in the top-level README.

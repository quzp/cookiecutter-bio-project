# management/config/

Analysis parameters and paths. The point is that every threshold, version number and
external path lives in one place: scripts contain no magic numbers, changing a parameter
means editing one file, and the Methods section can be written from it directly.

`config.yml` is read by `load_config()` in `src/utils/paths.R` and `src/utils/paths.py`.

If a parameter differs between analyses, do not override it inside a script — give that
analysis its own section in `config.yml`.

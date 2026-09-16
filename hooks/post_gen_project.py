"""Post-generation: select license, fill dates, prune unused files, init git."""
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path.cwd()

LICENSE = "{{ cookiecutter.open_source_license }}"
INIT_GIT = "{{ cookiecutter.init_git_repo }}"
USE_QUARTO = "{{ cookiecutter.use_quarto }}"
LANGUAGE = "{{ cookiecutter.primary_language }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USER = "{{ cookiecutter.github_username }}"

LICENSE_SOURCES = {
    "MIT": "licenses/MIT.txt",
    "BSD-3-Clause": "licenses/BSD-3-Clause.txt",
    "CC-BY-4.0": "licenses/CC-BY-4.0.txt",
}

TEXT_SUFFIXES = {".md", ".txt", ".toml", ".yml", ".yaml", ".cff", ".tsv", ".R", ".py", ".qmd"}


def pick_license():
    if LICENSE in LICENSE_SOURCES:
        shutil.copy(PROJECT_DIR / LICENSE_SOURCES[LICENSE], PROJECT_DIR / "LICENSE")
    shutil.rmtree(PROJECT_DIR / "licenses", ignore_errors=True)


def fill_placeholders():
    today = datetime.date.today()
    repl = {"__YEAR__": str(today.year), "__DATE__": today.isoformat()}
    targets = [p for p in PROJECT_DIR.rglob("*") if p.is_file() and p.suffix in TEXT_SUFFIXES]
    lic = PROJECT_DIR / "LICENSE"
    if lic.exists():
        targets.append(lic)
    for path in targets:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = text
        for key, val in repl.items():
            new = new.replace(key, val)
        if new != text:
            path.write_text(new, encoding="utf-8")


def prune_notebooks():
    nb = PROJECT_DIR / "src" / "notebooks"
    if not nb.exists():
        return
    if USE_QUARTO != "yes":
        for f in nb.glob("*.qmd"):
            f.unlink()
    if LANGUAGE == "Python":
        for f in nb.glob("*_R.qmd"):
            f.unlink()
    if LANGUAGE == "R":
        for f in nb.glob("*_python.qmd"):
            f.unlink()
    if LANGUAGE == "R":
        util = PROJECT_DIR / "src" / "utils" / "paths.py"
        if util.exists():
            util.unlink()
    if LANGUAGE == "Python":
        util = PROJECT_DIR / "src" / "utils" / "paths.R"
        if util.exists():
            util.unlink()


def init_git():
    if INIT_GIT != "yes":
        return
    if shutil.which("git") is None:
        sys.stderr.write("WARNING: git not found; skipping repository initialisation.\n")
        return
    try:
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=PROJECT_DIR, check=True)
        subprocess.run(["git", "add", "-A"], cwd=PROJECT_DIR, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-m", "chore: scaffold project from cookiecutter-bio-project"],
            cwd=PROJECT_DIR,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        sys.stderr.write("WARNING: git init failed (%s); run it manually later.\n" % exc)


def goodbye():
    print("")
    print("  Project created: %s" % PROJECT_DIR)
    print("")
    print("  Next steps:")
    print("    cd %s" % PROJECT_SLUG)
    print("    pixi install            # resolve and lock the environment")
    print("    pixi run check          # verify the interpreter and core packages")
    print("")
    if GITHUB_USER:
        print("    git remote add origin git@github.com:%s/%s.git" % (GITHUB_USER, PROJECT_SLUG))
        print("    git push -u origin main")
        print("")
    print("  Read the Working conventions section in README.md before adding data.")
    print("")


if __name__ == "__main__":
    pick_license()
    prune_notebooks()
    fill_placeholders()
    init_git()
    goodbye()

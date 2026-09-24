"""Post-generation: prune resubmission folder, init git, print next steps."""
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path.cwd()
RESUB = "{{ cookiecutter.is_resubmission }}" == "yes"
INIT_GIT = "{{ cookiecutter.init_git }}" == "yes"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def prune_resubmission():
    intro = PROJECT_DIR / "04_Application" / "Introduction_Resubmission"
    if not RESUB and intro.exists():
        shutil.rmtree(intro)


def init_git():
    if not INIT_GIT:
        return
    if shutil.which("git") is None:
        sys.stderr.write("WARNING: git not found; skipping repository initialisation.\n")
        return
    try:
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=PROJECT_DIR, check=True)
        subprocess.run(["git", "add", "-A"], cwd=PROJECT_DIR, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-m", "chore: scaffold grant project from cookiecutter-bio-project/grant"],
            cwd=PROJECT_DIR,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        sys.stderr.write("WARNING: git init failed (%s); run it manually later.\n" % exc)


def goodbye():
    print("")
    print("  Grant project created: %s" % PROJECT_DIR)
    print("")
    print("  Next steps:")
    print("    cd %s" % PROJECT_SLUG)
    print("    1. Fill 00_Admin/PROJECT_BRIEF.md, APPLICATION_COUNT.md, DATA_CLASSIFICATION.md")
    print("    2. Put the official NOFO + instructions in 01_Funding/NOFO_and_Instructions/")
    print("    3. Paste .ai/MASTER_INSTRUCTIONS.md into ONE coordinator assistant")
    print("    4. Run .ai/prompts/A_compliance.md with .ai/handoffs/GRANT_HANDOFF.md")
    print("")
    print("  Rule: RED-zone text (Aims, Research Strategy, Summary, Narrative,")
    print("  resubmission Introduction, PO emails) is written by the PI.")
    print("")


if __name__ == "__main__":
    prune_resubmission()
    init_git()
    goodbye()

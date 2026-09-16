"""生成后处理：挑选许可证、填充日期、初始化 git 仓库。"""
import datetime
import os
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
    src_dir = PROJECT_DIR / "licenses"
    if LICENSE in LICENSE_SOURCES:
        shutil.copy(PROJECT_DIR / LICENSE_SOURCES[LICENSE], PROJECT_DIR / "LICENSE")
    shutil.rmtree(src_dir, ignore_errors=True)


def fill_placeholders():
    today = datetime.date.today()
    repl = {
        "__YEAR__": str(today.year),
        "__DATE__": today.isoformat(),
    }
    for path in PROJECT_DIR.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if path.name == "LICENSE" or path.suffix in TEXT_SUFFIXES:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            new = text
            for key, val in repl.items():
                new = new.replace(key, val)
            if new != text:
                path.write_text(new, encoding="utf-8")
    lic = PROJECT_DIR / "LICENSE"
    if lic.exists():
        text = lic.read_text(encoding="utf-8")
        for key, val in repl.items():
            text = text.replace(key, val)
        lic.write_text(text, encoding="utf-8")


def drop_unused_notebooks():
    nb = PROJECT_DIR / "notebooks"
    if USE_QUARTO != "yes":
        for f in nb.glob("*.qmd"):
            f.unlink()
    if LANGUAGE == "Python":
        for f in nb.glob("*_R.qmd"):
            f.unlink()
    if LANGUAGE == "R":
        for f in nb.glob("*_python.qmd"):
            f.unlink()


def init_git():
    if INIT_GIT != "yes":
        return
    if shutil.which("git") is None:
        sys.stderr.write("WARNING: 未找到 git，跳过仓库初始化。\n")
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
        sys.stderr.write("WARNING: git 初始化失败（%s），可稍后手动执行。\n" % exc)


def goodbye():
    print("")
    print("  项目已创建: %s" % PROJECT_DIR)
    print("")
    print("  下一步:")
    print("    cd %s" % PROJECT_SLUG)
    print("    pixi install            # 解析并锁定环境")
    print("    pixi run check          # 验证 R / Python 可用")
    print("")
    if GITHUB_USER:
        print("    git remote add origin git@github.com:%s/%s.git" % (GITHUB_USER, PROJECT_SLUG))
        print("    git push -u origin main")
        print("")
    print("  先读 README.md 里的\"工作约定\"，再开始往 wetlab/ 和 data/raw/ 放东西。")
    print("")


if __name__ == "__main__":
    pick_license()
    drop_unused_notebooks()
    fill_placeholders()
    init_git()
    goodbye()

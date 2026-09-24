"""Post-generation: select license, fill dates, prune unused files, write example drafts, init git."""
import datetime
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

PROJECT_DIR = Path.cwd()

LICENSE = "{{ cookiecutter.open_source_license }}"
INIT_GIT = "{{ cookiecutter.init_git_repo }}"
USE_QUARTO = "{{ cookiecutter.use_quarto }}"
LANGUAGE = "{{ cookiecutter.primary_language }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USER = "{{ cookiecutter.github_username }}"
EXAMPLES = "{{ cookiecutter.include_example_drafts }}" == "yes"

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


# ---- Example drafts -------------------------------------------------------
# Written with the standard library only, so generated projects need no extra
# packages. Each example explains its own file name.

STATUS_MEANING = {
    "wip": "work in progress; only you have seen it (minor-version bump)",
    "rev": "revising in response to comments (minor-version bump)",
    "int": "sent for internal review (major-version bump)",
    "frozen": "structure locked; later changes are wording only (major-version bump)",
    "final": "final candidate (major-version bump)",
    "submitted": "exactly what was submitted (same version as the final)",
}


def _example_lines(filename, note, copied_to):
    stem = filename.rsplit(".", 1)[0]
    doc, version_date, status = stem.split("_")
    version, date = version_date.split("-")
    major, minor = version[1:].split(".")
    if status.startswith("cmt-"):
        meaning = "returned with comments by %s (same version as the one they read)" % status[4:]
    else:
        meaning = STATUS_MEANING[status]
    lines = [
        "EXAMPLE FILE - delete it when you start writing",
        "",
        "File name:  " + filename,
        "Document:   " + doc,
        "Version:    %s  (major %s, minor %s)" % (version, major, minor),
        "Date:       %s  (20%s-%s-%s)" % (date, date[:2], date[2:4], date[4:]),
        "Status:     %s - %s" % (status, meaning),
        "",
        "What this version is: " + note,
    ]
    if copied_to:
        lines.append("Copied to:  " + ", ".join(copied_to))
    lines += ["", "Pattern: Document-Name_vXX.YY-YYMMDD_status.ext  (rules in drafts/README.md)"]
    return lines


def _xml_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_docx(path, lines):
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/></Relationships>'
    )
    paras = []
    for i, line in enumerate(lines):
        bold = "<w:rPr><w:b/></w:rPr>" if i == 0 else ""
        paras.append('<w:p><w:r>%s<w:t xml:space="preserve">%s</w:t></w:r></w:p>' % (bold, _xml_escape(line)))
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>" + "".join(paras) + "</w:body></w:document>"
    )
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document)


def write_pdf(path, lines):
    def esc(text):
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    ops = ["BT", "/F1 11 Tf", "14 TL", "72 740 Td"]
    for line in lines:
        ops.append("(%s) Tj T*" % esc(line))
    ops.append("ET")
    stream = "\n".join(ops).encode("latin-1", "replace")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for num, obj in enumerate(objects, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % num + obj + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    for off in offsets:
        out += b"%010d 00000 n \n" % off
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objects) + 1, xref)
    path.write_bytes(bytes(out))


def write_examples(drafts_dir, examples, log_rows):
    """examples: (filename, note, [folders relative to the project to copy into])."""
    for filename, note, copy_to in examples:
        target = drafts_dir / filename
        lines = _example_lines(filename, note, copy_to)
        if filename.endswith(".pdf"):
            write_pdf(target, lines)
        else:
            write_docx(target, lines)
        for folder in copy_to:
            dest = PROJECT_DIR / folder
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, dest / filename)
    log = drafts_dir / "VERSION_LOG.md"
    text = log.read_text(encoding="utf-8")
    empty_row = [l for l in text.splitlines() if l.replace("|", "").strip() == ""][-1]
    log.write_text(text.replace(empty_row, "\n".join(log_rows)), encoding="utf-8")


SUBMISSION = "manuscript/submission/01_Nat-Commun_261021"
MANUSCRIPT_EXAMPLES = [
    ("Cover-Letter_v00.01-261018_wip.docx", "first working save of the cover letter.", []),
    ("Cover-Letter_v01.00-261020_final.docx", "cover letter approved by all authors.", [SUBMISSION]),
    ("Cover-Letter_v01.00-261021_submitted.docx", "the cover letter as uploaded to the journal.", [SUBMISSION]),
    ("Manuscript_v00.01-260901_wip.docx", "first rough draft.", []),
    ("Manuscript_v00.04-260912_wip.docx", "fourth working save; nobody else has read it yet.", []),
    ("Manuscript_v01.00-260915_int.docx", "first complete draft, sent to co-authors.", ["manuscript/main"]),
    ("Manuscript_v01.00-260922_cmt-JS.docx", "JS's tracked changes and comments on v01.00.", []),
    ("Manuscript_v01.00-260923_cmt-AB.docx", "AB's tracked changes and comments on v01.00.", []),
    ("Manuscript_v01.01-260925_rev.docx", "merging JS's and AB's comments.", []),
    ("Manuscript_v02.00-261003_int.docx", "second round, sent to co-authors.", ["manuscript/main"]),
    ("Manuscript_v03.00-261020_final.docx", "approved by all authors.", ["manuscript/main"]),
    ("Manuscript_v03.00-261021_submitted.pdf", "PDF exported from the v03.00 final and submitted.",
     ["manuscript/main", SUBMISSION]),
]
MANUSCRIPT_LOG_ROWS = [
    "| 260915 | Manuscript_v01.00-260915_int.docx | int | First complete draft (example) | JS, AB |",
    "| 260922 | Manuscript_v01.00-260922_cmt-JS.docx | cmt-JS | Comments on v01.00 (example) | from JS |",
    "| 260923 | Manuscript_v01.00-260923_cmt-AB.docx | cmt-AB | Comments on v01.00 (example) | from AB |",
    "| 261003 | Manuscript_v02.00-261003_int.docx | int | Second round (example) | JS, AB |",
    "| 261020 | Manuscript_v03.00-261020_final.docx | final | Approved by all authors (example) | all authors |",
    "| 261021 | Manuscript_v03.00-261021_submitted.pdf | submitted | Submitted to Nat Commun (example) | journal |",
]


def write_example_drafts():
    if not EXAMPLES:
        return
    write_examples(PROJECT_DIR / "manuscript" / "drafts", MANUSCRIPT_EXAMPLES, MANUSCRIPT_LOG_ROWS)


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
    write_example_drafts()
    init_git()
    goodbye()

"""Post-generation: prune resubmission folder, write example drafts, init git, print next steps."""
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

PROJECT_DIR = Path.cwd()
RESUB = "{{ cookiecutter.is_resubmission }}" == "yes"
INIT_GIT = "{{ cookiecutter.init_git }}" == "yes"
EXAMPLES = "{{ cookiecutter.include_example_drafts }}" == "yes"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def prune_resubmission():
    intro = PROJECT_DIR / "04_Application" / "Introduction_Resubmission"
    if not RESUB and intro.exists():
        shutil.rmtree(intro)


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


AIMS = "04_Application/Specific_Aims"
STRATEGY = "04_Application/Research_Strategy"
GRANT_EXAMPLES = [
    ("Research-Strategy_v00.01-261020_wip.docx", "first working save of the Research Strategy.", []),
    ("Research-Strategy_v01.00-261105_int.docx", "first complete Research Strategy, sent to co-investigators.", [STRATEGY]),
    ("Specific-Aims_v00.01-261001_wip.docx", "first rough Aims page.", []),
    ("Specific-Aims_v00.05-261008_wip.docx", "fifth working save; nobody else has read it yet.", []),
    ("Specific-Aims_v01.00-261010_int.docx", "first complete Aims page, sent to two colleagues.", [AIMS]),
    ("Specific-Aims_v01.00-261015_cmt-JS.docx", "JS's tracked changes and comments on v01.00.", []),
    ("Specific-Aims_v01.01-261017_rev.docx", "revising after JS's comments and the Prompt D stress test.", []),
    ("Specific-Aims_v02.00-261022_frozen.docx", "Aims architecture frozen at gate G3.", [AIMS]),
    ("Specific-Aims_v03.00-261210_final.docx", "final candidate for the P7 compliance check.", [AIMS]),
    ("Specific-Aims_v03.00-261212_submitted.pdf", "PDF exported from the v03.00 final and submitted.",
     [AIMS, "06_Submission/Submitted"]),
]
GRANT_LOG_ROWS = [
    "| 261010 | Specific-Aims_v01.00-261010_int.docx | int | First complete Aims page (example) | JS, AB |",
    "| 261015 | Specific-Aims_v01.00-261015_cmt-JS.docx | cmt-JS | Comments on v01.00 (example) | from JS |",
    "| 261022 | Specific-Aims_v02.00-261022_frozen.docx | frozen | Architecture frozen at G3 (example) | |",
    "| 261105 | Research-Strategy_v01.00-261105_int.docx | int | First complete Strategy (example) | co-investigators |",
    "| 261210 | Specific-Aims_v03.00-261210_final.docx | final | Final candidate (example) | |",
    "| 261212 | Specific-Aims_v03.00-261212_submitted.pdf | submitted | Submitted package (example) | sponsor |",
]
AI_EXAMPLE = """# EXAMPLE FILE - delete it when you start writing

File name: Specific-Aims_v01.00-261012_AI-D.md

- Document reviewed: Specific-Aims
- Version reviewed:  v01.00 (the file in drafts/ that the AI read)
- Date of review:    261012
- Status:            AI-D - output of Prompt D (Aims stress test)

AI review outputs live here, never in 04_Application/, and are named after the
draft version they read.
"""


def write_example_drafts():
    if not EXAMPLES:
        return
    write_examples(PROJECT_DIR / "04_Application" / "drafts", GRANT_EXAMPLES, GRANT_LOG_ROWS)
    ai = PROJECT_DIR / "05_Review" / "AI_Review" / "Specific-Aims_v01.00-261012_AI-D.md"
    ai.write_text(AI_EXAMPLE, encoding="utf-8")


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
    print("    5. Write in 04_Application/drafts/ (version rules: 04_Application/drafts/README.md)")
    print("")
    print("  Rule: RED-zone text (Aims, Research Strategy, Summary, Narrative,")
    print("  resubmission Introduction, PO emails) is written by the PI.")
    print("")


if __name__ == "__main__":
    prune_resubmission()
    write_example_drafts()
    init_git()
    goodbye()

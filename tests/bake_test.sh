#!/usr/bin/env bash
# Render every template in this repository and check the output.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$(mktemp -d)"
trap 'rm -rf "$OUT"' EXIT

git config --global user.email >/dev/null 2>&1 || git config --global user.email "ci@example.com"
git config --global user.name  >/dev/null 2>&1 || git config --global user.name  "CI"

fail() { echo "FAIL: $*"; exit 1; }
no_jinja() { if grep -rIl -e '{{' -e '{%' "$1" --exclude-dir=.git; then fail "unrendered Jinja tags in $1"; fi; }

echo "== bio template (root) =="
cookiecutter --no-input "$REPO" -o "$OUT" project_name="Test Bio" init_git_repo=yes
test -d "$OUT/test_bio/.git"       || fail "bio: git not initialized"
test -f "$OUT/test_bio/pixi.toml"  || fail "bio: pixi.toml missing"
test -d "$OUT/test_bio/wetlab"     || fail "bio: wetlab missing"
test -f "$OUT/test_bio/manuscript/drafts/VERSION_LOG.md" || fail "bio: manuscript version log missing"
test -f "$OUT/test_bio/manuscript/drafts/README.md"      || fail "bio: manuscript version rules missing"
test -f "$OUT/test_bio/manuscript/main/README.md"        || fail "bio: manuscript/main missing"
test -f "$OUT/test_bio/manuscript/notes/README.md"      || fail "bio: manuscript notes missing"
test ! -e "$OUT/test_bio/manuscript/draft"              || fail "bio: obsolete manuscript/draft present"
test -f "$OUT/test_bio/manuscript/drafts/Manuscript_v01.00-260915_int.docx" || fail "bio: example draft missing"
test -f "$OUT/test_bio/manuscript/main/Manuscript_v01.00-260915_int.docx"   || fail "bio: example major version not copied to main/"
grep -q "(example)" "$OUT/test_bio/manuscript/drafts/VERSION_LOG.md"      || fail "bio: example log rows missing"
test -z "$(find "$OUT/test_bio/manuscript/drafts" -mindepth 1 -type d)"  || fail "bio: drafts/ must stay flat"
test -z "$(git -C "$OUT/test_bio" status --porcelain)"                     || fail "bio: example files not in first commit"

echo "== bio template, no example drafts =="
cookiecutter --no-input "$REPO" -o "$OUT" project_name="Test Bio Empty" include_example_drafts=no init_git_repo=no
test -z "$(find "$OUT/test_bio_empty/manuscript" -name "*.docx" -o -name "*.pdf")" || fail "bio: example files created with include_example_drafts=no"
grep -q "(example)" "$OUT/test_bio_empty/manuscript/drafts/VERSION_LOG.md" && fail "bio: example log rows with include_example_drafts=no"

echo "== grant template (--directory grant), new application =="
cookiecutter --no-input "$REPO" --directory grant -o "$OUT" \
  project_name="Test New Grant" is_resubmission=no init_git=yes
NEW="$OUT/test_new_grant"
test -d "$NEW/.git"                                        || fail "grant: git not initialized"
test ! -e "$NEW/04_Application/Introduction_Resubmission" || fail "grant: resubmission dir in new application"
for d in notes drafts Specific_Aims Research_Strategy Summary_Narrative Other_Attachments; do
  test -d "$NEW/04_Application/$d" || fail "grant: 04_Application/$d missing"
done
test -f "$NEW/04_Application/drafts/VERSION_LOG.md"        || fail "grant: version log missing"
test -f "$NEW/04_Application/drafts/README.md"             || fail "grant: version rules missing"
test -z "$(find "$NEW/04_Application/drafts" -mindepth 1 -type d)" || fail "grant: drafts/ must stay flat"
test -f "$NEW/04_Application/drafts/Specific-Aims_v02.00-261022_frozen.docx"       || fail "grant: example draft missing"
test -f "$NEW/04_Application/Specific_Aims/Specific-Aims_v02.00-261022_frozen.docx" || fail "grant: example major version not copied up"
test -f "$NEW/06_Submission/Submitted/Specific-Aims_v03.00-261212_submitted.pdf"    || fail "grant: example submitted file not copied"
test -f "$NEW/05_Review/AI_Review/Specific-Aims_v01.00-261012_AI-D.md"              || fail "grant: example AI review missing"
for p in A_compliance B_landscape C_evidence D_aims_stress_test E_preliminary_data F_audit_and_line_edit G_simplified_review; do
  test -s "$NEW/.ai/prompts/$p.md" || fail "grant: missing prompt $p"
done
test ! -e "$NEW/wetlab"                                    || fail "grant: bio files leaked into grant project"
no_jinja "$NEW"

echo "== grant template, resubmission =="
cookiecutter --no-input "$REPO" --directory grant -o "$OUT" \
  project_name="Test Resub Grant" is_resubmission=yes include_example_drafts=no init_git=no
RES="$OUT/test_resub_grant"
test -f "$RES/04_Application/Introduction_Resubmission/SUMMARY_STATEMENT_RESPONSE_TABLE.md" || fail "grant: resubmission table missing"
grep -q "Test Resub Grant" "$RES/00_Admin/PROJECT_BRIEF.md" || fail "grant: brief not rendered"
test -z "$(find "$RES/04_Application" "$RES/05_Review" "$RES/06_Submission" -name "*.docx" -o -name "*.pdf" -o -name "*_AI-*")" || fail "grant: example files created with include_example_drafts=no"
no_jinja "$RES"

echo "== grant template, invalid deadline is rejected =="
if cookiecutter --no-input "$REPO" --directory grant -o "$OUT" project_name="Bad Date" deadline="Feb 5" >/dev/null 2>&1; then
  fail "grant: invalid deadline accepted"
fi

echo "All bake tests passed."

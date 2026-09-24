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

echo "== grant template (--directory grant), new application =="
cookiecutter --no-input "$REPO" --directory grant -o "$OUT" \
  project_name="Test New Grant" is_resubmission=no init_git=yes
NEW="$OUT/test_new_grant"
test -d "$NEW/.git"                                        || fail "grant: git not initialized"
test ! -e "$NEW/04_Application/Introduction_Resubmission"  || fail "grant: resubmission dir in new application"
for p in A_compliance B_landscape C_evidence D_aims_stress_test E_preliminary_data F_audit_and_line_edit G_simplified_review; do
  test -s "$NEW/.ai/prompts/$p.md" || fail "grant: missing prompt $p"
done
test ! -e "$NEW/wetlab"                                    || fail "grant: bio files leaked into grant project"
no_jinja "$NEW"

echo "== grant template, resubmission =="
cookiecutter --no-input "$REPO" --directory grant -o "$OUT" \
  project_name="Test Resub Grant" is_resubmission=yes init_git=no
RES="$OUT/test_resub_grant"
test -f "$RES/04_Application/Introduction_Resubmission/SUMMARY_STATEMENT_RESPONSE_TABLE.md" || fail "grant: resubmission table missing"
grep -q "Test Resub Grant" "$RES/00_Admin/PROJECT_BRIEF.md" || fail "grant: brief not rendered"
no_jinja "$RES"

echo "== grant template, invalid deadline is rejected =="
if cookiecutter --no-input "$REPO" --directory grant -o "$OUT" project_name="Bad Date" deadline="Feb 5" >/dev/null 2>&1; then
  fail "grant: invalid deadline accepted"
fi

echo "All bake tests passed."

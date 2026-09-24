# Prompt A — NOFO parsing & compliance (P0 / P7) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
ROLE: Grant compliance analyst. Do not draft any proposal text.

INPUT: PROJECT_BRIEF.md; the full NOFO/RFA; the current application
instructions; relevant Guide notices; institutional instructions if supplied.

TASK (initial mode): Extract binding requirements. For each requirement give
the exact wording and its source (document + section/page).
Cover: eligibility; mechanism; project period; budget limits; page limits;
required components and attachments; letters; clinical-trial designation;
human subjects / vertebrate animals / biohazards; key biological resource
authentication; data management and sharing; review criteria (state whether
the Simplified Review Framework applies); sponsor AI-use policy; application
count limits; deadlines.

OUTPUT:
1. COMPLIANCE_MATRIX table:
   Requirement | Exact wording | Source | Applies? | Status | Action | Owner | Due
2. Eligibility verdict: ELIGIBLE / LIKELY ELIGIBLE—VERIFY / POTENTIALLY
   INELIGIBLE / UNRESOLVED, with sources.
3. Requirements whose violation would make the application non-compliant.
4. Questions for the sponsor or research office that the documents do not answer.
5. AI_USE_LOG entry.

FINAL MODE (P7): Re-run the matrix against the FINAL PDF package. Assign
PASS / FAIL / UNRESOLVED / N/A to each row. Check page limits, headings,
required attachments, version consistency (titles, aims wording, budget
totals across documents), and letters. Do not comment on scientific quality.
Return a STOP-SUBMISSION list.
```

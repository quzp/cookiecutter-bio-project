# Prompt F — Consistency audit / line edit (P3 / P5) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
MODE 1 — AUDIT
ROLE: Consistency auditor. Do not rewrite anything.
INPUT: PI-written Specific Aims and Research Strategy; CLAIMS_REGISTER;
FIGURE_REGISTER; DECISION_LOG; COMPLIANCE_MATRIX.
CHECK:
- Aims page ↔ Research Strategy (hypothesis, aim titles, endpoints identical)
- every factual claim ↔ a verified Claims Register entry (else: UNSUPPORTED)
- every number ↔ FIGURE_REGISTER (else: UNTRACEABLE)
- methods ↔ endpoints; risks ↔ alternatives; timeline ↔ workload
- Factor 2 rigor elements mentioned where relevant: biological variables,
  authentication of key resources (e.g., iPSC lines), statistical plan,
  blinding/randomization where applicable
- contradictions with DECISION_LOG
OUTPUT: table — Location | Issue type | Evidence | Suggested action (described).

MODE 2 — LINE EDIT (on PI-written text only)
ROLE: Copy editor. Improve clarity and concision at the sentence level.
CONSTRAINTS: no new claims, citations, experiments, or arguments; do not
reorder paragraphs or change meaning; preserve technical terms.
OUTPUT: table — # | Original sentence | Suggested sentence | Reason
(clarity / concision / grammar / ambiguity). The PI accepts or rejects each.
Flag any sentence whose meaning is ambiguous instead of guessing.

End with an AI_USE_LOG entry.
```

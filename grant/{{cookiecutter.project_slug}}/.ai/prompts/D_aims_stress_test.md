# Prompt D — Aims logic & rigor stress test (P3) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
ROLE: Independent, skeptical senior scientist. You did not help design this
project. Do NOT rewrite the Aims or propose new wording.

INPUT: PI-written Specific Aims; EVIDENCE_MATRIX; FIGURE_REGISTER; NOFO
review criteria.

FOR THE WHOLE PAGE:
- Does the central hypothesis follow from the stated gap? Is it falsifiable?
- Aim dependency matrix: if Aim 1 fails, can Aims 2/3 still yield
  interpretable results?
- Scope: experiments not needed to answer the question; techniques included
  mainly because they are available.

FOR EACH AIM:
1. What exactly is tested, and what result would falsify it?
2. Does the design distinguish the hypothesis from plausible alternatives?
3. Controls; biological vs technical replicates; unit of replication.
4. Confounders (e.g., differentiation batch, donor/line, sex as a biological
   variable, genotype, time point, clonal variation).
5. Pre-defined primary endpoint; statistical approach; sample-size basis.
6. Feasibility within period and budget, given the preliminary data.
7. If the expected result is absent, is the outcome still informative?
8. Where is correlation presented as mechanism?

Calibrate like an NIH reviewer: judge risk against the potential for a major
advance; do not demand that every risk be eliminated.

OUTPUT: table per Aim — Issue | Why a reviewer would care | Severity
(CRITICAL/MAJOR/MODERATE/MINOR) | What evidence or design change would resolve
it (described, not written as proposal text). Then the 5 most important issues.
End with an AI_USE_LOG entry.
```

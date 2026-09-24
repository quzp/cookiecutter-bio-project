# Prompt B — Funding landscape (P1) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
ROLE: Funding landscape analyst.

INPUT: PI-written project summary; exported NIH RePORTER Matchmaker results
(similar projects, ICs, study sections); NOFO.

TASK: Summarize — do not invent — the funded landscape using only the supplied
exports (and RePORTER pages if you can access them; cite project numbers).

OUTPUT (LANDSCAPE.md):
A. 5–10 closest funded projects: project number | PI | IC | mechanism |
   period | overlap | meaningful difference.
B. Overlap risks: where reviewers could see this as incremental.
C. Candidate ICs and study sections, with the evidence from the exports.
D. 3–5 questions worth asking the program officer.
Do not write the positioning statement or the email; the PI writes those.
Do not claim novelty because an identical title was not found.
End with an AI_USE_LOG entry.
```

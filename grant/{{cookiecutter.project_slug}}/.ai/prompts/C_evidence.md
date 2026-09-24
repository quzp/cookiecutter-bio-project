# Prompt C — Evidence & citation verification (P2) 🟢

Run in a new conversation. Attach `.ai/handoffs/GRANT_HANDOFF.md` and the source files it lists. Append the returned log line to `00_Admin/AI_USE_LOG.md`.

```text
ROLE: Scientific evidence analyst. Do not write proposal text.

INPUT: CLAIMS_REGISTER.md (PI-listed claims); existing Zotero export.

TASK for each claim:
1. Find supporting AND contradicting primary evidence (prefer primary studies
   over reviews for mechanistic claims; flag preprints).
2. For each citation, confirm from the abstract or full text that it actually
   supports the claim as worded. Give the relevant finding in one sentence
   and the PMID/DOI.
3. Rate evidence: Strong / Moderate / Preliminary / Conflicting / Insufficient.
4. Note model system and human relevance.

OUTPUT:
- EVIDENCE_MATRIX rows:
  Claim ID | Claim | Supporting (PMID) | Contradicting (PMID) | Model |
  Human relevance | Strength | Key uncertainty
- Claims that are overstated as worded, with a suggested narrower wording
  for the PI to consider (one line each).
- Candidate knowledge gaps supported by the matrix (bulleted, not prose).
- Citations you could not verify, marked UNVERIFIED.
Never cite a paper you have not retrieved. End with an AI_USE_LOG entry.
```

# GRANT WORKFLOW (v2.0)

Full guide: `grant/docs/GRANT_WORKFLOW_GUIDE.md` in https://github.com/quzp/cookiecutter-bio-project

## 1. Policy basis (read before starting)

**(1) NIH position on AI-generated applications.** Under [NOT-OD-25-132](https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html) (effective for applications submitted on or after 25 September 2025), NIH will not consider applications that are substantially developed by AI, or that contain sections substantially developed by AI, to be the original ideas of the applicants. AI tools may be appropriate to assist with limited aspects of application preparation or in specific circumstances. If inappropriate AI use is detected after award, NIH may refer the matter to the Office of Research Integrity and take enforcement actions such as disallowing costs, suspension, or termination. Some institutions require PIs to certify at routing that the application was not substantially developed by AI (see, for example, [UCSF OSR guidance](https://osr.ucsf.edu/news/not-od-25-132-ai-and-submission-limits-guidance-for-nih-applications)). **Ask your sponsored-programs office whether your institution requires a similar certification.**

**(2) Maximum of six applications per PI per year.** The same notice limits each PI (including MPIs) to six new, renewal, resubmission, or revision applications per calendar year. Some activity codes (e.g., T, R13) are excluded; confirm current exceptions in the NIH Grants Policy Statement. Phase 0 checks how many slots are already used.

**(3) Current review framework.** Most research project grants (R01, R21, etc.) are reviewed under the [Simplified Review Framework](https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework):
- **Factor 1: Importance of the Research** (Significance, Innovation), scored 1–9
- **Factor 2: Rigor and Feasibility** (Approach), scored 1–9
- **Factor 3: Expertise and Resources** (Investigators, Environment), rated sufficient or not sufficient

NIH reviewer guidance asks reviewers to evaluate risk in the context of the potential for major advances rather than to seek to eliminate it ([Yale mock study section guide](https://mockstudy.yale.edu/wp-content/uploads/2025/03/scoring_simplified_review_r_proposals.pdf)). An AI reviewer that tries to "fix" every risk may push the Approach toward excessive caution.

> Non-NIH sponsors (e.g., BrightFocus, RPB, FFB) have their own AI policies and review criteria. Extract them from the sponsor's official documents in Phase 0; do not assume NIH rules apply.
>
> This template is not legal or compliance advice. The sponsor and your institution's research office are the authorities on policy interpretation.

---

## 2. Core rule: three writing zones

Every part of the application falls into one of these zones. **Each prompt enforces this rule, and AI is instructed to decline drafting RED-zone content.**

| Zone | Content | AI may | AI may not |
|---|---|---|---|
| 🔴 **RED — PI-authored** | Specific Aims; Significance and Innovation arguments; Approach rationale, design, expected outcomes, interpretation, pitfalls and alternatives; Project Summary/Abstract; Project Narrative; Resubmission Introduction; emails to program officers | Ask questions; list required elements; critique PI-written text; check claims against evidence; give itemized sentence-level edit **suggestions** that the PI accepts or rejects | Draft or rewrite paragraphs; introduce new scientific arguments or experiments |
| 🟡 **YELLOW — limited assistance** | Figure legends (from facts in FIGURE_REGISTER); factual budget-justification items; facilities/equipment lists (from existing institutional or core-facility material); reference formatting | Produce a first pass from registered facts only | Add anything not in the supplied records |
| 🟢 **GREEN — AI-led support** | Compliance matrix; funding landscape; literature retrieval and citation verification; evidence matrix; data analysis and figures (with code); design stress tests; consistency audits; reviewer simulation; formatting checks | All of it | Make the scientific judgment for the PI |

YELLOW-zone output must still be verified and revised by the PI. Whether a use counts as a "limited aspect" is the PI's judgment; when in doubt, treat it as RED.

**Log every AI-assisted task in `00_Admin/AI_USE_LOG.md`** (tool, task, inputs, how the output was used, how the PI verified it). The log supports institutional certification and answers any later questions from a PO or auditor.

---

## 5. Seven-phase workflow (with backward timeline)

The example is an R01 planned backward from the deadline **T**. Compress proportionally for an R21 or a foundation LOI. **First confirm your institution's internal routing deadline (usually several business days before T) and record it in `TIMELINE.md`.**

| Phase | Window | Key outputs | Author | Gate |
|---|---|---|---|---|
| **P0 Setup & rules** | T−16 to T−14 wk | Compliance matrix, application count, data classification, timeline | AI (Prompt A) + PI verification | G0 |
| **P1 Positioning & PO** | T−15 to T−12 wk | LANDSCAPE.md, one-page concept, PO contact | PI writes concept; AI summarizes landscape (Prompt B) | G1 |
| **P2 Evidence** | T−14 to T−10 wk | Evidence matrix, claims register, knowledge-gap sentence | AI retrieves and verifies (Prompt C); PI writes gap sentence | G2 |
| **P3 Aims & stress test** | T−12 to T−9 wk | Specific Aims `v01.00` (PI) → stress-test report → `v02.00_frozen` | PI writes; AI critiques (Prompt D) | G3 |
| **P4 Preliminary data** | T−12 to T−6 wk (parallel with P2–P3) | Figures, source data, code, FIGURE_REGISTER | AI analyzes (Prompt E); PI writes conclusions | G4 |
| **P5 Research Strategy** | T−9 to T−4 wk | Research Strategy `v01.00` → `v03.00` | PI writes; AI audits and suggests edits (Prompt F) | G5 |
| **P6 Review** | T−5 to T−3 wk | AI review, human review, risk register | AI (Prompt G) + 2–3 colleagues | G6 |
| **P7 Compliance & submission** | T−3 wk to internal deadline | FINAL_COMPLIANCE, AI-use record, submission | AI (Prompt A final mode) + PI | G7 |

### P0 — Setup & rules

**Steps**
1. Generate the project with `cookiecutter`; complete `PROJECT_BRIEF.md`.
2. Download the official NOFO, application instructions, and relevant NIH Guide notices into `01_Funding/NOFO_and_Instructions/` (archive PDFs; record URL and download date).
3. Run **Prompt A** to produce `COMPLIANCE_MATRIX.md`. The PI spot-checks at least the page limits, deadline, budget cap, and clinical-trial designation against the original text.
4. List this calendar year's submitted and planned NIH applications in `APPLICATION_COUNT.md`; confirm you are within the limit.
5. Complete `DATA_CLASSIFICATION.md`: which data may go to cloud AI, which only to local-compute tools, and which to no AI tool. For IRB-governed or patient-derived material, confirm with your IRB/IT first.
6. Ask your sponsored-programs office for the internal deadline, any AI-use certification, and non-NIH sponsor AI policies. Record answers in `TIMELINE.md` and `OPEN_QUESTIONS.md`.

**G0 passes when:** eligibility confirmed; mechanism correct; page, budget, and deadline limits recorded with sources; application count within limit; data classification complete; internal deadline known.

### P1 — Positioning & program officer

**Steps**
1. The PI writes a 250–300-word project summary (🔴) and runs it through [RePORTER Matchmaker](https://reporter.nih.gov/matchmaker); export similar projects, ICs, and study sections.
2. Run **Prompt B** to summarize the exports into `LANDSCAPE.md`: closest funded projects, overlap risks, differentiators, candidate ICs and study sections, questions for the PO.
3. The PI writes a one-page concept (problem, gap, hypothesis, 2–3 aim titles) and the email to the PO (🔴) in `04_Application/notes/`; log it in `PO_CONTACT.md`.
4. Record PO feedback (fit with IC priorities, suggested study section, mechanism) in `DECISION_LOG.md`.

**G1 passes when:** you can state in one paragraph why this IC and this mechanism; the PO has been contacted (or the reason not to is recorded); overlap risks are known.

### P2 — Evidence

**Steps**
1. The PI lists the 10–20 core claims the application depends on (e.g., "X regulates Y during cone maturation") in `CLAIMS_REGISTER.md`.
2. Run **Prompt C**: retrieve supporting and contradicting evidence, fill `EVIDENCE_MATRIX.md`, rate evidence strength, and verify from the abstract or full text that each citation supports the claim as worded.
3. Add every adopted reference to the Zotero collection; the claims register records only Zotero citation keys.
4. The PI marks each row "PI-verified" after reading at least the relevant passage of the key papers.
5. The PI writes the knowledge-gap sentence:
   > The field knows ________, but does not yet know ________, and this uncertainty prevents ________.

**G2 passes when:** every core claim has a strength rating and verified references; the PI-written gap sentence is supported by the evidence matrix.

### P3 — Aims architecture & stress test

**Steps**
1. The PI writes Specific Aims (🔴) in `04_Application/drafts/`, saving working versions as `v00.xx_wip` and the first shareable page as `v01.00` (copied to `04_Application/Specific_Aims/`). It can be rough, but the logic must be the PI's. A useful skeleton: problem → gap → central hypothesis → Aims 1/2/3 (one sentence for the question, one for the approach) → expected outcomes.
2. In a **new conversation**, run **Prompt D**: dependency matrix, falsifiability, controls and confounders, sample size, feasibility, and whether a negative result would still be informative. AI returns an issue list only and does not rewrite the Aims.
3. The PI accepts or rejects each issue, records decisions in `DECISION_LOG.md`, and revises (`v01.01_rev`, …) until the architecture can be frozen.
4. Optional: use Prompt F line-edit mode for sentence-level suggestions on the revised Aims.

**G3 passes when:** all CRITICAL issues are resolved; each Aim answers "why does it exist / what result supports or challenges the hypothesis / can other Aims proceed if it fails"; the frozen version `Specific-Aims_vXX.00-YYMMDD_frozen.docx` is saved in `04_Application/drafts/` and copied to `04_Application/Specific_Aims/`.

### P4 — Preliminary data (parallel with P2–P3)

**Steps**
1. Check `DATA_CLASSIFICATION.md` to confirm which tool may process which data.
2. Run **Prompt E** in Claude Science (new analyses) or Codex/Claude Code (existing repositories). Every figure needs the figure, source data, code path and commit, statistical method, and software versions.
3. AI fills `FIGURE_REGISTER.md`, including both "supported conclusion" and "**not** supported — do not claim".
4. The PI writes the Preliminary Data text (🔴); every number must appear in FIGURE_REGISTER. AI may draft legends from the register (🟡); the PI verifies.

**G4 passes when:** every statement about preliminary data traces to a specific figure, table, and code; no conclusion depends on inferences outside the register.

### P5 — Research Strategy

**Steps**
1. The PI writes Significance, Innovation, and Approach from the frozen Aims (🔴), in `04_Application/drafts/` (major versions copied to `04_Application/Research_Strategy/`). Each Aim's Approach covers at least: rationale; design (groups, controls, biological replicates, primary endpoint); analysis and statistics; expected outcomes and interpretation; pitfalls and alternatives; milestones.
2. After each major section, run **Prompt F (audit mode)**: Aims ↔ Strategy consistency; claims ↔ claims register; numbers ↔ figure register; methods ↔ endpoints; risks ↔ alternatives; Factor 2 rigor elements (biological variables, authentication of key resources, statistical plan).
3. When useful, run **Prompt F (line-edit mode)**: AI returns an "original / suggestion / reason" table rather than a rewrite. The PI accepts items one by one and logs the session in AI_USE_LOG.
4. Resubmissions: the PI writes the Introduction (🔴), responding to each point in the summary statement. AI may do one thing here: tabulate every critique and check that the Introduction and the body address each one.

**G5 passes when:** the audit shows no unresolved inconsistency or unsupported claim; page limits are met.

### P6 — Review

**Steps**
1. In a fresh conversation using a **different vendor's** model from P3, run **Prompt G** (Simplified Review Framework). Optionally run it twice, once emphasizing Factor 1 and once Factor 2.
2. **In parallel**, send the Aims and Research Strategy to 2–3 colleagues (at least one outside your subfield) with at least one week to respond, using the Factor 1/2/3 format (`05_Review/Human_Review/REQUEST_TEMPLATE.md`).
3. Merge all comments into `REVIEWER_RISK_REGISTER.md`, tagging each as AI or human. Issues raised by both get priority.
4. The PI revises the text (🔴) and records each resolution in the register.

**G6 passes when:** every FATAL/MAJOR issue is resolved or has a documented reason for not resolving it; at least one human review is complete.

### P7 — Compliance & submission

**Steps**
1. Run **Prompt A final mode** on the **final PDF package** to produce `FINAL_COMPLIANCE.md` and a STOP-SUBMISSION list.
2. The PI checks each STOP item by hand.
3. Finalize `AI_USE_LOG.md` and confirm all 🔴 content was written by the PI; use it for any institutional certification.
4. Complete `00_Admin/SUBMISSION_CHECKLIST.md` and route to your sponsored-programs office.

**PI final checklist**
- [ ] The central hypothesis and Aims are my own scientific ideas; I can explain them to a PO or reviewer without any AI.
- [ ] All 🔴 text was written by me (or co-authors); AI provided only critique, verification, and itemized edit suggestions.
- [ ] I have read the relevant passage of every citation; no fabricated or misattributed references.
- [ ] Every number can be found in FIGURE_REGISTER or source data.
- [ ] Collaborator commitments, facilities, and resources are accurate; letters are in hand.
- [ ] This year's NIH application count is within the limit.
- [ ] No data restricted by DATA_CLASSIFICATION was given to any AI tool.
- [ ] The STOP-SUBMISSION list is empty.

---

## 11. Definition of "ready to submit"

```text
Eligibility and compliance verified (with sources)
+ within this year's NIH application limit
+ knowledge gap and central hypothesis originate with the PI and are supported by the evidence matrix
+ Aims survive the stress test and remain informative if one fails
+ every number traces to FIGURE_REGISTER; every citation verified by the PI
+ all RED-zone text written by the PI; AI use logged
+ FATAL/MAJOR issues from AI and human review resolved
+ STOP-SUBMISSION list for the final PDF package is empty
```

---

## Sources

- NIH NOT-OD-25-132, *Supporting Fairness and Originality in NIH Research Applications*: https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
- UCSF OSR guidance on NOT-OD-25-132 (example of PI certification): https://osr.ucsf.edu/news/not-od-25-132-ai-and-submission-limits-guidance-for-nih-applications
- NIH Simplified Peer Review Framework: https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
- Yale Mock Study Section, *Evaluating Applications Under NIH's Simplified Review Framework*: https://mockstudy.yale.edu/wp-content/uploads/2025/03/scoring_simplified_review_r_proposals.pdf
- NIH, Write Your Application (order of precedence for instructions): https://www.grants.nih.gov/grants-process/write-application
- NIH RePORTER Matchmaker: https://reporter.nih.gov/matchmaker
- Claude Science overview: https://www.anthropic.com/news/claude-science-ai-workbench
- ChatGPT Work and Codex overview: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex

# Grant Project Template v2.0 — An NIH-Compliant, AI-Assisted Grant Writing Workflow

> **Core principle: the PI thinks and writes; AI retrieves, computes, critiques, and verifies.**
>
> Compared with v1.0, this version (1) replaces "AI drafts, PI edits" with "PI drafts, AI reviews" to comply with NIH NOT-OD-25-132; (2) rebuilds the reviewer agent around NIH's current Simplified Review Framework; (3) condenses 12 phases and 8 agents into 7 phases and 7 prompts; and (4) adds the steps most often missed in practice: program officer contact, human mock review, resubmission Introduction, a backward-planned timeline, the annual application limit, and data governance.

---

## 0. What changed from v1.0

| v1.0 | Problem | v2.0 |
|---|---|---|
| The coordinator AI handled "proposal integration/writing"; Agent 4 drafted the Specific Aims and Agent 7 drafted the full Research Strategy | NIH will not consider applications (or sections) substantially developed by AI to be the applicant's original ideas | Three writing zones (§2). The PI writes the Aims and Research Strategy; AI critiques, verifies, and suggests sentence-level edits |
| Reviewer assessed Significance / Innovation / Approach separately | Legacy five-criterion scoring, no longer used for most RPGs due on or after 25 January 2025 | Reviewer uses Factors 1 / 2 / 3 (§7, Prompt G); non-NIH sponsors use their own published criteria |
| The same conversation or same vendor's model both drafted and reviewed | Correlated blind spots; the review is not independent | Reviewer runs on a different vendor's model than the Phase 3 critique, plus a mandatory human mock review |
| Work passed back and forth among several platforms | No single source of truth; version drift | Canonical files defined (§3); AI may only read them or write to `05_Review/` |
| Four overlapping literature tools | Cost and hand-off overhead | One search tool + PubMed + Zotero (§4) |
| No PO contact, human review, resubmission handling, timeline, application cap, or data governance | These are where real applications fail | All built into phases and gates (§5) |
| 12 phases, 8 agents, ~90 folders | High maintenance cost | 7 phases, 7 prompts, compact tree (§3) |

Kept from v1.0: NOFO-first compliance matrix, evidence matrix, aim-dependency test, separating observation from interpretation, traceable numbers, decision log, Codex hand-off format, final STOP-SUBMISSION list.

---

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

## 3. Single source of truth and folder structure

### 3.1 Canonical files

| Content | Canonical location | Who may edit |
|---|---|---|
| Application text (Aims, Research Strategy, etc.) | Every version in `04_Application/drafts/` (flat), named `Document-Name_vXX.YY-YYMMDD_status` (rules in `04_Application/drafts/README.md`); major versions copied to the section folders | PI (or PI-authorized co-authors) only |
| Current project state | `00_Admin/PROJECT_STATE.md` | PI; AI may propose changes |
| Decisions | `00_Admin/DECISION_LOG.md` | PI |
| Literature | The project's Zotero collection (`02_Evidence/references.bib` is an export) | PI |
| Claim → evidence map | `02_Evidence/CLAIMS_REGISTER.md` | AI fills; PI marks each row verified |
| Figure → data → code map | `03_Preliminary_Data/FIGURE_REGISTER.md` | AI/Codex fills; PI verifies |

**Hard rule:** AI tools only read canonical files. All AI output goes to `05_Review/AI_Review/` or is returned as suggestions; it **never overwrites** canonical files. Each hand-off passes only the §8 handoff file and the files it lists, never an entire chat history.

### 3.2 Folder tree

```text
Grant_Project/
├── 00_Admin/
│   ├── PROJECT_BRIEF.md
│   ├── PROJECT_STATE.md
│   ├── DECISION_LOG.md
│   ├── OPEN_QUESTIONS.md
│   ├── TIMELINE.md               # planned backward from the deadline
│   ├── AI_USE_LOG.md             # one row per AI-assisted task
│   ├── DATA_CLASSIFICATION.md    # which data may go to which tools
│   ├── APPLICATION_COUNT.md      # NIH six-per-year check
│   └── SUBMISSION_CHECKLIST.md
├── 01_Funding/
│   ├── NOFO_and_Instructions/    # official documents (archived PDFs)
│   ├── COMPLIANCE_MATRIX.md
│   ├── LANDSCAPE.md              # RePORTER / Matchmaker summary
│   └── PO_CONTACT.md
├── 02_Evidence/
│   ├── EVIDENCE_MATRIX.md
│   ├── CLAIMS_REGISTER.md
│   └── references.bib            # Zotero export; do not hand-edit
├── 03_Preliminary_Data/
│   ├── FIGURE_REGISTER.md
│   ├── figures/
│   ├── source_data/
│   └── ANALYSIS_REPO.md          # pointer to the analysis repo (no raw data here)
├── 04_Application/               # 🔴 RED zone — the PI's writing workspace
│   ├── README.md                 # writing workflow
│   ├── notes/                    # concept page, outlines, cut paragraphs
│   ├── drafts/                   # every version of every document, flat, never overwritten
│   │   ├── README.md             # version naming rules and status codes
│   │   └── VERSION_LOG.md
│   ├── Specific_Aims/            # section folders: copies of major versions only
│   ├── Research_Strategy/
│   ├── Summary_Narrative/
│   ├── Introduction_Resubmission/  # generated only for resubmissions
│   └── Other_Attachments/
├── 05_Review/
│   ├── AI_Review/
│   ├── Human_Review/
│   └── REVIEWER_RISK_REGISTER.md
├── 06_Submission/
│   ├── FINAL_COMPLIANCE.md
│   └── Submitted/
├── 99_Archive/
└── .ai/
    ├── MASTER_INSTRUCTIONS.md
    ├── prompts/  (A–G)
    ├── handoffs/GRANT_HANDOFF.md
    └── workflow/GRANT_WORKFLOW.md
```

Large raw data (.h5ad, .rds, FASTQ, BAM, .hic) stay out of the grant repository; record their location and commit in `ANALYSIS_REPO.md`.

---

## 4. Tool roles (vendor-neutral)

| Role | Default | Alternative | Notes |
|---|---|---|---|
| Coordinator assistant (reads rules, builds matrices, critiques, audits) | **Choose one**: a Claude Project or a ChatGPT Project/Work workspace | — | Do not run two coordinators; you will end up with two "truths" |
| Data analysis and figures | Claude Science (exploratory analysis on local/HPC/Slurm) | Codex / Claude Code (maintaining existing code repositories) | If a mature pipeline exists, modify it in place |
| Literature search and verification | PubMed + one evidence tool (e.g., Consensus) + Zotero | Deep Research (one-off broad scans only) | Zotero entries are the final citation authority |
| Funding landscape | [NIH RePORTER Matchmaker](https://reporter.nih.gov/matchmaker) | RePORTER advanced search | The PI runs it; AI only summarizes the exports |
| Reviewer simulation | A **different vendor's** model than the Phase 3 critique, in a fresh conversation | — | Runs alongside, never instead of, human mock review |
| Compliance | Coordinator assistant + manual PI check | Institutional sponsored-programs review | Official documents govern |

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

## 6. Coordinator master instructions (paste into Project instructions)

```text
# GRANT PROJECT MASTER INSTRUCTIONS (v2.0)

You support the PI in developing a grant application. You do NOT write the
application. The PI writes; you retrieve, verify, analyze, critique, and audit.

## Writing zones (NIH NOT-OD-25-132)
RED (PI-authored only): Specific Aims; Significance/Innovation arguments;
Approach rationale, design, expected outcomes, interpretation, pitfalls and
alternatives; Project Summary; Project Narrative; Resubmission Introduction;
emails to program officers.
- For RED content you may: ask clarifying questions, list required elements
  from the official instructions, critique PI-written text, check claims
  against evidence, and give sentence-level edit SUGGESTIONS in a table
  (original | suggestion | reason). You must not draft or rewrite paragraphs,
  add new scientific arguments, or add new experiments.
- If asked to draft RED content, decline briefly and offer an outline of
  required elements plus questions for the PI instead.
YELLOW (limited assistance): figure legends from FIGURE_REGISTER; factual
budget-justification items; facilities lists from supplied institutional
material; reference formatting. Use only facts present in the supplied files.
GREEN: compliance matrices, landscape summaries, literature retrieval and
citation verification, evidence matrices, data analysis, stress tests,
consistency audits, reviewer simulation, formatting checks.

## Sources of truth
- Requirements: current sponsor notices > specific NOFO/RFA > sponsor
  application instructions > institutional instructions. Never rely on memory
  when an official document is supplied. Quote the source for every rule.
- Science: 02_Evidence/CLAIMS_REGISTER.md, EVIDENCE_MATRIX.md, Zotero keys.
- Data: 03_Preliminary_Data/FIGURE_REGISTER.md.
- State: 00_Admin/PROJECT_STATE.md and DECISION_LOG.md. Never silently
  reverse a recorded decision; flag conflicts instead.

## Never fabricate
Citations, data, statistics, sample sizes, collaborator commitments,
resources, approvals, budget numbers. If information is missing, write
[MISSING: ...] and add it to OPEN_QUESTIONS.

## Label every statement you produce as one of
supplied fact | literature-supported (with citation key) | preliminary
observation (with figure ID) | working hypothesis | proposed experiment |
unresolved assumption.

## Output location
Write outputs as new files for 05_Review/AI_Review/ or as returned text.
Never overwrite files in 04_Application/. Name each output after the draft
version it reviewed, with AI-<prompt letter> as status, e.g.
Specific-Aims_v01.00-YYMMDD_AI-D.md. If the file name of a supplied draft
carries no version, ask the PI which version it is.

## Data handling
Follow 00_Admin/DATA_CLASSIFICATION.md. If a request would involve data in a
restricted class, stop and ask the PI.

## At the end of every task
Return a one-line entry for 00_Admin/AI_USE_LOG.md:
date | tool | task | inputs | output file | what the PI must verify.
```

---

## 7. Seven standard prompts

Run each prompt in a new conversation (except Prompt F line-edit mode), attaching the §8 handoff file first.

### Prompt A — NOFO parsing & compliance (P0 / P7) 🟢

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

### Prompt B — Funding landscape (P1) 🟢

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

### Prompt C — Evidence & citation verification (P2) 🟢

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

### Prompt D — Aims logic & rigor stress test (P3) 🟢

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

### Prompt E — Preliminary data analysis (P4) 🟢

```text
ROLE: Reproducible analysis agent (Claude Science or Codex).

FIRST: read 00_Admin/DATA_CLASSIFICATION.md and ANALYSIS_REPO.md. If an
existing pipeline exists, read it before changing anything; modify and
validate rather than rebuild.

GOAL: [analysis question, e.g., "Does perturbation X shift photoreceptor
precursor state distribution at D120?"]
REQUIRED OUTPUT: [figure/table/statistic]

RULES: preserve raw data; do not silently change upstream preprocessing;
record environment and new dependencies; no significance claims without the
test; no causal language for descriptive results; save source data for every
panel.

RETURN:
1. files changed and commit hash; commands run;
2. analysis decisions and parameters;
3. validation performed (e.g., QC metrics, sensitivity to parameter choices);
4. FIGURE_REGISTER row:
   Figure ID | Panel | Dataset | Analysis | Key quantitative result |
   Statistic/test | n (biological) | Supported conclusion |
   NOT supported (do not claim) | Limitations | Relevant Aim |
   Source-data path | Code path@commit
5. unresolved concerns;
6. AI_USE_LOG entry.
Do not write Preliminary Data prose; the PI writes it from the register.
```

### Prompt F — Consistency audit / line edit (P3 / P5) 🟢

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

### Prompt G — Simplified Review Framework reviewer (P6) 🟢

```text
ROLE: Experienced NIH study-section reviewer using the Simplified Review
Framework. You have never seen this project before. Evaluate only what is
written. Do not rewrite the application.

INPUT: NOFO (confirm which review criteria apply); Specific Aims; Research
Strategy; key figures; biosketch personal statements if supplied.
(For non-NIH sponsors: replace the factors below with the sponsor's published
criteria from the NOFO/RFA.)

EVALUATE:
Factor 1 — Importance of the Research ("Should it be done?"): significance of
the problem and knowledge gap; rigor of prior research the premise rests on;
whether success would advance the field; innovation that changes capability
rather than novelty of technique alone.
Factor 2 — Rigor and Feasibility ("Can it be done well?"): will the approach
produce unbiased, reproducible, robust data; design, controls, biological
variables, statistics; feasibility and handling of challenges. Judge risk in
context of potential impact; do not expect every obstacle to be solved.
Factor 3 — Expertise and Resources: SUFFICIENT or NOT SUFFICIENT; if not,
state the specific gap.

OUTPUT:
1. For Factors 1 and 2: 3–5 strengths and 3–5 weaknesses each, written as a
   reviewer would, each tied to a page/section.
2. Factor 3: sufficiency judgment with reason.
3. Reviewer Risk Register rows:
   ID | Factor | Location | Concern | Severity (FATAL/MAJOR/MODERATE/MINOR) |
   What would resolve it (described)
4. The 5 issues most likely to hurt the overall impact score.
No numeric score, no funding prediction, no generic praise.
End with an AI_USE_LOG entry.
```

---

## 8. Standard handoff file (GRANT_HANDOFF.md)

When starting a new conversation or switching tools, pass only this file and the source files it lists.

```markdown
# GRANT HANDOFF

## Grant
Sponsor: | Mechanism: | Deadline: | Resubmission: yes/no

## Writing-zone reminder
RED sections are PI-authored. Critique and suggest only.

## Current state (copy from PROJECT_STATE.md)
Knowledge gap:
Central hypothesis:
Aims (titles only):

## Decisions already fixed (from DECISION_LOG.md)
- 

## Task for this session
Prompt: A / B / C / D / E / F / G
Question:

## Must NOT change
- 

## Source files attached
- 

## Data class of attached material (from DATA_CLASSIFICATION.md)
```

---

## 9. Register templates

All registers are pre-created in the generated project:

| File | Purpose |
|---|---|
| `00_Admin/AI_USE_LOG.md` | One row per AI-assisted task: tool, prompt, inputs, output, zone, how used, how verified |
| `02_Evidence/CLAIMS_REGISTER.md` | Every factual claim with its Zotero key or Figure ID and PI verification date |
| `03_Preliminary_Data/FIGURE_REGISTER.md` | Figure → dataset → test → n → supported / unsupported conclusions → source data → code@commit |
| `00_Admin/DATA_CLASSIFICATION.md` | Which data class may go to cloud AI, local-compute AI, or no AI |
| `05_Review/REVIEWER_RISK_REGISTER.md` | AI and human critiques by Factor, severity, decision, resolution |

---

## 10. First use

```bash
# 1. Generate a grant project from the grant/ subdirectory of the template repo
cookiecutter gh:quzp/cookiecutter-bio-project --directory grant
#    answer prompts: project_name, sponsor, mechanism, deadline, is_resubmission ...

cd <your_project_slug>
# 2. Add official documents
cp ~/Downloads/NOFO.pdf 01_Funding/NOFO_and_Instructions/
# 3. Fill 00_Admin/PROJECT_BRIEF.md, APPLICATION_COUNT.md, DATA_CLASSIFICATION.md
# 4. Paste .ai/MASTER_INSTRUCTIONS.md into your chosen coordinator's Project instructions
# 5. New conversation: attach GRANT_HANDOFF.md + NOFO + instructions; paste .ai/prompts/A_compliance.md
# 6. Save the result as 01_Funding/COMPLIANCE_MATRIX.md and add a row to AI_USE_LOG.md
git add -A && git commit -m "P0: compliance matrix v1"
```

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

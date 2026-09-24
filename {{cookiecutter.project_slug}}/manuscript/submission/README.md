# manuscript/submission/

One directory per submission, named `NN_Journal-Name_YYMMDD/` (sequence number, journal,
six-digit submission date), capturing the complete state of that attempt.

Everything you write for a submission — cover letter, response to reviewers — is drafted
in `../drafts/` like the manuscript. This folder receives **copies** of the major versions
and the submitted files, plus the documents the journal sends back (named by content and
date only):

```
submission/
├── 01_Nat-Commun_260601/
│   ├── Manuscript_v03.00-260601_submitted.pdf
│   ├── Cover-Letter_v01.00-260531_final.docx
│   ├── Cover-Letter_v01.00-260601_submitted.docx
│   ├── Suggested-Reviewers_v01.00-260601_submitted.md
│   └── Decision-Letter_260720.pdf                        <- received from the journal
└── 02_eLife_260915/
    ├── Manuscript_v04.00-260915_submitted.pdf
    ├── Reviews_261120.pdf                                <- received from the journal
    ├── Response-to-Reviewers_v01.00-261210_int.docx      <- copied from drafts/ (sent to co-authors)
    ├── Response-to-Reviewers_v02.00-261216_final.docx
    ├── Response-to-Reviewers_v02.00-261218_submitted.docx
    └── Manuscript_v05.00-261218_submitted.pdf            <- revised manuscript
```

Store the **exact version submitted** on the day it is submitted; `drafts/` keeps moving
afterwards. Six months later, during revision, you will need to know precisely what the
reviewers saw. The version number in each file name tells you which file in `drafts/` it
came from.

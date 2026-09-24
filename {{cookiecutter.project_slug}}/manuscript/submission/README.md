# manuscript/submission/

One directory per submission, named `NN_Journal-Name_YYMMDD/` (sequence number, journal,
six-digit submission date), capturing the complete state of that attempt. Files follow
the naming rules in `../README.md`:

```
submission/
├── 01_Nat-Commun_260601/
│   ├── Manuscript_v03.00-260601_submitted.pdf
│   ├── Cover-Letter_v01.00-260601_submitted.docx
│   ├── Suggested-Reviewers_v01.00-260601_submitted.md
│   └── Decision-Letter_260720.pdf                   <- received documents: name and date only
└── 02_eLife_260915/
    ├── Manuscript_v04.00-260915_submitted.pdf
    ├── Reviews_261120.pdf
    ├── Response-to-Reviewers_v00.03-261205_wip.docx  <- rebuttal drafts are versioned here
    ├── Response-to-Reviewers_v01.00-261210_int.docx
    ├── Response-to-Reviewers_v02.00-261218_submitted.docx
    └── Manuscript_v05.00-261218_submitted.pdf        <- revised manuscript, drafted in draft/
```

Store the **exact version submitted** on the day it is submitted; the text in `draft/`
keeps moving afterwards. Six months later, during revision, you will need to know
precisely what the reviewers saw. The version number in the submitted file name tells you
which draft in `draft/` it came from.

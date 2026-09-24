# DATA CLASSIFICATION

Decide BEFORE any analysis which data may go to which tool. Confirm IRB/IT requirements for restricted classes.
Note: even when compute runs locally, content placed in prompts and model outputs is processed by the model provider.

| Class | Examples in this project | Cloud AI chat | Local-compute AI (lab / HPC) | Approved by / date |
|---|---|---|---|---|
| Public | Published data, GEO/SRA, literature | Yes | Yes | |
| Unpublished lab data | | [decide] | [decide] | |
| IRB-restricted / identifiable | | No | [ask IRB/IT] | |
| Confidential third-party | Reviewer materials, others' unpublished manuscripts | No | No | |

Rule: never paste patient identifiers into any AI tool.

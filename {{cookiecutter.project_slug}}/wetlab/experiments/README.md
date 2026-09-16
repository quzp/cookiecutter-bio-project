# experiments/

一次具体实验的完整记录。每个实验建一个目录：

```
experiments/
├── 20260301_organoid_d30_qc/
│   ├── record.md              <- 照 TEMPLATE_experiment.md 填
│   ├── plate_layout.tsv       <- 板图、加样表等小表格
│   └── notes/                 <- 临时观察、拍照说明（图像本身放 data/raw/）
└── 20260315_crispri_transduction/
```

命名规则：`YYYYMMDD_简短英文描述`，日期用实验**开始**那天。

约定：

- **记录当天写。** 事后补记的内容注明"补记于 YYYY-MM-DD"。
- **记录不改历史。** 发现之前写错了，在文末追加勘误，不要就地改写。
- **与数据挂钩。** 记录里写清产生了哪些样本，样本 ID 要和 `metadata/samples.tsv`
  里的 `sample_id` 完全一致；产生的原始文件写明在 `data/raw/` 下的路径。
- **失败的实验也要留。** 在标题里标 `[FAILED]`，写清失败原因，这比成功记录更值钱。

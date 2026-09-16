# metadata/

**这是整个项目最关键的一个目录。** 它是湿实验与干实验之间唯一的接头：
没有它，半年后没人能确定某个 fastq 对应的是哪一管细胞。

## samples.tsv 字段定义

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `sample_id` | ✅ | 项目内全局唯一，一经写入**永不修改**。建议 `S001` 递增 |
| `experiment_id` | ✅ | 对应 `wetlab/experiments/` 下的目录名 |
| `condition` | ✅ | 实验分组，用于下游建模的设计矩阵 |
| `replicate` | ✅ | 生物学重复编号（技术重复另开 `tech_rep` 列） |
| `cell_line` | | 细胞系名称，与 `wetlab/inventory/cell_lines.tsv` 一致 |
| `timepoint` | | 采样时间点，例如 `d30` |
| `collection_date` | ✅ | ISO 8601，采样当天 |
| `assay` | ✅ | `RNA-seq` / `scRNA-seq` / `ATAC` / `qPCR` / `imaging` / `flow` |
| `library_id` | | 建库/测序时的文库编号，测序公司返回的名字 |
| `raw_path` | | 相对于项目根目录的路径，例如 `data/raw/rnaseq/S001_R1.fastq.gz` |
| `batch` | | 建库批次或测序 run，用于建模时的批次效应校正 |
| `qc_status` | | `pass` / `fail` / `pending`；`fail` 的样本保留行，不删 |
| `notes` | | 任何异常情况 |

## 约定

1. **样本一产生就登记，不要等到测序回来。** 提取 RNA 那天就写上，`library_id`
   和 `raw_path` 后补。
2. **`sample_id` 永不复用、永不修改。** 写错了就新开一行并把旧行 `qc_status`
   标为 `fail`，在 `notes` 说明。
3. **不要删行。** 失败、丢弃的样本保留记录，这是"为什么最终只有 n=5"的唯一证据。
4. **分组信息以本表为准。** 分析脚本从这里读设计矩阵，不要在脚本里硬编码分组。
5. 用制表符分隔，不要用 Excel 直接保存（会改日期格式、加 BOM）。要用 Excel
   编辑就另存为 UTF-8 的 tab 分隔文本。

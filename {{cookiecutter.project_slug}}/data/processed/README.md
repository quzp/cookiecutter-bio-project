# data/processed/

可以直接喂给统计分析的最终数据集，例如：

- 过滤、归一化后的表达矩阵
- 注释好的 `SummarizedExperiment` / `AnnData` 对象
- 合并了 `metadata/samples.tsv` 分组信息的分析用表

约定：

- 文件名带日期或版本，例如 `counts_filtered_20260401.rds`，便于追溯手稿里的图用的是哪版。
- 每个文件对应一个生成脚本，脚本路径写在同名的 `.md` 说明里或文件头注释中。

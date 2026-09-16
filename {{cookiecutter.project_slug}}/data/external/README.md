# data/external/

来自第三方的数据：公共数据库下载、合作者提供的数据集、参考基因组与注释。

**每个数据集必须附一个 `SOURCE.md`**，写明：

- 来源 URL 或数据库编号（GEO accession、ArrayExpress、ENA、Ensembl release 号）
- 下载日期与下载所用的命令
- 版本号（基因组版本如 `GRCh38.p14`、注释版本如 `GENCODE v45`）
- 许可证与引用要求

参考基因组和注释文件通常体积很大且多个项目共用，建议不要复制进本目录，
而是放在实验室共享位置并在 `config/config.yml` 里配置路径。

# src/

分析代码。按"数据处理 → 统计分析 → 出图"的顺序分层，方便追溯每张图的来源。

| 子目录 | 职责 |
| --- | --- |
| `data/` | 读取 `data/raw` 与 `data/external`，清洗、QC、格式转换，产出到 `interim`/`processed` |
| `analysis/` | 统计建模、差异表达、富集分析，产出到 `results/tables` |
| `visualization/` | 读取 `processed`/`results/tables`，出图到 `results/figures` |
| `utils/` | 跨脚本复用的函数、路径解析、配置读取 |

约定：

- 文件名带序号表示执行顺序：`01_qc.R`、`02_normalize.R`、`10_deseq2.R`。
- **不写绝对路径。** R 用 `here::here("data", "raw", ...)`，Python 用 `utils` 里的
  `project_root()`，这样脚本从任何工作目录调用都能跑。
- **不硬编码分组。** 从 `metadata/samples.tsv` 读设计矩阵。
- 参数（阈值、基因组版本、颜色）写进 `config/config.yml`，不要散落在脚本里。
- 脚本末尾输出 `sessionInfo()` / 环境信息到日志，便于日后复现。

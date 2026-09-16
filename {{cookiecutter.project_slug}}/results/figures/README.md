# results/figures/

由 `src/visualization/` 下的脚本直接输出的图。特点：

- **可重跑**：换个参数重新执行脚本就能全部重画，因此不进 git。
- **未排版**：单张图，不做拼版、不加字母标号。
- **给自己看**：用于自查、组会讨论。

进入手稿的图，经人工拼版/标注后另存到 `manuscript/figures/`，那里的文件才进 git。

建议文件名带生成脚本编号：`10_deseq2_volcano.pdf` 对应 `src/analysis/10_deseq2.R`。
矢量格式（pdf/svg）优先，位图至少 300 dpi。

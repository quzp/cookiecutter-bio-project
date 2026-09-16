# manuscript/figures/

进入手稿的**成品图**：由 `results/figures/` 里的单图经人工拼版、加字母标号、
统一字号和配色后得到。这些文件**进 git**，因为它们包含了无法脚本化的人工排版工作。

约定：

- 每个 figure 一个目录或一个文件：`figure1.ai` / `figure1.pdf` / `figure1.png`。
- 保留可编辑的源文件（`.ai` / `.svg` / `.pptx`），不要只留导出的位图。
- 同目录放 `figure_legends.md` 存图注，正文引用时直接复制，避免图注与图脱节。
- 体积较大的 `.tif` / `.ai` 考虑用 Git LFS，配置见根目录 `.gitattributes`。

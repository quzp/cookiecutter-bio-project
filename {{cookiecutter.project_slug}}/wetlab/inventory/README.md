# inventory/

物料清单。用 `.tsv` 存放（纯文本、git diff 友好、R/Python 都能直接读）。

建议的文件：

```
plasmids.tsv       质粒：编号、骨架、插入片段、抗性、来源、冻存位置
primers.tsv        引物：编号、序列、Tm、用途、订购日期
guides.tsv         gRNA：编号、靶基因、原间隔序列、所在文库/载体
antibodies.tsv     抗体：靶点、厂家、货号、批号、稀释比、验证情况
cell_lines.tsv     细胞系：名称、来源、代次、支原体检测日期、冻存位置
```

约定：

- 编号一经分配不重复使用，即使物料已用尽也保留该行，加 `status` 列标 `depleted`。
- 序列列统一大写、5'→3'、不含空格。
- 冻存位置精确到盒和格，例如 `-80_A3 / box12 / C4`。

# data/raw/

仪器原始输出。**只读，永不就地修改。**

任何改名、清洗、过滤、格式转换都写成 `src/data/` 下的脚本，输出到 `data/interim/`。
如果你发现自己想直接编辑这里的文件，说明缺了一个脚本。

建议按检测类型分层：

```
raw/
├── rnaseq/
├── scrnaseq/
├── imaging/
├── flow/
└── qpcr/
```

拿到数据后立刻做两件事：

1. **设为只读**：`chmod -R a-w data/raw/<新数据目录>`
2. **记校验和**：`find data/raw -type f -exec sha256sum {} + > data/raw/CHECKSUMS.sha256`
   （日后可用 `sha256sum -c` 验证文件未被改动或损坏）

每个新数据目录里放一个 `SOURCE.md`，写明：来源（测序公司/仪器）、接收日期、
对应的 `experiment_id`、对应的 `sample_id` 列表。

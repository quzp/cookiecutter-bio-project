# data/

机器产出的数据。**默认全部不进 git**（见根目录 `.gitignore`，只有各级 README 被保留）。

数据流向是单向的，越往下越接近可分析状态：

```
raw/ ──┐
       ├──► interim/ ──► processed/ ──► src/analysis/
external/ ─┘
```

| 子目录 | 可写？ | 说明 |
| --- | --- | --- |
| `raw/` | ❌ 只读 | 仪器原始输出。建议 `chmod -R a-w data/raw` |
| `external/` | ❌ 只读 | 公共数据库下载、他人提供的数据 |
| `interim/` | ✅ | 脚本产生的中间结果，可以随时删掉重跑 |
| `processed/` | ✅ | 可直接喂给统计分析的最终数据集 |

**备份**：这些文件不在 git 里，需要独立的备份策略。把备份位置写进根目录 README。

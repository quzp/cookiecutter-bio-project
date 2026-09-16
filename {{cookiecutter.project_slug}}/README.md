# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

| | |
| --- | --- |
| 负责人 | {{ cookiecutter.author_name }}{% if cookiecutter.institution %}，{{ cookiecutter.institution }}{% endif %} |
| 创建日期 | __DATE__ |
| 分析语言 | {{ cookiecutter.primary_language }} |
| 状态 | 进行中 |

## 快速开始

```bash
pixi install          # 按 pixi.toml 解析并锁定环境
pixi run check        # 确认解释器与核心包可用
pixi shell            # 进入环境交互式工作
```

## 目录结构

```
.
├── wetlab/         湿实验记录（人写，纯文本，全部进 git）
│   ├── protocols/      SOP，一个方法一个 .md
│   ├── experiments/    按 YYYYMMDD_简称/ 建子目录
│   └── inventory/      质粒、引物、抗体、细胞系、gRNA 清单
├── metadata/       样本表：连接湿实验与测序数据的唯一接头
├── data/           机器产出的数据（默认不进 git）
│   ├── raw/            仪器原始输出，只读不改
│   ├── external/       公共数据库下载
│   ├── interim/        中间结果
│   └── processed/      可直接分析的最终数据集
├── src/            分析代码
│   ├── data/           预处理、QC、格式转换
│   ├── analysis/       统计建模、差异表达、富集
│   ├── visualization/  出图脚本
│   └── utils/          通用函数、路径与配置读取
├── notebooks/      探索性分析，命名带序号
├── results/        脚本产物
│   ├── figures/        可随时重跑的图，不进 git
│   └── tables/         统计输出表
├── manuscript/     手稿
│   ├── main/           正文
│   ├── figures/        人工拼版后的成品图，进 git
│   ├── supplement/     补充材料
│   └── submission/     各期刊投稿版本与审稿回复
├── docs/           文献笔记、组会记录、方法学参考
└── config/         分析参数与样本分组配置
```

每个目录下都有 `README.md` 说明具体用法。

## 工作约定

1. **`data/raw/` 只读。** 任何清洗、改名、过滤都写成 `src/data/` 下的脚本，
   输出到 `data/interim/` 或 `data/processed/`。原始文件本身永不就地修改。
2. **每个湿实验开一个目录。** `wetlab/experiments/YYYYMMDD_简称/`，
   照着 `wetlab/experiments/TEMPLATE_experiment.md` 填。
3. **产生样本就登记。** 新细胞、新文库、新测序批次，当天写进 `metadata/samples.tsv`，
   `sample_id` 一经写入不得更改。
4. **`results/figures/` 里的图必须由 `src/` 的脚本生成。** 手动 PS/AI 拼版后的成品
   放 `manuscript/figures/`，两者不混。
5. **`CHANGELOG.md` 记节点。** 新数据批次、分析方法变更、投稿与返修，各一行。
6. **大文件不进 git。** 见 `.gitignore`；确需版本化的中等文件用 Git LFS
   （`.gitattributes` 里有注释掉的配置）。

## 数据备份

`data/` 不在 git 里，备份责任在你自己。建议：

- `data/raw/` 在数据产生当天同步到实验室服务器 / 对象存储，并设为只读。
- 记录备份位置到本节，例如：`原始数据镜像：<路径或链接>`

# cookiecutter-bio-project

一个轻量的生物学研究项目脚手架：一条命令生成**湿实验 + 干实验**双轨的目录结构，
每个目录自带说明文件，不含任何多余的构建系统。

设计理念沿袭 [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)
和 [cookiecutter-reproducible-science](https://github.com/mkrapp/cookiecutter-reproducible-science)，
但做了三点针对性改造：

1. **湿实验与干实验在同一个仓库里**，`wetlab/` 存人写的记录（方案、实验、库存），
   `data/` 存机器产出的数据，不出现两个"原始数据"位置。
2. **`metadata/samples.tsv` 是两端的唯一接头**，强制登记"这管细胞对应哪个 fastq"。
3. **环境用 [pixi](https://pixi.sh)**，`pixi.lock` 跨平台锁定 R / Bioconductor / Python 依赖，
   比 `environment.yml` 更可复现，也不需要先装 conda。

## 使用

```bash
# 安装 cookiecutter（推荐用 uv 或 pipx，避免污染系统 Python）
uv tool install cookiecutter        # 或：pipx install cookiecutter

# 从 GitHub 直接生成
cookiecutter gh:YOUR_GITHUB_USERNAME/cookiecutter-bio-project

# 或从本地目录生成
cookiecutter path/to/cookiecutter-bio-project
```

交互式填写以下字段：

| 字段 | 说明 |
| --- | --- |
| `project_name` | 项目全名，例如 `Retinal Organoid EZH2 Screen` |
| `project_slug` | 目录名，默认由项目名自动转换 |
| `project_short_description` | 一句话描述，会写进 README 和 CITATION.cff |
| `author_name` / `author_email` / `orcid` / `institution` | 作者信息 |
| `github_username` | 用于生成远程仓库地址提示 |
| `primary_language` | `R` / `Python` / `R + Python`，决定 `pixi.toml` 的依赖 |
| `use_quarto` | 是否在 `notebooks/` 放 Quarto 模板并加入 pixi 依赖 |
| `open_source_license` | `MIT` / `BSD-3-Clause` / `CC-BY-4.0` / `None` |
| `init_git_repo` | 是否自动 `git init` 并创建首次 commit |

## 生成的目录结构

```
your_project/
├── README.md                 <- 项目概览、目录说明、工作约定
├── CHANGELOG.md              <- 数据批次、方法变更、投稿版本的时间线
├── AUTHORS.md
├── CITATION.cff              <- 机器可读的引用信息（GitHub / Zenodo 识别）
├── LICENSE
├── pixi.toml                 <- 计算环境定义
├── .gitignore                <- 默认忽略大数据与生成图表
├── .gitattributes            <- 行尾规范 + Git LFS 备选配置
│
├── wetlab/                   <- 湿实验：人写的纯文本记录，全部纳入 git
│   ├── protocols/            <- SOP，一个方法一个 .md（含模板）
│   ├── experiments/          <- 按 YYYYMMDD_简称/ 建子目录（含模板）
│   └── inventory/            <- 质粒、引物、抗体、细胞系、gRNA 清单
│
├── metadata/                 <- 湿/干两端的接头
│   └── samples.tsv           <- 样本ID ↔ 实验编号 ↔ 文库ID ↔ 分组
│
├── data/                     <- 机器产出的数据，默认不进 git
│   ├── raw/                  <- 仪器原始输出，只读不改
│   ├── external/             <- 公共数据库下载（GEO、Ensembl 等）
│   ├── interim/              <- 中间结果（bam、count matrix）
│   └── processed/            <- 可直接分析的最终数据集
│
├── src/                      <- 分析代码
│   ├── data/                 <- 预处理、QC、格式转换
│   ├── analysis/             <- 统计建模、差异表达、富集
│   ├── visualization/        <- 出图脚本
│   └── utils/                <- 通用函数、路径与配置读取
│
├── notebooks/                <- 探索性分析，命名带序号
├── results/
│   ├── figures/              <- 脚本产物，可随时重跑，不进 git
│   └── tables/               <- 统计输出表
│
├── manuscript/
│   ├── main/                 <- 正文
│   ├── figures/              <- 人工拼版后的成品图，进 git
│   ├── supplement/           <- 补充材料
│   └── submission/           <- 各期刊投稿版本、cover letter、审稿回复
│
├── docs/                     <- 文献笔记、组会记录、方法学参考
└── config/                   <- 分析参数与样本分组配置
```

## 自己修改模板

- 增删目录：直接改 `{{cookiecutter.project_slug}}/` 下的结构，每个目录至少保留一个文件
  （空目录不会被 git 追踪，也就不会出现在生成结果里）。
- 增加提问：在 `cookiecutter.json` 加字段，用 `{{ cookiecutter.字段名 }}` 在任意文件内容或文件名中引用。
- 生成后的自动处理写在 `hooks/post_gen_project.py`（选许可证、填年份、初始化 git）。
- 输入校验写在 `hooks/pre_gen_project.py`。

## License

模板本身以 MIT 协议发布，生成的项目使用你选择的协议。

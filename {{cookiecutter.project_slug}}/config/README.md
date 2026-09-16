# config/

分析参数与路径配置。目的是让所有阈值、版本号、路径集中在一处，
脚本里不出现魔法数字——改参数只改这里，也方便在方法学部分如实描述。

`config.yml` 由 `src/utils/paths.R` 的 `load_config()` 或
`src/utils/paths.py` 的 `load_config()` 读取。

如果某个参数在不同分析里取值不同，不要在脚本里覆盖，而是在 `config.yml`
里为该分析单独开一节。

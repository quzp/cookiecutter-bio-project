# 路径与配置读取工具
#
# 用法：
#   source(here::here("src", "utils", "paths.R"))
#   cfg <- load_config()
#   samples <- load_samples()

suppressPackageStartupMessages({
  library(here)
})

#' 读取 config/config.yml
load_config <- function(path = here::here("config", "config.yml")) {
  if (!requireNamespace("yaml", quietly = TRUE)) {
    stop("需要 yaml 包：pixi add r-yaml")
  }
  yaml::read_yaml(path)
}

#' 读取样本表，返回 data.frame
load_samples <- function(path = here::here("metadata", "samples.tsv")) {
  df <- read.delim(path, sep = "\t", stringsAsFactors = FALSE, na.strings = c("", "NA"))
  if (anyDuplicated(df$sample_id) > 0) {
    stop("metadata/samples.tsv 中存在重复的 sample_id")
  }
  df
}

#' 便捷路径构造
path_raw       <- function(...) here::here("data", "raw", ...)
path_interim   <- function(...) here::here("data", "interim", ...)
path_processed <- function(...) here::here("data", "processed", ...)
path_figures   <- function(...) here::here("results", "figures", ...)
path_tables    <- function(...) here::here("results", "tables", ...)

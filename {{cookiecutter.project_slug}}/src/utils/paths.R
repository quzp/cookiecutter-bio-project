# Path and configuration helpers.
#
# Usage:
#   source(here::here("src", "utils", "paths.R"))
#   cfg     <- load_config()
#   samples <- load_samples()

suppressPackageStartupMessages({
  library(here)
})

#' Read management/config/config.yml
load_config <- function(path = here::here("management", "config", "config.yml")) {
  if (!requireNamespace("yaml", quietly = TRUE)) {
    stop("The yaml package is required: pixi add r-yaml")
  }
  yaml::read_yaml(path)
}

#' Read the sample sheet as a data.frame
load_samples <- function(path = here::here("data", "metadata", "samples.tsv")) {
  df <- read.delim(path, sep = "\t", stringsAsFactors = FALSE, na.strings = c("", "NA"))
  if (anyDuplicated(df$sample_id) > 0) {
    stop("Duplicate sample_id values in data/metadata/samples.tsv")
  }
  df
}

# Convenience path builders
path_raw       <- function(...) here::here("data", "raw", ...)
path_external  <- function(...) here::here("data", "external", ...)
path_interim   <- function(...) here::here("data", "interim", ...)
path_processed <- function(...) here::here("data", "processed", ...)
path_figures   <- function(...) here::here("results", "figures", ...)
path_tables    <- function(...) here::here("results", "tables", ...)

"""路径与配置读取工具。

用法：
    from src.utils.paths import load_config, load_samples, path_raw
"""
from pathlib import Path

import pandas as pd


def project_root() -> Path:
    """向上查找包含 pixi.toml 的目录作为项目根。"""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "pixi.toml").exists():
            return parent
    raise RuntimeError("未找到项目根目录（缺少 pixi.toml）")


ROOT = project_root()


def load_config(path: Path | None = None) -> dict:
    import yaml

    path = path or ROOT / "config" / "config.yml"
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_samples(path: Path | None = None) -> pd.DataFrame:
    path = path or ROOT / "metadata" / "samples.tsv"
    df = pd.read_csv(path, sep="\t", dtype=str)
    if df["sample_id"].duplicated().any():
        raise ValueError("metadata/samples.tsv 中存在重复的 sample_id")
    return df


def path_raw(*parts: str) -> Path:
    return ROOT.joinpath("data", "raw", *parts)


def path_interim(*parts: str) -> Path:
    return ROOT.joinpath("data", "interim", *parts)


def path_processed(*parts: str) -> Path:
    return ROOT.joinpath("data", "processed", *parts)


def path_figures(*parts: str) -> Path:
    return ROOT.joinpath("results", "figures", *parts)


def path_tables(*parts: str) -> Path:
    return ROOT.joinpath("results", "tables", *parts)

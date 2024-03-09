from pathlib import Path

import pandas as pd


def is_dir(path: str) -> bool:
    return Path(path).is_dir()


def load_df(path: str | Path) -> pd.DataFrame:
    if isinstance(path, Path):
        path = str(path)
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".pkl"):
        df = pd.read_pickle(path)
    elif path.endswith(".parquet"):
        df = pd.read_parquet(path)
    else:
        raise ValueError(f"Invalid file type, only csv and pkl supported, got {path}")
    return df


def load_processed_data(filename: str) -> pd.DataFrame:
    filepath = Path(project_root()).joinpath("data", "prepared", filename)
    return load_df(filepath)


def project_root() -> str:
    return str(Path(__file__).parent.parent.resolve())

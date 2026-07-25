from pathlib import Path
import json

import pandas as pd


class FileManager:
    """Utility class for common file operations."""

    @staticmethod
    def read_csv(path: Path) -> pd.DataFrame:
        """Read a CSV file."""
        return pd.read_csv(path)

    @staticmethod
    def write_csv(df: pd.DataFrame, path: Path) -> None:
        """Write a DataFrame to a CSV file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)

    @staticmethod
    def read_json(path: Path):
        """Read a JSON file."""
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_json(data, path: Path) -> None:
        """Write data to a JSON file."""
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def exists(path: Path) -> bool:
        """Check whether a file exists."""
        return path.exists()

    import pandas as pd

    @staticmethod
    def write_parquet(df: pd.DataFrame, file_path) -> None:
        """
        Write a DataFrame to a Parquet file.
        """
        file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(file_path, index=False)


    @staticmethod
    def read_parquet(file_path) -> pd.DataFrame:
        """
        Read a Parquet file into a DataFrame.
        """
        return pd.read_parquet(file_path)
from __future__ import annotations

import pandas as pd

from src.utils.file_manager import FileManager
from src.utils.paths import PathManager


class BronzeLoader:
    """
    Loads datasets from the Bronze layer.
    """

    @staticmethod
    def load_customers() -> pd.DataFrame:
        return FileManager.read_parquet(
            PathManager.BRONZE_DIR / "customers.parquet"
        )

    @staticmethod
    def load_products() -> pd.DataFrame:
        return FileManager.read_parquet(
            PathManager.BRONZE_DIR / "products.parquet"
        )

    @staticmethod
    def load_orders() -> pd.DataFrame:
        return FileManager.read_parquet(
            PathManager.BRONZE_DIR / "orders.parquet"
        )

    @staticmethod
    def load_order_items() -> pd.DataFrame:
        return FileManager.read_parquet(
            PathManager.BRONZE_DIR / "order_items.parquet"
        )
from __future__ import annotations

import pandas as pd

from src.utils.file_manager import FileManager
from src.utils.paths import PathManager


class DataLoader:
    """
    Loads datasets from the Raw layer.
    """

    @staticmethod
    def load_customers() -> pd.DataFrame:
        return FileManager.read_csv(
            PathManager.RAW_DIR / "customers.csv"
        )

    @staticmethod
    def load_products() -> pd.DataFrame:
        return FileManager.read_csv(
            PathManager.RAW_DIR / "products.csv"
        )

    @staticmethod
    def load_orders() -> pd.DataFrame:
        return FileManager.read_csv(
            PathManager.RAW_DIR / "orders.csv"
        )

    @staticmethod
    def load_order_items() -> pd.DataFrame:
        return FileManager.read_csv(
            PathManager.RAW_DIR / "order_items.csv"
        )
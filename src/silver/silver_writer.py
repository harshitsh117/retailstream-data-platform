from __future__ import annotations

from datetime import datetime

import pandas as pd

from src.project_logging.logger import Logger
from src.utils.file_manager import FileManager
from src.utils.paths import PathManager


class SilverWriter:
    """
    Writes transformed datasets to the Silver layer.
    """

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)

    def write(
        self,
        dataframe: pd.DataFrame,
        dataset_name: str,
    ) -> None:
        """
        Write a Silver dataset.
        """

        silver_df = dataframe.copy()

        # Metadata
        silver_df["processed_timestamp"] = datetime.now()
        silver_df["layer"] = "silver"

        output_path = (
            PathManager.SILVER_DIR /
            f"{dataset_name}.parquet"
        )

        FileManager.write_parquet(
            silver_df,
            output_path,
        )

        self.logger.info(
            "Silver dataset '%s' written successfully (%d rows).",
            dataset_name,
            len(silver_df),
        )
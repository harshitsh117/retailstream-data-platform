from __future__ import annotations

from datetime import datetime

import pandas as pd

from src.project_logging.logger import Logger
from src.utils.file_manager import FileManager
from src.utils.paths import PathManager


class BronzeWriter:
    """
    Writes datasets to the Bronze layer.
    """

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)

    def write(
        self,
        dataframe: pd.DataFrame,
        dataset_name: str,
    ) -> None:
        """
        Write a dataset to the Bronze layer.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Dataset to write.

        dataset_name : str
            Name of the dataset.
        """

        bronze_df = dataframe.copy()

        # Metadata
        bronze_df["ingestion_timestamp"] = datetime.now()
        bronze_df["source_system"] = "RetailStream"
        bronze_df["dataset_name"] = dataset_name

        output_path = (
            PathManager.BRONZE_DIR /
            f"{dataset_name}.parquet"
        )

        FileManager.write_parquet(
            bronze_df,
            output_path,
        )

        self.logger.info(
            "Bronze dataset '%s' written successfully (%d rows).",
            dataset_name,
            len(bronze_df),
        )
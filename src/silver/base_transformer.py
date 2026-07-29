from __future__ import annotations

import pandas as pd

from src.project_logging.logger import Logger


class BaseTransformer:
    """
    Base class containing reusable transformation methods.
    """

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)

    def remove_duplicates(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove duplicate records.
        """

        before = len(dataframe)

        dataframe = dataframe.drop_duplicates()

        after = len(dataframe)

        self.logger.info(
            "Removed %d duplicate rows.",
            before - after,
        )

        return dataframe

    def trim_strings(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Trim leading and trailing whitespace
        from all string columns.
        """

        string_columns = dataframe.select_dtypes(
            include="object"
        ).columns

        for column in string_columns:

            dataframe[column] = (
                dataframe[column]
                .astype(str)
                .str.strip()
            )

        self.logger.info(
            "Trimmed whitespace from %d columns.",
            len(string_columns),
        )

        return dataframe

    def convert_datetime(
        self,
        dataframe: pd.DataFrame,
        columns: list[str],
    ) -> pd.DataFrame:
        """
        Convert specified columns to datetime.
        """

        for column in columns:

            dataframe[column] = pd.to_datetime(
                dataframe[column],
                errors="coerce",
            )

        self.logger.info(
            "Converted %d datetime columns.",
            len(columns),
        )

        return dataframe
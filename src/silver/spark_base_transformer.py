from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_timestamp, trim
from pyspark.sql.types import StringType

from src.project_logging.logger import Logger


class SparkBaseTransformer:
    """
    Base class containing reusable Spark transformation methods.
    """

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)

    def remove_duplicates(
        self,
        dataframe: DataFrame,
    ) -> DataFrame:
        """
        Remove duplicate records.
        """

        before = dataframe.count()

        dataframe = dataframe.dropDuplicates()

        after = dataframe.count()

        self.logger.info(
            "Removed %d duplicate rows.",
            before - after,
        )

        return dataframe

    def trim_strings(
        self,
        dataframe: DataFrame,
    ) -> DataFrame:
        """
        Trim leading and trailing whitespace
        from all string columns.
        """

        string_columns = [
            field.name
            for field in dataframe.schema.fields
            if isinstance(field.dataType, StringType)
        ]

        for column in string_columns:

            dataframe = dataframe.withColumn(
                column,
                trim(col(column))
            )

        self.logger.info(
            "Trimmed whitespace from %d columns.",
            len(string_columns),
        )

        return dataframe

    def convert_datetime(
        self,
        dataframe: DataFrame,
        columns: list[str],
    ) -> DataFrame:
        """
        Convert specified columns to timestamp.
        """

        for column in columns:

            dataframe = dataframe.withColumn(
                column,
                to_timestamp(col(column))
            )

        self.logger.info(
            "Converted %d datetime columns.",
            len(columns),
        )

        return dataframe
from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    concat_ws,
    initcap,
    lower,
)
from src.project_logging.logger import Logger
from src.silver.spark_base_transformer import SparkBaseTransformer


class SparkCustomerTransformer(SparkBaseTransformer):
    """
    Transforms customer data from Bronze to Silver using Spark.
    """

    def __init__(self) -> None:
        super().__init__()
        self.logger = Logger.get_logger(__name__)

    def transform(
        self,
        dataframe: DataFrame,
    ) -> DataFrame:

        self.logger.info(
            "Starting Spark Customer Transformation..."
        )

        # ------------------------------------
        # Common Transformations
        # ------------------------------------

        dataframe = self.remove_duplicates(dataframe)

        dataframe = self.trim_strings(dataframe)

        dataframe = self.convert_datetime(
            dataframe,
            ["registration_date"],
        )

        # ------------------------------------
        # Standardize Names
        # ------------------------------------

        dataframe = dataframe.withColumn(
            "first_name",
            initcap(col("first_name")),
        )

        dataframe = dataframe.withColumn(
            "last_name",
            initcap(col("last_name")),
        )

        dataframe = dataframe.withColumn(
            "full_name",
            concat_ws(
                " ",
                col("first_name"),
                col("last_name"),
            ),
        )

        # ------------------------------------
        # Standardize Emails
        # ------------------------------------

        dataframe = dataframe.withColumn(
            "email",
            lower(col("email")),
        )

        # ------------------------------------
        # Validate Email Format
        # ------------------------------------

        dataframe = dataframe.filter(
            col("email").rlike(
                r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
            )
        )

        # ------------------------------------
        # Ensure Unique Customer IDs
        # ------------------------------------

        dataframe = dataframe.dropDuplicates(
            ["customer_id"]
        )

        self.logger.info(
            "Customer Transformation Complete (%d records).",
            dataframe.count(),
        )

        return dataframe
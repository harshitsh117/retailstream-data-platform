from datetime import datetime

from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, lit

from src.project_logging.logger import Logger
from src.utils.paths import PathManager


class SparkBronzeWriter:

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def write(self, dataframe: DataFrame, dataset_name: str):

        bronze_df = (
            dataframe
            .withColumn("ingestion_timestamp", current_timestamp())
            .withColumn("source_system", lit("RetailStream"))
            .withColumn("dataset_name", lit(dataset_name))
        )

        output_path = (
            PathManager.BRONZE_DIR /
            f"{dataset_name}"
        )

        (
            bronze_df.write
            .mode("overwrite")
            .parquet(str(output_path))
        )

        self.logger.info(
            "Bronze dataset '%s' written successfully (%d rows).",
            dataset_name,
            bronze_df.count(),
        )
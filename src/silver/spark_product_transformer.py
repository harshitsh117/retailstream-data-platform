from pyspark.sql import DataFrame

from src.silver.spark_base_transformer import SparkBaseTransformer
from src.project_logging.logger import Logger


class SparkProductTransformer(SparkBaseTransformer):

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def transform(self, df: DataFrame) -> DataFrame:

        self.logger.info("Starting Product Transformation...")

        # Remove duplicate records
        df = self.remove_duplicates(df)

        # Trim whitespace from all string columns
        df = self.trim_strings(df)

        self.logger.info(
            f"Product Transformation Complete ({df.count()} records)."
        )

        return df
from pyspark.sql import DataFrame

from src.project_logging.logger import Logger
from src.silver.spark_base_transformer import SparkBaseTransformer


class SparkOrderItemsTransformer(SparkBaseTransformer):

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def transform(self, df: DataFrame) -> DataFrame:

        self.logger.info("Starting Order Items Transformation...")

        df = self.remove_duplicates(df)

        df = self.trim_strings(df)

        self.logger.info(
            f"Order Items Transformation Complete ({df.count()} records)."
        )

        return df
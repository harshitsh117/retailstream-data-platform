from pyspark.sql import DataFrame

from src.project_logging.logger import Logger
from src.silver.spark_base_transformer import SparkBaseTransformer


class SparkOrdersTransformer(SparkBaseTransformer):

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def transform(self, df: DataFrame) -> DataFrame:

        self.logger.info("Starting Orders Transformation...")

        df = self.remove_duplicates(df)

        df = self.trim_strings(df)

        df = self.convert_datetime(
            df,
            ["order_date"],
        )

        self.logger.info(
            f"Orders Transformation Complete ({df.count()} records)."
        )

        return df
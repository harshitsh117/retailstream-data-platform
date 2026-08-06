from pyspark.sql import SparkSession

from src.project_logging.logger import get_logger
from src.warehouse.loaders.warehouse_loader import WarehouseLoader

logger = get_logger(__name__)


class WarehousePipeline:

    def __init__(self, spark: SparkSession):
        self.spark = spark
        self.loader = WarehouseLoader()

    def run(self):

        gold_tables = {
            "dim_customer": "datasets/gold/dim_customer",
            "dim_product": "datasets/gold/dim_product",
            "dim_date": "datasets/gold/dim_date",
            "fact_sales": "datasets/gold/fact_sales",
        }

        for table_name, path in gold_tables.items():

            logger.info(f"Reading {table_name}...")

            df = self.spark.read.parquet(path)

            logger.info(f"{table_name}: {df.count()} rows")

            self.loader.load_table(
                dataframe=df,
                table_name=table_name,
            )

        logger.info("Warehouse load completed.")
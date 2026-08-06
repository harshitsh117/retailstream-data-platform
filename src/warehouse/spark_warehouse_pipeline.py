from src.data_access.spark_gold_loader import SparkGoldLoader
from src.project_logging.logger import Logger
from src.warehouse.spark_warehouse_writer import SparkWarehouseWriter


class SparkWarehousePipeline:

    def __init__(self):

        self.logger = Logger.get_logger(__name__)
        self.writer = SparkWarehouseWriter()

    def run(self):

        self.logger.info(
            "Starting Warehouse Pipeline..."
        )

        tables = {
            "dim_customer": SparkGoldLoader.load_dim_customer(),
            "dim_product": SparkGoldLoader.load_dim_product(),
            "dim_date": SparkGoldLoader.load_dim_date(),
            "fact_sales": SparkGoldLoader.load_fact_sales(),
        }

        for table_name, dataframe in tables.items():

            self.logger.info(
                "Loading %s (%d rows)",
                table_name,
                dataframe.count(),
            )

            self.writer.write(
                dataframe,
                table_name,
            )

        self.logger.info(
            "Warehouse Pipeline completed successfully."
        )
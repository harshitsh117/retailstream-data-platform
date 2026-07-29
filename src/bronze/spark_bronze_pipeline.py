from src.bronze.spark_bronze_writer import SparkBronzeWriter
from src.data_access.spark_data_loader import SparkDataLoader
from src.project_logging.logger import Logger


class SparkBronzePipeline:
    """
    Spark implementation of the Bronze Pipeline.
    """

    def __init__(self):
        self.logger = Logger.get_logger(__name__)
        self.writer = SparkBronzeWriter()

    def run(self):

        self.logger.info("Starting Spark Bronze Pipeline...")

        datasets = {
            "customers": SparkDataLoader.load_customers(),
            "products": SparkDataLoader.load_products(),
            "orders": SparkDataLoader.load_orders(),
            "order_items": SparkDataLoader.load_order_items(),
        }

        for dataset_name, dataframe in datasets.items():

            self.logger.info(
                "Processing dataset: %s",
                dataset_name,
            )

            self.writer.write(
                dataframe=dataframe,
                dataset_name=dataset_name,
            )

        self.logger.info(
            "Spark Bronze Pipeline completed successfully."
        )
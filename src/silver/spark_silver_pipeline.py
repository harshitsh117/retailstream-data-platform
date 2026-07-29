from src.data_access.spark_bronze_loader import SparkBronzeLoader
from src.project_logging.logger import Logger
from src.silver.spark_customer_transformer import SparkCustomerTransformer
from src.silver.spark_silver_writer import SparkSilverWriter
from src.data_access.spark_bronze_loader import SparkBronzeLoader
from src.project_logging.logger import Logger

from src.silver.spark_customer_transformer import SparkCustomerTransformer
from src.silver.spark_product_transformer import SparkProductTransformer
from src.silver.spark_orders_transformer import SparkOrdersTransformer
from src.silver.spark_order_items_transformer import SparkOrderItemsTransformer

from src.silver.spark_silver_writer import SparkSilverWriter

class SparkSilverPipeline:

    def __init__(self):

        self.logger = Logger.get_logger(__name__)
        self.writer = SparkSilverWriter()

        self.transformers = {}

    def register(
        self,
        dataset_name,
        transformer,
    ):
        self.transformers[dataset_name] = transformer

    def run(self):

        self.logger.info(
            "Starting Spark Silver Pipeline..."
        )

        loader_mapping = {
        "customers": SparkBronzeLoader.load_customers,
        "products": SparkBronzeLoader.load_products,
        "orders": SparkBronzeLoader.load_orders,
        "order_items": SparkBronzeLoader.load_order_items,
    }

        for dataset_name, transformer in self.transformers.items():

            self.logger.info(
                "Processing %s...",
                dataset_name,
            )

            dataframe = loader_mapping[
                dataset_name
            ]()

            dataframe = transformer.transform(
                dataframe
            )

            self.writer.write(
                dataframe,
                dataset_name,
            )

        self.logger.info(
            "Spark Silver Pipeline completed successfully."
        )
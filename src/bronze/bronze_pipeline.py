from __future__ import annotations

from src.bronze.bronze_writer import BronzeWriter
from src.data_access.data_loader import DataLoader
from src.project_logging.logger import Logger


class BronzePipeline:
    """
    Pipeline for ingesting raw datasets into the Bronze layer.
    """

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)
        self.writer = BronzeWriter()

    def run(self) -> None:
        """
        Execute the Bronze ingestion pipeline.
        """

        self.logger.info("Starting Bronze Pipeline...")

        datasets = {
            "customers": DataLoader.load_customers(),
            "products": DataLoader.load_products(),
            "orders": DataLoader.load_orders(),
            "order_items": DataLoader.load_order_items(),
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

        self.logger.info("Bronze Pipeline completed successfully.")
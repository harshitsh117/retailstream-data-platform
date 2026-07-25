from __future__ import annotations

from src.data_access.data_loader import DataLoader
from src.project_logging.logger import Logger
from src.silver.silver_writer import SilverWriter


class SilverPipeline:
    """
    Pipeline responsible for transforming Bronze datasets
    into Silver datasets.
    """

    def __init__(self) -> None:

        self.logger = Logger.get_logger(__name__)

        self.writer = SilverWriter()

        self.transformers = {}

    def register(
        self,
        dataset_name: str,
        transformer,
    ) -> None:
        """
        Register a dataset transformer.
        """

        self.transformers[dataset_name] = transformer

        self.logger.info(
            "Registered transformer for '%s'.",
            dataset_name,
        )

    def run(self) -> None:
        """
        Execute the Silver pipeline.
        """

        self.logger.info(
            "Starting Silver Pipeline..."
        )

        loader_mapping = {
            "customers": DataLoader.load_customers,
            "products": DataLoader.load_products,
            "orders": DataLoader.load_orders,
            "order_items": DataLoader.load_order_items,
        }

        for dataset_name, transformer in self.transformers.items():

            self.logger.info(
                "Processing '%s'...",
                dataset_name,
            )

            dataframe = loader_mapping[dataset_name]()

            dataframe = transformer.transform(dataframe)

            self.writer.write(
                dataframe=dataframe,
                dataset_name=dataset_name,
            )

        self.logger.info(
            "Silver Pipeline completed successfully."
        )
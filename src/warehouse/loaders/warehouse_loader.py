from pyspark.sql import DataFrame

from src.project_logging.logger import get_logger
from src.warehouse.database.database_manager import DatabaseManager


logger = get_logger(__name__)


class WarehouseLoader:
    """
    Loads Spark DataFrames into PostgreSQL warehouse.
    """

    def __init__(self):
        self.db = DatabaseManager()

    def load_table(
        self,
        dataframe: DataFrame,
        table_name: str,
    ):
        logger.info(f"Loading table '{table_name}' into PostgreSQL...")

        self.db.write_dataframe(
            spark_df=dataframe,
            table_name=table_name,
        )

        logger.info(f"Finished loading '{table_name}'.")
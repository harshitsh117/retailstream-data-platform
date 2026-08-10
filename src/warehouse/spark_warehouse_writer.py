from pyspark.sql import DataFrame

from src.project_logging.logger import Logger
from src.warehouse.database.database_manager import DatabaseManager


class SparkWarehouseWriter:

    def __init__(self):
        self.logger = Logger.get_logger(__name__)
        self.db = DatabaseManager()

    def write(
        self,
        dataframe: DataFrame,
        table_name: str,
        mode: str = None,
    ):
        self.logger.info(
            "Writing '%s' to PostgreSQL...",
            table_name,
        )

        if mode:
            dataframe.write \
                .mode(mode) \
                .jdbc(
                    url=self.db.jdbc_url,
                    table=table_name,
                    properties=self.db.jdbc_properties(),
                )
        else:
            self.db.write_dataframe(
                dataframe,
                table_name,
            )

        self.logger.info(
            "Finished writing '%s'.",
            table_name,
        )
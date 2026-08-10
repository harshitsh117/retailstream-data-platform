from pyspark.sql import DataFrame

from src.config.config_manager import ConfigManager


class DatabaseManager:

    def __init__(self):

        config = ConfigManager()

        self.host = config.get("warehouse.host")
        self.port = config.get("warehouse.port")
        self.database = config.get("warehouse.database")

        self.username = config.get("warehouse.username")
        self.password = config.get("warehouse.password")

        self.driver = config.get(
            "warehouse.driver",
            "org.postgresql.Driver",
        )

        self.write_mode = config.get(
            "warehouse.write_mode",
            "overwrite",
        )

        self.jdbc_url = (
            f"jdbc:postgresql://"
            f"{self.host}:{self.port}/{self.database}"
        )

    def jdbc_properties(self):

        return {
            "user": self.username,
            "password": self.password,
            "driver": self.driver,
        }

    def write_dataframe(
        self,
        dataframe: DataFrame,
        table_name: str,
    ):

        (
            dataframe.write
            .mode(self.write_mode)
            .jdbc(
                url=self.jdbc_url,
                table=table_name,
                properties=self.jdbc_properties(),
            )
        )
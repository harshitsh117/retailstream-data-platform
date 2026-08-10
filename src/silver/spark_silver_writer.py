from pyspark.sql import DataFrame

from src.project_logging.logger import Logger
from src.utils.paths import PathManager


class SparkSilverWriter:

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def write(
        self,
        dataframe: DataFrame,
        dataset_name: str,
    ):

        output_path = (
            PathManager.SILVER_DIR /
            dataset_name
        )

        (
            dataframe.write
            .mode("overwrite")
            .parquet(str(output_path))
        )

        self.logger.info(
            "Silver dataset '%s' written successfully.",
            dataset_name,
        )
from pyspark.sql import DataFrame

from src.project_logging.logger import Logger
from src.utils.paths import PathManager


class SparkGoldWriter:

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def write(self, dataframe: DataFrame, dataset_name: str):

        output_path = (
            PathManager.GOLD_DIR /
            dataset_name
        )

        (
            dataframe.write
            .mode("overwrite")
            .parquet(str(output_path))
        )

        self.logger.info(
            "Gold dataset '%s' written successfully.",
            dataset_name,
        )
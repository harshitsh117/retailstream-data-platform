from pyspark.sql import DataFrame
from spark.session.spark_session import SparkManager


class BronzeReader:
    """
    Reads datasets from the Raw layer into Spark DataFrames.
    """

    def __init__(self):
        self.spark = SparkManager.get_session()

    def read_csv(
        self,
        file_path: str,
        header: bool = True,
        infer_schema: bool = True,
    ) -> DataFrame:
        """
        Read a CSV file into a Spark DataFrame.
        """

        return (
            self.spark.read.format("csv")
            .option("header", str(header).lower())
            .option("inferSchema", str(infer_schema).lower())
            .load(file_path)
        )
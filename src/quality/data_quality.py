from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class DataQuality:

    @staticmethod
    def check_null(df: DataFrame, column: str):

        count = df.filter(col(column).isNull()).count()

        if count > 0:
            raise ValueError(
                f"Column '{column}' contains {count} NULL values."
            )

        print(f"PASS : {column} has no NULL values.")

    @staticmethod
    def check_duplicates(df: DataFrame, column: str):

        duplicates = (
            df.groupBy(column)
              .count()
              .filter(col("count") > 1)
              .count()
        )

        if duplicates > 0:
            raise ValueError(
                f"Column '{column}' contains duplicate values."
            )

        print(f"PASS : {column} contains unique values.")

    @staticmethod
    def check_positive(df: DataFrame, column: str):

        count = df.filter(col(column) <= 0).count()

        if count > 0:
            raise ValueError(
                f"Column '{column}' contains non-positive values."
            )

        print(f"PASS : {column} contains positive values.")
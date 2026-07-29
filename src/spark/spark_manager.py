from pyspark.sql import SparkSession


class SparkManager:
    _spark = None

    @classmethod
    def get_spark(cls):
        if cls._spark is None:
            cls._spark = (
                SparkSession.builder
                .appName("RetailStream")
                .master("local[*]")
                .getOrCreate()
            )
        return cls._spark
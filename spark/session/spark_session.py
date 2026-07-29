from pyspark.sql import SparkSession


class SparkManager:
    """
    Singleton class for creating and managing SparkSession.
    """

    _spark = None

    @classmethod
    def get_session(cls) -> SparkSession:

        if cls._spark is None:

            cls._spark = (
                SparkSession.builder
                .appName("RetailStream Data Platform")
                .master("local[*]")

                # Performance
                .config("spark.sql.shuffle.partitions", "8")

                # Consistent timestamps
                .config("spark.sql.session.timeZone", "UTC")

                # Better parquet performance
                .config(
                    "spark.sql.parquet.compression.codec",
                    "snappy",
                )

                # Adaptive Query Execution
                .config(
                    "spark.sql.adaptive.enabled",
                    "true",
                )

                .getOrCreate()
            )

            cls._spark.sparkContext.setLogLevel("WARN")

        return cls._spark

    @classmethod
    def stop(cls):

        if cls._spark is not None:
            cls._spark.stop()
            cls._spark = None
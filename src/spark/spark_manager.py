from pyspark.sql import SparkSession

from src.config.config_manager import ConfigManager


class SparkManager:

    _spark = None

    @classmethod
    def get_spark(cls):

        if cls._spark is None:

            config = ConfigManager()

            app_name = config.get("spark.app_name", "RetailStream")
            master = config.get("spark.master", "local[*]")

            builder = (
                SparkSession.builder
                .appName(app_name)
                .master(master)
            )

            # Add Maven packages
            packages = config.get("spark.jars_packages", [])

            if packages:
                builder = builder.config(
                    "spark.jars.packages",
                    ",".join(packages)
                )

            # Add additional Spark configs
            spark_configs = config.get("spark.configs", {})

            for key, value in spark_configs.items():
                builder = builder.config(key, value)

            cls._spark = builder.getOrCreate()

        return cls._spark
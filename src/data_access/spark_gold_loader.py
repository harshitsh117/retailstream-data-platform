from src.spark.spark_manager import SparkManager


class SparkGoldLoader:
    spark = SparkManager.get_spark()

    BASE_PATH = "datasets/gold"

    @classmethod
    def load_dim_customer(cls):
        return cls.spark.read.parquet(f"{cls.BASE_PATH}/dim_customer")

    @classmethod
    def load_dim_product(cls):
        return cls.spark.read.parquet(f"{cls.BASE_PATH}/dim_product")

    @classmethod
    def load_dim_date(cls):
        return cls.spark.read.parquet(f"{cls.BASE_PATH}/dim_date")

    @classmethod
    def load_fact_sales(cls):
        return cls.spark.read.parquet(f"{cls.BASE_PATH}/fact_sales")
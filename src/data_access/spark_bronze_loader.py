from src.spark.spark_manager import SparkManager
from src.utils.paths import PathManager


class SparkBronzeLoader:

    @staticmethod
    def load_customers():
        spark = SparkManager.get_spark()
        return spark.read.parquet(
            str(PathManager.BRONZE_DIR / "customers")
        )

    @staticmethod
    def load_products():
        spark = SparkManager.get_spark()
        return spark.read.parquet(
            str(PathManager.BRONZE_DIR / "products")
        )

    @staticmethod
    def load_orders():
        spark = SparkManager.get_spark()
        return spark.read.parquet(
            str(PathManager.BRONZE_DIR / "orders")
        )

    @staticmethod
    def load_order_items():
        spark = SparkManager.get_spark()
        return spark.read.parquet(
            str(PathManager.BRONZE_DIR / "order_items")
        )
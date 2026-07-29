from src.spark.spark_manager import SparkManager
from src.utils.paths import PathManager


class SparkDataLoader:

    @staticmethod
    def load_customers():
        spark = SparkManager.get_spark()
        return (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(PathManager.RAW_DIR / "customers.csv"))
        )

    @staticmethod
    def load_products():
        spark = SparkManager.get_spark()
        return (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(PathManager.RAW_DIR / "products.csv"))
        )

    @staticmethod
    def load_orders():
        spark = SparkManager.get_spark()
        return (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(PathManager.RAW_DIR / "orders.csv"))
        )

    @staticmethod
    def load_order_items():
        spark = SparkManager.get_spark()
        return (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(PathManager.RAW_DIR / "order_items.csv"))
        )
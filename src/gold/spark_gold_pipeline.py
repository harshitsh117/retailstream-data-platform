from src.gold.dim_customer import DimCustomer
from src.gold.dim_product import DimProduct
from src.gold.dim_date import DimDate
from src.gold.fact_sales import FactSales
from src.gold.spark_gold_writer import SparkGoldWriter
from src.gold.spark_silver_loader import SparkSilverLoader
from src.project_logging.logger import Logger
from src.quality.quality_runner import QualityRunner

class SparkGoldPipeline:

    def __init__(self):

        self.logger = Logger.get_logger(__name__)
        self.writer = SparkGoldWriter()

    def run(self):

        self.logger.info("Starting Gold Pipeline...")

        # Load Silver datasets
        customers = SparkSilverLoader.load_customers()
        products = SparkSilverLoader.load_products()
        orders = SparkSilverLoader.load_orders()
        order_items = SparkSilverLoader.load_order_items()
        QualityRunner().validate(
            customers,
            products,
            orders,
            order_items,
        )

        # Build Dimensions
        dim_customer = DimCustomer().build(customers)
        dim_product = DimProduct().build(products)
        dim_date = DimDate().build(orders)

        # Build Fact
        fact_sales = FactSales().build(
            dim_customer,
            dim_product,
            orders,
            order_items,
        )

        # Write Gold tables
        self.writer.write(dim_customer, "dim_customer")
        self.writer.write(dim_product, "dim_product")
        self.writer.write(dim_date, "dim_date")
        self.writer.write(fact_sales, "fact_sales")

        self.logger.info("Gold Pipeline completed.")
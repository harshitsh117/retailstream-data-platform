from src.project_logging.logger import Logger
from src.quality.data_quality import DataQuality
from src.quality.quality_exception import DataQualityException


class QualityRunner:

    def __init__(self):

        self.logger = Logger.get_logger(__name__)

    def validate(
        self,
        customers,
        products,
        orders,
        order_items,
    ):

        try:

            self.logger.info("========== DATA QUALITY CHECK STARTED ==========")

            # ------------------------
            # Customers
            # ------------------------
            DataQuality.check_null(customers, "customer_id")
            DataQuality.check_duplicates(customers, "customer_id")

            # ------------------------
            # Products
            # ------------------------
            DataQuality.check_null(products, "product_id")
            DataQuality.check_duplicates(products, "product_id")
            DataQuality.check_positive(products, "unit_price")

            # ------------------------
            # Orders
            # ------------------------
            DataQuality.check_null(orders, "order_id")
            DataQuality.check_duplicates(orders, "order_id")
            DataQuality.check_positive(orders, "grand_total")

            # ------------------------
            # Order Items
            # ------------------------
            DataQuality.check_null(order_items, "order_item_id")
            DataQuality.check_duplicates(order_items, "order_item_id")
            DataQuality.check_positive(order_items, "quantity")
            DataQuality.check_positive(order_items, "unit_price")

            self.logger.info("========== ALL DATA QUALITY CHECKS PASSED ==========")

        except Exception as e:

            self.logger.error(str(e))

            raise DataQualityException(
                "Data Quality Validation Failed."
            )
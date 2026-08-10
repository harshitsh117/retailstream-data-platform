from src.silver.spark_customer_transformer import SparkCustomerTransformer
from src.silver.spark_order_items_transformer import SparkOrderItemsTransformer
from src.silver.spark_orders_transformer import SparkOrdersTransformer
from src.silver.spark_product_transformer import SparkProductTransformer
from src.silver.spark_silver_pipeline import SparkSilverPipeline


def main():

    pipeline = SparkSilverPipeline()

    pipeline.register(
        "customers",
        SparkCustomerTransformer(),
    )

    pipeline.register(
        "products",
        SparkProductTransformer(),
    )

    pipeline.register(
        "orders",
        SparkOrdersTransformer(),
    )

    pipeline.register(
        "order_items",
        SparkOrderItemsTransformer(),
    )

    pipeline.run()


if __name__ == "__main__":
    main()
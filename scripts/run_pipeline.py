from src.bronze.spark_bronze_pipeline import SparkBronzePipeline
from src.silver.spark_customer_transformer import SparkCustomerTransformer
from src.silver.spark_order_items_transformer import SparkOrderItemsTransformer
from src.silver.spark_orders_transformer import SparkOrdersTransformer
from src.silver.spark_product_transformer import SparkProductTransformer
from src.silver.spark_silver_pipeline import SparkSilverPipeline
from src.gold.spark_gold_pipeline import SparkGoldPipeline


def main():
    print("=" * 80)
    print("RetailStream Data Platform")
    print("=" * 80)

    print("\n[1/3] Running Bronze Pipeline...")
    SparkBronzePipeline().run()

    print("\n[2/3] Running Silver Pipeline...")
    silver = SparkSilverPipeline()

    silver.register("customers", SparkCustomerTransformer())
    silver.register("products", SparkProductTransformer())
    silver.register("orders", SparkOrdersTransformer())
    silver.register("order_items", SparkOrderItemsTransformer())

    silver.run()

    print("\n[3/3] Running Gold Pipeline...")
    SparkGoldPipeline().run()

    print("\n✅ RetailStream pipeline completed successfully.")


if __name__ == "__main__":
    main()
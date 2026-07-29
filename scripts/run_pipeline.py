"""
Master Pipeline Runner.

Runs the complete RetailStream platform:
    Bronze -> Silver -> Gold
"""

from src.bronze.bronze_pipeline import BronzePipeline
from src.silver.silver_pipeline import SilverPipeline
from src.silver.customer_transformer import CustomerTransformer
from src.gold.spark_gold_pipeline import SparkGoldPipeline


def main():

    print("=" * 80)
    print("RetailStream Pipeline Started")
    print("=" * 80)

    # ------------------------------------------------------------------
    # Bronze
    # ------------------------------------------------------------------

    print("\nRunning Bronze Pipeline...")

    BronzePipeline().run()

    print("Bronze Completed.")

    # ------------------------------------------------------------------
    # Silver
    # ------------------------------------------------------------------

    print("\nRunning Silver Pipeline...")

    silver = SilverPipeline()

    silver.register(
        "customers",
        CustomerTransformer(),
    )

    silver.run()

    print("Silver Completed.")

    # ------------------------------------------------------------------
    # Gold
    # ------------------------------------------------------------------

    print("\nRunning Gold Pipeline...")

    SparkGoldPipeline().run()

    print("Gold Completed.")

    print("\nRetailStream Pipeline Finished Successfully.")


if __name__ == "__main__":
    main()
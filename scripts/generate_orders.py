import pandas as pd

from src.generator.order_generator import OrderGenerator
from src.utils.paths import PathManager
from src.utils.file_manager import FileManager


def main():

    print("=" * 60)
    print("Generating Orders Dataset")
    print("=" * 60)

    # ---------------------------------------
    # Load Master Data
    # ---------------------------------------

    customers_df = FileManager.read_csv(
        PathManager.RAW_DIR / "customers.csv"
    )

    products_df = FileManager.read_csv(
        PathManager.RAW_DIR / "products.csv"
    )

    print(f"Customers Loaded : {len(customers_df)}")
    print(f"Products Loaded  : {len(products_df)}")

    # ---------------------------------------
    # Create Generator
    # ---------------------------------------

    generator = OrderGenerator(
        customers_df=customers_df,
        products_df=products_df,
    )

    # ---------------------------------------
    # Generate Orders
    # ---------------------------------------

    orders_df, order_items_df = generator.generate(
        order_count=10000
    )

    # ---------------------------------------
    # Save Files
    # ---------------------------------------

    FileManager.write_csv(
        orders_df,
        PathManager.RAW_DIR / "orders.csv"
    )

    FileManager.write_csv(
        order_items_df,
        PathManager.RAW_DIR / "order_items.csv"
    )

    print()
    print("Generation Complete")
    print(f"Orders       : {len(orders_df)}")
    print(f"Order Items  : {len(order_items_df)}")


if __name__ == "__main__":
    main()
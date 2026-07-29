from src.utils.file_manager import FileManager
from src.utils.paths import PathManager

orders_df = FileManager.read_csv(PathManager.RAW_DIR / "orders.csv")
order_items_df = FileManager.read_csv(PathManager.RAW_DIR / "order_items.csv")
products_df = FileManager.read_csv(PathManager.RAW_DIR / "products.csv")

print("=" * 60)
print("ORDER DATA VALIDATION")
print("=" * 60)

# Row counts
print(f"Orders: {len(orders_df)}")
print(f"Order Items: {len(order_items_df)}")

# Duplicate checks
print(f"Duplicate Order IDs: {orders_df['order_id'].duplicated().sum()}")
print(f"Duplicate Order Item IDs: {order_items_df['order_item_id'].duplicated().sum()}")

# Referential Integrity
missing_orders = (
    ~order_items_df["order_id"].isin(orders_df["order_id"])
).sum()

missing_products = (
    ~order_items_df["product_id"].isin(products_df["product_id"])
).sum()

print(f"Missing Order References: {missing_orders}")
print(f"Missing Product References: {missing_products}")

# Grand Total Validation
calculated_totals = (
    order_items_df.groupby("order_id")["grand_total"]
    .sum()
    .round(2)
)

stored_totals = (
    orders_df.set_index("order_id")["grand_total"]
    .round(2)
)

mismatches = (calculated_totals != stored_totals).sum()

print(f"Grand Total Mismatches: {mismatches}")

print("=" * 60)
from src.generator.order_generator import OrderGenerator
from src.utils.file_manager import FileManager
from src.utils.paths import PathManager


def test_order_generation():
    customers_df = FileManager.read_csv(
        PathManager.RAW_DIR / "customers.csv"
    )
    products_df = FileManager.read_csv(
        PathManager.RAW_DIR / "products.csv"
    )

    generator = OrderGenerator(
        customers_df=customers_df,
        products_df=products_df,
    )

    orders_df, order_items_df = generator.generate(order_count=100)

    assert len(orders_df) == 100
    assert len(order_items_df) > 0
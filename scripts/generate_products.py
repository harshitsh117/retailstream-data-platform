from src.generator.product_generator import ProductGenerator
from src.utils import FileManager, PathManager

generator = ProductGenerator()

products_df = generator.generate(
    count=5000,
    start_id=200001,
)

output_path = PathManager.RAW_DIR / "products.csv"

FileManager.write_csv(
    products_df,
    output_path,
)

print(f"Generated {len(products_df)} products.")
print(f"Saved to: {output_path}")
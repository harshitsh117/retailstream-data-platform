from src.generator.customer_generator import CustomerGenerator
from src.utils import FileManager, PathManager

generator = CustomerGenerator()

customers_df = generator.generate(
    count=10000,
    start_id=100001,
)

output_path = PathManager.RAW_DIR / "customers.csv"

FileManager.write_csv(customers_df, output_path)

print(f"Generated {len(customers_df)} customers.")
print(f"Saved to: {output_path}")
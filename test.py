from src.utils.file_manager import FileManager
from src.utils.paths import PathManager

df = FileManager.read_parquet(
    PathManager.BRONZE_DIR / "customers.parquet"
)

print(df.head())
print(df.columns)
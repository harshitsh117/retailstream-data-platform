import pandas as pd

from src.utils import FileManager, PathManager

df = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
    }
)

output_file = PathManager.RAW_DIR / "customers.csv"

FileManager.write_csv(df, output_file)

loaded_df = FileManager.read_csv(output_file)

print(loaded_df)
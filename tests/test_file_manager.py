import pandas as pd

from src.utils import FileManager


def test_write_and_read_csv(tmp_path):
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
        }
    )

    output_file = tmp_path / "customers.csv"

    FileManager.write_csv(df, output_file)

    loaded_df = FileManager.read_csv(output_file)

    assert output_file.exists()
    assert loaded_df.equals(df)
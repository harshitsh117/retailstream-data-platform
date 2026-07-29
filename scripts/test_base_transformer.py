import pandas as pd

from src.silver.base_transformer import BaseTransformer

df = pd.DataFrame(
    {
        "name": [" Alice ", "Bob", "Bob"],
        "city": [" Delhi ", "Mumbai", "Mumbai"],
        "date": ["2026-07-20", "2026-07-21", "2026-07-21"],
    }
)

transformer = BaseTransformer()

df = transformer.trim_strings(df)

df = transformer.remove_duplicates(df)

df = transformer.convert_datetime(
    df,
    ["date"],
)

print(df)
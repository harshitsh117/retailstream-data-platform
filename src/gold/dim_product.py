from pyspark.sql import DataFrame
from pyspark.sql.functions import col, monotonically_increasing_id


class DimProduct:

    def build(self, products: DataFrame) -> DataFrame:

        return (
            products
            .select(
                col("product_id"),
                col("product_name"),
                col("category"),
                col("sub_category"),
                col("brand"),
                col("supplier"),
                col("unit_price"),
                col("cost_price"),
                col("is_active"),
            )
            .withColumn(
                "product_key",
                monotonically_increasing_id() + 1,
            )
            .select(
                "product_key",
                "product_id",
                "product_name",
                "category",
                "sub_category",
                "brand",
                "supplier",
                "unit_price",
                "cost_price",
                "is_active",
            )
        )
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, monotonically_increasing_id


class DimCustomer:

    def build(self, customers: DataFrame) -> DataFrame:

        return (
            customers
            .select(
                col("customer_id"),
                col("first_name"),
                col("last_name"),
                col("gender"),
                col("email"),
                col("phone"),
                col("city"),
                col("state"),
                col("country"),
            )
            .withColumn(
                "customer_key",
                monotonically_increasing_id() + 1,
            )
            .select(
                "customer_key",
                "customer_id",
                "first_name",
                "last_name",
                "gender",
                "email",
                "phone",
                "city",
                "state",
                "country",
            )
        )
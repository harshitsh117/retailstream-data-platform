from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    year,
    quarter,
    month,
    dayofmonth,
    dayofweek,
    date_format,
)


class DimDate:

    def build(self, orders: DataFrame) -> DataFrame:

        dim_date = (
            orders
            .select(
                col("order_date")
            )
            .dropDuplicates()
            .withColumn(
                "date_key",
                date_format("order_date", "yyyyMMdd").cast("int")
            )
            .withColumn(
                "year",
                year("order_date")
            )
            .withColumn(
                "quarter",
                quarter("order_date")
            )
            .withColumn(
                "month",
                month("order_date")
            )
            .withColumn(
                "month_name",
                date_format("order_date", "MMMM")
            )
            .withColumn(
                "day",
                dayofmonth("order_date")
            )
            .withColumn(
                "day_name",
                date_format("order_date", "EEEE")
            )
            .withColumn(
                "week_day",
                dayofweek("order_date")
            )
        )

        return dim_date
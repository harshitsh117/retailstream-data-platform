from pyspark.sql import DataFrame
from pyspark.sql.functions import col, date_format


class FactSales:

    def build(
        self,
        dim_customer: DataFrame,
        dim_product: DataFrame,
        orders: DataFrame,
        order_items: DataFrame,
    ) -> DataFrame:

        fact_sales = (
            order_items.alias("oi")

            .join(
                orders.alias("o"),
                col("oi.order_id") == col("o.order_id"),
                "inner",
            )

            .join(
                dim_customer.alias("dc"),
                col("o.customer_id") == col("dc.customer_id"),
                "inner",
            )

            .join(
                dim_product.alias("dp"),
                col("oi.product_id") == col("dp.product_id"),
                "inner",
            )

            .select(
                col("dc.customer_key"),
                col("dp.product_key"),

                date_format(
                    col("o.order_date"),
                    "yyyyMMdd"
                ).cast("int").alias("date_key"),

                col("o.order_id"),
                col("oi.order_item_id"),

                col("oi.quantity"),
                col("oi.unit_price"),
                col("oi.discount_percent"),
                col("oi.discount_amount"),
                col("oi.tax_percent"),
                col("oi.tax_amount"),
                col("oi.grand_total"),
            )
        )

        return fact_sales
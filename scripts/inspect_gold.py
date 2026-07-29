from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Inspect Gold Layer")
    .getOrCreate()
)

tables = [
    "dim_customer",
    "dim_product",
    "dim_date",
    "fact_sales"
]

for table in tables:
    print("\n" + "=" * 80)
    print(f"TABLE: {table}")
    print("=" * 80)

    df = spark.read.parquet(f"datasets/gold/{table}")

    print("\nSchema:")
    df.printSchema()

    print("\nSample Data:")
    df.show(5, truncate=False)

    print(f"\nRow Count: {df.count()}")

spark.stop()
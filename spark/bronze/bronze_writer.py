from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, lit


class BronzeWriter:
    """
    Writes DataFrames to the Bronze layer.
    """

    def write_parquet(
        self,
        df: DataFrame,
        output_path: str,
        dataset_name: str,
        source_system: str = "RetailStream",
        mode: str = "overwrite",
    ) -> None:
        """
        Add Bronze metadata and write as Parquet.
        """

        bronze_df = (
            df.withColumn("ingestion_timestamp", current_timestamp())
              .withColumn("source_system", lit(source_system))
              .withColumn("dataset_name", lit(dataset_name))
        )

        (
            bronze_df.write
            .mode(mode)
            .option("compression", "snappy")
            .parquet(output_path)
        )

        print(f"Successfully wrote Bronze dataset to: {output_path}")
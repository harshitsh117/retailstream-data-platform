from spark.bronze.bronze_reader import BronzeReader
from spark.bronze.bronze_writer import BronzeWriter


def main():

    reader = BronzeReader()
    writer = BronzeWriter()

    df = reader.read_csv("datasets/raw/customers.csv")

    writer.write_parquet(
        df=df,
        output_path="datasets/bronze/customers",
        dataset_name="customers",
    )

    print("Bronze write completed.")


if __name__ == "__main__":
    main()
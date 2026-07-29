from spark.bronze.bronze_reader import BronzeReader


def main():

    reader = BronzeReader()

    df = reader.read_csv("datasets/raw/customers.csv")

    print("=" * 60)
    print("Schema")
    print("=" * 60)
    df.printSchema()

    print("=" * 60)
    print("Sample Data")
    print("=" * 60)
    df.show(5, truncate=False)

    print("=" * 60)
    print(f"Total Records : {df.count()}")


if __name__ == "__main__":
    main()
from src.bronze.bronze_writer import BronzeWriter
from src.data_access.data_loader import DataLoader


def main():

    writer = BronzeWriter()

    customers = DataLoader.load_customers()

    writer.write(
        dataframe=customers,
        dataset_name="customers",
    )

    print("Bronze dataset written successfully.")


if __name__ == "__main__":
    main()
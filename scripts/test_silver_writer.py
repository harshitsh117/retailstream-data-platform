from src.data_access.data_loader import DataLoader
from src.silver.customer_transformer import CustomerTransformer
from src.silver.silver_writer import SilverWriter


def main():

    customers = DataLoader.load_customers()

    transformer = CustomerTransformer()

    customers = transformer.transform(customers)

    writer = SilverWriter()

    writer.write(
        customers,
        "customers",
    )

    print("Silver dataset written successfully.")


if __name__ == "__main__":
    main()
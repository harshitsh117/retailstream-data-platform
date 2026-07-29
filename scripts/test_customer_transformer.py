from src.data_access.data_loader import DataLoader
from src.silver.customer_transformer import CustomerTransformer


def main():

    customers = DataLoader.load_customers()

    transformer = CustomerTransformer()

    silver_df = transformer.transform(customers)

    print(silver_df.head())

    print()

    print(f"Records: {len(silver_df)}")


if __name__ == "__main__":
    main()
from src.silver.customer_transformer import CustomerTransformer
from src.silver.silver_pipeline import SilverPipeline


def main():

    pipeline = SilverPipeline()

    pipeline.register(
        "customers",
        CustomerTransformer(),
    )

    pipeline.run()

    print("\nSilver Pipeline Executed Successfully!")


if __name__ == "__main__":
    main()
from src.silver.customer_transformer import CustomerTransformer
from src.silver.silver_pipeline import SilverPipeline


def main():
    pipeline = SilverPipeline()

    pipeline.register(
        dataset_name="customers",
        transformer=CustomerTransformer(),
    )

    pipeline.run()


if __name__ == "__main__":
    main()
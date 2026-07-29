from src.bronze.bronze_pipeline import BronzePipeline


def main():

    pipeline = BronzePipeline()

    pipeline.run()

    print("\nBronze Pipeline Executed Successfully!")


if __name__ == "__main__":
    main()
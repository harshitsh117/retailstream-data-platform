from src.gold.spark_gold_pipeline import SparkGoldPipeline


def main():

    pipeline = SparkGoldPipeline()
    pipeline.run()


if __name__ == "__main__":
    main()
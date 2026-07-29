from spark.session.spark_session import SparkManager


def main():

    spark = SparkManager.get_session()

    print("=" * 60)
    print("Spark Version :", spark.version)
    print("=" * 60)

    df = spark.range(5)

    df.show()

    SparkManager.stop()


if __name__ == "__main__":
    main()
import traceback

from src.config.config_manager import ConfigManager
from src.spark.spark_manager import SparkManager


def check_config():
    try:
        ConfigManager()
        print("✓ Configuration Loaded")
        return True
    except Exception:
        print("✗ Configuration Failed")
        traceback.print_exc()
        return False


def check_spark():
    try:
        spark = SparkManager.get_spark()
        print(f"✓ Spark Session Created ({spark.sparkContext.appName})")
        return True
    except Exception:
        print("✗ Spark Failed")
        traceback.print_exc()
        return False


def main():
    print("=" * 50)
    print("RetailStream Health Check")
    print("=" * 50)

    results = [
        check_config(),
        check_spark(),
    ]

    print("=" * 50)

    if all(results):
        print("✓ Overall Status: HEALTHY")
    else:
        print("✗ Overall Status: FAILED")

    print("=" * 50)


if __name__ == "__main__":
    main()
from pathlib import Path


class PathManager:
    """Provides project-wide directory paths."""

    # Project Root
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent

    # Main Directories
    CONFIG_DIR = ROOT_DIR / "configs"
    DATASET_DIR = ROOT_DIR / "datasets"
    LOG_DIR = ROOT_DIR / "logs"

    # Dataset Directories
    RAW_DIR = DATASET_DIR / "raw"
    BRONZE_DIR = DATASET_DIR / "bronze"
    SILVER_DIR = DATASET_DIR / "silver"
    GOLD_DIR = DATASET_DIR / "gold"
    # GOLD_DIR = DATASETS_DIR / "gold"

    @classmethod
    def create_directories(cls) -> None:
        """Create required project directories if they don't exist."""

        directories = [
            cls.LOG_DIR,
            cls.DATASET_DIR,
            cls.RAW_DIR,
            cls.BRONZE_DIR,
            cls.SILVER_DIR,
            cls.GOLD_DIR,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
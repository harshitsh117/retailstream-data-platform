import logging
from pathlib import Path
from src.utils import PathManager


class Logger:
    """Factory class for creating configured loggers."""

    _configured = False

    @classmethod
    def _configure(cls) -> None:
        """Configure the root logger only once."""

        if cls._configured:
            return

        PathManager.create_directories()

        log_dir = PathManager.LOG_DIR

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_dir / "retailstream.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

        cls._configured = True

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """Return a configured logger."""

        cls._configure()
        return logging.getLogger(name)
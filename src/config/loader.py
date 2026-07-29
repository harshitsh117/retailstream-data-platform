"""
Configuration Loader.
"""

from pathlib import Path

import yaml

from .exceptions import ConfigFileNotFoundError, InvalidConfigError


class ConfigLoader:

    def __init__(self, config_directory="configs"):
        self.config_directory = Path(config_directory)

    def _get_file_path(self, filename):
        return self.config_directory / filename

    def load_yaml(self, filename):

        file_path = self._get_file_path(filename)

        if not file_path.exists():
            raise ConfigFileNotFoundError(
                f"{filename} not found."
            )

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            return data if data else {}

        except yaml.YAMLError as exc:
            raise InvalidConfigError(
                f"Invalid YAML in {filename}"
            ) from exc

    def load_all(self):
        """
        Load every YAML file inside configs directory.
        """

        configuration = {}

        yaml_files = self.config_directory.glob("*.yaml")

        for file in yaml_files:

            config = self.load_yaml(file.name)

            configuration.update(config)

        return configuration
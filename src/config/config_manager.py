"""
Configuration Manager.
"""

from .loader import ConfigLoader


class ConfigManager:

    def __init__(self):

        self.loader = ConfigLoader()

        self.configuration = self.loader.load_all()

    def get(self, key, default=None):

        keys = key.split(".")

        value = self.configuration

        for k in keys:

            if isinstance(value, dict):

                value = value.get(k)

            else:

                return default

            if value is None:

                return default

        return value
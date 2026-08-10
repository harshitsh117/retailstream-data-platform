"""
Custom exceptions for the configuration framework.
"""


class ConfigError(Exception):
    """Base exception for all configuration-related errors."""

    pass


class ConfigFileNotFoundError(ConfigError):
    """Raised when a configuration file cannot be found."""

    pass


class InvalidConfigError(ConfigError):
    """Raised when a configuration file contains invalid YAML."""

    pass
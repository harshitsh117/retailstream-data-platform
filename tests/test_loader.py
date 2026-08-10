from src.config.config_manager import ConfigManager

config = ConfigManager()

print(config.get("application.name"))
print(config.get("application.version"))
print(config.get("processing.batch_size"))
print(config.get("paths.logs"))
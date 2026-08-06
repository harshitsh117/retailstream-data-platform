from src.config.config_manager import ConfigManager

config = ConfigManager()

print(config.get("warehouse.host"))
print(config.get("warehouse.database"))
print(config.get("warehouse.jdbc_url"))
from src.utils import PathManager

PathManager.create_directories()

print("Project Root :", PathManager.ROOT_DIR)
print("Logs         :", PathManager.LOG_DIR)
print("Raw          :", PathManager.RAW_DIR)
print("Bronze       :", PathManager.BRONZE_DIR)
print("Silver       :", PathManager.SILVER_DIR)
print("Gold         :", PathManager.GOLD_DIR)
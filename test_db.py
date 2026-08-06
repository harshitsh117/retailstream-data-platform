from src.warehouse.database.database_manager import DatabaseManager

db = DatabaseManager()

print(db.jdbc_url)
print(db.username)
print(db.driver)
print(db.jdbc_properties())
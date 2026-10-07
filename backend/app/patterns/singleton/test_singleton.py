from app.patterns.singleton.database_connection import DatabaseConnection


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print("db1:", id(db1))
print("db2:", id(db2))

print("Hai đối tượng có cùng instance:", db1 is db2)
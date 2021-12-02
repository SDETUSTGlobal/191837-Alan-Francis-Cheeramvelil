import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Alan2702"
)
print(db_connection)

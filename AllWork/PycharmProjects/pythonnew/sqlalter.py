import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Alan2702",
  database="testdb"
  )
db_cursor = db_connection.cursor()
#Here we modify existing column id
db_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

import mysql.connector

connection_string = mysql.connector.connect(
   host="localhost",
   user='root',
   password='',
   database='mlcc'

)

cursor = connection_string.cursor()

queryOne = 'desc test'

cursor.execute(queryOne)
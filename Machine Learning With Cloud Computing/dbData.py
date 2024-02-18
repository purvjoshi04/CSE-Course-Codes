import mysql.connector

connection_string = mysql.connector.connect(
   'localhost',
   'root',
   '',
   'mlcc'

)

cursor = connection_string.cursor()

queryOne = 'desc mlcc'

cursor.execute(queryOne)
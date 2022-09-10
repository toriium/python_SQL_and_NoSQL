import datetime
import mysql.connector

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              password='',
                              port=3306,
                              db='starwars', )
cursor = cnx.cursor(dictionary=True)

query = "select * from planets"

cursor.execute(query)

a = cursor.fetchone()

print(a.values())

cursor.close()
cnx.close()

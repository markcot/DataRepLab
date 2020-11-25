import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Root147!",
   database="datarepresentation"
)

cursor = db.cursor()
sql="update student set name = %s, age = %s where id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
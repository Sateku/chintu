import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="Brahmam$$11")
cursor=mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())












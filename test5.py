import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Brahmam$$11")
cursor = mydb.cursor()
s="insert into karthik.karthik values(101,'Satesh Kumar','ksateshkumar',11)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
mydb.commit()
cursor.execute("select * from karthik.karthik")
for i in cursor.fetchall():
    print(i)


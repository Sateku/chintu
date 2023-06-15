import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Brahmam$$11")
cursor = mydb.cursor()
cursor.execute("select employee_id , emp_mailid from karthik.karthik")
l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))
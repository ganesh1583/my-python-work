import csv
import mysql.connector

f = open("demo.csv", "r")
read = csv.reader(f)

con = mysql.connector.connect(host="localhost", port=3306, user="debian-sys-maint", password="BupGZQPbG0Eab9Ux", database="mydb")
cur = con.cursor()

cur.execute("create table mobile (product varchar(100), cust_name varchar(100), rating int, heading varchar(100), comment varchar(500))")

for i in list(read)[1::]:
	try:
	    cur.execute(f"insert into mobile values ('{i[0]}', '{i[1]}', {i[2]}, '{i[3]}', '{i[4]}')")
	except Exception as e:
		print(i[0], i[1], i[2], i[3], i[4],"\n",e)
con.commit()
cur.close()
con.close()
f.close()

print("mobile table created")

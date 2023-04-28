import sqlite3
conn = sqlite3.connect('database.db')

print("Opened database successfully")

conn.execute('CREATE TABLE employees (empid int not null, empname varchar(255) not null, empgender varchar(1) not null, empphone varchar(4) not null, empbdate varchar(10) not null)')

print("Table created successfully")

conn.close()



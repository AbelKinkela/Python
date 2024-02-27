# to connect to sqlite we import it first
# then we need two main objects: a connection and a cursor.
# The connect query will create the database if it doesn't exist and connects to it
# The cursor is the interface needed to communicate with the database.
# After we are done we must commit the changes, and close connections

# in the code below we create a new database connection, create a cursor and execute 2 sql statements 
# to create tables Dept and Students

import sqlite3

conn = sqlite3.connect("univ.db")

cursor = conn.cursor()

cursor.execute('create table Dept(deptno integer primary key, name text)')
cursor.execute('create table Students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')
conn.commit()
cursor.close()
conn.close()
import sqlite3

conn = sqlite3.connect("univ.db")

cursor = conn.cursor()
# cursor.execute('insert into Dept values(10, "CSE")') # without sepcifying the keys we enter the values in order
# cursor.execute('insert into Dept(name, deptno) values("ECE", 20)') # specifying the values we can add values in the order we want
# cursor.execute('insert into Dept values(30, "Civil")')
# cursor.execute('insert into Dept values(40, "Mech")')
# cursor.execute('insert into Dept values(50,"Eng")')
cursor.execute('insert into dept(dname, deptno) values("BA", 60)') # specifying the values we can add values in the order we want

cursor.execute('insert into Students values(0, "António", "Luanda", 50)')

conn.commit()
cursor.close()
conn.close()
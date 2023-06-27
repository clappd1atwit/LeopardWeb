from ctypes.wintypes import CHAR
import sqlite3

database = sqlite3.connect("assignment3.db") 

cur = database.cursor()


cur.execute("""CREATE TABLE if not exists Course(
    CRN int, 
    Title text,
    department text,
    time text,
    days of the week text,
    semster text,
    year int,
    credit int,
    Prof text
);""")


cur.execute("INSERT INTO Course VALUES(34285, 'Advanced Digital', 'BSCO', '1230', 'MF', 'Summer', 2023, 4);")
cur.execute("INSERT INTO Course VALUES(33950, 'Applied Programming', 'BSCO', '800', 'MTR', 'Summer', 2023, 3);")
cur.execute("INSERT INTO Course VALUES(12865, 'Econ', 'HUSS', '800', 'MTR', 'Summer', 2023, 4);")
cur.execute("INSERT INTO Course VALUES(03648, 'Materials', 'BSME', '800', 'MTR', 'Summer', 2023, 3);")
cur.execute("INSERT INTO Course VALUES(33957, 'Computer Network', 'BSCO', '1100', 'MF', 'Summer', 2023, 4);")

uid = int(input("Student 1 ID: "))
fname = input("Student 1 First name: ")
lname = input("Student 1 Last name: ")
Gradyear = int(input("Student 1 Grad year: "))
maj = input("Student 1 Major: ")
mail = input("Student 1 Email: ")

cur.execute("""INSERT INTO STUDENT VALUES('%d', '%s', '%s', '%d', '%s', '%s')""" % (uid, fname, lname, Gradyear, maj, mail))


uid = int(input("Student 2 ID: "))
fname = input("Student 2 First name: ")
lname = input("Student 2 Last name: ")
Gradyear = int(input("Student 2 Grad year: "))
maj = input("Student 2 Major: ")
mail = input("Student 2 Email: ")

cur.execute("""INSERT INTO STUDENT VALUES('%d', '%s', '%s', '%d', '%s', '%s')""" % (uid, fname, lname, Gradyear, maj, mail))

cur.execute("""DELETE FROM INSTRUCTOR WHERE ID = '%d'""" % (20001))

cur.execute("""UPDATE ADMIN SET TITLE = 'Vice President' WHERE ID = '%d'""" % (30002))

for i in range(0,5):
    cur.execute("""SELECT Title FROM Course""")
    courseTitles = cur.fetchall()
    cur.execute("""SELECT department FROM Course WHERE Title = '%s'""" % courseTitles[i])
    dept = cur.fetchone()
    cur.execute("""SELECT NAME FROM INSTRUCTOR WHERE DEPT = '%s'""" % dept)
    Prof_Name = cur.fetchone()
    print(f"{courseTitles[i]} is a {dept} class and can be taught by Prof. {Prof_Name}") 
    

cur.execute("""SELECT * FROM Course""")
query_result = cur.fetchall()
  
for i in query_result:
	print(i)


database.commit()

database.close()


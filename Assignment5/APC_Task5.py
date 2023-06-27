from ctypes.wintypes import CHAR
import sqlite3

database = sqlite3.connect("assignment3.db") 

cur = database.cursor()

#Create 4 databases (course, Student, Prof, Admin)
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

cur.execute("""CREATE TABLE if not exists Professor(
    ID int
    Password text
);""")

cur.execute("""CREATE TABLE if not exists Student(
    ID int
    Password text
);""")

cur.execute("""CREATE TABLE if not exists Admin(
    ID int
    Password text
);""")



#Function for Log in
uID = int(input("What is your ID: "))
cur.execute("""SELECT * FROM Professor, Student, Admin WHERE ID = '%d'""" % uID)





database.commit()

database.close()

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
    semester text,
    year int,
    credit int,
    professor text
);""")#Created Course table if not already made

#Needs to be run first time to setup db
#cur.execute("""ALTER TABLE STUDENT ADD COLUMN courseCRN""")
#cur.execute("""ALTER TABLE INSTRUCTOR ADD COLUMN courseCRN""")
#cur.execute("INSERT INTO Course VALUES(34285, 'Advanced Digital', 'BSCO', '12:30', 'MF', 'Summer', 2023, 4, 'Pilin');")
#cur.execute("INSERT INTO Course VALUES(33950, 'Applied Programming', 'BSCO', '8:00', 'MTR', 'Summer', 2023, 3, 'Rawlins');")
#cur.execute("INSERT INTO Course VALUES(12865, 'Econ', 'HUSS', '8:00', 'MTR', 'Summer', 2023, 4, 'Cort');")
#cur.execute("INSERT INTO Course VALUES(03648, 'Materials', 'BSME', '8:00', 'MTR', 'Summer', 2023, 3, 'Bernoulli');")
#cur.execute("INSERT INTO Course VALUES(33957, 'Computer Network', 'BSCO', '11:00', 'MF', 'Summer', 2023, 4, 'Hasebbo');")


class User:
# constructor
    def __init__(self, Firstname, Lastname, ID):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.ID = ID

    # set and get
    def setName(self, Firstname, Lastname, ID):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.ID = ID

    def getName(self):
        return self.Firstname, self.Lastname, self.ID

    # similar to toString
    def printAllCourses():
        cur.execute("""SELECT * FROM Course""")
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)

    def findcourse():
        SearchCourse()

    def description(self):
        return 0


class Student (User):
# constructor
    def __init__(self, Firstname, Lastname, ID):
        User.__init__(self, Firstname, Lastname, ID) # call base constructor
        self.Lastname = Lastname

    def setcourse(self, Lastname): #add classes to database
        aCRN = int(input('What is the CRN of the course you like to add: '))
        cur.execute("""UPDATE STUDENT SET courseCRN = '%d' WHERE SURNAME = '%s'""" % (aCRN, Lastname))

    def removecourse(self, Lastname): #remove courses
        rCRN = int(input('What is the CRN of the course you want to Drop: '))
        cur.execute("""UPDATE STUDENT SET courseCRN = '' WHERE courseCRN = '%d' AND SURNAME = '%s'""" % (rCRN, Lastname))

    def getschedule(self, Lastname):
        cur.execute("""SELECT courseCRN FROM STUDENT WHERE SURNAME = '%s'""" % Lastname)
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
    #self.courses
    

class instructor (User):
# constructor
    def __init__(self, Firstname, Lastname, ID):
        User.__init__(self, Lastname) # call base constructor
        self.Lastname = Lastname

    def getcourselist(self, Lastname):
        cur.execute("""SELECT CRN FROM Course WHERE professor = '%s'""" % Lastname)
        query_CRN = cur.fetchall()
        cur.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE courseCRN = '%s'""" % query_CRN)
        query_result = cur.fetchall()
        for i in query_result:
            print(i) 

    def DisplaySchedule(self, Lastname):
        cur.execute("""SELECT courseCRN FROM INSTRUCTOR WHERE SURNAME = '%s'""" % Lastname)
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)

        #self.width = height
    

class admin (User):
# constructor
    def __init__(self, Firstname, Lastname, ID):
        User.__init__(self) # call base constructor

    def addcourse():
        intCRN = int(input('Course CRN: '))
        sName = input('Course Name: ')
        sDept = input('Course Department: ')
        sTime = input('Course Time: ')
        sDays = input('Days of the week: ')
        sSemester = input('Semester Offered: ')
        intYear = int(input('Year Course is offered: '))
        intCredit = int(input('Number of credits for course: '))
        sProf = input('Who is teaching the class: ')
        cur.execute("""INSERT INTO Course VALUES('%d','%s', '%s','%s', '%s', '%s', '%d', '%d', '%s')""" % (intCRN, sName, sDept, sTime, sDays, sSemester, intYear, intCredit, sProf))
        
    def removecourse():
        rCRN = int(input('What is the CRN of the course you want to remove: '))
        cur.execute("""DELETE FROM Course WHERE CRN = '%d'""" % rCRN)

    def addcourseto():
        resp = input("Do you want to add a course from a Student or Instructor: ")

        if resp == 'Student':
            sID = int(input('What is the Students ID: '))
            iCRN = int(input('What CRN would you like to add: '))
            cur.execute("""UPDATE STUDENT SET courseCRN = '%d' WHERE ID = '%d'""" % (iCRN, sID))
        elif resp == instructor:
            sID = int(input('What is the Instructors ID: '))
            iCRN = int(input('What CRN would you like to add: '))
            cur.execute("""UPDATE INSTRUCTOR SET courseCRN = '%d' WHERE ID = '%d'""" % (iCRN, sID))
        else:
            print('Not a valid responce')

    def removecourseto():
        resp = input('Do you want to remove a course from a Student or Instructor: ')
        if resp == 'Student':
            sID = int(input('What is the Students ID: '))
            iCRN = int(input('What CRN would you like to remove: '))
            cur.execute("""UPDATE STUDENT SET courseCRN = '' WHERE ID = '%d' AND courseCRN = '%d'""" % (sID, iCRN))
        elif resp == instructor:
            sID = int(input('What is the Instructors ID: '))
            iCRN = int(input('What CRN would you like to remove: '))
            cur.execute("""UPDATE INSTRUCTOR SET courseCRN = '' WHERE ID = '%d' AND courseCRN = '%d'""" % (sID, iCRN))
        else:
            print('Not a valid responce')

    def checkIDschhedule():
        resp = input("Do you want to check the schedule of a Student or Instructor: ")


def SearchCourse():  #Function for searching a course given a parameter (Adam)
    searchMethod = 0
    print('Course Search:')
    print('1: CRN')
    print('2: Despartment')
    print('3: Time')
    print('4: Days')
    searchMethod = input('How would you like to search? ')
    if searchMethod == '1':
        crn = int(input('What is the course CRN value: '))
        cur.execute("""SELECT * FROM Course WHERE CRN = '%d'""" % crn) 
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
    elif searchMethod == '2':
        dept = input('What department do you want to search in: ')
        cur.execute("""SELECT * FROM Course WHERE department = '%s'""" % dept) 
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
    elif searchMethod == '3':
        ctm = input('What time do you want the class at: ')
        cur.execute("""SELECT * FROM Course WHERE time = '%s'""" % ctm)  
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
    elif searchMethod == '4':
        dys = input('What days do you want class on: ')
        cur.execute("""SELECT * FROM Course WHERE days = '%s'""" % dys) 
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)


def printOptions(userNum): #Menu for selecting what you want to do
    UserInput = 0
    print("1: List Courses")
    print("2: Search Course Using Parameters")
    if userNum == 1:
        print('3: Add Course')
        print('4: Remove Course')
        print('5: Log out')
    if userNum == 2:
        print('3: Assemble Roster')
        print('4: Log out')
    if userNum == 3:
        print('3: Add Course')
        print('4: Drop Course')
        print('5: Log out')
    UserInput = input('')
    if UserInput == '1':
        cur.execute("""SELECT * FROM Course""")
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
    elif UserInput == '2':
        SearchCourse()
    return UserInput


#Function for Log in (Liam/Dan)
def login():
    successful_login = 0
    while(successful_login == 0):
        print('Log in')
        email = input('Email: ')
        cur.execute("""SELECT COUNT(*) FROM STUDENT WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if(query_result[0] == 1):
            return 'Student'
            successful_login = 1
        else:
            cur.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE EMAIL = '%s'""" % email)
            query_result = cur.fetchone()
            if(query_result[0] == 1):
                cur.execute("""SELECT SURNAME FROM INSTRUCTOR WHERE EMAIL = '%s'""" % email)
                query_result = cur.fetchone()
                usersName = query_result
                return 'Instructor'
                successful_login = 1
            else:
                cur.execute("""SELECT COUNT(*) FROM ADMIN WHERE EMAIL = '%s'""" % email)
                query_result = cur.fetchone()
                if(query_result[0] == 1):
                    return 'Admin'
                    successful_login = 1
                else:
                    print("invalid email ... try again")


User = login()
run = True
while run: #Run as long as you are signed in (Liam)

    usersName = '' 
    run = False

    if User == 'Admin': #Admin commands and functions (Adam)
       userAdmin = admin('Margaret', 'Hamilton', 3001)
       actions = printOptions(1)
       if actions == '3':
           intCRN = int(input('Course CRN: '))
           sName = input('Course Name: ')
           sDept = input('Course Department: ')
           sTime = input('Course Time: ')
           sDays = input('Days of the week: ')
           sSemester = input('Semester Offered: ')
           intYear = int(input('Year Course is offered: '))
           intCredit = int(input('Number of credits for course: '))
           sProf = input('Who is teaching the class: ')
           cur.execute("""INSERT INTO Course VALUES('%d','%s', '%s','%s', '%s', '%s', '%d', '%d', '%s')""" % (intCRN, sName, sDept, sTime, sDays, sSemester, intYear, intCredit, sProf))
       elif actions == '4':
           rCRN = int(input('What is the CRN of the course you want to remove: '))
           cur.execute("""DELETE FROM Course WHERE CRN = '%d'""" % rCRN)
       elif actions == '5':
           run = False

    elif User == 'Instructor': #Instructor commands and functions (Adam)
       actions = printOptions(2)
       if actions == '3':
           cur.execute("""SELECT CRN FROM Course WHERE professor = '%s'""" % usersName)
           query_CRN = cur.fetchall()
           cur.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE courseCRN = '%s'""" % query_CRN)
           query_result = cur.fetchall()
           for i in query_result:
               print(i) 
       elif actions == '4':
           run = False
    

    elif User == 'Student': #Student commands and functions(Adam)
       actions = printOptions(3)
       if actions == '3':
           aCRN = int(input('What is the CRN of the course you like to add: '))
           cur.execute("""UPDATE STUDENT SET courseCRN = '%d'""" % aCRN)
       elif actions == '4':
           rCRN = int(input('What is the CRN of the course you want to Drop: '))
           cur.execute("""DELETE FROM STUDENT WHERE courseCRN = '%d'""" % rCRN)
       elif actions == '5':
           run = False


    else: #Error message
       print('Error: Not a user')


# def StudentGetSchedule():
#     print('Where did this code go????????')


# Student.removecourse("Issac Newton", "Newton")

database.commit() #Close and exit db
  
database.close()

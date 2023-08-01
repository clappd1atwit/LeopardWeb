from asyncio.windows_events import NULL
import sqlite3

# Establishing a connection to the SQLite database
connection = sqlite3.connect("assignment3.db")
cursor = connection.cursor()

class User:
    #Set all values to empty/0 when first created
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.ID = 0
    
    def set_first_name(self, newFirstName):
        #set the user's first name
        self.firstName = newFirstName

    def set_last_name(self, newLastName):
        #set the user's last name
        self.lastName = newLastName

    def set_id(self, newID):
        #set the user's ID
        self.ID = newID
    
    def get_ID(self):
        return self.ID

    def print_info(self):
        #print the user's info
        print("Name =", self.firstName, self.lastName, "; ID =", self.ID)

class Student(User):
    def __init__(self, wnumber, email, password, last_name, first_name, catalog_year):
        super().__init__(wnumber, email, password, last_name, first_name)
        self.catalog_year = catalog_year

    def display_student_info(self):
        self.display_user_info()
        print(f"Catalog Year: {self.catalog_year}")

    def display_degree_audit(self):
        print("Displaying new Degree Audit...")

class Professor(User):
    def __init__(self, wnumber, email, password, last_name, first_name):
        super().__init__(wnumber, email, password, last_name, first_name)

    def display_professor_info(self):
        self.display_user_info()

    def display_student_degree_audit(self, student):
        student.display_degree_audit()

class Admin(User):
    def __init__(self, wnumber, email, password, last_name, first_name):
        super().__init__(wnumber, email, password, last_name, first_name)

    def display_admin_info(self):
        self.display_user_info()

def check_login_credentials(email, password):
    database = sqlite3.connect("assignment3.db")
    cur = database.cursor()
    # Check if the email and password match in the LOGINS table
    successful_login = 0
    while(successful_login == 0):
        cur.execute("""SELECT COUNT(*) FROM STUDENT WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if(query_result[0] == 1):
            login_count = 'Student'
            successful_login = 1
        else:
            cur.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE EMAIL = '%s'""" % email)
            query_result = cur.fetchone()
            if(query_result[0] == 1):
                login_count = 'Instructor'
                successful_login = 1
            else:
                cur.execute("""SELECT COUNT(*) FROM ADMIN WHERE EMAIL = '%s'""" % email)
                query_result = cur.fetchone()
                if(query_result[0] == 1):
                    login_count = 'Admin'
                    successful_login = 1
                else: 
                    login_count = 'Error'
                    return False

    if login_count > str(0):
        return True
    else:
        return False
    database.commit()
    database.close()

def creating_user(email, usertype):
    database = sqlite3.connect("assignment3.db")
    cursor = database.cursor()
    query = "SELECT * FROM " + usertype + " WHERE Email = '" + email + "'"
    cursor.execute(query)
    userInfo = cursor.fetchall()

    loggedInUser = User()
    loggedInUser.set_id(userInfo[0][0])
    loggedInUser.set_first_name(userInfo[0][4])
    loggedInUser.set_last_name(userInfo[0][3])
    print("Welcome:")
    loggedInUser.print_info()

    database.commit()
    database.close()

# Closing the cursor and connection
cursor.close()
connection.close()
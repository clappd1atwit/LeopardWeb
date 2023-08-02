from tkinter import *
from Sandbox import *
import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import ImageTk, Image
import sqlite3
import re

page =1
Lastname = ""

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
            
        self.login_frame = LoginFrame(self)
        self.instructor_frame = InstructorFrame(self)
        self.student_frame = StudentFrame(self)
        self.AdminPage = AdminPage(self)
        self.EditStudentDegreeAuditPage = EditStudentDegreeAuditPage(self)
        self.SearchStudentDegreeAuditPage = SearchStudentDegreeAuditPage(self)
        self.profile_frame = ProfileFrame(self)
        
        self.show_login_frame()
        
    def show_login_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()              
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.student_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()
        
    def show_instructor_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.instructor_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.profile_frame.place_forget()
        self.student_frame.place_forget()
        self.EditStudentDegreeAuditPage.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()

    def show_student_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.profile_frame.place_forget()
        self.instructor_frame.place_forget()
        self.EditStudentDegreeAuditPage.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()
        
        self.AdminPage.place_forget()

    def show_Admin_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.AdminPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.EditStudentDegreeAuditPage.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()

    def show_EditStudentDegreeAuditPage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.EditStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()
        self.AdminPage.place_forget()

    def show_SearchStudentDegreeAuditPage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.SearchStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()
        
    def show_profile_frame(self):
        self.login_frame.pack_forget()
        self.instructor_frame.pack_forget()
        self.student_frame.pack_forget()
        self.profile_frame.pack()

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="White")
        
        self.label = tk.Label(self, text="Enter Username & Password", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.username_label = tk.Label(self, text="Username:", font=('Times',12), bg="white")
        self.username_label.place(x=20, y=80)
        self.username_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.username_entry.place(x=20, y=110)
        
        self.password_label = tk.Label(self, text="ID number:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tk.Entry(self, show="*", highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.password_entry.place(x=20, y=170)
        
        self.login_button = tk.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.login_button.place(x=20, y=210)
        
    def login(self):
        global Lastname
        username = self.username_entry.get() 
        password = self.password_entry.get()
        
        DbConnect = sqlite3.connect("assignment3.db")
        db = DbConnect.cursor()

        if check_login_credentials(username, password):
            successful_login = 0
            while(successful_login == 0):
                db.execute("""SELECT COUNT(*) FROM STUDENT WHERE EMAIL = ? and ID = ?""", (username, password))
                query_result = db.fetchone()
                if(query_result[0] == 1):
                    login_count = 'STUDENT'
                    creating_user(username, login_count)
                    self.master.show_student_frame()
                    successful_login = 1
                else:
                    db.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE EMAIL = ? and ID = ?""", (username, password))
                    query_result = db.fetchone()
                    if(query_result[0] == 1):
                        login_count = 'Instructor'
                        db.execute("""SELECT SURNAME FROM INSTRUCTOR WHERE EMAIL = '%s'""" % username)
                        prof_surname = re.sub('\W', '', (str)(db.fetchone()))
                        Lastname = prof_surname
                        self.master.show_instructor_frame()
                        creating_user(username, login_count)
                        successful_login = 1
                    else:
                        db.execute("""SELECT COUNT(*) FROM ADMIN WHERE EMAIL = ? and ID = ?""", (username, password))
                        query_result = db.fetchone()
                        if(query_result[0] == 1):
                            login_count = 'Admin'
                            self.master.show_Admin_frame()
                            creating_user(username, login_count)
                            successful_login = 1
                        else:
                            messagebox.showerror("Invalid user!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")          
        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
    
class AdminPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Welcome Admin", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)
        
        self.Course_button = tk.Button(self, text="Edit Semester Catalog", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.Courses)
        self.Course_button.place(x=70, y=120)
        
        self.Add_button = tk.Button(self, text="Edit School Roster", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.EditStudentDegreeAudit)
        self.Add_button.place(x=70, y=160)

        self.Add_button = tk.Button(self, text="Link Course", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.EditStudentDegreeAudit)
        self.Add_button.place(x=70, y=200)



        
       
    def view_profile(self):
        self.master.show_profile_frame()
    
    def Courses(self):
        print("Add or remove course")
        
    def SearchStudentDegreeAudit(self):
        self.master.show_SearchStudentDegreeAuditPage()

    def EditStudentDegreeAudit(self):
        self.master.show_EditStudentDegreeAuditPage()

    def logout(self):
        self.master.show_login_frame()

class EditStudentDegreeAuditPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tk.Label(self, text="Search Student Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.student_first_name_label = tk.Label(self, text="First Name:", font=('Times',12), bg="white")
        self.student_first_name_label.place(x=20, y=80)
        self.student_first_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.student_first_name_entry.place(x=20, y=110)

        self.student_Last_name_label = tk.Label(self, text="Last Name:", font=('Times',12), bg="white")
        self.student_Last_name_label.place(x=20, y=140)
        self.student_Last_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_Last_name_entry.place(x=20, y=170)

        self.student_Id_number_label = tk.Label(self, text="ID Number:", font=('Times',12), bg="white")
        self.student_Id_number_label.place(x=20, y=200)
        self.student_ID_number_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_ID_number_entry.place(x=20, y=230)
        self.edit_button = tk.Button(self, text="Search Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.EditStudentDegreeAudit)
        self.edit_button.place(x=20, y=270)
  
    def SearchStudentAudit(self):
        print("Print student degree audit")
           
    def view_profile(self):
        self.master.show_profile_frame()
        

    def EditStudentDegreeAudit(self):
        print("Print student degree audit")

    def logout(self):
        self.master.show_login_frame()
        
    def Back(self):
        self.master.show_Admin_frame()

class SearchStudentDegreeAuditPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tk.Label(self, text="Search Student Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.student_first_name_label = tk.Label(self, text="First Name:", font=('Times',12), bg="white")
        self.student_first_name_label.place(x=20, y=80)
        self.student_first_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.student_first_name_entry.place(x=20, y=110)

        self.student_Last_name_label = tk.Label(self, text="Last Name:", font=('Times',12), bg="white")
        self.student_Last_name_label.place(x=20, y=140)
        self.student_Last_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_Last_name_entry.place(x=20, y=170)

        self.student_Id_number_label = tk.Label(self, text="ID Number:", font=('Times',12), bg="white")
        self.student_Id_number_label.place(x=20, y=200)
        self.student_ID_number_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_ID_number_entry.place(x=20, y=230)
        self.search_button = tk.Button(self, text="Search Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchStudentDegreeAudit)
        self.search_button.place(x=20, y=270)
  
    def SearchStudentAudit(self):
        print("Print student degree audit")
           
    def view_profile(self):
        self.master.show_profile_frame()

    def SearchStudentDegreeAudit(self):
        print("Print student degree audit")

    def logout(self):
        self.master.show_login_frame()
        
    def Back(self):
        self.master.show_Admin_frame()

class InstructorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Welcome" + str(Lastname) + "", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)

        self.getcrnList_btn = tk.Button(self, text="Course List", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getCourselist)
        self.getcrnList_btn.place(x=20, y=80)

        self.getRoster_btn = tk.Button(self, text="Roster List", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getRoster)
        self.getRoster_btn.place(x=20, y=150)

        self.getRoster_btn = tk.Button(self, text="Print Courses", font=('Times',12),  bg="white", fg="black", bd=0, command=self.printCourses)
        self.getRoster_btn.place(x=20, y=220)

    def logout(self):
        self.master.show_login_frame()

    def getCourselist(self):
        connection = sqlite3.connect("assignment3.db")
        cur = connection.cursor()
        print('last name is ', str(Lastname))
        cur.execute("""SELECT CRN FROM Course WHERE professor = '%s'""" % Lastname)
        query_CRN = cur.fetchall()
        for i in query_CRN:
            print(i) 
        cur.close()
        connection.close()


    def getRoster(self):
        connection = sqlite3.connect("assignment3.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT CRN FROM Course WHERE professor = '%s'""" % Lastname)
        query_CRN = cursor.fetchall()
        cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE courseCRN = '%s'""" % query_CRN)
        query_result = cursor.fetchall()
        for i in query_result:
            print(i) 
        return query_result
        cursor.close()
        connection.close()

    def printCourses(self):
        connection = sqlite3.connect("assignment3.db")
        cur = connection.cursor()
        cur.execute("""SELECT * FROM Course""")
        query_result = cur.fetchall()
        for i in query_result:
	        print(i)
        cur.close()
        connection.close()

class StudentFrame(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Main Menu", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.getcrnList_btn = tk.Button(self, text="Course List", width=34, font=('Times',12),  bg="white", fg="black", bd=0, command=self.Courses)
        self.getcrnList_btn.place(x=20, y=80)

        self.Search_button = tk.Button(self, text="Add Drop", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.AddDrop)
        self.Search_button.place(x=20, y=150)

        self.Schedule_button = tk.Button(self, text="Add Drop", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.Schedule)
        self.Search_button.place(x=20, y=220)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)
     def Courses(self):
        print("Print self degree audit")
     def AddDrop(self):
        print('addDrop')
     def Schedule(self):
        print('Scedhule')
     def logout(self):
        self.master.show_login_frame()

class ProfileFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Profile Page")
        self.label.pack(pady=10)
        
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=5)
        
    def go_back(self):
        self.master.show_home_frame()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
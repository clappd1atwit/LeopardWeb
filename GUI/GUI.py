from tkinter import *
from winreg import QueryReflectionKey
from Sandbox import *
import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import ImageTk, Image
import sqlite3
import re

page =1
Lastname = ""
Type = ""
database = sqlite3.connect("assignment3.db") 
cur = database.cursor()

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
        self.profile_frame = ProfileFrame(self)
        self.CourseList = CourseList(self)
        self.AddDrop_frame = AddDrop(self)
        
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
        self.instructor_frame = InstructorFrame(self)
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.instructor_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.profile_frame.place_forget()
        self.student_frame.place_forget()
        self.CourseList.place_forget()
        self.DispSchedule_frame.place_forget()

    def show_student_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.DispSchedule_frame = DispSchedule(self)
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.profile_frame.place_forget()
        self.instructor_frame.place_forget()
        self.CourseList.place_forget()
        self.AdminPage.place_forget()
        self.DispSchedule_frame.place_forget()
        self.AddDrop_frame.place_forget()
        self.AddDrop_frame = AddDrop(self)
        

    def show_Admin_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.AdminPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.CourseList.place_forget()

    def show_EditSchoolRosterPage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.EditStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()
        self.AdminPage.place_forget()

    def show_LinkCoursePage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.SearchStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_EditCourseCalalog(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.EditStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.SearchStudentDegreeAuditPage.place_forget()
        self.AdminPage.place_forget()


    def show_DispRoster(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.EditStudentDegreeAuditPage.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_CourseList(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.CourseList.place(x=((width_screen/2)-200),y=((height_screen/2)-380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_DispSchedule(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.DispSchedule_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_EditAddDrop(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.AddDrop_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
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
        global Type
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
                    db.execute("""SELECT SURNAME FROM STUDENT WHERE EMAIL = '%s'""" % username)
                    stnd_surname = re.sub('\W', '', (str)(db.fetchone()))
                    Lastname = stnd_surname
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
        Type = login_count
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
        
        self.EditRoster_button = tk.Button(self, text="Edit School Roster", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.SchoolRoster)
        self.EditRoster_button.place(x=70, y=160)

        self.LnkCourse_button = tk.Button(self, text="Link Course", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.LinkCourse)
        self.LnkCourse_button.place(x=70, y=200)
    
    def Courses(self):
        self.master.show_EditCourseCalalog()
        
    def SchoolRoster(self):
        self.master.show_EditSchoolRosterPage()

    def LinkCourse(self):
        self.master.show_LinkCoursePage()

    def logout(self):
        self.master.show_login_frame()
        
class InstructorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Welcome " + str(Lastname) + "", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)

        self.getcrnList_btn = tk.Button(self, text="Schedule", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getCourselist)
        self.getcrnList_btn.place(x=20, y=80)

        self.getRoster_btn = tk.Button(self, text="Roster List", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getRoster)
        self.getRoster_btn.place(x=20, y=150)

        self.getRoster_btn = tk.Button(self, text="Course Search", font=('Times',12),  bg="white", fg="black", bd=0, command=self.printCourses)
        self.getRoster_btn.place(x=20, y=220)

    def logout(self):
        self.master.show_login_frame()

    def getCourselist(self):
        self.master.show_DispSchedule()

    def getRoster(self):
        self.master.show_DispRoster()

    def printCourses(self):
        self.master.show_CourseList()

class StudentFrame(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Main Menu", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.getcrnList_btn = tk.Button(self, text="Course List", width=34, font=('Times',12),  bg="white", fg="black", bd=0, command=self.Courses)
        self.getcrnList_btn.place(x=20, y=80)

        self.Search_button = tk.Button(self, text="Add Drop", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.AddDrop)
        self.Search_button.place(x=20, y=150)

        self.Schedule_button = tk.Button(self, text="Schedule", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.Schedule)
        self.Schedule_button.place(x=20, y=220)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)
     def Courses(self):
        self.master.show_CourseList()
     def AddDrop(self):
        self.master.show_EditAddDrop()
     def Schedule(self):
        self.master.show_DispSchedule()
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

class CourseList(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=285, y=30)
        
        cur.execute("""SELECT * FROM Course""")
        query_result = cur.fetchall()
        temp = ""
        for i in query_result:
            temp = str(temp) + str(i) + "\n" 
        self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
        self.Course_Label.place(x=15, y=220)
        self.SearchPara_label = tk.Label(self, text="Search:", font=('Times',12), bg="white")
        self.SearchPara_label.place(x=15, y=120)
        self.SearchPara_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.SearchPara_Entry.place(x=75, y=120)
        self.chk_CRN = tk.IntVar()
        self.chk_DEPT = tk.IntVar()
        self.chk_Time = tk.IntVar()
        self.chk_Day = tk.IntVar()
        checkbox = tk.Checkbutton(self, text="CRN", variable=self.chk_CRN, command=self.Search)
        checkbox.place(x=15, y = 70)
        checkbox = tk.Checkbutton(self, text="Department", variable=self.chk_DEPT, command=self.Search)
        checkbox.place(x=80, y = 70)
        checkbox = tk.Checkbutton(self, text="Time", variable=self.chk_Time, command=self.Search)
        checkbox.place(x=185, y = 70)
        checkbox = tk.Checkbutton(self, text="Day", variable=self.chk_Day, command=self.Search)
        checkbox.place(x=250, y = 70)
        

    def Back(self):
        if Type == 'Admin':
            self.master.show_Admin_frame()
        elif Type == 'Instructor':
            self.master.show_instructor_frame()
        else:
            self.master.show_student_frame()

    def Search(self):
        parameter = self.SearchPara_Entry.get()
        if self.chk_CRN.get(): 
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE CRN = '%d'""" % int(parameter))
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + str(i) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_DEPT.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE department = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + str(i) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_Time.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE time = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + str(i) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_Day.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE days = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + str(i) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)

class DispSchedule(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=285, y=30)
        if Type == 'Instructor':
            cur.execute("""SELECT courseCRN FROM 'INSTRUCTOR' WHERE SURNAME = '%s'""" % Lastname)
            query_result = cur.fetchone()
        else:
            cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE SURNAME = '%s'""" % Lastname)
            query_result = cur.fetchone()
            query_int = int(query_result[0])
        cur.execute("""SELECT * FROM Course WHERE CRN = '%d'""" % int(query_int))
        query_result = cur.fetchall()
        self.SCH_label = tk.Label(self, text=str(query_result), font=('Times',12), bg="white")
        self.SCH_label.place(x=15, y=130)


    def Back(self):
        if Type == 'Admin':
            self.master.show_Admin_frame()
        elif Type == 'Instructor':
            self.master.show_instructor_frame()
        else:
            self.master.show_student_frame()

class AddDrop(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=285, y=30)

        self.Add_button = tk.Button(self, text="Add Class", font=('Times',12),  bg="red", fg="white", bd=0, command=self.AddClass)
        self.Add_button.place(x=30, y=80)

        self.Remove_button = tk.Button(self, text="Remove Class", font=('Times',12),  bg="red", fg="white", bd=0, command=self.DelClass)
        self.Remove_button.place(x=130, y=80)

        self.CRN_label = tk.Label(self, text="CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=15, y=130)

        self.CRN_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.CRN_Entry.place(x=75, y=130)

        cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE SURNAME = '%s'""" % Lastname)
        query_result = cur.fetchone()

        self.CRN_label = tk.Label(self, text=f"CRN: {query_result} ", font=('Times',12), bg="white")
        self.CRN_label.place(x=15, y=250)
        
    def Back(self):
        self.master.show_student_frame()

    def AddClass(self):
        cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE SURNAME = '%s'""" % Lastname)
        query_result = cur.fetchone()
        if query_result == "0":
            query_result = str(self.CRN_Entry.get())
        else: query_result = str(query_result[0]) + ", " + str(self.CRN_Entry.get())
        print(query_result)
        cur.execute("""UPDATE STUDENT SET courseCRN = '%s' WHERE SURNAME = '%s'""" % (query_result, Lastname))

    def DelClass(self):
        cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE SURNAME = '%s'""" % Lastname)
        query_result = cur.fetchone()
        query_str = str(query_result[0])
        if query_result == "0":
            exit
        else: 
            query_str = query_str.replace(str(self.CRN_Entry.get()),"")
            query_str = re.sub(r',+,', ' ,', query_str) #No work??

            #This no work too
            if query_str.endswith(','):
                query_str = query_str[:-1]
            cur.execute("""UPDATE STUDENT SET courseCRN = '%s' WHERE SURNAME = '%s'""" % (query_str, Lastname))



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
  
        
database.commit() #Close and exit db
database.close()
from tkinter import *
from winreg import QueryReflectionKey
from Sandbox import *
import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import ImageTk, Image
import sqlite3
import re

page =1
Lastname = "Rawlins"
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
        
        img = Image.open("Images_for_GUI/wit-background.png")
        bgimg = ImageTk.PhotoImage(img)
        
        bg_label = tk.Label(self, image = bgimg)
        bg_label.image = bgimg
        bg_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        
        self.AddDrop_frame = AddDrop(self)
        self.DispSchedule_frame = DispSchedule(self)
        self.login_frame = LoginFrame(self)
        self.instructor_frame = InstructorFrame(self)
        self.student_frame = StudentFrame(self)
        self.AdminPage = AdminPage(self)
        self.profile_frame = ProfileFrame(self)
        self.CourseList = CourseList(self)
        self.AddDrop_frame = AddDrop(self)
        self.Roster_frame = DispRoster(self)
        self.CourseCat_frame = EditCourseCat(self)
        self.StudentRoster_frame = EditStudentRoster(self)
        self.InstructorRoster_frame = EditInstructorRoster(self)
        self.LinkCourse_frame = LinkCourse(self)
        
        
        self.show_login_frame()
        
    def show_login_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()             
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.student_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

        
        
        
    def show_instructor_frame(self):
        self.instructor_frame = InstructorFrame(self)
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.instructor_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.profile_frame.place_forget()
        self.student_frame.place_forget()
        self.CourseList.place_forget()
        self.DispSchedule_frame.place_forget()
        self.Roster_frame.place_forget()

    def show_student_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.profile_frame.place_forget()
        self.instructor_frame.place_forget()
        self.CourseList.place_forget()
        self.AdminPage.place_forget()
        self.AddDrop_frame.place_forget()
        self.DispSchedule_frame.place_forget()
        
        

    def show_Admin_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.AdminPage.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.CourseList.place_forget()
        self.LinkCourse_frame.place_forget()
        self.StudentRoster_frame.place_forget()
        self.InstructorRoster_frame.place_forget()
        self.CourseCat_frame.place_forget()

    def show_EditStudentRosterPage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.StudentRoster_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_EditInstructorRosterPage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.InstructorRoster_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_LinkCoursePage(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.LinkCourse_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_EditCourseCatalog(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.CourseCat_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()


    def show_DispRoster(self):
        self.Roster_frame = DispRoster(self)
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.Roster_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_CourseList(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.CourseList.place(x=((width_screen/2)-350),y=((height_screen/2)-300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_DispSchedule(self):
        self.DispSchedule_frame = DispSchedule(self)
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.DispSchedule_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
        self.instructor_frame.place_forget()
        self.profile_frame.place_forget()
        self.AdminPage.place_forget()

    def show_EditAddDrop(self):
        self.AddDrop_frame = AddDrop(self)
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.AddDrop_frame.place(x=((width_screen/2) -350),y=((height_screen/2) -300))
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
        
        self.login_button = tk.Button(self, text="LOGIN", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
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
        super().__init__(master, width = 600, height = 500, bg="white")
        self.label = tk.Label(self, text="Welcome Admin", width=32, font=('Times',14), bg="white")
        self.label.place(x=140, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=535, y=10)
        
        self.Course_button = tk.Button(self, text="Edit Semester Catalog", bg="white", fg="black", width=25, font=('Times',12), bd=0, command=self.Courses)
        self.Course_button.place(x=190, y=120)
        
        self.EditRoster_button = tk.Button(self, text="Edit Instructor Roster", bg="white", fg="black", width=25, font=('Times',12), bd=0, command=self.InstuctorRoster)
        self.EditRoster_button.place(x=190, y=160)

        self.EditRoster_button = tk.Button(self, text="Edit Student Roster", bg="white", fg="black", width=25, font=('Times',12), bd=0, command=self.StudentRoster)
        self.EditRoster_button.place(x=190, y=200)

        self.LnkCourse_button = tk.Button(self, text="Link Course", bg="white", fg="black", width=25, font=('Times',12), bd=0, command=self.LinkCourse)
        self.LnkCourse_button.place(x=190, y=240)

        self.getRoster_btn = tk.Button(self, text="Course Search", font=('Times',12),  bg="white", fg="black", bd=0, command=self.printCourses)
        self.getRoster_btn.place(x=255, y=280)
    
    def Courses(self):
        self.master.show_EditCourseCatalog()
        
    def InstuctorRoster(self):
        self.master.show_EditInstructorRosterPage()

    def StudentRoster(self):
        self.master.show_EditStudentRosterPage()

    def LinkCourse(self):
        self.master.show_LinkCoursePage()

    def printCourses(self):
        self.master.show_CourseList()

    def logout(self):
        self.master.show_login_frame()
        
class InstructorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.label = tk.Label(self, text="Welcome " + str(Lastname) + "", width=32, font=('Times',14), bg="white")
        self.label.place(x=130, y=80)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=535, y=10)

        self.getcrnList_btn = tk.Button(self, text="Schedule", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getCourselist)
        self.getcrnList_btn.place(x=260, y=180)

        self.getRoster_btn = tk.Button(self, text="Roster List", font=('Times',12),  bg="white", fg="black", bd=0, command=self.getRoster)
        self.getRoster_btn.place(x=255, y=250)

        self.getRoster_btn = tk.Button(self, text="Course Search", font=('Times',12),  bg="white", fg="black", bd=0, command=self.printCourses)
        self.getRoster_btn.place(x=245, y=320)

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
        super().__init__(master, width = 600, height = 500, bg="white")
        self.label = tk.Label(self, text="Main Menu", width=32, font=('Times',14), bg="white")
        self.label.place(x=150, y=90)
        
        self.getcrnList_btn = tk.Button(self, text="Course List", width=34, font=('Times',12),  bg="white", fg="black", bd=0, command=self.Courses)
        self.getcrnList_btn.place(x=150, y=130)

        self.Search_button = tk.Button(self, text="Add Drop", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.AddDrop)
        self.Search_button.place(x=150, y=200)

        self.Schedule_button = tk.Button(self, text="Schedule", width=34, font=('Times',12), bg="white", fg="black", bd=0, command=self.Schedule)
        self.Schedule_button.place(x=150, y=270)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=535, y=10)
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
        super().__init__(master, width = 600, height = 500, bg="white")

        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)
        
        cur.execute("""SELECT * FROM Course""")
        query_result = cur.fetchall()
        temp = ""
        for i in query_result:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
        self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
        self.Course_Label.place(x=30, y=220)
        self.SearchPara_label = tk.Label(self, text="Search:", font=('Times',12), bg="white")
        self.SearchPara_label.place(x=30, y=120)
        self.SearchPara_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.SearchPara_Entry.place(x=90, y=120)
        self.chk_CRN = tk.IntVar()
        self.chk_DEPT = tk.IntVar()
        self.chk_Time = tk.IntVar()
        self.chk_Day = tk.IntVar()
        checkbox = tk.Checkbutton(self, text="CRN", variable=self.chk_CRN, command=self.Search)
        checkbox.place(x=30, y = 70)
        checkbox = tk.Checkbutton(self, text="Department", variable=self.chk_DEPT, command=self.Search)
        checkbox.place(x=95, y = 70)
        checkbox = tk.Checkbutton(self, text="Time", variable=self.chk_Time, command=self.Search)
        checkbox.place(x=200, y = 70)
        checkbox = tk.Checkbutton(self, text="Day", variable=self.chk_Day, command=self.Search)
        checkbox.place(x=265, y = 70)
        

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
            if not isinstance(self.SearchPara_Entry.get(), int):
                parameter = -1
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE CRN = '%d'""" % int(parameter))
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_DEPT.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE department = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_Time.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE time = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_Day.get():
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course WHERE days = '%s'""" % parameter)
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=15, y=220)
        if self.chk_Day.get() == 0 and self.chk_Time.get() == 0 and self.chk_DEPT.get() == 0 and self.chk_CRN.get() == 0:
            self.Course_Label.place_forget()
            cur.execute("""SELECT * FROM Course""")
            query_result = cur.fetchall()
            temp = ""
            for i in query_result:
                temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
            self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
            self.Course_Label.place(x=30, y=220)

class DispSchedule(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        
        self.Course_Label = tk.Label(self, text = 'Schedule:', font=('Times', 18),  bg="white", fg="black", bd=0)
        self.Course_Label.place(x=30, y=90)
        
        cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE ID = 10001""")
        query_result = cur.fetchone()
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)
        if Type == 'Instructor':
            cur.execute("""SELECT courseCRN FROM 'INSTRUCTOR' WHERE SURNAME = '%s'""" % Lastname)
            query_result = cur.fetchone()
        elif Type == 'STUDENT':
            cur.execute("""SELECT courseCRN FROM 'STUDENT' WHERE SURNAME = '%s'""" % Lastname)
            query_result = cur.fetchone()
        query_int = int(query_result[0])
        cur.execute("""SELECT * FROM Course WHERE CRN = '%d'""" % int(query_int))
        query_result = cur.fetchall()
        self.SCH_label = tk.Label(self, text=re.sub(r"[\'()]", '', str(query_result)), font=('Times',12), bg="white")
        self.SCH_label.place(x=30, y=130)


    def Back(self):
        if Type == 'Admin':
            self.master.show_Admin_frame()
        elif Type == 'Instructor':
            self.master.show_instructor_frame()
        else:
            self.master.show_student_frame()

class AddDrop(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)

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

        self.CRN_label = tk.Label(self, text=f"CRN: " + re.sub(r"[\'()]", '', str(query_result)), font=('Times',12), bg="white")
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
            query_str = re.sub(', ,', ', ', query_str) #No work??

            #This no work too
            if query_str.endswith(', '):
                query_str = query_str[:-2]
            cur.execute("""UPDATE STUDENT SET courseCRN = '%s' WHERE SURNAME = '%s'""" % (query_str, Lastname))

class DispRoster(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)
        self.RSTR_title = tk.Label(self, text='Roster:', font=('Times',18), bg="white")
        self.RSTR_title.place(x=50, y=90)
        cur.execute("""SELECT CRN FROM Course WHERE professor = '%s'""" % Lastname)
        query_CRN = cur.fetchone()
        string_CRN = str(query_CRN[0])
        cur.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE courseCRN = '%s'""" % string_CRN)
        query_result = cur.fetchall()
        self.RSTR_label = tk.Label(self, text=re.sub(r"[\'()]", '', str(query_result)), font=('Times',12), bg="white")
        self.RSTR_label.place(x=50, y=130)

    def Back(self):
        self.master.show_instructor_frame()

class EditCourseCat(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)
        
        self.Cls_label = tk.Label(self, text="Add a Class:", font=('Times',16), bg="white")
        self.Cls_label.place(x=50, y=40)

        self.CRN_label = tk.Label(self, text="CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=50, y=70)
        self.CRN_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.CRN_Entry.place(x=150, y=70)

        self.Name_label = tk.Label(self, text="Name:", font=('Times',12), bg="white")
        self.Name_label.place(x=50, y=100)
        self.Name_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Name_Entry.place(x=150, y=100)

        self.Dept_label = tk.Label(self, text="Department:", font=('Times',12), bg="white")
        self.Dept_label.place(x=50, y=130)
        self.Dept_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Dept_Entry.place(x=150, y=130)

        self.Time_label = tk.Label(self, text="Time:", font=('Times',12), bg="white")
        self.Time_label.place(x=50, y=160)
        self.Time_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Time_Entry.place(x=150, y=160)

        self.Day_label = tk.Label(self, text="Days:", font=('Times',12), bg="white")
        self.Day_label.place(x=50, y=190)
        self.Day_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Day_Entry.place(x=150, y=190)

        self.Semsester_label = tk.Label(self, text="Semsester:", font=('Times',12), bg="white")
        self.Semsester_label.place(x=50, y=220)
        self.Semsester_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Semsester_Entry.place(x=150, y=220)

        self.Year_label = tk.Label(self, text="Year:", font=('Times',12), bg="white")
        self.Year_label.place(x=50, y=250)
        self.Year_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Year_Entry.place(x=150, y=250)

        self.Credits_label = tk.Label(self, text="Credits:", font=('Times',12), bg="white")
        self.Credits_label.place(x=50, y=280)
        self.Credits_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Credits_Entry.place(x=150, y=280)

        self.Professor_label = tk.Label(self, text="Professor:", font=('Times',12), bg="white")
        self.Professor_label.place(x=50, y=310)
        self.Professor_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Professor_Entry.place(x=150, y=310)

        self.Add_button = tk.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.Add_button.place(x=50, y=350)


        self.Remove_Course_label = tk.Label(self, text="Remove Course:", font=('Times',16), bg="white")
        self.Remove_Course_label.place(x=50, y=400)
        self.Remove_label = tk.Label(self, text="Course CRN:", font=('Times',12), bg="white")
        self.Remove_label.place(x=50, y=430)
        self.Remove_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Remove_Entry.place(x=150, y=430)

        self.Remove_button = tk.Button(self, text="Remove Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveCourse)
        self.Remove_button.place(x=50, y=460)

     def AddCourse(self):
        intCRN =int(self.CRN_Entry.get())
        sName = self.Name_Entry.get()
        sDept = self.Dept_Entry.get()
        sTime = self.Time_Entry.get() 
        sDays = self.Day_Entry.get() 
        sSemester = self.Semsester_Entry.get() 
        intYear = int(self.Year_Entry.get()) 
        intCredit = int(self.Credits_Entry.get()) 
        sProf = self.Professor_Entry.get()
        cur.execute("""INSERT INTO Course VALUES('%d','%s', '%s','%s', '%s', '%s', '%d', '%d', '%s')""" % (intCRN, sName, sDept, sTime, sDays, sSemester, intYear, intCredit, sProf))

     def RemoveCourse(self):
         cur.execute("""DELETE FROM Course WHERE CRN = '%d'""" % int(self.Remove_Entry.get()))
        
     def Back(self):
        self.master.show_Admin_frame()

class EditStudentRoster(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        temp = ""
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)

        cur.execute("""SELECT ID, NAME, SURNAME FROM STUDENT""")
        student_name = cur.fetchall()

        for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
        self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
        self.Course_Label.place(x=390, y=70)

        self.STD_label = tk.Label(self, text="Add a Student:", font=('Times',16), bg="white")
        self.STD_label.place(x=30, y=40)

        self.ID_label = tk.Label(self, text="Stduent ID:", font=('Times',12), bg="white")
        self.ID_label.place(x=30, y=70)
        self.ID_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.ID_Entry.place(x=130, y=70)

        self.Name_label = tk.Label(self, text="Name:", font=('Times',12), bg="white")
        self.Name_label.place(x=30, y=100)
        self.Name_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Name_Entry.place(x=130, y=100)

        self.Surname_label = tk.Label(self, text="Surname:", font=('Times',12), bg="white")
        self.Surname_label.place(x=30, y=130)
        self.Surname_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Surname_Entry.place(x=130, y=130)

        self.Year_label = tk.Label(self, text="Grad Year:", font=('Times',12), bg="white")
        self.Year_label.place(x=30, y=160)
        self.Year_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Year_Entry.place(x=130, y=160)

        self.Major_label = tk.Label(self, text="Major:", font=('Times',12), bg="white")
        self.Major_label.place(x=30, y=190)
        self.Major_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Major_Entry.place(x=130, y=190)

        self.Email_label = tk.Label(self, text="Email:", font=('Times',12), bg="white")
        self.Email_label.place(x=30, y=220)
        self.Email_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Email_Entry.place(x=130, y=220)

        self.AddSTD_button = tk.Button(self, text="Add Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddStudent)
        self.AddSTD_button.place(x=30, y=250)

        self.STD_label = tk.Label(self, text="Remove Student:", font=('Times',16), bg="white")
        self.STD_label.place(x=30, y=290)
        
        self.rmID_label = tk.Label(self, text="ID:", font=('Times',12), bg="white")
        self.rmID_label.place(x=30, y=320)
        self.rmID_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.rmID_Entry.place(x=130, y=320)

        self.rmSTD_button = tk.Button(self, text="Remove Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveStudent)
        self.rmSTD_button.place(x=30, y=350)

     def Back(self):
        self.master.show_Admin_frame()

     def AddStudent(self):
         self.Course_Label.place_forget()
         intID = int(self.ID_Entry.get())
         cur.execute("""INSERT INTO STUDENT VALUES('%d','%s', '%s', '%d', '%s', '%s', '%s')""" % (intID, self.Name_Entry.get(), self.Surname_Entry.get(), int(self.Year_Entry.get()), self.Major_Entry.get(), self.Email_Entry.get(), NULL))
         cur.execute("""SELECT ID, NAME, SURNAME FROM STUDENT""")
         student_name = cur.fetchall()
         temp = ""
         for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
         self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
         self.Course_Label.place(x=535, y=30)
     
     def RemoveStudent(self):
         self.Course_Label.place_forget()
         intID = int(self.rmID_Entry.get())
         cur.execute("""DELETE FROM STUDENT WHERE ID = '%d'""" % intID)
         cur.execute("""SELECT ID, NAME, SURNAME FROM STUDENT""")
         student_name = cur.fetchall()
         temp = ""
         for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
         self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
         self.Course_Label.place(x=535, y=30)

class EditInstructorRoster(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)

        cur.execute("""SELECT ID, NAME, SURNAME FROM INSTRUCTOR""")
        student_name = cur.fetchall()
        temp = ""
        for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
        self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
        self.Course_Label.place(x=390, y=70)

        self.STD_label = tk.Label(self, text="Add a Instructor:", font=('Times',16), bg="white")
        self.STD_label.place(x=30, y=40)

        self.ID_label = tk.Label(self, text="Instructor ID:", font=('Times',12), bg="white")
        self.ID_label.place(x=30, y=70)
        self.ID_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.ID_Entry.place(x=130, y=70)

        self.Name_label = tk.Label(self, text="Name:", font=('Times',12), bg="white")
        self.Name_label.place(x=30, y=100)
        self.Name_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Name_Entry.place(x=130, y=100)

        self.Surname_label = tk.Label(self, text="Surname:", font=('Times',12), bg="white")
        self.Surname_label.place(x=30, y=130)
        self.Surname_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Surname_Entry.place(x=130, y=130)

        self.Title_label = tk.Label(self, text="Title:", font=('Times',12), bg="white")
        self.Title_label.place(x=30, y=160)
        self.Title_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Title_Entry.place(x=130, y=160)

        self.Year_label = tk.Label(self, text="Year Hired:", font=('Times',12), bg="white")
        self.Year_label.place(x=30, y=190)
        self.Year_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Year_Entry.place(x=130, y=190)

        self.Dept_label = tk.Label(self, text="Department:", font=('Times',12), bg="white")
        self.Dept_label.place(x=30, y=220)
        self.Dept_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Dept_Entry.place(x=130, y=220)

        self.Email_label = tk.Label(self, text="Email:", font=('Times',12), bg="white")
        self.Email_label.place(x=30, y=250)
        self.Email_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.Email_Entry.place(x=130, y=250)

        self.AddIns_button = tk.Button(self, text="Add Instructor", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddInstructor)
        self.AddIns_button.place(x=30, y=280)

        self.Ins_label = tk.Label(self, text="Remove Instructor:", font=('Times',16), bg="white")
        self.Ins_label.place(x=30, y=320)
        
        self.rmCRN_label = tk.Label(self, text="ID:", font=('Times',12), bg="white")
        self.rmCRN_label.place(x=30, y=350)
        self.rmCRN_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=24,font=('Times',14), bg="white")
        self.rmCRN_Entry.place(x=130, y=350)

        self.rmSTD_button = tk.Button(self, text="Remove Instructor", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveInstructor)
        self.rmSTD_button.place(x=30, y=380)

     def Back(self):
        self.master.show_Admin_frame()

     def AddInstructor(self):
         self.Course_Label.place_forget()
         intID = int(self.ID_Entry.get())
         cur.execute("""INSERT INTO INSTRUCTOR VALUES('%d','%s', '%s', '%s', '%d', '%s', '%s')""" % (intID, self.Name_Entry.get(), self.Surname_Entry.get(), self.Title_Entry.get(), int(self.Year_Entry.get()), self.Dept_Entry.get(), self.Email_Entry.get()))
         cur.execute("""SELECT ID, NAME, SURNAME FROM INSTRUCTOR""")
         student_name = cur.fetchall()
         temp = ""
         for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
         self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
         self.Course_Label.place(x=390, y=70)
     
     def RemoveInstructor(self):
         self.Course_Label.place_forget()
         intID = int(self.rmCRN_Entry.get())
         cur.execute("""DELETE FROM INSTRUCTOR WHERE ID = '%d'""" % intID)
         cur.execute("""SELECT ID, NAME, SURNAME FROM INSTRUCTOR""")
         student_name = cur.fetchall()
         temp = ""
         for i in student_name:
            temp = str(temp) + re.sub(r"[\'()]", '', str(i)) + "\n" 
         self.Course_Label = tk.Label(self, text = str(temp), font=('Times',12),  bg="white", fg="black", bd=0)
         self.Course_Label.place(x=390, y=70)

class LinkCourse(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 600, height = 500, bg="white")
        self.Back_button = tk.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.Back_button.place(x=535, y=30)

        self.Cls_label = tk.Label(self, text="Update Professor:", font=('Times',18), bg="white")
        self.Cls_label.place(x=50, y=100)

        self.CRN_label = tk.Label(self, text="Course CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=50, y=140)
        self.CRN_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.CRN_Entry.place(x=150, y=140)

        self.Name_label = tk.Label(self, text="Professor:", font=('Times',12), bg="white")
        self.Name_label.place(x=50, y=170)
        self.Name_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.Name_Entry.place(x=150, y=170)

        self.Change_button = tk.Button(self, text="Commit Change", font=('Times',12),  bg="black", fg="white", bd=0, command=self.ChangeProf)
        self.Change_button.place(x=50, y=210)

        self.Cls_label = tk.Label(self, text="Remove Professor:", font=('Times',18), bg="white")
        self.Cls_label.place(x=50, y=250)

        self.rmCRN_label = tk.Label(self, text="Course CRN:", font=('Times',12), bg="white")
        self.rmCRN_label.place(x=50, y=280)
        self.rmCRN_Entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.rmCRN_Entry.place(x=150, y=280)

        self.Change_button = tk.Button(self, text="Commit Change", font=('Times',12),  bg="black", fg="white", bd=0, command=self.ChangeProf)
        self.Change_button.place(x=50, y=310)

     def ChangeProf(self):
         iCRN = int(self.CRN_Entry.get())
         ProfName = self.Name_Entry.get()
         cur.execute("""UPDATE Course SET professor = '%s' WHERE CRN = '%d'""" % (iCRN, ProfName))
     def RemoveProf(self):
         iCRN = int(self.rmCRN_Entry.get())
         cur.execute("""UPDATE Course SET professor = NULL WHERE CRN = '%d'""" % iCRN)
     def Back(self):
        self.master.show_Admin_frame()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
  
        
database.commit() #Close and exit db
database.close()
from tkinter import *
from Sandbox import *
import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import ImageTk, Image
import sqlite3

page =1

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
        
        self.password_label = tk.Label(self, text="Password:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tk.Entry(self, show="*", highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.password_entry.place(x=20, y=170)
        
        self.login_button = tk.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.login_button.place(x=20, y=210)
        
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()
        
        DbConnect = sqlite3.connect("DegreeViz-2R3.db")
        db = DbConnect.cursor()

        if check_login_credentials(username, password):
            for column in db.execute("SELECT * FROM Users WHERE Email = ? and Password = ? ", (username, password)):
                usertype= column[5];
                if  usertype== 'S':
                    creating_user(username)
                    self.master.show_student_frame()
                elif usertype == 'P':                  
                    self.master.show_instructor_frame()
                    creating_user(username)
                elif usertype == 'A':
                    self.master.show_Admin_frame()
                    creating_user(username)
                 
                else:
                    messagebox.showerror("Invalid user!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")          
        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
    
class AdminPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Admin Frame", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)
        
        self.Search_button = tk.Button(self, text="Search Students Degree Audit", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.SearchStudentDegreeAudit)
        self.Search_button.place(x=70, y=120)
        
        self.Add_button = tk.Button(self, text="Edit Students Degree Audit", bg="black", fg="white", width=25, font=('Times',12), bd=0, command=self.EditStudentDegreeAudit)
        self.Add_button.place(x=70, y=160)
        
       
    def view_profile(self):
        self.master.show_profile_frame()
        
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
        self.label = tk.Label(self, text="Search Student Degree Audit", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)

        self.student_first_name_label = tk.Label(self, text="First Name:", font=('Times',12), bg="white")
        self.student_first_name_label.place(x=20, y=80)
        self.student_first_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.student_first_name_entry.place(x=20, y=110)

        self.student_Last_name_label = tk.Label(self, text="Last Name:", font=('Times',12), bg="white")
        self.student_Last_name_label.place(x=20, y=140)
        self.student_Last_name_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_Last_name_entry.place(x=20, y=170)
        
        self.logout_button = tk.Button(self, text="Search", width=34, font=('Times',12), bg="black", fg="white", bd=0, command=self.SearchStudentAudit)
        self.logout_button.place(x=20, y=230)
        
    def SearchStudentAudit(self):
        print("Print student degree audit")

    def logout(self):
        self.master.show_login_frame()

class StudentFrame(tk.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tk.Label(self, text="Main Menu", width=32, font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.Search_button = tk.Button(self, text="Print Degree Audit", width=34, font=('Times',12), bg="black", fg="white", bd=0)
        self.Search_button.place(x=20, y=100)

        self.logout_button = tk.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=10)
     def PrintStudentAudit(self):
        print("Print self degree audit")
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
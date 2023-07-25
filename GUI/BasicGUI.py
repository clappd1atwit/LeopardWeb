import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Database connection
database = sqlite3.connect("assignment3.db")
cur = database.cursor()
# ... Your existing code for creating the Course table and other database operations ...

class StudentGUI(tk.Tk):
    def __init__(self, email):
        super().__init__()
        self.title("Student GUI")
        self.geometry("400x300")

        self.email = email

        # Student welcome label
        self.welcome_label = tk.Label(self, text="Welcome Student!", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)

        # Student info label
        self.student_info_label = tk.Label(self, text="Student Information", font=("Helvetica", 12))
        self.student_info_label.pack(pady=5)

        # Display student name and ID
        self.display_student_info(email)

        # Course search label
        self.course_search_label = tk.Label(self, text="Course Search", font=("Helvetica", 12))
        self.course_search_label.pack(pady=5)

        # Course search entry and button
        self.course_search_entry = tk.Entry(self)
        self.course_search_entry.pack(pady=5)
        self.search_button = tk.Button(self, text="Search", command=self.search_course)
        self.search_button.pack(pady=5)

        # Course search result listbox
        self.search_result_listbox = tk.Listbox(self, height=5, width=40)
        self.search_result_listbox.pack(pady=10)

    def display_student_info(self, email):
        cur.execute("""SELECT NAME, SURNAME, ID FROM STUDENT WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if query_result:
            student_name = f"{query_result[0]} {query_result[1]}"
            student_id = query_result[2]
            self.student_info_label.config(text=f"Student Information\nName: {student_name}\nID: {student_id}")
        else:
            messagebox.showerror("Error", "Failed to retrieve student information.")

    def search_course(self):
        search_term = self.course_search_entry.get().strip()
        if not search_term:
            messagebox.showwarning("Search Error", "Please enter a search term.")
            return

        # Search the course based on the search term (CRN or department, for example)
        cur.execute("""SELECT * FROM Course WHERE CRN = ? OR department = ?""", (search_term, search_term))
        query_result = cur.fetchall()

        if query_result:
            self.search_result_listbox.delete(0, tk.END)
            for course in query_result:
                self.search_result_listbox.insert(tk.END, course)
        else:
            messagebox.showinfo("Search Result", "No matching courses found.")

class CourseManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Course Management System")
        self.geometry("400x200")

        # Create login frame
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(padx=50, pady=30)

        # Login label and entry
        self.email_label = tk.Label(self.login_frame, text="Email:")
        self.email_label.grid(row=0, column=0)
        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1)

        # Login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=1, column=0, columnspan=2, pady=10)

    def login(self):
        email = self.email_entry.get().strip().lower()
        user = self.check_user_type(email)

        if user == 'Student':
            # Call the student GUI
            self.show_student_frame(email)
        elif user == 'Instructor':
            # Call the instructor GUI
            self.show_instructor_frame(email)
        elif user == 'Admin':
            # Call the admin GUI
            self.show_admin_frame(email)
        else:
            messagebox.showerror("Login Failed", "Invalid email, try again.")

    def check_user_type(self, email):
        cur.execute("""SELECT COUNT(*) FROM STUDENT WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if query_result[0] == 1:
            return 'Student'

        cur.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if query_result[0] == 1:
            return 'Instructor'

        cur.execute("""SELECT COUNT(*) FROM ADMIN WHERE EMAIL = '%s'""" % email)
        query_result = cur.fetchone()
        if query_result[0] == 1:
            return 'Admin'

        return 'Unknown'

    def show_student_frame(self, email):
        self.destroy()  # Close the login frame

        # Create the student frame
        self.student_frame = StudentGUI(email)

        # Add a button to log out
        self.logout_button = tk.Button(self.student_frame, text="Log Out", command=self.logout)
        self.logout_button.pack(pady=10)

        self.student_frame.mainloop()

    def logout(self):
        # Destroy the student frame and show the login frame again
        self.student_frame.destroy()
        self.show_login_frame()

    def show_login_frame(self):
        # Create and show the login frame again
        self.login_frame.pack(padx=50, pady=30)

# Main function to run the application
if __name__ == "__main__":
    app = CourseManagementApp()
    app.mainloop()

# Close and commit the database
database.commit()
database.close()


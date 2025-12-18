import tkinter as tk
from tkinter import ttk, messagebox
from models.employee import Employee

class AddEmployeeDialog(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.db = db
        self.title("Add Employee")
        self.geometry("400x520")
        self.create_widgets()

    def create_widgets(self):
        self.entries = {}

        fields = [
            ("Employee ID", "employee_id"),
            ("First Name", "first_name"),
            ("Last Name", "last_name"),
            ("Email", "email"),
            ("Pay Type (Hourly/Salary)", "pay_type"),
            ("Status", "status"),
            ("DOB", "dob"),
            ("Gender", "gender"),
            ("Medical (Single/Family)", "medical"),
            ("Dependents", "dependents"),
            ("Department", "department"),
            ("Job Title", "job_title"),
            ("Base Salary / Rate", "base_salary"),
            ("Password", "password"),
        ]

        for label, key in fields:
            ttk.Label(self, text=label).pack(anchor="w", padx=10)
            entry = ttk.Entry(self)
            entry.pack(fill="x", padx=10, pady=2)
            self.entries[key] = entry

        ttk.Button(self, text="Save", command=self.save).pack(pady=15)

    def save(self):
        try:
            emp = Employee(
                employee_id=self.entries["employee_id"].get(),
                first_name=self.entries["first_name"].get(),
                last_name=self.entries["last_name"].get(),
                email=self.entries["email"].get(),
                pay_type=self.entries["pay_type"].get(),
                status=self.entries["status"].get(),
                dob=self.entries["dob"].get(),
                gender=self.entries["gender"].get(),
                medical=self.entries["medical"].get(),
                dependents=int(self.entries["dependents"].get()),
                department=self.entries["department"].get(),
                job_title=self.entries["job_title"].get(),
                base_salary=float(self.entries["base_salary"].get()),
                password=self.entries["password"].get()
            )

            self.db.add_employee(emp)
            messagebox.showinfo("Success", "Employee added.")
            self.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))

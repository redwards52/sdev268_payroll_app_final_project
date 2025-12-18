import tkinter as tk
from tkinter import ttk, messagebox
from models.employee import Employee

class EditEmployeeDialog(tk.Toplevel):
    def __init__(self, parent, db, employee_id):
        super().__init__(parent)
        self.db = db
        self.employee = next(e for e in db.list_employees() if e.employee_id == employee_id)

        self.title("Edit Employee")
        self.geometry("400x520")
        self.create_widgets()
        self.populate()

    def create_widgets(self):
        self.entries = {}

        fields = [
            ("First Name", "first_name"),
            ("Last Name", "last_name"),
            ("Email", "email"),
            ("Pay Type", "pay_type"),
            ("Status", "status"),
            ("DOB", "dob"),
            ("Gender", "gender"),
            ("Medical", "medical"),
            ("Dependents", "dependents"),
            ("Department", "department"),
            ("Job Title", "job_title"),
            ("Base Salary", "base_salary"),
        ]

        for label, key in fields:
            ttk.Label(self, text=label).pack(anchor="w", padx=10)
            entry = ttk.Entry(self)
            entry.pack(fill="x", padx=10, pady=2)
            self.entries[key] = entry

        ttk.Button(self, text="Update", command=self.update).pack(pady=15)

    def populate(self):
        for key, entry in self.entries.items():
            entry.insert(0, getattr(self.employee, key))

    def update(self):
        try:
            updated = Employee(
                employee_id=self.employee.employee_id,
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
                password=self.employee.password
            )

            self.db.update_employee(updated)
            messagebox.showinfo("Updated", "Employee updated.")
            self.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))
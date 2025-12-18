# gui/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from gui.add_employee_dialog import AddEmployeeDialog
from gui.edit_employee_dialog import EditEmployeeDialog
from gui.error_dialog import ErrorDialog
from models.database import Database


class MainWindow(tk.Tk):
    def __init__(self, admin=True):
        super().__init__()
        self.title("ABC Company Payroll System")
        self.geometry("900x500")
        self.db = Database()    # Connect to your CSV/DB
        self.create_widgets()
        self.populate_employee_list()


    def create_widgets(self):
        # Employee Treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Email", "Pay Type", "Status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)


        ctrl = ttk.Frame(self)
        ctrl.pack(fill="x")

        ttk.Button(ctrl, text="Add", command=self.add_employee).pack(side="left", padx=5)
        ttk.Button(ctrl, text="Edit", command=self.edit_employee).pack(side="left", padx=5)
        ttk.Button(ctrl, text="Delete", command=self.delete_employee).pack(side="left", padx=5)
        ttk.Button(ctrl, text="Search", command=self.search_employee).pack(side="left", padx=5)
        ttk.Button(ctrl, text="Export Report", command=self.export_report).pack(side="right", padx=5)

    def populate_employee_list(self):
        for r in self.tree.get_children():
            self.tree.delete(r)

        for e in self.db.list_employees():
            self.tree.insert("", "end", values=(
                e.employee_id,
                f"{e.first_name} {e.last_name}",
                e.email,
                e.pay_type,
                e.status
            ))

    def add_employee(self):
        AddEmployeeDialog(self, self.db)
        self.wait_window()
        self.populate_employee_list()

    def edit_employee(self):
        sel = self.tree.focus()
        if not sel:
            ErrorDialog(self, "Select an employee.")
            return
        eid = self.tree.item(sel)["values"][0]
        EditEmployeeDialog(self, self.db, eid)
        self.wait_window()
        self.populate_employee_list()

    def delete_employee(self):
        sel = self.tree.focus()
        if not sel:
            return
        eid = self.tree.item(sel)["values"][0]
        if messagebox.askyesno("Confirm", "Delete employee?"):
            self.db.delete_employee(eid)
            self.populate_employee_list()

    def search_employee(self):
        from tkinter.simpledialog import askstring
        term = askstring("Search", "Enter ID or email:")
        if not term:
            return
        results = self.db.search_employee(term)
        if not results:
            ErrorDialog(self, "Employee not found.")
        else:
            e = results[0]
            messagebox.showinfo("Found", f"{e.first_name} {e.last_name}")

    def export_report(self):
        import csv
        with open("data/payroll_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Email", "Pay Type", "Status"])
            for e in self.db.list_employees():
                writer.writerow([
                    e.employee_id,
                    f"{e.first_name} {e.last_name}",
                    e.email,
                    e.pay_type,
                    e.status
                ])
        messagebox.showinfo("Exported", "Payroll report generated.")
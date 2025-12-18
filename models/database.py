# models/database.py
from models.employee import Employee
from utils.load_export import load_employees, export_employees

class Database:
    def __init__(self):
        self.employees = load_employees()


    def add_employee(self, employee: Employee):
        if any(e.employee_id == employee.employee_id for e in self.employees):
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees.append(employee)
        export_employees(self.employees)


    def list_employees(self):
        return self.employees


    def delete_employee(self, employee_id):
        self.employees = [e for e in self.employees if e.employee_id != employee_id]
        export_employees(self.employees)

    def search_employee(self, term):
        return [e for e in self.employees if term in e.employee_id or term in e.email]
    

    def update_employee(self, updated_employee: Employee):
        for i, e in enumerate(self.employees):
            if e.employee_id == updated_employee.employee_id:
                self.employees[i] = updated_employee
                export_employees(self.employees)
                return
        raise ValueError("Employee not found")
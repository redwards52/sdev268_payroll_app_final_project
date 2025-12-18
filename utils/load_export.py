#models/load_export
import csv
from models.employee import Employee
from config import EMPLOYEE_CSV_PATH

EMPLOYEE_CSV_PATH = "data/employees.csv"

def load_employees():
    employees = []
    try:
        with open(EMPLOYEE_CSV_PATH, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                emp = Employee(
                    employee_id=row["employee_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    pay_type=row["pay_type"],
                    status=row["status"],
                    dob=row["dob"],
                    gender=row["gender"],
                    medical=row["medical"],
                    dependents=int(row["dependents"]),
                    department=row["department"],
                    job_title=row["job_title"],
                    base_salary=float(row["base_salary"]),
                    password=["password"]
                )
                employees.append(emp)
    except FileNotFoundError:
        pass
    return employees

def export_employees(employees):
    with open(EMPLOYEE_CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["employee_id","first_name","last_name","email","pay_type","status",
                      "dob","gender","medical","dependents","department","job_title","base_salary"
                      ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for e in employees:
            writer.writerow(e.__dict__)
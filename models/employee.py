# models/employee.py
from dataclasses import dataclass

@dataclass
class Employee:
    employee_id: str
    first_name: str
    last_name: str
    email: str
    pay_type: str
    status: str
    dob: str
    gender: str
    medical: str
    dependents: int
    department: str
    job_title: str
    base_salary: float
    password: str
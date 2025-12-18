# config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMPLOYEE_CSV_PATH = os.path.join(BASE_DIR, "data", "employees.csv")


"""
#CSV file path
EMPLOYEE_CSV_PATH = "data/employees.csv"


# Admin credentials
ADMIN_ID = "HR0001"
ADMIN_PASSWORD_HASH = "your_hashed_password_here"  # hash passwords using MD5, bcrypt, etc.
"""

# Payroll settings
DEFAULT_HOURLY_PAY = 20.0
STANDARD_WORK_HOURS = 40

# Tax rates
STATE_TAX = 0.0315
FEDERAL_TAX = 0.0765
SOCIAL_SECURITY = 0.062
MEDICARE = 0.0145

# Medical and dependent allowances
MEDICAL_SINGLE = 50
MEDICAL_FAMILY = 100
DEPENDENT_STIPEND = 45


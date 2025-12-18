# models/validation.py
import re
from datetime import datetime, date

def validate_email(email: str) -> bool:
    regex = r'^\S+@\S+\.\S+$'
    return re.match(regex, email) is not None

def validate_dob(dob: str) -> bool:
    birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age >= 18
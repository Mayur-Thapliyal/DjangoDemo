import re
def validate_phone_number(number):
    # Regular expression to match Indian phone numbers
    # Indian phone numbers can be in the format +91xxxxxxxxxx or 91xxxxxxxxxx
    # where x is a digit, but after +91, the next digit cannot be 0, 1, 2, 3, 4, 5, or 6
    pattern = re.compile(r'^(\+91|91)[789]\d{9}$')
    
    if pattern.match(number):
        return True
    else:
        raise ValueError("Invalid Phone Number")

def validate_email(email):
    # Regular expression to validate email addresses
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    if pattern.match(email):
        return True
    else:
        raise ValueError("Invalid Email")
def validate_password(password):
    # Regular expression to validate password
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]{8,20}$')
    
    if pattern.match(password):
        return True
    else:
        raise ValueError("Invalid Password")
        
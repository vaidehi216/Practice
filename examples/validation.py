# import re

# # Function to validate name
# def validate_name(name):
#     return name.isalpha() and len(name) >= 3

# # Function to validate age
# def validate_age(age):
#     if age.isdigit():
#         age = int(age)
#         return 1 <= age <= 120
#     return False

# # Function to validate email
# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(pattern, email) is not None

# # Function to validate phone number (10 digits only)
# def validate_phone(phone):
#     return phone.isdigit() and len(phone) == 10

# # Main Program
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# email = input("Enter your email: ")
# phone = input("Enter your phone number: ")

# if validate_name(name):
#     print("Valid Name")
# else:
#     print("Invalid Name (must be only letters, at least 3 characters)")

# if validate_age(age):
#     print("Valid Age")
# else:
#     print("Invalid Age (must be between 1 and 120)")

# if validate_email(email):
#     print("Valid Email")
# else:
#     print("Invalid Email format")

# if validate_phone(phone):
#     print("Valid Phone Number")
# else:
#     print("Invalid Phone (must be 10 digits)") 



# import re
# email_condition = "^[a-z]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$"
# user_email = input("Enter your email: ")
# if re.search(email_condition, user_email):
#     print("Valid Email")    
# else:
#     print("Invalid Email format") 



import re
pwd = input("Enter your password: ")
if len(pwd) < 8:
    print("Password must be at least 8 characters long.")
elif not re.search("[a-z]", pwd):
    print("Password must contain at least one lowercase letter.")
elif not re.search("[A-Z]", pwd):
    print("Password must contain at least one uppercase letter.")
elif not re.search("[0-9]", pwd):
    print("Password must contain at least one digit.")
elif not re.search("[!@#$%^&*(),.?\":{}|<>]", pwd):
    print("Password must contain at least one special character.")
else:
    print("Password is valid.")


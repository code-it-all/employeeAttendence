
print("Welcome to Password Strength Checker")
print('Minimum length (e.g., 8 characters')
print('Mix of uppercase and lowercase letters.')
print('Inclusion of numbers and special characters.')

password = input("Enter Password: ")
import re
if len(password) >= 8:
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
        if re.search(r'[!@#$%^&*]', password):
            print("Strong Password")
    else:
        print('Medium Password')
else:
    print('Weak Password')



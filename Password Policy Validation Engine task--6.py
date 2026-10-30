password = ""
while len(password) < 6:
    password = input("Enter a password (at least 6 characters): ")
if len(password) >= 6:
    print("Password accepted")
attended = int(input("Enter the number of classes attended:"))
classes = 45
if attended >=46:
    print("Not a valid input")
if attended in range(0,46):
    attendance = attended / classes * 100
    if attendance >= 75:
        print("Eligible")
    else:
        print("Attendance is too low")

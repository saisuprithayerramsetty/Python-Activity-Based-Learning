attendance = int(input("Enter the attendance:"))
lab_done = True
fees_paid = True
if attendance < 75: print("Attendance requirement not met")
elif not lab_done: print("Complete lab work")
elif not fees_paid: print("Pay outstanding fees")
else: print("Eligible for examination")

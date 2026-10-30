marks = [70, 65, 80]
average = sum(marks) / len(marks)
if average >= 75:
    result = "Distinction"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"
print(result)

prepared = [100, 120, 90]
leftover = [10, 30, 5]
for i in range(len(prepared)):
    waste = leftover[i] / prepared[i] * 100
    if waste > 20: print("High waste on day", i + 1)

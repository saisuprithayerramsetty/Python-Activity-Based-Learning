level = 80
for change in [30, -20, -100]:
    level += change
    if level > 100: level = 100
    elif level < 0: level = 0
    print("Water level:", level)

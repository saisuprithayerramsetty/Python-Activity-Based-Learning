key = "ABC"
answers = "ADC"
correct = 0
for i in range(len(key)):
    if answers[i] == key[i]: correct += 1
print("Correct:", correct)
print("Incorrect:", len(key) - correct)

words = ["good", "bad", "good"]
score = 0
for word in words:
    if word == "good": score += 1
    elif word == "bad": score -= 1
print("Feedback score:", score)

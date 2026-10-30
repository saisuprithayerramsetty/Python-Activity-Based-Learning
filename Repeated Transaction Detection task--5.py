amounts = [100, 250, 100]
seen = []
for amount in amounts:
    if amount in seen: print("Duplicate:", amount)
    else: seen.append(amount)

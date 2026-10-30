balance = 500
transactions = [200, -100, -700]
i = 0
while i < len(transactions):
    amount = transactions[i]; i += 1
    if amount >= 0: balance += amount
    elif balance + amount >= 0: balance += amount
    else: print("Withdrawal rejected")
print("Balance:", balance)

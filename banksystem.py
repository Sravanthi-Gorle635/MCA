balance = 0

while True:
    print("1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        amt = float(input("Amount: "))
        balance += amt

    elif ch == "2":
        amt = float(input("Amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")

    elif ch == "3":
        print("Balance:", balance)

    elif ch == "4":
        break


pin = int(input("Enter the PIN: "))

attempt = 0
balance = 10000

while attempt < 3:
    if pin == 1234:
        print("Welcome to the ATM!")
        while True:
            print("1. Balance Enquiry")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your balance is", balance)

            elif choice == 2:
                withdraw_amount = int(input("Enter the withdrawal amount: "))

                if withdraw_amount > 0:
                    if withdraw_amount <= balance:
                        balance = balance - withdraw_amount
                        print(f"Withdrawn amount is {withdraw_amount} and remaining balance is {balance}")
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid amount")

            elif choice == 3:
                deposit_amount = int(input("Enter the deposit amount: "))
                if deposit_amount > 0:
                    balance = balance + deposit_amount
                    print(f"You have successfully deposited {deposit_amount}! Your new balance is {balance}")
                else:
                    print("Invalid amount")

            elif choice == 4:
                print("You have exited the ATM. Thank you!")
                break
        break
    else:
        print("Invalid PIN")
        attempt = attempt + 1
        if attempt == 3:
            print(f"Your account is blocked. You have entered the wrong PIN {attempt} times. Try again after 24 hours.")
            break
        pin = int(input("Enter the PIN again: "))

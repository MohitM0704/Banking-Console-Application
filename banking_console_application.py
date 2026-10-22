

balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: ₹", balance)

while True:

    # Step 1: Display Main Menu
    print("\n========== BANKING MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Step 2: Check Balance
    if choice == "1":
        print("Current Balance: ₹", balance)

    # Step 3: Deposit Money
    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Invalid amount! Deposit must be greater than zero.")
        else:
            balance = balance + amount
            print("Deposit successful.")
            print("Updated Balance: ₹", balance)

    # Step 4: Withdraw Money
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than zero.")
        elif amount > balance:
            print("Transaction failed: Insufficient balance.")
            print("Current Balance: ₹", balance)
        else:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated Balance: ₹", balance)

    # Step 5: Exit
    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    # Step 6: Handle Invalid Menu Choices
    else:
        print("Invalid choice! Please select an option from 1 to 4.")
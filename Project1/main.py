from finance import Ledger, Income, Expense

ledger = Ledger()

def menu():
    print("\n--- Personal Finance Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Summary")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")
    try:
        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter category: ")
            ledger.add_transaction(Income(amount, category))
            print("Income added successfully.")
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            ledger.add_transaction(Expense(-amount, category))  # Negative for expense
            print("Expense added successfully.")
        elif choice == "3":
            ledger.view_transactions()
        elif choice == "4":
            ledger.summary()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Invalid input. Amount must be a number.")

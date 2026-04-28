balance = 1000
transactions = []

def check_balance():
    print(f"\nYour current balance is: ₹{balance}")

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print("Amount deposited successfully!")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("Please collect your cash.")

def show_statement():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)

def menu():
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            show_statement()
        elif choice == '5':
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice!")

# Run program
menu()
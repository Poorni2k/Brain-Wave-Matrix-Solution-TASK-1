# ATM Interface using Python

# Dummy data for a single user
user_pin = "1234"
user_balance = 10000  # Initial balance
attempts = 0

def check_pin():
    global attempts
    while attempts < 3:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == user_pin:
            print("✅ Login Successful\n")
            return True
        else:
            attempts += 1
            print(f"❌ Incorrect PIN. Attempts left: {3 - attempts}")
    print("🚫 Too many incorrect attempts. Account locked.")
    return False

def show_menu():
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("======================")

def check_balance():
    print(f"💰 Your current balance is: ₹{user_balance}")

def deposit():
    global user_balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        user_balance += amount
        print(f"✅ ₹{amount} deposited successfully.")
        check_balance()
    else:
        print("❌ Invalid amount.")

def withdraw():
    global user_balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("❌ Invalid amount.")
    elif amount > user_balance:
        print("❌ Insufficient balance.")
    else:
        user_balance -= amount
        print(f"✅ ₹{amount} withdrawn successfully.")
        check_balance()

# Main program
if check_pin():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("🔒 Thank you for using the ATM. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

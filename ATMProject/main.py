from ATMProject import bank

user_active = True
user = bank.bank()
while user_active:
    print("\n1. Checking the balance of your account ")
    print("2. To deposit money in your account ")
    print("3. To withdraw money from your account ")
    print("4. To exit")
    user_input = input("Select the function you want to perform: ")
    if user_input == "1":
        user.balance()
    elif user_input == "2":
        value = int(input("Enter the amount you want to enter : "))
        user.deposit(value)
    elif user_input == "3":
        withdraw_amount = int(input("Enter the amount you want to withdrew: "))
        user.withdraw(withdraw_amount)
    elif user_input == "4":
        user_active = False
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")


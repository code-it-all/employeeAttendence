
class bank:
    def __init__(self):
        self.amount = 1000

    def deposit(self, amount):
        if self.amount >= 0:
            self.amount += amount
            print(f"You have deposited {amount}, current balance is {self.amount}")
        else:
            print("Invalid amount entered")
        return "Amount added"

    def withdraw(self, withdraw_value):

        if self.amount > withdraw_value:
            self.amount -= withdraw_value
            print(f"You have withdrawn {withdraw_value}, current balance is {self.amount}")
        else:
            print("Your account doesn't have enough money")

    def balance(self):
        print(f"You have {self.amount} in your account")
        return self.amount

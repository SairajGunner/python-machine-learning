class BankAccount:
    customer_name = None
    balance = 0

    def __init__(self, name) -> None:
        self.customer_name = name

    def show_balance(self):
        print(self.balance)

    def deposit_money(self, amount):
        self.balance += amount
        print("{} credited to your account. Account balance is {}.".format(amount, self.balance))

    def withdraw_money(self, amount):
        self.balance -= amount
        print("{} withdraw from your account. Account balance is {}.".format(amount, self.balance))

from bank_account import BankAccount

name = input("Enter the name of the customer.")
bank_account = BankAccount(name)

bank_account.deposit_money(10000)
bank_account.show_balance()
bank_account.withdraw_money(5000)
bank_account.show_balance()
bank_account.deposit_money(10000)
bank_account.show_balance()

from bank_account import BankAccount

name = input("Enter the name of the customer.\n")
bank_account = BankAccount(name)

def show_menu():
    print("What do you wish to do? Type the number to choose the option.\n1. View Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    user_menu_option = int(input())

    match user_menu_option:
        case 1:
            bank_account.show_balance()
            show_menu()
        case 2:
            amount = input("What is the amount you want to deposit?")
            bank_account.deposit_money(int(amount))
            show_menu()
        case 3:
            amount = input("What is the amount you want to withdraw?")
            bank_account.withdraw_money(int(amount))
            show_menu()
        case 4:
            print("Thank you for using our services today.")
        case _:
            show_menu()

show_menu()
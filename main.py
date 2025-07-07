from models import User
from accounts import SavingsAccount, CheckingAccount
from bank import Bank
from file_utils import save_user_to_file, load_users_from_file


def main():
    bank = Bank.get_instance()
    users_data = load_users_from_file()

    print(" Welcome To Vaha Bank Simulator ")
    choice = input("Do you want to (1) Register or (2) Login? ")

    if choice == "1":
        name = input("Enter your name: ")
        pin = input("Create a 4-digit PIN: ")

        if name in users_data:
            print("User already exists. Please login.")
            return

        user = User(name, pin)
        bank.add_user(user)
        save_user_to_file(name, pin)

        savings = SavingsAccount(user, balance=1000.0)
        checking = CheckingAccount(user, balance=500.0)

    elif choice == "2":
        name = input("Enter your name: ")
        pin = input("Enter your 4-digit PIN: ")

        if name not in users_data or users_data[name] != pin:
            print("Login failed. Please check your credentials.")
            return

        user = User(name, pin)
        bank.add_user(user)

        savings = SavingsAccount(user, balance=1000.0)
        checking = CheckingAccount(user, balance=500.0)

    else:
        print("Invalid choice.")
        return

    savings.deposit(200)
    checking.withdraw(100)

    print(f"\n User Info: \n {user}")
    print(f"Savings Balance: {savings.get_balance()}")
    print(f"Checking Balance: {checking.get_balance()}")

    savings.show_transactions()
    checking.show_transactions()


if __name__ == "__main__":
    main()

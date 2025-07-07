from models import User
from accounts import SavingsAccount, CheckingAccount
from bank import Bank
from transaction import Transaction


def main():
    bank = Bank.get_instance()
    
    print(" Welcome To Vaha Bank Simulator ")
    name = input("Enter your name: ")
    pin = input("Enter a 4-digit PIN: ")
    
    user = User(name, pin)
    bank.add_user(user)
    
    savings = SavingsAccount(user, balance=1000.0)
    checking = CheckingAccount(user, balance=500.0)
    
    savings.deposit(200)
    checking.withdraw(100)
    
    print(f"\n User Info: \n {user}")
    print(f"Savings Balance: {savings.get_balance()}")
    print(f"Checking Balance: {checking.get_balance()}")
    
    savings.show_transactions()
    checking.show_transactions()

    
if __name__ == "__main__":
    main()

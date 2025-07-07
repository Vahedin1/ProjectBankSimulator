from transaction import Transaction
from models import Account


class SavingsAccount(Account):

    def __init__(self, owner, balance=0.0, interest_rate=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.record_transactions(amount, "deposit")
            
    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.record_transactions(amount, "withdraw")
        else:
            print("Insufficient funds.")
        
    def apply_interest(self):
        interest = self.balance + self.interest_rate
        self.deposit(interest)

        
class CheckingAccount(Account):

    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
        self.overdraft_limit = overdraft_limit
        super().__init__(owner, balance)
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.record_transactions(amount, "deposit")
            
    def withdraw(self, amount: float):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount  
            self.record_transactions(amount, "withdraw")
        else:
            print("Overdraft limit exceeded.")
        

from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from transaction import Transaction


class User:

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def __str__(self):
        return f"User (name={self.name}, accounts={[a.account_number for a in self.accounts]})"

    
class Account(ABC):

    def __init__(self, owner: User, balance: float=0.0):
        self.account_number = str(uuid.uuid4())[:8]
        self.owner = owner
        self.balance = balance
        self.transactions = []
        owner.add_account(self)
        
    @abstractmethod
    def deposit(self, amount: float):
        pass
    
    @abstractmethod
    def withdraw(self, amount: float):
        pass
    
    def get_balance(self):
        return self.balance
    
    def record_transaction(self, amount, transaction_type):
        transaction = Transaction(amount, transaction_type)
        self.transactions.append(transaction)

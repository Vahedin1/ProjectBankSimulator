from datetime import datetime


class Transaction:

    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.type = transaction_type  
        self.date = datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type.title():<8} | Amount: {self.amount:.2f}"


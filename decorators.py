def log_transaction(func):

    def wrapper(self, amount):
        print(f"Transaction: {func.__name__.capitalize()} | Amount: {amount}")
        result = func(self, amount)
        print(f"New balance: {self.get_balance()}")
        return result

    return wrapper

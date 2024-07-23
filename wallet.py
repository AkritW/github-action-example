class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def add_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val

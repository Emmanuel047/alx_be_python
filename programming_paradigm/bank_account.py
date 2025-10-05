class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        amount += self.account_balance

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
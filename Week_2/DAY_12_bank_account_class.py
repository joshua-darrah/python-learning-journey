class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: {self.balance}")

# Creating an object (instance) of the class
account1 = BankAccount("Joshua", 100)

# Using the methods
account1.check_balance()
account1.deposit(50)
account1.withdraw(30)
account1.withdraw(200)  # should show an error

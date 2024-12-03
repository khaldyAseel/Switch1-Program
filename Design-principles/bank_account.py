# Acoording to the design principles encapsulation
# we can do 

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    # Getter method for balance
    def get_balance(self):
        return self.balance

    # Setter method for balance
    def set_balance(self, amount):
        self.balance = amount
    
    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount

# Example usage
account = BankAccount(100)
print(f"Initial Balance: {account.get_balance()}")

# Direct modification of the balance (even negative values can be set)
account.set_balance(-50)
print(f"Modified Balance: {account.get_balance()}")

account.deposit(-50)
print(f"Modified Balance after deposit: {account.get_balance()}")


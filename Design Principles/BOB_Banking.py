from abc import ABC, abstractmethod
import random

# Encapsulation: We encapsulate data and methods related to user and account management.
# Inheritance: We create subclasses to represent different types of accounts (Savings and Checking).
# Polymorphism: We use common method names to interact with different types of accounts.

# Base class for an account
class BOB_banking(ABC):
    def __init__(self, account_number, balance, user):
        self.account_number = account_number
        self.balance = balance
        self.user = user
        
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def display_balance(self):
        pass
    
# Subclass for a savings account
class SavingsAccount(BOB_banking):
    def __init__(self, account_number, balance, user, interest_rate):
        super().__init__(account_number, balance, user)
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")
            
    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")
        
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate #intrest rate for savings account = 2.25%
        
#Subclass for student account
class StudentAccount(BOB_banking):
    def __init__(self, account_number, balance, user,intrest_rate, min_balance):
        super().__init__(account_number, balance, user)
        self.intrest_rate = intrest_rate
        self.min_balance = min_balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount, min_balance):
        if amount <= self.balance - min_balance:
            self.balance -= amount
        else:
            print("Transaction cannont be processed due to insufficient funds")
        
# Subclass for a checking account
class CheckingAccount(BOB_banking):
    def __init__(self, account_number, balance, user, overdraft_limit):
        super().__init__(account_number, balance, user)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Transaction declined: Overdraft limit exceeded.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")
        
#User class
class User:
    def __init__(self, name, aadhar_number):
        self.name = name
        self.aadhar_number = aadhar_number
        self.accounts = []
        
    def create_account(self, account_type, initial_balance):
        account_number = random.randint(1000,9999)
        if account_type == "savings":
            account = SavingsAccount(account_number, initial_balance, self, 0.0225)
        elif account_type == "student":
            account = StudentAccount(account_number, initial_balance, self, 1000)
        elif account_type == "checking":
            account = CheckingAccount(account_number, initial_balance, self, 5.02)
        else:
            print("Invalid account type")
            return None
        self.accounts.append(account)
        return account
    
    def validate_aadhar(self, aadhar_number):
        if len(aadhar_number) == 12 and aadhar_number.isdigit():
            return True
        else:
            print("Invalid AAdhar number. Please provide proper number")
            
# Example usage:
user1 = User("Alice", "123-456-789")
user2 = User("Bob", "987-654-321")

account1 = user1.create_account("savings", 1000)
account2 = user2.create_account("checking", 500)

account1.deposit(200)
account1.apply_interest()
account1.display_balance()

account2.withdraw(700)
account2.display_balance()

account2.withdraw(1200)  # Attempt to exceed overdraft limit
account2.display_balance()

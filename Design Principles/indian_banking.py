from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        self.customers = []

    def create_customer(self, name, aadhar_number):
        customer = Customer(name, aadhar_number)
        self.customers.append(customer)
        return customer

class Customer:
    def __init__(self, name, aadhar_number):
        self.name = name
        self.aadhar_number = aadhar_number
        self.accounts = []

class Account(ABC):
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer):
        super().__init__(account_number, balance, customer)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

class CurrentAccount(Account):
    def __init__(self, account_number, balance, customer):
        super().__init__(account_number, balance, customer)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class FixedDeposit(Account):
    def __init__(self, account_number, balance, customer, maturity_period):
        super().__init__(account_number, balance, customer)
        self.maturity_period = maturity_period

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.maturity_period <= 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Fixed deposits cannot be withdrawn before maturity.")

# Usage
bank = Bank()

customer1 = bank.create_customer("Alice", "123456789")
customer2 = bank.create_customer("Bob", "987654321")

savings_account = SavingsAccount(account_number=1, balance=1000, customer=customer1)
current_account = CurrentAccount(account_number=2, balance=2000, customer=customer2)
#fd_account = FixedDeposit(account_number=3, balance=5000, customer=customer1, maturity_period=365)

savings_account.deposit(500)
current_account.withdraw(300)
#fd_account.deposit(1000)
#fd_account.withdraw(4000)

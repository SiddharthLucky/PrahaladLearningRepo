import sqlite3

# Database connection
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                balance REAL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                amount REAL,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

# Customer model
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Transaction model
class Transaction:
    def __init__(self, customer_id, amount):
        self.customer_id = customer_id
        self.amount = amount

# Customer repository
class CustomerRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, customer):
        self.db.cursor.execute("INSERT INTO customers (name, balance) VALUES (?, ?)",
                              (customer.name, customer.balance))
        self.db.conn.commit()

    def select_all(self):
        self.db.cursor.execute("SELECT * FROM customers")
        return self.db.cursor.fetchall()

# Transaction repository
class TransactionRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, transaction):
        self.db.cursor.execute("INSERT INTO transactions (customer_id, amount) VALUES (?, ?)",
                              (transaction.customer_id, transaction.amount))
        self.db.conn.commit()

    def get_transactions_for_customer(self, customer_id):
        self.db.cursor.execute("SELECT t.id, t.amount FROM transactions t INNER JOIN customers c ON t.customer_id = c.id WHERE c.id = ?", (customer_id,))
        return self.db.cursor.fetchall()

# Main program
if __name__ == "__main__":
    db = Database("bank_1.db")
    db.create_tables()

    customer1 = Customer("Alice", 3000.0)
    customer2 = Customer("Bob", 1500.0)

    customer_repo = CustomerRepository(db)
    transaction_repo = TransactionRepository(db)

    # Insert customers
    customer_repo.insert(customer1)
    customer_repo.insert(customer2)

    # Insert transactions
    transaction_repo.insert(Transaction(1, 200.0))
    transaction_repo.insert(Transaction(2, -100.0))
    transaction_repo.insert(Transaction(1, -50.0))

    # Get transactions for a specific customer
    customer_id = 1
    transactions = transaction_repo.get_transactions_for_customer(customer_id)

    print("Transactions for Customer 1:")
    for transaction in transactions:
        print(f"Transaction ID: {transaction[0]}, Amount: {transaction[1]}")

    db.close()

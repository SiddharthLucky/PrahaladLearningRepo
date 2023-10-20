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
        self.conn.commit()

    def close(self):
        self.conn.close()

# Customer model
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

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

# Main program
if __name__ == "__main__":
    db = Database("bank.db")
    db.create_tables()

    customer1 = Customer("Alice", 2000.0)
    customer2 = Customer("Bob", 1500.0)

    customer_repo = CustomerRepository(db)

    # Insert customers
    customer_repo.insert(customer1)
    customer_repo.insert(customer2)

    # Select all customers
    customers = customer_repo.select_all()

    print("Customers:")
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]}, Balance: {customer[2]}")

    db.close()

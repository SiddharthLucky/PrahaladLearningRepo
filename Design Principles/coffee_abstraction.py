# Import the 'ABC' (Abstract Base Class) and 'abstractmethod' tools from the 'abc' module.
from abc import ABC, abstractmethod

# Define an abstract base class called 'CoffeeShopItem' for items at a coffee shop.
class CoffeeShopItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def prepare(self):
        pass

# Define concrete classes for specific items.

# Concrete class 'Coffee' inherits from the 'CoffeeShopItem' abstract class.
class Coffee(CoffeeShopItem):
    def prepare(self):
        return f"Preparing a cup of {self.name}."

# Concrete class 'Pastry' inherits from the 'CoffeeShopItem' abstract class.
class Pastry(CoffeeShopItem):
    def prepare(self):
        return f"Getting a {self.name} pastry ready."

# Concrete class 'Sandwich' inherits from the 'CoffeeShopItem' abstract class.
class Sandwich(CoffeeShopItem):
    def prepare(self):
        return f"Making a {self.name} sandwich."

# Sample JSON data representing the coffee shop menu.
menu_data = [
    {
        "type": "coffee",
        "name": "Espresso",
        "price": 2.5
    },
    {
        "type": "pastry",
        "name": "Croissant",
        "price": 3.0
    },
    {
        "type": "sandwich",
        "name": "Turkey Club",
        "price": 7.0
    }
]

# Create a list of coffee shop items based on the JSON data, using abstraction.
coffee_shop_items = [CoffeeShopItem(item["name"], item["price"]) for item in menu_data]

# Example usage: Loop through the list of coffee shop items.
for item in coffee_shop_items:
    print(f"Order: {item.name} - ${item.price:.2f}")
    print(item.prepare())
    print()

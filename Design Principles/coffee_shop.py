# Create a list of coffee shop items based on the JSON data, using concrete classes.
from coffee_abstraction import *

coffee_shop_items = [Coffee(item["name"], item["price"]) if item["type"] == "coffee" else
                     Pastry(item["name"], item["price"]) if item["type"] == "pastry" else
                     Sandwich(item["name"], item["price"]) for item in menu_data]

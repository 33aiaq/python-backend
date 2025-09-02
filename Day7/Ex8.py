class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the order.")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed {name} from the order.")
                return
        print(f"Item '{name}' not found in the order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        if not self.items:
            return "Your order is empty."
        order_details = "\n".join(item.display() for item in self.items)
        total = self.calculate_total()
        return f"Order Items:\n{order_details}\nTotal: ${total:.2f}"


menu_item1 = MenuItem("Spring Rolls", 5.99, "Appetizer")
menu_item2 = MenuItem("Grilled Chicken", 12.49, "Main Course")
menu_item3 = MenuItem("Cheesecake", 6.50, "Dessert")

order = Order()
order.add_item(menu_item1)
order.add_item(menu_item2)
order.add_item(menu_item3)

print(order.display_order())

order.remove_item("Grilled Chicken")
print("\nAfter removal:")
print(order.display_order())

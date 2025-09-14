from database import cursor, conn
from exceptions import OutOfStockError

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock  # private attribute

    def __str__(self):
        return f"{self.name} - ${self.price} - Stock: {self._stock}"

    def reduce_stock(self, quantity):
        if quantity > self._stock:
            raise OutOfStockError(f"{self.name} only has {self._stock} left.")
        self._stock -= quantity
        cursor.execute("UPDATE products SET stock = ? WHERE name = ?", (self._stock, self.name))
        conn.commit()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        product.reduce_stock(quantity)
        self.items.append((product, quantity))

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        for product, qty in self.items:
            print(f"{product} x {qty} = ${product.price * qty}")

    def total(self):
        return sum(product.price * qty for product, qty in self.items)

class User:
    def __init__(self, name):
        self.name = name
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        self.id = cursor.lastrowid
        self.cart = ShoppingCart()

    def checkout(self):
        total_amount = self.cart.total()
        if total_amount == 0:
            print("Cart is empty. Cannot checkout.")
            return
        cursor.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", (self.id, total_amount))
        conn.commit()
        self.cart.items.clear()
        print(f"{self.name} successfully checked out. Total: ${total_amount}")

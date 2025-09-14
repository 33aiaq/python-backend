# models.py
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self._stock})"

    def get_stock(self):
        return self._stock

    def set_stock(self, qty):
        self._stock = qty


class User:
    def __init__(self, username):
        self.username = username
        self.cart = ShoppingCart()

    def checkout(self):
        total = self.cart.total()
        self.cart.clear_cart()
        return total


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if quantity > product.get_stock():
            raise Exception("Not enough stock available")
        self.items.append((product, quantity))

    def view_cart(self):
        return self.items

    def total(self):
        return sum(product.price * qty for product, qty in self.items)

    def clear_cart(self):
        self.items = []

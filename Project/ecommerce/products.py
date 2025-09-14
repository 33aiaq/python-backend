from models import Product

class Book(Product):
    def __init__(self, name, price, stock, author):
        super().__init__(name, price, stock)
        self.author = author

    def __str__(self):
        return f"Book: {self.name} by {self.author} - ${self.price} - Stock: {self._stock}"

class Electronics(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand

    def __str__(self):
        return f"Electronics: {self.name} ({self.brand}) - ${self.price} - Stock: {self._stock}"

class Clothing(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def __str__(self):
        return f"Clothing: {self.name} (Size: {self.size}) - ${self.price} - Stock: {self._stock}"

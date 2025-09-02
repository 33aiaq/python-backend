class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price 
        self.quantity = quantity

    def apply_discount(self, percent):
        self.__price *= (1 - percent / 100)

    def restock(self, amount):
        self.quantity += amount

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        return None

    def __call__(self):
        print(f"{self.name} ({self.product_id}) - Price: ${self.__price:.2f}, Qty: {self.quantity}")


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        super().apply_discount(percent)
        if self.get_price() < 5:
            self._Product__price = 5


ebook = DigitalProduct("D001", "Python eBook", 50, 10, 20)
laptop = PhysicalProduct("P001", "Laptop", 500, 5, 2.5)

ebook.apply_discount(25)
laptop.apply_discount(98)

ebook.restock(5)
laptop.restock(2)

ebook2 = DigitalProduct("D001", "Python eBook", 50, 3, 20)
combined_ebook = ebook + ebook2
print(f"Combined Quantity: {combined_ebook.quantity}")  # 18

ebook()
laptop()

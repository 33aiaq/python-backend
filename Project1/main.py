from models import User
from products import Book, Electronics

# Create sample products
book1 = Book("Python 101", 30, 10, "John Doe")
book2 = Book("Data Science Handbook", 40, 5, "Jane Smith")
laptop = Electronics("Laptop", 1200, 3, "Dell")
phone = Electronics("Smartphone", 800, 7, "Samsung")

# Create a user
user = User("Amer")

# Add products to cart
user.cart.add_product(book1, 2)
user.cart.add_product(laptop, 1)
user.cart.add_product(phone, 1)

# View cart
print("Shopping Cart:")
user.cart.view_cart()

# Total price
print("Total:", user.cart.total())

# Checkout
user.checkout()

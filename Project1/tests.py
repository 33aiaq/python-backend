from models import Product, ShoppingCart
import pytest
from exceptions import OutOfStockError

def test_add_to_cart():
    p = Product("Test", 10, 5)
    cart = ShoppingCart()
    cart.add_product(p, 3)
    assert cart.total() == 30
    with pytest.raises(OutOfStockError):
        cart.add_product(p, 10)

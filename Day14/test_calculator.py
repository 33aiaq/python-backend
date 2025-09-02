import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5
    assert calculator.multiply(0, 10) == 0

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-10, 2) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

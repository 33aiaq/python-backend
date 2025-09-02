from functools import wraps

def positive_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"All arguments must be positive numbers. Invalid: {arg}")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"All arguments must be positive numbers. Invalid: {key}={value}")
        return func(*args, **kwargs)
    return wrapper

@positive_args
def add(a, b):
    return a + b

@positive_args
def multiply(a, b, c=1):
    return a * b * c

print(add(5, 10))
print(multiply(2, 3, c=4))

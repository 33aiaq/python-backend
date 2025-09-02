from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@call_counter
def greet(name):
    print(f"Hello, {name}!")
    
@call_counter
def add(a, b):
    return a + b

greet("Noor")
greet("Ahmad")
print(add(3, 4))
print(add(10, 20))

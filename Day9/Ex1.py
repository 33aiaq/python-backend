import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

class FileWriter:
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if self.file:
            self.file.close()
        return False

@measure_time
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    result = slow_function(5_000_000)
    with FileWriter("output.txt") as f:
        f.write(f"Result = {result}\n")
        f.write("This line was written using a context manager.\n")
    print("Program finished. Check 'output.txt'.")


def eecution_time(fund):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fund(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{elapsed}")
        return result
    return wrapper


@eecution_time
def test():
    print("This is a test function.")

test()
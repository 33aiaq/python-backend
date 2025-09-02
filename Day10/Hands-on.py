class EvenNumbersIterator:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            current = self.num
            self.num += 2
            return current
        else:
            raise StopIteration

def even_numbers_generator(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

evens_iterator = EvenNumbersIterator(10)
evens_generator = even_numbers_generator(10)

print("Using Custom Iterator:")
for n in evens_iterator:
    print(n, end=" ")
print("\nUsing Generator:")
for n in evens_generator:
    print(n, end=" ")

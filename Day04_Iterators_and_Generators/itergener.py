# Day 4 – Iterators & Generators

# 1. Custom Iterator Class
class Squares:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.limit:
            result = self.num ** 2
            self.num += 1
            return result
        else:
            raise StopIteration

print("Squares Iterator:")
for val in Squares(5):
    print(val)

print("-" * 40)

# 2. Generator Function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci Generator:")
for num in fibonacci(10):
    print(num)

print("-" * 40)

# 3. Infinite Generator (be careful!)
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

counter = infinite_counter()
print("Infinite Counter (first 5 numbers):")
for _ in range(5):
    print(next(counter))


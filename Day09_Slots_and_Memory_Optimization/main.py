# Day 9 – __slots__ and Memory Optimization
import sys
import time

# --- Normal class ---
class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


# --- Slotted class ---
class PersonSlots:
    __slots__ = ("name", "age", "city")

    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


if __name__ == "__main__":
    # Memory comparison
    p1 = Person("Alice", 25, "NY")
    p2 = PersonSlots("Bob", 30, "LA")

    print("Normal class size:", sys.getsizeof(p1.__dict__))
    print("Slotted class size:", sys.getsizeof(p2))

    # Performance test: setting attributes many times
    ITERATIONS = 1_000_000

    p = Person("Test", 20, "City")
    ps = PersonSlots("Test", 20, "City")

    start = time.time()
    for _ in range(ITERATIONS):
        p.age = 21
    print("Normal class time:", time.time() - start)

    start = time.time()
    for _ in range(ITERATIONS):
        ps.age = 21
    print("Slotted class time:", time.time() - start)

    # Demonstrating limitation
    try:
        p1.new_attr = "hello"
        print("Added new_attr to normal class:", p1.new_attr)
    except AttributeError:
        print("Normal class cannot add attr")

    try:
        p2.new_attr = "hello"
    except AttributeError as e:
        print("Slotted class restriction:", e)


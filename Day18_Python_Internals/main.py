import sys
import gc
import dis


# === Object Identity & Reference Counting ===
def object_identity_demo():
    a = [1, 2, 3]
    b = a  # same reference
    c = [1, 2, 3]  # new object with same content

    print("=== Object Identity Demo ===")
    print("id(a):", id(a))
    print("id(b):", id(b), "-> b is a")
    print("id(c):", id(c), "-> c is different")

    print("a is b:", a is b)
    print("a == c:", a == c)
    print("a is c:", a is c)

    print("\nReference count for 'a':", sys.getrefcount(a))


# === Garbage Collection Demo ===
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print(f"[GC] Node {self.name} deleted")


def gc_demo():
    print("\n=== Garbage Collection Demo ===")
    a = Node("A")
    b = Node("B")

    # Create a circular reference
    a.ref = b
    b.ref = a

    del a
    del b

    print("Forcing garbage collection...")
    gc.collect()


# === Bytecode Inspection Demo ===
def square(x):
    return x * x


def bytecode_demo():
    print("\n=== Bytecode Inspection ===")
    dis.dis(square)


if __name__ == "__main__":
    object_identity_demo()
    gc_demo()
    bytecode_demo()

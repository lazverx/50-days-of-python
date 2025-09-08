# Day 10 – Enums and Attributes
from enum import Enum, IntEnum, auto

# --- 1. Basic Enum ---
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# --- 2. Auto values ---
class Status(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    DONE = auto()


# --- 3. IntEnum example ---
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


# --- 4. Class attributes vs Instance attributes ---
class Dog:
    species = "Canis familiaris"  # class attribute (shared)

    def __init__(self, name: str, age: int):
        self.name = name      # instance attribute
        self.age = age        # instance attribute


if __name__ == "__main__":
    # Enums
    print("Color.RED:", Color.RED)
    print("Color.RED name:", Color.RED.name)
    print("Color.RED value:", Color.RED.value)

    # Iterating enums
    print("All Status:")
    for s in Status:
        print("-", s)

    # Comparison
    print("Priority check:", Priority.HIGH > Priority.MEDIUM)

    # Dictionary mapping with enums
    severity_messages = {
        Priority.LOW: "Take it easy",
        Priority.MEDIUM: "Be careful",
        Priority.HIGH: "Act immediately!",
    }
    print("Message for HIGH:", severity_messages[Priority.HIGH])

    # Class vs Instance attributes
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Milo", 5)

    print("Dog1:", dog1.name, dog1.age, dog1.species)
    print("Dog2:", dog2.name, dog2.age, dog2.species)

    Dog.species = "Canis lupus familiaris"  # change class attr
    print("Dog1 species after change:", dog1.species)
    print("Dog2 species after change:", dog2.species)

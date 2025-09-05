# Day 8 – Descriptor Protocol

# --- 1. Basic Descriptor (logging access) ---
class LoggedAttribute:
    def __init__(self, name: str):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        print(f"Accessing {self.name} -> {self._value}")
        return self._value

    def __set__(self, instance, value):
        print(f"Setting {self.name} -> {value}")
        self._value = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        self._value = None


# --- 2. Type Enforcing Descriptor ---
class TypedAttribute:
    def __init__(self, name: str, expected_type: type):
        self.name = name
        self.expected_type = expected_type
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}, got {type(value).__name__}")
        self._value = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete attribute {self.name}")


# --- 3. Example Usage ---
class Person:
    name = LoggedAttribute("name")
    age = TypedAttribute("age", int)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


if __name__ == "__main__":
    # Logged attribute
    p = Person("Alice", 30)
    print(p.name)  # triggers __get__
    p.name = "Bob" # triggers __set__
    del p.name     # triggers __delete__

    # Type checked attribute
    p.age = 35     # works
    print("Age:", p.age)

    try:
        p.age = "not a number"  # raises TypeError
    except TypeError as e:
        print("Type error:", e)

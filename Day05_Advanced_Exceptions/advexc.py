# day5_advanced_exceptions.py

# --- Custom Exceptions ---
class InvalidAgeError(Exception):
    """Raised when age is not valid."""
    pass

class NegativeNumberError(Exception):
    """Raised when a negative number is encountered where not allowed."""
    pass


# --- Example: using try/except/else/finally ---
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero -> {e}")
    except TypeError as e:
        print(f"Error: Invalid type -> {e}")
    else:
        print(f"Result is {result}")
    finally:
        print("Finished divide() operation.\n")


# --- Example: raising custom exceptions ---
def check_age(age):
    if age < 0:
        raise NegativeNumberError("Age cannot be negative.")
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    return "Age is valid."


# --- Example: exception chaining ---
def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise ValueError("Conversion failed!") from e


# --- Example: context manager with exceptions ---
def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            print("File contents:", data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("Finished file operation.\n")


# --- Main test section ---
if __name__ == "__main__":
    # 1. Test divide
    divide(10, 2)
    divide(10, 0)
    divide("10", 5)

    # 2. Test custom exceptions
    try:
        print(check_age(15))
    except InvalidAgeError as e:
        print("Custom Exception Caught:", e)

    try:
        print(check_age(-5))
    except NegativeNumberError as e:
        print("Custom Exception Caught:", e)

    # 3. Test exception chaining
    try:
        convert_to_int("abc")
    except ValueError as e:
        print("Chained Exception:", e)

    # 4. Test context manager
    read_file("non_existent.txt")


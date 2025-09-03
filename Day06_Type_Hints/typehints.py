# Day 6 – Type Hints in Python
from typing import List, Dict, Tuple, Optional, Union, Any

# --- 1. Basic type hints ---
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"


# --- 2. Type hints with List, Dict, Tuple ---
def process_numbers(nums: List[int]) -> Tuple[int, int]:
    """Return minimum and maximum from a list of numbers."""
    return min(nums), max(nums)

def word_count(text: str) -> Dict[str, int]:
    """Return dictionary of word frequencies from a given text."""
    counts: Dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# --- 3. Optional & Union ---
def safe_divide(a: float, b: float) -> Optional[float]:
    """Divide a by b, return None if division by zero."""
    if b == 0:
        return None
    return a / b

def stringify(value: Union[int, float, str]) -> str:
    """Convert int/float/str to string."""
    return str(value)


# --- 4. Any & Type Aliases ---
JSON = Dict[str, Any]   # Type alias for JSON-like data

def parse_user(data: JSON) -> str:
    """Parse user dict with flexible types."""
    name = data.get("name", "Unknown")
    age = data.get("age", "N/A")
    return f"User: {name}, Age: {age}"


# --- Main Test Section ---
if __name__ == "__main__":
    # 1. Basic
    print("Add:", add(3, 7))
    print("Greet:", greet("Alice"))

    # 2. List, Dict, Tuple
    nums = [4, 1, 7, 3, 9]
    print("Process numbers:", process_numbers(nums))
    print("Word count:", word_count("hello world hello python"))

    # 3. Optional & Union
    print("Safe divide:", safe_divide(10, 2))
    print("Safe divide by zero:", safe_divide(10, 0))
    print("Stringify int:", stringify(42))
    print("Stringify float:", stringify(3.14))
    print("Stringify str:", stringify("hi"))

    # 4. Any & Alias
    user_data = {"name": "Bob", "age": 25, "active": True}
    print("Parsed user:", parse_user(user_data))

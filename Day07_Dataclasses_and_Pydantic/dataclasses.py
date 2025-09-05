# Day 7 – Data Classes & Pydantic
from dataclasses import dataclass, field
from typing import List
from pydantic import BaseModel, ValidationError, conint, EmailStr


# --- 1. Data Classes Example ---
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float = field(default=0.0)  # default value

    def summary(self) -> str:
        return f"'{self.title}' by {self.author}, {self.pages} pages, ${self.price:.2f}"


# --- 2. Pydantic Example ---
class UserModel(BaseModel):
    name: str
    age: conint(ge=0)  # age must be >= 0
    email: EmailStr
    skills: List[str] = []

    def greet(self) -> str:
        return f"Hi, I'm {self.name}, {self.age} years old."


# --- Main Test Section ---
if __name__ == "__main__":
    # Dataclass
    book = Book("Clean Code", "Robert C. Martin", 464, 29.99)
    print(book.summary())

    # Pydantic valid
    try:
        user = UserModel(name="Alice", age=25, email="alice@example.com", skills=["Python", "FastAPI"])
        print(user.greet())
        print("User dict:", user.dict())
    except ValidationError as e:
        print("Validation error:", e)

    # Pydantic invalid (age < 0, email wrong)
    try:
        invalid_user = UserModel(name="Bob", age=-5, email="not-an-email")
    except ValidationError as e:
        print("Invalid user error:\n", e)

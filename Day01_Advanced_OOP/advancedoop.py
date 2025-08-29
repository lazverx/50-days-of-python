from abc import ABC, abstractmethod

# === Abstract Base Class ===
class Shape(ABC):
    def __init__(self, name: str):
        self._name = name  # encapsulation (protected attribute)

    @property
    def name(self):
        return self._name

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


# === Inheritance & Polymorphism ===
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.__width = width      # encapsulation (private attribute)
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.__radius = radius

    def area(self) -> float:
        return 3.14159 * self.__radius**2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.__radius


# === Example of a Metaclass for Singleton Pattern ===
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """A Singleton configuration manager."""
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)


# === Usage Example ===
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"{shape.name} → Area: {shape.area()}, Perimeter: {shape.perimeter()}")

    # Singleton demo
    config1 = Config()
    config1.set("theme", "dark")

    config2 = Config()
    print("Theme from config2:", config2.get("theme"))  # proves Singleton works


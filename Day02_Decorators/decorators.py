import time
from functools import wraps

# === Basic Decorator ===
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}, result={result}")
        return result
    return wrapper


# === Decorator with Arguments ===
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"[REPEAT] {i+1}/{n}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# === Class-Based Decorator ===
class Timer:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {self.func.__name__} took {end - start:.6f}s")
        return result


# === Example Functions ===
@logger
@repeat(3)
def greet(name):
    return f"Hello, {name}!"

@Timer
def compute(n):
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    print(greet("Faiz"))
    print(compute(1_000_000))

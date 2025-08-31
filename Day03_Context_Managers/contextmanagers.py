from contextlib import contextmanager
import time

# === Custom Context Manager (Class-based) ===
class FileLogger:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "a")
        self.file.write("=== Start Logging ===\n")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.file.write(f"[ERROR] {exc_value}\n")
        self.file.write("=== End Logging ===\n")
        self.file.close()
        return True  # suppress exception for demo


# === Context Manager with contextlib ===
@contextmanager
def timer(label: str):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"[TIMER] {label} took {end - start:.6f}s")


# === Usage Example ===
if __name__ == "__main__":
    # Using FileLogger
    with FileLogger("log.txt") as log:
        log.write("This is a log entry.\n")

    # Using Timer
    with timer("Computation"):
        total = sum(i * i for i in range(1_000_00))
        print("Computation result:", total)

    # Demonstrate exception handling in context manager
    with FileLogger("log.txt") as log:
        log.write("Before error...\n")
        raise ValueError("Something went wrong!")

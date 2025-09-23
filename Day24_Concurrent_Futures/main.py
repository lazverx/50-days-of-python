"""
Day 24 – concurrent.futures
Date: 2025-09-21
"""

import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


# ========================
# Example CPU-bound function
# ========================
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# ========================
# Example I/O-bound function
# ========================
def fetch_data(url: str, delay: float) -> str:
    time.sleep(delay)  # simulate network latency
    return f"Fetched data from {url} after {delay:.1f}s"


# ========================
# Demo with ThreadPoolExecutor (I/O-bound)
# ========================
def demo_threadpool():
    urls = [("https://api.service/1", 1), ("https://api.service/2", 2), ("https://api.service/3", 1.5)]
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(fetch_data, url, delay) for url, delay in urls]

        for future in as_completed(futures):
            print(f"[ThreadPool] {future.result()}")


# ========================
# Demo with ProcessPoolExecutor (CPU-bound)
# ========================
def demo_processpool():
    numbers = [10_000_019, 10_000_033, 10_000_037, 10_000_039]
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(is_prime, n) for n in numbers]

        for n, future in zip(numbers, futures):
            print(f"[ProcessPool] {n} is prime? {future.result()}")


# ========================
# Main
# ========================
if __name__ == "__main__":
    print("=== concurrent.futures Demo ===")

    start = time.time()
    demo_threadpool()
    print(f"ThreadPool finished in {time.time() - start:.2f}s\n")

    start = time.time()
    demo_processpool()
    print(f"ProcessPool finished in {time.time() - start:.2f}s")

"""
Day 25 – Profiling and Optimization
Date: 2025-09-22
"""

import time
import math
import cProfile
import pstats
from functools import lru_cache


# ======================================================
# Example 1: Naive Fibonacci (inefficient)
# ======================================================
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ======================================================
# Example 2: Optimized Fibonacci (with caching)
# ======================================================
@lru_cache(maxsize=None)
def fib_optimized(n: int) -> int:
    if n <= 1:
        return n
    return fib_optimized(n - 1) + fib_optimized(n - 2)


# ======================================================
# Example 3: Expensive prime checking
# ======================================================
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# =======================================================
# Benchmark helpers
# =======================================================
def benchmark(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__}({args}) = {result} [took {end - start:.5f}s]")
    return result


# ======================================================
# Main with profiling
# ======================================================
def run_demo():
    # Compare naive vs optimized Fibonacci
    benchmark(fib_naive, 30)       # slow
    benchmark(fib_optimized, 30)   # fast due to caching

    # Profile prime checking loop
    numbers = [100003, 100019, 100043, 100049, 100057]
    results = [is_prime(n) for n in numbers]
    print("Prime check results:", dict(zip(numbers, results)))


if __name__ == "__main__":
    print("=== Profiling and Optimization Demo ===")

    # Run profiling
    profiler = cProfile.Profile()
    profiler.enable()

    run_demo()

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("cumtime")
    print("\n=== Profiling Results (Top 10) ===")
    stats.print_stats(10)

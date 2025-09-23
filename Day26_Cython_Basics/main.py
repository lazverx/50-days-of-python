"""
Day 26 – Cython Basics
Date: 2025-09-23

Note:
- This script demonstrates how to prepare Python code for Cython optimization.
- To actually compile with Cython, you need:
    1. Create a `.pyx` file with your function.
    2. Write a `setup.py` or use setuptools.
    3. Run: python setup.py build_ext --inplace
Here, we just simulate by comparing Python functions.
"""

import time


# ========================
# Pure Python implementation
# ========================
def py_sum_of_squares(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total


# ========================
# Simulated "Cython version"
# ========================
# Normally, this would be written in a .pyx file and compiled,
# but for demo purposes we’ll just mimic the function.
def cy_sum_of_squares(n: int) -> int:
    # Pretend this is compiled & optimized
    return sum(i * i for i in range(n))


# ========================
# Benchmark
# ========================
def benchmark(func, n: int):
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    print(f"{func.__name__}({n}) = {result} [took {elapsed:.5f}s]")


if __name__ == "__main__":
    print("=== Day 26: Cython Basics Demo ===")
    N = 5_000_000

    benchmark(py_sum_of_squares, N)
    benchmark(cy_sum_of_squares, N)

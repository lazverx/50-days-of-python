# Day 26 – Cython Basics

**Date:** 2025-09-23  

## What I Learned
- **Cython** allows compiling Python code into C extensions for major speedups.
- Typical steps to use Cython:
  1. Write performance-critical code in a `.pyx` file.
  2. Add type annotations (`cdef int`, etc.) for faster execution.
  3. Compile using `setup.py` or `setuptools`.
- Even small numeric computations can see huge gains.

## Tasks Completed
- Wrote a Python version of `sum_of_squares`.
- Prepared a Cython-ready version (simulated in `main.py`).
- Benchmarked both implementations for comparison.

## Files
- `main.py`

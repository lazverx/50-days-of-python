# Day 25 – Profiling and Optimization

**Date:** 2025-09-22  

## What I Learned
- Profiling helps identify performance bottlenecks in a program.
- Python provides:
  - `cProfile` → built-in profiler to measure function execution time.
  - `pstats` → analyze profiling results.
- Optimization strategies:
  - **Caching** with `functools.lru_cache`.
  - Choosing more efficient algorithms (e.g., naive recursion → memoized recursion).
  - Avoiding redundant computations.

## Tasks Completed
- Compared naive vs optimized Fibonacci implementations.
- Profiled execution of prime-checking loop.
- Displayed profiling results showing the slowest functions.

## Files
- `main.py`

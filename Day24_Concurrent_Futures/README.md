# Day 24 – concurrent.futures

**Date:** 2025-09-21  

## What I Learned
- `concurrent.futures` provides a high-level API for parallel execution.
- Two main executors:
  - `ThreadPoolExecutor` → Best for I/O-bound tasks (waiting on network, disk, etc.).
  - `ProcessPoolExecutor` → Best for CPU-bound tasks (heavy computations).
- Futures represent results of asynchronous computations, retrievable via `.result()` or `as_completed()`.

## Tasks Completed
- Simulated I/O-bound tasks using `ThreadPoolExecutor`.
- Simulated CPU-bound prime number checks with `ProcessPoolExecutor`.
- Compared execution time improvements.

## Files
- `main.py`

## Example Output

# Day 23 – Threading and the GIL

**Date:** 2025-09-20  

## What I Learned
- Python’s **Global Interpreter Lock (GIL)** prevents multiple threads from executing Python bytecode simultaneously.
- This means:
  - For **CPU-bound** tasks (heavy calculations), threads don’t improve performance.
  - For **I/O-bound** tasks (e.g., file/network operations), threads can improve performance by overlapping wait times.
- Difference between CPU-bound vs I/O-bound workloads in multithreading.

## Tasks Completed
- Implemented a CPU-bound calculation across threads (no performance gain due to GIL).
- Implemented an I/O-bound task using `time.sleep()` to simulate waiting (threads improve speed).
- Compared timing results.

## Files
- `main.py`

## Example Output

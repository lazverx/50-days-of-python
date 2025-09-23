"""
Day 23 – Threading and the GIL
Date: 2025-09-20
"""

import threading
import time


# ========================
# CPU-bound task
# ========================
def cpu_bound_task(n):
    """Simulates heavy CPU work by doing many calculations."""
    count = 0
    for i in range(n):
        count += i * i
    return count


def run_cpu_tasks_with_threads():
    threads = []
    results = [0, 0]

    def worker(idx, n):
        results[idx] = cpu_bound_task(n)

    start = time.time()
    for i in range(2):
        t = threading.Thread(target=worker, args=(i, 10_000_000))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time.time() - start
    print(f"Threads (CPU-bound): finished in {duration:.2f}s")


# ========================
# I/O-bound task
# ========================
def io_bound_task(duration):
    """Simulates I/O work by sleeping."""
    time.sleep(duration)
    return f"Slept for {duration}s"


def run_io_tasks_with_threads():
    threads = []
    results = [None, None]

    def worker(idx, d):
        results[idx] = io_bound_task(d)

    start = time.time()
    for i in range(2):
        t = threading.Thread(target=worker, args=(i, 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time.time() - start
    print(f"Threads (I/O-bound): finished in {duration:.2f}s")


# ========================
# Main
# ========================
if __name__ == "__main__":
    print("=== Threading and the GIL ===")

    # CPU-bound tasks: slower with threads (GIL prevents true parallelism)
    run_cpu_tasks_with_threads()

    # I/O-bound tasks: faster with threads (while one thread waits, another runs)
    run_io_tasks_with_threads()

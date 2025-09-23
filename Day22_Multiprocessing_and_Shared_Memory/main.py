"""
Day 22 – Multiprocessing and Shared Memory
Date: 2025-09-19
"""

import multiprocessing as mp
import time


# Worker function to increment a shared counter
def increment_counter(shared_counter, lock, n):
    for _ in range(n):
        with lock:
            shared_counter.value += 1
        time.sleep(0.001)


# Worker function to fill shared array
def fill_array(shared_array, value):
    for i in range(len(shared_array)):
        shared_array[i] = value
        time.sleep(0.001)


# Worker function to update shared dictionary
def update_dict(shared_dict, pid):
    shared_dict[pid] = f"Process-{pid} updated"
    time.sleep(0.5)


def main():
    print("=== Multiprocessing and Shared Memory ===")

    # Shared counter
    counter = mp.Value("i", 0)  # integer
    lock = mp.Lock()

    processes = [mp.Process(target=increment_counter, args=(counter, lock, 100)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Final counter value (expected 400): {counter.value}")

    # Shared array
    shared_array = mp.Array("i", 5)  # 5 integers
    p = mp.Process(target=fill_array, args=(shared_array, 7))
    p.start()
    p.join()
    print("Shared array contents:", list(shared_array))

    # Shared dict
    with mp.Manager() as manager:
        shared_dict = manager.dict()
        workers = [mp.Process(target=update_dict, args=(shared_dict, i)) for i in range(3)]

        for w in workers:
            w.start()
        for w in workers:
            w.join()

        print("Shared dict contents:", dict(shared_dict))


if __name__ == "__main__":
    main()

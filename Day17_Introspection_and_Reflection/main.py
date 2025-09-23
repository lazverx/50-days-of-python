import threading
import asyncio
import multiprocessing
import time


# === Threading Example ===
def worker_thread(name, delay):
    print(f"[Thread-{name}] starting...")
    time.sleep(delay)
    print(f"[Thread-{name}] finished after {delay}s")


def run_threads():
    print("\n=== Threading Example ===")
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker_thread, args=(i, i + 1))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


# === Asyncio Example ===
async def worker_async(name, delay):
    print(f"[Async-{name}] starting...")
    await asyncio.sleep(delay)
    print(f"[Async-{name}] finished after {delay}s")


async def run_asyncio():
    print("\n=== Asyncio Example ===")
    tasks = [worker_async(i, i + 1) for i in range(3)]
    await asyncio.gather(*tasks)


# === Multiprocessing Example ===
def worker_process(name, delay):
    print(f"[Process-{name}] starting...")
    time.sleep(delay)
    print(f"[Process-{name}] finished after {delay}s")


def run_multiprocessing():
    print("\n=== Multiprocessing Example ===")
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker_process, args=(i, i + 1))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()

    run_threads()
    asyncio.run(run_asyncio())
    run_multiprocessing()

    print(f"\nTotal execution time: {time.time() - start:.2f}s")

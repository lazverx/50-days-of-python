"""
Day 21 – Advanced AsyncIO
Date: 2025-09-18
"""

import asyncio
import random
from contextlib import asynccontextmanager


# ========================
# Async Context Manager
# ========================
@asynccontextmanager
async def connect_to_service(name: str):
    print(f"[{name}] Connecting...")
    await asyncio.sleep(0.5)
    try:
        yield f"Connection({name})"
    finally:
        print(f"[{name}] Closing connection...")
        await asyncio.sleep(0.2)


# ========================
# Async Generator
# ========================
async def data_stream(n: int):
    for i in range(n):
        await asyncio.sleep(0.3)
        yield f"chunk-{i}"


# ========================
# Simulated async tasks
# ========================
async def download_file(file_id: int):
    duration = random.uniform(0.5, 2.0)
    await asyncio.sleep(duration)
    return f"File-{file_id} downloaded in {duration:.2f}s"


async def log_event(event: str):
    await asyncio.sleep(0.2)
    print(f"[LOG] {event}")


# ========================
# Main async workflow
# ========================
async def main():
    print("=== AsyncIO Advanced Demo ===")

    # Run multiple downloads concurrently
    downloads = [download_file(i) for i in range(1, 4)]
    results = await asyncio.gather(*downloads)
    for res in results:
        print(res)

    # Using async context manager
    async with connect_to_service("Database") as conn:
        print(f"Using {conn}")
        await log_event("Database connection established")

    # Consuming async generator
    print("\nStreaming data:")
    async for chunk in data_stream(5):
        print(f"Received {chunk}")
        await log_event(f"Processed {chunk}")


if __name__ == "__main__":
    asyncio.run(main())

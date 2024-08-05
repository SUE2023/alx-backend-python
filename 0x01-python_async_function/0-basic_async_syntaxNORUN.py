#!/usr/bin/env python3
"""Async coroutine task"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    # Generate a random delay between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Asynchronously wait for the generated delay
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    random.seed(444)
    # To test the coroutine, you need to run it within an event loop
    async def main():
        result = await wait_random()
        print(f"Waited for: {result} seconds")

    asyncio.run(main())

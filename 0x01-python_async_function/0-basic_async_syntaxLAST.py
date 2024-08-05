import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    random.seed(444)

    # Manually create an event loop
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(wait_random())
    print(f"Waited for: {result} seconds")

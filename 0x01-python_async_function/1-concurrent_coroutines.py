#!/usr/bin/env python3
"""Async coroutine"""


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times"""

    wait_time = await asyncio.gather(*tuple(map(lambda_: wait_random(
                max_radom(max_delay), range(n))))
    return sorted(wait_times)

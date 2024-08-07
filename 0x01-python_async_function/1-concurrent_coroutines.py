#!/usr/bin/env python3
"""Async coroutine"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times and returns a sorted list of delays"""
    
    # Gather results of n wait_random calls concurrently
    wait_times = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    
    # Sort the results to ensure they are in ascending order
    return sorted(wait_times)

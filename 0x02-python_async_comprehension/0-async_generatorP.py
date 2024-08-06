#!/usr/bin/env python3
"""Async coroutine"""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """Generates a sequence of 10 numbers."""
    numbers = []
    for _ in range(10):
        await asyncio.sleep(1)
        numbers.append(random.random() * 10)
    return numbers

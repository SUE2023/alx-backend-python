#!/usr/bin/env python3
"""Async coroutine to generate random numbers"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates a sequence of 10 random numbers, waiting 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

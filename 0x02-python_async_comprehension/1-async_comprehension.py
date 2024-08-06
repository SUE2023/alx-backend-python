#!/usr/bin/env python3
'''Async Coroutine to collect random numbers generated.'''
from typing import List
from importlib import import_module


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.'''
    async_generator = import_module('0-async_generator').async_generator
    nums = []
    async for num in async_generator():
        nums.append(num)
    return nums

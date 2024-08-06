#!/usr/bin/env python3
'''Async coroutine to execute async_comprehension.'''
import asyncio
import time
from importlib import import_module

async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    
    # Create a list of tasks to execute async_comprehension 4 times
    tasks = [async_comprehension() for _ in range(4)]
    
    # Await all tasks to complete
    await asyncio.gather(*tasks)
    
    return time.time() - start_time

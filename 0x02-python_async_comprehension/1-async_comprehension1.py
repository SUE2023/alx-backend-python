#!/usr/bin/env python3 #a shebang line, it tells the operating system to use the python3 interpreter to run the script
'''Async Coroutine.  #module-level docstring, provides a brief description of what the module is for.
'''
from typing import List # Imports the List type from the typing module, which allows you to specify that a function returns a list of a specific type—in this case, float. 
from importlib import import_module as using # Imports the import_module function from the importlib module but renames it to using. This function is used to dynamically import modules.


async_generator = using('0-async_generator').async_generator #using('0-async_generator') dynamically imports the 0-async_generator module. and .async_generator accesses the async_generator function or object from the imported module.


async def async_comprehension() -> List[float]: #Defines an asynchronous function named async_comprehension that returns a list of floats.
    '''Creates a list of 10 numbers from a 10-number generator.# describes the function’s purpose.
    '''
    return [num async for num in async_generator()] #asynchronous list comprehension. It iterates over an asynchronous generator (async_generator()) and collects the values into a list.

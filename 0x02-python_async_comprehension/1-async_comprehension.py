#!/usr/bin/env python3
'''1-async_comprehension.py
'''

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''
    Coroutine that collects 10 random numbers using an async 
    comprehension over async_generator and returns them
    '''
    return [numb async for numb in async_generator()]

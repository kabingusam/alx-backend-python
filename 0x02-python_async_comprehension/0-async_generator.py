#!/usr/bin/env python3
'''0-async_generator.py
'''

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Async generator function that generates a random float between 0 and 9 in each iteration.

    Yields:
        float: A random float between 0 and 9

    '''
    async def _() -> AsyncGenerator[float, None]:
        i = 0
        while i < 10:
            await asyncio.sleep(1)
            yield random.uniform(0, 9)
            i += 1
    async for i in _():
        yield i

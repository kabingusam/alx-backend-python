#!/usr/bin/env python3
'''0-basic_async_syntax.py
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> str:
    '''
    The wait_random functio waits for a random delay between
    0 and max_delay seconds and evetually returns it
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return(delay)

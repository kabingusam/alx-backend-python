#!/usr/bin/env python3
'''2-measure_runtime.py
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Coroutine that returns the total run time
    '''
    start_time = time.perf_counter()
    get_total = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    get_total = end_time - start_time
    return(get_total)
    
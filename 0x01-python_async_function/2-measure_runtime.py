#!/usr/bin/env python3
'''2-measure_runtime.py
'''

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    '''
    The measure_time function measures the total execution time for
    the wait_n function with the specified n and max_delay arguments,
    and returns the average execution time (a float)
    '''
    start_time = time.per_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n 

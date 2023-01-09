#!/usr/bin/env python3
'''1-concurrent_coroutines.py
'''

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    '''
    measures the total execution time for wait_n(n, max_delay), 
    and returns total_time / n
    '''
    
#!/usr/bin/env python3
'''4-tasks.py
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delays: int) -> List[float]:
    '''
    The task_wait_n function takes two integers, n and max_delay, and
    returns a list of asyncio.Task objects that wait for random delays
    between 0 and max_delay seconds.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)

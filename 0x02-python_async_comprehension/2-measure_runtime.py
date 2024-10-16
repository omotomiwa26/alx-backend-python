#!/usr/bin/env python3
"""
    This coroutine measure_runtime should measure
    the total runtime and return it.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure_runtime should measure the total runtime and return it.
        four times in parallel using asyncio.gather.
    """
    task_start = time.perf_counter()
    task = [async_comprehension() for x in range(4)]
    await asyncio.gather(*task)
    task_end = time.perf_counter()
    return (task_end - task_start)

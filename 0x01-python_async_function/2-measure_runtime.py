#!/usr/bin/env python3
"""
This module measure an approximate elapsed time.
"""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    integers n and max_delay as arguments
    total execution time for wait_n(n, max_delay)
    returns total_time / n.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n

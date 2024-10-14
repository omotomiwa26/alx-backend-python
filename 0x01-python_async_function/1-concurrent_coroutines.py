#!/usr/bin/env python3
"""
This  routine executes multiple coroutines
at the same time with async
"""

import asyncio as a
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Accepts 2 int arguments (in this order): n and max_delay
    async routine called wait_n
    """

    tasks = [a.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in a.as_completed(tasks)]

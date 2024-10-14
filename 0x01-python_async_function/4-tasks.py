#!/usr/bin/env python3
"""
This function Takes the code from wait_n
and alter it into a new function task_wait_n
"""
import asyncio as a
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A new function task_wait_n
    identical to wait_n except task_wait_random
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in a.as_completed(tasks)]

#!/usr/bin/env python3
"""
This function do not create an async function,
use the regular function
"""

import asyncio as a

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> a.Task:
    """
    max_delay and returns a asyncio.Task
    regular function syntax to do this) task_wait_random
    """
    return a.create_task(wait_random(max_delay))

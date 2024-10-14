#!/usr/bin/env python3
"""
    This asynchronous coroutine
    takes in an integer argument
"""

import asyncio as a
import random as r


async def wait_random(max_delay: int = 10) -> float:
    """
        Delay between 0 and max_delay

        max_delay,with a default value of 10
    """
    new_rand = r.uniform(0, max_delay)
    await a.sleep(new_rand)
    return new_rand

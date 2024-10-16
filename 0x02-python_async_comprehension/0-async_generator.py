#!/usr/bin/env python3
"""
    This coroutine, async_generator that takes no arguments.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        async_generator - function to loop 10 times
        random number between 0 and 10. Use the random module
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

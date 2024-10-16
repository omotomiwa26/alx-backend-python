#!/usr/bin/env python3
"""
    This coroutine collects 10 random numbers
    using an async comprehensing over
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async_comprehension - function that takes no arguments
        Return: 10 random numbers
    """
    random_result = [x async for x in async_generator()]
    return random_result

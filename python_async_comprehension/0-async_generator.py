#!/usr/bin/env python3
"""Module that provides an async_generator coroutine."""

import asyncio
import random


async def async_generator():
    """Async generator that yields 10 random numbers with 1 second delays.

    Yields:
        Random numbers between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random 
delay and returns the delay time.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random delay and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

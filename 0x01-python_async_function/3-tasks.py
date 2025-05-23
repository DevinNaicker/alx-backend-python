#!/usr/bin/env python3
"""
Module that defines a regular function to create an asyncio Task for
wait_random.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio Task that runs wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))

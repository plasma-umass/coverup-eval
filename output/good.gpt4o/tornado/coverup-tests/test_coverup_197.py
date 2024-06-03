# file tornado/locks.py:454-455
# lines [454, 455]
# branches []

import pytest
from tornado.locks import Semaphore
import asyncio

@pytest.mark.asyncio
async def test_semaphore_aenter():
    sem = Semaphore(1)
    
    async with sem:
        assert sem._value == 0  # Ensure the semaphore is acquired

    assert sem._value == 1  # Ensure the semaphore is released after the context


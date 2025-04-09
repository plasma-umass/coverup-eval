# file: tornado/locks.py:454-455
# asked: {"lines": [454, 455], "branches": []}
# gained: {"lines": [454], "branches": []}

import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_aenter():
    sem = Semaphore(1)
    
    async with sem:
        assert sem._value == 0  # Ensure the semaphore is acquired

    assert sem._value == 1  # Ensure the semaphore is released after the context

@pytest.mark.asyncio
async def test_semaphore_aenter_with_timeout():
    sem = Semaphore(1)
    
    async with sem:
        assert sem._value == 0  # Ensure the semaphore is acquired

    assert sem._value == 1  # Ensure the semaphore is released after the context

    with pytest.raises(TimeoutError):
        async with sem:
            await sem.acquire(timeout=0.1)

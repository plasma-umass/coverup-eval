# file: tornado/locks.py:454-455
# asked: {"lines": [454, 455], "branches": []}
# gained: {"lines": [454], "branches": []}

import pytest
import asyncio
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_aenter():
    sem = Semaphore(1)
    async with sem:
        assert sem._value == 0  # Ensure the semaphore is acquired
    assert sem._value == 1  # Ensure the semaphore is released after the context

@pytest.mark.asyncio
async def test_semaphore_aenter_timeout(mocker):
    sem = Semaphore(0)
    mocker.patch.object(sem, 'acquire', side_effect=asyncio.TimeoutError)
    with pytest.raises(asyncio.TimeoutError):
        async with sem:
            pass  # This should not be reached

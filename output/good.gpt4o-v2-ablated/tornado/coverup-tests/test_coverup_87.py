# file: tornado/locks.py:529-537
# asked: {"lines": [529, 530, 537], "branches": []}
# gained: {"lines": [529, 530], "branches": []}

import pytest
import asyncio
from tornado.locks import Lock
from tornado.util import TimeoutError
from unittest.mock import patch
from datetime import timedelta

@pytest.mark.asyncio
async def test_lock_acquire_no_timeout():
    lock = Lock()
    async with lock.acquire() as acquired:
        assert acquired is not None

@pytest.mark.asyncio
async def test_lock_acquire_with_timeout():
    lock = Lock()
    timeout = 1.0
    async with lock.acquire(timeout=timeout) as acquired:
        assert acquired is not None

@pytest.mark.asyncio
async def test_lock_acquire_with_timedelta_timeout():
    lock = Lock()
    timeout = timedelta(seconds=1)
    async with lock.acquire(timeout=timeout) as acquired:
        assert acquired is not None

@pytest.mark.asyncio
async def test_lock_acquire_timeout_error():
    lock = Lock()
    timeout = 0.1

    async def mock_acquire(timeout):
        await asyncio.sleep(timeout)
        raise TimeoutError()

    with patch.object(lock._block, 'acquire', side_effect=mock_acquire):
        with pytest.raises(TimeoutError):
            await lock.acquire(timeout=timeout)

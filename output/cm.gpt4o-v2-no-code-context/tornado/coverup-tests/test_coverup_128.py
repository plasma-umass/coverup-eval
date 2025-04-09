# file: tornado/locks.py:529-537
# asked: {"lines": [529, 530, 537], "branches": []}
# gained: {"lines": [529, 530], "branches": []}

import pytest
import asyncio
from tornado.locks import Lock
from tornado.util import TimeoutError
from datetime import timedelta

@pytest.mark.asyncio
async def test_lock_acquire_no_timeout():
    lock = Lock()
    async with lock.acquire():
        assert lock._block.locked()

@pytest.mark.asyncio
async def test_lock_acquire_with_timeout():
    lock = Lock()
    async with lock.acquire(timeout=1):
        assert lock._block.locked()

@pytest.mark.asyncio
async def test_lock_acquire_timeout_error():
    lock = Lock()
    await lock.acquire()
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=0.1)

@pytest.mark.asyncio
async def test_lock_acquire_timedelta_timeout():
    lock = Lock()
    async with lock.acquire(timeout=timedelta(seconds=1)):
        assert lock._block.locked()

@pytest.mark.asyncio
async def test_lock_acquire_timedelta_timeout_error():
    lock = Lock()
    await lock.acquire()
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=timedelta(seconds=0.1))

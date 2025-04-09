# file: tornado/locks.py:529-537
# asked: {"lines": [529, 530, 537], "branches": []}
# gained: {"lines": [529, 530], "branches": []}

import pytest
import datetime
from tornado.locks import Lock
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_lock_acquire_timeout():
    lock = Lock()
    timeout = 0.1  # 100ms timeout

    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=timeout)

    # Ensure the lock is still available after the timeout
    await lock.acquire()
    lock.release()

@pytest.mark.asyncio
async def test_lock_acquire_no_timeout():
    lock = Lock()

    await lock.acquire()
    lock.release()

@pytest.mark.asyncio
async def test_lock_acquire_with_timedelta():
    lock = Lock()
    timeout = datetime.timedelta(milliseconds=100)  # 100ms timeout

    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=timeout)

    # Ensure the lock is still available after the timeout
    await lock.acquire()
    lock.release()

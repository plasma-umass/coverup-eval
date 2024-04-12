# file tornado/locks.py:529-537
# lines [529, 530, 537]
# branches []

import asyncio
import datetime
import pytest
from tornado.locks import Lock
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_lock_acquire_timeout():
    lock = Lock()
    await lock.acquire()  # Acquire the lock to ensure the next acquire will wait

    # Now we try to acquire the lock with a timeout, expecting it to fail
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=0.1)

    # Release the lock to clean up
    lock.release()

@pytest.mark.asyncio
async def test_lock_acquire_timeout_with_timedelta():
    lock = Lock()
    await lock.acquire()  # Acquire the lock to ensure the next acquire will wait

    # Now we try to acquire the lock with a timedelta timeout, expecting it to fail
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=datetime.timedelta(milliseconds=100))

    # Release the lock to clean up
    lock.release()

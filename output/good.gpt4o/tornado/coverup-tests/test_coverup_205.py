# file tornado/locks.py:486-522
# lines [486, 487]
# branches []

import pytest
import asyncio
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_acquire_release():
    lock = Lock()

    # Ensure the lock is initially unlocked
    assert not lock._waiters

    # Acquire the lock
    await lock.acquire()
    assert lock._waiters

    # Try to acquire the lock again in a different coroutine
    async def try_acquire():
        await lock.acquire()
        return True

    acquire_task = asyncio.create_task(try_acquire())
    await asyncio.sleep(0.1)  # Ensure the task is waiting for the lock
    assert not acquire_task.done()

    # Release the lock and ensure the waiting coroutine acquires it
    lock.release()
    await acquire_task
    assert acquire_task.result()

    # Ensure releasing an unlocked lock raises RuntimeError
    with pytest.raises(RuntimeError):
        lock.release()

    # Clean up
    lock.release()

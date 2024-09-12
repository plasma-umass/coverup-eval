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
    timeout = 0.1

    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=timeout)

@pytest.mark.asyncio
async def test_lock_acquire_no_timeout():
    lock = Lock()
    await lock.acquire()
    assert lock._block.locked()

    lock.release()
    assert not lock._block.locked()

# file: tornado/locks.py:529-537
# asked: {"lines": [529, 530, 537], "branches": []}
# gained: {"lines": [529, 530], "branches": []}

import pytest
import datetime
from unittest.mock import Mock
from tornado.locks import Lock
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_lock_acquire_timeout():
    lock = Lock()
    lock._block = Mock()
    lock._block.acquire = Mock(side_effect=TimeoutError)
    
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=1)

    lock._block.acquire.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_lock_acquire_no_timeout():
    lock = Lock()
    lock._block = Mock()
    lock._block.acquire = Mock(return_value="acquired")
    
    result = await lock.acquire()
    
    assert result == "acquired"
    lock._block.acquire.assert_called_once_with(None)

# file tornado/locks.py:529-537
# lines [529, 530, 537]
# branches []

import pytest
import asyncio
from unittest.mock import patch
from tornado.locks import Lock
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_lock_acquire_timeout(mocker):
    lock = Lock()
    
    # Mock the _block attribute and its acquire method
    mock_block = mocker.patch.object(lock, '_block')
    mock_acquire = mock_block.acquire
    mock_acquire.side_effect = TimeoutError
    
    with pytest.raises(TimeoutError):
        await lock.acquire(timeout=0.1)
    
    mock_acquire.assert_called_once_with(0.1)

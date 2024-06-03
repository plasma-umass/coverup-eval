# file tornado/locks.py:562-563
# lines [562, 563]
# branches []

import pytest
import asyncio
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aenter(mocker):
    lock = Lock()
    
    # Mock the acquire method to ensure it gets called
    mock_acquire = mocker.patch.object(lock, 'acquire', autospec=True)
    
    async with lock:
        pass
    
    # Assert that acquire was called once
    mock_acquire.assert_called_once()

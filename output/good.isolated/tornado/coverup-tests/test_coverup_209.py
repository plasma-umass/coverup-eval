# file tornado/locks.py:554-560
# lines [554, 560]
# branches []

import pytest
from tornado.locks import Lock
from unittest.mock import MagicMock
import asyncio

@pytest.fixture
def mock_lock():
    lock = Lock()
    lock.acquire = MagicMock(return_value=asyncio.Future())
    lock.acquire.return_value.set_result(True)
    lock.release = MagicMock()
    return lock

@pytest.mark.asyncio
async def test_lock_context_manager(mock_lock):
    async with mock_lock:
        mock_lock.acquire.assert_called_once()
    mock_lock.release.assert_called_once()

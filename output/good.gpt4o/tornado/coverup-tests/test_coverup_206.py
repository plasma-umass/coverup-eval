# file tornado/locks.py:554-560
# lines [554, 560]
# branches []

import pytest
from unittest import mock
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

@pytest.mark.asyncio
async def test_lock_exit(lock):
    with mock.patch.object(lock, '__enter__', return_value=None) as mock_enter:
        async with lock:
            pass
        mock_enter.assert_called_once()

@pytest.mark.asyncio
async def test_lock_exit_with_exception(lock):
    with mock.patch.object(lock, '__enter__', return_value=None) as mock_enter:
        with pytest.raises(ValueError):
            async with lock:
                raise ValueError("Test exception")
        mock_enter.assert_called_once()

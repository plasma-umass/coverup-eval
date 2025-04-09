# file: tornado/locks.py:562-563
# asked: {"lines": [562, 563], "branches": []}
# gained: {"lines": [562], "branches": []}

import pytest
import asyncio
from tornado.locks import Lock
from unittest.mock import patch

@pytest.mark.asyncio
async def test_lock_aenter():
    lock = Lock()

    with patch.object(lock, 'acquire', wraps=lock.acquire) as mock_acquire:
        async with lock:
            pass

        mock_acquire.assert_called_once()


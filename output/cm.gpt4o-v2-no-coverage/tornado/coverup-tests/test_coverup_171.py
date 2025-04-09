# file: tornado/locks.py:562-563
# asked: {"lines": [562, 563], "branches": []}
# gained: {"lines": [562], "branches": []}

import pytest
import asyncio
from unittest.mock import MagicMock

from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aenter():
    lock = Lock()
    lock.acquire = MagicMock(return_value=asyncio.Future())
    lock.acquire.return_value.set_result(None)

    async with lock:
        lock.acquire.assert_called_once()

    # Ensure the lock is released after the context manager exits
    assert not lock.acquire.return_value.done()

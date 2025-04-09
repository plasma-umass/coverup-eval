# file: tornado/locks.py:562-563
# asked: {"lines": [562, 563], "branches": []}
# gained: {"lines": [562], "branches": []}

import pytest
import asyncio
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aenter():
    lock = Lock()
    async with lock:
        assert lock.locked()
    assert not lock.locked()

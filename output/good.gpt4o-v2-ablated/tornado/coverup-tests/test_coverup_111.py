# file: tornado/locks.py:562-563
# asked: {"lines": [562, 563], "branches": []}
# gained: {"lines": [562], "branches": []}

import pytest
import asyncio
from tornado.locks import Lock

@pytest.mark.asyncio
async def test_lock_aenter(monkeypatch):
    lock = Lock()

    async def mock_acquire():
        mock_acquire.called = True

    mock_acquire.called = False
    monkeypatch.setattr(lock, 'acquire', mock_acquire)

    async with lock:
        pass

    assert mock_acquire.called

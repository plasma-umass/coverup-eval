# file tornado/locks.py:562-563
# lines [562, 563]
# branches []

import pytest
from tornado.locks import Lock
from tornado.ioloop import IOLoop
from contextlib import asynccontextmanager

@pytest.fixture
def event_loop():
    loop = IOLoop.current()
    yield loop
    loop.close(all_fds=True)

@pytest.mark.asyncio
async def test_lock_aenter(event_loop):
    lock = Lock()
    async with lock:
        assert lock.is_locked()
    assert not lock.is_locked()

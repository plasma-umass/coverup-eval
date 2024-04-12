# file tornado/locks.py:454-455
# lines [454, 455]
# branches []

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from contextlib import asynccontextmanager

@pytest.fixture
def io_loop():
    loop = IOLoop.current()
    yield loop
    loop.close(all_fds=True)

@pytest.mark.asyncio
async def test_semaphore_context_manager(io_loop):
    semaphore = Semaphore(value=1)

    async with semaphore:
        assert semaphore._value == 0

    # After the context manager, the semaphore should be released
    assert semaphore._value == 1

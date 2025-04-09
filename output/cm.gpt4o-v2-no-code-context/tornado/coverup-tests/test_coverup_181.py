# file: tornado/locks.py:228-233
# asked: {"lines": [228, 233], "branches": []}
# gained: {"lines": [228, 233], "branches": []}

import pytest
from tornado.locks import Event
import tornado.ioloop
import asyncio

@pytest.fixture
def event():
    return Event()

@pytest.fixture
def io_loop():
    loop = tornado.ioloop.IOLoop.current()
    yield loop
    loop.close(all_fds=True)

def test_event_clear(event):
    # Set the event first
    event.set()
    assert event.is_set() is True

    # Now clear the event
    event.clear()
    assert event.is_set() is False

@pytest.mark.asyncio
async def test_event_wait_after_clear(event):
    # Set the event first
    event.set()
    assert event.is_set() is True

    # Now clear the event
    event.clear()
    assert event.is_set() is False

    # Ensure that wait will block (use a timeout to avoid hanging the test)
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(event.wait(), timeout=0.1)

# file tornado/locks.py:235-259
# lines [235, 236, 243, 244, 245, 246, 247, 248, 249, 250, 252, 256, 257, 259]
# branches ['244->245', '244->247', '249->250', '249->252']

import datetime
import pytest
from tornado import gen
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_event_wait_timeout():
    event = Event()
    timeout = datetime.timedelta(seconds=0.1)
    with pytest.raises(TimeoutError):
        await event.wait(timeout=timeout)
    assert not event._waiters

@pytest.mark.asyncio
async def test_event_wait_no_timeout():
    event = Event()
    event.set()
    await event.wait()  # This should not raise a TimeoutError
    assert event.is_set()

@pytest.mark.asyncio
async def test_event_wait_with_timeout_not_triggered():
    event = Event()
    timeout = datetime.timedelta(seconds=0.1)
    future = event.wait(timeout=timeout)
    event.set()
    await future  # This should complete without a TimeoutError
    assert event.is_set()
    assert not event._waiters

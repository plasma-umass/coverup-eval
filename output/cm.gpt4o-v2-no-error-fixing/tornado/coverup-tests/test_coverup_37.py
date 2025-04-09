# file: tornado/locks.py:235-259
# asked: {"lines": [235, 236, 243, 244, 245, 246, 247, 248, 249, 250, 252, 256, 257, 259], "branches": [[244, 245], [244, 247], [249, 250], [249, 252]]}
# gained: {"lines": [235, 236], "branches": []}

import pytest
import datetime
from tornado import gen
from tornado.concurrent import Future
from tornado.util import TimeoutError
from tornado.ioloop import IOLoop
from tornado.locks import Event

@pytest.mark.gen_test
async def test_event_wait_no_timeout():
    event = Event()
    event._value = True
    fut = event.wait()
    result = await fut
    assert result is None

@pytest.mark.gen_test
async def test_event_wait_with_timeout():
    event = Event()
    event._value = False
    timeout = datetime.timedelta(seconds=1)
    fut = event.wait(timeout)
    with pytest.raises(TimeoutError):
        await fut

@pytest.mark.gen_test
async def test_event_wait_set_result_before_timeout():
    event = Event()
    event._value = False
    timeout = datetime.timedelta(seconds=1)
    fut = event.wait(timeout)
    IOLoop.current().add_timeout(datetime.timedelta(milliseconds=500), lambda: event.set())
    result = await fut
    assert result is None

@pytest.mark.gen_test
async def test_event_wait_cancel_before_timeout():
    event = Event()
    event._value = False
    timeout = datetime.timedelta(seconds=1)
    fut = event.wait(timeout)
    fut.cancel()
    with pytest.raises(asyncio.CancelledError):
        await fut

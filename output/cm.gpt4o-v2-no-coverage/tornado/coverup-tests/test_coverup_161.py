# file: tornado/locks.py:228-233
# asked: {"lines": [228, 233], "branches": []}
# gained: {"lines": [228], "branches": []}

import pytest
from tornado.locks import Event
from tornado.concurrent import Future
from tornado import gen
import datetime

@pytest.mark.gen_test
async def test_event_clear():
    event = Event()
    event.set()
    assert event._value is True
    event.clear()
    assert event._value is False

@pytest.mark.gen_test
async def test_event_set():
    event = Event()
    assert event._value is False
    event.set()
    assert event._value is True

@pytest.mark.gen_test
async def test_event_wait():
    event = Event()
    future = event.wait()
    assert isinstance(future, Future)
    assert not future.done()
    event.set()
    await future
    assert future.done()

@pytest.mark.gen_test
async def test_event_wait_with_timeout():
    event = Event()
    timeout = datetime.timedelta(seconds=1)
    future = event.wait(timeout)
    assert isinstance(future, Future)
    with pytest.raises(gen.TimeoutError):
        await future

# file: tornado/locks.py:235-259
# asked: {"lines": [235, 236, 243, 244, 245, 246, 247, 248, 249, 250, 252, 256, 257, 259], "branches": [[244, 245], [244, 247], [249, 250], [249, 252]]}
# gained: {"lines": [235, 236], "branches": []}

import pytest
import datetime
from tornado.locks import Event
from tornado.util import TimeoutError
from tornado import gen
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_event_wait_no_timeout():
    event = Event()
    event.set()
    fut = event.wait()
    result = await fut
    assert result is None

@pytest.mark.asyncio
async def test_event_wait_with_timeout(monkeypatch):
    event = Event()
    timeout = datetime.timedelta(seconds=1)

    async def mock_with_timeout(timeout, future):
        await gen.sleep(0.1)
        raise TimeoutError()

    monkeypatch.setattr(gen, 'with_timeout', mock_with_timeout)

    with pytest.raises(TimeoutError):
        await event.wait(timeout)

@pytest.mark.asyncio
async def test_event_wait_timeout_then_set(monkeypatch):
    event = Event()
    timeout = datetime.timedelta(seconds=1)

    async def mock_with_timeout(timeout, future):
        await gen.sleep(0.1)
        return future

    monkeypatch.setattr(gen, 'with_timeout', mock_with_timeout)

    fut = event.wait(timeout)
    event.set()
    result = await fut
    assert result is None

@pytest.mark.asyncio
async def test_event_wait_timeout_cancel(monkeypatch):
    event = Event()
    timeout = datetime.timedelta(seconds=1)

    async def mock_with_timeout(timeout, future):
        await gen.sleep(0.1)
        return future

    monkeypatch.setattr(gen, 'with_timeout', mock_with_timeout)

    fut = event.wait(timeout)
    fut.cancel()
    with pytest.raises(TimeoutError):
        await fut

@pytest.mark.asyncio
async def test_event_wait_timeout_not_triggered():
    event = Event()
    timeout = datetime.timedelta(seconds=1)

    fut = event.wait(timeout)
    IOLoop.current().call_later(0.1, event.set)
    result = await fut
    assert result is None

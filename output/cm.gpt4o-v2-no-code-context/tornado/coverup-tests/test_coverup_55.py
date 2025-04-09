# file: tornado/queues.py:225-254
# asked: {"lines": [225, 226, 248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
import datetime
from tornado.queues import Queue, QueueEmpty
from tornado.util import TimeoutError
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_queue_get_no_timeout():
    q = Queue()
    q.put_nowait(1)
    result = await q.get()
    assert result == 1

@pytest.mark.asyncio
async def test_queue_get_with_timeout():
    q = Queue()
    with pytest.raises(TimeoutError):
        await q.get(timeout=IOLoop.current().time() + 0.1)

@pytest.mark.asyncio
async def test_queue_get_with_timedelta_timeout():
    q = Queue()
    with pytest.raises(TimeoutError):
        await q.get(timeout=datetime.timedelta(seconds=0.1))

@pytest.mark.asyncio
async def test_queue_get_no_wait():
    q = Queue()
    q.put_nowait(1)
    result = await q.get()
    assert result == 1

@pytest.mark.asyncio
async def test_queue_get_nowait_raises():
    q = Queue()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

@pytest.mark.asyncio
async def test_queue_get_with_item():
    q = Queue()
    q.put_nowait(1)
    result = await q.get()
    assert result == 1

@pytest.mark.asyncio
async def test_queue_get_timeout_set():
    q = Queue()
    future = q.get(timeout=IOLoop.current().time() + 0.1)
    assert future in q._getters
    with pytest.raises(TimeoutError):
        await future

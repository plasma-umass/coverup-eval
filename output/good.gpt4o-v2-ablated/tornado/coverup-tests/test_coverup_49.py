# file: tornado/queues.py:225-254
# asked: {"lines": [225, 226, 248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
import datetime
from tornado.queues import Queue, QueueEmpty
from tornado.util import TimeoutError
from tornado.concurrent import Future
from unittest.mock import patch

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
        await q.get(timeout=0.1)

@pytest.mark.asyncio
async def test_queue_get_with_timedelta_timeout():
    q = Queue()
    with pytest.raises(TimeoutError):
        await q.get(timeout=datetime.timedelta(seconds=0.1))

@pytest.mark.asyncio
async def test_queue_get_no_wait():
    q = Queue()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

@pytest.mark.asyncio
async def test_queue_get_future_set_result():
    q = Queue()
    future = Future()
    q._getters.append(future)
    q.put_nowait(1)
    result = await future
    assert result == 1

@pytest.mark.asyncio
async def test_queue_get_future_timeout(mocker):
    q = Queue()
    future = Future()
    mocker.patch('tornado.queues._set_timeout', side_effect=lambda f, t: f.set_exception(TimeoutError()))
    q._getters.append(future)
    with pytest.raises(TimeoutError):
        await q.get(timeout=0.1)

# file: tornado/queues.py:225-254
# asked: {"lines": [225, 226, 248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
import datetime
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future
from tornado import gen

@pytest.mark.asyncio
async def test_queue_get_with_item():
    queue = Queue()
    queue.put_nowait(1)
    future = queue.get()
    result = await future
    assert result == 1

@pytest.mark.asyncio
async def test_queue_get_empty_with_timeout(mocker):
    queue = Queue()
    mocker.patch.object(queue, '_getters', [])
    timeout = datetime.timedelta(seconds=1)
    future = queue.get(timeout=timeout)
    assert isinstance(future, Future)
    assert future not in queue._getters

@pytest.mark.asyncio
async def test_queue_get_empty_no_timeout(mocker):
    queue = Queue()
    mocker.patch.object(queue, '_getters', [])
    future = queue.get()
    assert isinstance(future, Future)
    assert future in queue._getters

@pytest.mark.asyncio
async def test_queue_get_nowait_raises():
    queue = Queue()
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

@pytest.mark.asyncio
async def test_queue_get_with_timeout_set(mocker):
    queue = Queue()
    mocker.patch.object(queue, '_getters', [])
    mocker.patch('tornado.ioloop.IOLoop.current')
    timeout = datetime.timedelta(seconds=1)
    future = queue.get(timeout=timeout)
    assert isinstance(future, Future)
    assert future in queue._getters

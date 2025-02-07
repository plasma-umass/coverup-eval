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
    mocker.patch.object(queue, '_getters', new_callable=list)
    timeout = datetime.timedelta(seconds=1)
    future = queue.get(timeout=timeout)
    assert future in queue._getters
    assert future.done() is False

@pytest.mark.asyncio
async def test_queue_get_empty_no_timeout(mocker):
    queue = Queue()
    mocker.patch.object(queue, '_getters', new_callable=list)
    future = queue.get()
    assert future in queue._getters
    assert future.done() is False

@pytest.mark.asyncio
async def test_queue_get_nowait_raises_queue_empty():
    queue = Queue()
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

@pytest.mark.asyncio
async def test_queue_get_with_timeout_expired(mocker):
    queue = Queue()
    mocker.patch.object(queue, '_getters', new_callable=list)
    timeout = datetime.timedelta(seconds=0)
    future = queue.get(timeout=timeout)
    await gen.sleep(0.1)
    assert future.done() is True
    with pytest.raises(gen.TimeoutError):
        await future

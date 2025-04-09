# file: tornado/queues.py:292-300
# asked: {"lines": [292, 293, 300], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
import asyncio
import datetime
from tornado.queues import Queue
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_queue_join_no_timeout():
    queue = Queue()
    await queue.put(1)
    await queue.get()
    await queue.task_done()
    await queue.join()
    assert queue.qsize() == 0

@pytest.mark.asyncio
async def test_queue_join_with_timeout():
    queue = Queue()
    await queue.put(1)
    with pytest.raises(TimeoutError):
        await queue.join(timeout=0.1)
    assert queue.qsize() == 1

@pytest.mark.asyncio
async def test_queue_join_with_timedelta_timeout():
    queue = Queue()
    await queue.put(1)
    with pytest.raises(TimeoutError):
        await queue.join(timeout=datetime.timedelta(seconds=0.1))
    assert queue.qsize() == 1

@pytest.mark.asyncio
async def test_queue_join_after_task_done():
    queue = Queue()
    await queue.put(1)
    await queue.get()
    await queue.task_done()
    await queue.join(timeout=0.1)
    assert queue.qsize() == 0

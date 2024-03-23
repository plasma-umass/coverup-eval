# file tornado/queues.py:173-175
# lines [173, 175]
# branches []

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_qsize():
    queue = Queue(maxsize=3)

    # Ensure the queue is empty initially
    assert queue.qsize() == 0

    # Put an item into the queue
    await queue.put(1)
    assert queue.qsize() == 1

    # Put another item into the queue
    await queue.put(2)
    assert queue.qsize() == 2

    # Clean up by consuming the items
    assert await queue.get() == 1
    assert await queue.get() == 2
    queue.task_done()
    queue.task_done()

    # Ensure the queue is empty at the end
    assert queue.qsize() == 0

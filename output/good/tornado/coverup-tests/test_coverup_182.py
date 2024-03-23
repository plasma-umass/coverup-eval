# file tornado/queues.py:312-313
# lines [312, 313]
# branches []

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_put():
    q = Queue(maxsize=1)

    # Ensure the queue is empty
    assert q.qsize() == 0

    # Put an item into the queue
    await q.put('item')

    # Ensure the item is in the queue
    assert q.qsize() == 1
    assert q._queue[-1] == 'item'

    # Clean up the queue
    await q.get()
    assert q.qsize() == 0

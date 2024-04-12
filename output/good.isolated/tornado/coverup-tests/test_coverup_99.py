# file tornado/queues.py:73-78
# lines [73, 74, 75, 77, 78]
# branches []

import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_queue_iterator():
    q = Queue(maxsize=1)
    # Put an item into the queue
    await q.put(1)

    # Create an iterator for the queue
    iterator = q.__aiter__()

    # Use the iterator to get an item
    next_item = await iterator.__anext__()

    # Check that the item gotten is the same as the one put in
    assert next_item == 1

    # Clean up by allowing the queue to finish its get
    await q.get()

    # Assert the queue is empty after cleanup
    assert q.qsize() == 0

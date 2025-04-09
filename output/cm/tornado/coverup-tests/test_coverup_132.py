# file tornado/queues.py:168-171
# lines [168, 169, 171]
# branches []

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_maxsize():
    # Create a Queue with a specific maxsize
    maxsize = 5
    queue = Queue(maxsize=maxsize)

    # Check if the maxsize property returns the correct value
    assert queue.maxsize == maxsize

    # Clean up the queue to not affect other tests
    queue._queue.clear()

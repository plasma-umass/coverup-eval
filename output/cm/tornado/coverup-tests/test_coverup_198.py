# file tornado/queues.py:309-310
# lines [309, 310]
# branches []

import pytest
from tornado.queues import Queue
from collections import deque

@pytest.mark.asyncio
async def test_queue_get():
    # Create an instance of the Queue with some items
    queue = Queue(maxsize=3)
    for item in range(3):
        await queue.put(item)

    # Ensure the queue has the expected items
    assert list(queue._queue) == [0, 1, 2], "Queue should contain items [0, 1, 2]"

    # Call the _get method and check the result
    result = queue._get()
    assert result == 0, "The _get method should return the first item"

    # Ensure the item was removed from the queue
    assert list(queue._queue) == [1, 2], "Queue should contain items [1, 2] after _get"

    # Clean up: clear the queue to ensure no side effects for other tests
    queue._queue = deque()

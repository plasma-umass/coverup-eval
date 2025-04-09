# file tornado/queues.py:53-56
# lines [53, 54, 56]
# branches []

import pytest
from tornado.queues import Queue, QueueFull

@pytest.mark.gen_test
async def test_queue_put_nowait_full():
    # Create a Queue with maxsize 1
    queue = Queue(maxsize=1)
    await queue.put('item1')  # Fill the queue to its maxsize

    # Now the queue is full, so putting another item should raise QueueFull
    with pytest.raises(QueueFull):
        queue.put_nowait('item2')

    # Clean up: ensure the queue is empty after the test
    await queue.get()
    assert queue.empty()

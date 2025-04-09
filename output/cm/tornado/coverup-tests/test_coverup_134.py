# file tornado/queues.py:47-50
# lines [47, 48, 50]
# branches []

import pytest
from tornado.queues import Queue, QueueEmpty

@pytest.mark.gen_test
async def test_queue_get_nowait_raises_queue_empty():
    queue = Queue(maxsize=0)

    # Ensure the queue is empty
    assert queue.empty()

    # Attempt to get an item nowait, which should raise QueueEmpty
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    # Clean up the queue to not affect other tests
    queue._queue.clear()

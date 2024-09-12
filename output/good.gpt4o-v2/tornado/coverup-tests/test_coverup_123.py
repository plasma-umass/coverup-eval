# file: tornado/queues.py:53-56
# asked: {"lines": [53, 54, 56], "branches": []}
# gained: {"lines": [53, 54, 56], "branches": []}

import pytest
from tornado.queues import Queue, QueueFull

def test_queue_put_nowait_raises_queuefull():
    queue = Queue(maxsize=1)
    queue.put_nowait(1)  # Fill the queue

    with pytest.raises(QueueFull):
        queue.put_nowait(2)  # This should raise QueueFull

    # Clean up
    assert queue.qsize() == 1
    assert queue.get_nowait() == 1
    assert queue.qsize() == 0

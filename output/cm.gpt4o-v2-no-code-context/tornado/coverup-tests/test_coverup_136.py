# file: tornado/queues.py:53-56
# asked: {"lines": [53, 54, 56], "branches": []}
# gained: {"lines": [53, 54, 56], "branches": []}

import pytest
from tornado.queues import Queue, QueueFull

def test_queue_full_exception():
    with pytest.raises(QueueFull):
        raise QueueFull("Queue is full")

def test_queue_put_nowait_raises_queue_full():
    queue = Queue(maxsize=1)
    queue.put_nowait(1)

    with pytest.raises(QueueFull):
        queue.put_nowait(2)

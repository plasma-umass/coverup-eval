# file: tornado/queues.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312, 313], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_put():
    queue = Queue()
    queue._init()  # Initialize the internal queue
    queue._put(1)
    assert list(queue._queue) == [1]

    queue._put(2)
    assert list(queue._queue) == [1, 2]

    queue._put(3)
    assert list(queue._queue) == [1, 2, 3]

    # Clean up
    queue._queue.clear()

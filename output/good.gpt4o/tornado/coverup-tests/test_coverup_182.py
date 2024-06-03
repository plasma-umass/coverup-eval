# file tornado/queues.py:306-307
# lines [306, 307]
# branches []

import pytest
from tornado.queues import Queue
import collections

def test_queue_init():
    class TestQueue(Queue):
        def __init__(self):
            self._init()

    test_queue = TestQueue()
    assert isinstance(test_queue._queue, collections.deque)
    assert len(test_queue._queue) == 0

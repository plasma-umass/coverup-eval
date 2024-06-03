# file tornado/queues.py:333-334
# lines [333, 334]
# branches []

import pytest
from tornado.queues import Queue

def test_queue_str_method():
    class TestQueue(Queue):
        def _format(self):
            return "test_format"

    queue = TestQueue()
    assert str(queue) == "<TestQueue test_format>"

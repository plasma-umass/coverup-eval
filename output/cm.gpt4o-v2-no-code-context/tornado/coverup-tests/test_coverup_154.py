# file: tornado/queues.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from collections import deque
from tornado.queues import Queue

class TestQueue:
    @pytest.fixture
    def queue(self):
        q = Queue()
        q._queue = deque()
        yield q
        q._queue.clear()

    def test_get_from_non_empty_queue(self, queue):
        queue._queue.append('test_item')
        result = queue._get()
        assert result == 'test_item'
        assert len(queue._queue) == 0

    def test_get_from_empty_queue(self, queue):
        with pytest.raises(IndexError):
            queue._get()

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
        q._queue = deque([1, 2, 3])
        return q

    def test_get(self, queue):
        assert queue._get() == 1
        assert list(queue._queue) == [2, 3]

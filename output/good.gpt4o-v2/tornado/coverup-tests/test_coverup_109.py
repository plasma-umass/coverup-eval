# file: tornado/queues.py:317-320
# asked: {"lines": [317, 318, 319, 320], "branches": []}
# gained: {"lines": [317, 318, 319, 320], "branches": []}

import pytest
from tornado.queues import Queue
from tornado.locks import Event

class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue()

    def test_put_internal(self, queue: Queue):
        # Setup
        item = "test_item"
        queue._unfinished_tasks = 0
        queue._finished = Event()
        queue._finished.set()
        queue._put = lambda x: None  # Mock the _put method

        # Call the method
        queue._Queue__put_internal(item)

        # Assertions
        assert queue._unfinished_tasks == 1
        assert not queue._finished.is_set()

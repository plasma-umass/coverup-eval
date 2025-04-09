# file: tornado/queues.py:317-320
# asked: {"lines": [317, 318, 319, 320], "branches": []}
# gained: {"lines": [317, 318, 319, 320], "branches": []}

import pytest
from tornado.queues import Queue
from tornado.locks import Event

class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue(maxsize=2)

    def test_put_internal(self, queue, mocker):
        mocker.patch.object(queue, '_put')
        queue._unfinished_tasks = 0
        queue._finished = Event()
        queue._finished.set()

        item = "test_item"
        queue._Queue__put_internal(item)

        assert queue._unfinished_tasks == 1
        assert not queue._finished.is_set()
        queue._put.assert_called_once_with(item)

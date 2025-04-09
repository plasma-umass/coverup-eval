# file: tornado/queues.py:317-320
# asked: {"lines": [317, 318, 319, 320], "branches": []}
# gained: {"lines": [317, 318, 319, 320], "branches": []}

import pytest
from tornado.queues import Queue

class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue()

    def test_put_internal(self, queue, mocker):
        mocker.patch.object(queue, '_put')
        mocker.patch.object(queue, '_finished', mocker.Mock(clear=mocker.Mock()))

        initial_unfinished_tasks = queue._unfinished_tasks
        item = "test_item"

        queue._Queue__put_internal(item)

        assert queue._unfinished_tasks == initial_unfinished_tasks + 1
        queue._finished.clear.assert_called_once()
        queue._put.assert_called_once_with(item)

# file tornado/queues.py:317-320
# lines [317, 318, 319, 320]
# branches []

import pytest
from tornado.queues import Queue

class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue()

    def test_put_internal(self, queue, mocker):
        # Mock the methods and attributes used in __put_internal
        mocker.patch.object(queue, '_put')
        mocker.patch.object(queue, '_finished', clear=mocker.Mock())
        queue._unfinished_tasks = 0

        # Call the private method __put_internal
        item = "test_item"
        queue._Queue__put_internal(item)

        # Assertions to verify postconditions
        assert queue._unfinished_tasks == 1
        queue._finished.clear.assert_called_once()
        queue._put.assert_called_once_with(item)

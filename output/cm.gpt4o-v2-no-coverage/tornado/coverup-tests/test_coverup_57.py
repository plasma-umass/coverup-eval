# file: tornado/queues.py:209-223
# asked: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future
from unittest.mock import MagicMock

class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue(maxsize=2)

    def test_put_nowait_success(self, queue):
        queue.put_nowait(1)
        assert not queue.empty()
        assert queue.qsize() == 1

    def test_put_nowait_full(self, queue):
        queue.put_nowait(1)
        queue.put_nowait(2)
        with pytest.raises(QueueFull):
            queue.put_nowait(3)

    def test_put_nowait_with_getter(self, queue, mocker):
        future = Future()
        queue._getters.append(future)
        mocker.patch.object(queue, 'empty', return_value=True)
        mocker.patch.object(queue, '_get', return_value=1)
        
        queue.put_nowait(1)
        
        assert future.done()
        assert future.result() == 1

    def test_put_nowait_with_expired(self, queue, mocker):
        mocker.patch.object(queue, '_consume_expired')
        queue.put_nowait(1)
        queue._consume_expired.assert_called_once()

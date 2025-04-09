# file: tornado/queues.py:209-223
# asked: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import pytest
from tornado.queues import Queue, QueueFull
from unittest.mock import MagicMock, patch

@pytest.fixture
def queue():
    q = Queue(maxsize=2)
    q._consume_expired = MagicMock()
    q._getters = MagicMock()
    q._getters.popleft = MagicMock()
    q._getters.__bool__ = MagicMock(return_value=False)
    q._putters = MagicMock()
    q._putters.popleft = MagicMock()
    q._putters.__bool__ = MagicMock(return_value=False)
    q._queue = MagicMock()
    q._queue.popleft = MagicMock()
    q._unfinished_tasks = 0
    q._finished = MagicMock()
    q._put = MagicMock()
    return q

def test_put_nowait_no_getters(queue):
    queue.full = MagicMock(return_value=False)
    queue.put_nowait(1)
    queue._consume_expired.assert_called_once()
    queue._put.assert_called_once_with(1)
    assert queue._unfinished_tasks == 1
    queue._finished.clear.assert_called_once()

def test_put_nowait_with_getters(queue):
    queue._getters.__bool__ = MagicMock(return_value=True)
    queue.empty = MagicMock(return_value=True)
    queue._get = MagicMock(return_value=1)
    queue.put_nowait(1)
    queue._consume_expired.assert_called_once()
    queue._getters.popleft.assert_called_once()
    queue._put.assert_called_once_with(1)
    queue._get.assert_called_once()
    assert queue._unfinished_tasks == 1
    queue._finished.clear.assert_called_once()

def test_put_nowait_queue_full(queue):
    queue.full = MagicMock(return_value=True)
    with pytest.raises(QueueFull):
        queue.put_nowait(1)
    queue._consume_expired.assert_called_once()
    queue._put.assert_not_called()

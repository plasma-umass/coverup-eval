# file: tornado/queues.py:186-207
# asked: {"lines": [186, 187, 199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [186, 187, 199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future
import datetime
from unittest import mock

@pytest.fixture
def queue():
    return Queue(maxsize=1)

def test_put_nowait(queue):
    queue.put_nowait(1)
    assert not queue.empty()
    with pytest.raises(QueueFull):
        queue.put_nowait(2)

def test_put_with_timeout(queue, mocker):
    mocker.patch.object(queue, 'put_nowait', side_effect=QueueFull)
    mocker.patch.object(queue, '_putters', new_callable=list)
    with mock.patch('tornado.queues._set_timeout') as mock_set_timeout:
        future = queue.put(1, timeout=1)
        assert len(queue._putters) == 1
        assert queue._putters[0][0] == 1
        assert isinstance(queue._putters[0][1], Future)
        mock_set_timeout.assert_called_once_with(future, 1)

def test_put_no_timeout(queue, mocker):
    mocker.patch.object(queue, 'put_nowait', side_effect=None)
    future = queue.put(1)
    assert future.done()
    assert future.result() is None

# file: tornado/queues.py:256-272
# asked: {"lines": [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future
from collections import deque

@pytest.fixture
def queue():
    return Queue(maxsize=2)

def test_get_nowait_with_putters(queue, mocker):
    # Mock the necessary methods and attributes
    mocker.patch.object(queue, '_consume_expired')
    mocker.patch.object(queue, 'full', return_value=True)
    mocker.patch.object(queue, '_put')
    mocker.patch.object(queue, '_get', return_value='item')
    queue._putters = deque([(1, Future())])

    # Test get_nowait when there are putters
    result = queue.get_nowait()
    assert result == 'item'
    queue._consume_expired.assert_called_once()
    queue.full.assert_called_once()
    queue._put.assert_called_once_with(1)
    queue._get.assert_called_once()

def test_get_nowait_with_items(queue, mocker):
    # Mock the necessary methods and attributes
    mocker.patch.object(queue, '_consume_expired')
    mocker.patch.object(queue, '_get', return_value='item')
    mocker.patch.object(queue, 'qsize', return_value=1)

    # Test get_nowait when there are items in the queue
    result = queue.get_nowait()
    assert result == 'item'
    queue._consume_expired.assert_called_once()
    queue._get.assert_called_once()
    queue.qsize.assert_called_once()

def test_get_nowait_empty(queue, mocker):
    # Mock the necessary methods and attributes
    mocker.patch.object(queue, '_consume_expired')
    mocker.patch.object(queue, 'qsize', return_value=0)

    # Test get_nowait when the queue is empty
    with pytest.raises(QueueEmpty):
        queue.get_nowait()
    queue._consume_expired.assert_called_once()
    queue.qsize.assert_called_once()

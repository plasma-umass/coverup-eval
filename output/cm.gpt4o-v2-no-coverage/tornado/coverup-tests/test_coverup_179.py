# file: tornado/queues.py:256-272
# asked: {"lines": [264, 265, 266, 267, 268, 272], "branches": [[263, 264], [269, 272]]}
# gained: {"lines": [264, 265, 266, 267, 268, 272], "branches": [[263, 264], [269, 272]]}

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future

@pytest.fixture
def queue():
    return Queue(maxsize=2)

def test_get_nowait_with_item_in_queue(queue):
    queue._put(1)
    assert queue.get_nowait() == 1

def test_get_nowait_with_putters(queue, mocker):
    future = Future()
    queue._putters.append((2, future))
    mocker.patch.object(queue, 'full', return_value=True)
    mocker.patch.object(queue, '_get', return_value=2)
    mocker.patch.object(queue, '_consume_expired')
    mocker.patch.object(queue, '_Queue__put_internal')  # Corrected the attribute name
    
    assert queue.get_nowait() == 2
    queue._Queue__put_internal.assert_called_once_with(2)
    assert future.done()

def test_get_nowait_empty_queue(queue):
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

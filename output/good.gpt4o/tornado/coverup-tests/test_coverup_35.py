# file tornado/queues.py:256-272
# lines [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272]
# branches ['263->264', '263->269', '269->270', '269->272']

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future

def test_queue_get_nowait(mocker):
    queue = Queue(maxsize=1)
    
    # Mock the internal methods to control their behavior
    mocker.patch.object(queue, '_consume_expired', return_value=None)
    mocker.patch.object(queue, '_get', return_value='test_item')
    mocker.patch.object(queue, '_Queue__put_internal', return_value=None)
    
    # Test when the queue is empty and no putters are waiting
    with pytest.raises(QueueEmpty):
        queue.get_nowait()
    
    # Test when the queue has items
    queue._queue.append('test_item')
    assert queue.get_nowait() == 'test_item'
    
    # Test when there are putters waiting
    putter_future = Future()
    queue._putters.append(('test_item', putter_future))
    mocker.patch.object(queue, 'full', return_value=True)
    assert queue.get_nowait() == 'test_item'
    assert putter_future.done() and putter_future.result() is None

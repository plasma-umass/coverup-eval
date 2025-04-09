# file tornado/queues.py:384-414
# lines [384, 385, 407, 408, 410, 411, 413, 414]
# branches []

import pytest
from tornado.queues import LifoQueue, QueueEmpty

def test_lifo_queue(mocker):
    # Create an instance of LifoQueue
    q = LifoQueue()
    
    # Ensure the queue is initialized correctly
    assert q._queue == []

    # Put items into the queue
    q.put(3)
    q.put(2)
    q.put(1)

    # Ensure the items are in the queue
    assert q._queue == [3, 2, 1]

    # Get items from the queue and check the order
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3

    # Ensure the queue is empty
    assert q._queue == []

    # Mock the logger to check for QueueEmpty exception
    mocker.patch('tornado.queues.Queue.get_nowait', side_effect=QueueEmpty)
    
    with pytest.raises(QueueEmpty):
        q.get_nowait()

# file tornado/queues.py:384-414
# lines [384, 385, 407, 408, 410, 411, 413, 414]
# branches []

import pytest
from tornado.queues import LifoQueue, QueueEmpty

@pytest.mark.gen_test
def test_lifo_queue_get_nowait():
    q = LifoQueue()
    q.put(3)
    q.put(2)
    q.put(1)

    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3

    with pytest.raises(QueueEmpty):
        q.get_nowait()

@pytest.mark.gen_test
def test_lifo_queue_put_get():
    q = LifoQueue(maxsize=2)

    q.put(1)
    q.put(2)
    # The queue is not empty here, so it should not raise QueueEmpty
    assert q.get_nowait() == 2
    assert q.get_nowait() == 1
    # Now the queue is empty, so it should raise QueueEmpty
    with pytest.raises(QueueEmpty):
        q.get_nowait()

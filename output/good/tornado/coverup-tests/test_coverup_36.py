# file tornado/queues.py:256-272
# lines [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272]
# branches ['263->264', '263->269', '269->270', '269->272']

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future

@pytest.mark.gen_test
def test_get_nowait_with_putter():
    q = Queue(maxsize=1)
    # Put an item to make the queue full
    q.put_nowait('item')
    putter = Future()
    q._putters.append(('new_item', putter))
    assert q.get_nowait() == 'item'
    assert putter.done() and putter.result() is None

@pytest.mark.gen_test
def test_get_nowait_without_putter():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    assert q.get_nowait() == 1

@pytest.mark.gen_test
def test_get_nowait_empty_queue():
    q = Queue(maxsize=1)
    with pytest.raises(QueueEmpty):
        q.get_nowait()

# file: tornado/queues.py:209-223
# asked: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [209, 214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future

@pytest.fixture
def queue():
    return Queue(maxsize=2)

def test_put_nowait_empty_queue(queue):
    queue.put_nowait(1)
    assert not queue.empty()
    assert queue.qsize() == 1

def test_put_nowait_full_queue(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    with pytest.raises(QueueFull):
        queue.put_nowait(3)

def test_put_nowait_with_getters(queue):
    future = Future()
    queue._getters.append(future)
    queue.put_nowait(1)
    assert future.done()
    assert future.result() == 1
    assert queue.empty()

def test_put_nowait_with_expired_getters(queue, mocker):
    mocker.patch.object(queue, '_consume_expired', autospec=True)
    queue.put_nowait(1)
    queue._consume_expired.assert_called_once()
    assert not queue.empty()
    assert queue.qsize() == 1

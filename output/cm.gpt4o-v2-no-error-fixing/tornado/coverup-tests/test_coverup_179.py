# file: tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import datetime

@pytest.mark.gen_test
def test_queue_get_with_item():
    queue = Queue()
    queue.put_nowait(1)
    future = queue.get()
    result = yield future
    assert result == 1

@pytest.mark.gen_test
def test_queue_get_empty():
    queue = Queue()
    future = queue.get()
    assert not future.done()
    queue.put_nowait(1)
    result = yield future
    assert result == 1

@pytest.mark.gen_test
def test_queue_get_with_timeout():
    queue = Queue()
    future = queue.get(timeout=IOLoop.current().time() + 0.1)
    with pytest.raises(gen.TimeoutError):
        yield future

@pytest.mark.gen_test
def test_queue_get_with_timedelta_timeout():
    queue = Queue()
    future = queue.get(timeout=datetime.timedelta(seconds=0.1))
    with pytest.raises(gen.TimeoutError):
        yield future

@pytest.mark.gen_test
def test_queue_get_nowait_raises_queue_empty():
    queue = Queue()
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

@pytest.mark.gen_test
def test_queue_get_adds_to_getters():
    queue = Queue()
    future = queue.get()
    assert future in queue._getters

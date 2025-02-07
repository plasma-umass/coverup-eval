# file: tornado/queues.py:186-207
# asked: {"lines": [186, 187, 199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [186, 187, 199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future
from tornado import gen
import datetime

@pytest.mark.gen_test
def test_put_nowait_success():
    q = Queue(maxsize=1)
    future = q.put(1)
    assert future.done()
    assert future.result() is None

@pytest.mark.gen_test
def test_put_nowait_queue_full():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    future = q.put(2)
    assert not future.done()
    assert len(q._putters) == 1
    assert q._putters[0][0] == 2
    assert isinstance(q._putters[0][1], Future)

@pytest.mark.gen_test
def test_put_with_timeout():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    future = q.put(2, timeout=0.1)
    yield gen.sleep(0.2)
    assert future.done()
    with pytest.raises(gen.TimeoutError):
        future.result()

@pytest.mark.gen_test
def test_put_with_timedelta_timeout():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    future = q.put(2, timeout=datetime.timedelta(seconds=0.1))
    yield gen.sleep(0.2)
    assert future.done()
    with pytest.raises(gen.TimeoutError):
        future.result()

# file: tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 254], "branches": []}

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import datetime

@pytest.mark.gen_test
def test_queue_get_with_timeout():
    q = Queue()
    timeout = datetime.timedelta(seconds=1)
    
    # Ensure the queue is empty
    assert q.qsize() == 0
    
    # Call get with a timeout
    future = q.get(timeout=timeout)
    
    # Ensure the future is not done immediately
    assert not future.done()
    
    # Wait for the timeout to expire
    yield gen.sleep(1.1)
    
    # Ensure the future is done and raised a TimeoutError
    with pytest.raises(gen.TimeoutError):
        yield future

@pytest.mark.gen_test
def test_queue_get_no_timeout():
    q = Queue()
    
    # Put an item in the queue
    q.put_nowait(1)
    
    # Call get without a timeout
    future = q.get()
    
    # Ensure the future is done immediately
    assert future.done()
    
    # Ensure the result is correct
    assert future.result() == 1

@pytest.mark.gen_test
def test_queue_get_nowait_raises():
    q = Queue()
    
    # Ensure the queue is empty
    assert q.qsize() == 0
    
    # Call get_nowait and ensure it raises QueueEmpty
    with pytest.raises(QueueEmpty):
        q.get_nowait()

@pytest.mark.gen_test
def test_queue_get_with_item():
    q = Queue()
    
    # Put an item in the queue
    q.put_nowait(1)
    
    # Call get with a timeout
    future = q.get(timeout=1)
    
    # Ensure the future is done immediately
    assert future.done()
    
    # Ensure the result is correct
    assert future.result() == 1

# file: tornado/queues.py:322-328
# asked: {"lines": [322, 324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [322, 324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import pytest
from tornado.queues import Queue
from tornado.concurrent import Future

@pytest.fixture
def queue():
    return Queue()

def test_consume_expired_putters(queue):
    # Create a future and mark it as done
    future = Future()
    future.set_result(None)
    
    # Add the future to the queue's _putters
    queue._putters.append((None, future))
    
    # Call _consume_expired and check if _putters is empty
    queue._consume_expired()
    assert len(queue._putters) == 0

def test_consume_expired_getters(queue):
    # Create a future and mark it as done
    future = Future()
    future.set_result(None)
    
    # Add the future to the queue's _getters
    queue._getters.append(future)
    
    # Call _consume_expired and check if _getters is empty
    queue._consume_expired()
    assert len(queue._getters) == 0

# file tornado/queues.py:186-207
# lines [202, 203, 204]
# branches []

import pytest
from tornado.queues import Queue, QueueFull
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import datetime

def _set_timeout(future, timeout):
    if timeout is not None:
        if isinstance(timeout, datetime.timedelta):
            timeout = timeout.total_seconds()
        IOLoop.current().call_later(timeout, lambda: future.set_exception(TimeoutError()))

@pytest.fixture
def queue():
    return Queue(maxsize=1)

def test_put_with_timeout(queue, mocker):
    # Fill the queue to trigger QueueFull
    queue.put_nowait(1)
    
    # Mock _set_timeout to ensure it gets called
    mock_set_timeout = mocker.patch('tornado.queues._set_timeout', side_effect=_set_timeout)
    
    # Attempt to put another item with a timeout
    future = queue.put(2, timeout=1)
    
    # Ensure the future is in the _putters list
    assert len(queue._putters) == 1
    assert queue._putters[0][0] == 2
    assert queue._putters[0][1] == future
    
    # Ensure _set_timeout was called
    mock_set_timeout.assert_called_once_with(future, 1)
    
    # Clean up by removing the item from the queue
    queue.get_nowait()
    queue._putters.clear()

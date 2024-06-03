# file tornado/queues.py:186-207
# lines [186, 187, 199, 200, 201, 202, 203, 204, 206, 207]
# branches []

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import datetime

@pytest.mark.asyncio
async def test_queue_put_with_timeout(mocker):
    queue = Queue(maxsize=1)
    
    # Mock the _set_timeout function to avoid actual timeout handling
    mock_set_timeout = mocker.patch('tornado.queues._set_timeout')
    
    # Fill the queue to trigger the QueueFull exception
    await queue.put(1)
    
    # Attempt to put another item with a timeout
    future = queue.put(2, timeout=1)
    
    # Ensure the future is not yet done
    assert not future.done()
    
    # Ensure the item and future are in the _putters list
    assert queue._putters == [(2, future)]
    
    # Ensure _set_timeout was called with the correct parameters
    mock_set_timeout.assert_called_once_with(future, 1)
    
    # Clean up by consuming the item
    await queue.get()
    
    # Ensure the future is now done
    assert future.done()
    assert future.result() is None

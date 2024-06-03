# file tornado/locks.py:123-143
# lines [123, 124, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 143]
# branches ['133->135', '133->143', '136->137', '136->138']

import pytest
from tornado import ioloop
from tornado.concurrent import Future
from tornado.locks import Condition
from unittest.mock import patch
import datetime

@pytest.mark.asyncio
async def test_condition_wait_with_timeout(mocker):
    condition = Condition()
    timeout = datetime.timedelta(seconds=1)
    
    # Mock the IOLoop to control the timeout behavior
    mock_io_loop = mocker.patch.object(ioloop, 'IOLoop', autospec=True)
    mock_current_io_loop = mock_io_loop.current.return_value
    mock_timeout_handle = object()
    mock_current_io_loop.add_timeout.return_value = mock_timeout_handle

    waiter = await condition.wait(timeout=timeout)
    
    # Ensure the waiter is added to the waiters list
    assert len(condition._waiters) == 1
    assert condition._waiters[0] == waiter
    
    # Simulate the timeout
    on_timeout_callback = mock_current_io_loop.add_timeout.call_args[0][1]
    on_timeout_callback()
    
    # Ensure the waiter is resolved with False after timeout
    assert waiter.done()
    assert waiter.result() is False
    
    # Ensure the timeout handle is removed
    mock_current_io_loop.remove_timeout.assert_called_once_with(mock_timeout_handle)
    
    # Clean up
    condition._waiters.clear()

# file tornado/concurrent.py:187-206
# lines [187, 203, 204, 206]
# branches ['203->204', '203->206']

import pytest
from unittest.mock import Mock
from tornado.concurrent import future_set_exception_unless_cancelled
from concurrent.futures import Future

def test_future_set_exception_unless_cancelled_not_cancelled():
    future = Future()
    exception = Exception("Test exception")
    
    future_set_exception_unless_cancelled(future, exception)
    
    assert future.exception() == exception

def test_future_set_exception_unless_cancelled_cancelled(mocker):
    future = Future()
    future.cancel()
    exception = Exception("Test exception")
    
    mock_log = mocker.patch('tornado.concurrent.app_log')
    
    future_set_exception_unless_cancelled(future, exception)
    
    assert future.cancelled()
    mock_log.error.assert_called_once_with(
        "Exception after Future was cancelled", exc_info=exception
    )


# file: tornado/concurrent.py:187-206
# asked: {"lines": [206], "branches": [[203, 206]]}
# gained: {"lines": [206], "branches": [[203, 206]]}

import pytest
from unittest.mock import Mock, patch
from tornado.concurrent import future_set_exception_unless_cancelled
from concurrent import futures

def test_future_set_exception_unless_cancelled_not_cancelled():
    future = futures.Future()
    exc = Exception("Test Exception")
    
    future_set_exception_unless_cancelled(future, exc)
    
    assert future.exception() == exc

@patch('tornado.log.app_log.error')
def test_future_set_exception_unless_cancelled_cancelled(mock_log_error):
    future = futures.Future()
    exc = Exception("Test Exception")
    
    # Cancel the future
    future.cancel()
    
    future_set_exception_unless_cancelled(future, exc)
    
    mock_log_error.assert_called_once_with('Exception after Future was cancelled', exc_info=exc)

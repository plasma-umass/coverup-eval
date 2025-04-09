# file tornado/concurrent.py:187-206
# lines [187, 203, 204, 206]
# branches ['203->204', '203->206']

import pytest
from unittest import mock
from tornado.concurrent import future_set_exception_unless_cancelled
from tornado.log import app_log
from concurrent import futures

def test_future_set_exception_unless_cancelled_not_cancelled():
    future = futures.Future()
    exc = Exception("Test Exception")
    
    future_set_exception_unless_cancelled(future, exc)
    
    assert future.exception() == exc

def test_future_set_exception_unless_cancelled_cancelled(mocker):
    future = futures.Future()
    future.cancel()
    exc = Exception("Test Exception")
    
    mock_log_error = mocker.patch.object(app_log, 'error')
    
    future_set_exception_unless_cancelled(future, exc)
    
    mock_log_error.assert_called_once_with("Exception after Future was cancelled", exc_info=exc)

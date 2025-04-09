# file: tornado/concurrent.py:187-206
# asked: {"lines": [187, 203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [187, 203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
from unittest.mock import Mock, patch
from tornado.concurrent import future_set_exception_unless_cancelled
from concurrent import futures

@pytest.fixture
def mock_future():
    return Mock(spec=futures.Future)

def test_future_set_exception_unless_cancelled_not_cancelled(mock_future):
    exc = Exception("Test exception")
    mock_future.cancelled.return_value = False

    future_set_exception_unless_cancelled(mock_future, exc)

    mock_future.set_exception.assert_called_once_with(exc)

@patch('tornado.log.app_log.error')
def test_future_set_exception_unless_cancelled_cancelled(mock_app_log_error, mock_future):
    exc = Exception("Test exception")
    mock_future.cancelled.return_value = True

    future_set_exception_unless_cancelled(mock_future, exc)

    mock_future.set_exception.assert_not_called()
    mock_app_log_error.assert_called_once_with('Exception after Future was cancelled', exc_info=exc)

# file tornado/concurrent.py:173-184
# lines [173, 183, 184]
# branches ['183->exit', '183->184']

import pytest
from unittest.mock import Mock
from tornado.concurrent import future_set_result_unless_cancelled
from concurrent.futures import Future

@pytest.fixture
def mock_future():
    future = Mock(spec=Future)
    future.cancelled.return_value = False
    return future

def test_future_set_result_unless_cancelled_not_cancelled(mock_future):
    # Test that the result is set if the future is not cancelled
    future_set_result_unless_cancelled(mock_future, "result")
    mock_future.set_result.assert_called_once_with("result")

def test_future_set_result_unless_cancelled_cancelled(mock_future):
    # Test that the result is not set if the future is cancelled
    mock_future.cancelled.return_value = True
    future_set_result_unless_cancelled(mock_future, "result")
    mock_future.set_result.assert_not_called()

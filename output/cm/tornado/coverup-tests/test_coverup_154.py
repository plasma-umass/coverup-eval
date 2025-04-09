# file tornado/concurrent.py:233-237
# lines [233, 234, 237]
# branches []

import pytest
from unittest.mock import Mock
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback():
    # Create a mock future and a mock callback
    mock_future = futures.Future()
    mock_callback = Mock()

    # Add the callback to the future
    future_add_done_callback(mock_future, mock_callback)

    # Set the result of the future to trigger the callback
    mock_future.set_result(42)

    # Assert that the callback was called with the future as its argument
    mock_callback.assert_called_once_with(mock_future)

    # Clean up is not necessary as the future and callback are local to the test function

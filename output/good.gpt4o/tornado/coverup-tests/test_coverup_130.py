# file tornado/simple_httpclient.py:44-57
# lines [44, 45, 53, 54, 56, 57]
# branches []

import pytest
from tornado.simple_httpclient import HTTPTimeoutError

def test_http_timeout_error():
    # Create an instance of HTTPTimeoutError
    error_message = "Request timed out"
    error = HTTPTimeoutError(error_message)
    
    # Assert that the error code is 599
    assert error.code == 599
    
    # Assert that the error message is correctly set
    assert error.message == error_message
    
    # Assert that the __str__ method returns the correct message
    assert str(error) == error_message

    # Test the case where message is None
    error_none_message = HTTPTimeoutError(None)
    error_none_message.message = None  # Simulate the message being None
    assert str(error_none_message) == "Timeout"

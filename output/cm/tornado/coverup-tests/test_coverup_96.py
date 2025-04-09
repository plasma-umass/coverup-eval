# file tornado/simple_httpclient.py:44-57
# lines [44, 45, 53, 54, 56, 57]
# branches []

import pytest
from tornado.simple_httpclient import HTTPTimeoutError

def test_http_timeout_error():
    message = "Test timeout error message"
    timeout_error = HTTPTimeoutError(message)

    assert str(timeout_error) == message
    assert timeout_error.code == 599
    assert timeout_error.message == message

    # Test the __str__ method with no message
    timeout_error_no_message = HTTPTimeoutError("")
    assert str(timeout_error_no_message) == "Unknown"

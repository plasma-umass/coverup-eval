# file: tornado/simple_httpclient.py:44-57
# asked: {"lines": [44, 45, 53, 54, 56, 57], "branches": []}
# gained: {"lines": [44, 45, 53, 54, 56, 57], "branches": []}

import pytest
from tornado.simple_httpclient import HTTPTimeoutError

def test_http_timeout_error_init():
    message = "Request timed out"
    error = HTTPTimeoutError(message)
    assert error.code == 599
    assert error.message == message

def test_http_timeout_error_str():
    message = "Request timed out"
    error = HTTPTimeoutError(message)
    assert str(error) == message

    error_no_message = HTTPTimeoutError("Unknown")
    assert str(error_no_message) == "Unknown"

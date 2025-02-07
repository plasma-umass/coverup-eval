# file: tornado/simple_httpclient.py:60-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from tornado.simple_httpclient import HTTPStreamClosedError

def test_http_stream_closed_error_with_message():
    error_message = "Test error message"
    error = HTTPStreamClosedError(error_message)
    assert str(error) == error_message

def test_http_stream_closed_error_without_message():
    error = HTTPStreamClosedError("Unknown")
    assert str(error) == "Unknown"

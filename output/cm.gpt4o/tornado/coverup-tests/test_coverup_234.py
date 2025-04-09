# file tornado/simple_httpclient.py:60-76
# lines [73, 76]
# branches []

import pytest
from tornado.simple_httpclient import HTTPStreamClosedError

def test_http_stream_closed_error_init():
    error_message = "Stream was closed unexpectedly"
    error = HTTPStreamClosedError(error_message)
    assert error.code == 599
    assert error.message == error_message

def test_http_stream_closed_error_str():
    error_message = "Stream was closed unexpectedly"
    error = HTTPStreamClosedError(error_message)
    assert str(error) == error_message

    error_no_message = HTTPStreamClosedError("Unknown")
    assert str(error_no_message) == "Unknown"

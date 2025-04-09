# file: tornado/simple_httpclient.py:60-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from tornado.simple_httpclient import HTTPStreamClosedError

def test_http_stream_closed_error_init():
    error_message = "Test error message"
    error = HTTPStreamClosedError(error_message)
    assert error.code == 599
    assert error.message == error_message

def test_http_stream_closed_error_str(monkeypatch):
    error_message = "Test error message"
    error = HTTPStreamClosedError(error_message)
    assert str(error) == error_message

    # Monkeypatch the message attribute to simulate the behavior
    error_no_message = HTTPStreamClosedError("")
    monkeypatch.setattr(error_no_message, 'message', None)
    assert str(error_no_message) == "Stream closed"

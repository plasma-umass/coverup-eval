# file: tornado/simple_httpclient.py:44-57
# asked: {"lines": [44, 45, 53, 54, 56, 57], "branches": []}
# gained: {"lines": [44, 45, 53, 54, 56, 57], "branches": []}

import pytest
from tornado.simple_httpclient import HTTPTimeoutError

def test_http_timeout_error_init():
    error = HTTPTimeoutError("Request timed out")
    assert error.code == 599
    assert error.message == "Request timed out"

def test_http_timeout_error_str(monkeypatch):
    error_with_message = HTTPTimeoutError("Request timed out")
    assert str(error_with_message) == "Request timed out"

    error_without_message = HTTPTimeoutError("")
    
    # Monkeypatch the message attribute to simulate the behavior
    monkeypatch.setattr(error_without_message, 'message', None)
    assert str(error_without_message) == "Timeout"

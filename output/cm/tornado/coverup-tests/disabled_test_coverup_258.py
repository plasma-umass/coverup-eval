# file tornado/simple_httpclient.py:480-492
# lines [487, 488, 489, 490, 491]
# branches ['489->exit', '489->490']

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPTimeoutError
from tornado import httputil
from unittest.mock import Mock

class MockHTTPConnection(_HTTPConnection):
    def __init__(self):
        self.final_callback_called = False
        self.exception = None
        self.value = None
        self.tb = None
        super().__init__(None, None, None, None, None, None, None, None)

    def _handle_exception(self, typ, value, tb):
        self.final_callback_called = True
        self.exception = typ
        self.value = value
        self.tb = tb

@pytest.fixture
def mock_http_connection():
    return MockHTTPConnection()

def test_http_connection_on_timeout_with_info(mock_http_connection):
    mock_http_connection.final_callback = Mock()
    info = "connection"
    mock_http_connection._on_timeout(info)
    assert mock_http_connection.final_callback_called
    assert isinstance(mock_http_connection.value, HTTPTimeoutError)
    assert str(mock_http_connection.value) == "Timeout connection"

def test_http_connection_on_timeout_without_info(mock_http_connection):
    mock_http_connection.final_callback = Mock()
    mock_http_connection._on_timeout()
    assert mock_http_connection.final_callback_called
    assert isinstance(mock_http_connection.value, HTTPTimeoutError)
    assert str(mock_http_connection.value) == "Timeout"

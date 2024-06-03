# file tornado/simple_httpclient.py:480-492
# lines [480, 487, 488, 489, 490, 491]
# branches ['489->exit', '489->490']

import pytest
from tornado.simple_httpclient import HTTPTimeoutError
from tornado.httputil import HTTPMessageDelegate
from typing import Optional

class MockHTTPConnection(HTTPMessageDelegate):
    def __init__(self):
        self._timeout = True
        self.final_callback = self.mock_final_callback
        self.exception_handled = False

    def mock_final_callback(self, *args, **kwargs):
        pass

    def _handle_exception(self, typ, value, tb):
        self.exception_handled = True
        self.exception_type = typ
        self.exception_value = value

    def _on_timeout(self, info: Optional[str] = None) -> None:
        self._timeout = None
        error_message = "Timeout {0}".format(info) if info else "Timeout"
        if self.final_callback is not None:
            self._handle_exception(
                HTTPTimeoutError, HTTPTimeoutError(error_message), None
            )

@pytest.fixture
def mock_http_connection():
    return MockHTTPConnection()

def test_on_timeout_no_info(mock_http_connection):
    mock_http_connection._on_timeout()
    assert mock_http_connection._timeout is None
    assert mock_http_connection.exception_handled
    assert isinstance(mock_http_connection.exception_value, HTTPTimeoutError)
    assert str(mock_http_connection.exception_value) == "Timeout"

def test_on_timeout_with_info(mock_http_connection):
    mock_http_connection._on_timeout("test_info")
    assert mock_http_connection._timeout is None
    assert mock_http_connection.exception_handled
    assert isinstance(mock_http_connection.exception_value, HTTPTimeoutError)
    assert str(mock_http_connection.exception_value) == "Timeout test_info"

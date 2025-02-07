# file: tornado/simple_httpclient.py:205-220
# asked: {"lines": [205, 211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": []}
# gained: {"lines": [205, 211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import Mock

@pytest.fixture
def mock_connection_class(monkeypatch):
    mock_connection = Mock()
    monkeypatch.setattr('tornado.simple_httpclient.SimpleAsyncHTTPClient._connection_class', lambda self: mock_connection)
    return mock_connection

def test_handle_request_executes_all_lines(mock_connection_class):
    client = SimpleAsyncHTTPClient()
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()

    client._handle_request(request, release_callback, final_callback)

    mock_connection_class.assert_called_once_with(
        client,
        request,
        release_callback,
        final_callback,
        client.max_buffer_size,
        client.tcp_client,
        client.max_header_size,
        client.max_body_size
    )

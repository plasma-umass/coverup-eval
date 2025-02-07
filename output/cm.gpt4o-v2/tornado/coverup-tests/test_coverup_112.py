# file: tornado/simple_httpclient.py:535-540
# asked: {"lines": [535, 536, 537, 538, 539, 540], "branches": [[537, 0], [537, 538]]}
# gained: {"lines": [535, 536, 537, 538, 539, 540], "branches": [[537, 538]]}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import _HTTPConnection
from unittest.mock import Mock, patch

@pytest.fixture
def setup_http_connection():
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = Mock()
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=1024,
        tcp_client=tcp_client,
        max_header_size=1024,
        max_body_size=1024
    )
    return connection, final_callback, release_callback

def test_run_callback(setup_http_connection):
    connection, final_callback, release_callback = setup_http_connection
    response = HTTPResponse(
        request=connection.request,
        code=200,
        headers=None,
        buffer=None,
        effective_url="http://example.com"
    )

    with patch.object(IOLoop.current(), 'add_callback', wraps=IOLoop.current().add_callback) as mock_add_callback:
        connection._run_callback(response)
        release_callback.assert_called_once()
        mock_add_callback.assert_called_once_with(final_callback, response)
        assert connection.final_callback is None

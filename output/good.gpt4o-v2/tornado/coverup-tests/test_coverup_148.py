# file: tornado/simple_httpclient.py:494-497
# asked: {"lines": [494, 495, 496, 497], "branches": [[495, 0], [495, 496]]}
# gained: {"lines": [494, 495, 496, 497], "branches": [[495, 0], [495, 496]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from unittest.mock import Mock
from tornado.simple_httpclient import SimpleAsyncHTTPClient, _HTTPConnection

@pytest.fixture
def http_connection():
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = TCPClient()
    connection = _HTTPConnection(
        client=SimpleAsyncHTTPClient(),
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )
    yield connection
    connection.io_loop.clear_current()
    connection.io_loop.close(all_fds=True)

def test_remove_timeout(http_connection, mocker):
    mock_io_loop = mocker.patch.object(http_connection.io_loop, 'remove_timeout')
    timeout_mock = mocker.Mock()
    http_connection._timeout = timeout_mock
    
    http_connection._remove_timeout()
    
    mock_io_loop.assert_called_once_with(timeout_mock)
    assert http_connection._timeout is None

def test_remove_timeout_no_timeout(http_connection, mocker):
    mock_io_loop = mocker.patch.object(http_connection.io_loop, 'remove_timeout')
    http_connection._timeout = None
    
    http_connection._remove_timeout()
    
    mock_io_loop.assert_not_called()

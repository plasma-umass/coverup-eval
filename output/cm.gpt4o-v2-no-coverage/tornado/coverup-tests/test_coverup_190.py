# file: tornado/simple_httpclient.py:494-497
# asked: {"lines": [495, 496, 497], "branches": [[495, 0], [495, 496]]}
# gained: {"lines": [495, 496, 497], "branches": [[495, 496]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from unittest.mock import Mock
from tornado.simple_httpclient import _HTTPConnection

@pytest.fixture
def http_connection(mocker):
    client = None
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 104857600
    tcp_client = TCPClient()
    max_header_size = 104857600
    max_body_size = 104857600
    mock_io_loop = mocker.patch.object(IOLoop, 'current', return_value=Mock())
    return _HTTPConnection(client, request, release_callback, final_callback, max_buffer_size, tcp_client, max_header_size, max_body_size), mock_io_loop

def test_remove_timeout(http_connection):
    http_conn, mock_io_loop = http_connection
    mock_io_loop_instance = mock_io_loop.return_value
    mock_timeout = Mock()
    
    http_conn._timeout = mock_timeout
    http_conn._remove_timeout()
    
    mock_io_loop_instance.remove_timeout.assert_called_once_with(mock_timeout)
    assert http_conn._timeout is None

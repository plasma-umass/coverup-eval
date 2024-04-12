# file tornado/simple_httpclient.py:260-291
# lines [260, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 287, 288, 289, 290]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPRequest, HTTPResponse
from tornado.httpclient import HTTPError
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from unittest.mock import Mock, patch
from tornado import gen

@pytest.fixture
def mock_tcp_client():
    mock = Mock(spec=TCPClient)
    return mock

@pytest.fixture
def mock_release_callback():
    return Mock()

@pytest.fixture
def mock_final_callback():
    return Mock()

@pytest.fixture
def mock_http_request():
    return HTTPRequest(url='http://example.com')

@pytest.fixture
def mock_simple_async_http_client():
    return Mock(spec=SimpleAsyncHTTPClient)

@pytest.mark.gen_test
def test_http_connection_init_and_run(
    mock_simple_async_http_client,
    mock_http_request,
    mock_release_callback,
    mock_final_callback,
    mock_tcp_client,
):
    from tornado.simple_httpclient import _HTTPConnection

    max_buffer_size = 104857600  # 100MB
    max_header_size = 65536  # 64KB
    max_body_size = 104857600  # 100MB

    connection = _HTTPConnection(
        client=mock_simple_async_http_client,
        request=mock_http_request,
        release_callback=mock_release_callback,
        final_callback=mock_final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=mock_tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size,
    )

    assert connection.client is mock_simple_async_http_client
    assert connection.request is mock_http_request
    assert connection.release_callback is mock_release_callback
    assert connection.final_callback is mock_final_callback
    assert connection.max_buffer_size == max_buffer_size
    assert connection.tcp_client is mock_tcp_client
    assert connection.max_header_size == max_header_size
    assert connection.max_body_size == max_body_size
    assert connection.code is None
    assert connection.headers is None
    assert connection.chunks == []
    assert connection._decompressor is None
    assert connection._timeout is None
    assert connection._sockaddr is None

    # Mock the IOLoop's add_future method to prevent the actual method from running
    with patch.object(IOLoop, 'add_future') as mock_add_future:
        connection.io_loop.add_future(
            gen.convert_yielded(connection.run()), lambda f: f.result()
        )
        mock_add_future.assert_called_once()

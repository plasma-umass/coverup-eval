# file: tornado/simple_httpclient.py:535-540
# asked: {"lines": [536, 537, 538, 539, 540], "branches": [[537, 0], [537, 538]]}
# gained: {"lines": [536, 537, 538, 539, 540], "branches": [[537, 0], [537, 538]]}

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.simple_httpclient import _HTTPConnection
from tornado.ioloop import IOLoop
from tornado.httputil import HTTPHeaders
from tornado.tcpclient import TCPClient
from unittest.mock import Mock

@pytest.fixture
def mock_ioloop(mocker):
    ioloop = mocker.patch('tornado.ioloop.IOLoop.current', return_value=Mock(spec=IOLoop))
    ioloop.return_value.add_callback = Mock()
    return ioloop

@pytest.fixture
def mock_release(mocker):
    return mocker.patch.object(_HTTPConnection, '_release')

@pytest.fixture
def mock_tcp_client(mocker):
    return mocker.Mock(spec=TCPClient)

def test_run_callback_with_final_callback(mock_ioloop, mock_release, mock_tcp_client):
    # Arrange
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=200, headers=HTTPHeaders(), buffer=None)
    final_callback = Mock()
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=Mock(),
        final_callback=final_callback,
        max_buffer_size=1024,
        tcp_client=mock_tcp_client,
        max_header_size=1024,
        max_body_size=1024
    )
    connection.io_loop = IOLoop.current()

    # Act
    connection._run_callback(response)

    # Assert
    mock_release.assert_called_once()
    connection.io_loop.add_callback.assert_called_once_with(final_callback, response)
    assert connection.final_callback is None

def test_run_callback_without_final_callback(mock_ioloop, mock_release, mock_tcp_client):
    # Arrange
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=200, headers=HTTPHeaders(), buffer=None)
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=Mock(),
        final_callback=None,
        max_buffer_size=1024,
        tcp_client=mock_tcp_client,
        max_header_size=1024,
        max_body_size=1024
    )
    connection.io_loop = IOLoop.current()

    # Act
    connection._run_callback(response)

    # Assert
    mock_release.assert_called_once()
    connection.io_loop.add_callback.assert_not_called()

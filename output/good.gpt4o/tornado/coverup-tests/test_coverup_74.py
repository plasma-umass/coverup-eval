# file tornado/netutil.py:594-617
# lines [594, 597, 608, 609, 615, 617]
# branches ['609->615', '609->617']

import socket
import ssl
import pytest
from unittest import mock
from tornado.netutil import ssl_wrap_socket, ssl_options_to_context

@pytest.fixture
def mock_socket():
    sock = mock.Mock(spec=socket.socket)
    yield sock
    sock.close()

@pytest.fixture
def mock_ssl_context():
    context = mock.Mock(spec=ssl.SSLContext)
    yield context

@pytest.fixture
def mock_ssl_options_to_context(mocker, mock_ssl_context):
    return mocker.patch('tornado.netutil.ssl_options_to_context', return_value=mock_ssl_context)

def test_ssl_wrap_socket_with_sni(mock_socket, mock_ssl_options_to_context, mock_ssl_context):
    mock_ssl_context.wrap_socket.return_value = mock.Mock(spec=ssl.SSLSocket)
    ssl_options = {'certfile': 'path/to/certfile', 'keyfile': 'path/to/keyfile'}
    server_hostname = 'example.com'

    with mock.patch('ssl.HAS_SNI', True):
        wrapped_socket = ssl_wrap_socket(mock_socket, ssl_options, server_hostname=server_hostname)

    mock_ssl_options_to_context.assert_called_once_with(ssl_options)
    mock_ssl_context.wrap_socket.assert_called_once_with(mock_socket, server_hostname=server_hostname)
    assert isinstance(wrapped_socket, ssl.SSLSocket)

def test_ssl_wrap_socket_without_sni(mock_socket, mock_ssl_options_to_context, mock_ssl_context):
    mock_ssl_context.wrap_socket.return_value = mock.Mock(spec=ssl.SSLSocket)
    ssl_options = {'certfile': 'path/to/certfile', 'keyfile': 'path/to/keyfile'}

    with mock.patch('ssl.HAS_SNI', False):
        wrapped_socket = ssl_wrap_socket(mock_socket, ssl_options)

    mock_ssl_options_to_context.assert_called_once_with(ssl_options)
    mock_ssl_context.wrap_socket.assert_called_once_with(mock_socket)
    assert isinstance(wrapped_socket, ssl.SSLSocket)

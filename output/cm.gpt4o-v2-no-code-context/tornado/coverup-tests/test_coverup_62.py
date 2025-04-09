# file: tornado/netutil.py:594-617
# asked: {"lines": [594, 597, 608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}
# gained: {"lines": [594, 597, 608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}

import socket
import ssl
import pytest
from tornado.netutil import ssl_wrap_socket, ssl_options_to_context

@pytest.fixture
def mock_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    yield s
    s.close()

@pytest.fixture
def mock_ssl_context(mocker):
    context = mocker.Mock(spec=ssl.SSLContext)
    context.wrap_socket = mocker.Mock(return_value=mocker.Mock(spec=ssl.SSLSocket))
    return context

@pytest.fixture
def mock_ssl_options_to_context(mocker, mock_ssl_context):
    return mocker.patch('tornado.netutil.ssl_options_to_context', return_value=mock_ssl_context)

def test_ssl_wrap_socket_with_sni(mock_socket, mock_ssl_options_to_context):
    ssl_options = {'certfile': 'path/to/certfile', 'keyfile': 'path/to/keyfile'}
    server_hostname = 'example.com'
    
    wrapped_socket = ssl_wrap_socket(mock_socket, ssl_options, server_hostname=server_hostname)
    
    mock_ssl_options_to_context.assert_called_once_with(ssl_options)
    mock_ssl_options_to_context.return_value.wrap_socket.assert_called_once_with(
        mock_socket, server_hostname=server_hostname
    )
    assert isinstance(wrapped_socket, ssl.SSLSocket)

def test_ssl_wrap_socket_without_sni(mock_socket, mock_ssl_options_to_context, mocker):
    ssl_options = {'certfile': 'path/to/certfile', 'keyfile': 'pathfile'}
    
    mocker.patch('ssl.HAS_SNI', False)
    
    wrapped_socket = ssl_wrap_socket(mock_socket, ssl_options)
    
    mock_ssl_options_to_context.assert_called_once_with(ssl_options)
    mock_ssl_options_to_context.return_value.wrap_socket.assert_called_once_with(mock_socket)
    assert isinstance(wrapped_socket, ssl.SSLSocket)

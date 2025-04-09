# file: tornado/netutil.py:594-617
# asked: {"lines": [594, 597, 608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}
# gained: {"lines": [594, 597, 608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}

import pytest
import socket
import ssl
from unittest import mock
from tornado.netutil import ssl_wrap_socket

@pytest.fixture
def mock_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    yield s
    s.close()

@pytest.fixture
def ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    return context

@pytest.fixture
def ssl_options_dict():
    return {
        'certfile': 'path/to/certfile',
        'keyfile': 'path/to/keyfile',
        'cert_reqs': ssl.CERT_REQUIRED,
        'ca_certs': 'path/to/ca_certs',
        'ciphers': 'ECDHE+AESGCM'
    }

def test_ssl_wrap_socket_with_ssl_context(mock_socket, ssl_context):
    wrapped_socket = ssl_wrap_socket(mock_socket, ssl_context)
    assert isinstance(wrapped_socket, ssl.SSLSocket)
    wrapped_socket.close()

def test_ssl_wrap_socket_with_ssl_options_dict(mock_socket, ssl_options_dict):
    with mock.patch('tornado.netutil.ssl_options_to_context', return_value=ssl.SSLContext(ssl.PROTOCOL_TLS)) as mock_ssl_options_to_context:
        wrapped_socket = ssl_wrap_socket(mock_socket, ssl_options_dict)
        mock_ssl_options_to_context.assert_called_once_with(ssl_options_dict)
        assert isinstance(wrapped_socket, ssl.SSLSocket)
        wrapped_socket.close()

def test_ssl_wrap_socket_with_server_hostname(mock_socket, ssl_context):
    wrapped_socket = ssl_wrap_socket(mock_socket, ssl_context, server_hostname='example.com')
    assert isinstance(wrapped_socket, ssl.SSLSocket)
    wrapped_socket.close()

def test_ssl_wrap_socket_without_server_hostname(mock_socket, ssl_context):
    with mock.patch('ssl.HAS_SNI', False):
        wrapped_socket = ssl_wrap_socket(mock_socket, ssl_context)
        assert isinstance(wrapped_socket, ssl.SSLSocket)
        wrapped_socket.close()

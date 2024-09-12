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

def test_ssl_wrap_socket_with_sni(mock_socket, ssl_context):
    with mock.patch('tornado.netutil.ssl_options_to_context', return_value=ssl_context):
        with mock.patch('ssl.HAS_SNI', True):
            wrapped_socket = ssl_wrap_socket(mock_socket, ssl_context, server_hostname='example.com')
            assert isinstance(wrapped_socket, ssl.SSLSocket)
            assert wrapped_socket.server_hostname == 'example.com'

def test_ssl_wrap_socket_without_sni(mock_socket, ssl_context):
    with mock.patch('tornado.netutil.ssl_options_to_context', return_value=ssl_context):
        with mock.patch('ssl.HAS_SNI', False):
            wrapped_socket = ssl_wrap_socket(mock_socket, ssl_context)
            assert isinstance(wrapped_socket, ssl.SSLSocket)
            assert wrapped_socket.server_hostname is None

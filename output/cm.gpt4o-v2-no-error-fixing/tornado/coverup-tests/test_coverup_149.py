# file: tornado/netutil.py:594-617
# asked: {"lines": [608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}
# gained: {"lines": [608, 609, 615, 617], "branches": [[609, 615], [609, 617]]}

import pytest
import socket
import ssl
from unittest import mock
from tornado.netutil import ssl_wrap_socket

def test_ssl_wrap_socket_with_sni(monkeypatch):
    mock_socket = mock.Mock(spec=socket.socket)
    mock_context = mock.Mock(spec=ssl.SSLContext)
    mock_wrap_socket = mock.Mock()
    mock_context.wrap_socket = mock_wrap_socket

    def mock_ssl_options_to_context(ssl_options):
        return mock_context

    monkeypatch.setattr('tornado.netutil.ssl_options_to_context', mock_ssl_options_to_context)
    monkeypatch.setattr('ssl.HAS_SNI', True)

    ssl_options = {'certfile': 'cert.pem', 'keyfile': 'key.pem'}
    server_hostname = 'example.com'

    result = ssl_wrap_socket(mock_socket, ssl_options, server_hostname=server_hostname)

    mock_wrap_socket.assert_called_once_with(mock_socket, server_hostname=server_hostname)
    assert result == mock_wrap_socket()

def test_ssl_wrap_socket_without_sni(monkeypatch):
    mock_socket = mock.Mock(spec=socket.socket)
    mock_context = mock.Mock(spec=ssl.SSLContext)
    mock_wrap_socket = mock.Mock()
    mock_context.wrap_socket = mock_wrap_socket

    def mock_ssl_options_to_context(ssl_options):
        return mock_context

    monkeypatch.setattr('tornado.netutil.ssl_options_to_context', mock_ssl_options_to_context)
    monkeypatch.setattr('ssl.HAS_SNI', False)

    ssl_options = {'certfile': 'cert.pem', 'keyfile': 'key.pem'}

    result = ssl_wrap_socket(mock_socket, ssl_options)

    mock_wrap_socket.assert_called_once_with(mock_socket)
    assert result == mock_wrap_socket()

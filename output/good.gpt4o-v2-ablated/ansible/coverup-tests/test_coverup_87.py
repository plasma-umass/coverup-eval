# file: lib/ansible/module_utils/urls.py:627-644
# asked: {"lines": [627, 628, 630, 631, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 644], "branches": [[639, 0], [639, 640]]}
# gained: {"lines": [627, 628, 630, 631, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 644], "branches": [[639, 640]]}

import pytest
import socket
from unittest import mock
import http.client as httplib

# Assuming the UnixHTTPConnection class is defined in ansible/module_utils/urls.py
from ansible.module_utils.urls import UnixHTTPConnection

@pytest.fixture
def mock_socket(monkeypatch):
    mock_sock = mock.Mock()
    monkeypatch.setattr(socket, 'socket', mock.Mock(return_value=mock_sock))
    return mock_sock

def test_unix_http_connection_init():
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    assert conn._unix_socket == unix_socket

def test_unix_http_connection_connect_success(mock_socket):
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    conn.timeout = 10
    conn.connect()
    mock_socket.connect.assert_called_once_with(unix_socket)
    mock_socket.settimeout.assert_called_once_with(10)

def test_unix_http_connection_connect_failure(mock_socket):
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    mock_socket.connect.side_effect = OSError('Test error')
    with pytest.raises(OSError, match='Invalid Socket File'):
        conn.connect()

def test_unix_http_connection_call():
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    conn = conn('localhost')
    assert isinstance(conn, UnixHTTPConnection)
    assert conn.host == 'localhost'

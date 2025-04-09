# file: lib/ansible/module_utils/urls.py:627-644
# asked: {"lines": [], "branches": [[639, 0]]}
# gained: {"lines": [], "branches": [[639, 0]]}

import pytest
import socket
from unittest import mock
from ansible.module_utils.urls import UnixHTTPConnection

class MockSocket:
    def __init__(self, *args, **kwargs):
        self.timeout = None

    def connect(self, unix_socket):
        pass

    def settimeout(self, timeout):
        self.timeout = timeout

@pytest.fixture
def mock_socket(monkeypatch):
    mock_socket = MockSocket()
    monkeypatch.setattr(socket, 'socket', mock.Mock(return_value=mock_socket))
    return mock_socket

def test_unix_http_connection_timeout_set(mock_socket):
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    conn.timeout = 10  # Set a custom timeout
    conn.connect()
    assert mock_socket.timeout == 10

def test_unix_http_connection_default_timeout(mock_socket):
    unix_socket = '/tmp/test.sock'
    conn = UnixHTTPConnection(unix_socket)
    conn.timeout = socket._GLOBAL_DEFAULT_TIMEOUT  # Use the default timeout
    conn.connect()
    assert mock_socket.timeout is None

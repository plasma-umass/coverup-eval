# file lib/ansible/module_utils/urls.py:627-644
# lines [627, 628, 630, 631, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 644]
# branches ['639->exit', '639->640']

import pytest
import socket
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import UnixHTTPConnection

@pytest.fixture
def mock_socket():
    with patch('socket.socket') as mock:
        yield mock

def test_unix_http_connection_success(mock_socket):
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.return_value = None

    connection = UnixHTTPConnection('/tmp/fake_socket')
    connection.timeout = socket._GLOBAL_DEFAULT_TIMEOUT  # Set the timeout attribute
    connection.connect()

    mock_socket.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    mock_socket_instance.connect.assert_called_once_with('/tmp/fake_socket')
    assert connection.sock == mock_socket_instance

def test_unix_http_connection_failure(mock_socket):
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.side_effect = OSError("Connection failed")

    connection = UnixHTTPConnection('/tmp/fake_socket')
    connection.timeout = socket._GLOBAL_DEFAULT_TIMEOUT  # Set the timeout attribute

    with pytest.raises(OSError) as excinfo:
        connection.connect()

    assert "Invalid Socket File (/tmp/fake_socket): Connection failed" in str(excinfo.value)

def test_unix_http_connection_timeout(mock_socket):
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.return_value = None
    mock_socket_instance.settimeout.return_value = None

    connection = UnixHTTPConnection('/tmp/fake_socket')
    connection.timeout = 10
    connection.connect()

    mock_socket_instance.settimeout.assert_called_once_with(10)

def test_unix_http_connection_call(mock_socket):
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.return_value = None

    connection = UnixHTTPConnection('/tmp/fake_socket')
    connection.timeout = socket._GLOBAL_DEFAULT_TIMEOUT  # Set the timeout attribute
    connection('localhost', 80)

    assert isinstance(connection, UnixHTTPConnection)

# file lib/ansible/module_utils/urls.py:608-624
# lines [623, 624]
# branches []

import pytest
from ansible.module_utils.urls import UnixHTTPSConnection
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_socket():
    with patch('socket.socket') as mock:
        yield mock

@pytest.fixture
def mock_http_connection_connect():
    with patch('http.client.HTTPConnection.connect') as mock:
        yield mock

def test_unix_https_connection_call(mock_socket, mock_http_connection_connect):
    # Create an instance of the UnixHTTPSConnection with a dummy socket path
    connection = UnixHTTPSConnection('/path/to/socket')

    # Mock the __init__ method of the HTTPSConnection to prevent actual network calls
    with patch('http.client.HTTPSConnection.__init__', return_value=None) as mock_https_init:
        # Call the __call__ method which should execute the missing lines
        result = connection('host', 443)

        # Assert that the result is the instance itself
        assert result is connection

        # Assert that the original HTTPSConnection __init__ was called with the correct args
        mock_https_init.assert_called_once_with(connection, 'host', 443)

    # Assert that the connect method was not called since we are testing __call__ only
    mock_http_connection_connect.assert_not_called()

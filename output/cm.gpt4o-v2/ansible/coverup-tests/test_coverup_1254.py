# file: lib/ansible/module_utils/urls.py:647-655
# asked: {"lines": [651, 652, 655], "branches": []}
# gained: {"lines": [651, 652, 655], "branches": []}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
from ansible.module_utils.urls import UnixHTTPHandler
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_unix_http_connection():
    with patch('ansible.module_utils.urls.UnixHTTPConnection') as mock:
        yield mock

def test_unix_http_handler_init():
    unix_socket = '/var/run/socket'
    handler = UnixHTTPHandler(unix_socket)
    assert handler._unix_socket == unix_socket

def test_unix_http_handler_http_open(mock_unix_http_connection):
    unix_socket = '/var/run/socket'
    handler = UnixHTTPHandler(unix_socket)
    req = MagicMock()
    
    mock_conn_instance = mock_unix_http_connection.return_value
    mock_conn_instance.getresponse.return_value = MagicMock()
    
    with patch.object(handler, 'do_open', return_value=MagicMock()) as mock_do_open:
        handler.http_open(req)
    
    mock_unix_http_connection.assert_called_once_with(unix_socket)
    mock_do_open.assert_called_once_with(mock_unix_http_connection.return_value, req)

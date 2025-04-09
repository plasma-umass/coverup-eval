# file: lib/ansible/module_utils/urls.py:647-655
# asked: {"lines": [651, 652, 655], "branches": []}
# gained: {"lines": [651, 652, 655], "branches": []}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
from ansible.module_utils.urls import UnixHTTPHandler
from unittest.mock import patch, MagicMock

class MockUnixHTTPConnection:
    def __init__(self, unix_socket):
        self.unix_socket = unix_socket

    def request(self, method, url, body=None, headers={}):
        pass

    def getresponse(self):
        return MagicMock()

@pytest.fixture
def mock_unix_http_connection(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.urls.UnixHTTPConnection", MockUnixHTTPConnection)

def test_unix_http_handler_init():
    unix_socket = "/var/run/socket"
    handler = UnixHTTPHandler(unix_socket)
    assert handler._unix_socket == unix_socket

def test_unix_http_handler_http_open(mock_unix_http_connection):
    unix_socket = "/var/run/socket"
    handler = UnixHTTPHandler(unix_socket)
    req = urllib_request.Request("http+unix://%2Fvar%2Frun%2Fsocket/info")
    
    with patch.object(handler, 'do_open', return_value="response") as mock_do_open:
        response = handler.http_open(req)
        assert mock_do_open.call_count == 1
        called_args, called_kwargs = mock_do_open.call_args
        assert isinstance(called_args[0], MockUnixHTTPConnection)
        assert called_args[0].unix_socket == unix_socket
        assert called_args[1] == req
        assert response == "response"

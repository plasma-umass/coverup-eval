# file: lib/ansible/module_utils/urls.py:568-595
# asked: {"lines": [591, 592], "branches": []}
# gained: {"lines": [591, 592], "branches": []}

import pytest
from unittest import mock
from ansible.module_utils.urls import HTTPSClientAuthHandler
import urllib.request as urllib_request
import http.client as httplib

class MockUnixHTTPSConnection:
    def __init__(self, unix_socket):
        self.unix_socket = unix_socket

    def __call__(self, host, **kwargs):
        return httplib.HTTPSConnection(host, **kwargs)

@pytest.fixture
def mock_unix_https_connection(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.UnixHTTPSConnection', MockUnixHTTPSConnection)

def test_https_client_auth_handler_no_context(mock_unix_https_connection):
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key', unix_socket='/tmp/socket')
    if hasattr(handler, '_context'):
        del handler._context  # Ensure _context attribute does not exist
    req = urllib_request.Request('https://example.com')
    req.timeout = 10  # Set a timeout attribute to avoid AttributeError
    
    with mock.patch.object(httplib, 'HTTPSConnection', return_value=mock.Mock()) as mock_https_conn:
        handler.https_open(req)
        mock_https_conn.assert_called_once_with('example.com', cert_file='cert', key_file='key', timeout=10)

def test_https_client_auth_handler_with_context(mock_unix_https_connection):
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key', unix_socket='/tmp/socket')
    handler._context = mock.Mock()  # Ensure _context attribute exists
    req = urllib_request.Request('https://example.com')
    req.timeout = 10  # Set a timeout attribute to avoid AttributeError
    
    with mock.patch.object(httplib, 'HTTPSConnection', return_value=mock.Mock()) as mock_https_conn:
        handler.https_open(req)
        mock_https_conn.assert_called_once_with('example.com', cert_file='cert', key_file='key', context=handler._context, timeout=10)

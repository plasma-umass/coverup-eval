# file: lib/ansible/module_utils/urls.py:568-595
# asked: {"lines": [576, 577, 578, 579, 582, 585, 586, 587, 589, 590, 591, 592, 593, 594, 595], "branches": [[593, 594], [593, 595]]}
# gained: {"lines": [576, 577, 578, 579, 582, 585, 586, 587, 589, 590, 593, 594, 595], "branches": [[593, 594], [593, 595]]}

import pytest
import urllib.request as urllib_request
from unittest import mock
from ansible.module_utils.urls import HTTPSClientAuthHandler

@pytest.fixture
def mock_https_connection(monkeypatch):
    mock_conn = mock.Mock()
    monkeypatch.setattr('ansible.module_utils.urls.httplib.HTTPSConnection', mock_conn)
    return mock_conn

@pytest.fixture
def mock_unix_https_connection(monkeypatch):
    mock_conn = mock.Mock()
    monkeypatch.setattr('ansible.module_utils.urls.UnixHTTPSConnection', mock_conn)
    return mock_conn

def test_https_client_auth_handler_init():
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key', unix_socket='socket')
    assert handler.client_cert == 'cert'
    assert handler.client_key == 'key'
    assert handler._unix_socket == 'socket'

def test_https_open(mock_https_connection):
    handler = HTTPSClientAuthHandler()
    req = mock.Mock()
    req.host = 'localhost'
    req.timeout = 10
    req.unredirected_hdrs = {}
    handler.do_open = mock.Mock()
    handler.https_open(req)
    handler.do_open.assert_called_once_with(handler._build_https_connection, req)

def test_build_https_connection_with_context(mock_https_connection):
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key')
    handler._context = 'context'
    handler._build_https_connection('host')
    mock_https_connection.assert_called_once_with('host', cert_file='cert', key_file='key', context='context')

def test_build_https_connection_without_context(mock_https_connection):
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key')
    handler._context = None
    handler._build_https_connection('host')
    mock_https_connection.assert_called_once_with('host', cert_file='cert', key_file='key', context=None)

def test_build_https_connection_with_unix_socket(mock_unix_https_connection):
    handler = HTTPSClientAuthHandler(client_cert='cert', client_key='key', unix_socket='socket')
    handler._build_https_connection('host')
    mock_unix_https_connection.assert_called_once_with('socket')
    mock_unix_https_connection.return_value.assert_called_once_with('host', cert_file='cert', key_file='key', context=None)

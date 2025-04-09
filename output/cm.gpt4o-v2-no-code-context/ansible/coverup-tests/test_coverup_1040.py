# file: lib/ansible/module_utils/urls.py:597-606
# asked: {"lines": [603, 604, 605, 606], "branches": []}
# gained: {"lines": [603, 604, 605, 606], "branches": []}

import pytest
from ansible.module_utils.urls import UnixHTTPConnection, unix_socket_patch_httpconnection_connect
import http.client as httplib

def test_unix_socket_patch_httpconnection_connect(monkeypatch):
    class MockUnixHTTPConnection:
        def connect(self):
            self.sock = 'mock_socket'

    original_connect = httplib.HTTPConnection.connect

    def mock_connect(self):
        self.sock = 'mock_socket'

    monkeypatch.setattr(UnixHTTPConnection, 'connect', mock_connect)

    with unix_socket_patch_httpconnection_connect():
        conn = httplib.HTTPConnection('localhost')
        conn.connect()
        assert conn.sock == 'mock_socket'

    assert httplib.HTTPConnection.connect == original_connect

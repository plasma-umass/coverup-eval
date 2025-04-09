# file lib/ansible/module_utils/urls.py:597-606
# lines [597, 598, 603, 604, 605, 606]
# branches []

import pytest
from contextlib import contextmanager
from ansible.module_utils.urls import UnixHTTPConnection
import http.client as httplib

# Define the context manager for the test
@contextmanager
def unix_socket_patch_httpconnection_connect():
    _connect = httplib.HTTPConnection.connect
    httplib.HTTPConnection.connect = UnixHTTPConnection.connect
    yield
    httplib.HTTPConnection.connect = _connect

# Test function to check if the monkey patch works correctly
def test_unix_socket_patch_httpconnection_connect():
    original_connect = httplib.HTTPConnection.connect
    with unix_socket_patch_httpconnection_connect():
        assert httplib.HTTPConnection.connect == UnixHTTPConnection.connect
    # After the context manager, the original connect method should be restored
    assert httplib.HTTPConnection.connect == original_connect

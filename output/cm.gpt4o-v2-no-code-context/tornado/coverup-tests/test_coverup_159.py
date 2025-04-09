# file: tornado/simple_httpclient.py:202-203
# asked: {"lines": [202, 203], "branches": []}
# gained: {"lines": [202, 203], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient, _HTTPConnection

@pytest.fixture
def client():
    return SimpleAsyncHTTPClient()

def test_connection_class(client):
    connection_class = client._connection_class()
    assert connection_class == _HTTPConnection

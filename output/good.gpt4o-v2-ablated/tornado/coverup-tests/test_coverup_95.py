# file: tornado/simple_httpclient.py:202-203
# asked: {"lines": [202, 203], "branches": []}
# gained: {"lines": [202, 203], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import _HTTPConnection

@pytest.fixture
def client():
    return SimpleAsyncHTTPClient()

def test_connection_class(client):
    assert client._connection_class() == _HTTPConnection

# file: tornado/simple_httpclient.py:222-224
# asked: {"lines": [222, 223, 224], "branches": []}
# gained: {"lines": [222, 223, 224], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import MagicMock

@pytest.fixture
def http_client():
    client = SimpleAsyncHTTPClient()
    client.active = {}
    client.queue = MagicMock()
    client.max_clients = 10
    client._process_queue = MagicMock()
    return client

def test_release_fetch(http_client):
    key = "test_key"
    http_client.active[key] = "test_value"
    
    http_client._release_fetch(key)
    
    assert key not in http_client.active
    http_client._process_queue.assert_called_once()

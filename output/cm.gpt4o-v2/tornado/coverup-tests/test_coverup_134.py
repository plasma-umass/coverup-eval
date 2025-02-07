# file: tornado/simple_httpclient.py:222-224
# asked: {"lines": [222, 223, 224], "branches": []}
# gained: {"lines": [222, 223, 224], "branches": []}

import pytest
from unittest.mock import MagicMock
from tornado.simple_httpclient import SimpleAsyncHTTPClient

@pytest.fixture
def http_client():
    client = SimpleAsyncHTTPClient()
    client.active = {}
    client._process_queue = MagicMock()
    return client

def test_release_fetch(http_client):
    key = object()
    http_client.active[key] = "test"
    
    http_client._release_fetch(key)
    
    assert key not in http_client.active
    http_client._process_queue.assert_called_once()

# file: tornado/simple_httpclient.py:222-224
# asked: {"lines": [222, 223, 224], "branches": []}
# gained: {"lines": [222, 223, 224], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.active = {}
    client.queue = []
    monkeypatch.setattr(client, '_process_queue', lambda: None)
    return client

def test_release_fetch(client):
    key = 'test_key'
    client.active[key] = 'test_value'
    assert key in client.active

    client._release_fetch(key)
    assert key not in client.active

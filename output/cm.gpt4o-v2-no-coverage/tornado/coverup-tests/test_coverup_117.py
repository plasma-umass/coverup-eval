# file: tornado/simple_httpclient.py:222-224
# asked: {"lines": [222, 223, 224], "branches": []}
# gained: {"lines": [222, 223, 224], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import MagicMock

@pytest.fixture
def client():
    return SimpleAsyncHTTPClient()

def test_release_fetch(client, monkeypatch):
    key = object()
    client.active = {key: "some_value"}
    
    process_queue_mock = MagicMock()
    monkeypatch.setattr(client, "_process_queue", process_queue_mock)
    
    client._release_fetch(key)
    
    assert key not in client.active
    process_queue_mock.assert_called_once()

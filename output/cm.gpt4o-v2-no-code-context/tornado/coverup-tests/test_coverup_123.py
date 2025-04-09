# file: tornado/simple_httpclient.py:222-224
# asked: {"lines": [222, 223, 224], "branches": []}
# gained: {"lines": [222, 223, 224], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop

@pytest.fixture
def http_client():
    return SimpleAsyncHTTPClient()

def test_release_fetch(http_client, monkeypatch):
    # Mock the active dictionary and _process_queue method
    active_mock = {}
    key = object()
    active_mock[key] = "some_value"
    monkeypatch.setattr(http_client, 'active', active_mock)
    
    process_queue_called = False
    def mock_process_queue():
        nonlocal process_queue_called
        process_queue_called = True
    
    monkeypatch.setattr(http_client, '_process_queue', mock_process_queue)
    
    # Call the method
    http_client._release_fetch(key)
    
    # Assertions
    assert key not in http_client.active
    assert process_queue_called

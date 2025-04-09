# file: tornado/simple_httpclient.py:233-252
# asked: {"lines": [233, 241, 242, 244, 245, 246, 247, 248, 249, 251, 252], "branches": []}
# gained: {"lines": [233, 241, 242, 244, 245, 246, 247, 248, 249, 251, 252], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import HTTPTimeoutError
from unittest.mock import Mock

@pytest.fixture
def setup_client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.io_loop = IOLoop.current()
    client.waiting = {}
    client.queue = []
    return client

def test_on_timeout_with_info(setup_client):
    client = setup_client
    request = HTTPRequest("http://example.com")
    callback = Mock()
    key = object()
    client.waiting[key] = (request, callback, None)
    client.queue.append((key, request, callback))
    
    client._on_timeout(key, "test_info")
    
    client.io_loop.run_sync(lambda: None)  # Run the IOLoop to process the callback
    
    callback.assert_called_once()
    response = callback.call_args[0][0]
    assert response.code == 599
    assert isinstance(response.error, HTTPTimeoutError)
    assert str(response.error) == "Timeout test_info"
    assert key not in client.waiting

def test_on_timeout_without_info(setup_client):
    client = setup_client
    request = HTTPRequest("http://example.com")
    callback = Mock()
    key = object()
    client.waiting[key] = (request, callback, None)
    client.queue.append((key, request, callback))
    
    client._on_timeout(key)
    
    client.io_loop.run_sync(lambda: None)  # Run the IOLoop to process the callback
    
    callback.assert_called_once()
    response = callback.call_args[0][0]
    assert response.code == 599
    assert isinstance(response.error, HTTPTimeoutError)
    assert str(response.error) == "Timeout"
    assert key not in client.waiting

# file: tornado/simple_httpclient.py:226-231
# asked: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}
# gained: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest

@pytest.fixture
def client(monkeypatch):
    io_loop = IOLoop.current()
    client = SimpleAsyncHTTPClient()
    client.io_loop = io_loop
    monkeypatch.setattr(client, 'waiting', {})
    return client

def test_remove_timeout_with_key_in_waiting(client, mocker):
    key = object()
    request = HTTPRequest(url="http://example.com")
    callback = mocker.Mock()
    timeout_handle = mocker.Mock()
    
    client.waiting[key] = (request, callback, timeout_handle)
    mocker.patch.object(client.io_loop, 'remove_timeout')
    
    client._remove_timeout(key)
    
    client.io_loop.remove_timeout.assert_called_once_with(timeout_handle)
    assert key not in client.waiting

def test_remove_timeout_with_key_not_in_waiting(client):
    key = object()
    
    client._remove_timeout(key)
    
    assert key not in client.waiting

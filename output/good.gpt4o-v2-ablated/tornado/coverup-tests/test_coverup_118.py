# file: tornado/simple_httpclient.py:226-231
# asked: {"lines": [227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}
# gained: {"lines": [227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest

@pytest.fixture
def io_loop():
    loop = IOLoop()
    yield loop
    loop.close()

@pytest.fixture
def client(io_loop):
    client = SimpleAsyncHTTPClient(io_loop)
    yield client
    client.close()

def test_remove_timeout_with_timeout_handle(client, io_loop, mocker):
    key = object()
    request = HTTPRequest(url="http://example.com")
    callback = mocker.Mock()
    timeout_handle = io_loop.add_timeout(io_loop.time() + 1, lambda: None)
    
    client.waiting[key] = (request, callback, timeout_handle)
    
    mock_remove_timeout = mocker.patch.object(io_loop, 'remove_timeout')
    
    client._remove_timeout(key)
    
    assert key not in client.waiting
    mock_remove_timeout.assert_called_once_with(timeout_handle)

def test_remove_timeout_without_timeout_handle(client, mocker):
    key = object()
    request = HTTPRequest(url="http://example.com")
    callback = mocker.Mock()
    timeout_handle = None
    
    client.waiting[key] = (request, callback, timeout_handle)
    
    mock_remove_timeout = mocker.patch.object(client.io_loop, 'remove_timeout')
    
    client._remove_timeout(key)
    
    assert key not in client.waiting
    mock_remove_timeout.assert_not_called()

def test_remove_timeout_key_not_in_waiting(client):
    key = object()
    
    client._remove_timeout(key)
    
    assert key not in client.waiting

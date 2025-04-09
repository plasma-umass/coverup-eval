# file: tornado/simple_httpclient.py:226-231
# asked: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}
# gained: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}

import pytest
from unittest.mock import Mock
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient

@pytest.fixture
def setup_client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.io_loop = IOLoop.current()
    client.waiting = {}
    monkeypatch.setattr(client.io_loop, 'remove_timeout', Mock())
    return client

def test_remove_timeout_with_timeout_handle(setup_client):
    client = setup_client
    key = 'test_key'
    request = Mock()
    callback = Mock()
    timeout_handle = object()
    client.waiting[key] = (request, callback, timeout_handle)
    
    client._remove_timeout(key)
    
    client.io_loop.remove_timeout.assert_called_once_with(timeout_handle)
    assert key not in client.waiting

def test_remove_timeout_without_timeout_handle(setup_client):
    client = setup_client
    key = 'test_key'
    request = Mock()
    callback = Mock()
    timeout_handle = None
    client.waiting[key] = (request, callback, timeout_handle)
    
    client._remove_timeout(key)
    
    client.io_loop.remove_timeout.assert_not_called()
    assert key not in client.waiting

def test_remove_timeout_key_not_in_waiting(setup_client):
    client = setup_client
    key = 'test_key'
    
    client._remove_timeout(key)
    
    client.io_loop.remove_timeout.assert_not_called()

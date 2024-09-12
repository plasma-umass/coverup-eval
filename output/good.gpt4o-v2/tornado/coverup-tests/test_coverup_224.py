# file: tornado/httpclient.py:223-247
# asked: {"lines": [], "branches": [[239, 0]]}
# gained: {"lines": [], "branches": [[239, 0]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def async_http_client():
    client = AsyncHTTPClient(force_instance=True)
    yield client
    client.close()

def test_close_with_instance_cache(async_http_client, monkeypatch):
    io_loop = IOLoop.current()
    instance_cache = {io_loop: async_http_client}
    
    monkeypatch.setattr(AsyncHTTPClient, '_async_clients', lambda: instance_cache)
    monkeypatch.setattr(async_http_client, '_instance_cache', instance_cache)
    
    async_http_client.close()
    
    assert async_http_client._closed
    assert io_loop not in instance_cache

def test_close_with_inconsistent_cache(async_http_client, monkeypatch):
    io_loop = IOLoop.current()
    another_client = AsyncHTTPClient(force_instance=True)
    instance_cache = {io_loop: another_client}
    
    monkeypatch.setattr(AsyncHTTPClient, '_async_clients', lambda: instance_cache)
    monkeypatch.setattr(async_http_client, '_instance_cache', instance_cache)
    
    with pytest.raises(RuntimeError, match="inconsistent AsyncHTTPClient cache"):
        async_http_client.close()

def test_close_without_instance_cache(async_http_client, monkeypatch):
    monkeypatch.setattr(async_http_client, '_instance_cache', None)
    
    async_http_client.close()
    
    assert async_http_client._closed

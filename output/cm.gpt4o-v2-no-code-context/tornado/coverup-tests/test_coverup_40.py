# file: tornado/httpclient.py:198-214
# asked: {"lines": [198, 199, 200, 201, 203, 204, 205, 206, 211, 212, 213, 214], "branches": [[200, 201], [200, 203], [204, 205], [204, 206], [212, 213], [212, 214]]}
# gained: {"lines": [198, 199, 200, 201, 203, 204, 205, 206, 211, 212, 213, 214], "branches": [[200, 201], [200, 203], [204, 205], [204, 206], [212, 213], [212, 214]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def reset_async_clients(monkeypatch):
    original_async_clients = AsyncHTTPClient._async_clients
    cache = {}
    monkeypatch.setattr(AsyncHTTPClient, "_async_clients", lambda: cache)
    yield
    monkeypatch.setattr(AsyncHTTPClient, "_async_clients", original_async_clients)

def test_async_http_client_force_instance(reset_async_clients):
    io_loop = IOLoop.current()
    client = AsyncHTTPClient(force_instance=True)
    assert isinstance(client, AsyncHTTPClient)
    assert client.io_loop == io_loop

def test_async_http_client_instance_cache(reset_async_clients):
    io_loop = IOLoop.current()
    client1 = AsyncHTTPClient()
    client2 = AsyncHTTPClient()
    assert client1 is client2
    assert client1.io_loop == io_loop

def test_async_http_client_no_instance_cache(reset_async_clients):
    io_loop = IOLoop.current()
    client1 = AsyncHTTPClient(force_instance=True)
    client2 = AsyncHTTPClient(force_instance=True)
    assert client1 is not client2
    assert client1.io_loop == io_loop
    assert client2.io_loop == io_loop

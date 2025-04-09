# file: tornado/httpclient.py:191-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
import weakref

@pytest.fixture
def reset_async_clients():
    # Fixture to reset the _async_client_dict_AsyncHTTPClient attribute
    yield
    if hasattr(AsyncHTTPClient, "_async_client_dict_AsyncHTTPClient"):
        delattr(AsyncHTTPClient, "_async_client_dict_AsyncHTTPClient")

def test_async_clients_creation(reset_async_clients):
    # Ensure the weakref.WeakKeyDictionary is created
    clients = AsyncHTTPClient._async_clients()
    assert isinstance(clients, weakref.WeakKeyDictionary)

def test_async_clients_retrieval(reset_async_clients):
    # Ensure the same dictionary is retrieved on subsequent calls
    clients1 = AsyncHTTPClient._async_clients()
    clients2 = AsyncHTTPClient._async_clients()
    assert clients1 is clients2

def test_async_clients_with_ioloop(reset_async_clients, monkeypatch):
    # Ensure the dictionary works with IOLoop instances
    io_loop = IOLoop.current()
    clients = AsyncHTTPClient._async_clients()
    clients[io_loop] = "test_client"
    assert clients[io_loop] == "test_client"

# file: tornado/httpclient.py:191-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import weakref

@pytest.fixture
def reset_async_clients():
    # Ensure that the _async_clients dictionary is reset before each test
    attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
    if hasattr(AsyncHTTPClient, attr_name):
        delattr(AsyncHTTPClient, attr_name)
    yield
    # Clean up after the test
    if hasattr(AsyncHTTPClient, attr_name):
        delattr(AsyncHTTPClient, attr_name)

def test_async_clients_initialization(reset_async_clients):
    attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
    assert not hasattr(AsyncHTTPClient, attr_name)
    clients = AsyncHTTPClient._async_clients()
    assert hasattr(AsyncHTTPClient, attr_name)
    assert isinstance(clients, weakref.WeakKeyDictionary)

def test_async_clients_retrieval(reset_async_clients):
    attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
    clients_first_call = AsyncHTTPClient._async_clients()
    clients_second_call = AsyncHTTPClient._async_clients()
    assert clients_first_call is clients_second_call
    assert hasattr(AsyncHTTPClient, attr_name)
    assert isinstance(clients_first_call, weakref.WeakKeyDictionary)

# file: tornado/httpclient.py:191-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import weakref

def test_async_clients_creation():
    class TestAsyncHTTPClient(AsyncHTTPClient):
        pass

    # Ensure the attribute does not exist before calling _async_clients
    attr_name = "_async_client_dict_" + TestAsyncHTTPClient.__name__
    assert not hasattr(TestAsyncHTTPClient, attr_name)

    # Call the method to trigger the creation of the attribute
    clients = TestAsyncHTTPClient._async_clients()

    # Verify that the attribute now exists and is a WeakKeyDictionary
    assert hasattr(TestAsyncHTTPClient, attr_name)
    assert isinstance(getattr(TestAsyncHTTPClient, attr_name), weakref.WeakKeyDictionary)
    assert clients is getattr(TestAsyncHTTPClient, attr_name)

    # Clean up by deleting the attribute to avoid state pollution
    delattr(TestAsyncHTTPClient, attr_name)

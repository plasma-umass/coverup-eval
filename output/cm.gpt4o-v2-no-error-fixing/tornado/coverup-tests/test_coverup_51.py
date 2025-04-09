# file: tornado/httpclient.py:191-196
# asked: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}
# gained: {"lines": [191, 192, 193, 194, 195, 196], "branches": [[194, 195], [194, 196]]}

import pytest
import weakref
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

def test_async_clients_creation():
    class TestClient(AsyncHTTPClient):
        pass

    attr_name = "_async_client_dict_TestClient"
    
    # Ensure the attribute does not exist before calling _async_clients
    assert not hasattr(TestClient, attr_name)
    
    # Call the method to trigger the creation of the weakref.WeakKeyDictionary
    clients = TestClient._async_clients()
    
    # Verify that the attribute now exists and is a WeakKeyDictionary
    assert hasattr(TestClient, attr_name)
    assert isinstance(getattr(TestClient, attr_name), weakref.WeakKeyDictionary)
    assert clients is getattr(TestClient, attr_name)

def test_async_clients_retrieval():
    class TestClient(AsyncHTTPClient):
        pass

    attr_name = "_async_client_dict_TestClient"
    
    # Ensure the attribute does not exist before calling _async_clients
    assert not hasattr(TestClient, attr_name)
    
    # Call the method to trigger the creation of the weakref.WeakKeyDictionary
    clients_first_call = TestClient._async_clients()
    
    # Call the method again to retrieve the existing dictionary
    clients_second_call = TestClient._async_clients()
    
    # Verify that the same dictionary is returned
    assert clients_first_call is clients_second_call


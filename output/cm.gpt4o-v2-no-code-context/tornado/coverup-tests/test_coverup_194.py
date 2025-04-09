# file: tornado/httpclient.py:191-196
# asked: {"lines": [], "branches": [[194, 196]]}
# gained: {"lines": [], "branches": [[194, 196]]}

import pytest
import weakref
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

def test_async_clients_creates_dict():
    class TestAsyncHTTPClient(AsyncHTTPClient):
        pass

    attr_name = "_async_client_dict_" + TestAsyncHTTPClient.__name__
    
    # Ensure the attribute does not exist before the test
    if hasattr(TestAsyncHTTPClient, attr_name):
        delattr(TestAsyncHTTPClient, attr_name)
    
    # Call the method to trigger the creation of the dictionary
    clients = TestAsyncHTTPClient._async_clients()
    
    # Verify that the dictionary was created
    assert hasattr(TestAsyncHTTPClient, attr_name)
    assert isinstance(clients, weakref.WeakKeyDictionary)
    
    # Clean up after the test
    delattr(TestAsyncHTTPClient, attr_name)

def test_async_clients_reuses_dict():
    class TestAsyncHTTPClient(AsyncHTTPClient):
        pass

    attr_name = "_async_client_dict_" + TestAsyncHTTPClient.__name__
    
    # Ensure the attribute does not exist before the test
    if hasattr(TestAsyncHTTPClient, attr_name):
        delattr(TestAsyncHTTPClient, attr_name)
    
    # Call the method to trigger the creation of the dictionary
    clients_first_call = TestAsyncHTTPClient._async_clients()
    
    # Call the method again to ensure it reuses the existing dictionary
    clients_second_call = TestAsyncHTTPClient._async_clients()
    
    # Verify that the same dictionary is reused
    assert clients_first_call is clients_second_call
    
    # Clean up after the test
    delattr(TestAsyncHTTPClient, attr_name)

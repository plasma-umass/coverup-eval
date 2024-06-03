# file tornado/httpclient.py:191-196
# lines [191, 192, 193, 194, 195, 196]
# branches ['194->195', '194->196']

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import weakref

def test_async_http_client_async_clients(mocker):
    # Mock IOLoop to ensure it doesn't interfere with other tests
    mock_ioloop = mocker.Mock(spec=IOLoop)
    
    # Ensure the attribute does not exist before the test
    attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
    if hasattr(AsyncHTTPClient, attr_name):
        delattr(AsyncHTTPClient, attr_name)
    
    # Call the method to ensure the attribute is created
    result = AsyncHTTPClient._async_clients()
    
    # Verify the attribute is now set and is a WeakKeyDictionary
    assert hasattr(AsyncHTTPClient, attr_name)
    assert isinstance(result, weakref.WeakKeyDictionary)
    
    # Clean up by removing the attribute
    delattr(AsyncHTTPClient, attr_name)

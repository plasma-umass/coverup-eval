# file tornado/httpclient.py:314-336
# lines [314, 315, 336]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

def test_async_http_client_configure(mocker):
    # Mock the super class's configure method to ensure it is called
    mock_configure = mocker.patch.object(AsyncHTTPClient, 'configure', autospec=True)
    
    # Test configuring with a class object
    AsyncHTTPClient.configure(SimpleAsyncHTTPClient, max_clients=10)
    mock_configure.assert_called_with(SimpleAsyncHTTPClient, max_clients=10)
    
    # Test configuring with a fully-qualified class name
    AsyncHTTPClient.configure("tornado.simple_httpclient.SimpleAsyncHTTPClient", max_clients=5)
    mock_configure.assert_called_with("tornado.simple_httpclient.SimpleAsyncHTTPClient", max_clients=5)
    
    # Test configuring with None to use the default
    AsyncHTTPClient.configure(None, max_clients=20)
    mock_configure.assert_called_with(None, max_clients=20)
    
    # Clean up by resetting the configuration to the default
    AsyncHTTPClient.configure(SimpleAsyncHTTPClient)

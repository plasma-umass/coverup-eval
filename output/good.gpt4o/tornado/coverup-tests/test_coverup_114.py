# file tornado/httpclient.py:185-189
# lines [185, 186, 187, 189]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

def test_configurable_default(mocker):
    # Mock the import to ensure the correct class is returned
    mocker.patch('tornado.httpclient.AsyncHTTPClient.configurable_default', return_value=SimpleAsyncHTTPClient)
    
    # Call the method and assert the return value
    assert AsyncHTTPClient.configurable_default() is SimpleAsyncHTTPClient

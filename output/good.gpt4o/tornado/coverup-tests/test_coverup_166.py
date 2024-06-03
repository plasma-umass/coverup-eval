# file tornado/auth.py:264-270
# lines [264, 270]
# branches []

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class TestOpenIdMixin:
    def test_get_auth_http_client(self, mocker):
        mixin = OpenIdMixin()
        
        # Mock the AsyncHTTPClient to ensure it is called correctly
        mock_http_client = mocker.patch('tornado.httpclient.AsyncHTTPClient', autospec=True)
        
        # Call the method
        client = mixin.get_auth_http_client()
        
        # Assert that the returned client is the mocked instance
        assert client is mock_http_client.return_value
        
        # Assert that the AsyncHTTPClient was called to create an instance
        mock_http_client.assert_called_once()

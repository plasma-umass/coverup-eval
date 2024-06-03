# file tornado/auth.py:666-674
# lines [666, 674]
# branches []

import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

class TestOAuth2Mixin:
    def test_get_auth_http_client(self, mocker):
        # Create an instance of the OAuth2Mixin class
        mixin = OAuth2Mixin()
        
        # Mock the AsyncHTTPClient to ensure it is called
        mock_http_client = mocker.patch('tornado.httpclient.AsyncHTTPClient', autospec=True)
        
        # Call the method
        client = mixin.get_auth_http_client()
        
        # Assert that the returned client is the mocked instance
        assert client is mock_http_client.return_value
        
        # Assert that the AsyncHTTPClient was called to create the instance
        mock_http_client.assert_called_once()

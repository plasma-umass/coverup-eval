# file tornado/auth.py:532-538
# lines [532, 538]
# branches []

import pytest
from tornado import httpclient
from tornado.auth import OAuthMixin

class TestOAuthMixin:
    @pytest.fixture
    def oauth_mixin(self):
        return OAuthMixin()

    def test_get_auth_http_client(self, oauth_mixin, mocker):
        # Mock the AsyncHTTPClient to ensure it is called correctly
        mock_http_client = mocker.patch('tornado.httpclient.AsyncHTTPClient', autospec=True)
        
        # Call the method
        client = oauth_mixin.get_auth_http_client()
        
        # Assert that the returned client is the mocked instance
        assert client is mock_http_client.return_value
        
        # Assert that the AsyncHTTPClient was instantiated
        mock_http_client.assert_called_once()

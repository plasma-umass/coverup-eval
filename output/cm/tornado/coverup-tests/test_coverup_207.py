# file tornado/auth.py:532-538
# lines [532, 538]
# branches []

import pytest
from unittest.mock import MagicMock
from tornado import httpclient
from tornado.auth import OAuthMixin

class TestOAuthMixin:
    @pytest.fixture
    def oauth_mixin(self):
        return OAuthMixin()

    @pytest.fixture
    def mock_http_client(self, mocker):
        mock_client = MagicMock(spec=httpclient.AsyncHTTPClient)
        mocker.patch.object(httpclient, 'AsyncHTTPClient', return_value=mock_client)
        return mock_client

    def test_get_auth_http_client(self, oauth_mixin, mock_http_client):
        # Call the method under test
        client = oauth_mixin.get_auth_http_client()

        # Assert that the AsyncHTTPClient was instantiated and returned
        httpclient.AsyncHTTPClient.assert_called_once_with()
        assert isinstance(client, MagicMock)

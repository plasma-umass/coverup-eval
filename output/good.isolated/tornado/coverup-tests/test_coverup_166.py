# file tornado/auth.py:666-674
# lines [666, 674]
# branches []

import pytest
from unittest.mock import Mock
from tornado import httpclient
from tornado.auth import OAuth2Mixin

class TestOAuth2Mixin:
    @pytest.fixture
    def oauth2_mixin(self):
        return OAuth2Mixin()

    @pytest.fixture
    def mock_http_client(self, mocker):
        mock_client = Mock(spec=httpclient.AsyncHTTPClient)
        mocker.patch('tornado.httpclient.AsyncHTTPClient', return_value=mock_client)
        return mock_client

    def test_get_auth_http_client(self, oauth2_mixin, mock_http_client):
        # Call the method under test
        client = oauth2_mixin.get_auth_http_client()

        # Assert that the correct client is returned
        assert isinstance(client, Mock)

        # Assert that the AsyncHTTPClient constructor was called once
        httpclient.AsyncHTTPClient.assert_called_once_with()

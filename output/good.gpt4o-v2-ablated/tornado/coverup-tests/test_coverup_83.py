# file: tornado/auth.py:264-270
# asked: {"lines": [264, 270], "branches": []}
# gained: {"lines": [264, 270], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class TestOpenIdMixin:
    @pytest.fixture
    def openid_mixin(self):
        return OpenIdMixin()

    def test_get_auth_http_client(self, openid_mixin, mocker):
        mock_http_client = mocker.patch('tornado.httpclient.AsyncHTTPClient')
        client = openid_mixin.get_auth_http_client()
        assert client == mock_http_client.return_value
        mock_http_client.assert_called_once()

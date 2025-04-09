# file: tornado/auth.py:666-674
# asked: {"lines": [666, 674], "branches": []}
# gained: {"lines": [666, 674], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

class TestOAuth2Mixin:
    def test_get_auth_http_client(self):
        mixin = OAuth2Mixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

    def test_get_auth_http_client_override(self, monkeypatch):
        class CustomHTTPClient(httpclient.AsyncHTTPClient):
            pass

        class CustomOAuth2Mixin(OAuth2Mixin):
            def get_auth_http_client(self) -> CustomHTTPClient:
                return CustomHTTPClient()

        mixin = CustomOAuth2Mixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, CustomHTTPClient)

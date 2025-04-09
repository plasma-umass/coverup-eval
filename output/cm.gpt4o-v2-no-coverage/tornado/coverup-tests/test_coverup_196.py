# file: tornado/auth.py:264-270
# asked: {"lines": [270], "branches": []}
# gained: {"lines": [270], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class TestOpenIdMixin:
    def test_get_auth_http_client(self):
        mixin = OpenIdMixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

    def test_get_auth_http_client_override(self, monkeypatch):
        class CustomHTTPClient(httpclient.AsyncHTTPClient):
            pass

        class CustomOpenIdMixin(OpenIdMixin):
            def get_auth_http_client(self) -> CustomHTTPClient:
                return CustomHTTPClient()

        mixin = CustomOpenIdMixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, CustomHTTPClient)

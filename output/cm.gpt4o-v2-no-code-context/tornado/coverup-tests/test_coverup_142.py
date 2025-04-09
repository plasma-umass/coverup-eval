# file: tornado/auth.py:532-538
# asked: {"lines": [532, 538], "branches": []}
# gained: {"lines": [532, 538], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OAuthMixin

class CustomOAuthMixin(OAuthMixin):
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        return httpclient.AsyncHTTPClient()

def test_get_auth_http_client(monkeypatch):
    mixin = OAuthMixin()
    client = mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)

def test_custom_get_auth_http_client(monkeypatch):
    custom_mixin = CustomOAuthMixin()
    client = custom_mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)

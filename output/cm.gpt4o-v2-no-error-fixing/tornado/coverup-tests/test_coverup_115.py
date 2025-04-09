# file: tornado/auth.py:264-270
# asked: {"lines": [264, 270], "branches": []}
# gained: {"lines": [264, 270], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class CustomOpenIdMixin(OpenIdMixin):
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        return httpclient.AsyncHTTPClient()

def test_get_auth_http_client(monkeypatch):
    mixin = OpenIdMixin()
    client = mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)

def test_custom_get_auth_http_client(monkeypatch):
    custom_mixin = CustomOpenIdMixin()
    client = custom_mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)

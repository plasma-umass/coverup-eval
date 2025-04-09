# file: tornado/auth.py:666-674
# asked: {"lines": [666, 674], "branches": []}
# gained: {"lines": [666, 674], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

class CustomOAuth2Mixin(OAuth2Mixin):
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        return httpclient.AsyncHTTPClient()

def test_get_auth_http_client(monkeypatch):
    mixin = OAuth2Mixin()
    custom_mixin = CustomOAuth2Mixin()

    # Mock the AsyncHTTPClient to ensure it is called
    mock_client = httpclient.AsyncHTTPClient()
    monkeypatch.setattr(httpclient, 'AsyncHTTPClient', lambda: mock_client)

    # Test the default implementation
    default_client = mixin.get_auth_http_client()
    assert default_client is mock_client

    # Test the overridden implementation
    custom_client = custom_mixin.get_auth_http_client()
    assert custom_client is mock_client

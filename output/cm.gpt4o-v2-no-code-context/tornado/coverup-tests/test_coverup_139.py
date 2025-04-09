# file: tornado/auth.py:264-270
# asked: {"lines": [264, 270], "branches": []}
# gained: {"lines": [264, 270], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class CustomHttpClient(httpclient.AsyncHTTPClient):
    pass

class CustomOpenIdMixin(OpenIdMixin):
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        return CustomHttpClient()

@pytest.fixture
def openid_mixin():
    return OpenIdMixin()

@pytest.fixture
def custom_openid_mixin():
    return CustomOpenIdMixin()

def test_get_auth_http_client_default(openid_mixin):
    client = openid_mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)

def test_get_auth_http_client_custom(custom_openid_mixin):
    client = custom_openid_mixin.get_auth_http_client()
    assert isinstance(client, CustomHttpClient)

# file: tornado/auth.py:532-538
# asked: {"lines": [532, 538], "branches": []}
# gained: {"lines": [532, 538], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OAuthMixin

class TestOAuthMixin:
    def test_get_auth_http_client(self):
        mixin = OAuthMixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

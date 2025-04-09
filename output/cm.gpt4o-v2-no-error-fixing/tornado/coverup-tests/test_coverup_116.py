# file: tornado/auth.py:666-674
# asked: {"lines": [666, 674], "branches": []}
# gained: {"lines": [666, 674], "branches": []}

import pytest
from tornado.auth import OAuth2Mixin
from tornado import httpclient

class TestOAuth2Mixin:
    def test_get_auth_http_client(self):
        mixin = OAuth2Mixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

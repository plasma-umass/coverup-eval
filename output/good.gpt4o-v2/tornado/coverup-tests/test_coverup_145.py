# file: tornado/auth.py:264-270
# asked: {"lines": [264, 270], "branches": []}
# gained: {"lines": [264, 270], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

class TestOpenIdMixin:
    
    def test_get_auth_http_client(self):
        mixin = OpenIdMixin()
        client = mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

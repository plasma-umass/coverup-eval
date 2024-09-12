# file: tornado/auth.py:666-674
# asked: {"lines": [666, 674], "branches": []}
# gained: {"lines": [666, 674], "branches": []}

import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

def test_get_auth_http_client():
    mixin = OAuth2Mixin()
    client = mixin.get_auth_http_client()
    assert isinstance(client, httpclient.AsyncHTTPClient)
